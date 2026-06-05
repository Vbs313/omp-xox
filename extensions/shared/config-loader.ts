// omp-xox v3.1: Unified config loader for all extension modules
// Each module reads its own JSON config from .omp-xox/<module>.json (project scope)
// with fallback to ~/.omp/agent/omp-xox/<module>.json (user scope).
// OMP's own config resolution handles env vars and settings.yml — we layer on top.

import { existsSync, readFileSync } from "fs";
import path from "path";

export interface ConfigResult<T> {
  config: T;
  source: "project" | "user" | "default";
  path?: string;
}

/**
 * Load config with project > user > default precedence.
 * Project: <cwd>/.omp-xox/<name>.json
 * User:    ~/.omp/agent/omp-xox/<name>.json
 */
export function loadConfig<T>(cwd: string, name: string, defaults: T): ConfigResult<T> {
  const projectPath = path.join(cwd, ".omp-xox", `${name}.json`);
  const userPath = path.join(
    process.env.HOME ?? process.env.USERPROFILE ?? "/tmp",
    ".omp", "agent", "omp-xox", `${name}.json`
  );

  // Project-level takes priority
  if (existsSync(projectPath)) {
    try {
      const raw = readFileSync(projectPath, "utf-8");
      return { config: { ...defaults, ...JSON.parse(raw) }, source: "project", path: projectPath };
    } catch { /* fall through */ }
  }

  // User-level fallback
  if (existsSync(userPath)) {
    try {
      const raw = readFileSync(userPath, "utf-8");
      return { config: { ...defaults, ...JSON.parse(raw) }, source: "user", path: userPath };
    } catch { /* fall through */ }
  }

  return { config: defaults, source: "default" };
}

/**
 * Resolve env var with optional default. Empty string = disabled.
 */
export function envFlag(name: string, defaultVal = false): boolean {
  const raw = process.env[name];
  if (raw === undefined) return defaultVal;
  if (raw === "" || raw === "0" || raw === "false" || raw === "off") return false;
  return true;
}
