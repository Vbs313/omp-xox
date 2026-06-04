// omp-xox v2: Knowledge Writer — Captures /compact summaries into Obsidian knowledge base
//
// Flow:
//   1. User runs /compact in TUI
//   2. OMP produces high-quality session summary
//   3. compact_output event fires with the summary
//   4. We intercept, auto-categorize, and write to Obsidian vault
//   5. User says "记录到知识库" → triggers /archive command
//
// This replaces the low-quality raw session export script.
// The /compact summary is produced by the LLM itself — it's distilled knowledge.

import type { ExtensionAPI } from "@oh-my-pi/pi-coding-agent";
import * as fs from "node:fs";
import * as path from "node:path";

// ── Obsidian Vault ──

const VAULT_ROOT = "/mnt/e/DataDB/ObsidianDB/memory";

interface KnowledgeDomain {
  path: string;
  keywords: RegExp;
  tags: string[];
}

const DOMAINS: KnowledgeDomain[] = [
  { path: "AI-Agent/架构对比", keywords: /agent|architect|multi.agent|omp|omp-xox|oh.my.open/i, tags: ["ai", "agent", "architecture"] },
  { path: "AI-Agent/工具生态", keywords: /mcp|tool|extension|plugin|skill|provider/i, tags: ["ai", "tools"] },
  { path: "AI-Agent/开发方法论", keywords: /tdd|methodology|workflow|superpowers|best.practice/i, tags: ["ai", "methodology"] },
  { path: "AI-Agent/协议与接口", keywords: /mcp|acp|protocol|interface|api.spec/i, tags: ["ai", "protocol"] },
  { path: "Hearthstone/架构设计", keywords: /hearthstone|silverfish|playfield|ipc|epoll|router/i, tags: ["hearthstone", "architecture"] },
  { path: "Hearthstone/Unity-Mono-BepInEx", keywords: /unity|mono|bepinex|il2cpp|harmony|assembly/i, tags: ["hearthstone", "unity", "modding"] },
  { path: "Hearthstone/安全与注入", keywords: /inject|dll|hook|detour|acg|exploit|bypass/i, tags: ["hearthstone", "security"] },
  { path: "Rust/FFI与跨语言", keywords: /rust|ffi|interop|unsafe|extern|cargo/i, tags: ["rust", "ffi"] },
  { path: "Python/实战", keywords: /python|pip|pandas|flask|fastapi|crawler/i, tags: ["python"] },
  { path: "系统与安全/Windows内存保护", keywords: /windows|memory|acg|dep|aslr|cfg|exploit/i, tags: ["security", "windows"] },
  { path: "系统与安全/WSL与容器", keywords: /wsl|docker|container|linux|ubuntu/i, tags: ["devops", "docker"] },
  { path: "DevOps/Git工作流", keywords: /git|branch|merge|rebase|ci.cd|pipeline/i, tags: ["devops", "git"] },
  { path: "前端/设计与CSS", keywords: /css|html|ui.ux|design|frontend|react|vue/i, tags: ["frontend"] },
  { path: "算法/基础", keywords: /algorithm|greedy|dp|sort|graph|tree|complexity/i, tags: ["algorithm"] },
];

function classifyDomain(text: string): KnowledgeDomain {
  for (const domain of DOMAINS) {
    if (domain.keywords.test(text)) return domain;
  }
  return { path: "AI-Agent/工具生态", keywords: /./, tags: ["misc"] };
}

function sanitizeFilename(text: string): string {
  return text
    .replace(/[^\w\u4e00-\u9fff\s-]/g, "")
    .replace(/\s+/g, "-")
    .slice(0, 60)
    .toLowerCase();
}

// ── Extension Entry ──

