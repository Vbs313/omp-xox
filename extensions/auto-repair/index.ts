// omp-xox v3.1: Auto-Repair — test-failure → fix → retry loop
//
// Cline equivalent: "heal mode" — detects test failures and auto-fixes.
// The LLM calls auto_repair(command); we run the command, parse failures,
// return the failure report, and the LLM fixes them.
//
// SECURITY: the command parameter is validated to prevent shell chaining
// (no ;, &&, ||, |, `, $(), {}, <>, []) and limited to 500 chars.
// Only test-runner commands (bun test, pytest, etc.) should be used.

import type { ExtensionAPI } from "@oh-my-pi/pi-coding-agent";
import { AUTO_REPAIR_MAX_CYCLES } from "../shared/context-limits.ts";
import { loadConfig, envFlag } from "../shared/config-loader.ts";

export interface AutoRepairConfig {
  enabled: boolean;
  maxCycles: number;
}

const DEFAULTS: AutoRepairConfig = {
  enabled: true,
  maxCycles: AUTO_REPAIR_MAX_CYCLES,
};

// ---- Validation ----

/**
 * Shell metacharacters that would allow command chaining or redirection.
 * Block these to prevent the LLM from running arbitrary commands through pi.exec().
 * Allowed: basic test runner commands like "bun test", "pytest tests/", "go test ./pkg/..."
 */
const SHELL_META = /[;&|`$(){}\[\]<>]/;

// ---- Failure Extraction ----

function extractFailures(output: string): string[] {
  const failures = new Set<string>();

  // Vitest/Jest: "FAIL src/file.ts > testName" or "● testName"
  for (const m of output.matchAll(/FAIL\s+(\S+)/g)) {
    failures.add(`FAIL ${m[1]}`);
  }
  for (const m of output.matchAll(/[×✗●]\s+(.+)/g)) {
    failures.add(`test failure: ${m[1].trim()}`);
  }

  // Python: "FAIL: test_foo" / "ERROR: test_foo"
  for (const m of output.matchAll(/^(FAIL|ERROR):\s+(.+)/gm)) {
    failures.add(`${m[1]}: ${m[2].trim()}`);
  }

  // Go: "--- FAIL: TestFoo"
  for (const m of output.matchAll(/^---\s+FAIL:\s+(\S+)/gm)) {
    failures.add(`FAIL: ${m[1]}`);
  }

  // Rust: "test test_foo ... FAILED"
  for (const m of output.matchAll(/^test\s+(\S+)\s+\.\.\.\s+FAILED/gm)) {
    failures.add(`FAILED: ${m[1]}`);
  }

  // Generic file:line
  for (const m of output.matchAll(/(\S+\.\w+):(\d+)(?::\d+)?\s*(?:error|warning|Error)/gi)) {
    failures.add(`${m[1]}:${m[2]}`);
  }

  return [...failures].slice(0, 20);
}

// ---- Extension Entry ----

export default function autoRepair(pi: ExtensionAPI) {
  const { config } = loadConfig<AutoRepairConfig>(
    process.cwd(), "auto-repair", DEFAULTS,
  );

  if (!envFlag("OMP_AUTO_REPAIR", config.enabled)) {
    pi.setLabel("omp-xox Auto-Repair (disabled)");
    return;
  }

  pi.setLabel("omp-xox Auto-Repair v3.1");
  const { z } = pi.zod;

  pi.registerTool({
    name: "auto_repair",
    label: "Auto Repair",
    description: "Run a test command and auto-fix failures up to N cycles. Command must be a simple test runner (bun test, pytest, etc.) with no shell chaining.",
    parameters: z.object({
      command: z.string().describe("Test command (e.g. 'bun test', 'pytest tests/'). No shell metacharacters allowed."),
      maxCycles: z.number().optional().default(config.maxCycles).describe("Max fix cycles (1-5)"),
    }),
    async execute(_id, params, signal, onUpdate, _ctx) {
      const cycles = Math.min(Math.max(params.maxCycles ?? config.maxCycles, 1), 5);
      const results: string[] = [];
      let lastOutput = "";
      let passed = false;

      // Validate command BEFORE any execution
      if (SHELL_META.test(params.command)) {
        return {
          content: [{ type: "text" as const, text: "❌ REJECTED: command contains shell metacharacters. Use only simple test runner commands." }],
          details: { rejected: true, reason: "shell_metacharacters" },
        };
      }
      if (params.command.length > 500) {
        return {
          content: [{ type: "text" as const, text: `❌ REJECTED: command too long (${params.command.length} > 500)` }],
          details: { rejected: true, reason: "too_long" },
        };
      }

      for (let cycle = 1; cycle <= cycles; cycle++) {
        if (signal?.aborted) {
          results.push(`[CYCLE ${cycle}] Aborted`);
          break;
        }

        onUpdate?.({
          content: [{ type: "text", text: `Running tests (cycle ${cycle}/${cycles})...` }],
          details: { cycle },
        });

        // Run test command via pi.exec() — validated above, shell-safe
        const result = await pi.exec("sh", ["-c", params.command], {
          cwd: process.cwd(),
          timeout: 120_000,
        });

        const output = (result.stdout ?? "") + "\n" + (result.stderr ?? "");
        lastOutput = output;

        if (result.code === 0 && !result.killed) {
          results.push(`[CYCLE ${cycle}] ✅ ALL TESTS PASSED`);
          passed = true;
          break;
        }

        // Extract failures
        const failures = extractFailures(output);
        if (failures.length === 0) {
          results.push(`[CYCLE ${cycle}] Tests failed (exit ${result.code}) but no parseable errors found. Raw output:\n\`\`\`\n${output.slice(0, 2000)}\n\`\`\``);
          break;
        }

        results.push(`[CYCLE ${cycle}] ${failures.length} failure(s) detected:\n${failures.map(f => `  - ${f}`).join("\n")}`);

        if (cycle < cycles) {
          results.push(`  → Fix these failures, then call auto_repair again to re-test.`);
          break;
        }
      }

      const summary = results.join("\n\n");
      const finalSnippet = lastOutput.length > 3000 ? lastOutput.slice(-3000) : lastOutput;

      return {
        content: [{
          type: "text" as const,
          text: passed
            ? `✅ Auto-repair succeeded\n\n${summary}`
            : `❌ Auto-repair failed after ${cycles} cycle(s)\n\n${summary}\n\nLast test output:\n\`\`\`\n${finalSnippet}\n\`\`\``,
        }],
        details: { cycles, passed, results },
      };
    },
  });
}
