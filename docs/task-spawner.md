# Task Spawner

## Overview

Persistent task queue + filesystem mailbox for cross-turn coordination. Tasks survive conversation turns — enabling multi-turn agent workflows.

## File

`extensions/task-spawner/index.ts`

## Design

Task-spawner provides:

1. **Task queue** — `.omp-xox/tasks/<id>.json` persists task records across turns
2. **Mailbox** — `.omp-xox/mailbox/<id>.json` enables agent-to-agent messaging
3. **Status tracking** — pending → running → completed/failed

The primary agent reads pending tasks and executes them via `delegate` tool in subsequent turns.

## Tools

### `enqueue_task`

Add a task to the persistent queue. Returns task ID.

```
Parameters:
  capability: string  — Capability needed
  task: string        — Task description
  label?: string      — Human-readable label
```

### `mark_task`

Update a task's status after execution.

```
Parameters:
  taskId: string
  status: "running" | "completed" | "failed"
  result?: string
```

### `task_status`

Check status of one or all tasks.

```
Parameters:
  taskId?: string
  filter?: "all" | "pending" | "running" | "completed" | "failed"
```

### `collect_task`

Read the persisted result of a completed task.

### `mailbox_send` / `mailbox_read`

Agent-to-agent messaging via `.omp-xox/mailbox/`.

## Slash Command

`/tasks` — Show task queue status

## Filesystem Layout

```
.omp-xox/
├── tasks/
│   ├── a1b2c3d4.json   — Task record
│   └── e5f6g7h8.json
└── mailbox/
    ├── i9j0k1l2.json   — Message
    └── m3n4o5p6.json
```
