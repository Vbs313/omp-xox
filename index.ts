// omp-xox v3.1 — 9 modules: 4 kept from v3 + 5 new
// Registration order is intentional — hooks fire in register order

import type { ExtensionAPI } from "@oh-my-pi/pi-coding-agent";

// v3 (kept)
import safetyGate from "./extensions/safety-gate/index.ts";
import devTools from "./extensions/dev-tools/index.ts";
import dagScheduler from "./extensions/dag-scheduler/index.ts";
import verificationGate from "./extensions/verification-gate/index.ts";

// v3.1 (new)
import workspaceMap from "./extensions/workspace-map/index.ts";
import execSandbox from "./extensions/exec-sandbox/index.ts";
import planMode from "./extensions/plan-mode/index.ts";
import pathGuard from "./extensions/path-guard/index.ts";
import autoRepair from "./extensions/auto-repair/index.ts";

export default function ompXox(pi: ExtensionAPI) {
  pi.setLabel("omp-xox v3.1");

  // --- tool_call hooks (fire in order: block first, then mutate) ---
  safetyGate(pi);           // command-content rules — block destructive commands
  pathGuard(pi);            // per-dir path rules — block restricted paths
  execSandbox(pi);          // docker/podman wrapper — mutates command last

  // --- before_agent_start hooks (first-wins for message injection) ---
  workspaceMap(pi);         // repo structure index — injects once per session

  // --- commands (registration order for conflict resolution) ---
  planMode(pi);             // /plan + /plan-execute

  // --- tools (no order dependency between them) ---
  devTools(pi);             // run_tests
  autoRepair(pi);           // auto_repair (depends on delegate from dagScheduler)
  dagScheduler(pi);         // delegate + agent_status + /orchestrate
  verificationGate(pi);     // run_verification + /verify
}
