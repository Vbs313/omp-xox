# omp-xox v3.1 — Extension Pack for OMP

9 modules. Only what OMP doesn't provide natively.

## Module Inventory

| # | Module | Hook/Tool | Purpose |
|---|---|---|---|
| 1 | safety-gate | `tool_call` hook | Block dangerous bash commands (20 rules) |
| 2 | path-guard | `tool_call` hook | Per-directory path whitelist |
| 3 | exec-sandbox | `tool_call` hook | Docker/Podman container isolation |
| 4 | workspace-map | `before_agent_start` hook | Repo structure index injection |
| 5 | plan-mode | `/plan` `/plan-execute` | Read-only analysis mode |
| 6 | dev-tools | `run_tests` tool | Framework auto-detection + output parsing |
| 7 | auto-repair | `auto_repair` tool | Test-failure → fix → retest loop |
| 8 | dag-scheduler | `delegate` `agent_status` tools | Capability-based sub-agent spawning |
| 9 | verification-gate | `run_verification` tool `/verify` | Post-agent quality checks |

## Hook Order (same event, registration order)

```
tool_call:  safety-gate → path-guard → exec-sandbox
before_agent_start:  workspace-map (first-wins)
```

## Slash Commands

`/safety` `/plan` `/plan-execute` `/orchestrate` `/verify`

## Tools (LLM-callable)

`run_tests` `auto_repair` `delegate` `agent_status` `run_verification`

## Configuration

Per-module JSON: `.omp-xox/<module>.json` (project) or `~/.omp/agent/omp-xox/<module>.json` (user).

Environment flags: `OMP_SANDBOX=0` `OMP_PATH_GUARD=0` `OMP_AUTO_REPAIR=0`.

## Docs

`docs/architecture.md` — full module map, hook order, config layers.
Per-module docs in `docs/<module>.md`.
