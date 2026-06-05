// omp-xox v3.1: test-runner — Auto-detect test framework and execute tests
// Structured output with pass/fail parsing for common frameworks.
// Uses pi.exec() (Bun-native) instead of node:child_process execSync.

import type { ExtensionAPI } from "@oh-my-pi/pi-coding-agent";
import * as fs from "node:fs";
import * as path from "node:path";

// ── Framework Detection ──

interface Framework {
  name: string;
  command: string;
  files: string[];
}

const FRAMEWORKS: Framework[] = [
  { name: "vitest", command: "bun test", files: ["vitest.config.ts", "vitest.config.js", "vitest.config.mjs"] },
  { name: "jest", command: "bun test", files: ["jest.config.ts", "jest.config.js", "jest.config.mjs"] },
  { name: "mocha", command: "bun test", files: [".mocharc.js", ".mocharc.json", ".mocharc.yml"] },
  { name: "playwright", command: "bunx playwright test", files: ["playwright.config.ts", "playwright.config.js"] },
  { name: "pytest", command: "python -m pytest", files: ["pytest.ini", "pyproject.toml", "setup.cfg"] },
  { name: "go-test", command: "go test ./...", files: ["go.mod"] },
  { name: "cargo-test", command: "cargo test", files: ["Cargo.toml"] },
];

function detectFramework(cwd: string): Framework | null {
  for (const fw of FRAMEWORKS) {
    for (const f of fw.files) {
      if (fs.existsSync(path.join(cwd, f))) return fw;
    }
  }
  // Fallback heuristics
  if (fs.existsSync(path.join(cwd, "package.json"))) {
    try {
      const pkg = JSON.parse(fs.readFileSync(path.join(cwd, "package.json"), "utf-8"));
      if (pkg.scripts?.test) return { name: "npm-test", command: "bun test", files: ["package.json"] };
    } catch { /* ignore malformed package.json */ }
  }
  return null;
}

// ── Output Parsing ──

interface TestReport {
  framework: string;
  passed: number;
  failed: number;
  skipped: number;
  duration: string;
  failures: Array<{ file: string; test: string; error: string }>;
  rawOutput: string;
}

function parseTestOutput(output: string, framework: string): TestReport {
  const report: TestReport = {
    framework,
    passed: 0,
    failed: 0,
    skipped: 0,
    duration: "",
    failures: [],
    rawOutput: output,
  };

  // Vitest/Jest: "Tests: 10 passed, 2 failed, 1 skipped (13)"
  const vitestRe = /Tests:\s*(\d+)\s+passed,\s*(\d+)\s+failed(?:,\s*(\d+)\s+skipped)?/;
  const vitestMatch = output.match(vitestRe);
  if (vitestMatch) {
    report.passed = parseInt(vitestMatch[1], 10);
    report.failed = parseInt(vitestMatch[2], 10);
    report.skipped = vitestMatch[3] ? parseInt(vitestMatch[3], 10) : 0;
  }

  // Vitest/Jest failures: "● testName" or "× testName"
  for (const m of output.matchAll(/[×✗●]\s+(.+)/g)) {
    report.failures.push({ file: "see output", test: m[1].trim(), error: "see raw output" });
  }
  // Vitest/Jest failure details: "FAIL src/file.ts > testName"
  for (const m of output.matchAll(/FAIL\s+(\S+)\s+>\s+(.+)/g)) {
    report.failures.push({ file: m[1], test: m[2].trim(), error: "see raw output" });
  }

  // Pytest: "= N failed, M passed ... in X.XXs ="
  const pyRe = /=\s*(\d+)\s+failed,\s*(\d+)\s+passed(?:,\s*(\d+)\s+skipped)?.*in\s+(\S+)/;
  const pyMatch = output.match(pyRe);
  if (pyMatch) {
    report.failed = parseInt(pyMatch[1], 10);
    report.passed = parseInt(pyMatch[2], 10);
    report.skipped = pyMatch[3] ? parseInt(pyMatch[3], 10) : report.skipped;
    report.duration = pyMatch[4];
  }

  // Go test: "--- FAIL: TestName"
  for (const m of output.matchAll(/^---\s+FAIL:\s+(\S+)/gm)) {
    report.failures.push({ file: "see output", test: m[1], error: "see raw output" });
  }

  // Cargo test: "test testname ... FAILED"
  for (const m of output.matchAll(/^test\s+(\S+)\s+\.\.\.\s+FAILED/gm)) {
    report.failures.push({ file: "see output", test: m[1], error: "see raw output" });
  }

  // Playwright: "N failed, M passed"
  const pwRe = /(\d+)\s+failed(?:,\s*(\d+)\s+passed)?/;
  const pwMatch = output.match(pwRe);
  if (pwMatch) {
    report.failed = parseInt(pwMatch[1], 10);
    if (pwMatch[2]) report.passed = parseInt(pwMatch[2], 10);
  }

  // Dedupe failures by test name
  const seen = new Set<string>();
  report.failures = report.failures.filter(f => {
    const key = `${f.file}:${f.test}`;
    if (seen.has(key)) return false;
    seen.add(key);
    return true;
  });

  return report;
}

