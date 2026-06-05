# Skill Evolver

Crystallize completed task executions into reusable OMP skills. Self-evolving skill tree — the longer you use omp-xox, the more skills accumulate.

GenericAgent equivalent: L3 SOP crystallization via `code_run`. omp-xox writes SKILL.md files that OMP auto-discovers and injects as system prompt guidance.

## Tools

### `crystallize_skill`

Save a successfully completed task as a reusable skill.

| Parameter | Type | Description |
|---|---|---|
| `name` | string | Short skill name (kebab-case, e.g. `postgres-backup`) |
| `description` | string | One-line description — used for skill discovery and matching |
| `task` | string | What task does this skill solve? |
| `patterns` | string | Key learnings: what worked, pitfalls, prerequisites |
| `keywords` | string[]? | Trigger keywords for L1 insight index |

Writes to `~/.omp/agent/skills/omp-xox-evolved/<name>/SKILL.md` (user) or `<project>/.omp/skills/omp-xox-evolved/<name>/SKILL.md` (project).

### `l1_insight`

Read or update the L1 insight index — maps trigger keywords to skill names.

| Parameter | Type | Description |
|---|---|---|
| `action` | `read \| add \| remove` | Operation |
| `keyword` | string? | Trigger keyword (required for add/remove) |
| `skill` | string? | Skill slug (required for add) |

## How It Works

```text
LLM completes a difficult task
    │
    ▼
LLM calls crystallize_skill(
  name="postgres-backup",
  description="Safe PostgreSQL backup with verification",
  task="Backup a PostgreSQL database to S3 with integrity check",
  patterns="- Use pg_dump -Fc for compressed format\n- Always verify with pg_restore --list\n- Set PGPASSWORD via env, not CLI",
  keywords=["postgres", "backup", "pg_dump", "s3"]
)
    │
    ▼
Writes ~/.omp/agent/skills/omp-xox-evolved/postgres-backup/SKILL.md
Updates .omp-xox/l1-insight.json: {"postgres": "postgres-backup", "backup": "postgres-backup", ...}
    │
    ▼
Next session: OMP auto-discovers the skill → injects into system prompt
Workspace-map reads L1 index → skill matching via keywords
```

## Configuration

```json
// .omp-xox/skill-evolver.json
{
  "enabled": true,
  "skillDir": "",
  "maxSkills": 50
}
```

Env: `OMP_SKILL_EVOLVER=0` to disable.

## Integration

- OMP auto-discovers `SKILL.md` files under `skills/` directories
- L1 index persists in `.omp-xox/l1-insight.json` (project scope)
- Works with OMP's `skill://<name>` URL protocol for on-demand reading

## Technical

- Skills are Markdown (no code execution — security-safe)
- `maxSkills: 50` prevents unbounded growth
- Skill content is LLM-written guidance, not executable code
- See `extensions/skill-evolver/index.ts`
