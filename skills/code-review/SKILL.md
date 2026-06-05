---
name: code-review
description: Systematic code review for quality, security, performance, and style.
---

# Code Review

Systematic review before merging. Use `delegate(capability=review)` for deep reviews on large diffs.

## Workflow

1. **Understand context**: Read diff or full files. Check workspace-map for surrounding code.
2. **Review checklist** (in order):

### Correctness
- Does it do what it claims? Logic errors, off-by-one, race conditions?
- All branches handled? Error paths covered?

### Security
- User inputs validated/sanitized? Injection vulnerabilities?
- Secrets hardcoded? Use environment variables.
- Authentication/authorization checked on protected paths?

### Performance
- N+1 queries? Unnecessary loops?
- Memory issues with large datasets?
- Blocking calls in async/hot paths?

### Maintainability
- Follows project conventions? Reasonable function size?
- Duplicated code? Descriptive names?

### Testing
- Tests for new code? Edge cases covered?
- Test names descriptive?

## Output Format

```
## Review: <scope>

### BLOCKER — Must fix before merge
- **file:line** — problem → fix

### MAJOR — Should fix
- **file:line** — problem → suggestion

### MINOR — Nice to fix
- **file:line** — suggestion

### PRAISE — Well done
- description
```
