// omp-xox v3.2: Checkpoint Notepad — working memory during task execution
//
// GenericAgent equivalent: update_working_checkpoint — a short-term notepad
// the agent writes to during execution. Prevents context loss when the model
// loses track of what it was doing mid-task.
//
// Tool:
//   set_checkpoint — write a working checkpoint note
//
// Hook integration:
//   workspace-map reads checkpoints and injects them on session start/resume

import type { ExtensionAPI } from "@oh-my-pi/pi-coding-agent";
import { loadConfig, envFlag } from "../shared/config-loader.ts";

export interface CheckpointConfig {
  enabled: boolean;
  maxCheckpoints: number;  // keep only the N most recent
}

const DEFAULTS: CheckpointConfig = {
  enabled: true,
  maxCheckpoints: 10,
};

// ---- Extension Entry ----

export default function checkpointNotepad(pi: ExtensionAPI) {
  const { z } = pi.zod;
  const { config } = loadConfig<CheckpointConfig>(
    process.cwd(), "checkpoint-notepad", DEFAULTS,
  );

  if (!envFlag("OMP_CHECKPOINT", config.enabled)) {
    pi.setLabel("omp-xox Checkpoint (disabled)");
    return;
  }

  pi.setLabel("omp-xox Checkpoint Notepad v3.2");

  pi.registerTool({
    name: "set_checkpoint",
    label: "Set Checkpoint",
    description: "Write a working checkpoint note. Use during long tasks to record progress, decisions, or next steps. Prevents context loss.",
    parameters: z.object({
      note: z.string().describe("Checkpoint content: what did you just finish, what's next, any decisions made, or pitfalls discovered"),
      status: z.enum(["in_progress", "blocked", "done", "note"]).optional().default("in_progress").describe("Current status of the work"),
    }),
    async execute(_id, params, _signal, _onUpdate, _ctx) {
      const now = new Date().toISOString();

      // Persist via OMP custom entry — survives compaction and session restart
      pi.appendEntry("omp-xox-checkpoint", {
        note: params.note.slice(0, 2000),
        status: params.status ?? "in_progress",
        at: now,
      });

      return {
        content: [{
          type: "text" as const,
          text: `📝 Checkpoint [${params.status ?? "in_progress"}]: ${params.note.slice(0, 300)}${params.note.length > 300 ? "..." : ""}`,
        }],
        details: { status: params.status, at: now },
      };
    },
  });
}
