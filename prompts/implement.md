---
description: Implement a new feature or change
argument-hint: feature description
---

# Implement

Implement: $@. Use `/plan` for analysis before code. Use `delegate(capability=implement)` for complex features. Use `set_checkpoint(note)` during long tasks.

## Workflow
1. **Plan** — `/plan` to analyze and produce plan. Read `l1_insight(action=read)` for relevant existing skills.
2. **Execute** — `/plan-execute`. Write tests first, then implementation.
   - `set_checkpoint("Tests written, starting implementation", status=in_progress)`
3. **Verify** — `run_tests(filter=new_tests)`, then `run_verification`.
4. **Evolve** — `crystallize_skill` to save the implementation pattern for future reuse.
5. **Archive** — `distill_session(summary="...", learnings=[...], tags=[...])` to preserve session knowledge.

## Rules
- One feature per session. Don't mix unrelated changes.
- Write tests before or alongside implementation.
- Follow existing patterns in the codebase. Don't invent new patterns.
- Update docs, types, and config alongside code changes.
- Use LSP `rename` for symbol changes (not text replace).
