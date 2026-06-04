---
name: code-review
description: Systematic code review for quality, security, performance, and style. TRIGGERS: review, code review, review code, check code, quality check, security review
---

# Code Review Skill

Systematic code review for quality, security, performance, and style.

## When to Use

Use this skill when asked to:
- Review code changes before merging
- Check for security vulnerabilities
- Evaluate code quality and style
- Assess performance implications
- Verify test coverage

## Workflow

### 1. Understand the Context

- What does this code do? Read the diff or full file.
- What is the expected behavior? Check linked issues or PR descriptions.
- What are the project conventions? Glance at nearby code for style.

### 2. Run the Review Checklist

Generate a review template using the helper script:

```bash
bash skills/code-review/scripts/review-template.sh
```

### 3. Review Categories

#### Correctness
- Does the code do what it claims?
- Are there off-by-one errors, race conditions, or logic bugs?
- Are all branches handled (if/else, switch cases, pattern matches)?
- Are error paths handled consistently?

#### Security
- Are user inputs validated and sanitized?
- Are there injection vulnerabilities (SQL, command, XSS)?
- Are secrets hardcoded instead of using environment variables?
- Is authentication/authorization checked on every protected path?
- Are dependencies up to date without known CVEs?

#### Performance
- Are there N+1 queries or unnecessary loops?
- Could large data sets cause memory issues?
- Are expensive operations cached or lazy where appropriate?
- Are there obvious bottlenecks (sync I/O in async context, blocking calls)?

#### Style & Maintainability
- Does the code follow project conventions (naming, formatting, file structure)?
- Are functions/methods a reasonable size?
- Is there duplicated code that could be extracted?
- Are names descriptive and unambiguous?
- Are comments necessary or could the code speak for itself?

#### Testing
- Are there tests for the new code?
- Do tests cover edge cases, not just the happy path?
- Are test names descriptive (what scenario, what expected outcome)?
- Are there integration tests for cross-component changes?

### 4. Write the Review

Structure your review response like this:

```
## Review: <file(s) or scope>

### ✅ Strong Points
- ...

### 🔧 Issues
- **Severity: high/medium/low** — Description with line reference
- ...

### 💡 Suggestions
- Optional improvements that are not blocking
- ...

### ❓ Questions
- Anything unclear that needs clarification
- ...
```

### 5. Severity Guide

| Severity | Meaning |
|----------|---------|
| **High** | Bug, security hole, or correctness issue. Must fix before merge. |
| **Medium** | Violates project standards, significant maintainability concern. Should fix. |
| **Low** | Style nit, minor improvement. Nice to fix but not required. |

## Scripts

- `scripts/review-template.sh` — Prints a reusable review checklist template.
