---
name: code-review
description: Systematic code review for quality, security, performance, and style.
---

# Code Review

Systematic review before merging. Use `delegate(capability=review)` for deep reviews on large diffs. After review, call `crystallize_skill` if you discovered reusable review patterns.

## Workflow

1. **Understand context**: Read diff or full files. Check `l1_insight(action=read)` for related skills.
2. **Review checklist** (in order):

### Correctness
- Does it do what it claims? Logic errors, off-by-one, race conditions?
- All branches handled? Error paths covered?

### Security
- User inputs validated/sanitized? Injection vulnerabilities?
- Secrets hardcoded? Use environment variables.
- Auth checked on protected paths?

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

3. **Evolve**: If you discovered a systematic issue pattern, call `crystallize_skill(name="review-pattern-X", description="...", task="...", patterns="...")` to save it for future sessions.

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
