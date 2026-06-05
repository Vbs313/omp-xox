// omp-xox v3.1: Path Guard — per-directory permit rules for tool operations
//
// Extends safety-gate's command-content rules with path-level whitelisting.
// Claude Code equivalent: .claude/settings.json PermissionRequest hooks with path matchers.
//
// Config: .omp-xox/path-rules.json (project) or ~/.omp/agent/omp-xox/path-rules.json (user)

import type { ExtensionAPI } from "@oh-my-pi/pi-coding-agent";
import { loadConfig, envFlag } from "../shared/config-loader.ts";

export interface PathRule {
  path: string;
  action: "allow" | "deny" | "confirm" | "warn";
  tools: string[];
}

export interface PathGuardConfig {
  enabled: boolean;
  defaultAction: "allow" | "deny";
  rules: PathRule[];
}

const DEFAULTS: PathGuardConfig = {
  enabled: true,
  defaultAction: "allow",
  rules: [
    { path: "/tmp/*", action: "allow", tools: ["*"] },
    { path: ".env*", action: "warn", tools: ["read", "write", "edit"] },
    { path: "/etc/*", action: "deny", tools: ["*"] },
    { path: "/proc/*", action: "deny", tools: ["*"] },
    { path: "/sys/*", action: "deny", tools: ["*"] },
    { path: "~/.ssh/*", action: "deny", tools: ["read", "write", "edit"] },
    { path: "~/.gnupg/*", action: "deny", tools: ["read", "write", "edit"] },
  ],
};

// Path matching: supports glob syntax (*, **, ?)
function matchPath(pattern: string, target: string): boolean {
  const reStr = pattern
    .replace(/[.+^${}()|[\]\\]/g, "\\$&")
    .replace(/\*/g, ".*")
    .replace(/\?/g, ".");
  const re = new RegExp(`^${reStr}$`, "i");
  return re.test(target);
}

function extractPaths(toolName: string, input: Record<string, unknown>): string[] {
  switch (toolName) {
    case "write":
    case "edit": {
      const p = String(input.path ?? input.file_path ?? "");
      return p ? [p] : [];
    }
    case "read": {
      const p = String(input.path ?? input.file_path ?? "");
      return p ? [p.split(":")[0]] : [];
    }
    case "bash": {
      const cmd = String(input.command ?? "");
      const paths: string[] = [];
      const re = /(?:\/[\w.-]+)+(?:\/[\w.-]+)*/g;
      let m: RegExpExecArray | null;
      while ((m = re.exec(cmd)) !== null) {
        paths.push(m[0]);
      }
      return paths;
    }
    default:
      return [];
  }
}

// ---- Extension Entry ----

export default function pathGuard(pi: ExtensionAPI) {
  const { config } = loadConfig<PathGuardConfig>(
    process.cwd(), "path-rules", DEFAULTS,
  );

  if (!envFlag("OMP_PATH_GUARD", config.enabled)) {
    pi.setLabel("omp-xox Path Guard (disabled)");
    return;
  }

  pi.setLabel("omp-xox Path Guard v3.1");

  pi.on("tool_call", async (event, ctx) => {
    if (event.toolName === "lsp") return;
    if (event.toolName === "skill") return;

    const paths = extractPaths(event.toolName, event.input ?? {});
    if (paths.length === 0) return;

    const home = process.env.HOME ?? "/root";

    for (const rawPath of paths) {
      const target = rawPath.startsWith("~") ? rawPath.replace("~", home) : rawPath;

      let matched: PathRule | null = null;
      for (const rule of config.rules) {
        const expanded = rule.path.startsWith("~")
          ? rule.path.replace("~", home)
          : rule.path;
        if (matchPath(expanded, target)) {
          if (rule.tools.includes("*") || rule.tools.includes(event.toolName)) {
            matched = rule;
            break;
          }
        }
      }

      if (!matched) continue;

      if (matched.action === "deny") {
        return {
          block: true,
          reason: `Path Guard: "${rawPath}" denied by rule "${matched.path}"`,
        };
      }

      if (matched.action === "warn") {
        ctx.ui.notify(`Path Guard: "${rawPath}" matched rule "${matched.path}" (warn)`, "warn");
      }
      // "allow" and "confirm" (future) — no action
    }
  });
}
