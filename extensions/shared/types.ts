// omp-xox v2: Capability Contract type system
// Based on Anthropic 2026 Agentic Coding Trends Report & "Building Effective Agents"

export type AgentMode = "subagent";

export type ThinkingLevel = "off" | "minimal" | "low" | "medium" | "high" | "xhigh";

export interface AgentBudget {
  modelRole: string;
  thinking: ThinkingLevel;
  maxTurns: number;
  maxTokens: number;
}

export interface VerificationCheck {
  type: "test-pass" | "lint-pass" | "no-new-todos" | "diff-limit" | "custom";
  command?: string;
  critical: boolean;
  maxLines?: number;
}

export interface EscalationRule {
  condition: string;
  action: "escalate_to_human" | "escalate_to_review_agent" | "abort" | "retry_with_thinking";
}

export interface CapabilityContract {
  id: string;
  name: string;
  provides: string[];
  mode: AgentMode;
  budget: AgentBudget;
  tools: string[];
  verification: string[];
  escalation: EscalationRule[];
  prompt: string;
}

/** Maps a capability string → agent + model configuration + omp agent type */
export interface CapabilityEntry {
  id: string;
  agent: string;
  /** omp bundled agent type for the task tool: explore/plan/task/quick_task/reviewer/oracle */
  ompAgentType: string;
  modelRole?: string;
  thinking?: ThinkingLevel;
  timeoutSeconds: number;
  maxRetries: number;
}

export interface TaskNode {
  id: string;
  capability: string;
  prompt: string;
  dependsOn: string[];
  context?: { files?: string[]; maxTurns?: number };
}

export interface NodeResult {
  nodeId: string;
  status: "completed" | "failed" | "escalated";
  output: string;
  verificationResults: VerificationResult[];
  tokensUsed: number;
  elapsedMs: number;
}

export interface VerificationResult {
  type: string;
  passed: boolean;
  output?: string;
}
