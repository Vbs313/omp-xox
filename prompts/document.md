---
description: Generate documentation for code
argument-hint: target and format
---

# Document

Generate documentation for $@.

## Target

Identify what we are documenting:

- **API / Endpoint** - Request/response schemas, auth, error codes, example calls.
- **Function / Module** - Purpose, parameters, return value, side effects, usage example.
- **Configuration** - Each option, its type, default, and effect.
- **Architecture** - Components, data flow, assumptions, tradeoffs.

## Content Rules

- Start with *what* and *why*. The *how* comes second.
- One concept per section. Short paragraphs.
- Include a minimal working example that the reader can copy-paste.
- Document gotchas and non-obvious behavior explicitly.
- Use relative links to reference other parts of the project.

## Format

- Follow the existing documentation style in the project.
- Use code blocks with language tags for all code examples.
- Keep line lengths readable. Use lists for enumerations.
- Mark deprecated or experimental features clearly.

## Review

- Does the doc answer the questions a new user would have?
- Can you understand the interface without reading the implementation?
- Remove filler phrases. Every sentence should carry information.
