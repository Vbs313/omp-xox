// pi-xox v2: git-ops — Structured Git Operation Tools
// Replaces raw `bash "git ..."` with typed parameters and structured output

import type { ExtensionAPI } from "@oh-my-pi/pi-coding-agent";
import { execSync } from "node:child_process";

// ── Git Helpers ──

function git(args: string[], cwd?: string): string {
  try {
    return execSync(`git ${args.join(" ")}`, {
      cwd: cwd ?? process.cwd(),
      encoding: "utf-8",
      maxBuffer: 10 * 1024 * 1024, // 10MB
      timeout: 15000,
    }).trim();
  } catch (e: unknown) {
    const err = e as { stderr?: string; message?: string };
    throw new Error(`git ${args[0]} failed: ${err.stderr ?? err.message ?? String(e)}`);
  }
}

function parseGitStatus(output: string) {
  const staged: string[] = [];
  const unstaged: string[] = [];
  const untracked: string[] = [];
  for (const line of output.split("\n")) {
    if (!line) continue;
    const stagedCode = line[0];
    const unstagedCode = line[1];
    const file = line.slice(3).trim();
    if (stagedCode !== " " && stagedCode !== "?") staged.push(`${stagedCode} ${file}`);
    if (unstagedCode !== " " && unstagedCode !== "?") unstaged.push(`${unstagedCode} ${file}`);
    if (stagedCode === "?" && unstagedCode === "?") untracked.push(file);
  }
  return { staged, unstaged, untracked };
}

// ── Extension Entry ──

export default function gitOps(pi: ExtensionAPI) {
  const { z } = pi.zod;

  pi.setLabel("pi-xox Git Tools");

  // ── git_diff ──
  pi.registerTool({
    name: "git_diff",
    label: "Git Diff",
    description:
      "Show git diff. Default: staged changes. Use mode to select staged, unstaged, or both.",
    parameters: z.object({
      mode: z.enum(["staged", "unstaged", "all"]).default("staged").describe(
        "staged: diff --cached, unstaged: diff, all: HEAD"
      ),
      path: z.string().optional().describe("Limit diff to a specific file or directory"),
      stat: z.boolean().default(false).describe("Show only --stat summary"),
      nameOnly: z.boolean().default(false).describe("Show only changed filenames"),
    }),
    async execute(_id, params, _onUpdate, _signal) {
      const args = ["diff"];
      if (params.mode === "staged") args.push("--cached");
      else if (params.mode === "all") args.push("HEAD");
      if (params.stat) args.push("--stat");
      if (params.nameOnly) args.push("--name-only");
      if (params.path) args.push("--", params.path);

      const output = git(args);
      return {
        content: [{ type: "text" as const, text: output || "(no changes)" }],
        details: { mode: params.mode, stat: params.stat, nameOnly: params.nameOnly },
      };
    },
  });

  // ── git_log ──
  pi.registerTool({
    name: "git_log",
    label: "Git Log",
    description: "Show commit history with optional filtering.",
    parameters: z.object({
      maxCount: z.number().default(20).describe("Max commits to show (1-100)"),
      author: z.string().optional().describe("Filter by author name or email"),
      since: z.string().optional().describe("Show commits after date (e.g., '2026-01-01', '2 weeks ago')"),
      until: z.string().optional().describe("Show commits before date"),
      path: z.string().optional().describe("Limit to commits touching this file or directory"),
      format: z.enum(["oneline", "medium", "full"]).default("oneline").describe("Output format"),
    }),
    async execute(_id, params, _onUpdate, _signal) {
      const args = ["log", `-${Math.max(1, Math.min(100, params.maxCount))}`];
      if (params.author) args.push(`--author=${params.author}`);
      if (params.since) args.push(`--since="${params.since}"`);
      if (params.until) args.push(`--until="${params.until}"`);
      if (params.format === "oneline") args.push("--oneline");
      else if (params.format === "full") args.push("--format=fuller");
      if (params.path) args.push("--", params.path);

      const output = git(args);
      return {
        content: [{ type: "text" as const, text: output || "(no commits match)" }],
        details: { count: output ? output.split("\n").length : 0 },
      };
    },
  });

  // ── git_status ──
  pi.registerTool({
    name: "git_status",
    label: "Git Status",
    description: "Show working tree status: staged, unstaged, and untracked files.",
    parameters: z.object({
      path: z.string().optional().describe("Limit to a specific path"),
    }),
    async execute(_id, params, _onUpdate, _signal) {
      const args = ["status", "--porcelain"];
      if (params.path) args.push("--", params.path);

      const output = git(args);
      const { staged, unstaged, untracked } = parseGitStatus(output);

      const lines: string[] = [];
      if (staged.length) lines.push(`## Staged (${staged.length})\n${staged.map(s => `  ${s}`).join("\n")}`);
      if (unstaged.length) lines.push(`## Unstaged (${unstaged.length})\n${unstaged.map(s => `  ${s}`).join("\n")}`);
      if (untracked.length) lines.push(`## Untracked (${untracked.length})\n${untracked.map(s => `  ${s}`).join("\n")}`);
      if (lines.length === 0) lines.push("Working tree clean.");

      return {
        content: [{ type: "text" as const, text: lines.join("\n\n") }],
        details: { staged: staged.length, unstaged: unstaged.length, untracked: untracked.length },
      };
    },
  });

  // ── git_blame ──
  pi.registerTool({
    name: "git_blame",
    label: "Git Blame",
    description: "Show line-by-line authorship for a file.",
    parameters: z.object({
      path: z.string().describe("File path to blame"),
      startLine: z.number().optional().describe("Start line (1-indexed, inclusive)"),
      endLine: z.number().optional().describe("End line (1-indexed, inclusive)"),
    }),
    async execute(_id, params, _onUpdate, _signal) {
      const args = ["blame", "--date=short"];
      if (params.startLine && params.endLine) {
        args.push(`-L${params.startLine},${params.endLine}`);
      } else if (params.startLine) {
        args.push(`-L${params.startLine},`);
      }
      args.push("--", params.path);

      const output = git(args);
      return {
        content: [{ type: "text" as const, text: output || "(no blame data)" }],
        details: { path: params.path, lines: output ? output.split("\n").length : 0 },
      };
    },
  });
}
