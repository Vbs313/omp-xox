# Path Guard

Per-directory permit rules for tool operations. Extends safety-gate's command-content rules with path-level whitelisting.

Claude Code equivalent: `.claude/settings.json` PermissionRequest hooks with path matchers.

## Hook

`tool_call` — fires after safety-gate, before exec-sandbox. Checks file paths against rules.

## Rules

| Action | Behavior |
|---|---|
| `deny` | Block tool call, return reason |
| `warn` | Allow but notify via UI |
| `allow` | No action |
| `confirm` | Reserved for future UI prompt |

7 built-in rules:

```json
[
  { "path": "/tmp/*", "action": "allow", "tools": ["*"] },
  { "path": ".env*", "action": "warn", "tools": ["read", "write", "edit"] },
  { "path": "/etc/*", "action": "deny", "tools": ["*"] },
  { "path": "/proc/*", "action": "deny", "tools": ["*"] },
  { "path": "/sys/*", "action": "deny", "tools": ["*"] },
  { "path": "~/.ssh/*", "action": "deny", "tools": ["read", "write", "edit"] },
  { "path": "~/.gnupg/*", "action": "deny", "tools": ["read", "write", "edit"] }
]
```

## Path Extraction

Extracts file paths from tool inputs:
- `write`/`edit` → `input.path` / `input.file_path`
- `read` → strips `:` line selectors from path
- `bash` → regex-match absolute paths from command string

## Configuration

```json
// .omp-xox/path-rules.json
{
  "enabled": true,
  "defaultAction": "allow",
  "rules": [...]
}
```

Env: `OMP_PATH_GUARD=0` to disable.

## Technical

- Path matching supports `*` (glob), `?`, `~` expansion
- Rules are first-match by tool applicability
- See `extensions/path-guard/index.ts`
