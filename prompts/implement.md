---
description: Implement a feature or fix
argument-hint: specification
---

# Implement

Implement $@. Follow this workflow:

## 1. Clarify

Before writing code, restate the requirements:

- What is the expected behavior? List specific inputs and expected outputs.
- What are the acceptance criteria? Make them measurable.
- What is out of scope for this change?

## 2. Design

- Sketch the approach. Which files need to change? What new types or functions are needed?
- Consider alternatives briefly. Why is this approach better?
- Identify integration points: how does this connect to existing code?

## 3. Implement

- Write the smallest test that captures the requirement. Watch it fail.
- Implement the minimum code to make the test pass.
- Refactor for clarity without changing behavior.
- Repeat for each acceptance criterion.

## 4. Integrate

- Wire up the new code with the existing system.
- Update any callers or interfaces that need to change.
- Add or update documentation if the public API changed.

## 5. Verify

- Run the full test suite. Everything must pass.
- Run manual checks for the acceptance criteria.
- Review the final diff. Remove debug code, commented-out code, and TODOs that belong in issues.
