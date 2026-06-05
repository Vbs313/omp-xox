# Dev Tools

Test runner with framework auto-detection and structured output parsing. Only module remaining from v2 dev-tools (git-ops and safe-edit removed as redundant with OMP's bash/edit tools).

## Tool: `run_tests`

Auto-detects the project's test framework and runs tests. Returns pass/fail/skip counts and failure details.

### Parameters

| Parameter | Type | Description |
|---|---|---|
| `filter` | string? | Run only tests matching this pattern (file path or test name) |
| `cwd` | string? | Working directory (defaults to project root) |

### Security

`filter` parameter is sanitized: only `\w`, `-`, `.`, `/`, `:`, `\` allowed. Shell metacharacters stripped. Max 200 chars.

### Supported Frameworks

| Framework | Detection | Command |
|---|---|---|
| Vitest | `vitest.config.{ts,js,mjs}` | `bun test` |
| Jest | `jest.config.{ts,js,mjs}` | `bun test` |
| Mocha | `.mocharc.{js,json,yml}` | `bun test` |
| Playwright | `playwright.config.{ts,js}` | `bunx playwright test` |
| Pytest | `pytest.ini`, `pyproject.toml` | `python -m pytest` |
| Go | `go.mod` | `go test ./...` |
| Rust | `Cargo.toml` | `cargo test` |

### Output Parsing

Parses test output from all supported frameworks:
- Vitest/Jest: `Tests: N passed, M failed`
- Pytest: `= N failed, M passed in Xs =`
- Go: `--- FAIL: TestName`
- Rust: `test testname ... FAILED`
- Playwright: `N failed, M passed`

### Example Result

```markdown
## Test Results: FAILED
Framework: vitest
Passed: 42 | Failed: 3 | Skipped: 1

### Failures (3)
- **should handle edge case** (src/utils.test.ts)
- **validates input** (src/api.test.ts)
- **timeout on large dataset** (src/batch.test.ts)
```

## Technical

- Uses `pi.exec("sh", ["-c", command])` — Bun-native, no `node:child_process`
- 120s timeout per run, 20MB output buffer
- See `extensions/dev-tools/test-runner.ts`
