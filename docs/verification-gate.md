# Verification Gate

Post-agent completion quality checks. Run before merging or after finishing a task.

## Tool: `run_verification`

| Parameter | Type | Default | Description |
|---|---|---|---|
| `checks` | array? | all 4 | Which checks to run |

### Checks

| Check | Critical | What it does |
|---|---|---|
| `test-pass` | ✅ Yes | Auto-detect test framework, run tests |
| `lint-pass` | No | Run `bun run lint` if configured |
| `no-new-todos` | No | Count `TODO`/`FIXME`/`HACK` markers, warn if > 10 |
| `diff-limit` | No | Check git diff size, warn if > 200 lines |

### Example Output

```markdown
## Verification: ISSUES FOUND
Results (3/4 passed):

- ✅ **test-pass**: bun test: all tests passed
- ⚠️ **lint-pass**: bun run lint: 12 errors found
- ✅ **no-new-todos**: 3 markers found — within threshold
- ✅ **diff-limit**: Diff: 45 lines — within limit
```

Critical failures block the gate; non-critical failures warn but pass.

## Command

| Command | Effect |
|---|---|
| `/verify` | Run all 4 checks and show results in notification |

## Technical

- All subprocess calls use `pi.exec()` — Bun-native, no `node:child_process`
- Framework auto-detection matches test-runner's detection logic
- Commands are hardcoded (not LLM-controlled) — no injection risk
- See `extensions/verification-gate/index.ts`
