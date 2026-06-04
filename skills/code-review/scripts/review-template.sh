#!/usr/bin/env bash
# review-template.sh — Generate a code review checklist template
#
# Usage: bash scripts/review-template.sh [file-or-diff-path]
#
# Prints a markdown checklist you can paste into a PR review or issue.
# Optionally accepts a file path to pre-fill the scope.

set -euo pipefail

SCOPE="${1:-<file(s) to review>}"

cat <<TEMPLATE
## Review: ${SCOPE}

### ✅ Strong Points
-

### 🔧 Issues

#### Correctness
- [ ] Does the code do what it claims?
- [ ] Are all branches handled?
- [ ] Are error paths consistent?
- [ ] Any off-by-one or race conditions?

#### Security
- [ ] Input validated and sanitized?
- [ ] Injection vectors checked?
- [ ] Secrets in environment variables?
- [ ] Auth checked on every protected path?

#### Performance
- [ ] N+1 queries or unnecessary loops?
- [ ] Memory concerns with large data?
- [ ] Expensive operations cached or lazy?
- [ ] Blocking calls in async context?

#### Style & Maintainability
- [ ] Follows project conventions?
- [ ] Functions/methods reasonable size?
- [ ] Duplicated code to extract?
- [ ] Names descriptive?

#### Testing
- [ ] Tests exist for new code?
- [ ] Edge cases covered?
- [ ] Test names describe scenario + expected outcome?
- [ ] Integration tests for cross-component changes?

### 💡 Suggestions
-

### ❓ Questions
-
TEMPLATE
