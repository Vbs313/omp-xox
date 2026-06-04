---
name: debugging
description: Structured debugging workflow for finding and fixing bugs. TRIGGERS: debug, fix bug, find bug, troubleshoot, error, crash, exception
---

# Debugging Skill

Structured debugging workflow for finding and fixing bugs.

## When to Use

Use this skill when asked to:
- Debug a failing test or broken feature
- Investigate a crash, error, or exception
- Troubleshoot unexpected behavior
- Fix a reported bug

## Workflow

### 1. Reproduce

Before fixing anything, confirm the bug exists and understand the trigger.

- **What input causes the failure?** Get a minimal reproduction.
- **What is the expected output?** Define correct behavior.
- **What actually happens?** Capture the error message, stack trace, or wrong output.
- **Is it deterministic or intermittent?** If intermittent, look for race conditions, timing, or state leaks.

### 2. Isolate

Narrow down where the bug lives.

- **Binary search**: Cut the code in half. Does the bug still reproduce? Halve again.
- **Simplify inputs**: Reduce input data to the smallest case that still triggers the bug.
- **Check assumptions**: Add assertions or log statements at key points. Do values match expectations?
- **Examine the call stack**: What path led to the failure? Check all frames.
- **Use the log analyzer** for parsing log files:
  ```bash
  bash skills/debugging/scripts/log-analyzer.sh <log-file>
  ```

### 3. Hypothesize

Form a clear theory of the root cause.

- State it in one sentence: "The bug is that when X happens, Y is null because Z was never initialized."
- If you cannot state the root cause clearly, you have not finished isolating.

### 4. Fix

Write the minimal change that addresses the root cause.

- Do not fix symptoms. Fix the root cause.
- Do not add unrelated refactoring or features.
- Write or update a test that would have caught this bug.

### 5. Verify

- Run the reproduction case. Does it pass now?
- Run the full test suite. Did anything break?
- Revert your fix temporarily and confirm the bug returns (proving your fix is necessary).
- Check adjacent code for the same pattern of bug.

## Log Analysis

The `scripts/log-analyzer.sh` script can parse log files, extract stack traces, error frequencies, and timestamps.

```bash
bash scripts/log-analyzer.sh path/to/app.log
```

## Anti-Patterns

| Trap | Why It Fails |
|------|-------------|
| Changing code before reproducing | You might fix a symptom, not the cause |
| Fixing multiple things at once | You won't know which change fixed it |
| Skipping the test update | The same bug may re-appear silently |
| Assuming without checking | Check the actual values, don't guess |

## Scripts

- `scripts/log-analyzer.sh` — Parse log files for errors, stack traces, and patterns.
