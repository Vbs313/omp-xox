// omp-xox v2: Dev Tools — Unified entry point
// Bundles safe-edit, git-ops, and test-runner into a single extension

import type { ExtensionAPI } from "@oh-my-pi/pi-coding-agent";
import safeEdit from "./safe-edit.ts";
import gitOps from "./git-ops.ts";
import testRunner from "./test-runner.ts";

export default function devTools(pi: ExtensionAPI) {
  pi.setLabel("omp-xox Dev Tools");

  // Delegate to each sub-module
  safeEdit(pi);
  gitOps(pi);
  testRunner(pi);
}
