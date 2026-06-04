# Auto-Delegate

## Overview

Keyword-based automatic task routing. Injects routing rules into the system prompt via `before_agent_start` hook. The LLM reads rules and calls `delegate` tool directly.

## File

`extensions/auto-delegate/index.ts`

## How It Works

```
User types: "审查当前pi-xox的安全问题"
  │
  ├─ 1. before_agent_start hook fires
  ├─ 2. Routing rules injected into system prompt
  │     "When user says '审查/review/audit', call delegate with capability=review"
  ├─ 3. LLM reads routing rules
  ├─ 4. LLM detects "审查" → review
  └─ 5. LLM calls delegate tool → delegate spawns sub-agent via pi.pi.createAgentSession()
```

## Routing Table

| Keywords | Capability | Agent | Model | Read-only |
|----------|-----------|-------|-------|-----------|
| 审查/review/audit/assess | review | Code Reviewer | default | Yes |
| 实现/implement/开发/build | implement | Software Engineer | default | No |
| 修复/fix/bug/debug | fix | Software Engineer | default | No |
| 重构/refactor/重写 | refactor | Software Engineer | default | No |
| 探索/explore/搜索/search/find | explore | Code Explorer | smol | Yes |
| 规划/plan/设计/design/架构 | plan | Planner | default | Yes |
| 测试/test/验证/verify | verify | Verifier | default | Yes |
| (no match) | quick | swe | smol | — |

## Model Resolution

- `default` → `xiaomi-token-plan-sgp/mimo-v2.5-pro:high`
- `smol` → `xiaomi-token-plan-sgp/mimo-v2.5:high`

## Hook

`before_agent_start` — Injects routing rules into the system context. Rules tell the LLM to call `delegate` tool (which spawns sub-agents directly via `pi.pi.createAgentSession()`).

## Slash Command

`/auto-delegate [toggle|routes]`

- `toggle` — Enable/disable auto-delegation
- `routes` — Show all routing rules
