---
description: Refactor code — change structure without changing behavior
argument-hint: scope or target
---

# Refactor

Refactor: $@. Use `/plan` before starting. Use `delegate(capability=refactor)` for large efforts.

## Workflow
1. `/plan` — analyze scope, identify dependencies, find all call sites
2. Run baseline: `run_tests` to confirm current state
3. `/plan-execute` — apply changes incrementally
4. After each change: `run_tests(filter=affected)`
5. Final gate: `run_verification`

## Safety Rules
- NEVER mix refactoring with feature changes
- Run tests before AND after every change
- Atomic commits per refactoring step
- Use LSP `rename` for symbols (not text replace)
- Read workspace-map for dependency graph

## Refactoring Patterns
- Extract function/variable for clarity
- Early return / guard clauses to reduce nesting
- Replace magic numbers with named constants
- Split large modules at natural boundaries
- Remove dead code, unused imports, unreachable branches
