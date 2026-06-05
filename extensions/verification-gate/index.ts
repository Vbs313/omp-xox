// omp-xox v3.1: Verification Gate — Post-agent completion quality checks
// Uses pi.exec() (Bun-native) instead of node:child_process execSync.

import type { ExtensionAPI } from "@oh-my-pi/pi-coding-agent";
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
  checks: VerificationCheck[];
}

// ── Verification Executors (async, pi.exec()-based) ──

async function runTestPass(cwd: string, pi: ExtensionAPI): Promise<VerificationResult> {
  const frameworks = ["bun test", "npm test", "python -m pytest", "go test ./...", "cargo test"];
  let lastError = "";

  for (const cmd of frameworks) {
    // Quick existence check for JS projects
    if (cmd === "bun test" || cmd === "npm test") {
      const pkgPath = path.join(cwd, "package.json");
      if (!fs.existsSync(pkgPath)) continue;
      try {
        const pkg = JSON.parse(fs.readFileSync(pkgPath, "utf-8"));
        if (!pkg.scripts?.test) continue;
      } catch { continue; }
    }

    const result = await pi.exec("sh", ["-c", cmd], { cwd, timeout: 120_000 });
    if (result.code === 0) {
      return { check: "test-pass", passed: true, critical: true, output: `${cmd}: all tests passed` };
    }
    lastError = result.stderr ?? result.stdout ?? `exit code ${result.code}`;
  }

  return { check: "test-pass", passed: false, critical: true, output: lastError };
}

async function runLintPass(cwd: string, pi: ExtensionAPI): Promise<VerificationResult> {
  const pkgPath = path.join(cwd, "package.json");
  if (!fs.existsSync(pkgPath)) {
    return { check: "lint-pass", passed: true, critical: false, output: "no package.json (skipped)" };
  }

  let pkg: Record<string, unknown>;
  try {
    pkg = JSON.parse(fs.readFileSync(pkgPath, "utf-8"));
  } catch {
    return { check: "lint-pass", passed: true, critical: false, output: "invalid package.json (skipped)" };
  }

  const scripts = pkg.scripts as Record<string, string> | undefined;
  if (!scripts?.lint) {
    return { check: "lint-pass", passed: true, critical: false, output: "no lint script configured (skipped)" };
  }

  const result = await pi.exec("sh", ["-c", "bun run lint"], { cwd, timeout: 60_000 });
  if (result.code === 0) {
    return { check: "lint-pass", passed: true, critical: false, output: "bun run lint: clean" };
  }

  return { check: "lint-pass", passed: false, critical: false, output: result.stderr ?? result.stdout ?? `exit ${result.code}` };
}

async function runNoNewTodos(cwd: string, pi: ExtensionAPI): Promise<VerificationResult> {
  const result = await pi.exec(
    "sh",
    ["-c", `grep -rn "TODO\\|FIXME\\|HACK" --include="*.ts" --include="*.js" --include="*.py" . 2>/dev/null || true`],
    { cwd, timeout: 15_000 },
  );

  const output = (result.stdout ?? "").trim();
  const count = output ? output.split("\n").length : 0;
  if (count > 10) {
    return { check: "no-new-todos", passed: false, critical: false, output: `${count} TODO/FIXME/HACK markers found (threshold: 10). Review before merging.` };
  }
  return { check: "no-new-todos", passed: true, critical: false, output: `${count} markers found — within threshold` };
}

async function runDiffLimit(cwd: string, maxLines: number, pi: ExtensionAPI): Promise<VerificationResult> {
  const result = await pi.exec("git", ["diff", "HEAD", "--stat"], { cwd, timeout: 10_000 });
  if (result.code !== 0) {
    return { check: "diff-limit", passed: true, critical: false, output: "not a git repo (skipped)" };
  }

  const diff = (result.stdout ?? "").trim();
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
}

// ── Gate Execution ──

async function runVerificationGate(
  checks: VerificationCheck[],
  cwd: string,
  pi: ExtensionAPI,
): Promise<{ allPassed: boolean; results: VerificationResult[] }> {
  const results: VerificationResult[] = [];

  for (const check of checks) {
    let result: VerificationResult;

    switch (check.type) {
      case "test-pass":
        result = await runTestPass(cwd, pi);
        break;
      case "lint-pass":
        result = await runLintPass(cwd, pi);
        break;
      case "no-new-todos":
        result = await runNoNewTodos(cwd, pi);
        break;
      case "diff-limit":
        result = await runDiffLimit(cwd, check.maxLines ?? 200, pi);
        break;
      default:
        result = { check: check.type, passed: true, critical: check.critical, output: "unknown check type (skipped)" };
    }

    results.push(result);
  }

  const allPassed = results.every(r => r.critical ? r.passed : true);
  return { allPassed, results };
}

// ── Extension Entry ──

export default function verificationGate(pi: ExtensionAPI) {
  const { z } = pi.zod;

  pi.setLabel("omp-xox Verification Gate v3.1");

  const DEFAULT_CHECKS: VerificationCheck[] = [
    { type: "test-pass", critical: true },
    { type: "lint-pass", critical: false },
    { type: "no-new-todos", critical: false },
    { type: "diff-limit", critical: false, maxLines: 200 },
  ];

  pi.registerTool({
    name: "run_verification",
    label: "Run Verification",
    description: "Run post-completion quality checks: tests, lint, TODO scan, diff size limit.",
    parameters: z.object({
      checks: z.array(z.object({
        type: z.enum(["test-pass", "lint-pass", "no-new-todos", "diff-limit"]),
        maxLines: z.number().optional(),
      })).optional().describe("Checks to run (defaults to all 4)"),
    }),
    async execute(_id, params, _signal, _onUpdate, _ctx) {
      const checks = params.checks ?? DEFAULT_CHECKS;
      const cwd = process.cwd();
      const { allPassed, results } = await runVerificationGate(checks, cwd, pi);

      const lines = results.map(r =>
        `- ${r.passed ? "✅" : r.critical ? "🔴" : "⚠️"} **${r.check}**: ${r.output.slice(0, 500)}`
      );

      return {
        content: [{
          type: "text" as const,
          text: [
            `## Verification: ${allPassed ? "ALL CHECKS PASSED" : "ISSUES FOUND"}`,
            `Results (${results.filter(r => r.passed).length}/${results.length} passed):`,
            ...lines,
          ].join("\n"),
        }],
        details: { allPassed, results },
      };
    },
  });

  pi.registerCommand("verify", {
    description: "Run verification checks and show results",
    handler: async (_args, ctx) => {
      const cwd = ctx.cwd ?? process.cwd();
      const { allPassed, results } = await runVerificationGate(DEFAULT_CHECKS, cwd, pi);

      const lines = results.map(r =>
        `${r.passed ? "✅" : r.critical ? "🔴" : "⚠️"} ${r.check}: ${r.output.slice(0, 200)}`
      );

      ctx.ui.notify(`Verification: ${allPassed ? "ALL PASSED" : "ISSUES"}\n${lines.join("\n")}`, allPassed ? "info" : "warn");
    },
  });
}
