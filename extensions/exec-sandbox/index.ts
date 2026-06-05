// omp-xox v3.1: Exec Sandbox — transparent docker/podman isolation for bash
//
// Architecture:
//   tool_call hook intercepts bash → wraps command in container
//   Config driven by env vars: OMP_SANDBOX_BACKEND, OMP_SANDBOX_IMAGE.
//
// Two-layer model (similar to Codex CLI):
//   1. Sandbox layer: container isolates filesystem + network
//   2. OMP's approval layer: still active (tool_call hook doesn't disable it)

import type { ExtensionAPI } from "@oh-my-pi/pi-coding-agent";
import { loadConfig, envFlag } from "../shared/config-loader.ts";

export interface SandboxConfig {
  enabled: boolean;
  backend: string;
  image: string;
  allowNetwork: boolean;
}

const DEFAULTS: SandboxConfig = {
  enabled: true,
  backend: "docker",
  image: "alpine:latest",
  allowNetwork: false,
};

/** Check if a container runtime binary is on PATH via sh -c "command -v NAME" */
async function runtimeAvailable(pi: ExtensionAPI, name: string): Promise<boolean> {
  const result = await pi.exec("sh", ["-c", `command -v ${name}`], { timeout: 5000 });
  return result.code === 0;
}

// ---- Extension Entry ----

export default function execSandbox(pi: ExtensionAPI) {
  // Load and resolve config lazily — runtime actions not available during registration
  let runner: string | null = null;
  let image: string;
  let netFlag: string;
  let configured = false;

  async function ensureConfigured(): Promise<boolean> {
    if (configured) return runner !== null;
    configured = true;

    const { config } = loadConfig<SandboxConfig>(process.cwd(), "exec-sandbox", DEFAULTS);
    if (!envFlag("OMP_SANDBOX", config.enabled)) {
      pi.setLabel("omp-xox Exec Sandbox (disabled)");
      return false;
    }

    const explicit = process.env.OMP_SANDBOX_BACKEND ?? config.backend;
    if (!explicit || explicit === "none") {
      pi.setLabel("omp-xox Exec Sandbox (disabled)");
      return false;
    }

    if (explicit !== "docker" && explicit !== "podman") {
      // Custom binary
      const ok = await runtimeAvailable(pi, explicit);
      if (!ok) {
        pi.setLabel("omp-xox Exec Sandbox (no runtime)");
        return false;
      }
      runner = explicit;
    } else {
      const ok = await runtimeAvailable(pi, explicit);
      if (!ok) {
        pi.setLabel("omp-xox Exec Sandbox (no runtime)");
        return false;
      }
      runner = explicit;
    }

    image = process.env.OMP_SANDBOX_IMAGE ?? config.image;
    netFlag = config.allowNetwork ? "" : "--network none";
    pi.setLabel(`omp-xox Exec Sandbox (${runner})`);
    return true;
  }

  pi.on("session_start", async (_event, ctx) => {
    await ensureConfigured();
    if (runner) {
      ctx.ui.notify(`Sandbox: ${runner} ${image}${config.allowNetwork ? "" : " (no network)"}`, "info");
    }
  });

  // Intercept bash tool calls — wrap command in container
  pi.on("tool_call", async (event) => {
    if (event.toolName !== "bash") return;
    await ensureConfigured();
    if (!runner) return;

    const rawCmd = String(event.input?.command ?? "");
    if (!rawCmd.trim()) return;

    const cwd = String(event.input?.cwd ?? process.cwd());
    const home = process.env.HOME ?? "/root";

    // Build: docker run --rm --network none -v cwd:cwd:rw -w cwd -e HOME home image sh -c 'cmd'
    const args: string[] = ["run", "--rm", "-v", `${cwd}:${cwd}:rw`, "-w", cwd, "-e", `HOME=${home}`];
    if (netFlag) args.splice(2, 0, netFlag); // insert after run --rm
    args.push(image, "sh", "-c", rawCmd);

    // Wrap command — the bash tool executes this as a single string
    event.input.command = `${runner} ${args.map(a =>
      a.includes(" ") ? `'${a.replace(/'/g, "'\\''")}'` : a
    ).join(" ")}`;
  });
}
