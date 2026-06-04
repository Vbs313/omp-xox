---
name: test-generation
description: Generate comprehensive test suites for code. TRIGGERS: test, generate tests, write tests, unit test, integration test, test coverage
---

# Test Generation Skill

Generate comprehensive test suites for code.

## When to Use

Use this skill when asked to:
- Write unit tests for a function, class, or module
- Generate integration tests for API endpoints or services
- Increase test coverage
- Create test fixtures or mock data
- Set up testing infrastructure for a new project

## Workflow

### 1. Detect the Test Framework

Run the detection script to identify which testing framework the project uses:

```bash
bash skills/test-generation/scripts/detect-framework.sh /path/to/project
```

This checks for Jest, Mocha, Vitest, pytest, unittest, Go test, cargo test, and others.

### 2. Analyze the Code Under Test

- **What does the code export?** List public functions, classes, and interfaces.
- **What are the inputs and outputs?** Understand types, ranges, and edge cases.
- **What are the dependencies?** Identify mocks or stubs needed.
- **What are the side effects?** File I/O, network calls, database writes, global state.

### 3. Plan Test Cases

Cover these categories for every function or module:

| Category | Example |
|----------|---------|
| **Happy path** | Valid inputs produce expected output |
| **Edge cases** | Empty input, max values, null/undefined, boundary conditions |
| **Error handling** | Invalid input raises expected exception / returns error |
| **State changes** | Mutable objects modified correctly |
| **Idempotency** | Running twice gives same result |

### 4. Generate Tests

For each test case, write:

- A descriptive name: `describe('functionName')` + `it('returns X when given Y')`
- Arrange: set up inputs, mocks, and state
- Act: call the function under test
- Assert: check the result matches expectations

### 5. Verify

- Run the test suite. All new tests should pass.
- Run coverage to identify missed branches.
- Run existing tests to confirm no regressions.

## Project Conventions

- Place tests next to source files (`src/foo.ts` → `src/foo.test.ts`) or in a `__tests__/` or `tests/` directory.
- Match the project's existing test framework and configuration.
- Use the project's existing mock/stub patterns rather than introducing new ones.

## Scripts

- `scripts/detect-framework.sh` — Detect which test framework a project uses.
