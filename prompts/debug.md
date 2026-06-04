---
description: Debug an issue with systematic analysis
argument-hint: error description or file
---

# Debug

Investigate this issue systematically: $@

## 1. Reproduce

- What are the exact steps to trigger the bug? Pin down inputs, state, environment.
- Does it happen consistently or intermittently? If intermittent, what varies?

## 2. Isolate

- What is the expected behavior vs actual behavior?
- Narrow the scope. Binary search: comment out halves of the code until the bug disappears.
- Check assumptions. Is the data what you think it is? Log or dump the relevant values.

## 3. Root Cause

- Trace the call path from entry point to failure.
- What changed recently? Check git log for the last commits touching this area.
- Look at the error message or stack trace carefully. Each frame is a clue.

## 4. Fix

- Propose the smallest change that addresses the root cause.
- Check that the fix does not break adjacent functionality.
- Add a regression test that would catch this if it reappears.

## 5. Verify

- Run the reproduction steps against the fix. Confirm the bug is gone.
- Run the full test suite.
- Document the root cause and fix in the commit message.
