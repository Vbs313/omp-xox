# Workspace Map

Repository structure index + active checkpoint injection at session start.

Aider equivalent: repo-map + GenericAgent equivalent: working_checkpoint injection.

## Hook

`before_agent_start` — fires once per top-level session, injects `<workspace-map>` block as custom message.

## v3.2: Checkpoint Integration

Workspace-map now reads active `in_progress` checkpoints from the session branch and injects them alongside the repo structure:

```xml
<workspace-map>
# Repository Structure (85 files)
## src/
### src/index.ts
  - export default function ompXox(pi: ExtensionAPI)

## Active Checkpoints
- Confirmed DB connection params work, moving to backup script
- Found edge case: NULL handling in migration v4 needs fix
</workspace-map>
```

Checkpoints come from the `set_checkpoint` tool (checkpoint-notepad module). Only the 5 most recent `in_progress` checkpoints are injected — prevents accumulation across compaction cycles.

## How It Works

```text
Session starts
    │
    ├─ Scan repo files (max 200, skip node_modules/.git/etc)
    ├─ Extract signatures (function/class/interface declarations)
    ├─ Build Markdown index grouped by top-level directory
    │
    ├─ Read session branch → filter omp-xox-checkpoint entries
    ├─ Take last 5 in_progress checkpoints
    │
    └─ Inject as <workspace-map> custom message
```

## Output Format

```markdown
<workspace-map>
# Repository Structure (85 files)

## src/
### src/index.ts
  - export default function ompXox(pi: ExtensionAPI)
### src/config.ts
  - export interface AppConfig
...
</workspace-map>
```

## Supported Languages

Signature extraction for: TypeScript, JavaScript, Python, Rust, Go, C, C++.

## Token Budget

~2000 tokens max for repo map. Checkpoint injection adds ~50 tokens per checkpoint (max 250).

## Configuration

```json
// .omp-xox/workspace-map.json
{
  "enabled": true,
  "maxFiles": 200,
  "tokenBudget": 2000
}
```

## Technical

- Uses `fs.readdirSync` + `fs.readFileSync` (first 8KB per file) — no LSP dependency
- Regex-based signature extraction — portable across languages
- `injected` flag prevents re-injection on sub-agent spawn
- Hooks.md guarantee: "first returned message is kept; later messages ignored" — double protection
- Checkpoint reading via `ctx.sessionManager.getBranch()` — survives compaction
- Checkpoints limited to last 5 to prevent accumulation
- See `extensions/workspace-map/index.ts`
