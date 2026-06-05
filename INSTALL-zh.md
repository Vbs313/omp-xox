# omp-xox — OMP 多智能体扩展包

[English](INSTALL.md) | [中文](#安装)

## 简介

omp-xox 是 [Oh My Pi (OMP)](https://github.com/can1357/oh-my-pi) 的扩展包，提供：

- **多智能体编排** — 基于 DAG 的任务分解与并行子代理
- **结构化开发工具** — hashline 安全编辑器、Git 集成、测试运行器
- **安全门控** — 19 条可配置的 bash 命令规则
- **上下文守卫** — 4 种语义截断策略，处理长会话
- **故障回退** — 3 链模型回退（主模型 → 降级 → 备用）
- **验证门控** — 完成前的 test/lint/todo/diff 检查
- **任务生成器** — 持久化文件系统任务队列 + 代理间邮箱
- **自动委派** — 基于关键词的智能路由
- **知识写入** — 捕获 `/compact` 摘要到 Obsidian 知识库

## 环境要求

- [Oh My Pi (OMP)](https://github.com/can1357/oh-my-pi) ≥ 15.9.0
- Bun 或 Node.js ≥ 18

---

## 安装

### 方式 1：安装脚本（推荐）

```bash
# 克隆仓库
git clone https://github.com/Vbs313/omp-xox.git
cd omp-xox

# 用户级安装（所有项目生效）
./install.sh

# 或项目级安装（仅当前项目生效）
./install.sh --project

# 验证安装
./install.sh --check
```

### 方式 2：手动配置 settings.json

将绝对路径添加到 OMP 配置文件：

**用户级** (`~/.omp/agent/settings.json`)：
```json
{
  "extensions": ["/absolute/path/to/omp-xox"]
}
```

**项目级** (项目根目录下 `.omp/settings.json`)：
```json
{
  "extensions": ["/absolute/path/to/omp-xox"]
}
```

### 方式 3：命令行参数（临时）

```bash
omp -e /path/to/omp-xox
```

### 验证安装

```bash
# 检查注册状态
./install.sh --check

# 在 OMP 中测试
omp --max-turns 1 --print "列出所有 omp-xox 工具"
```

预期输出应包含：`delegate`、`safe_edit`、`archive_to_knowledge`、`run_verification`、`enqueue_task` 等。

### 卸载

```bash
./install.sh --uninstall
```

或手动从 `~/.omp/agent/settings.json` 中删除路径。

---

## 使用方式

### 自然语言（自动委派）

直接用自然语言描述任务，auto-delegate 模块会自动检测意图并路由：

```
审查当前代码的安全性          → reviewer agent
修复登录超时的bug            → task agent (fix)
探索认证模块的代码结构        → explore agent
规划新的缓存架构             → plan agent
```

### 显式委派

```
delegate task="审查认证模块" capability=review
```

### 任务编排

```
/orchestrate "实现 OAuth 登录并添加单元测试"
```

### 知识归档

```
/archive                          # 归档最近的 /compact 摘要
/archive OAuth 实现方案            # 自定义主题
```

或通过工具调用：
```
archive_to_knowledge topic="解决方案" content="..." domain="AI-Agent"
```

---

## 模块列表

| 模块 | 工具 | 命令 | 钩子 |
|------|------|------|------|
| [DAG 调度器](docs/dag-scheduler.md) | `delegate`、`agent_status` | `/orchestrate` | — |
| [开发工具](docs/dev-tools.md) | `safe_edit`、`git_diff`、`git_log`、`git_status`、`git_blame`、`run_tests` | — | — |
| [安全门控](docs/safety-gate.md) | — | `/safety` | `tool_call` |
| [上下文守卫](docs/context-guard.md) | — | `/context` | `tool_result` |
| [故障回退](docs/fallback-pipeline.md) | — | `/fallback` | `session_error` |
| [验证门控](docs/verification-gate.md) | `run_verification` | `/verify` | — |
| [任务生成器](docs/task-spawner.md) | `enqueue_task`、`mark_task`、`task_status`、`collect_task`、`mailbox_send`、`mailbox_read` | `/tasks` | — |
| [自动委派](docs/auto-delegate.md) | — | `/auto-delegate` | `before_agent_start` |
| [知识写入](extensions/knowledge-writer/) | `archive_to_knowledge` | `/archive`、`/knowledge` | `compact_output` |

## 代理（能力契约）

| 代理 | 能力 | OMP 代理类型 | 只读 |
|------|------|-------------|------|
| `swe` | implement、fix、refactor | task | 否 |
| `explore` | explore、search、map、trace | explore | 是 |
| `verify` | verify、test、audit、check | quick_task | 是 |
| `review` | review、critique、assess | reviewer | 是 |
| `plan` | plan、design、spec、architect | plan | 是 |

---

## 架构

```
用户: "审查当前代码"
  │
  ├─ auto-delegate 检测到"审查" → 路由到 review 能力
  ├─ delegate 工具解析能力 → 找到 "review" 代理契约
  ├─ 从 agents/review.md 构建系统提示词
  ├─ pi.pi.createAgentSession({ systemPrompt })
  ├─ session.prompt(task)
  ├─ session.waitForIdle()
  └─ 返回结构化审查结果
```

---

## 目录结构

```
omp-xox/
├── index.ts                    # 统一入口（加载全部 9 个扩展）
├── package.json                # OMP 扩展清单
├── install.sh                  # 安装脚本
├── extensions/
│   ├── dag-scheduler/          # 多智能体编排
│   ├── dev-tools/              # safe_edit、git_*、run_tests
│   ├── safety-gate/            # Bash 命令规则
│   ├── context-guard/          # 上下文截断
│   ├── fallback-pipeline/      # 模型回退链
│   ├── verification-gate/      # 完成前验证
│   ├── task-spawner/           # 持久化任务队列
│   ├── auto-delegate/          # 关键词路由
│   ├── knowledge-writer/       # Compact → Obsidian 归档
│   └── shared/                 # 共享工具
├── agents/                     # 代理能力契约
│   ├── explore.md
│   ├── plan.md
│   ├── review.md
│   ├── swe.md
│   └── verify.md
├── prompts/                    # 可复用提示词模板
│   ├── code-review.md
│   ├── debug.md
│   ├── document.md
│   ├── explain.md
│   ├── generate-tests.md
│   ├── implement.md
│   ├── optimize.md
│   └── refactor.md
├── skills/                     # OMP 技能定义
│   ├── code-analysis/
│   ├── code-review/
│   ├── documentation/
│   ├── debugging/
│   ├── refactoring/
│   └── test-generation/
└── docs/                       # 模块文档
```

---

## 许可证

MIT
