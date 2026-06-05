---
name: documentation
description: Generate documentation: README, API docs, architecture docs, inline comments.
---

# Documentation

Use workspace-map for module context. Use `delegate(capability=implement)` for large doc generation.

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
3. **Write docs** — one doc type at a time
4. **Verify** — does a new team member understand from these docs?

## Output Format

```
## Documentation: <scope>

### Files Created/Modified
- path/to/doc.md — brief summary

### Content Summary
- what was documented and why
```
