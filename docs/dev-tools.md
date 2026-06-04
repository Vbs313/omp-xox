# Dev Tools

## Files

- `extensions/dev-tools/index.ts` — Unified entry
- `extensions/dev-tools/safe-edit.ts` — Hashline optimistic lock edit
- `extensions/dev-tools/git-ops.ts` — Structured git operations
- `extensions/dev-tools/test-runner.ts` — Framework detection and execution

---

## safe_edit

Edit files with optional hash verification. No hooks — hash is passed explicitly by the LLM.

**Parameters:**
```
path: string        — File path
hash?: string       — Optional 4-char content hash. If provided and file changed, edit rejected.
operations: [{
  op: "replace" | "delete" | "insert_before" | "insert_after"
  range: [startLine, endLine]  — 1-indexed, inclusive
  content?: string[]
}]
```

**Flow:**
```
1. LLM reads file (via omp's read tool)
2. LLM calls safe_edit with or without hash
3. If hash provided: compare against current file content hash
   - Match → apply edits → return new hash
   - Mismatch → reject with error
4. If hash omitted: apply edits directly → return new hash
5. LLM can use new hash for subsequent edits on the same file
```

**Hash algorithm:** `sha1(head(256) + tail(-256) + size).hex().slice(0, 4)`

---

## git_ops

### `git_diff`
```
mode: "staged" | "unstaged" | "all"  (default: staged)
path?: string
stat?: boolean
nameOnly?: boolean
```

### `git_log`
```
maxCount?: number  (default: 20, max: 100)
author?: string
since?: string     ("2026-01-01", "2 weeks ago")
until?: string
path?: string
format?: "oneline" | "medium" | "full"
```

### `git_status`
```
path?: string
```
Returns structured: staged/unstaged/untracked counts + file lists.

### `git_blame`
```
path: string
startLine?: number
endLine?: number
```

---

## run_tests

Auto-detect framework, execute, parse results.

**Detected frameworks (priority order):**

| Framework | Config Files | Command |
|-----------|-------------|---------|
| vitest | vitest.config.{ts,js,mjs} | bun test |
| jest | jest.config.{ts,js,mjs} | bun test |
| mocha | .mocharc.{js,json,yml} | bun test |
| playwright | playwright.config.{ts,js} | bunx playwright test |
| pytest | pytest.ini, pyproject.toml | python -m pytest |
| go-test | go.mod | go test ./... |
| cargo-test | Cargo.toml | cargo test |
| npm-test | package.json#scripts.test | bun run test |

**Output parsing:** Extracts pass/fail/skip counts and failure details (file, test name, error message) from framework-specific output formats.
