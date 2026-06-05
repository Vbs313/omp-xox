# Safety Gate

Content-level bash command safety rules. Extends OMP's built-in bash interceptor (~6 rules) with 20 additional patterns.

## Hook

`tool_call` — fires before every tool execution. Registered first so it blocks before any mutation hooks.

## Rules

20 built-in rules, 3 action levels:

| Action | Behavior |
|---|---|
| `block` | Tool call blocked immediately, reason returned to LLM |
| `confirm` | In permissive mode: allow. In strict mode: block |
| `warn` | Allow but track in stats |

Sample rules:
- `rm -rf /` → block
- `sudo su` → warn
- `npm publish` → confirm
- `eval ` → warn
- `curl | bash` → block
- `DROP TABLE` → warn

## Commands

| Command | Effect |
|---|---|
| `/safety` | Show stats: blocked, confirmed, warned counts |
| `/safety toggle` | Enable/disable |
| `/safety mode` | Toggle strict/permissive |
| `/safety rules` | List all rules |

## Configuration

```json
// .omp-xox/safety-gate.json
{
  "enabled": true,
  "mode": "strict",
  "rules": [
    { "pattern": "rm -rf /", "action": "block", "message": "Destructive rm blocked" }
  ]
}
```

## Technical

- Regexes pre-compiled at load time into `config.compiled`
- `config.mode: "strict"` → `confirm` rules treated as `block`
- Handles `event.toolName !== "bash"` early-return
- See `extensions/safety-gate/index.ts`
