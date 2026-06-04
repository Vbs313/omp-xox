---
description: Refactor code safely with verification
argument-hint: target and goal
---

# Refactor

Refactor $@. Work in small, reversible steps.

## 1. Characterize

Before changing anything, understand the current behavior:

- Read the code. Map inputs to outputs and side effects.
- Check for existing tests. If tests are sparse, write characterization tests that pin down current behavior.
- Note any implicit contracts: argument order, mutation patterns, return value guarantees.

## 2. Plan

- State the goal clearly: what improves and what stays the same.
- Break the refactor into atomic steps. Each step must keep the code working.
- Identify risk areas: shared state, complex conditionals, tight coupling.

## 3. Execute

One step at a time. After each step:

- Run the tests (existing + characterization). They must all pass.
- Check for regressions manually if coverage is thin.
- Commit or stage the step so you can revert if needed.

## 4. Verify

- Run the full test suite.
- Check that the public API and behavior are unchanged.
- Remove characterization tests if they duplicated existing coverage.
- Review the diff. Is the result cleaner than what you started with?

## Stop Conditions

- If a step requires changing behavior, stop. File a separate issue.
- If a step grows beyond 50 lines, split it.
- If tests break and the fix is not obvious, roll back the step.
