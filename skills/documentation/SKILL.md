---
name: documentation
description: Generate documentation: README, API docs, architecture docs, inline comments.
---

# Documentation

Use workspace-map for module context. Use `delegate(capability=implement)` for large doc generation. Use `crystallize_skill` to save documentation templates.

## Document Types

### API Documentation
- Every exported function/class/interface: parameters, return type, errors thrown
- Include code examples where behavior isn't obvious
- Mark deprecated items with `@deprecated` and migration path

### Architecture Documentation
- Module map: what lives where, responsibility boundaries
- Data flow: inputs → processing → outputs → storage
- Key design decisions and tradeoffs

### README / Getting Started
- What the project does (one sentence)
- Quick start: install → configure → run
- Prerequisites and dependencies
- Link to full docs

### Inline Comments
- Explain WHY, not WHAT (code shows what)
- Document assumptions, edge cases, known limitations
- Mark hacks/workarounds with `// HACK:` and reason

## Workflow

1. **Read workspace-map** for module layout
2. **Read key files** — entry points, config, public API surfaces
3. **Check L2 facts** — `l2_fact(action=read)` for known environment details
4. **Write docs** — one doc type at a time
5. **Evolve** — `crystallize_skill` to save doc templates
