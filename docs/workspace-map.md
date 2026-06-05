# Workspace Map

Repository structure index injected into system prompt at session start. Gives the LLM a bird's-eye view of the codebase before it starts reading files.

Aider equivalent: repo-map — the most impactful single feature for token efficiency.

## Hook

`before_agent_start` — fires once per top-level session, injects `<workspace-map>` block as custom message.

## How It Works

```text
Session starts
    │
    ▼
Scan repo files (max 200, skip node_modules/.git/etc)
    │
    ▼
Extract signatures (function/class/interface declarations)
    │
    ▼
Build Markdown index grouped by top-level directory
    │
    ▼
Inject as <workspace-map> custom message
    │
    ▼
LLM sees repo structure in system prompt
```

## Output Format

```markdown
<workspace-map>
# Repository Structure (85 files)

## src/
### src/index.ts
  - export default function ompXox(pi: ExtensionAPI)
  - function autoDetectCapability(task: string): string
### src/config.ts
  - export interface AppConfig

## extensions/
### extensions/safety-gate/index.ts
  - export default function safetyGate(pi: ExtensionAPI)
...
</workspace-map>
```

## Supported Languages

Signature extraction for: TypeScript, JavaScript, Python, Rust, Go, C, C++.

## Token Budget

~2000 tokens max. Automatically truncated if oversized.

## Configuration

```json
// .omp-xox/workspace-map.json
{
  "enabled": true,
  "maxFiles": 200,
  "tokenBudget": 2000
}
```

## Technical

- Uses `fs.readdirSync` + `fs.readFileSync` (first 8KB per file) — no LSP dependency
- Regex-based signature extraction — portable across languages
- `injected` flag prevents re-injection on sub-agent spawn
- Hooks.md guarantee: "first returned message is kept; later messages ignored" — double protection
- See `extensions/workspace-map/index.ts`
