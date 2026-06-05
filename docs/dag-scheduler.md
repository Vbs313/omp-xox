# DAG Scheduler

Multi-agent orchestration with capability-based routing. Agent contracts define which agent handles which task type.

OMP's `task` tool spawns sub-agents; dag-scheduler adds capability resolution and agent contracts.

## Tools

### `delegate`

Spawn a specialized sub-agent for a task.

| Parameter | Type | Description |
|---|---|---|
| `task` | string | Task description in natural language |
| `capability` | string? | Explicit capability override (auto-detect if omitted) |

The tool:
1. Auto-detects capability from task keywords (or uses explicit override)
2. Resolves capability to agent contract
3. Builds system prompt from contract + task
4. Spawns sub-agent via `pi.pi.createAgentSession()`
5. Returns sub-agent response

### `agent_status`

List all loaded agent contracts and their capabilities. No parameters.

## Capabilities

| Capability | Agent | Tools | Model |
|---|---|---|---|
| `review` | reviewer | read, search, find, lsp | slow (high thinking) |
| `implement` | swe | read, write, edit, bash, lsp, search, find | default (high thinking) |
| `fix` | swe | read, write, edit, bash, lsp, search, find | default (medium thinking) |
| `refactor` | swe | read, write, edit, bash, lsp, search, find | default (high thinking) |
| `explore` | explore | read, search, find, lsp, web_search | smol (low thinking) |
| `plan` | plan | read, search, find, lsp, web_search | slow (high thinking) |
| `verify` | verify | read, bash, lsp, search, find | smol (low thinking) |

Auto-detection keywords: 审查/review → `review`, 实现/implement → `implement`, 修复/fix → `fix`, etc.

## Commands

| Command | Effect |
|---|---|
| `/orchestrate <task>` | Delegate task with auto-detected capability |

## Technical

- Hook: `session_start` — loads agent contracts from `agents/*.md`
- Uses `pi.pi.createAgentSession()` directly (OMP SDK)
- Agent contracts: Markdown files with frontmatter (`name`, `provides`, `tools`, `prompt`)
- See `extensions/dag-scheduler/index.ts`
