---
name: omp-xox-release
description: Release workflow: audit, verify, tag, publish. Use for omp-xox development only.
---

# omp-xox Release

Full release pipeline for omp-xox itself. Use `distill_session` to archive release notes.

## Workflow

1. **Audit** — review all modules against OMP docs for redundancy. Use `delegate(capability=review)`.
2. **Plan** — `/plan` to analyze changes without touching files
3. **Implement** — `/plan-execute` to apply changes. `set_checkpoint("Added X module", status=in_progress)`
4. **Verify** — `run_verification` run all 4 checks
5. **Test** — `run_tests` on the extension pack
6. **Evolve** — `crystallize_skill` to save release patterns
7. **Archive** — `distill_session(summary="omp-xox vX.Y.Z released", learnings=[...], tags=["omp-xox", "release"])`
8. **Release** — git tag, push, update marketplace

## Module Checklist (per module)

- [ ] `index.ts` imports resolve correctly
- [ ] Hook registration order matches docs/architecture.md
- [ ] `docs/<module>.md` exists and accurate
- [ ] `l1_insight` updated if new keywords needed
- [ ] `AGENTS.md` updated with module count and inventory
- [ ] No `node:child_process` imports (`pi.exec()` only)
- [ ] `execute` signature: 5 params `(id, params, signal, onUpdate, ctx)`
- [ ] Context injection guarded (injected flag or user-triggered only)

## Post-Release

- Update `AGENTS.md`
- Update `docs/architecture.md`
- `distill_session` to archive
