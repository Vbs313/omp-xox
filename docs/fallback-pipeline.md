# Fallback Pipeline

## Overview

Model fallback visibility + tracking. The actual fallback logic runs in the `delegate` tool's `createAgentSession` call. This extension provides visibility and the `/fallback` command.

## File

`extensions/fallback-pipeline/index.ts`

## Fallback Chains

All coding roles resolve to `xiaomi-token-plan-sgp/mimo-v2.5-pro:high`. Fallback chains provide real model switching when the primary fails:

### Implementation (implement, fix, refactor)

```
Step 1: mimo-v2.5-pro:high  → default + high thinking
Step 2: mimo-v2.5-pro:medium → default + medium thinking (降级)
Step 3: opencode-go/deepseek-v4-flash:high → 真正兜底（不同模型）
```

### Planning/Review (plan, design, review, critique)

```
Step 1: mimo-v2.5-pro:xhigh → default + xhigh thinking
Step 2: mimo-v2.5-pro:high  → default + high thinking (降级)
Step 3: opencode-go/deepseek-v4-flash:high → 真正兜底
```

### Light (verify, test, explore, search)

```
Step 1: mimo-v2.5-pro:low  → default + low thinking
Step 2: mimo-v2.5-pro:off  → default + off thinking (关闭推理)
Step 3: mimo-v2.5:high     → 视觉模型兜底（不同模型）
```

## Error Classification

| Error | Keywords | Action |
|-------|----------|--------|
| rate_limit | 429, rate | Next step |
| server_error | 503, 502, 500 | Next step |
| context_length | context length | Next step |
| timeout | timeout, timed | Next step |
| unknown | everything else | Next step |

## Hooks

`session_error` — Tracks fallback events for visibility. Does not change execution.

## Slash Command

`/fallback [status|toggle]`
