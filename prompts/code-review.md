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

## Readability
- Names reveal intent? Variables, functions, classes.
- Flow easy to follow? Avoid deep nesting, complex conditionals.

## Performance
- N+1 queries? Unnecessary allocations? Blocking calls in hot paths?

## Output Format
For each issue: **file:line** — problem → suggestion
Severity: `BLOCKER | MAJOR | MINOR | PRAISE`

## After Review
- If a systematic issue pattern found: `crystallize_skill(name="review-pattern-X", ...)`
- If critical findings: `distill_session(summary="...", learnings=[...])`
