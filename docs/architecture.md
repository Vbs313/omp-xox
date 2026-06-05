# Architecture

omp-xox v3.2 — 12-module extension pack for OMP.

## Module Map

```
extensions/
├── shared/           # config-loader, context-limits, capability-registry, types
├── safety-gate/      # tool_call hook — block dangerous bash (20 rules)
├── path-guard/       # tool_call hook — per-dir path whitelist
├── exec-sandbox/     # tool_call hook — docker/podman container wrap
├── workspace-map/    # session_start hook — repo map + orchestration hint + checkpoint injection
├── plan-mode/        # /plan + /plan-execute — read-only analysis mode
├── dev-tools/        # run_tests — framework detection + output parsing
├── auto-repair/      # auto_repair — test→fix→retest loop
├── dag-scheduler/    # delegate + agent_status + /orchestrate — sub-agent orchestration
├── verification-gate/# run_verification + /verify — 4 quality checks
├── skill-evolver/    # crystallize_skill + l1_insight — self-evolving skills
├── memory-tools/     # l2_fact + distill_session — L2+L4 layered memory
└── checkpoint-notepad/# set_checkpoint — working memory notes
```

## Hook Execution Order

```
tool_call:  safety-gate → path-guard → exec-sandbox
session_start: workspace-map (sendMessage inject)
```

## Slash Commands

`/plan` `/plan-execute` `/safety` `/verify` `/orchestrate <task>`

## Tools

`run_tests` `auto_repair` `delegate` `agent_status` `run_verification` `crystallize_skill` `l1_insight` `l2_fact` `distill_session` `set_checkpoint`

## Memory Architecture (GenericAgent-inspired)

```
L1: Insight Index    → .omp-xox/l1-insight.json          (keyword → skill)
L2: Global Facts     → .omp-xox/memory/l2-global-facts.md
L3: Task SOPs        → skills/omp-xox-evolved/*/SKILL.md
L4: Session Archive  → .omp-xox/memory/l4-sessions/*.md
```

## Configuration

Per-module JSON: `.omp-xox/<module>.json` (project) or `~/.omp/agent/omp-xox/<module>.json` (user).

Environment flags: `OMP_SANDBOX=0` `OMP_PATH_GUARD=0` `OMP_AUTO_REPAIR=0` `OMP_SKILL_EVOLVER=0` `OMP_MEMORY_TOOLS=0` `OMP_CHECKPOINT=0`

## Key Design Decisions

- `pi.sendMessage({ deliverAs: "steer" })` for LLM-visible injection (not `before_agent_start` custom messages)
- `pi.pi.Settings.isolated({ "tools.approvalMode": "yolo" })` for headless sub-agent approval
- `import.meta.dir` for agent discovery paths (not `import.meta.url` + `URL.pathname`)
- Flat frontmatter in agent contracts (parser only handles top-level YAML)
- `pi.exec()` exclusively, zero `node:child_process`
