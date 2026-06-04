---
description: Review code for quality, bugs, and improvements
argument-hint: file or scope
---

# Code Review

Review $@. Focus on these areas in order:

## Correctness

- Does the code do what it claims? Check for logic errors, off-by-one, race conditions.
- Are edge cases handled? Empty states, null values, boundary conditions.
- Are error paths covered? Exceptions caught, errors returned, resources cleaned up.

## Readability

- Do names reveal intent? Variables, functions, classes should be self-documenting.
- Is the flow easy to follow? Avoid deep nesting, complex conditionals, magic numbers.
- Are there comments where needed? Not for what, but for why.

## Maintainability

- Is the code DRY? Repeated logic should be extracted.
- Are functions and modules focused on a single responsibility?
- Are dependencies explicit and minimal?

## Security & Performance

- Are inputs validated and sanitized?
- Any N+1 queries, unnecessary allocations, or blocking calls in hot paths?
- Are secrets, tokens, or sensitive data exposed?

## Format

For each issue, state: **file:line** - problem - suggestion

Mark severity: [BLOCKER] / [MAJOR] / [MINOR] / [PRAISE]
