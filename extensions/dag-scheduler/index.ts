// omp-xox v3.2: DAG Scheduler — orchestrator-workers with agent contracts
// Uses pi.pi.createAgentSession() for direct sub-agent spawning.

import type { ExtensionAPI } from "@oh-my-pi/pi-coding-agent";
import * as fs from "node:fs";
import * as path from "node:path";
import { resolveCapability } from "../shared/capability-registry.ts";

// ── Agent Contract Loader ──

interface AgentDef {
  id: string;
  name: string;
  provides: string[];
  mode: string;
  budget: { modelRole: string; thinking: string; maxTurns: number; maxTokens: number };
  tools: string[];
  verification: string[];
  prompt: string;
}

function parseFrontmatter(content: string): { frontmatter: Record<string, unknown>; body: string } {
  const match = content.match(/^---\n([\s\S]*?)\n---\n([\s\S]*)$/);
  if (!match) return { frontmatter: {}, body: content };
  const frontmatter: Record<string, unknown> = {};
  for (const line of match[1].split("\n")) {
    const kv = line.match(/^(\w[\w-]*):\s*(.*)$/);
    if (kv) {
      const key = kv[1];
      let value: unknown = kv[2].trim();
      if (value === "true") value = true;
      else if (value === "false") value = false;
      else if (/^\d+$/.test(value as string)) value = parseInt(value as string, 10);
      else if ((value as string).startsWith("[") && (value as string).endsWith("]")) {
        value = (value as string).slice(1, -1).split(",").map((s: string) => s.trim()).filter(Boolean);
      }
      frontmatter[key] = value;
    }
  }
  return { frontmatter, body: match[2].trim() };
}

