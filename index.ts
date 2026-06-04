// omp-xox v2: Unified entry point
// Imports and delegates to all 8 extensions in a single module.
// OMP auto-discovers this as the extension entry when loading from ~/.omp/agent/extensions/omp-xox/

import type { ExtensionAPI } from "@oh-my-pi/pi-coding-agent";
import dagScheduler from "./extensions/dag-scheduler/index.ts";
import devTools from "./extensions/dev-tools/index.ts";
import safetyGate from "./extensions/safety-gate/index.ts";
import contextGuard from "./extensions/context-guard/index.ts";
import fallbackPipeline from "./extensions/fallback-pipeline/index.ts";
import verificationGate from "./extensions/verification-gate/index.ts";
import taskSpawner from "./extensions/task-spawner/index.ts";
import autoDelegate from "./extensions/auto-delegate/index.ts";
import knowledgeWriter from "./extensions/knowledge-writer/index.ts";

export default function ompXox(pi: ExtensionAPI) {
  pi.setLabel("omp-xox v2");

  // Register all extensions in dependency order
  safetyGate(pi);        // tool_call hook — must be first to intercept bash
  contextGuard(pi);      // tool_result hook — truncates large outputs
  fallbackPipeline(pi);  // session_error hook — tracks fallback events
  verificationGate(pi);  // run_verification tool + /verify command
  devTools(pi);          // safe_edit + git_* + run_tests
  taskSpawner(pi);       // enqueue_task + mailbox_*
  knowledgeWriter(pi);   // compact_output hook + /archive + archive_to_knowledge
  autoDelegate(pi);      // before_agent_start hook — keyword routing
  dagScheduler(pi);      // delegate + agent_status + /orchestrate
}
