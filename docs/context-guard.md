# Context Guard

## Overview

Semantic context management — preserves important information while truncating noise. Detects omp's native minimizer to avoid double-truncation.

## Files

- `extensions/context-guard/index.ts`
- `extensions/context-guard/strategies/index.ts`

## How It Works

```
tool_result(tool, output > 2000 chars)
  → Skip if omp minimizer already truncated ([Output truncated...])
  → Match strategy by tool name
  → Apply semantic truncation
  → Append: [CG: 15000→8000]
```

## Strategies

### Bash (max 8000 chars)

Preserve error lines + 3 context lines. Keep last 30 lines. Errors are the most important signal in bash output.

### Read (max 15000 chars)

Keep first 80 lines (imports + initial functions) and last 40 lines. Middle replaced with elision notice.

### Grep (max 10000 chars)

Deduplicate by normalized content. Limit to 60 unique matches.

### Default (max 12000 chars)

60% from start, 40% from end.

## Configuration

| Setting | Default |
|---------|---------|
| enabled | true |
| minTriggerChars | 2000 |

## Slash Command

`/context [status|toggle|reset]`
