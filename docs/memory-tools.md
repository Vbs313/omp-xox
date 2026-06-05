# Memory Tools

Layered memory system (L1-L4) inspired by GenericAgent. Works alongside OMP's `memory.backend: local`.

GenericAgent equivalent: L1 Insight Index, L2 Global Facts, L4 Session Archive.

## Tools

### `l2_fact`

Read or write global facts — environment-specific knowledge the LLM cannot infer.

| Parameter | Type | Description |
|---|---|---|
| `action` | `read \| add \| remove` | Operation |
| `key` | string? | Fact key (e.g. `db-host`, `api-base-url`) |
| `value` | string? | Fact value (required for add) |

Stored in `.omp-xox/memory/l2-global-facts.md` as Markdown sections.

### `distill_session`

Compress the current session's key learnings into L4 session archive.

| Parameter | Type | Description |
|---|---|---|
| `summary` | string | What was accomplished this session |
| `learnings` | string[]? | Key takeaways, pitfalls, patterns |
| `tags` | string[]? | Tags for cross-session search |

## Memory Layers

| Layer | Name | Tool | Storage |
|---|---|---|---|
| L1 | Insight Index | `l1_insight` (skill-evolver) | `.omp-xox/l1-insight.json` |
| L2 | Global Facts | `l2_fact` | `.omp-xox/memory/l2-global-facts.md` |
| L3 | Task Skills | `crystallize_skill` (skill-evolver) | `skills/omp-xox-evolved/*/SKILL.md` |
| L4 | Session Archive | `distill_session` | `.omp-xox/memory/l4-sessions/*.md` |

## GA Design Principles Applied

1. **Action-Verified Only** — no facts without execution evidence
2. **Minimum Sufficient Pointer** — L1 is keyword→skill, ≤50 entries
3. **No Volatile State** — facts are environment config, not runtime state

## Configuration

```json
// .omp-xox/memory-tools.json
{
  "enabled": true,
  "memoryDir": ""
}
```

Env: `OMP_MEMORY_TOOLS=0` to disable.

## Technical

- Filesystem-based (`.omp-xox/memory/`) — no external DB
- `l2_fact` uses regex-based section replace for atomic key updates
- `distill_session` writes timestamped Markdown with YAML frontmatter
- See `extensions/memory-tools/index.ts`
