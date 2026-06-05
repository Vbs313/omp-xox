# omp-xox v3.2 — Extension Pack for OMP

12 modules. Only what OMP doesn't provide natively + self-evolving skills + layered memory.

## Module Inventory

| # | Module | Hook/Tool | Purpose |
|---|---|---|---|
| 1 | safety-gate | `tool_call` hook | Block dangerous bash commands (20 rules) |
| 2 | path-guard | `tool_call` hook | Per-directory path whitelist |
| 3 | exec-sandbox | `tool_call` hook | Docker/Podman container isolation |
| 4 | workspace-map | `session_start` hook | Repo map + orchestration hint + checkpoints |
| 5 | plan-mode | `/plan` `/plan-execute` | Read-only analysis mode |
| 6 | dev-tools | `run_tests` tool | Framework auto-detection + output parsing |
| 7 | auto-repair | `auto_repair` tool | Test-failure → fix → retest loop |
| 8 | dag-scheduler | `delegate` `agent_status` + `/orchestrate` | Capability-based sub-agent spawning |
| 9 | verification-gate | `run_verification` `/verify` | 4 quality checks |
| 10 | skill-evolver | `crystallize_skill` `l1_insight` | Self-evolving skills |
| 11 | memory-tools | `l2_fact` `distill_session` | L2+L4 layered memory |
| 12 | checkpoint-notepad | `set_checkpoint` | Working memory notes |

## Slash Commands

`/plan` `/plan-execute` `/safety` `/verify` `/orchestrate <task>`

## Tools (LLM-callable)

`run_tests` `auto_repair` `delegate(task, capability?)` `agent_status` `run_verification` `crystallize_skill` `l1_insight` `l2_fact` `distill_session` `set_checkpoint`

## Configuration

Per-module JSON: `.omp-xox/<module>.json` | Env: `OMP_SANDBOX=0` `OMP_PATH_GUARD=0` `OMP_AUTO_REPAIR=0` `OMP_SKILL_EVOLVER=0` `OMP_MEMORY_TOOLS=0` `OMP_CHECKPOINT=0`

## OMP Config Required

```yaml
# ~/.omp/agent/config.yml
extensions:
  - /home/vbs/code/omp-xox
```

## Docs

`docs/architecture.md` — full module map, hook order, config layers.
Per-module docs in `docs/<module>.md`.
