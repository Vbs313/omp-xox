---
description: Optimize code for performance, memory, or bundle size
argument-hint: file, function, or module
---

# Optimize

Optimize: $@. Use `run_tests` before and after for regression check. Use `delegate(capability=implement)` for complex optimizations. Use `distill_session` to record benchmarks.

## Workflow
1. Profile baseline: identify bottleneck (don't guess)
2. `/plan` — propose optimization with expected improvement
3. Implement after user approves. `set_checkpoint("Applied X optimization", status=in_progress)`
4. `run_tests` — confirm no regression
5. Compare metrics: before vs after
6. `distill_session(summary="...", learnings=["before: Xms, after: Yms"], tags=["perf", "optimization"])`

## Dimensions

### CPU
- Remove unnecessary work: redundant calculations, repeated parsing
- Cache expensive results: memoize pure functions
- Use appropriate data structures: Map vs Array.find, Set vs Array.includes

### Memory
- Avoid large allocations in hot paths
- Release references for garbage collection
- Stream large data instead of buffering

### I/O
- Batch operations instead of N individual calls
- Parallelize independent async work
- Debounce/throttle frequent operations

## Rules
- NEVER optimize without measurement first
- Clean code > micro-optimizations
- One optimization at a time, verify each
