# Verification Gate

## Overview

Post-agent completion quality checks. Runs after subagent completes via `run_verification` tool.

## File

`extensions/verification-gate/index.ts`

## Check Types

| Check | Critical | Behavior |
|-------|----------|----------|
| test-pass | Yes | Runs: bun test → npm test → pytest → go test → cargo test |
| lint-pass | No | Runs: bun run lint (if configured in package.json) |
| no-new-todos | No | Counts TODO/FIXME/HACK markers (threshold: 10) |
| diff-limit | No | Checks git diff size (threshold: 200 lines) |

## Tool

### `run_verification`

```
Parameters:
  checks?: string[]   — Which checks to run (default: all four)

Output:
  ## Verification: PASSED|FAILED
  - ✓ test-pass: all tests passed
  - ✓ lint-pass: clean
  - ⚠ no-new-todos: 3 markers — within threshold
  - ✓ diff-limit: 42 lines — within limit
```

## Integration

Exposes checker via `pi.__piXoxVerify` for other extensions. The `delegate` tool runs verification checks after sub-agent completion (if the agent contract declares `verification` fields). Results are included in the delegation output.

## Slash Command

`/verify`
