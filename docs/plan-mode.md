# Plan Mode

Read-only analysis mode before execution. The agent plans without touching files.

Claude Code / Cursor / Cline equivalent: Plan Mode / Plan/Act split.

## Commands

| Command | Effect |
|---|---|
| `/plan` | Restrict to read-only tools (`read`, `search`, `find`, `lsp`, `web_search`), raise thinking to `high`. Saves original tool set. |
| `/plan-execute` | Restore full tool set, return to normal thinking. Injects execution prompt. |

## Flow

```text
User: /plan
    │
    ├─ pi.getActiveTools() → save
    ├─ pi.setActiveTools(["read","search","find","lsp","web_search"])
    ├─ pi.setThinkingLevel("high")
    ├─ pi.sendMessage(PLAN_PROMPT, { deliverAs: "steer" })
    │
    ▼
LLM produces plan (no file writes allowed)
    │
    ▼
User: /plan-execute
    │
    ├─ pi.setActiveTools(savedTools)
    ├─ pi.setThinkingLevel("high")
    ├─ pi.sendMessage(EXECUTION_PROMPT, { deliverAs: "steer" })
    │
    ▼
LLM implements the plan
```

## Plan Prompt Content

- "You CAN: read files, search code, explore repo"
- "You CANNOT: write/edit files, run bash, spawn sub-agents"
- Expected output: files to modify, code changes, testing strategy, risks

## Technical

- `planActive` closure variable tracks state
- `originalTools` saved on first `/plan` call, restored on `/plan-execute`
- If `pi.setActiveTools()` fails (e.g., during registration phase), warns but continues
- OMP's task tool already has plan mode for sub-agents — this brings it to the top-level agent
- See `extensions/plan-mode/index.ts`
