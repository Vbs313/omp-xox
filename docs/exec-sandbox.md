# Exec Sandbox

Transparent Docker/Podman container isolation for bash commands. Wraps every bash tool call in a container before OMP executes it.

Codex CLI equivalent: bubblewrap sandbox with two-layer security.

## Hook

`tool_call` — fires last in the tool_call chain (after safety-gate, path-guard). Mutates `event.input.command` to wrap in container.

## Two-Layer Security

1. **Sandbox layer** (this module): container isolates filesystem + network
2. **OMP approval layer**: still active — sandbox wrapping happens below approval

## How It Works

```text
LLM calls bash("rm -rf /tmp/build")
    │
    ▼
event.input.command = "docker run --rm --network none
    -v /path/cwd:/path/cwd:rw -w /path/cwd -e HOME=/root
    alpine:latest sh -c 'rm -rf /tmp/build'"
    │
    ▼
OMP bash tool executes the wrapped command
```

## Container Flags

| Flag | Purpose |
|---|---|
| `--rm` | Remove container after execution |
| `--network none` | No network access (configurable) |
| `-v cwd:cwd:rw` | Mount working directory read-write |
| `-w cwd` | Set working directory inside container |
| `-e HOME` | Preserve home directory |

## Configuration

Environment variables:

| Variable | Default | Description |
|---|---|---|
| `OMP_SANDBOX` | `1` | Set to `0` to disable |
| `OMP_SANDBOX_BACKEND` | `docker` | `docker`, `podman`, or path to runtime |
| `OMP_SANDBOX_IMAGE` | `alpine:latest` | Container image |

```json
// .omp-xox/exec-sandbox.json
{
  "enabled": true,
  "backend": "docker",
  "image": "alpine:latest",
  "allowNetwork": false
}
```

## Technical

- Runtime availability checked via `pi.exec("sh", ["-c", "command -v docker"])`
- Falls back gracefully if no runtime found
- Shell escaping: single quotes handled via `'\''` pattern
- Does NOT mount Docker socket — no container escape
- See `extensions/exec-sandbox/index.ts`
