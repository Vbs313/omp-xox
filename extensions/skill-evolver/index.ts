// omp-xox v3.2: Skill Evolver — crystallize task executions into reusable OMP skills
//
// GenericAgent equivalent: self-evolving skill tree via L3 SOP crystallization.
// Unlike GA's code_run approach, omp-xox writes SKILL.md files that OMP
// auto-discovers and injects as system prompt guidance.
//
// Tools:
//   crystallize_skill — write SKILL.md + update L1 insight index
//   l1_insight        — read/write the insight index (keyword → skill mapping)

import type { ExtensionAPI } from "@oh-my-pi/pi-coding-agent";
import { existsSync, readFileSync, writeFileSync, mkdirSync, readdirSync } from "fs";
import path from "path";
import { loadConfig, envFlag } from "../shared/config-loader.ts";

export interface SkillEvolverConfig {
  enabled: boolean;
  skillDir: string;       // where to write SKILL.md files
  maxSkills: number;       // max skills before prompting cleanup
}

const DEFAULTS: SkillEvolverConfig = {
  enabled: true,
  skillDir: "",           // empty = auto-detect: project .omp/skills or user ~/.omp/agent/skills
  maxSkills: 50,
};

function resolveSkillDir(cwd: string, cfg: SkillEvolverConfig): string {
  if (cfg.skillDir) return cfg.skillDir;
  const projectDir = path.join(cwd, ".omp", "skills", "omp-xox-evolved");
  if (existsSync(path.join(cwd, ".omp"))) return projectDir;
  const home = process.env.HOME ?? process.env.USERPROFILE ?? "/tmp";
  return path.join(home, ".omp", "agent", "skills", "omp-xox-evolved");
}

const L1_INDEX_FILE = ".omp-xox/l1-insight.json";

function loadL1Index(cwd: string): Record<string, string> {
  const fp = path.join(cwd, L1_INDEX_FILE);
  try { return JSON.parse(readFileSync(fp, "utf-8")); } catch { return {}; }
}

function saveL1Index(cwd: string, index: Record<string, string>): void {
  const fp = path.join(cwd, L1_INDEX_FILE);
  mkdirSync(path.dirname(fp), { recursive: true });
  writeFileSync(fp, JSON.stringify(index, null, 2), "utf-8");
}

function slugify(name: string): string {
  return name
    .toLowerCase()
    .replace(/[^\w\u4e00-\u9fff\s-]/g, "")
    .replace(/\s+/g, "-")
    .slice(0, 40);
}

// ---- Extension Entry ----

