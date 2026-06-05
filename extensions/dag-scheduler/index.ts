// omp-xox v3.2: DAG Scheduler — orchestrator-workers with agent contracts

import type { ExtensionAPI } from "@oh-my-pi/pi-coding-agent";
import * as fs from "node:fs";
import * as path from "node:path";
import { resolveCapability } from "../shared/capability-registry.ts";

interface AgentDef {
  id: string; name: string; provides: string[];
  budget: { modelRole: string; thinking: string; maxTurns: number; maxTokens: number };
  tools: string[]; verification: string[]; prompt: string;
}

function parseFrontmatter(content: string): { frontmatter: Record<string, unknown>; body: string } {
  const m = content.match(/^---\n([\s\S]*?)\n---\n([\s\S]*)$/);
  if (!m) return { frontmatter: {}, body: content };
  const fm: Record<string, unknown> = {};
  for (const line of m[1].split("\n")) {
    const kv = line.match(/^(\w[\w-]*):\s*(.*)$/);
    if (!kv) continue;
    let v: unknown = kv[2].trim();
    if (v === "true") v = true; else if (v === "false") v = false;
    else if (/^\d+$/.test(v as string)) v = parseInt(v as string, 10);
    else if ((v as string).startsWith("[") && (v as string).endsWith("]"))
      v = (v as string).slice(1, -1).split(",").map((s: string) => s.trim()).filter(Boolean);
    fm[kv[1]] = v;
  }
  return { frontmatter: fm, body: m[2].trim() };
}

function discoverAgents(dir: string): AgentDef[] {
  if (!fs.existsSync(dir)) return [];
  return fs.readdirSync(dir).filter(f => f.endsWith(".md")).map(f => {
    const c = fs.readFileSync(path.join(dir, f), "utf-8");
    const { frontmatter, body } = parseFrontmatter(c);
    return {
      id: (frontmatter.id as string) || f.replace(".md", ""),
      name: (frontmatter.name as string) || (frontmatter.id as string),
      provides: (frontmatter.provides as string[]) || [],
      budget: {
        modelRole: (frontmatter.modelRole as string) || "default",
        thinking: (frontmatter.thinking as string) || "medium",
        maxTurns: (frontmatter.maxTurns as number) || 20,
        maxTokens: (frontmatter.maxTokens as number) || 100000,
      },
      tools: (frontmatter.tools as string[]) || [],
      verification: (frontmatter.verification as string[]) || [],
      prompt: body,
    };
  });
}

function autoDetectCapability(task: string): string {
  const t = task.toLowerCase();
  if (/审查|review|check|audit|assess/.test(t)) return "review";
  if (/实现|implement|build|开发|编写/.test(t)) return "implement";
  if (/修复|fix|bug|error|缺陷/.test(t)) return "fix";
  if (/重构|refactor|重写|rewrite/.test(t)) return "refactor";
  if (/探索|explore|搜索|search|find/.test(t)) return "explore";
  if (/规划|plan|设计|design|架构/.test(t)) return "plan";
  if (/测试|test|验证|verify/.test(t)) return "verify";
  return "quick";
}

export default function dagScheduler(pi: ExtensionAPI) {
  const { z } = pi.zod;
  let agents: AgentDef[] = [];

  pi.setLabel("omp-xox DAG Scheduler v3.2");

  pi.on("session_start", async (_e, ctx) => {
    for (const dir of [
      path.join(ctx.cwd ?? ".", ".omp/agents"),
      path.join(process.env.HOME ?? "~", ".omp/agents"),
      path.join(import.meta.dir, "../../agents"),
    ]) {
      for (const a of discoverAgents(dir)) {
        if (!agents.find(e => e.id === a.id)) agents.push(a);
      }
    }
    if (agents.length) ctx.ui.notify(`omp-xox: ${agents.length} agents`, "info");
  });

  pi.registerCommand("orchestrate", {
    description: "Delegate task with auto-detected capability",
    handler: async (args, ctx) => {
      const t = args.trim();
      if (!t) { ctx.ui.notify("Usage: /orchestrate <task>", "warn"); return; }
      ctx.ui.notify(`→ ${autoDetectCapability(t)}`, "info");
      await pi.sendMessage({
        customType: "orchestrate",
        content: `Use \`delegate(task="${t}", capability="${autoDetectCapability(t)}")\`.`,
        display: true,
      }, { deliverAs: "steer" });
    },
  });

  pi.registerTool({
    name: "delegate",
    label: "Delegate",
    description: "Delegate a task to a specialized sub-agent.",
    parameters: z.object({
      task: z.string(),
      capability: z.string().optional(),
    }),
    async execute(_id, params, _signal, _onUpdate, _ctx) {
      const task = params.task;
      const capId = params.capability ?? autoDetectCapability(task);
      const cap = resolveCapability(capId);
      const agent = agents.find(a => a.id === cap.agent) ?? agents[0];
      if (!agent) return { content: [{ type: "text" as const, text: "No agent." }], details: {} };

      try {
        const prompt = `${agent.prompt}\n\nTask: ${task}`;
        const { session } = await pi.pi.createAgentSession({
          systemPrompt: () => prompt,
          settings: (pi.pi as Record<string, unknown>).Settings
            ? (pi.pi as Record<string, { isolated: (o: Record<string, unknown>) => unknown }>).Settings.isolated({ "tools.approvalMode": "yolo" })
            : undefined,
        } as Record<string, unknown>);

        let out = "";
        (session as { subscribe: (f: (e: Record<string, unknown>) => void) => void }).subscribe((e: Record<string, unknown>) => {
          const ae = e.assistantMessageEvent as Record<string, unknown> | undefined;
          if (e.type === "message_update" && ae?.type === "text_delta") out += String(ae.delta ?? "");
        });
        await (session as { prompt: (t: string) => Promise<void> }).prompt(task);
        return {
          content: [{ type: "text" as const, text: `## ${capId} → ${agent.name}\n\n${out.trim() || "(no output)"}` }],
          details: { task, capability: capId, agent: agent.name },
        };
      } catch (err) {
        return { content: [{ type: "text" as const, text: `Failed: ${String(err)}` }], details: { error: String(err) } };
      }
    },
  });

  pi.registerTool({
    name: "agent_status",
    label: "Agent Status",
    description: "List loaded agent contracts.",
    parameters: z.object({}),
    async execute() {
      if (!agents.length) return { content: [{ type: "text" as const, text: "No agents." }], details: { count: 0 } };
      return {
        content: [{ type: "text" as const, text: `## Agents (${agents.length})\n\n${agents.map(a => `- **${a.name}** (\`${a.id}\`): provides [${a.provides.join(", ")}], model=${a.budget.modelRole}, thinking=${a.budget.thinking}`).join("\n")}` }],
        details: { count: agents.length },
      };
    },
  });
}
