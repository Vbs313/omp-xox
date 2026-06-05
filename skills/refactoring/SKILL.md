---
name: refactoring
description: Safe refactoring: plan, execute, verify. Behavior-preserving changes.
---

# Refactoring

Use `/plan` before starting. Use `run_verification` after finishing. Use `delegate(capability=refactor)` for large efforts.

## Workflow

1. **Plan** — `/plan` to analyze scope without touching files
2. **Understand** — workspace-map for module boundaries, `run_tests` for baseline
3. **Execute** — `/plan-execute`, apply changes incrementally
4. **Verify** — `run_tests` after each change, `run_verification` as final gate

## Refactoring Types

### Extract Function/Method
- Identify coherent block of code
- Extract to named function with clear inputs/outputs
- Replace original with call

### Rename
- Use LSP `rename` (not text replace) for symbols
- Update imports, call sites, docs, configs
- Check for string references (API routes, config keys)

### Reduce Nesting
- Early return / guard clauses
- Extract nested conditionals to named predicates
- Flatten callbacks to async/await

### Remove Duplication
- Find identical or near-identical code blocks
- Extract to shared function/module
- Parameterize the differences

### Split Large Module
- Identify natural boundaries (by responsibility, by domain)
- Move code incrementally, keeping tests passing
- Update imports across codebase

## Safety Rules

- **Never mix refactoring with feature changes.** One type of change per commit.
- **Run tests before and after.** If tests didn't pass before, fix that first.
- **Commit small, revert easy.** Atomic commits per refactoring step.
- **Use LSP for renames.** Text replace misses shadowing and re-exports.