export default function skillEvolver(pi: ExtensionAPI) {
  const { z } = pi.zod;
  const { config } = loadConfig<SkillEvolverConfig>(
    process.cwd(), "skill-evolver", DEFAULTS,
  );

  if (!envFlag("OMP_SKILL_EVOLVER", config.enabled)) {
    pi.setLabel("omp-xox Skill Evolver (disabled)");
    return;
  }

  pi.setLabel("omp-xox Skill Evolver v3.2");

  // ── Tool: crystallize_skill ──

  pi.registerTool({
    name: "crystallize_skill",
    label: "Crystallize Skill",
    description: "Save a successfully completed task as a reusable OMP skill. The skill auto-loads on next session start.",
    parameters: z.object({
      name: z.string().describe("Short skill name (kebab-case, e.g. 'postgres-backup')"),
      description: z.string().describe("One-line description — used for skill discovery and matching"),
      task: z.string().describe("What task does this skill solve?"),
      patterns: z.string().describe("Key learnings: what worked, pitfalls to avoid, required prerequisites"),
      keywords: z.array(z.string()).optional().describe("Trigger keywords for L1 insight index"),
    }),
    async execute(_id, params, _signal, _onUpdate, _ctx) {
      const cwd = process.cwd();
      const skillDir = resolveSkillDir(cwd, config);
      const slug = slugify(params.name);
      const targetDir = path.join(skillDir, slug);

      // Check max skill count
      mkdirSync(skillDir, { recursive: true });
      const existing = readdirSync(skillDir).filter(d => !d.startsWith("."));
      if (existing.length >= config.maxSkills) {
        return {
          content: [{ type: "text" as const, text: `Skill directory full (${existing.length}/${config.maxSkills}). Consider consolidating or removing unused skills from ${skillDir}.` }],
          details: { status: "full", count: existing.length, max: config.maxSkills },
        };
      }

      mkdirSync(targetDir, { recursive: true });

      // Build SKILL.md with frontmatter
      const frontmatter = [
        "---",
        `name: ${slug}`,
        `description: ${params.description}`,
        "---",
      ].join("\n");

      const body = [
        `# ${params.name}`,
        "",
        "## Task",
        params.task,
        "",
        "## Key Patterns",
        params.patterns,
        "",
        "## Auto-generated",
        `Created by omp-xox skill-evolver at ${new Date().toISOString()}`,
      ].join("\n");

      const skillPath = path.join(targetDir, "SKILL.md");
      writeFileSync(skillPath, `${frontmatter}\n\n${body}`, "utf-8");

      // Update L1 insight index
      const l1 = loadL1Index(cwd);
      const kw = params.keywords ?? params.name.toLowerCase().split(/[\s-]+/);
      for (const k of kw.slice(0, 8)) {
        const key = k.toLowerCase().trim();
        if (key && key.length >= 2) l1[key] = slug;
      }
      saveL1Index(cwd, l1);

      return {
        content: [{
          type: "text" as const,
          text: `✅ Skill crystallized: **${slug}**\n\nFile: \`${skillPath}\`\nL1 keywords: ${kw.slice(0, 5).join(", ")}${kw.length > 5 ? "..." : ""}\n\nThe skill will be available on next session start via OMP's auto-discovery.`,
        }],
        details: { slug, path: skillPath, keywords: kw.slice(0, 8) },
      };
    },
  });

  // ── Tool: l1_insight ──

  pi.registerTool({
    name: "l1_insight",
    label: "L1 Insight",
    description: "Read or update the L1 insight index — maps trigger keywords to crystallized skill names.",
    parameters: z.object({
      action: z.enum(["read", "add", "remove"]).describe("read full index / add keyword→skill / remove keyword"),
      keyword: z.string().optional().describe("Trigger keyword (required for add/remove)"),
      skill: z.string().optional().describe("Skill slug (required for add)"),
    }),
    async execute(_id, params, _signal, _onUpdate, _ctx) {
      const cwd = process.cwd();
      const l1 = loadL1Index(cwd);

      if (params.action === "read") {
        const entries = Object.entries(l1).sort(([a], [b]) => a.localeCompare(b));
        if (entries.length === 0) {
          return {
            content: [{ type: "text" as const, text: "L1 insight index is empty. Use `crystallize_skill` to create skills and populate the index." }],
            details: { count: 0 },
          };
        }
        const lines = entries.map(([k, v]) => `- **${k}** → \`${v}\``);
        return {
          content: [{ type: "text" as const, text: `# L1 Insight Index (${entries.length} entries)\n\n${lines.join("\n")}` }],
          details: { count: entries.length, entries },
        };
      }

      if (params.action === "add" && params.keyword && params.skill) {
        l1[params.keyword.toLowerCase().trim()] = params.skill;
        saveL1Index(cwd, l1);
        return {
          content: [{ type: "text" as const, text: `Added: **${params.keyword}** → \`${params.skill}\`` }],
          details: { keyword: params.keyword, skill: params.skill },
        };
      }

      if (params.action === "remove" && params.keyword) {
        delete l1[params.keyword.toLowerCase().trim()];
        saveL1Index(cwd, l1);
        return {
          content: [{ type: "text" as const, text: `Removed: **${params.keyword}**` }],
          details: { keyword: params.keyword },
        };
      }

      return {
        content: [{ type: "text" as const, text: "Invalid parameters. Use action=read, action=add (with keyword + skill), or action=remove (with keyword)." }],
        details: { status: "invalid" },
      };
    },
  });
}
