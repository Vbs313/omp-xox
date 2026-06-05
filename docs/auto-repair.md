# Auto Repair

Test-failure → fix → retry loop. The LLM calls `auto_repair(command)`, we run the tests, parse failures, and return a structured failure report. The LLM then fixes the code and calls `auto_repair` again.

Cline equivalent: "heal mode".

## Tool: `auto_repair`

### Parameters

| Parameter | Type | Default | Description |
|---|---|---|---|
| `command` | string | required | Test command (e.g. `bun test`, `pytest tests/`) |
| `maxCycles` | number? | 3 | Max fix cycles (1-5) |

### Security

Command is validated before execution:
- `/[;&|\`$(){}\[\]<>]/` — reject shell metacharacters (prevents chaining/redirection)
- Max 500 chars
- Only simple test runner commands pass validation

### Flow

```text
LLM: auto_repair("bun test", maxCycles=3)
    │
    ├─ Validate command (no shell meta)
    ├─ Cycle 1: run tests → FAIL
    │   ├─ Extract 5 failures
    │   └─ Return failure report
    │
    ▼
LLM reads failures, calls delegate(fix) to fix them
    │
    ▼
LLM: auto_repair("bun test")  [cycle 2]
    │
    ├─ Cycle 2: run tests → FAIL (2 remaining)
    │   └─ Return failure report
    │
    ▼
LLM fixes remaining, calls auto_repair again
    │
    ▼
LLM: auto_repair("bun test")  [cycle 3]
    │
    └─ Cycle 3: run tests → ✅ ALL TESTS PASSED
```

### Failure Extraction

Parses failure signatures from:
- Vitest/Jest: `FAIL src/file.ts`, `● testName`
- Pytest: `FAIL: test_name`, `ERROR: test_name`
- Go: `--- FAIL: TestName`
- Rust: `test test_name ... FAILED`
- Generic: `file.ts:42: error`

### Example Result

```markdown
❌ Auto-repair failed after 3 cycle(s)

[CYCLE 1] 5 failure(s) detected:
  - FAIL src/utils.test.ts
  - test failure: should handle edge case
  - src/api.test.ts:42
  → Fix these failures, then call auto_repair again to re-test.

[CYCLE 2] 2 failure(s) detected:
  - FAIL src/api.test.ts
  ...

[CYCLE 3] Tests failed (exit 1) but no parseable errors found.
```

## Technical

- Uses `pi.exec("sh", ["-c", command])` — Bun-native
- 120s timeout per test run
- Does NOT auto-delegate fixes — returns report and lets LLM decide
- See `extensions/auto-repair/index.ts`
