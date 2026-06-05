---
name: test-generation
description: Generate tests with coverage analysis and edge case detection.
---

# Test Generation

Use `run_tests` to detect framework and run existing tests. Use `auto_repair` to fix failures. Use `crystallize_skill` to save test patterns.

## Workflow

1. **Detect framework** — `run_tests` auto-detects
2. **Analyze target** — read the file to test, identify public API surfaces
3. **Generate tests** — one test file per source file. `set_checkpoint("Generated tests for X, running verification", status=in_progress)`
4. **Run** — `run_tests(filter=new_test_file)`
5. **Fix** — `auto_repair(command, maxCycles=2)` if tests fail
6. **Evolve** — `crystallize_skill` for reusable test patterns (mocking strategies, edge case templates)

## Test Categories

### Unit Tests
- Test one function/class in isolation
- Mock external dependencies
- Cover: happy path, edge cases, error paths

### Integration Tests
- Test multiple components together
- Real (or realistic) dependencies
- Cover: cross-component data flow, error propagation

## Edge Cases Checklist
- Empty input (null, undefined, "", [], {})
- Boundary values (0, -1, MAX_INT, empty string)
- Concurrent access (if applicable)
- Error conditions (network failure, file not found, permission denied)
- Invalid input (wrong type, malformed data, injection attempts)

## Coverage Targets
- Critical path code: 90%+
- Utility functions: 80%+
- UI/rendering: snapshot tests
- Error handling: 100% (every error path tested)
