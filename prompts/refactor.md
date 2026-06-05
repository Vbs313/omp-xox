---
description: Refactor code — change structure without changing behavior
argument-hint: scope or target
---

# Refactor

Refactor: $@. Use `/plan` before starting. Use `delegate(capability=refactor)` for large efforts. Use `set_checkpoint(note)` to track each step.

## Workflow
1. `/plan` — analyze scope, identify dependencies, find all call sites
2. Run baseline: `run_tests` to confirm current state. `l1_insight(action=read)` for related skills.
3. `/plan-execute` — apply changes incrementally. `set_checkpoint("Extracted X", status=in_progress)` after each step.
4. After each change: `run_tests(filter=affected)`
5. Final gate: `run_verification`
6. Evolve: `crystallize_skill` to save refactoring patterns

## Safety Rules
- NEVER mix refactoring with feature changes
- Run tests before AND after every change
- Atomic commits per refactoring step
- Use LSP `rename` for symbols (not text replace)
