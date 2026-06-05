---
name: refactoring
description: Safe refactoring: plan, execute, verify. Behavior-preserving changes.
---

# Refactoring

Use `/plan` before starting. Use `run_verification` after finishing. Use `delegate(capability=refactor)` for large efforts. Use `set_checkpoint(note, status=in_progress)` to track each step.

## Workflow

1. **Plan** — `/plan` to analyze scope without touching files
2. **Understand** — `l1_insight(action=read)` for existing patterns, workspace-map for module boundaries, `run_tests` for baseline
3. **Execute** — `/plan-execute`, apply changes incrementally. `set_checkpoint("Extracted X to helper", status=in_progress)` after each step
4. **Verify** — `run_tests` after each change, `run_verification` as final gate
5. **Evolve** — `crystallize_skill` to save successful refactoring patterns

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

## Safety Rules
- **Never mix refactoring with feature changes.**
- **Run tests before and after.**
- **Commit small, revert easy.** Atomic commits per step.
- **Use LSP for renames.**
