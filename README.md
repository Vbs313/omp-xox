# omp-xox v3.1

OMP extension pack — 9 modules, only what OMP doesn't provide natively.

[English](#quick-start) | [中文](INSTALL-zh.md)

## Quick Start

```bash
omp plugin install github:Vbs313/omp-xox
```

Or clone and symlink:

```bash
git clone https://github.com/Vbs313/omp-xox.git
ln -sfn $(pwd)/omp-xox ~/.omp/agent/extensions/omp-xox
```

## Modules

| Module | Type | Purpose |
|---|---|---|
| [safety-gate](docs/safety-gate.md) | `tool_call` hook | Block dangerous bash commands (20 rules) |
| [path-guard](docs/path-guard.md) | `tool_call` hook | Per-directory file path whitelist |
| [exec-sandbox](docs/exec-sandbox.md) | `tool_call` hook | Docker/Podman container isolation |
| [workspace-map](docs/workspace-map.md) | `before_agent_start` hook | Repo structure index injection |
| [plan-mode](docs/plan-mode.md) | slash commands | `/plan` + `/plan-execute` — read-only analysis |
| [dev-tools](docs/dev-tools.md) | `run_tests` tool | Framework auto-detection + output parsing |
| [auto-repair](docs/auto-repair.md) | `auto_repair` tool | Test-failure → fix → retest loop |
| [dag-scheduler](docs/dag-scheduler.md) | `delegate` tool | Capability-based sub-agent spawning |
| [verification-gate](docs/verification-gate.md) | `run_verification` tool | Post-agent quality checks |

## Slash Commands

`/plan` `/plan-execute` `/safety` `/verify` `/orchestrate <task>`

## Tools (LLM-callable)

`run_tests` `auto_repair` `delegate(task, capability?)` `agent_status` `run_verification`

## Hook Architecture

```
tool_call:
  safety-gate  →  block  →  path-guard  →  block  →  exec-sandbox  →  mutate

before_agent_start:
  workspace-map  →  inject repo index  (once per session, first-wins)
```

## Configuration

Per-module JSON in `.omp-xox/<module>.json` (project) or `~/.omp/agent/omp-xox/<module>.json` (user).

Environment flags:

| Flag | Effect |
|---|---|
| `OMP_SANDBOX=0` | Disable exec-sandbox |
| `OMP_SANDBOX_BACKEND=podman` | Use Podman instead of Docker |
| `OMP_SANDBOX_IMAGE=ubuntu:latest` | Container image |
| `OMP_PATH_GUARD=0` | Disable path-guard |
| `OMP_AUTO_REPAIR=0` | Disable auto-repair |

## Agents

| Agent | Capabilities | Read-only |
|---|---|---|
| swe | implement, fix, refactor | No |
| explore | explore, search, map | Yes |
| review | review, critique, assess | Yes |
| plan | plan, design, architect | Yes |
| verify | verify, test, audit | Yes |

## Why v3.1 Rebuild

7 original modules were redundant with OMP native features:

| Removed | OMP Built-in |
|---|---|
| fallback-pipeline | `retry.fallbackChains` |
| context-guard | minimizer + `pruneToolOutputs` |
| task-spawner | `todo` + `task` tools |
| git-ops | `bash` tool |
| safe-edit | `edit` tool (hashline + stale-anchor) |
| knowledge-writer | `memory.backend: local` |
| auto-delegate | dag-scheduler `delegate` tool |

5 new modules fill genuine OMP gaps (cross-referenced against Cursor, Cline, Aider, Codex, Claude Code).

Full methodology: [docs/architecture.md](docs/architecture.md)
