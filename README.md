# pi-xox v2

OMP extension pack — 9 modules: DAG-based multi-agent orchestration, structured dev tools, safety gate, semantic context guard, unified fallback pipeline, verification gate, task spawner, auto-delegation, and knowledge writer.

## Installation

### Quick Install (Recommended)

```bash
# Clone the repository
git clone https://github.com/your-org/pi-xox.git
cd pi-xox

# Install as user-level OMP extension
./install.sh

# Or install as project-level extension
./install.sh --project
```

### Manual Install

```bash
# Option 1: Direct path in settings.json
# Add to ~/.omp/agent/settings.json (user) or .omp/settings.json (project):
{
  "extensions": ["/absolute/path/to/pi-xox"]
}

# Option 2: CLI flag (temporary)
omp -e /path/to/pi-xox
```

### Verify Installation

```bash
./install.sh --check
```

### Uninstall

```bash
./install.sh --uninstall
```

## Usage

### Natural Language (Auto-Delegate)

Just type normally. Auto-delegate detects intent from keywords and routes to the right agent:

```
审查当前pi-xox的安全性        → reviewer agent
修复登录超时的bug            → task agent (fix)
探索认证模块的代码结构        → explore agent
规划新的缓存架构             → plan agent
```

### Explicit Delegation

Use the `delegate` tool for explicit capability control:

```
delegate task="..." capability=review
```

### Orchestration

Decompose complex tasks into parallel subtasks:

```
/orchestrate "实现 OAuth 登录并添加单元测试"
```

## Modules

| Module | Tools | Hooks | Commands |
|--------|-------|-------|----------|
| [DAG Scheduler](docs/dag-scheduler.md) | delegate, agent_status | — | /orchestrate |
| [Dev Tools](docs/dev-tools.md) | safe_edit, git_*, run_tests | — | — |
| [Safety Gate](docs/safety-gate.md) | — | tool_call | /safety |
| [Context Guard](docs/context-guard.md) | — | tool_result | /context |
| [Fallback Pipeline](docs/fallback-pipeline.md) | — | session_error | /fallback |
| [Verification Gate](docs/verification-gate.md) | run_verification | — | /verify |
| [Task Spawner](docs/task-spawner.md) | enqueue_task, mark_task, task_status, collect_task, mailbox_* | — | /tasks |
| [Auto-Delegate](docs/auto-delegate.md) | — | before_agent_start | /auto-delegate |

## Architecture

```
delegate task="review safe-edit" capability=review
  │
  ├─ 1. resolveCapability("review") → { agent: "reviewer", ompAgentType: "reviewer", modelRole: "slow" }
  ├─ 2. find agent contract "review" → { prompt, tools, verification }
  ├─ 3. buildSystemPrompt(agent, task)
  ├─ 4. pi.pi.createAgentSession({ systemPrompt })
  ├─ 5. session.prompt(task)
  ├─ 6. session.waitForIdle()
  └─ 7. session.getLastAssistantText() → return result
```

## Agents

| Agent | Capability | OMP Agent Type | Read-only |
|-------|-----------|---------------|-----------|
| swe | implement, fix, refactor | task | No |
| explore | explore, search, map, trace | explore | Yes |
| verify | verify, test, audit, check | quick_task | Yes |
| review | review, critique, assess | reviewer | Yes |
| plan | plan, design, spec, architect | plan | Yes |

See [docs/architecture.md](docs/architecture.md) for full architecture.
