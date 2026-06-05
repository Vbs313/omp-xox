---
name: omp-xox-release
description: Release workflow: audit, verify, tag, publish. Use for omp-xox development only.
---

# omp-xox Release

Full release pipeline for omp-xox itself.

## Workflow

1. **Audit** — review all modules against OMP docs for redundancy. Use `delegate(capability=review)`.
2. **Plan** — `/plan` to analyze changes without touching files
3. **Implement** — `/plan-execute` to apply changes
4. **Verify** — `run_verification` run all 4 checks
5. **Test** — `run_tests` on the extension pack
6. **Release** — git tag, push, update marketplace

## Module Checklist (per module)

- [ ] `index.ts` imports resolve correctly
- [ ] Hook registration order matches docs/architecture.md
- [ ] `docs/<module>.md` exists and accurate
- [ ] `skills/` entries reference module if relevant
- [ ] `AGENTS.md` updated with module count and inventory
- [ ] No `node:child_process` imports (`pi.exec()` only)
- [ ] No `xhigh` thinking level (`high` only)
- [ ] `execute` signature: 5 params `(id, params, signal, onUpdate, ctx)`
- [ ] Context injection guarded (injected flag or user-triggered only)

## Post-Release

- Update `AGENTS.md`
- Update `docs/architecture.md`
- Archive release notes to knowledge base
