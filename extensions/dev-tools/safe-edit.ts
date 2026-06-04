// pi-xox v2: safe-edit — Hashline-style optimistic locking for file edits
// v2.1: Removed hash injection hook. Uses optional hash verification.
// Hash comes from omp's native read output header (¶PATH#TAG) or prior safe_edit return.
// No hook → no conflict with omp read cache.

import type { ExtensionAPI } from "@oh-my-pi/pi-coding-agent";
import * as fs from "node:fs";
import * as path from "node:path";
import * as crypto from "node:crypto";

// ── Content Hash ──

function contentHash(content: string): string {
  const head = content.slice(0, 256);
  const tail = content.length > 512 ? content.slice(-256) : "";
  const size = content.length.toString();
  return crypto.createHash("sha1").update(head + tail + size).digest("hex").slice(0, 4);
}

// ── Edit Operations ──

interface EditOperation {
  op: "replace" | "delete" | "insert_before" | "insert_after";
  range: [number, number];
  content?: string[];
}

function applyEdit(content: string, op: EditOperation): string {
  const lines = content.split("\n");
  const [start, end] = op.range;
  const startIdx = Math.max(0, start - 1);
  const endIdx = Math.min(lines.length, end);

  switch (op.op) {
    case "replace":
      return [...lines.slice(0, startIdx), ...(op.content ?? []), ...lines.slice(endIdx)].join("\n");
    case "delete":
      return [...lines.slice(0, startIdx), ...lines.slice(endIdx)].join("\n");
    case "insert_before":
      return [...lines.slice(0, startIdx), ...(op.content ?? []), ...lines.slice(startIdx)].join("\n");
    case "insert_after":
      return [...lines.slice(0, endIdx), ...(op.content ?? []), ...lines.slice(endIdx)].join("\n");
    default:
      return content;
  }
}

// ── Extension Entry ──

export default function safeEdit(pi: ExtensionAPI) {
  const { z } = pi.zod;

  pi.setLabel("pi-xox safe-edit");

  pi.registerTool({
    name: "safe_edit",
    label: "Safe Edit",
    description:
      "Edit a file. Hash verification is optional: if you pass a hash (from a prior read or safe_edit result), " +
      "the edit is rejected if the file has changed since that hash was generated. " +
      "Without a hash, the edit proceeds directly. " +
      "The tool always returns the new content-hash after editing — use this for subsequent safe_edit calls on the same file. " +
      "Line numbers are 1-indexed and inclusive.",
    parameters: z.object({
      path: z.string().describe("Path to the file to edit"),
      hash: z.string().optional().describe(
        "Optional 4-char content hash. If provided and file content has changed since this hash was generated, edit is rejected. " +
        "Obtain from prior safe_edit output (newHash field) or from omp read output."
      ),
      operations: z.array(
        z.object({
          op: z.enum(["replace", "delete", "insert_before", "insert_after"]),
          range: z.tuple([z.number(), z.number()]).describe("[startLine, endLine] — 1-indexed inclusive"),
          content: z.array(z.string()).optional().describe("New lines (required for replace/insert_before/insert_after)"),
        })
      ).describe("Operations to apply, in order"),
    }),
    async execute(_id, params, _onUpdate, _signal) {
      const resolved = path.resolve(params.path);

      if (!fs.existsSync(resolved)) {
        return {
          content: [{ type: "text" as const, text: `Safe edit error: file not found: ${resolved}` }],
          details: { status: "error", reason: "file_not_found" },
        };
      }

      const current = fs.readFileSync(resolved, "utf-8");
      const currentHash = contentHash(current);

      // Optional hash verification
      if (params.hash && params.hash !== currentHash) {
        return {
          content: [{
            type: "text" as const,
            text: `Safe edit REJECTED: file has changed since the hash was generated.\n` +
              `  Expected hash: ${params.hash}\n` +
              `  Current hash:  ${currentHash}\n` +
              `Re-read the file and retry with the new hash, or call safe_edit without a hash to bypass verification.`,
          }],
          details: { status: "rejected", reason: "hash_mismatch", expectedHash: params.hash, currentHash },
        };
      }

      // Apply operations
      let edited = current;
      for (const op of params.operations as EditOperation[]) {
        edited = applyEdit(edited, op);
      }
      fs.writeFileSync(resolved, edited, "utf-8");

      const newHash = contentHash(edited);
      const hashNote = params.hash
        ? `Verified hash ${params.hash} → new hash ${newHash}`
        : `No hash verification. New hash: ${newHash}`;

      return {
        content: [{ type: "text" as const, text: `Edit applied. ${hashNote}\nUse this hash for subsequent safe_edit calls: ${newHash}` }],
        details: { status: "applied", newHash, verifiedHash: params.hash ?? null },
      };
    },
  });
}
