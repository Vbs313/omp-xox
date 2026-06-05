# Architecture

omp-xox v3.1 — 9-module extension pack for OMP. Only what OMP doesn't provide natively.

## Module Map

```
omp-xox/
├── index.ts                    # Entry: registers 9 modules in hook-safe order
├── docs/                       # Module documentation (this directory)
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
│   ├── workspace-map/          # before_agent_start hook → repo index
│   │
│   ├── plan-mode/              # /plan + /plan-execute commands
│   │
│   ├── dev-tools/              # run_tests tool
│   ├── auto-repair/            # auto_repair tool → test→fix loop
│   ├── dag-scheduler/          # delegate + agent_status + /orchestrate
│   └── verification-gate/      # run_verification + /verify
│
├── agents/                     # Agent contract .md files (5 agents)
└── prompts/                    # Prompt templates (8 templates)
```

## Hook Execution Order

Registration order in `index.ts` is intentional:

| Order | Module | Hook | When Fires | Returns |
|---|---|---|---|---|
| 1 | safety-gate | `tool_call` | Before every tool execution | `{ block, reason }` or void |
| 2 | path-guard | `tool_call` | Before every tool execution | `{ block, reason }` or void |
| 3 | exec-sandbox | `tool_call` | Before bash execution | Mutates `event.input.command` |
| 4 | workspace-map | `before_agent_start` | Once per session start | `{ message }` (first wins) |

Hooks on the same event fire in registration order. Later hooks see mutations from earlier ones.

## Configuration Layers

Each module reads config from:
1. `.omp-xox/<module>.json` (project scope)
2. `~/.omp/agent/omp-xox/<module>.json` (user scope)
3. Built-in defaults

Environment variables override config:
- `OMP_SANDBOX=0` — disable exec-sandbox
- `OMP_SANDBOX_BACKEND=docker|podman` — container runtime
- `OMP_SANDBOX_IMAGE=alpine:latest` — container image
- `OMP_PATH_GUARD=0` — disable path-guard
- `OMP_AUTO_REPAIR=0` — disable auto-repair

## Runtime APIs Used

All modules use only `ExtensionAPI` methods from `@oh-my-pi/pi-coding-agent`:
- `pi.on(event, handler)` — hook registration
- `pi.registerTool({ name, parameters, execute })` — LLM-callable tools
- `pi.registerCommand(name, { handler })` — slash commands
- `pi.sendMessage(msg, { deliverAs })` — context injection
- `pi.exec(cmd, args, opts)` — subprocess (Bun-native, no node:child_process)
- `pi.setActiveTools(names)` / `pi.getAllTools()` — tool filtering
- `pi.setThinkingLevel(level)` — thinking toggle
- `pi.zod` — parameter schemas
- `pi.pi.createAgentSession()` — sub-agent spawning
