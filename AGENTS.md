# omp-xox v2 — Architecture

Built on Anthropic 2026 Agentic Coding Trends Report and "Building Effective Agents" (Dec 2024).

## 8 Extensions, 14 Tools, 5 Agents

- **DAG Scheduler** — `delegate` (direct sub-agent spawn via `pi.pi.createAgentSession`), `agent_status`
- **Dev Tools** — `safe_edit` (hashline optimistic lock), `git_diff/log/status/blame`, `run_tests`
- **Safety Gate** — 19 default rules, bash command interception via `tool_call` hook
- **Context Guard** — 4 semantic truncation strategies, detects omp minimizer
- **Fallback Pipeline** — 3-chain model fallback (SGP →降级 thinking → opencode-go)
- **Verification Gate** — 4 check types (test/lint/todos/diff), `run_verification`
- **Task Spawner** — persistent task queue + mailbox (`.omp-xox/tasks/`, `.omp-xox/mailbox/`)
- **Auto-Delegate** — keyword-based routing via `before_agent_start` hook

## Subagent Spawning

Uses `pi.pi.createAgentSession()` — the omp SDK's native sub-agent API. The `delegate` tool resolves capability → agent contract, builds system prompt, calls `createAgentSession`, drives the session, and returns the result directly.

```typescript
// delegate tool internals
const { session } = await pi.pi.createAgentSession({
  systemPrompt: [systemPrompt],
});
await session.prompt(task);
await session.waitForIdle();
const result = session.getLastAssistantText();
```

No delegation workaround. No LLM round-trip to `task` tool. Direct SDK call.

## Model Architecture

- **Primary**: `xiaomi-token-plan-sgp/mimo-v2.5-pro:high` (all coding roles)
- **Vision**: `xiaomi-token-plan-sgp/mimo-v2.5:high` (image input support)
- **Fallback**: `opencode-go/deepseek-v4-flash:high` (Step 3 backup)
- **Endpoint**: Anthropic-compatible (`/anthropic`)

## Design Principles

1. **Simplicity first** — 5 capability contracts, not 11 personas
2. **ACI > HCI** — Tool design matters more than prompt design
3. **Verification-driven** — Agent "done" = verification passes
4. **Security-first** — Safety gate from day one
5. **Native SDK** — `pi.pi.createAgentSession()` for direct sub-agent spawning

## Files

```
omp-xox/
├── extensions/           10 TS modules (1972 lines)
├── agents/               5 Capability Contracts (.md)
├── skills/               6 Skills
├── prompts/              8 Prompt templates
└── docs/                 10 Documentation files
```
