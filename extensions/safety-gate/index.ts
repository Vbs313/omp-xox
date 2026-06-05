// omp-xox v2: Safety Gate — Rule-driven command interception
// Based on Anthropic 2026 Trend #8: "Security-first architecture"
// + Anthropic BEA: "Guardrails: one model instance processes user queries
// while another screens for inappropriate content"

import type { ExtensionAPI } from "@oh-my-pi/pi-coding-agent";
import * as fs from "node:fs";
import * as path from "node:path";
import * as os from "node:os";

// ── Rule Engine ──

interface CompiledRule {
  regex: RegExp;
  action: "block" | "confirm" | "warn";
  message: string;
}

interface SafetyRule {
  pattern: string;
  action: "block" | "confirm" | "warn";
  message: string;
}

interface SafetyConfig {
  enabled: boolean;
  mode: "strict" | "permissive";
  rules: SafetyRule[];
  compiled: CompiledRule[];
}

const DEFAULT_RULES: SafetyRule[] = [
  { pattern: "rm\\s+-rf\\s+/", action: "block", message: "Blocked: recursive delete of root filesystem" },
  { pattern: "rm\\s+-rf\\s+~", action: "block", message: "Blocked: recursive delete of home directory" },
  { pattern: "rm\\s+-rf\\s+\\$HOME", action: "block", message: "Blocked: recursive delete of home directory" },
  { pattern: "curl.*\\|\\s*(ba)?sh", action: "block", message: "Blocked: piping curl to shell — use package manager instead" },
  { pattern: "wget.*\\|\\s*(ba)?sh", action: "block", message: "Blocked: piping wget to shell" },
  { pattern: ">\\s*/dev/sd[a-z]", action: "block", message: "Blocked: writing directly to block device" },
  { pattern: "dd\\s+if=.*of=/dev/sd", action: "block", message: "Blocked: dd to block device" },
  { pattern: "mkfs\\.", action: "block", message: "Blocked: filesystem format command" },
  { pattern: ":\\{\\s*:\\|:.*\\}", action: "block", message: "Blocked: fork bomb pattern" },
  { pattern: "chmod\\s+777\\s+/", action: "warn", message: "Warning: chmod 777 on root-level paths" },
  { pattern: "git\\s+push\\s+.*--force", action: "confirm", message: "Confirm: force push to remote" },
  { pattern: "git\\s+push\\s+.*-f", action: "confirm", message: "Confirm: force push to remote" },
  { pattern: "git\\s+reset\\s+--hard", action: "confirm", message: "Confirm: hard reset — will discard changes" },
  { pattern: "docker\\s+rm\\s+-f", action: "confirm", message: "Confirm: force-remove docker containers" },
  { pattern: "docker\\s+system\\s+prune", action: "confirm", message: "Confirm: docker system prune — irreversible cleanup" },
  { pattern: "shutdown|reboot|halt|poweroff", action: "confirm", message: "Confirm: system power operation" },
  { pattern: "sudo\\s+su", action: "warn", message: "Warning: switching to root user" },
  { pattern: "eval\\s+", action: "warn", message: "Warning: eval can execute arbitrary code" },
  { pattern: "npm\\s+publish|bun\\s+publish", action: "confirm", message: "Confirm: publishing package" },
  { pattern: "DROP\\s+(TABLE|DATABASE)", action: "warn", message: "Warning: destructive SQL operation" },
];

function compileRules(rules: SafetyRule[]): CompiledRule[] {
  const compiled: CompiledRule[] = [];
  for (const r of rules) {
    try {
      compiled.push({ regex: new RegExp(r.pattern, "i"), action: r.action, message: r.message });
    } catch { /* skip invalid regex */ }
  }
  return compiled;
}
// ── Rule Loading ──

function loadRules(userDir: string, projectDir?: string): SafetyConfig {
  const config: SafetyConfig = { enabled: true, mode: "strict", rules: [...DEFAULT_RULES] };

  // Load user-level rules
  const userPath = path.join(userDir, "safety-rules.json");
  if (fs.existsSync(userPath)) {
    try {
      const userRules: SafetyRule[] = JSON.parse(fs.readFileSync(userPath, "utf-8"));
      for (const r of userRules) config.rules.push(r);
    } catch { /* ignore parse errors */ }
  }

  // Load project-level rules (override user)
  if (projectDir) {
    const projPath = path.join(projectDir, ".omp-xox", "safety-rules.json");
    if (fs.existsSync(projPath)) {
      try {
        const projRules: SafetyRule[] = JSON.parse(fs.readFileSync(projPath, "utf-8"));
        for (const r of projRules) config.rules.push(r);
      } catch { /* ignore parse errors */ }
    }
  }

  config.compiled = compileRules(config.rules);
  return config;
}