export default function knowledgeWriter(pi: ExtensionAPI) {
  let lastCompactSummary = "";
  let lastCompactTimestamp = "";
  let enabled = true;

  pi.setLabel("omp-xox Knowledge Writer");

  // ── Hook: compact_output — capture the high-quality summary ──
  pi.on("compact_output", async (event) => {
    if (!enabled) return;

    try {
      // The compact_output event contains the LLM-generated summary
      const summary = (event as Record<string, unknown>).content as string
        ?? (event as Record<string, unknown>).text as string
        ?? (event as Record<string, unknown>).summary as string
        ?? "";

      if (summary && summary.length > 50) {
        lastCompactSummary = summary;
        lastCompactTimestamp = new Date().toISOString();
      }
    } catch {
      // best-effort
    }
  });

  // ── Command: /archive — write last compact summary to knowledge base ──
  pi.registerCommand("archive", {
    description: "Write last /compact summary to Obsidian knowledge base",
    handler: async (args, ctx) => {
      if (!enabled) {
        ctx.ui.notify("Knowledge Writer is disabled.", "warning");
        return;
      }

      // Check if vault exists
      if (!fs.existsSync(VAULT_ROOT)) {
        ctx.ui.notify(`Vault not found: ${VAULT_ROOT}`, "error");
        return;
      }

      // Allow custom topic override
      const customTopic = args.trim();

      // Get the summary — either from last compact, or trigger a new one
      let summary = lastCompactSummary;
      if (!summary) {
        ctx.ui.notify("No compact summary available. Run /compact first, then /archive.", "warning");
        return;
      }

      // Classify domain
      const domain = classifyDomain(summary);
      const targetDir = path.join(VAULT_ROOT, domain.path);

      // Generate filename
      const topic = customTopic || extractTopic(summary);
      const date = new Date().toISOString().slice(0, 10);
      const filename = `${date}-${sanitizeFilename(topic)}.md`;
      const filepath = path.join(targetDir, filename);

      // Ensure directory exists
      fs.mkdirSync(targetDir, { recursive: true });

      // Write the note
      const note = [
        "---",
        `type: note`,
        `tags: [${domain.tags.join(", ")}]`,
        `difficulty: intermediate`,
        `created: ${date}`,
        `source: session-compact`,
        "---",
        "",
        `# ${topic}`,
        "",
        summary,
        "",
        "---",
        `*Auto-archived from /compact output on ${lastCompactTimestamp || date}*`,
      ].join("\n");

      fs.writeFileSync(filepath, note, "utf-8");

      // Clear the buffer
      lastCompactSummary = "";

      ctx.ui.notify(`Archived to ${domain.path}/${filename}`, "info");
    },
  });

  // ── Tool: archive_to_knowledge — LLM-callable archiving ──
  pi.registerTool({
    name: "archive_to_knowledge",
    label: "Archive to Knowledge Base",
    description:
      "Archive structured knowledge to the Obsidian vault. " +
      "Use this to persist decisions, solutions, architecture notes, or research findings. " +
      "The tool auto-categorizes based on content keywords.",
    parameters: pi.zod.object({
      topic: pi.zod.string().describe("Topic title for the note"),
      content: pi.zod.string().describe("The knowledge content to archive"),
      domain: pi.zod.string().optional().describe("Override domain: AI-Agent, Hearthstone, Rust, Python, etc."),
      tags: pi.zod.array(pi.zod.string()).optional().describe("Additional tags"),
    }),
    async execute(_id, params, _onUpdate, _signal, ctx) {
      if (!fs.existsSync(VAULT_ROOT)) {
        return {
          content: [{ type: "text" as const, text: `Error: vault not found at ${VAULT_ROOT}` }],
          details: { status: "error" },
        };
      }

      const domain = params.domain
        ? DOMAINS.find(d => d.path.startsWith(params.domain!)) ?? classifyDomain(params.content)
        : classifyDomain(params.content);

      const date = new Date().toISOString().slice(0, 10);
      const filename = `${date}-${sanitizeFilename(params.topic)}.md`;
      const targetDir = path.join(VAULT_ROOT, domain.path);
      const filepath = path.join(targetDir, filename);

      fs.mkdirSync(targetDir, { recursive: true });

      const allTags = [...domain.tags, ...(params.tags ?? [])];
      const note = [
        "---",
        `type: note`,
        `tags: [${allTags.join(", ")}]`,
        `difficulty: intermediate`,
        `created: ${date}`,
        "---",
        "",
        `# ${params.topic}`,
        "",
        params.content,
      ].join("\n");

      fs.writeFileSync(filepath, note, "utf-8");

      return {
        content: [{ type: "text" as const, text: `Archived: ${domain.path}/${filename}` }],
        details: { path: filepath, domain: domain.path, status: "ok" },
      };
    },
  });

  // ── Command: /knowledge — toggle or show status ──
  pi.registerCommand("knowledge", {
    description: "Show knowledge writer status or toggle",
    handler: async (args, ctx) => {
      const sub = args.trim().toLowerCase();
      if (sub === "toggle") {
        enabled = !enabled;
        ctx.ui.notify(`Knowledge Writer: ${enabled ? "ENABLED" : "DISABLED"}`, "info");
      } else {
        ctx.ui.notify(
          `Knowledge Writer: ${enabled ? "ON" : "OFF"} | ` +
          `Vault: ${VAULT_ROOT} | ` +
          `Buffer: ${lastCompactSummary ? `${lastCompactSummary.length} chars` : "empty"} | ` +
          `Domains: ${DOMAINS.length}`,
          "info"
        );
      }
    },
  });
}

// ── Helpers ──

function extractTopic(summary: string): string {
  // Try to extract a topic from the first heading or first line
  const heading = summary.match(/^#+\s*(.+)$/m);
  if (heading) return heading[1].trim().slice(0, 60);

  const firstLine = summary.split("\n").find(l => l.trim().length > 5);
  if (firstLine) return firstLine.trim().slice(0, 60);

  return "session-summary";
}
