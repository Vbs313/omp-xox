// omp-xox v2: Fallback Pipeline — Model fallback visibility + manual control
// v2.1: Removed hook-based retry (inline fallback in run_subagent handles this natively).
// Keeps the /fallback command for visibility into fallback chain configuration.

import type { ExtensionAPI } from "@oh-my-pi/pi-coding-agent";

type ErrorClass = "rate_limit" | "server_error" | "context_length" | "timeout" | "tool_error" | "unknown";

interface FallbackStep {
  modelRole: string;
  thinking: string;
  maxRetries: number;
  description: string;
}

interface FallbackChain {
  capabilities: string[];
  steps: FallbackStep[];
}

const DEFAULT_CHAINS: FallbackChain[] = [
  {
    capabilities: ["implement", "fix", "refactor"],
    steps: [
      { modelRole: "default", thinking: "high", maxRetries: 1, description: "mimo-v2.5-pro:high (primary)" },
      { modelRole: "default", thinking: "medium", maxRetries: 1, description: "mimo-v2.5-pro:medium (降级 thinking)" },
      { modelRole: "slow", thinking: "high", maxRetries: 1, description: "opencode-go/deepseek-v4-flash:high (真正兜底)" },
    ],
  },
  {
    capabilities: ["plan", "design", "review", "critique"],
    steps: [
      { modelRole: "default", thinking: "xhigh", maxRetries: 1, description: "mimo-v2.5-pro:xhigh (primary)" },
      { modelRole: "default", thinking: "high", maxRetries: 1, description: "mimo-v2.5-pro:high (降级 thinking)" },
      { modelRole: "slow", thinking: "high", maxRetries: 1, description: "opencode-go/deepseek-v4-flash:high (真正兜底)" },
    ],
  },
  {
    capabilities: ["verify", "test", "explore", "search"],
    steps: [
      { modelRole: "default", thinking: "low", maxRetries: 1, description: "mimo-v2.5-pro:low (primary)" },
      { modelRole: "default", thinking: "off", maxRetries: 1, description: "mimo-v2.5-pro:off (关闭 thinking)" },
      { modelRole: "smol", thinking: "high", maxRetries: 1, description: "mimo-v2.5:high (视觉模型兜底)" },
    ],
  },
];

function classifyError(error: unknown): ErrorClass {
  const msg = String(error ?? "").toLowerCase();
  if (msg.includes("429") || msg.includes("rate")) return "rate_limit";
  if (msg.includes("503") || msg.includes("502") || msg.includes("500") || msg.includes("unavailable")) return "server_error";
  if (msg.includes("context") && (msg.includes("length") || msg.includes("exceed"))) return "context_length";
  if (msg.includes("timeout") || msg.includes("timed")) return "timeout";
  return "unknown";
}

export default function fallbackPipeline(pi: ExtensionAPI) {
  let enabled = true;
  let totalFallbacks = 0;

  pi.setLabel("omp-xox Fallback Pipeline");

  // Track fallback events for visibility (does not change execution)
  pi.on("session_error", async (event, ctx) => {
    if (!enabled) return;
    const errorClass = classifyError(event.error);
    totalFallbacks++;
    ctx.ui.notify(`[Fallback] ${event.agentId ?? "agent"}: ${errorClass} → inline fallback in run_subagent`, "warning");
  });

  pi.registerCommand("fallback", {
    description: "Show fallback chain configuration",
    handler: async (args, ctx) => {
      const sub = args.trim().toLowerCase();
      if (sub === "status" || sub === "") {
        const lines = [
          `## Fallback Pipeline — ${enabled ? "ACTIVE" : "OFF"} | ${totalFallbacks} fallbacks tracked`,
          "",
          "Fallback chains (used by run_subagent inline):",
        ];
        for (const chain of DEFAULT_CHAINS) {
          lines.push(`**${chain.capabilities.join(", ")}**`);
          for (const step of chain.steps) {
            lines.push(`  → ${step.description} (retries: ${step.maxRetries})`);
          }
        }
        ctx.ui.notify(lines.join("\n"), "info");
      } else if (sub === "toggle") {
        enabled = !enabled;
        ctx.ui.notify(`Fallback tracking: ${enabled ? "ENABLED" : "DISABLED"}`, "info");
      } else {
        ctx.ui.notify("Usage: /fallback [status|toggle]", "warning");
      }
    },
  });
}
