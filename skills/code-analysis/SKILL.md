---
name: code-analysis
description: Deep analysis of code structure, architecture, and data flow.
---

# Code Analysis

Use workspace-map for top-level structure. Use `delegate(capability=explore)` for broad searches.

## Workflow

1. **Read workspace-map** — understand module layout before reading files
2. **Trace data flow** — follow inputs → transformations → outputs
3. **Identify architectural patterns** — MVC, layered, microservices, event-driven?
4. **Map dependencies** — which modules call which? Circular dependencies?
5. **Document findings** — explicit, file:line references

## Analysis Dimensions

### Structure
- Module boundaries, responsibility separation
- Coupling: tight or loose? Dependency direction?
- Cohesion: focused or scattered?

### Data Flow
- Entry points and exit points
- State mutations: where, when, by whom?
- Async boundaries: event loop, workers, queues

### Anti-Patterns
- God objects, shotgun surgery, feature envy
- Hidden dependencies, temporal coupling

## Output Format

```
## Analysis: <scope>

### Architecture Overview
- Pattern: <identified pattern>
- Key modules: <list with responsibilities>
- Data flow: <description>

### Issues Found
- **file:line** — problem → resolution

### Recommendations
- actionable change → expected benefit
```
