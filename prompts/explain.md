---
description: Explain how code works at multiple levels
argument-hint: file, function, or concept
---

# Explain

Explain: $@. Read workspace-map for context. Use `delegate(capability=explore)` for broad searches. Check `l2_fact(action=read)` for known environment facts.

## Levels

### High-Level (architecture)
- What problem does this solve?
- Where does it fit in the overall system?
- Key design decisions and tradeoffs.

### Mid-Level (module/class)
- Public API surface: inputs, outputs, side effects.
- Internal state management.
- Dependencies and interactions.

### Low-Level (function/line)
- Step-by-step walkthrough of logic.
- Edge cases handled.
- Performance characteristics.

## Output Format
```
## Overview
<one-paragraph summary>

## Architecture / Design
<how it fits, key decisions>

## Detailed Walkthrough
<step-by-step, file:line references>

## Key Points
- <takeaway 1>
- <takeaway 2>
```
