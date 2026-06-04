# Agents — Capability Contract Reference

## Format

```markdown
---
id: swe
name: Software Engineer
provides: [implement, fix, refactor]
mode: subagent
budget:
  modelRole: slow
  thinking: high
  maxTurns: 30
  maxTokens: 200000
tools: [read, bash, edit, ...]
verification: [test-pass, lint-pass, no-new-todos]
escalation:
  - condition: "test pass after 3+ retry cycles"
    action: escalate_to_human
---

[Markdown body: system prompt, tool guidance, constraints]
```

## Current Agents

| Agent | Provides | OMP Agent Type | Tools |
|-------|----------|---------------|-------|
| `swe` | implement, fix, refactor | task | read, bash, edit, write, grep, glob, lsp, ast_grep, safe_edit, git_*, run_tests |
| `explore` | explore, search, map, trace | explore | read, grep, glob, lsp, ast_grep, git_log, git_status |
| `verify` | verify, test, audit, check | quick_task | read, bash, grep, run_tests, git_diff, git_log, lsp |
| `review` | review, critique, assess, security-review | reviewer | read, grep, git_diff, git_log, lsp, ast_grep |
| `plan` | plan, design, spec, architect, decompose | plan | read, grep, glob, lsp, ast_grep, git_log |

## How Agents Are Used

The `delegate` tool reads agent contracts and passes them to `pi.pi.createAgentSession()`:

```typescript
// 1. Read agent contract (.md file)
const agent = agents.find(a => a.id === "review");

// 2. Build system prompt from contract
const systemPrompt = buildSystemPrompt(agent, task);

// 3. Create sub-agent session directly
const { session } = await pi.pi.createAgentSession({
  systemPrompt: [systemPrompt],
});

// 4. Drive the session
await session.prompt(task);
await session.waitForIdle();

// 5. Extract result
const result = session.getLastAssistantText();
```

## Verification

Verification checks run after agent completion. `test-pass` is always critical. All others are non-critical.

| Check | Behavior |
|-------|----------|
| test-pass | Runs: bun test / npm test / pytest / go test / cargo test |
| lint-pass | Runs: bun run lint (if configured) |
| no-new-todos | Counts TODO/FIXME/HACK markers (threshold: 10) |
| diff-limit | Checks git diff size (threshold: 200 lines) |

## Discovery

Agents discovered from three layers (later overrides earlier):

1. `<cwd>/.omp/agents/*.md` (project)
2. `~/.omp/agents/*.md` (user)
3. `<omp-xox>/agents/*.md` (bundled)