function discoverAgents(agentsDir: string): AgentDef[] {
  if (!fs.existsSync(agentsDir)) return [];
  return fs.readdirSync(agentsDir)
    .filter(f => f.endsWith(".md"))
    .map(f => {
      const content = fs.readFileSync(path.join(agentsDir, f), "utf-8");
      const { frontmatter, body } = parseFrontmatter(content);
      return {
        id: (frontmatter.id as string) || f.replace(".md", ""),
        name: (frontmatter.name as string) || (frontmatter.id as string),
        provides: (frontmatter.provides as string[]) || [],
        mode: "subagent",
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

// ── Capability auto-detection ──

function autoDetectCapability(task: string): string {
  const t = task.toLowerCase();
  if (/审查|review|check|audit|assess|检查|评审/.test(t)) return "review";
  if (/实现|implement|写|code|build|开发|编写|创建/.test(t)) return "implement";
  if (/修复|fix|修|bug|error|缺陷|补丁/.test(t)) return "fix";
  if (/重构|refactor|重写|优化|rewrite/.test(t)) return "refactor";
  if (/探索|explore|搜索|search|find|找|查|定位/.test(t)) return "explore";
  if (/规划|plan|设计|design|架构|方案/.test(t)) return "plan";
  if (/测试|test|验证|verify|检查|运行/.test(t)) return "verify";
  return "quick";
}

// ── Extension Entry ──

export default function dagScheduler(pi: ExtensionAPI) {
  const { z } = pi.zod;
  let agents: AgentDef[] = [];

  pi.setLabel("omp-xox DAG Scheduler v3.2");

  // ── Initialization ──
  pi.on("session_start", async (_event, ctx) => {
    const dirs = [
      path.join(ctx.cwd ?? process.cwd(), ".omp/agents"),
      path.join(process.env.HOME ?? "~", ".omp/agents"),
      path.join(import.meta.dir, "../../agents"),
    ];
    for (const dir of dirs) {
      const found = discoverAgents(dir);
      for (const a of found) {
        if (!agents.find(existing => existing.id === a.id)) {
          agents.push(a);
        }
      }
    }
    if (agents.length > 0) {
      ctx.ui.notify(`omp-xox: ${agents.length} agents loaded`, "info");
    }
  });

  // ── Slash Command: /orchestrate ──
  pi.registerCommand("orchestrate", {
    description: "Decompose a task and delegate to specialized agents",
    handler: async (args, ctx) => {
      const task = args.trim();
      if (!task) {
        ctx.ui.notify("Usage: /orchestrate <task description>", "warn");
        return;
      }
      const capId = autoDetectCapability(task);
      ctx.ui.notify(`Orchestrating: "${task.slice(0, 80)}" → ${capId}`, "info");
      await pi.sendMessage({
        customType: "orchestrate",
        content: `Please use \`delegate(task="${task}", capability="${capId}")\` to execute this task with the appropriate sub-agent.`,
        display: true,
      }, { deliverAs: "steer" });
    },
  });

  // ── Tool: delegate ──
  pi.registerTool({
    name: "delegate",
    label: "Delegate Task",
    description: "Delegate a task to a specialized sub-agent. Auto-detects capability from task description, or use explicit capability override.",
    parameters: z.object({
      task: z.string().describe("Task description in natural language"),
      capability: z.string().optional().describe("Explicit capability override (omit for auto-detect)"),
    }),
    async execute(_id, params, _signal, _onUpdate, _ctx) {
      const task = params.task;
      const capId = params.capability ?? autoDetectCapability(task);
      const cap = resolveCapability(capId);
      const agent = agents.find(a => a.id === cap.agent) ?? agents[0];
      if (!agent) {
        return {
          content: [{ type: "text" as const, text: "No agent available. Load agent contracts first." }],
          details: { task, capability: capId },
        };
      }

      try {
        const { session } = await pi.pi.createAgentSession({
          systemPrompt: (_default: { systemPrompt: string }) => `${agent.prompt}\n\n---\n\nTask: ${task}\n\nExecute this task efficiently. Use the tools available to you. Return your findings or results clearly.`,
          agentType: cap.ompAgentType as "task" | "explore" | "plan" | "designer" | "reviewer" | "quick_task",
          thinkingLevel: cap.thinking,
          timeout: cap.timeoutSeconds * 1000,
        });

        let output = "";
        session.subscribe((event: { type: string; assistantMessageEvent?: { type: string; delta?: string } }) => {
          if (event.type === "message_update" && event.assistantMessageEvent?.type === "text_delta") {
            output += event.assistantMessageEvent.delta ?? "";
          }
        });

        await session.prompt(task);

        const text = output.trim() || "(no output)";
        return {
          content: [{ type: "text" as const, text: `## Delegation: ${capId} → ${agent.name}\n\n${text}` }],
          details: { task, capability: capId, agent: agent.name },
        };
      } catch (err) {
        return {
          content: [{ type: "text" as const, text: `Delegation failed: ${String(err)}` }],
          details: { task, capability: capId, error: String(err) },
        };
      }
    },
  });

  // ── Tool: agent_status ──
  pi.registerTool({
    name: "agent_status",
    label: "Agent Status",
    description: "List all loaded agent contracts and their capabilities",
    parameters: z.object({}),
    async execute(_id, _params, _signal, _onUpdate, _ctx) {
      if (agents.length === 0) {
        return {
          content: [{ type: "text" as const, text: "No agents loaded. Agent contracts are loaded from .omp/agents/, ~/.omp/agents/, or the bundled agents/ directory on session start." }],
          details: { count: 0, agents: [] },
        };
      }
      const lines = agents.map(a =>
        `- **${a.name}** (\`${a.id}\`): provides [${a.provides.join(", ")}], model=${a.budget.modelRole}, thinking=${a.budget.thinking}, tools=[${a.tools.join(", ")}]`
      );
      return {
        content: [{ type: "text" as const, text: `## Loaded Agents (${agents.length})\n\n${lines.join("\n")}` }],
        details: { count: agents.length, agents: agents.map(a => ({ id: a.id, name: a.name, provides: a.provides, modelRole: a.budget.modelRole, thinking: a.budget.thinking })) },
      };
    },
  });
}
