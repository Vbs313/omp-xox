// omp-xox v2: Context Guard — Semantic context preservation
// v2.1: Detects omp minimizer to avoid double-truncation

import type { ExtensionAPI } from "@oh-my-pi/pi-coding-agent";
import { strategyFor } from "./strategies/index.ts";

interface ContextGuardConfig {
  enabled: boolean;
  minTriggerChars: number;
  totalTruncated: number;
  totalSavedChars: number;
}

export default function contextGuard(pi: ExtensionAPI) {
  const config: ContextGuardConfig = { enabled: true, minTriggerChars: 2000, totalTruncated: 0, totalSavedChars: 0 };

  pi.setLabel("omp-xox Context Guard");

  pi.on("session_start", async (_event, ctx) => {
    ctx.ui.notify(`Context Guard: active, trigger ≥ ${config.minTriggerChars} chars`, "info");
  });

  pi.on("tool_result", async (event) => {
    if (!config.enabled) return;
    const content = event.result?.content;
    if (!content || !Array.isArray(content)) return;

    const strategy = strategyFor(event.toolName);

    for (let i = 0; i < content.length; i++) {
      const block = content[i];
      if (block?.type !== "text" || typeof block.text !== "string") continue;
      if (block.text.length < config.minTriggerChars) continue;

      // Skip if omp minimizer already truncated (prevents double-truncation)
      if (block.text.includes("[raw output: artifact://") || block.text.includes("[Output truncated")) continue;

      const originalLen = block.text.length;
      const truncated = strategy.apply(block.text, {
        exitCode: event.result?.details?.exitCode as number | undefined,
      });

      if (truncated.length < originalLen) {
        content[i] = { ...block, text: truncated + `\n[CG: ${originalLen}→${truncated.length}]` };
        config.totalTruncated++;
        config.totalSavedChars += originalLen - truncated.length;
      }
    }
  });

  pi.registerCommand("context", {
    description: "Show or manage context guard settings",
    handler: async (args, ctx) => {
      const sub = args.trim().toLowerCase();
      if (sub === "status" || sub === "") {
        ctx.ui.notify(
          `Context Guard: ${config.enabled ? "ACTIVE" : "OFF"} | trigger ≥ ${config.minTriggerChars} chars | ${config.totalTruncated} interventions, ${config.totalSavedChars.toLocaleString()} chars saved`,
          "info"
        );
      } else if (sub === "toggle") {
        config.enabled = !config.enabled;
        ctx.ui.notify(`Context Guard: ${config.enabled ? "ENABLED" : "DISABLED"}`, "info");
      } else if (sub === "reset") {
        config.totalTruncated = 0;
        config.totalSavedChars = 0;
        ctx.ui.notify("Context Guard: stats reset", "info");
      } else {
        ctx.ui.notify("Usage: /context [status|toggle|reset]", "warning");
      }
    },
  });
}
