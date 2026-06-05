# Checkpoint Notepad

Working memory during long task execution. Prevents context loss when the model loses track mid-task.

GenericAgent equivalent: `update_working_checkpoint` tool.

## Tool: `set_checkpoint`

| Parameter | Type | Default | Description |
|---|---|---|---|
| `note` | string | required | Checkpoint content: progress, decisions, next steps, pitfalls |
| `status` | `in_progress \| blocked \| done \| note` | `in_progress` | Current work status |

Uses `pi.appendEntry("omp-xox-checkpoint", data)` for persistence — survives compaction and session restart.

## Integration with workspace-map

Workspace-map reads active `in_progress` checkpoints from the session branch and injects them:

```xml
<workspace-map>
# Repository Structure (85 files)
...

## Active Checkpoints
- Confirmed Postgres connection params work, moving to backup script
- Found edge case: NULL handling in migration v4 needs fix
</workspace-map>
```

This lets the agent resume a long task after compaction without losing context.

## Usage Pattern

```text
Agent working on a multi-step task:
  1. set_checkpoint("Analyzed DB schema, 12 tables, 3 need migration", status=in_progress)
  2. ... work ...
  3. [COMPACTION HAPPENS — context is trimmed]
  4. set_checkpoint("Migration v4 done, v5 failed — NULL constraint issue", status=blocked)
  5. [Session resumes — checkpoints are injected via workspace-map]
  6. Agent sees: "Migration v4 done, v5 failed — NULL constraint issue"
  7. Continues from where it left off
```

## Configuration

```json
// .omp-xox/checkpoint-notepad.json
{
  "enabled": true,
  "maxCheckpoints": 10
}
```

Env: `OMP_CHECKPOINT=0` to disable.

## Technical

- Uses `pi.appendEntry("omp-xox-checkpoint", data)` — OMP native persistence
- Survives compaction (custom entries pass through)
- Survives session restart (branch reconstruction)
- Workspace-map reads via `ctx.sessionManager.getBranch()` filter
- See `extensions/checkpoint-notepad/index.ts`
