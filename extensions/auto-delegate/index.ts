// omp-xox v2: Auto-Delegate — Natural language → specialized agent routing
// Implements oh-my-openagent's pattern: user types "审查代码"
// → system auto-routes to reviewer agent via omp's task tool.
//
// Strategy: inject routing rules into the system prompt at agent start.
// The LLM reads natural language, matches keywords, and auto-delegates.
// No tool call needed. No hook rewriting needed.
//
// Based on: oh-my-openagent keyword-detector → injects delegation directive
// Adapted for omp: uses before_agent_start → appends routing rules to system prompt

import type { ExtensionAPI } from "@oh-my-pi/pi-coding-agent";

// ── Routing Table ──

interface Route {
  keywords: RegExp;
  agentType: string;
  agentName: string;
  model: string;
  tools: string;
  readOnly: boolean;
}


const ROUTES: Route[] = [
  {
    keywords: /审查|review|code.review|检查代码|评审|audit|assess|安全审查|security.review/i,
    agentType: "reviewer", agentName: "Code Reviewer", model: "default",
    tools: "read, grep, git_diff, git_log, lsp, ast_grep", readOnly: true,
  },
  {
    keywords: /实现|implement|写代码|编写|创建|开发|build|code|write.code/i,
    agentType: "task", agentName: "Software Engineer", model: "default",
    tools: "read, bash, edit, write, grep, glob, lsp, ast_grep, safe_edit, git_diff, git_log, git_status, run_tests", readOnly: false,
  },
  {
    keywords: /修复|fix|修|bug|错误|error|缺陷|补丁|debug|调试/i,
    agentType: "task", agentName: "Software Engineer", model: "default",
    tools: "read, bash, edit, write, grep, glob, lsp, ast_grep, safe_edit, git_diff, git_log, run_tests", readOnly: false,
  },
  {
    keywords: /重构|refactor|重写|rewrite|优化结构|clean.*up/i,
    agentType: "task", agentName: "Software Engineer", model: "default",
    tools: "read, bash, edit, write, grep, glob, lsp, ast_grep, safe_edit, git_diff, git_log, run_tests", readOnly: false,
  },
  {
    keywords: /探索|explore|搜索|search|find|找|查|定位|了解|查看|看看|show|list|ls|grep|glob/i,
    agentType: "explore", agentName: "Code Explorer", model: "smol",
    tools: "read, grep, glob, lsp, ast_grep, git_log, git_status", readOnly: true,
  },
  {
    keywords: /规划|plan|设计|design|架构|architect|方案|spec/i,
    agentType: "plan", agentName: "Planner / Architect", model: "default",
    tools: "read, grep, glob, lsp, ast_grep, git_log", readOnly: true,
  },
  {
    keywords: /测试|test|验证|verify|检查|运行测试|run.test/i,
    agentType: "quick_task", agentName: "Verifier", model: "default",
    tools: "read, bash, grep, run_tests, git_diff, git_log, lsp", readOnly: true,
  },
];

function buildRoutingPrompt(): string {
  const lines = [
    "## Auto-Delegation Rules",
    "",
    "When the user asks you to do something, check if it matches any of these patterns.",
    "If it does, use the `delegate` tool to spawn a specialized sub-agent. Do NOT do the work yourself — delegate it.",
    "",
    "| User intent | delegate capability |",
    "|-------------|-------------------|",
  ];

  for (const r of ROUTES) {
    const cap = r.agentType === "task" ? "implement" : r.agentType === "quick_task" ? "verify" : r.agentType;
    lines.push(`| ${r.keywords.source.replace(/\\/g, "").replace(/\/i$/, "").slice(0, 50)} | \`${cap}\` ${r.readOnly ? "🔒" : "🔧"} |`);
  }

  lines.push(
    "",
    "### How to delegate",
    "```",
    "Call the `delegate` tool with:",
    "  capability: <from table above>",
    "  task: <user's request, verbatim>",
    "```",
    "",
    "If no pattern matches, or the task is trivial (e.g., 'hello', 'what is 2+2'), handle it directly.",
    "For exploration tasks ('看看', '了解', '有哪些'), use capability=explore.",
    "For review tasks ('审查', 'review'), use capability=review.",
    ""
  );

  return lines.join("\n");
}

// ── Extension Entry ──

export default function autoDelegate(pi: ExtensionAPI) {
  let enabled = true;
  let routedCount = 0;
  let injected = false;

  pi.setLabel("omp-xox Auto-Delegate");

  const routingPrompt = buildRoutingPrompt();

  pi.on("before_agent_start", async (_event, ctx) => {
    if (!enabled || injected) return;
    injected = true;
    ctx.ui.notify(`Auto-Delegate: ${ROUTES.length} routing rules active`, "info");

    // Inject routing instructions into the system context (once per session)
    return {
      message: {
        customType: "auto_delegate_rules",
        content: routingPrompt,
        display: "Auto-delegation rules injected",
        details: { routes: ROUTES.length },
      },
    };
  });


  pi.registerCommand("auto-delegate", {
    description: "Show or toggle auto-delegation routing",
    handler: async (args, ctx) => {
      const sub = args.trim().toLowerCase();
      if (sub === "toggle") {
        enabled = !enabled;
        ctx.ui.notify(`Auto-Delegate: ${enabled ? "ENABLED" : "DISABLED"}`, "info");
      } else if (sub === "routes") {
        const lines = ROUTES.map(r =>
          `- \`${r.agentType}\` (${r.agentName}, model=${r.model}): ${r.readOnly ? "read-only" : "can edit"}`
        );
        ctx.ui.notify(`Routes:\n${lines.join("\n")}`, "info");
      } else {
        ctx.ui.notify(
          `Auto-Delegate: ${enabled ? "ACTIVE" : "OFF"} | ${routedCount} routed | ${ROUTES.length} routes\n/auto-delegate [toggle|routes]`,
          "info"
        );
      }
    },
  });
}
