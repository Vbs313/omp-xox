---
description: Optimize code for performance
argument-hint: target and metric
---

# Optimize

Optimize $@. Never guess -- measure first.

## 1. Profile

- What is the metric? Latency, throughput, memory, bundle size, startup time?
- Measure the current baseline. Get concrete numbers.
- Identify the bottleneck. Where is the time or memory actually going? Use a profiler or instrumentation.
- Is this the right thing to optimize? The bottleneck might be elsewhere.

## 2. Analyze

- What is the theoretical minimum for this operation? Compare current performance to it.
- Is the bottleneck algorithmic (wrong data structure, unnecessary work) or systems (I/O, contention, cache misses)?
- Check for obvious waste: repeated computation, excessive allocation, serialized work that could be parallelized.

## 3. Propose

- For each optimization, state: expected gain, complexity cost, and risk.
- Prefer algorithmic improvements over micro-optimizations.
- When micro-optimizing, verify the compiler or runtime does not already handle it.

## 4. Implement & Measure

- Apply one optimization at a time.
- Remeasure after each change. Did it actually improve? If not, revert.
- Keep the optimization only if it shows measurable improvement in the target metric.

## 5. Verify Correctness

- Run the full test suite. Optimizations must not change behavior.
- Check edge cases and boundary conditions. Performance fixes often introduce subtle bugs.
- Document the optimization and its measured impact.