// ── Extension Entry ──

export default function testRunner(pi: ExtensionAPI) {
  const { z } = pi.zod;

  pi.setLabel("omp-xox Test Runner v3.1");

  pi.registerTool({
    name: "run_tests",
    label: "Run Tests",
    description:
      "Auto-detect the project's test framework and run tests. Returns structured pass/fail/skip counts and failure details.",
    parameters: z.object({
      filter: z.string().optional().describe("Run only tests matching this pattern (file path or test name)"),
      cwd: z.string().optional().describe("Working directory (defaults to project root)"),
    }),
    async execute(_id, params, _signal, _onUpdate, _ctx) {
      const cwd = params.cwd ? path.resolve(params.cwd) : process.cwd();
      const framework = detectFramework(cwd);

      if (!framework) {
        return {
          content: [{ type: "text" as const, text: "No test framework detected. Supported: vitest, jest, mocha, playwright, pytest, go test, cargo test." }],
          details: { detected: false },
        };
      }

      let command = framework.command;
      // Sanitize filter: only allow alphanumeric, dash, underscore, dot, slash, colon
      if (params.filter) {
        const safe = String(params.filter).replace(/[^\w\-./:\\]/g, "").slice(0, 200);
        if (safe) command += ` -- ${safe}`;
      }
      // Use pi.exec() — returns { code, stdout, stderr, killed }
      const result = await pi.exec("sh", ["-c", command], { cwd, timeout: 120_000 });
      const output = (result.stdout ?? "") + "\n" + (result.stderr ?? "");

      const report = parseTestOutput(output, framework.name);
      const status = report.failed === 0 ? "PASSED" : "FAILED";

      const summary = [
        `## Test Results: ${status}`,
        `Framework: ${report.framework}`,
        `Passed: ${report.passed} | Failed: ${report.failed} | Skipped: ${report.skipped}`,
      ];

      if (report.failures.length > 0) {
        summary.push(`\n### Failures (${report.failures.length})`);
        for (const f of report.failures.slice(0, 10)) {
          summary.push(`- **${f.test}** (${f.file})`);
          if (f.error !== "see raw output") summary.push(`  \`\`\`\n  ${f.error.slice(0, 300)}\n  \`\`\``);
        }
        if (report.failures.length > 10) summary.push(`... and ${report.failures.length - 10} more failures.`);
      }

      return {
        content: [{ type: "text" as const, text: summary.join("\n") }],
        details: {
          framework: report.framework,
          passed: report.passed,
          failed: report.failed,
          skipped: report.skipped,
          status,
        },
      };
    },
  });
}
