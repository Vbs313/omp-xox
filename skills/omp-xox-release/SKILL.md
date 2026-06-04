# Skill: omp-xox Release

专业化的 omp-xox 扩展包更新、打包、发布工作流。

## 适用场景

- 新增/修改扩展模块后发布新版本
- 修复 bug 后发布补丁版本
- 更新文档后同步发布

## 工作流

### Step 1: 验证（必须）

发布前必须通过所有检查：

```bash
# 1. TypeScript 编译检查
cd /home/vbs/code/pi-xox && bun --eval 'import("./index.ts").then(m=>console.log("OK:",typeof m.default))'

# 2. 检查所有扩展文件存在
ls extensions/*/index.ts | wc -l  # 应为 9

# 3. 检查 marketplace.json 与 package.json 一致性
python3 -c "
import json
pkg = json.load(open('package.json'))
mkt = json.load(open('.claude-plugin/marketplace.json'))
assert pkg['name'] == 'omp-xox', f'package.json name mismatch: {pkg[\"name\"]}'
assert mkt['plugins'][0]['name'] == 'omp-xox', f'marketplace name mismatch'
print('Consistency OK')
"
```

### Step 2: 版本号更新

遵循 semver：
- **MAJOR**: 不兼容的 API 变更
- **MINOR**: 新增扩展/工具（向下兼容）
- **PATCH**: bug 修复、文档更新

同步更新以下文件中的版本号：
1. `package.json` → `version`
2. `.claude-plugin/marketplace.json` → `plugins[0].version`

### Step 3: 更新 CHANGELOG

在 commit message 中描述变更。

### Step 4: 提交并推送

```bash
cd /home/vbs/code/pi-xox

# Stage all changes
git add -A

# Commit with conventional commit format
git commit -m "feat: <description>"   # 新功能
git commit -m "fix: <description>"    # Bug 修复
git commit -m "docs: <description>"   # 文档更新

# Tag the release
git tag -a "v2.0.0" -m "Release v2.0.0"

# Push commit + tags
git push origin main --tags
```

### Step 5: 验证发布

```bash
# 验证 GitHub 上的文件
curl -s https://api.github.com/repos/Vbs313/omp-xox/contents/package.json \
  -H "Accept: application/vnd.github.v3+json" | python3 -c "
import json,sys,base64
d=json.load(sys.stdin)
content=base64.b64decode(d['content']).decode()
pkg=json.loads(content)
print(f\"Published version: {pkg['version']}\")
"

# 验证 marketplace catalog
curl -s https://api.github.com/repos/Vbs313/omp-xox/contents/.claude-plugin/marketplace.json \
  -H "Accept: application/vnd.github.v3+json" | python3 -c "
import json,sys,base64
d=json.load(sys.stdin)
content=base64.b64decode(d['content']).decode()
mkt=json.loads(content)
print(f\"Marketplace plugin version: {mkt['plugins'][0]['version']}\")
"

# 测试 plugin install（dry-run）
omp plugin install github:Vbs313/omp-xox --dry-run
```

## 安装方式（发布后告知用户）

### 方式 1: OMP Plugin Install（推荐）

```bash
omp plugin install github:Vbs313/omp-xox
```

### 方式 2: Install Script

```bash
git clone https://github.com/Vbs313/omp-xox.git
cd omp-xox
./install.sh
```

### 方式 3: Manual settings.json

```json
{ "extensions": ["/path/to/omp-xox"] }
```

## 文件结构

```
omp-xox/
├── .claude-plugin/
│   └── marketplace.json      # 市场目录（必须与 package.json 版本同步）
├── package.json               # 插件清单（omp 字段）
├── install.sh                 # 安装脚本
├── index.ts                   # 统一入口
├── extensions/                # 9 个扩展模块
├── agents/                    # 代理能力契约
├── prompts/                   # 提示词模板
├── skills/                    # 技能定义
└── docs/                      # 文档
```

## 注意事项

- `package.json` 的 `name` 必须为 `omp-xox`（与 marketplace 一致）
- `.claude-plugin/marketplace.json` 的 `plugins[0].source.repo` 必须为 `Vbs313/omp-xox`
- 发布前设置 `GITHUB_TOKEN` 环境变量用于 API 验证
- OMP 版本要求: ≥ 15.9.0
