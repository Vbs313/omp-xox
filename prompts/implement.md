---
description: Implement a new feature or change
argument-hint: feature description
---

# Implement

Implement: $@. Use `/plan` for analysis before code. Use `delegate(capability=implement)` for complex features.

## Workflow
1. **Plan** — `/plan` to analyze and produce plan. Read workspace-map for relevant modules.
2. **Execute** — `/plan-execute`. Write tests first, then implementation.
3. **Verify** — `run_tests(filter=new_tests)`, then `run_verification`.

## Rules
- One feature per session. Don't mix unrelated changes.
- Write tests before or alongside implementation.
- Follow existing patterns in the codebase. Don't invent new patterns.
- Update docs, types, and config alongside code changes.
- Use LSP `rename` for symbol changes (not text replace).

## Output
```
## Plan
- Files to create/modify
- Implementation approach
- Testing strategy

## Implementation
<code changes with file:line references>

## Verification
<test results>
```
