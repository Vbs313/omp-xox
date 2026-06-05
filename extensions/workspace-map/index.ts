// omp-xox v3.2: Workspace Map — repo structure + checkpoint + orchestration injection
//
// Architecture:
//   session_start hook → pi.sendMessage() → injects as steer message visible to LLM
//   Fires ONCE per session (injected flag).
//
// v3.2 fix: before_agent_start custom messages are stored but NOT included in the
// LLM's system prompt. Switched to pi.sendMessage() with deliverAs:"steer" which IS
// included in the conversation context.

import type { ExtensionAPI } from "@oh-my-pi/pi-coding-agent";
import { readdirSync, readFileSync, statSync } from "fs";
import path from "path";
import {
  WORKSPACE_MAP_TOKEN_BUDGET,
  WORKSPACE_MAP_MAX_FILES,
  CODE_FILE_EXTS,
  SKIP_DIRS,
} from "../shared/context-limits.ts";
import { loadConfig } from "../shared/config-loader.ts";

export interface WorkspaceMapConfig {
  enabled: boolean;
  maxFiles: number;
  tokenBudget: number;
}

const DEFAULTS: WorkspaceMapConfig = {
  enabled: true,
  maxFiles: WORKSPACE_MAP_MAX_FILES,
  tokenBudget: WORKSPACE_MAP_TOKEN_BUDGET,
};

function extractSignatures(filepath: string, maxSigs: number): string[] {
  let content: string;
  try { content = readFileSync(filepath, "utf-8").slice(0, 8192); } catch { return []; }
  const entries: string[] = [];
  const ext = path.extname(filepath);

  if (ext === ".ts" || ext === ".tsx" || ext === ".js" || ext === ".jsx") {
    const re = /^\s*(export\s+)?(async\s+)?(function|class|interface|type|enum|const|let|var)\s+(\w+)/gm;
    let m: RegExpExecArray | null;
    while ((m = re.exec(content)) !== null && entries.length < maxSigs) entries.push(m[0].trim().replace(/\s+/g, " ").slice(0, 120));
  }
  if (ext === ".py") {
    const re = /^\s*(async\s+)?(def|class)\s+(\w+)/gm;
    let m: RegExpExecArray | null;
    while ((m = re.exec(content)) !== null && entries.length < maxSigs) entries.push(m[0].trim().replace(/\s+/g, " ").slice(0, 120));
  }
  if (ext === ".rs") {
    const re = /^\s*(pub\s+)?(fn|struct|enum|trait|impl|mod)\s+(\w+)/gm;
    let m: RegExpExecArray | null;
    while ((m = re.exec(content)) !== null && entries.length < maxSigs) entries.push(m[0].trim().replace(/\s+/g, " ").slice(0, 120));
  }
  if (ext === ".go") {
    const re = /^\s*(func|type)\s+(\w+)/gm;
    let m: RegExpExecArray | null;
    while ((m = re.exec(content)) !== null && entries.length < maxSigs) entries.push(m[0].trim().replace(/\s+/g, " ").slice(0, 120));
  }
  if (ext === ".c" || ext === ".cpp" || ext === ".h" || ext === ".hpp") {
    const re = /^\s*\w[\w:*&<>,\s]+\s+(\w+)\s*\(/gm;
    let m: RegExpExecArray | null;
    while ((m = re.exec(content)) !== null && entries.length < maxSigs) entries.push(m[0].trim().replace(/\s+/g, " ").slice(0, 120));
  }
  return entries;
}

function buildMap(cwd: string, maxFiles: number): string {
  const results = new Map<string, string[]>();
  let fileCount = 0;

  function scan(dir: string, depth: number) {
    if (fileCount >= maxFiles || depth > 10) return;
    let entries: string[];
    try { entries = readdirSync(dir); } catch { return; }
    for (const name of entries) {
      if (fileCount >= maxFiles) return;
      const full = path.join(dir, name);
      if (SKIP_DIRS[name]) continue;
      if (name.startsWith(".")) continue;
      let st: ReturnType<typeof statSync>;
      try { st = statSync(full); } catch { continue; }
      if (st.isDirectory()) { scan(full, depth + 1); }
      else if (st.isFile()) {
        const ext = path.extname(name);
        if (!CODE_FILE_EXTS[ext]) continue;
        fileCount++;
        const sigs = extractSignatures(full, 20);
        if (sigs.length > 0) results.set(path.relative(cwd, full), sigs.slice(0, 8));
      }
    }
  }
  scan(cwd, 0);
  if (results.size === 0) return "";

  const lines: string[] = [`# Repository Structure (${results.size} files)`];
  const byDir = new Map<string, string[]>();
  for (const [rel, sigs] of results) {
    const topDir = rel.split(path.sep, 1)[0] ?? ".";
    const existing = byDir.get(topDir);
    if (existing) existing.push(rel);
    else byDir.set(topDir, [rel]);
  }
  for (const dir of [...byDir.keys()].sort()) {
    const files = (byDir.get(dir) ?? []).sort();
    lines.push(`\n## ${dir}/`);
    for (const file of files) {
      const sigs = results.get(file) ?? [];
      if (!sigs.length) continue;
      const block = `### ${file}\n${sigs.map(s => `  - ${s}`).join("\n")}`;
      lines.push(block);
    }
  }
  const full = lines.join("\n");
  const maxChars = maxFiles * 200;
  return full.length > maxChars ? `${full.slice(0, maxChars)}\n... (truncated)` : full;
}

function readCheckpoints(ctx: { sessionManager: { getBranch(): Array<Record<string, unknown>> } }): string {
  try {
    const items: string[] = [];
    for (const entry of ctx.sessionManager.getBranch()) {
      if (entry.type === "custom" && entry.customType === "omp-xox-checkpoint") {
        const data = (entry as Record<string, unknown>).data as Record<string, unknown> | undefined;
        if (data?.note && data?.status === "in_progress") {
          items.push(`- ${String(data.note).slice(0, 200)}`);
        }
      }
    }
    const recent = items.slice(-5);
    if (recent.length > 0) return `\n## Active Checkpoints\n${recent.join("\n")}`;
  } catch { /* session manager may not be available */ }
  return "";
}

// ---- Extension Entry ----

export default function workspaceMap(pi: ExtensionAPI) {
  let injected = false;
  pi.setLabel("omp-xox Workspace Map v3.2");

  pi.on("session_start", async (_event, ctx) => {
    if (injected) return;
    injected = true;

    const cwd = ctx.cwd ?? process.cwd();
    const { config } = loadConfig(cwd, "workspace-map", DEFAULTS);
    if (!config.enabled) return;

    const map = buildMap(cwd, config.maxFiles);
    const checkpoints = readCheckpoints(ctx as unknown as { sessionManager: { getBranch(): Array<Record<string, unknown>> } });

    // Inject orchestration hint — must reach the LLM.
    // pi.sendMessage with deliverAs:"steer" is included in the conversation context.
    // before_agent_start custom messages are NOT (they're stored but not rendered).
    await pi.sendMessage({
      customType: "workspace-map",
      content: [
        "<workspace-map>",
        map,
        checkpoints,
        "",
        "<orchestration>",
        "For task routing, prefer `delegate(task=\"...\", capability=\"...\")` over the raw `task` tool.",
        "Available capabilities: review, implement, fix, refactor, explore, plan, verify, test.",
        "Use `agent_status` to list all loaded agents and their capabilities.",
        "</orchestration>",
        "</workspace-map>",
      ].filter(Boolean).join("\n"),
      display: false,
    }, { deliverAs: "steer" });
  });
}
