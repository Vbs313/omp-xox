---
name: code-analysis
description: Static code analysis for complexity, dependencies, and quality metrics. TRIGGERS: analyze, code analysis, complexity, dependencies, metrics, static analysis
---

# Code Analysis Skill

Static code analysis for complexity, dependencies, and quality metrics.

## When to Use

Use this skill when asked to:
- Analyze code complexity (cyclomatic, cognitive)
- Map module or file dependencies
- Measure code quality metrics
- Find dead code or unused exports
- Identify tight coupling or circular dependencies
- Report on technical debt

## Workflow

### 1. Scan

Select the right tool for the analysis goal:

| Goal | Recommended Tool |
|------|----------------|
| Cyclomatic complexity | `lizard`, `radon`, ESLint `complexity` rule |
| Cognitive complexity | SonarQube, or manual review |
| Dependency graph | `madge` (JS/TS), `pydeps` (Python), `go mod graph` |
| Dead code | `ts-prune` (TS), `vulture` (Python), `unused` (Go) |
| Code quality | `eslint`/`tslint`, `pylint`, `golangci-lint`, `clippy` |
| Duplication | `jscpd`, `pmd-cpd`, `dupl` |
| Test coverage | `istanbul`/`c8`, `pytest-cov`, `go test -cover` |

If a tool is not available, use the project's existing linter or formatter configuration.

### 2. Measure

Run analysis and capture metrics:

- **Complexity**: List functions/files with highest cyclomatic complexity. Flag anything above 10 (or the project's threshold).
- **Dependencies**: Identify circular dependencies, deep module coupling, and unreachable modules.
- **Size**: File line counts, function lengths, class sizes.
- **Duplication**: Percentage of duplicated code and locations.
- **Coverage**: Overall coverage percentage and uncovered critical paths.

### 3. Report

Structure your findings:

```
## Code Analysis: <scope>

### Summary
- Total files: N
- Total lines: N
- Test coverage: N%

### Complexity Hotspots
| File | Function | Complexity | Threshold |
|------|----------|-----------|-----------|
| src/foo.ts | bar() | 15 | 10 |

### Dependency Issues
- Circular: modules/A → modules/B → modules/A
- High fan-in: utils.ts (imported by 23 files)

### Recommendations
1. Extract switch/if-chain in src/foo.ts:bar() into strategy pattern
2. Break circular dependency between modules A and B
3. ...
```

### 4. Prioritize

Not every metric problem needs fixing. Prioritize based on:

- **Risk**: Does this cause bugs or make bugs harder to find?
- **Frequency**: How often is this code touched?
- **Cost**: How hard is it to fix?
- **Coverage**: Is there test coverage to support a fix?

## Thresholds (Common)

| Metric | Warning | Critical |
|--------|---------|----------|
| Cyclomatic complexity | 10+ | 20+ |
| Function length | 30+ lines | 60+ lines |
| File length | 300+ lines | 500+ lines |
| Duplication | 5%+ | 15%+ |
| Coupling (fan-out) | 10+ dependencies | 20+ dependencies |
| Test coverage | < 80% | < 50% |

## Scripts

No scripts for this skill. Use the appropriate static analysis tool for the project's language and ecosystem.
