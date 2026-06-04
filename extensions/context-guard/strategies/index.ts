// omp-xox v2: Context Guard — Semantic truncation strategies per tool type
// Based on Anthropic BEA: "Tailoring capabilities to your specific use case"
// Not just truncation — semantically aware content preservation

// ── Strategy interface ──

export interface TruncationStrategy {
  /** Which tools this strategy applies to */
  tools: string[];
  /** Maximum characters before truncation */
  maxChars: number;
  /** Apply strategy to the content, return truncated text */
  apply(text: string, details?: { exitCode?: number; error?: string }): string;
}

// ── Strategies ──

/** Bash: keep errors and tail. Test failures are the most important signal. */
export const bashStrategy: TruncationStrategy = {
  tools: ["bash"],
  maxChars: 8000,
  apply(text, details) {
    if (text.length <= this.maxChars) return text;

    const lines = text.split("\n");

    // Always preserve error lines
    const errorLines = lines.filter(l =>
      /error|fail|Error|FAIL|exception|panic|Aborted|Segfault/i.test(l)
    );

    // Last 30 lines (errors tend to be at the end)
    const tail = lines.slice(-30);

    // If there are specific error lines, keep them + context
    const kept = new Set<string>();
    for (const el of errorLines) {
      const idx = lines.indexOf(el);
      kept.add(el);
      // Keep ±3 context lines around each error
      for (let i = Math.max(0, idx - 3); i < Math.min(lines.length, idx + 4); i++) {
        kept.add(lines[i]);
      }
    }
    for (const tl of tail) kept.add(tl);

    const result = [...kept].join("\n");
    if (result.length > this.maxChars) {
      return result.slice(0, this.maxChars) + `\n... [truncated ${text.length - this.maxChars} more chars]`;
    }
    return result + `\n... [${lines.length - tail.length} earlier lines truncated, ${errorLines.length} errors preserved]`;
  },
};

/** Read: collapse function bodies for large files, keep signatures */
export const readStrategy: TruncationStrategy = {
  tools: ["read"],
  maxChars: 15000,
  apply(text) {
    if (text.length <= this.maxChars) return text;

    // For read output, keep the header + first N and last N lines
    const lines = text.split("\n");
    const head = lines.slice(0, 80);  // imports + first functions
    const tail = lines.slice(-40);     // last functions

    return [
      ...head,
      `... [${lines.length - 120} lines elided — re-read with line ranges for specific sections]`,
      ...tail,
    ].join("\n");
  },
};

/** Grep/Glob: deduplicate, group by file, limit results */
export const grepStrategy: TruncationStrategy = {
  tools: ["grep", "glob"],
  maxChars: 10000,
  apply(text) {
    if (text.length <= this.maxChars) return text;

    const lines = text.split("\n");
    // Group by file (lines starting with non-whitespace after a header)
    const seen = new Set<string>();
    const unique: string[] = [];
    for (const line of lines) {
      const normalized = line.trim();
      if (!seen.has(normalized)) {
        seen.add(normalized);
        unique.push(line);
      }
      if (unique.length >= 60) break;
    }

    const result = unique.join("\n");
    if (result.length > this.maxChars) {
      return result.slice(0, this.maxChars) + `\n... [${lines.length - unique.length} duplicates removed, further truncated]`;
    }
    return result + `\n... [${lines.length - unique.length} duplicate lines removed]`;
  },
};

/** Default: truncate to maxChars, keep head + tail */
export const defaultStrategy: TruncationStrategy = {
  tools: ["*"],
  maxChars: 12000,
  apply(text) {
    if (text.length <= this.maxChars) return text;
    const head = text.slice(0, Math.floor(this.maxChars * 0.6));
    const tail = text.slice(-Math.floor(this.maxChars * 0.4));
    return `${head}\n... [${text.length - this.maxChars} chars truncated] ...\n${tail}`;
  },
};

/** All strategies in priority order (first match wins) */
export const ALL_STRATEGIES: TruncationStrategy[] = [
  bashStrategy,
  readStrategy,
  grepStrategy,
  defaultStrategy,
];

/** Find the strategy for a given tool name */
export function strategyFor(toolName: string): TruncationStrategy {
  for (const s of ALL_STRATEGIES) {
    if (s.tools.includes(toolName) || s.tools.includes("*")) return s;
  }
  return defaultStrategy;
}
