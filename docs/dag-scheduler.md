# DAG Scheduler

Multi-agent orchestration with capability-based routing. Agent contracts define which agent handles which task type.

OMP's `task` tool spawns sub-agents; dag-scheduler adds capability resolution and agent contracts.

## Tools

### `delegate`

Spawn a specialized sub-agent for a task. The sub-agent runs with the agent contract's system prompt and `tools.approvalMode: yolo` (no approval prompts).

| Parameter | Type | Description |
|---|---|---|
| `task` | string | Task description in natural language |
| `capability` | string? | Explicit capability override (auto-detect if omitted) |

Flow:
1. Auto-detect capability from task keywords
2. Resolve capability → agent contract
3. Build system prompt from contract + task
4. Spawn sub-agent via `pi.pi.createAgentSession()`
5. Collect streaming output via `session.subscribe()`
6. Start agent turn via `session.prompt(task)`
7. Return sub-agent response

Sub-agent settings:
- `tools.approvalMode: yolo` — matches OMP's native `task` tool behavior
- `systemPrompt: () => agentPrompt` — custom agent contract
- Auth/model auto-resolved from parent session

### `agent_status`

List all loaded agent contracts and their capabilities. No parameters.

## Capabilities

| Capability | Agent | Model | Thinking |
|---|---|---|---|
| `review` | reviewer | slow | high |
| `implement` | swe | slow | high |
| `fix` | swe | slow | high |
| `refactor` | swe | slow | high |
| `explore` | explore | smol | off |
| `plan` | plan | slow | high |
| `verify` | verify | smol | low |
| `quick` | swe | smol | off |

Auto-detection keywords: 审查/review → `review`, 实现/implement → `implement`, 修复/fix → `fix`, etc.

## Commands

| Command | Effect |
|---|---|
| `/orchestrate <task>` | Delegate task with auto-detected capability |

## Agent Discovery

Agents are loaded from (first-wins dedup):
1. `<cwd>/.omp/agents/*.md` (project)
2. `~/.omp/agents/*.md` (user)
3. `agents/*.md` (bundled with omp-xox)

Agent contracts use flat YAML frontmatter:
```yaml
---
id: review
name: Code Reviewer
provides: [review, critique, assess]
modelRole: slow
thinking: high
maxTurns: 15
maxTokens: 100000
tools: [read, grep, git_diff, git_log, lsp, ast_grep]
---
# Agent prompt body...
```

## Technical

- `pi.pi.createAgentSession()` — SDK sub-agent spawning
- `pi.pi.Settings.isolated({ "tools.approvalMode": "yolo" })` — headless approval
- `import.meta.dir` — reliable module path for agent discovery
- Agent contracts: Markdown with flat frontmatter
- See `extensions/dag-scheduler/index.ts`
