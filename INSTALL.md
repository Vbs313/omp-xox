# omp-xox — OMP Extension Pack for Multi-Agent Orchestration

[English](#installation) | [中文](INSTALL-zh.md)

## What is omp-xox?

omp-xox is an extension pack for [Oh My Pi (OMP)](https://github.com/can1357/oh-my-pi) that adds:

- **Multi-agent orchestration** — DAG-based task decomposition with parallel subagents
- **Structured dev tools** — hashline-safe editor, git integration, test runner
- **Safety gate** — 19 configurable bash command rules
- **Context guard** — 4 semantic truncation strategies for long sessions
- **Fallback pipeline** — 3-chain model fallback (primary → degraded → backup)
- **Verification gate** — test/lint/todo/diff checks before completion
- **Task spawner** — persistent filesystem task queue + inter-agent mailbox
- **Auto-delegate** — keyword-based routing to specialized agents
- **Knowledge writer** — captures `/compact` summaries to Obsidian vault

## Requirements

- [Oh My Pi (OMP)](https://github.com/can1357/oh-my-pi) ≥ 15.9.0
- Bun or Node.js ≥ 18

---

## Installation

### Method 1: Install Script (Recommended)

```bash
# Clone
git clone https://github.com/Vbs313/omp-xox.git
cd omp-xox

# Install as user-level extension (persists across all projects)
./install.sh

# Or install as project-level extension (only for current project)
./install.sh --project

# Verify
./install.sh --check
```

### Method 2: Manual — settings.json

Add the absolute path to your OMP settings file:

**User-level** (`~/.omp/agent/settings.json`):
```json
{
  "extensions": ["/absolute/path/to/omp-xox"]
}
```

**Project-level** (`.omp/settings.json` in your project root):
```json
{
  "extensions": ["/absolute/path/to/omp-xox"]
}
```

### Method 3: CLI Flag (Temporary)

```bash
omp -e /path/to/omp-xox
```

### Verify Installation

```bash
# Check registration
./install.sh --check

# Test in OMP
omp --max-turns 1 --print "list all omp-xox tools"
```

Expected output should include: `delegate`, `safe_edit`, `archive_to_knowledge`, `run_verification`, `enqueue_task`, etc.

### Uninstall

```bash
./install.sh --uninstall
```

Or manually remove the path from `~/.omp/agent/settings.json`.

---

## Usage

### Natural Language (Auto-Delegate)

Just type normally. The auto-delegate module detects intent from keywords:

```
审查当前代码的安全性          → reviewer agent
修复登录超时的bug            → task agent (fix)
探索认证模块的代码结构        → explore agent
规划新的缓存架构             → plan agent
```

### Explicit Delegation

```
delegate task="review the authentication module" capability=review
```

### Orchestration

```
/orchestrate "implement OAuth login with unit tests"
```

### Knowledge Archiving

```
/archive                          # Archive last /compact summary
/archive OAuth implementation      # With custom topic
```

Or via tool:
```
archive_to_knowledge topic="Solution" content="..." domain="AI-Agent"
```

---

## Modules

| Module | Tools | Commands | Hooks |
|--------|-------|----------|-------|
| [DAG Scheduler](docs/dag-scheduler.md) | `delegate`, `agent_status` | `/orchestrate` | — |
| [Dev Tools](docs/dev-tools.md) | `safe_edit`, `git_diff`, `git_log`, `git_status`, `git_blame`, `run_tests` | — | — |
| [Safety Gate](docs/safety-gate.md) | — | `/safety` | `tool_call` |
| [Context Guard](docs/context-guard.md) | — | `/context` | `tool_result` |
| [Fallback Pipeline](docs/fallback-pipeline.md) | — | `/fallback` | `session_error` |
| [Verification Gate](docs/verification-gate.md) | `run_verification` | `/verify` | — |
| [Task Spawner](docs/task-spawner.md) | `enqueue_task`, `mark_task`, `task_status`, `collect_task`, `mailbox_send`, `mailbox_read` | `/tasks` | — |
| [Auto-Delegate](docs/auto-delegate.md) | — | `/auto-delegate` | `before_agent_start` |
| [Knowledge Writer](extensions/knowledge-writer/) | `archive_to_knowledge` | `/archive`, `/knowledge` | `compact_output` |

## Agents (Capability Contracts)

| Agent | Capabilities | OMP Agent Type | Read-only |
|-------|-------------|---------------|-----------|
| `swe` | implement, fix, refactor | task | No |
| `explore` | explore, search, map, trace | explore | Yes |
| `verify` | verify, test, audit, check | quick_task | Yes |
| `review` | review, critique, assess | reviewer | Yes |
| `plan` | plan, design, spec, architect | plan | Yes |

---

## Architecture

```
User: "审查当前代码"
  │
  ├─ auto-delegate detects "审查" → routes to review capability
  ├─ delegate tool resolves capability → finds "review" agent contract
  ├─ builds system prompt from agents/review.md
  ├─ pi.pi.createAgentSession({ systemPrompt })
  ├─ session.prompt(task)
  ├─ session.waitForIdle()
  └─ returns structured review result
```

---

## Directory Structure

```
omp-xox/
├── index.ts                    # Unified entry point (loads all 9 extensions)
├── package.json                # OMP extension manifest
├── install.sh                  # Installation script
├── extensions/
│   ├── dag-scheduler/          # Multi-agent orchestration
│   ├── dev-tools/              # safe_edit, git_*, run_tests
│   ├── safety-gate/            # Bash command rules
│   ├── context-guard/          # Context truncation
│   ├── fallback-pipeline/      # Model fallback chain
│   ├── verification-gate/      # Pre-completion checks
│   ├── task-spawner/           # Persistent task queue
│   ├── auto-delegate/          # Keyword routing
│   ├── knowledge-writer/       # Compact → Obsidian archiver
│   └── shared/                 # Shared utilities
├── agents/                     # Agent capability contracts
│   ├── explore.md
│   ├── plan.md
│   ├── review.md
│   ├── swe.md
│   └── verify.md
├── prompts/                    # Reusable prompt templates
│   ├── code-review.md
│   ├── debug.md
│   ├── document.md
│   ├── explain.md
│   ├── generate-tests.md
│   ├── implement.md
│   ├── optimize.md
│   └── refactor.md
├── skills/                     # OMP skill definitions
│   ├── code-analysis/
│   ├── code-review/
│   ├── documentation/
│   ├── debugging/
│   ├── refactoring/
│   └── test-generation/
└── docs/                       # Module documentation
```

---

## License

MIT
