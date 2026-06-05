# Architecture

omp-xox v3.2 — 12-module extension pack for OMP. Only what OMP doesn't provide natively + self-evolving skills + layered memory.

## Module Map

```
omp-xox/
├── index.ts                    # Entry: registers 12 modules in hook-safe order
├── docs/                       # Per-module documentation (this directory)
├── extensions/
│   ├── shared/                 # Foundation
│   │   ├── config-loader.ts    # Unified config: project > user > default
│   │   ├── context-limits.ts   # Token budgets, file extension sets
│   │   ├── capability-registry.ts  # Agent capability definitions
│   │   └── types.ts            # Shared TypeScript types
│   │
│   ├── safety-gate/            # tool_call hook → block dangerous bash
│   ├── path-guard/             # tool_call hook → per-directory whitelist
│   ├── exec-sandbox/           # tool_call hook → docker/podman wrap
│   │
│   ├── workspace-map/          # before_agent_start hook → repo index + checkpoints
│   │
│   ├── plan-mode/              # /plan + /plan-execute commands
│   │
│   ├── dev-tools/              # run_tests tool
│   ├── auto-repair/            # auto_repair tool → test→fix loop
│   ├── dag-scheduler/          # delegate + agent_status + /orchestrate
│   ├── verification-gate/      # run_verification + /verify
│   │
│   ├── skill-evolver/          # crystallize_skill + l1_insight (L1+L3)
│   ├── memory-tools/           # l2_fact + distill_session (L2+L4)
│   └── checkpoint-notepad/     # set_checkpoint (working memory)
│
├── agents/                     # Agent contract .md files (5 agents)
└── prompts/                    # Prompt templates (8 templates)
```

## Memory Architecture (GenericAgent-inspired)

```
L1: Insight Index    → .omp-xox/l1-insight.json          ← skill-evolver (keyword → skill)
L2: Global Facts     → .omp-xox/memory/l2-global-facts.md ← memory-tools (env config)
L3: Task SOPs        → skills/omp-xox-evolved/*/SKILL.md  ← skill-evolver (reusable workflows)
L4: Session Archive  → .omp-xox/memory/l4-sessions/*.md   ← memory-tools (distillations)

Checkpoints: pi.appendEntry("omp-xox-checkpoint") → workspace-map injection ← checkpoint-notepad
```

## Hook Execution Order

| Order | Module | Hook | When Fires | Returns |
|---|---|---|---|---|
| 1 | safety-gate | `tool_call` | Before every tool execution | `{ block, reason }` or void |
| 2 | path-guard | `tool_call` | Before every tool execution | `{ block, reason }` or void |
| 3 | exec-sandbox | `tool_call` | Before bash execution | Mutates `event.input.command` |
| 4 | workspace-map | `before_agent_start` | Once per session start | `{ message }` (first wins) |

Hooks on the same event fire in registration order. Later hooks see mutations from earlier ones.

## All Tools (LLM-callable)

| Tool | Module | Purpose |
|---|---|---|
| `run_tests` | dev-tools | Framework detection + test execution |
| `auto_repair` | auto-repair | Test→fix→retest loop (validated command) |
| `delegate` | dag-scheduler | Capability-based sub-agent spawning |
| `agent_status` | dag-scheduler | List loaded agent contracts |
| `run_verification` | verification-gate | 4 quality checks |
| `crystallize_skill` | skill-evolver | Write SKILL.md + update L1 index |
| `l1_insight` | skill-evolver | Read/write insight index |
| `l2_fact` | memory-tools | Read/write global facts |
| `distill_session` | memory-tools | Compress session to L4 archive |
| `set_checkpoint` | checkpoint-notepad | Write working memory note |

## All Slash Commands

`/plan` `/plan-execute` `/safety` `/verify` `/orchestrate <task>`

## Configuration Layers

Each module reads config from:
1. `.omp-xox/<module>.json` (project scope)
2. `~/.omp/agent/omp-xox/<module>.json` (user scope)
3. Built-in defaults

Environment flags:

| Flag | Module |
|---|---|
| `OMP_SANDBOX=0` | exec-sandbox |
| `OMP_SANDBOX_BACKEND=docker\|podman` | exec-sandbox |
| `OMP_SANDBOX_IMAGE=alpine:latest` | exec-sandbox |
| `OMP_PATH_GUARD=0` | path-guard |
| `OMP_AUTO_REPAIR=0` | auto-repair |
| `OMP_SKILL_EVOLVER=0` | skill-evolver |
| `OMP_MEMORY_TOOLS=0` | memory-tools |
| `OMP_CHECKPOINT=0` | checkpoint-notepad |

## Runtime APIs Used

All modules use only `ExtensionAPI` methods from `@oh-my-pi/pi-coding-agent`:
- `pi.on(event, handler)` — hook registration
- `pi.registerTool({ name, parameters, execute })` — LLM-callable tools
- `pi.registerCommand(name, { handler })` — slash commands
- `pi.sendMessage(msg, { deliverAs })` — context injection
- `pi.exec(cmd, args, opts)` — subprocess (Bun-native)
- `pi.setActiveTools(names)` / `pi.getAllTools()` — tool filtering
- `pi.setThinkingLevel(level)` — thinking toggle
- `pi.zod` — parameter schemas
- `pi.pi.createAgentSession()` — sub-agent spawning
- `pi.appendEntry(customType, data)` — persistent custom entries
