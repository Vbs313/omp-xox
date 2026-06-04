// pi-xox v2: test-runner — Auto-detect test framework and execute tests
// Structured output with pass/fail parsing for common frameworks

import type { ExtensionAPI } from "@oh-my-pi/pi-coding-agent";
import { execSync } from "node:child_process";
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
    for (const file of fw.files) {
      if (fs.existsSync(path.join(cwd, file))) return fw;
    }
  }
  // Fallback heuristics
  if (fs.existsSync(path.join(cwd, "package.json"))) {
    try {
      const pkg = JSON.parse(fs.readFileSync(path.join(cwd, "package.json"), "utf-8"));
      if (pkg.devDependencies?.vitest || pkg.dependencies?.vitest) return FRAMEWORKS[0]; // vitest
      if (pkg.devDependencies?.jest || pkg.dependencies?.jest) return FRAMEWORKS[1]; // jest
      if (pkg.devDependencies?.mocha || pkg.dependencies?.mocha) return FRAMEWORKS[2]; // mocha
      if (pkg.scripts?.test) return { name: "npm-test", command: "bun run test", files: [] };
    } catch { /* ignore parse errors */ }
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

  // Vitest / Jest patterns
  if (framework === "vitest" || framework === "jest" || framework === "npm-test") {
    const testsMatch = output.match(/Tests\s+(\d+)\s+failed\s*\|\s*(\d+)\s+passed\s*(?:\|\s*(\d+)\s+skipped)?/i);
    if (testsMatch) {
      report.failed = parseInt(testsMatch[1], 10);
      report.passed = parseInt(testsMatch[2], 10);
      report.skipped = testsMatch[3] ? parseInt(testsMatch[3], 10) : 0;
    }
    // Alternative: ✓ N passed | ✗ M failed
    const altMatch = output.match(/(\d+)\s+passed.*?(\d+)\s+failed/);
    if (!testsMatch && altMatch) {
      report.passed = parseInt(altMatch[1], 10);
      report.failed = parseInt(altMatch[2], 10);
    }

    // Extract failures
    const failBlocks = output.split(/FAIL\s+/);
    for (let i = 1; i < failBlocks.length; i++) {
      const block = failBlocks[i];
      const fileMatch = block.match(/^(\S+)/);
      const testMatch = block.match(/[×✗]\s+(.+?)(?:\n|$)/);
      const errMatch = block.match(/Error:(.+?)(?:\n\n|\n\s+at|$)/s);
      report.failures.push({
        file: fileMatch?.[1] ?? "unknown",
        test: testMatch?.[1]?.trim() ?? "unknown",
        error: errMatch?.[1]?.trim() ?? "see raw output",
      });
    }
  }

  // Pytest patterns
  if (framework === "pytest") {
    const summary = output.match(/(\d+)\s+passed.*?(\d+)\s+failed.*?(\d+)\s+skipped/i)
      ?? output.match(/=+.*?(\d+)\s+passed.*?(\d+)\s+failed.*?(\d+)\s+\w+/);
    if (summary) {
      report.passed = parseInt(summary[1], 10);
      report.failed = parseInt(summary[2], 10);
      report.skipped = parseInt(summary[3], 10);
    }
    // Extract failures
    const failSections = output.split(/_+\s+FAILURES\s+_+/);
    if (failSections.length > 1) {
      const failText = failSections[1];
      const testFailures = failText.split(/_+\s+/);
      for (const tf of testFailures) {
        const lines = tf.trim().split("\n");
        if (lines.length > 1) {
          report.failures.push({
            file: lines[0]?.trim() ?? "unknown",
            test: lines[1]?.trim() ?? "unknown",
            error: lines.slice(2).join("\n").slice(0, 500),
          });
        }
      }
    }
  }

  // Go test patterns
  if (framework === "go-test") {
    const failMatches = output.match(/--- FAIL:\s+(.+?)\s+\(/g);
    if (failMatches) report.failed = failMatches.length;
    const passMatches = output.match(/--- PASS:\s+(.+?)\s+\(/g);
    if (passMatches) report.passed = passMatches.length;
    for (const fm of failMatches ?? []) {
      const name = fm.replace(/--- FAIL:\s+(.+?)\s+\(/, "$1");
      report.failures.push({ file: name.split("/")[0] ?? "unknown", test: name, error: "see raw output" });
    }
  }

  return report;
}

// ── Extension Entry ──

export default function testRunner(pi: ExtensionAPI) {
  const { z } = pi.zod;

  pi.setLabel("pi-xox Test Runner");

  pi.registerTool({
    name: "run_tests",
    label: "Run Tests",
    description:
      "Auto-detect the project's test framework and run tests. Returns structured pass/fail/skip counts and failure details.",
    parameters: z.object({
      filter: z.string().optional().describe("Run only tests matching this pattern (file path or test name)"),
      cwd: z.string().optional().describe("Working directory (defaults to project root)"),
    }),
    async execute(_id, params, _onUpdate, _signal) {
      const cwd = params.cwd ? path.resolve(params.cwd) : process.cwd();
      const framework = detectFramework(cwd);

      if (!framework) {
        return {
          content: [{ type: "text" as const, text: "No test framework detected. Supported: vitest, jest, mocha, playwright, pytest, go test, cargo test." }],
          details: { detected: false },
        };
      }

      let command = framework.command;
      if (params.filter) command += ` -- ${params.filter}`;

      let output: string;
      try {
        output = execSync(command, { cwd, encoding: "utf-8", maxBuffer: 20 * 1024 * 1024, timeout: 120000 }).trim();
      } catch (e: unknown) {
        // Tests failed — still capture output
        const err = e as { stdout?: string; stderr?: string };
        output = (err.stdout ?? "") + "\n" + (err.stderr ?? "");
      }

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
