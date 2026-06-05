# omp-xox v3.2 — Extension Pack for OMP

12 modules. Only what OMP doesn't provide natively + self-evolving skills.

## Module Inventory

| # | Module | Hook/Tool | Purpose |
|---|---|---|---|
| 1 | safety-gate | `tool_call` hook | Block dangerous bash commands (20 rules) |
| 2 | path-guard | `tool_call` hook | Per-directory path whitelist |
| 3 | exec-sandbox | `tool_call` hook | Docker/Podman container isolation |
| 4 | workspace-map | `before_agent_start` hook | Repo structure index + checkpoint injection |
| 5 | plan-mode | `/plan` `/plan-execute` | Read-only analysis mode |
| 6 | dev-tools | `run_tests` tool | Framework auto-detection + output parsing |
| 7 | auto-repair | `auto_repair` tool | Test-failure → fix → retest loop |
| 8 | dag-scheduler | `delegate` `agent_status` tools | Capability-based sub-agent spawning |
| 9 | verification-gate | `run_verification` tool `/verify` | Post-agent quality checks |
| 10 | skill-evolver | `crystallize_skill` `l1_insight` tools | Self-evolving skill tree + L1 index |
| 11 | memory-tools | `l2_fact` `distill_session` tools | L2 global facts + L4 session archive |
| 12 | checkpoint-notepad | `set_checkpoint` tool | Working memory during long tasks |

## Memory Architecture (GenericAgent-inspired)

```
L1: Insight Index    → .omp-xox/l1-insight.json          (keyword → skill)
L2: Global Facts     → .omp-xox/memory/l2-global-facts.md (env config)
L3: Task Skills      → skills/omp-xox-evolved/*/SKILL.md  (SOPs)
L4: Session Archive  → .omp-xox/memory/l4-sessions/*.md   (distillations)
```

## Slash Commands

`/plan` `/plan-execute` `/safety` `/verify` `/orchestrate <task>`

## Tools (LLM-callable)

`run_tests` `auto_repair` `delegate` `agent_status` `run_verification` `crystallize_skill` `l1_insight` `l2_fact` `distill_session` `set_checkpoint`

## Configuration

Per-module JSON: `.omp-xox/<module>.json` (project) or `~/.omp/agent/omp-xox/<module>.json` (user).

Environment flags: `OMP_SANDBOX=0` `OMP_PATH_GUARD=0` `OMP_AUTO_REPAIR=0` `OMP_SKILL_EVOLVER=0` `OMP_MEMORY_TOOLS=0` `OMP_CHECKPOINT=0`

## Docs

`docs/architecture.md` — full module map, hook order, config layers.
Per-module docs in `docs/<module>.md`.
