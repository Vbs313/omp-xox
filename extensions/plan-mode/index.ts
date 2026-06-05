// omp-xox v3.1: Plan Mode — read-only analysis before execution
//
// /plan        → restricts to read-only tools, raises thinking level
// /plan-execute → restores full tool set
//
// OMP already supports plan mode for sub-agents via task tool's effectiveAgent.
// This module brings it to the TOP-LEVEL agent.

import type { ExtensionAPI } from "@oh-my-pi/pi-coding-agent";

const READONLY_TOOLS = ["read", "search", "find", "lsp", "web_search"];

const PLAN_PROMPT = [
  "PLAN MODE ACTIVE — read-only analysis.",
  "You CAN: read files, search code, explore the repo, inspect LSP symbols.",
  "You CANNOT: write/edit files, run bash commands, spawn sub-agents.",
  "When your plan is complete, the user will run /plan-execute to switch.",
  "",
  "Your task: produce a clear, actionable plan with:",
  "1. Files to create/modify (with paths)",
  "2. Specific code changes needed",
  "3. Testing strategy",
  "4. Potential risks or edge cases",
].join("\n");

const EXECUTE_PROMPT = "EXECUTION MODE — full tool access restored. Implement the plan now.";

export default function planMode(pi: ExtensionAPI) {
  let planActive = false;
  let originalTools: string[] = [];

  pi.setLabel("omp-xox Plan Mode v3.1");

  pi.registerCommand("plan", {
    description: "Enter read-only plan mode",
    handler: async (_args, ctx) => {
      if (planActive) {
        ctx.ui.notify("Already in plan mode. Use /plan-execute to exit.", "info");
        return;
      }

      originalTools = pi.getActiveTools();
      planActive = true;
      pi.setThinkingLevel("high");

      try {
        const allTools = pi.getAllTools();
        const available = READONLY_TOOLS.filter(t => allTools.includes(t));
        pi.setActiveTools(available);
      } catch (err) {
        ctx.ui.notify(`Plan mode: tool restriction failed (${String(err)}), continuing`, "warn");
      }

      await pi.sendMessage(
        { customType: "plan-mode", content: PLAN_PROMPT, display: true },
        { deliverAs: "steer" },
      );

      ctx.ui.notify("Plan mode active — read-only tools + high thinking", "info");
    },
  });

  pi.registerCommand("plan-execute", {
    description: "Exit plan mode, restore all tools",
    handler: async (_args, ctx) => {
      if (!planActive) {
        ctx.ui.notify("Not in plan mode. Use /plan to enter.", "info");
        return;
      }

      planActive = false;
      pi.setThinkingLevel("high");

      if (originalTools.length > 0) {
        try {
          pi.setActiveTools(originalTools);
        } catch (err) {
          ctx.ui.notify(`Plan-execute: tool restore failed (${String(err)})`, "warn");
        }
      }

      await pi.sendMessage(
        { customType: "plan-execute", content: EXECUTE_PROMPT, display: true },
        { deliverAs: "steer" },
      );

      ctx.ui.notify("Execution mode — full tools restored", "info");
    },
  });
}
