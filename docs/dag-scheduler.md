# DAG Scheduler

## Overview

Orchestration core. Provides capability routing and direct sub-agent spawning via `pi.pi.createAgentSession()`.

## File

`extensions/dag-scheduler/index.ts`

## Tools

### `delegate`

Direct sub-agent spawning. Auto-detects capability from keywords, resolves to agent contract, calls `pi.pi.createAgentSession()` directly, drives the session, returns the result.

```
delegate task="审查safe-edit的安全性"
  → auto-detect: capability=review
  → find agent contract "review" (Code Reviewer, slow model)
  → pi.pi.createAgentSession({ systemPrompt })
  → session.prompt(task)
  → session.waitForIdle()
  → session.getLastAssistantText()
  → return result
```

**No delegation workaround.** Direct SDK call — the sub-agent runs inside omp's native session management.

**Auto-detection keywords:**

| Keywords | Capability | Agent |
|----------|-----------|-------|
| 审查/review/audit/assess | review | reviewer |
| 实现/implement/开发/build | implement | swe |
| 修复/fix/bug/debug | fix | swe |
| 重构/refactor/重写 | refactor | swe |
| 探索/explore/搜索/search | explore | explore |
| 规划/plan/设计/design | plan | plan |
| 测试/test/验证/verify | verify | verify |
| (no match) | quick | swe (smol) |

**Explicit capability override:**
```
delegate task="..." capability=review
```

### `agent_status`

List all loaded agent contracts with capabilities, model roles, tools, and read-only status.

## Slash Commands

### `/orchestrate <task>`

Injects a structured orchestration prompt into the conversation. The LLM then:
1. Calls `delegate` with capability=plan to decompose the task
2. Calls `delegate` for each subtask (parallel when possible)
3. Calls `run_verification` after all complete

## Key Architecture Change (v2.1)

**Before (v2.0):** `delegate` returned delegation instructions → LLM called omp's `task` tool → extra LLM round-trip.

**Now (v2.1):** `delegate` calls `pi.pi.createAgentSession()` directly → no LLM round-trip → deterministic execution.

```typescript
// Internal implementation
const { session } = await pi.pi.createAgentSession({
  systemPrompt: [systemPrompt],
});
await session.prompt(task);
await session.waitForIdle();
const result = session.getLastAssistantText();
```

## Integration with Auto-Delegate

The `auto-delegate` extension (`extensions/auto-delegate/`) hooks `before_agent_start` to inject routing rules into the system prompt. The LLM reads these rules and calls `delegate` directly (not `task` tool) — matching the new architecture.
