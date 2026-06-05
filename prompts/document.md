---
description: Generate documentation for code
argument-hint: module, function, or project
---

# Document

Document: $@. Read workspace-map for module context. Use `delegate(capability=explore)` to gather information. Check `l2_fact(action=read)` for known environment details.

## Document Types

### API Reference
- Every exported symbol: parameters, return type, errors
- Code example for non-obvious behavior
- Mark deprecated with `@deprecated` and migration path

### Architecture Overview
- Module map: what lives where
- Data flow: inputs → process → outputs
- Key design decisions

### README / Guide
- What it does (one sentence)
- Quick start: install → configure → run
- Link to full docs

## Rules
- Explain WHY, not WHAT (code shows what)
- Keep examples minimal and runnable
- Link to related docs, don't duplicate
- After documenting: `crystallize_skill` to save doc templates
