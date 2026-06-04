// omp-xox v2: Capability Registry
// Maps task capabilities to agent + model configurations
// Based on Anthropic 2026 Trends: Orchestrator-Workers pattern

import type { CapabilityEntry } from "./types.ts";

export const CAPABILITY_REGISTRY: Record<string, CapabilityEntry> = {
  // ── Exploration ──
  explore: {
    id: "explore", agent: "explore", ompAgentType: "explore",
    modelRole: "smol", thinking: "off", timeoutSeconds: 60, maxRetries: 1,
  },

  plan: {
    id: "plan", agent: "plan", ompAgentType: "plan",
    modelRole: "slow", thinking: "xhigh", timeoutSeconds: 240, maxRetries: 1,
  },

  implement: {
    id: "implement", agent: "swe", ompAgentType: "task",
    modelRole: "slow", thinking: "high", timeoutSeconds: 300, maxRetries: 2,
  },
  fix: {
    id: "fix", agent: "swe", ompAgentType: "task",
    modelRole: "slow", thinking: "high", timeoutSeconds: 300, maxRetries: 2,
  },
  refactor: {
    id: "refactor", agent: "swe", ompAgentType: "task",
    modelRole: "slow", thinking: "high", timeoutSeconds: 300, maxRetries: 2,
  },

  verify: {
    id: "verify", agent: "verify", ompAgentType: "quick_task",
    modelRole: "default", thinking: "low", timeoutSeconds: 120, maxRetries: 1,
  },
  test: {
    id: "test", agent: "verify", ompAgentType: "quick_task",
    modelRole: "default", thinking: "low", timeoutSeconds: 120, maxRetries: 1,
  },

  review: {
    id: "review", agent: "review", ompAgentType: "reviewer",
    modelRole: "slow", thinking: "high", timeoutSeconds: 180, maxRetries: 0,
  },

  quick: {
    id: "quick", agent: "swe", ompAgentType: "quick_task",
    modelRole: "smol", thinking: "off", timeoutSeconds: 120, maxRetries: 1,
  },
};

/** Resolve a capability ID to its entry, with fallback */
export function resolveCapability(capability: string): CapabilityEntry {
  if (CAPABILITY_REGISTRY[capability]) {
    return CAPABILITY_REGISTRY[capability];
  }
  return {
    id: capability, agent: "swe", ompAgentType: "task",
    modelRole: "default", thinking: "medium", timeoutSeconds: 180, maxRetries: 1,
  };
}