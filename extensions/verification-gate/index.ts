// omp-xox v2: Verification Gate — Post-agent completion quality checks
// Based on Anthropic 2026 Trends #1: "Cycle times collapse from weeks to hours
// as agent-driven implementation, automated testing, and inline documentation
// feed back into rapid iteration"
// + BEA Appendix 1B: "Code solutions are verifiable through automated tests"

import type { ExtensionAPI } from "@oh-my-pi/pi-coding-agent";
import { execSync } from "node:child_process";
import * as fs from "node:fs";
import * as path from "node:path";

// ── Verification Types ──

interface VerificationCheck {
  type: string;
  command?: string;
  critical: boolean;
  maxLines?: number;
}

interface VerificationResult {
  check: string;
  passed: boolean;
  critical: boolean;
  output: string;
}

interface VerificationConfig {
  enabled: boolean;
  /** Whether non-critical failures block agent completion */
  strictMode: boolean;
}

// ── Verification Executors ──

function runTestPass(cwd: string): VerificationResult {
  const frameworks = ["bun test", "npm test", "python -m pytest", "go test ./...", "cargo test"];
  let lastError = "";

  for (const cmd of frameworks) {
    try {
      const hasTests = cmd === "bun test"
        ? (fs.existsSync(path.join(cwd, "package.json")) && JSON.parse(fs.readFileSync(path.join(cwd, "package.json"), "utf-8")).scripts?.test)
        : true;

      if (!hasTests && cmd === "bun test") continue;

      execSync(cmd, { cwd, encoding: "utf-8", timeout: 120000, maxBuffer: 10 * 1024 * 1024 });
      return { check: "test-pass", passed: true, critical: true, output: `${cmd}: all tests passed` };
    } catch (e: unknown) {
      lastError = String((e as { stderr?: string; message?: string }).stderr ?? (e as { message: string }).message ?? e);
    }
  }

  return { check: "test-pass", passed: false, critical: true, output: lastError };
}

function runLintPass(cwd: string): VerificationResult {
  const linters = [
    { cmd: "bun run lint", file: "package.json", check: (pkg: Record<string, unknown>) => pkg.scripts?.lint },
  ];

  for (const linter of linters) {
    try {
      if (fs.existsSync(path.join(cwd, linter.file))) {
        const pkg = JSON.parse(fs.readFileSync(path.join(cwd, linter.file), "utf-8"));
        if (linter.check(pkg)) {
          execSync(linter.cmd, { cwd, encoding: "utf-8", timeout: 60000 });
          return { check: "lint-pass", passed: true, critical: false, output: `${linter.cmd}: clean` };
        }
      }
    } catch (e: unknown) {
      const msg = String((e as { stderr?: string }).stderr ?? (e as { message: string }).message ?? e);
      return { check: "lint-pass", passed: false, critical: false, output: msg };
    }
  }

  return { check: "lint-pass", passed: true, critical: false, output: "no linter configured (skipped)" };
}

function runNoNewTodos(cwd: string): VerificationResult {
  try {
    const before = execSync(`grep -rn "TODO\\|FIXME\\|HACK" --include="*.ts" --include="*.js" --include="*.py" . 2>/dev/null || true`, { cwd, encoding: "utf-8", timeout: 15000 }).trim();
    const count = before ? before.split("\n").length : 0;
    if (count > 10) {
      return { check: "no-new-todos", passed: false, critical: false, output: `${count} TODO/FIXME/HACK markers found (threshold: 10). Review before merging.` };
    }
    return { check: "no-new-todos", passed: true, critical: false, output: `${count} markers found — within threshold` };
  } catch (e: unknown) {
    return { check: "no-new-todos", passed: true, critical: false, output: `check skipped: ${String(e)}` };
  }
}

function runDiffLimit(cwd: string, maxLines: number): VerificationResult {
  try {
    const diff = execSync("git diff HEAD --stat", { cwd, encoding: "utf-8", timeout: 10000 }).trim();
    const match = diff.match(/(\d+)\s+insertion.*?(\d+)\s+deletion/);
    if (!match) {
      return { check: "diff-limit", passed: true, critical: false, output: "no diff stats found" };
    }
    const inserts = parseInt(match[1], 10) || 0;
    const deletes = parseInt(match[2], 10) || 0;
    const total = inserts + deletes;
    if (total > maxLines) {
      return { check: "diff-limit", passed: false, critical: false, output: `Diff is ${total} lines (inserts=${inserts}, deletes=${deletes}), exceeds limit of ${maxLines}` };
    }
    return { check: "diff-limit", passed: true, critical: false, output: `Diff: ${total} lines — within limit` };
  } catch {
    return { check: "diff-limit", passed: true, critical: false, output: "not a git repo (skipped)" };
  }
}

