// omp-xox v3.1: Token budget and context size limits
// Based on OMP's default compaction reserve (16K) and typical model windows.

export const WORKSPACE_MAP_TOKEN_BUDGET = 2000;
export const AUTO_REPAIR_MAX_CYCLES = 3;
export const WORKSPACE_MAP_MAX_FILES = 200;

export const CODE_FILE_EXTS: Record<string, true> = {
  ".ts": true, ".tsx": true, ".js": true, ".jsx": true, ".py": true,
  ".rs": true, ".go": true, ".java": true, ".rb": true, ".swift": true,
  ".kt": true, ".c": true, ".cpp": true, ".h": true, ".hpp": true,
};

export const SKIP_DIRS: Record<string, true> = {
  "node_modules": true, ".git": true, "dist": true, "build": true,
  "__pycache__": true, ".next": true, ".nuxt": true, "target": true,
  "vendor": true, ".cache": true,
};