// ── Extension Entry ──

export default function safetyGate(pi: ExtensionAPI) {
  const { z } = pi.zod;
  let config: SafetyConfig = { enabled: true, mode: "strict", rules: [...DEFAULT_RULES], compiled: compileRules(DEFAULT_RULES) };
  const stats = { blocked: 0, confirmed: 0, warned: 0 };


  pi.setLabel("omp-xox Safety Gate");

  // Load rules on session start
  pi.on("session_start", async (_event, ctx) => {
    const userDir = path.join(os.homedir(), ".omp", "agent");
    const projectDir = ctx.cwd ?? undefined;
    config = loadRules(userDir, projectDir);
    ctx.ui.notify(
      `Safety Gate: ${config.mode} mode, ${config.rules.length} rules loaded (${stats.blocked}b/${stats.confirmed}c/${stats.warned}w)`,
      "info"
    );
  });

  // Intercept bash commands
  pi.on("tool_call", async (event) => {
    if (event.toolName !== "bash") return;
    if (!config.enabled) return;

    const command = String(event.input?.command ?? "");
    if (!command.trim()) return;

    // Check against all rules
    let highestAction: "block" | "confirm" | "warn" | null = null;
    let highestMessage = "";

    for (const rule of config.compiled) {
      if (rule.regex.test(command)) {
        if (rule.action === "block") {
          highestAction = "block";
          highestMessage = rule.message;
          break;
        }
        if (rule.action === "confirm" && highestAction !== "block") {
          highestAction = "confirm";
          highestMessage = rule.message;
        }
        if (rule.action === "warn" && !highestAction) {
          highestAction = "warn";
          highestMessage = rule.message;
        }
      }
    }

    if (!highestAction) return;

    switch (highestAction) {
      case "block":
        stats.blocked++;
        return { block: true, reason: highestMessage };

      case "confirm":
        if (config.mode === "strict") {
          // In strict mode without UI, confirm acts like block
          stats.blocked++;
          return { block: true, reason: `${highestMessage} (strict mode: confirm → block)` };
        }
        stats.confirmed++;
        // In permissive mode, allow with warning injected
        if (event.input) {
          event.input.command = `echo "[SAFETY] ${highestMessage}" && ${command}`;
        }
        return;

      case "warn":
        stats.warned++;
        if (event.input) {
          event.input.command = `echo "[SAFETY] ${highestMessage}" && ${command}`;
        }
        return;
    }
  });

  // ── Slash Command: /safety ──
  pi.registerCommand("safety", {
    description: "Show or manage safety gate rules",
    handler: async (args, ctx) => {
      const subcommand = args.trim().toLowerCase();

      if (subcommand === "status" || subcommand === "") {
        const lines = [
          `## Safety Gate — ${config.mode} mode (${config.enabled ? "enabled" : "disabled"})`,
          `Rules: ${config.rules.length} loaded`,
          `Stats: ${stats.blocked} blocked, ${stats.confirmed} confirmed, ${stats.warned} warned`,
          "",
          "### Active Rules",
        ];
        for (const r of config.rules) {
          lines.push(`- \`${r.pattern}\` → **${r.action}**: ${r.message}`);
        }
        ctx.ui.notify(lines.join("\n"), "info");
      } else if (subcommand === "toggle") {
        config.enabled = !config.enabled;
        ctx.ui.notify(`Safety Gate: ${config.enabled ? "ENABLED" : "DISABLED"}`, "info");
      } else if (subcommand === "strict") {
        config.mode = "strict";
        ctx.ui.notify("Safety Gate: strict mode (confirm → block)", "info");
      } else if (subcommand === "permissive") {
        config.mode = "permissive";
        ctx.ui.notify("Safety Gate: permissive mode (confirm → allow with warning)", "info");
      } else {
        ctx.ui.notify("Usage: /safety [status|toggle|strict|permissive]", "warning");
      }
    },
  });
}
