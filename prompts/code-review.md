---
description: Review code for quality, bugs, and improvements
argument-hint: file or scope
---

# Code Review

Review $@. Use `delegate(capability=review)` for deep review on large diffs.

## Correctness
- Does it do what it claims? Logic errors, off-by-one, race conditions.
- Edge cases handled? Empty, null, boundary, concurrent.
- Error paths covered? Exceptions caught, resources cleaned up.

## Security
- Inputs validated/sanitized? Injection vulnerabilities?
- Secrets hardcoded? Use environment variables.
- Auth checked on protected paths?

## Readability
- Names reveal intent? Variables, functions, classes.
- Flow easy to follow? Avoid deep nesting, complex conditionals.
- Comments explain WHY, not WHAT.

## Maintainability
- DRY? Repeated logic extracted.
- Single responsibility? Modules focused.
- Dependencies explicit and minimal?

## Performance
- N+1 queries? Unnecessary allocations?
- Blocking calls in hot paths?

## Output Format
For each issue: **file:line** — problem → suggestion
Severity: `BLOCKER | MAJOR | MINOR | PRAISE`
