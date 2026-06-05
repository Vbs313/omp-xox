---
description: Generate tests with edge case coverage
argument-hint: file or module
---

# Generate Tests

Generate tests for: $@. Use `run_tests` to detect framework. Use `auto_repair(command, maxCycles=2)` if generated tests fail.

## Workflow
1. `run_tests` — detect framework, confirm baseline
2. Read target file — identify all exported symbols
3. Generate tests — one test file covering all public APIs
4. `run_tests(filter=new_file)` — verify
5. `auto_repair(command)` — fix failures in loop
6. `crystallize_skill` — save test patterns for reuse

## Coverage Checklist
Per function/method:
- [ ] Happy path (normal input → expected output)
- [ ] Edge cases (empty, null, boundary, max)
- [ ] Error paths (invalid input, missing deps, timeout)
- [ ] Async/eventual consistency (if applicable)

## Test Pattern
```
describe("<unit>", () => {
  it("should <behavior> when <condition>", () => {
    // arrange → act → assert
  });
});
```

## Coverage Targets
- Critical path: 90%+
- Utilities: 80%+
- Error handling: 100%
