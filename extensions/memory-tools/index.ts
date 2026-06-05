// omp-xox v3.2: Memory Tools — layered memory L0-L4 inspired by GenericAgent
//
// GenericAgent equivalent: L1 insight index, L2 global facts, L4 session archive.
// Works alongside OMP's memory.backend: local (extraction + consolidation).
//
// Tools:
//   l2_fact      — read/write global facts (environment config, known constraints)
//   distill_session — compress current session into L3/L4 archive

import type { ExtensionAPI } from "@oh-my-pi/pi-coding-agent";
import { existsSync, readFileSync, writeFileSync, mkdirSync } from "fs";
import path from "path";
import { loadConfig, envFlag } from "../shared/config-loader.ts";

export interface MemoryToolsConfig {
  enabled: boolean;
  memoryDir: string;    // where L2/L3/L4 files live
}

const DEFAULTS: MemoryToolsConfig = {
  enabled: true,
  memoryDir: "",
};

function resolveMemoryDir(cwd: string, cfg: MemoryToolsConfig): string {
  if (cfg.memoryDir) return cfg.memoryDir;
  return path.join(cwd, ".omp-xox", "memory");
}

const L2_FACT_FILE = "l2-global-facts.md";
const L4_ARCHIVE_DIR = "l4-sessions";

// ---- Extension Entry ----

export default function memoryTools(pi: ExtensionAPI) {
  const { z } = pi.zod;
  const { config } = loadConfig<MemoryToolsConfig>(
    process.cwd(), "memory-tools", DEFAULTS,
  );

  if (!envFlag("OMP_MEMORY_TOOLS", config.enabled)) {
    pi.setLabel("omp-xox Memory Tools (disabled)");
    return;
  }

  pi.setLabel("omp-xox Memory Tools v3.2");

  // ── Tool: l2_fact ──

  pi.registerTool({
    name: "l2_fact",
    label: "L2 Global Fact",
    description: "Read or write global facts — environment-specific knowledge that the LLM cannot infer: paths, credentials locations, non-standard config, known pitfalls.",
    parameters: z.object({
      action: z.enum(["read", "add", "remove"]).describe("read all facts / add a fact / remove a fact by key"),
      key: z.string().optional().describe("Fact key (e.g. 'db-host', 'api-base-url'). Required for add/remove."),
      value: z.string().optional().describe("Fact value. Required for add."),
    }),
    async execute(_id, params, _signal, _onUpdate, _ctx) {
      const cwd = process.cwd();
      const memDir = resolveMemoryDir(cwd, config);
      mkdirSync(memDir, { recursive: true });
      const factPath = path.join(memDir, L2_FACT_FILE);

      let content = existsSync(factPath) ? readFileSync(factPath, "utf-8") : "";

      if (params.action === "read") {
        if (!content.trim()) {
          return {
            content: [{ type: "text" as const, text: "L2 global facts are empty. Use `l2_fact(action=add, key=..., value=...)` to record environment-specific knowledge." }],
            details: { count: 0 },
          };
        }
        return {
          content: [{ type: "text" as const, text: content }],
          details: { length: content.length },
        };
      }

      if (params.action === "add" && params.key && params.value) {
        const section = `## ${params.key}\n${params.value}\n`;
        // Replace existing section with same key, or append
        const re = new RegExp(`^## ${params.key.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")}\\n[\\s\\S]*?(?=\\n## |$)`, "m");
        if (re.test(content)) {
          content = content.replace(re, section.trimEnd());
        } else {
          content = content.trimEnd() + (content ? "\n\n" : "") + section;
        }
        writeFileSync(factPath, content, "utf-8");
        return {
          content: [{ type: "text" as const, text: `Fact recorded: **${params.key}**` }],
          details: { key: params.key, action: "added" },
        };
      }

      if (params.action === "remove" && params.key) {
        const re = new RegExp(`^## ${params.key.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")}\\n[\\s\\S]*?(?=\\n## |$)`, "m");
        if (re.test(content)) {
          content = content.replace(re, "").replace(/\n{3,}/g, "\n\n").trim();
          writeFileSync(factPath, content, "utf-8");
          return {
            content: [{ type: "text" as const, text: `Fact removed: **${params.key}**` }],
            details: { key: params.key, action: "removed" },
          };
        }
        return {
          content: [{ type: "text" as const, text: `Fact not found: **${params.key}**` }],
          details: { key: params.key, action: "not_found" },
        };
      }

      return {
        content: [{ type: "text" as const, text: "Invalid parameters. Use action=read, action=add (key+value), or action=remove (key)." }],
        details: { status: "invalid" },
      };
    },
  });

  // ── Tool: distill_session ──

  pi.registerTool({
    name: "distill_session",
    label: "Distill Session",
    description: "Compress the current session's key learnings into L4 session archive for future recall.",
    parameters: z.object({
      summary: z.string().describe("Concise summary of what was accomplished this session"),
      learnings: z.array(z.string()).optional().describe("Key takeaways, pitfalls discovered, or patterns established"),
      tags: z.array(z.string()).optional().describe("Tags for cross-session search (e.g. ['postgres', 'migration'])"),
    }),
    async execute(_id, params, _signal, _onUpdate, _ctx) {
      const cwd = process.cwd();
      const memDir = resolveMemoryDir(cwd, config);
      const archiveDir = path.join(memDir, L4_ARCHIVE_DIR);
      mkdirSync(archiveDir, { recursive: true });

      const date = new Date().toISOString().slice(0, 19).replace(/:/g, "-");
      const filename = `session-${date}.md`;
      const filepath = path.join(archiveDir, filename);

      const tags = (params.tags ?? []).map(t => t.trim()).filter(Boolean);
      const learnings = (params.learnings ?? []).filter(Boolean);

      const note = [
        "---",
        `type: session-archive`,
        `tags: [${tags.join(", ")}]`,
        `created: ${date}`,
        `source: omp-xox memory-tools`,
        "---",
        "",
        `# Session Archive — ${date}`,
        "",
        "## Summary",
        params.summary,
        "",
        learnings.length > 0 ? `## Key Learnings\n${learnings.map(l => `- ${l}`).join("\n")}` : "",
      ].filter(Boolean).join("\n");

      writeFileSync(filepath, note, "utf-8");

      return {
        content: [{
          type: "text" as const,
          text: `✅ Session distilled to L4 archive: \`${filename}\`\n\nTags: ${tags.join(", ") || "none"}\nLearnings: ${learnings.length} recorded`,
        }],
        details: { file: filename, tags, learnings: learnings.length },
      };
    },
  });
}