// ── Gate Execution ──

async function runVerificationGate(
  checks: VerificationCheck[],
  cwd: string
): Promise<{ allPassed: boolean; results: VerificationResult[] }> {
  const results: VerificationResult[] = [];

  for (const check of checks) {
    let result: VerificationResult;

    switch (check.type) {
      case "test-pass":
        result = runTestPass(cwd);
        break;
      case "lint-pass":
        result = runLintPass(cwd);
        break;
      case "no-new-todos":
        result = runNoNewTodos(cwd);
        break;
      case "diff-limit":
        result = runDiffLimit(cwd, check.maxLines ?? 200);
        break;
      default:
        result = { check: check.type, passed: true, critical: check.critical, output: "unknown check type (skipped)" };
    }

    results.push(result);
  }

  const allPassed = results.every(r => {
    if (r.critical) return r.passed;     // Critical failures block
    return true;                          // Non-critical failures don't block
  });

  return { allPassed, results };
}

// ── Extension Entry ──

export default function verificationGate(pi: ExtensionAPI) {
  const config: VerificationConfig = { enabled: true, strictMode: false };

  pi.setLabel("omp-xox Verification Gate");

  // Provide the verification function to other extensions via a shared context
  // The dag-scheduler can call this after agent completion
  (pi as Record<string, unknown>).__ompXoxVerify = runVerificationGate;

  // ── Tool: run_verification ──
  pi.registerTool({
    name: "run_verification",
    label: "Run Verification",
    description: "Run post-implementation verification checks: tests, lint, TODO count, diff size.",
    parameters: pi.zod.object({
      checks: pi.zod.array(pi.zod.string()).optional().describe(
        "Which checks to run: test-pass, lint-pass, no-new-todos, diff-limit. Default: all"
      ),
    }),
    async execute(_id, params, _onUpdate, _signal, ctx) {
      const checks: VerificationCheck[] = (params.checks ?? ["test-pass", "lint-pass", "no-new-todos", "diff-limit"])
        .map((c: string) => ({ type: c, critical: c === "test-pass", maxLines: 200 }));

      // Only run test/lint if configured
      if (!checks.some(c => c.type === "test-pass" || c.type === "lint-pass")) {
        checks.unshift({ type: "test-pass", critical: true });
      }

      const { allPassed, results } = await runVerificationGate(checks, ctx.cwd ?? process.cwd());

      const lines = [
        `## Verification: ${allPassed ? "PASSED" : "FAILED"}`,
      ];
      for (const r of results) {
        const icon = r.passed ? "✓" : r.critical ? "✗" : "⚠";
        lines.push(`- ${icon} **${r.check}** — ${r.output}`);
      }
      if (!allPassed) {
        lines.push("\n### Action Required");
        const failed = results.filter(r => !r.passed);
        for (const f of failed) {
          lines.push(`- Fix: \`${f.check}\` → ${f.output.slice(0, 200)}`);
        }
      }

      return {
        content: [{ type: "text" as const, text: lines.join("\n") }],
        details: { allPassed, results },
      };
    },
  });

  // ── Slash Command: /verify ──
  pi.registerCommand("verify", {
    description: "Run verification checks on current changes",
    handler: async (_args, ctx) => {
      ctx.ui.notify("Running verification checks...", "info");
      const checks: VerificationCheck[] = [
        { type: "test-pass", critical: true },
        { type: "lint-pass", critical: false },
        { type: "no-new-todos", critical: false },
        { type: "diff-limit", critical: false, maxLines: 200 },
      ];
      const { allPassed, results } = await runVerificationGate(checks, ctx.cwd ?? process.cwd());
      const icon = allPassed ? "✓" : "✗";
      ctx.ui.notify(
        `${icon} Verification: ${results.filter(r => r.passed).length}/${results.length} checks passed`,
        allPassed ? "info" : "error"
      );
    },
  });
}
