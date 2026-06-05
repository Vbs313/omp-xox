---
name: debugging
description: Systematic debugging: reproduce, isolate, fix, verify.
---

# Debugging

Use `auto_repair(command)` to loop test→fix→retest. Use `run_tests` to verify fixes. Use `set_checkpoint(note, status=in_progress)` to track progress during long debug sessions.

## Workflow

1. **Reproduce** — what exact inputs trigger the bug? Can you make it fail reliably?
2. **Isolate** — narrow to smallest possible reproduction. Which module/function is the culprit?
   - `set_checkpoint("Reproduced bug in X, narrowing to function Y", status=in_progress)`
3. **Fix** — make the minimal change. One bug per fix.
4. **Verify** — run tests with `run_tests(filter=affected_file)`. Run `run_verification` for full check.
5. **Evolve** — call `crystallize_skill` to save the fix pattern for future similar bugs.

## Investigation Patterns

### Crashes / Exceptions
- Read the traceback: file, line, error message
- Check surrounding context: what state led here?
- Add defensive checks if root cause is unexpected input

### Incorrect Output
- Trace the data through the pipeline: input → transform → output
- Check edge cases: empty, null, boundary, concurrent
- Compare against expected: golden file, snapshot, known-good version

### Performance
- Profile: where is time spent?
- Check for: N+1 queries, unbounded loops, blocking calls
- Measure before/after

### Heisenbugs (intermittent)
- Race conditions? Check shared mutable state
- Async ordering? Promise.all vs sequential
- Environment differences? Record facts with `l2_fact(action=add, key="env", value="...")`

## Key Tools

| Tool | Use |
|---|---|
| `run_tests(filter=...)` | Run specific test file or pattern |
| `auto_repair(command, maxCycles=3)` | Test→fix→retest loop |
| `run_verification` | Full quality check after fix |
| `delegate(capability=fix)` | Delegate to fix sub-agent |
| `set_checkpoint(note, status=in_progress)` | Track debug progress |
| `crystallize_skill` | Save fix pattern for future |
