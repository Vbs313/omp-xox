---
name: refactoring
description: Safe refactoring with before/after verification. TRIGGERS: refactor, refactor code, clean up, improve code, restructure, extract method
---

# Refactoring Skill

Safe refactoring with before/after verification.

## When to Use

Use this skill when asked to:
- Improve code structure without changing behavior
- Extract a method, class, or module from existing code
- Rename symbols for clarity
- Reduce duplication
- Simplify complex conditionals
- Migrate from one pattern to another

## Principles

1. **Refactoring does NOT change behavior.** If behavior changes, it is not refactoring, it is a feature change or a bug fix.
2. **Tests are your safety net.** Never refactor without a passing test suite.
3. **One change at a time.** Small, reversible steps reduce risk.
4. **The code should be cleaner after each step.** If it is not cleaner, undo and try a different approach.

## Workflow

### 1. Analyze

- **What needs to change?** Identify the specific code smell: long method, duplicated code, large class, shotgun surgery, primitive obsession, etc.
- **What are the dependencies?** Find all callers, consumers, and tests for the code being refactored.
- **Is there a clear goal?** State the desired outcome before starting.

### 2. Lock Behavior With Tests

Before any refactoring:

- Run the existing test suite. It must be green.
- If tests are missing for the code being changed, write **characterization tests** that pin current behavior.
- These tests capture the exact inputs and outputs so you know when behavior has drifted.

### 3. Plan the Refactoring

Break the refactoring into small, reversible steps. Each step should:

- Be completable in a few minutes.
- Keep the tests green at every intermediate state.
- Be independently reviewable.

Example plan for "extract method":

1. Identify the lines to extract and their local variables.
2. Create the new method with those variables as parameters.
3. Replace the original code with a call to the new method.
4. Run tests to confirm.

### 4. Execute Each Step

For each step:

1. Make the change.
2. Run the tests. If they fail, **undo** (do not fix forward — the step was too big).
3. Commit if using version control.

### 5. Verify

- The full test suite is green.
- The code is measurably cleaner (fewer lines, less nesting, better names).
- No behavior drift: characterization tests still pass with identical output.
- Run any linters or formatters used by the project.

## Common Refactoring Patterns

| Pattern | When to Use |
|---------|-------------|
| **Extract Method** | A method is too long or has a clear sub-step |
| **Rename** | A name is misleading or unclear |
| **Extract Class** | A class has multiple responsibilities |
| **Introduce Parameter Object** | Many methods share the same parameter group |
| **Replace Conditional with Polymorphism** | Complex conditionals that dispatch on type |
| **Extract Module** | A file has grown too large and has natural sections |
| **Inline** | A method is trivial and only called in one place |

## Scripts

No scripts for this skill. Verification relies on the project's existing test suite.
