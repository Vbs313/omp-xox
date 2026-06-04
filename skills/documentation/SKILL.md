---
name: documentation
description: Generate API documentation, README files, and inline comments. TRIGGERS: document, documentation, readme, api docs, jsdoc, tsdoc, comments
---

# Documentation Skill

Generate API documentation, README files, and inline comments.

## When to Use

Use this skill when asked to:
- Write or update a README file
- Document a function, class, module, or API
- Add JSDoc/TSDoc comments to code
- Generate API reference docs
- Write inline comments for complex logic

## Workflow

### 1. Analyze the Code

- **What is the public surface?** Exported functions, classes, types, constants.
- **What are the inputs and outputs?** Parameters, return values, thrown exceptions.
- **What are the side effects?** Network calls, file I/O, database operations, global state.
- **What is the non-obvious behavior?** Edge cases, error states, ordering dependencies.

### 2. Choose the Documentation Style

| Surface | Style |
|---------|-------|
| Public API / library | JSDoc/TSDoc block comments with `@param`, `@returns`, `@throws` |
| Internal function | Short inline comment above the function |
| Complex logic | Line comments explaining the "why", not the "what" |
| README | Project overview, install, usage, API, contributing, license |
| CLI tool | `--help` output, man page, or README section |

### 3. Generate Documentation

For API comments (JSDoc/TSDoc):

```
/**
 * Brief description of what the function does.
 *
 * Longer description if behavior is non-obvious.
 *
 * @param {Type} paramName - Description of the parameter.
 * @returns {Type} Description of the return value.
 * @throws {ErrorType} When and why this error is thrown.
 */
```

For README files, structure as follows:

```
# Project Name

Brief one-line description.

## Installation

## Usage

## API

## Contributing

## License
```

### 4. Review

- Does every public export have documentation?
- Is the documentation accurate? (Check against the actual code.)
- Are examples runnable? (Test them if possible.)
- Is the tone professional but readable? Avoid jargon where plain language works.

## Guidelines

- **Document the "why", not the "what"**. The code already says what it does. Comments should explain why it does it that way.
- **Keep docs close to the code**. Inline comments and docstrings stay in the source file. README and API docs can be separate.
- **Update docs when code changes**. Outdated documentation is worse than no documentation.
- **Use complete sentences** for docstrings and README content.
- **Include at least one example** for every public API surface.
