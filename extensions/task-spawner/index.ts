// omp-xox v2: Task Spawner — Task state persistence + mailbox coordination
// Implements lightweight cross-turn coordination within omp's extension API.
//
// Design: task-spawner does NOT spawn subagents (ctx.createSubSession unavailable).
// Instead it writes tasks to .omp-xox/tasks/ as a persistent queue.
// The primary agent executes them via run_subagent in subsequent turns.
//
// mailbox_send / mailbox_read provide filesystem-based agent-to-agent messaging.
// All state survives across conversation turns — enabling multi-turn coordination.

import type { ExtensionAPI } from "@oh-my-pi/pi-coding-agent";
import * as fs from "node:fs";
import * as path from "node:path";
import * as crypto from "node:crypto";

function ensureDir(dir: string): void { fs.mkdirSync(dir, { recursive: true }); }

interface TaskRecord {
  id: string; capability: string; task: string; label: string;
  status: "pending" | "running" | "completed" | "failed";
  createdAt: number; startedAt?: number; completedAt?: number;
  result?: string; error?: string;
}

interface MailboxMessage {
  from: string; to: string; subject: string; body: string; timestamp: number;
}

export default function taskSpawner(pi: ExtensionAPI) {
  const { z } = pi.zod;
  pi.setLabel("omp-xox Task Spawner");

  // ── enqueue_task ──
  pi.registerTool({
    name: "enqueue_task",
    label: "Enqueue Task",
    description:
      "Add a task to the persistent queue (.omp-xox/tasks/). Executed later via run_subagent. " +
      "Use task_status to check progress and collect_task to get results.",
    parameters: z.object({
      capability: z.string(),
      task: z.string(),
      label: z.string().optional(),
    }),
    async execute(_id, params, _onUpdate, _signal, ctx) {
      const taskDir = path.join(ctx.cwd ?? process.cwd(), ".omp-xox", "tasks");
      ensureDir(taskDir);
      const taskId = crypto.randomBytes(4).toString("hex");
      const label = params.label ?? `${params.capability}: ${params.task.slice(0, 40)}`;
      fs.writeFileSync(
        path.join(taskDir, `${taskId}.json`),
        JSON.stringify({ id: taskId, capability: params.capability, task: params.task, label, status: "pending", createdAt: Date.now() }, null, 2),
        "utf-8"
      );
      return {
        content: [{ type: "text" as const, text: `Task enqueued: ${taskId} (${label})` }],
        details: { taskId, capability: params.capability, status: "pending" },
      };
    },
  });

  // ── mark_task ──
  pi.registerTool({
    name: "mark_task",
    label: "Mark Task",
    description: "Update a task's status and result after execution.",
    parameters: z.object({
      taskId: z.string(),
      status: z.enum(["running", "completed", "failed"]),
      result: z.string().optional(),
    }),
    async execute(_id, params, _onUpdate, _signal, ctx) {
      const p = path.join(ctx.cwd ?? process.cwd(), ".omp-xox", "tasks", `${params.taskId}.json`);
      if (!fs.existsSync(p)) return { content: [{ type: "text" as const, text: `Task ${params.taskId} not found.` }], details: {} };
      const record: TaskRecord = JSON.parse(fs.readFileSync(p, "utf-8"));
      record.status = params.status;
      if (params.status === "running") record.startedAt = Date.now();
      else record.completedAt = Date.now();
      if (params.result !== undefined) {
        if (params.status === "completed") record.result = params.result;
        else record.error = params.result;
      }
      fs.writeFileSync(p, JSON.stringify(record, null, 2), "utf-8");
      return {
        content: [{ type: "text" as const, text: `Task ${params.taskId}: ${params.status}` }],
        details: { taskId: params.taskId, status: params.status },
      };
    },
  });

  // ── task_status ──
  pi.registerTool({
    name: "task_status",
    label: "Task Status",
    description: "Check status of tasks in .omp-xox/tasks/. Omit taskId for all, use filter to narrow.",
    parameters: z.object({
      taskId: z.string().optional(),
      filter: z.enum(["all", "pending", "running", "completed", "failed"]).default("all"),
    }),
    async execute(_id, params, _onUpdate, _signal, ctx) {
      const taskDir = path.join(ctx.cwd ?? process.cwd(), ".omp-xox", "tasks");
      if (!fs.existsSync(taskDir)) return { content: [{ type: "text" as const, text: "No tasks." }], details: { tasks: [] } };
      let records: TaskRecord[] = [];
      for (const f of fs.readdirSync(taskDir)) {
        if (!f.endsWith(".json")) continue;
        const r: TaskRecord = JSON.parse(fs.readFileSync(path.join(taskDir, f), "utf-8"));
        if (params.taskId && r.id !== params.taskId) continue;
        if (params.filter !== "all" && r.status !== params.filter) continue;
        records.push(r);
      }
      records.sort((a, b) => b.createdAt - a.createdAt);
      if (records.length === 0) return { content: [{ type: "text" as const, text: "No matching tasks." }], details: { tasks: [] } };
      const icons: Record<string, string> = { pending: "○", running: "…", completed: "✓", failed: "✗" };
      const lines = records.map(r => {
        const elapsed = r.completedAt ? `${Math.round((r.completedAt - r.createdAt) / 1000)}s` : r.startedAt ? "running" : "pending";
        return `- ${icons[r.status]} **${r.id}** ${r.label} — ${r.status} (${elapsed})`;
      });
      return {
        content: [{ type: "text" as const, text: `## Tasks (${records.length})\n${lines.join("\n")}` }],
        details: { tasks: records.map(r => ({ id: r.id, capability: r.capability, status: r.status })) },
      };
    },
  });

  // ── collect_task ──
  pi.registerTool({
    name: "collect_task",
    label: "Collect Task",
    description: "Read the result of a completed task.",
    parameters: z.object({ taskId: z.string() }),
    async execute(_id, params, _onUpdate, _signal, ctx) {
      const p = path.join(ctx.cwd ?? process.cwd(), ".omp-xox", "tasks", `${params.taskId}.json`);
      if (!fs.existsSync(p)) return { content: [{ type: "text" as const, text: `Task ${params.taskId} not found.` }], details: {} };
      const r: TaskRecord = JSON.parse(fs.readFileSync(p, "utf-8"));
      return {
        content: [{ type: "text" as const, text: r.result ?? r.error ?? "(no result)" }],
        details: { taskId: params.taskId, status: r.status, capability: r.capability },
      };
    },
  });

  // ── mailbox_send ──
  pi.registerTool({
    name: "mailbox_send",
    label: "Send Mail",
    description: "Send a message to another agent via .omp-xox/mailbox/. Survives across turns.",
    parameters: z.object({ to: z.string(), subject: z.string(), body: z.string() }),
    async execute(_id, params, _onUpdate, _signal, ctx) {
      const dir = path.join(ctx.cwd ?? process.cwd(), ".omp-xox", "mailbox");
      ensureDir(dir);
      const id = crypto.randomBytes(4).toString("hex");
      fs.writeFileSync(path.join(dir, `${id}.json`), JSON.stringify({
        from: "agent", to: params.to, subject: params.subject, body: params.body, timestamp: Date.now(),
      }, null, 2), "utf-8");
      return {
        content: [{ type: "text" as const, text: `Sent to ${params.to}: "${params.subject}"` }],
        details: { to: params.to },
      };
    },
  });

  // ── mailbox_read ──
  pi.registerTool({
    name: "mailbox_read",
    label: "Read Mailbox",
    description: "Read messages from .omp-xox/mailbox/.",
    parameters: z.object({ recipient: z.string().default("orchestrator") }),
    async execute(_id, params, _onUpdate, _signal, ctx) {
      const dir = path.join(ctx.cwd ?? process.cwd(), ".omp-xox", "mailbox");
      if (!fs.existsSync(dir)) return { content: [{ type: "text" as const, text: "No mailbox." }], details: { count: 0 } };
      const messages: MailboxMessage[] = [];
      for (const f of fs.readdirSync(dir)) {
        if (!f.endsWith(".json")) continue;
        const m: MailboxMessage = JSON.parse(fs.readFileSync(path.join(dir, f), "utf-8"));
        if (m.to === params.recipient || params.recipient === "orchestrator") messages.push(m);
      }
      messages.sort((a, b) => a.timestamp - b.timestamp);
      if (messages.length === 0) return { content: [{ type: "text" as const, text: "No messages." }], details: { count: 0 } };
      const lines = messages.map(m => `- **${m.subject}** (from: ${m.from})\n  ${m.body.slice(0, 500)}`);
      return {
        content: [{ type: "text" as const, text: `## Mailbox (${messages.length})\n${lines.join("\n\n")}` }],
        details: { count: messages.length },
      };
    },
  });

  // ── /tasks ──
  pi.registerCommand("tasks", {
    description: "Show task queue status",
    handler: async (_args, ctx) => {
      const taskDir = path.join(ctx.cwd ?? process.cwd(), ".omp-xox", "tasks");
      if (!fs.existsSync(taskDir)) { ctx.ui.notify("No tasks.", "info"); return; }
      const files = fs.readdirSync(taskDir).filter(f => f.endsWith(".json"));
      if (files.length === 0) { ctx.ui.notify("No tasks.", "info"); return; }
      const counts: Record<string, number> = { pending: 0, running: 0, completed: 0, failed: 0 };
      const icons: Record<string, string> = { pending: "○", running: "…", completed: "✓", failed: "✗" };
      const lines = files.map(f => {
        const r: TaskRecord = JSON.parse(fs.readFileSync(path.join(taskDir, f), "utf-8"));
        counts[r.status] = (counts[r.status] || 0) + 1;
        return `${icons[r.status]} ${r.id} ${r.label}`;
      });
      ctx.ui.notify(`Tasks: ${counts.pending}p ${counts.running}r ${counts.completed}✓ ${counts.failed}✗\n${lines.join("\n")}`, "info");
    },
  });
}
