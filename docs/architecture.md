# Architecture

## Overview

omp-xox v2 is an OMP extension pack of **8 independent extensions**. Each extension registers hooks, tools, and slash commands via the OMP extension API. Extensions communicate through shared context (`pi.__ompXoxVerify`) and filesystem state (`.omp-xox/tasks/`, `.omp-xox/mailbox/`).

## Module Graph

```
                      ┌─────────────────────────────────┐
                      │         OMP Core Engine          │
                      │  (hooks, tools, commands, task)  │
                      └──────┬──────────┬───────────────┘
                             │          │
     ┌───────────────────────┤          ├──────────────────────┐
     ▼                       ▼          ▼                      ▼
┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────────┐
│ Safety   │   │ Context  │   │ Fallback │   │ Verification │
│ Gate     │   │ Guard    │   │ Pipeline │   │ Gate         │
│ hook:    │   │ hook:    │   │ hook:    │   │ tool:        │
│ tool_call│   │ tool_    │   │ session_ │   │ run_         │
│          │   │ result   │   │ error    │   │ verification │
└──────────┘   └──────────┘   └──────────┘   └──────────────┘

┌──────────┐   ┌──────────────┐   ┌──────────────┐
│ Dev      │   │ DAG          │   │ Task         │
│ Tools    │   │ Scheduler    │   │ Spawner      │
│ tools:   │   │ tools:       │   │ tools:       │
│ safe_edit│   │ delegate     │   │ enqueue_task │
│ git_*    │   │ agent_status │   │ task_status  │
│ run_tests│   │              │   │ mailbox_*    │
└──────────┘   └──────────────┘   └──────────────┘

┌──────────────┐
│ Auto-        │
│ Delegate     │
│ hook:        │
│ before_      │
│ agent_start  │
└──────────────┘
```

## Subagent Spawning

`delegate` tool uses `pi.pi.createAgentSession()` — the omp SDK's native sub-agent API:

```typescript
const { session } = await pi.pi.createAgentSession({
  systemPrompt: [systemPrompt],
});
await session.prompt(task);
await session.waitForIdle();
const result = session.getLastAssistantText();
```

No delegation workaround. Direct SDK call.

## Filesystem as State Store

- `.omp-xox/tasks/` — Persistent task queue (JSON files)
- `.omp-xox/mailbox/` — Agent-to-agent messaging (JSON files)
- State survives across conversation turns

## Hook-First Safety

- `tool_call` hook → Safety Gate intercepts bash commands
- `tool_result` hook → Context Guard applies semantic truncation
- `session_error` hook → Fallback Pipeline tracks errors
- `before_agent_start` hook → Auto-Delegate injects routing rules
