// omp-xox v2: DAG Scheduler — Orchestrator-Workers Execution Engine
// Uses pi.pi.createAgentSession() for direct sub-agent spawning (no delegation workaround)

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
        name: (frontmatter.name as string) || frontmatter.id as string,
        provides: (frontmatter.provides as string[]) || [],
        mode: (frontmatter.mode as string) || "subagent",
        budget: (frontmatter.budget as AgentDef["budget"]) || { modelRole: "default", thinking: "medium", maxTurns: 20, maxTokens: 100000 },
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

  pi.setLabel("omp-xox DAG Scheduler");

  // ── Initialization ──
  pi.on("session_start", async (_event, ctx) => {
    const dirs = [
      path.join(ctx.cwd ?? process.cwd(), ".omp/agents"),
      path.join(process.env.HOME ?? "~", ".omp/agents"),
      path.join(path.dirname(new URL(import.meta.url).pathname), "../../agents"),
    ];
    for (const dir of dirs) {
      const found = discoverAgents(dir);
      for (const a of found) {
        if (!agents.find(existing => existing.id === a.id)) {
          agents.push(a);
        }
      }
    }
    ctx.ui.notify(`omp-xox: ${agents.length} agents loaded`, "info");
  });

  // ── Slash Command: /orchestrate ──
  pi.registerCommand("orchestrate", {
    description: "Decompose a task into a DAG and execute with specialized agents",
    handler: async (args, ctx) => {
      const task = args.trim();
      if (!task) {
        ctx.ui.notify("Usage: /orchestrate <task description>", "warning");
        return;
      }
      ctx.ui.notify(`Orchestrating: "${task.slice(0, 60)}..."`, "info");
      await ctx.sendMessage([
        "## Orchestration Task",
        "",
        `**Task**: ${task}`,
        "",
        "### Instructions",
        "1. **Plan**: Call `delegate` with capability=plan to decompose the task into subtasks.",
        "2. **Execute**: For each subtask, call `delegate` with the appropriate capability.",
        "   - Independent subtasks can be called in parallel (multiple `delegate` calls in one message).",
        `   - Available capabilities: explore, implement, fix, refactor, verify, test, review, plan, quick`,
        "3. **Verify**: After all subtasks complete, call `run_verification`.",
        "4. **Report**: Summarize results.",
      ].join("\n"));
    },
  });

  // ── Tool: delegate ──
  // Direct sub-agent spawning via pi.pi.createAgentSession()
  pi.registerTool({
    name: "delegate",
    label: "Delegate Task",
    description:
      "Delegate a task to a specialized sub-agent. Auto-detects capability from task keywords, "
      + "or accepts explicit capability override. Spawns a sub-agent session directly.",
    parameters: z.object({
      task: z.string().describe("Task description in natural language"),
      capability: z.string().optional().describe("Explicit capability override (omit for auto-detect)"),
    }),
    async execute(_id, params, _signal, _onUpdate, _ctx) {
      const task = params.task.trim();
      const capId = params.capability || autoDetectCapability(task);
      const cap = resolveCapability(capId);
      const agent = agents.find(a => a.id === cap.agent);

      if (!agent) {
        return {
          content: [{ type: "text" as const, text: `No agent for capability "${capId}". Available: ${agents.map(a => a.id).join(", ") || "none"}.` }],
          details: { capability: capId, status: "no_agent" },
        };
      }

      const systemPrompt = [
        `You are a specialized sub-agent: **${agent.name}**.`,
        `Capabilities: ${agent.provides.join(", ")}.`,
        `Tools available: ${agent.tools.join(", ")}.`,
        "",
        agent.prompt,
        "",
        "---",
        `Task: ${task}`,
        "",
        "Return only the result. No meta-commentary.",
      ].join("\n");

      try {
        // Direct SDK call — no delegation workaround
        const { session } = await pi.pi.createAgentSession({
          systemPrompt: [systemPrompt],
        });
        await session.prompt(task);
        await session.waitForIdle();
        const resultText = session.getLastAssistantText() ?? "(no response)";

        return {
          content: [{ type: "text" as const, text: `## Delegation: ${capId} → ${agent.name}\n\n${resultText}` }],
          details: { capability: capId, agent: agent.id, status: "ok" },
        };
      } catch (err) {
        return {
          content: [{ type: "text" as const, text: `Sub-agent execution failed: ${err instanceof Error ? err.message : String(err)}` }],
          details: { capability: capId, agent: agent.id, status: "error" },
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
          content: [{ type: "text" as const, text: "No agents loaded." }],
          details: { count: 0, agents: [] },
        };
      }
      const lines = agents.map(a =>
        `- **${a.id}** (${a.name}): provides [${a.provides.join(", ")}], model=${a.budget.modelRole}, thinking=${a.budget.thinking}, tools=[${a.tools.join(", ")}]`
      );
      return {
        content: [{ type: "text" as const, text: `## Loaded Agents (${agents.length})\n\n${lines.join("\n")}` }],
        details: { count: agents.length, agents: agents.map(a => ({ id: a.id, name: a.name, provides: a.provides })) },
      };
    },
  });
}
