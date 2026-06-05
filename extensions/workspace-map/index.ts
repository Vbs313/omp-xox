// omp-xox v3.1: Workspace Map — repo structure index injected at session start
//
// Architecture:
//   before_agent_start hook → scan repo files → extract signatures → inject as custom message
//   Fires ONCE per top-level session (injected flag reset on session_start).
//
// Token budget: WORKSPACE_MAP_TOKEN_BUDGET (~2000 tokens ≈ 8000 chars)

import type { ExtensionAPI } from "@oh-my-pi/pi-coding-agent";
import { existsSync, readdirSync, readFileSync, statSync } from "fs";
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
  try {
    content = readFileSync(filepath, "utf-8").slice(0, 8192);
  } catch {
    return [];
  }
  const entries: string[] = [];
  const ext = path.extname(filepath);

  // TS/JS: function, class, interface, type, enum, const, let, var, export
  if (ext === ".ts" || ext === ".tsx" || ext === ".js" || ext === ".jsx") {
    const re = /^\s*(export\s+)?(async\s+)?(function|class|interface|type|enum|const|let|var)\s+(\w+)/gm;
    let m: RegExpExecArray | null;
    while ((m = re.exec(content)) !== null && entries.length < maxSigs) {
      entries.push(m[0].trim().replace(/\s+/g, " ").slice(0, 120));
    }
  }
  // Python: def, class
  if (ext === ".py") {
    const re = /^\s*(async\s+)?(def|class)\s+(\w+)/gm;
    let m: RegExpExecArray | null;
    while ((m = re.exec(content)) !== null && entries.length < maxSigs) {
      entries.push(m[0].trim().replace(/\s+/g, " ").slice(0, 120));
    }
  }
  // Rust: fn, struct, enum, trait, impl, mod
  if (ext === ".rs") {
    const re = /^\s*(pub\s+)?(fn|struct|enum|trait|impl|mod)\s+(\w+)/gm;
    let m: RegExpExecArray | null;
    while ((m = re.exec(content)) !== null && entries.length < maxSigs) {
      entries.push(m[0].trim().replace(/\s+/g, " ").slice(0, 120));
    }
  }
  // Go: func, type
  if (ext === ".go") {
    const re = /^\s*(func|type)\s+(\w+)/gm;
    let m: RegExpExecArray | null;
    while ((m = re.exec(content)) !== null && entries.length < maxSigs) {
      entries.push(m[0].trim().replace(/\s+/g, " ").slice(0, 120));
    }
  }
  // C/C++/H: function declarations
  if (ext === ".c" || ext === ".cpp" || ext === ".h" || ext === ".hpp") {
    const re = /^\s*\w[\w:*&<>,\s]+\s+(\w+)\s*\(/gm;
    let m: RegExpExecArray | null;
    while ((m = re.exec(content)) !== null && entries.length < maxSigs) {
      entries.push(m[0].trim().replace(/\s+/g, " ").slice(0, 120));
    }
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
      if (st.isDirectory()) {
        scan(full, depth + 1);
      } else if (st.isFile()) {
        const ext = path.extname(name);
        if (!CODE_FILE_EXTS[ext]) continue;
        fileCount++;
        const sigs = extractSignatures(full, 20);
        if (sigs.length > 0) {
          results.set(path.relative(cwd, full), sigs.slice(0, 8));
        }
      }
    }
  }

  scan(cwd, 0);
  if (results.size === 0) return "";

  // Build the Markdown index
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
    let dirChars = 0;
    for (const file of files) {
      const sigs = results.get(file) ?? [];
      if (!sigs.length) continue;
      const block = `### ${file}\n${sigs.map(s => `  - ${s}`).join("\n")}`;
      dirChars += block.length;
      lines.push(block);
    }
  }

  const full = lines.join("\n");
  const maxChars = maxFiles * 200; // rough upper bound
  return full.length > maxChars ? `${full.slice(0, maxChars)}\n... (truncated)` : full;
}

// ---- Extension Entry ----

export default function workspaceMap(pi: ExtensionAPI) {
  let injected = false;

  pi.setLabel("omp-xox Workspace Map v3.1");

  pi.on("session_start", () => { injected = false; });

  pi.on("before_agent_start", async (_event, ctx) => {
    if (injected) return;
    injected = true;

    const { config } = loadConfig(ctx.cwd, "workspace-map", DEFAULTS);
    if (!config.enabled) return;

    const map = buildMap(ctx.cwd, config.maxFiles);
    if (!map) return;

    return {
      message: {
        customType: "workspace-map",
        content: `<workspace-map>\n${map}\n</workspace-map>`,
        display: false,
        details: { generated: true, at: new Date().toISOString() },
      },
    };
  });
}
