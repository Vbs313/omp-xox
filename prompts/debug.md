---
description: Debug bugs, crashes, or unexpected behavior
argument-hint: bug description
---

# Debug

Debug: $@. Use `run_tests(filter=...)` to isolate. Use `auto_repair(command, maxCycles=2)` for test-fix loops.

## Steps
1. **Reproduce** — exact inputs, reliable failure?
2. **Isolate** — narrow to minimal repro. Which file/function?
3. **Fix** — minimal change, one bug per fix.
4. **Verify** — `run_tests(filter=affected)` then `run_verification`.

## Investigation
- Read traceback: file, line, error message
- Check surrounding context: state before failure
- Consider: race conditions, async ordering, env differences
- Check git log: when was this code last changed?

## Output
```
## Root Cause
file:line — <explanation>

## Fix
<code change>

## Verification
<test results>
```
