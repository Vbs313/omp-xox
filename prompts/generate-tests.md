---
description: Generate comprehensive test cases
argument-hint: target file or function
---

# Generate Tests

Generate tests for $@. Follow this structure:

## Test Plan

List the scenarios before writing any code:

- **Happy path**: Normal inputs produce expected output.
- **Edge cases**: Empty input, max/min values, boundary conditions.
- **Error cases**: Invalid input, missing dependencies, network failures.
- **State transitions**: If stateful, test each state and transition.

## Per Scenario

For each scenario, produce:

1. **Setup** - Arrange the test fixtures, mocks, and preconditions.
2. **Action** - The single operation under test.
3. **Assertion** - Check the result, side effects, and that nothing else changed.

## Style

- Use the project's existing test framework and conventions.
- Name tests descriptively: `$behavior_$condition_$expected`.
- One logical assertion per test. Use descriptive assertion messages.
- Prefer realistic data over dummy values.

## Coverage

- Aim for statement coverage, branch coverage, and edge case coverage.
- Run the tests after writing. Verify all pass.
- If the code is hard to test, suggest refactoring for testability.
