# competitors — light-consistency（跨材料术语 / 指标 / claim 一致性）

> **Round 2 R1 对标判据唯一真相源（SSOT）**。检索与复核日期：**2026-07-01**。
> star 均由当日 GitHub API 读取，写的是**整仓 star**；skills.sh install 只用于发现，不冒充 star。
> 每条真同类都读了固定 commit 下的 `SKILL.md`；有脚本者继续读脚本。工具 / SaaS / 标准只放 §0.B，
> **不顶 §0.A 的同类 skill 名额**。

## 0.A 真同类 agent skills（10 个，逐份读码）

### A1 · Community-Access/accessibility-agents — cross-document-analyzer

- **当日整仓 star**：348★；repo：
  [`Community-Access/accessibility-agents`](https://github.com/Community-Access/accessibility-agents)；
  commit `0872b4a7763145fc0e5847d8357fb446a857c683`。
- **精确路径 / 复验点**：
  [`codex-skills/cross-document-analyzer/SKILL.md` L21-L25](https://github.com/Community-Access/accessibility-agents/blob/0872b4a7763145fc0e5847d8357fb446a857c683/codex-skills/cross-document-analyzer/SKILL.md#L21-L25)
  定义跨文件 / 跨格式 / 文件夹 / 系统性模式；
  [L64-L68](https://github.com/Community-Access/accessibility-agents/blob/0872b4a7763145fc0e5847d8357fb446a857c683/codex-skills/cross-document-analyzer/SKILL.md#L64-L68)
  把基线差异分成 Fixed / New / Persistent / Regressed；
  [L103-L124](https://github.com/Community-Access/accessibility-agents/blob/0872b4a7763145fc0e5847d8357fb446a857c683/codex-skills/cross-document-analyzer/SKILL.md#L103-L124)
  规定 read-only 输出契约，并在只收到部分 scanner 结果时显式宣布 incomplete。
- **它怎样做 consistency**：消费多文档 scanner findings，聚合频率、严重度、模板级根因和修复前后 delta；
  不重新扫描、不改文件。
- **值得借入**：**输入完整性声明 + baseline delta**。跨材料审计不能把“收到 3/5 份材料”说成全覆盖。
- **Light 强 / 弱**：Light 强在项目事实源、科研指标 / claim 门和真实 exit 1；弱在尚无持久化
  Fixed/New/Persistent/Regressed 历史，也没有 scanner 完整率字段。

### A2 · memect/kc — cross-document-verification

- **当日整仓 star**：11★；repo：[`memect/kc`](https://github.com/memect/kc)；
  commit `a48b87f7d97c525aa16043fefc0157695ec4ffb5`。
- **精确路径 / 复验点**：
  [`template/skills/zh/cross-document-verification/SKILL.md` L15-L24](https://github.com/memect/kc/blob/a48b87f7d97c525aa16043fefc0157695ec4ffb5/template/skills/zh/cross-document-verification/SKILL.md#L15-L24)
  要求源文档、锚点实体、目标文档、目标实体、PASS 等级、FAIL 类型；
  [L30-L36](https://github.com/memect/kc/blob/a48b87f7d97c525aa16043fefc0157695ec4ffb5/template/skills/zh/cross-document-verification/SKILL.md#L30-L36)
  规定 case 级比较矩阵；
  [L103-L118](https://github.com/memect/kc/blob/a48b87f7d97c525aa16043fefc0157695ec4ffb5/template/skills/zh/cross-document-verification/SKILL.md#L103-L118)
  要求 verdict 的证据带来源文档与页码。
- **它怎样做 consistency**：把跨文档关系编码成规则专属矩阵，而不是无边界地比较“所有实体 × 所有文件”。
- **值得借入**：权威记录必须同时知道“**从哪份源材料、哪个 locator、与哪个目标比较**”。
- **Light 强 / 弱**：Light 已有可运行的十类检测和统一 findings；该 skill 是 builder、没有同目录 executor。
  Light 弱在现有 YAML 没机械要求每条 canonical / record 带 source + locator。

### A3 · aipoch/medical-research-skills — content-proofreading

- **当日整仓 star**：1,277★；repo：
  [`aipoch/medical-research-skills`](https://github.com/aipoch/medical-research-skills)；
  commit `d92441066ea6259967469be8e0c8c7b6587928ab`。
- **精确路径 / 复验点**：
  [`SKILL.md` L48-L66](https://github.com/aipoch/medical-research-skills/blob/d92441066ea6259967469be8e0c8c7b6587928ab/scientific-skills/Other/content-proofreading/SKILL.md#L48-L66)
  把术语映射、缩写首次出现、synonym 统一和 location/type/fix 报告写进流程；
  [`terminology_manager.py` L47-L58](https://github.com/aipoch/medical-research-skills/blob/d92441066ea6259967469be8e0c8c7b6587928ab/scientific-skills/Other/content-proofreading/scripts/terminology_manager.py#L47-L58)
  的 `Term` 真有 `source`；
  [L656-L760](https://github.com/aipoch/medical-research-skills/blob/d92441066ea6259967469be8e0c8c7b6587928ab/scientific-skills/Other/content-proofreading/scripts/terminology_manager.py#L656-L760)
  真跑 variant / abbreviation / capitalization；
  [L802-L842](https://github.com/aipoch/medical-research-skills/blob/d92441066ea6259967469be8e0c8c7b6587928ab/scientific-skills/Other/content-proofreading/scripts/terminology_manager.py#L802-L842)
  真能导入导出 termbase。
- **它怎样做 consistency**：单稿内中英术语库 + variants + 首次缩写 + 定位报告。
- **值得借入**：把 provenance 做成 term 数据的一等字段，而不是只写在文档说明里。
- **Light 强 / 弱**：Light 强在跨材料、指标真值、claim 强度和 checkpoint；对方强在中英 termbase 与导入导出。
  读码还发现其首次出现判断把**行内 offset**拿去切全文（`full_text[:match.start()]`），多行时可能误判；
  因此不照抄实现。

### A4 · minicoohei/ai-agent-camp — proofreading-agent

- **当日整仓 star**：344★；repo：
  [`minicoohei/ai-agent-camp`](https://github.com/minicoohei/ai-agent-camp)；
  commit `9b99d569cca73cdf84836b44534f0f9021b9c875`。
- **精确路径 / 复验点**：
  [`SKILL.md` L44-L53](https://github.com/minicoohei/ai-agent-camp/blob/9b99d569cca73cdf84836b44534f0f9021b9c875/skills/proofreading-agent/SKILL.md#L44-L53)
  把表记、数字、标点、缩写列成独立 consistency sweep；
  [`proofreading_agent.py` L166-L213](https://github.com/minicoohei/ai-agent-camp/blob/9b99d569cca73cdf84836b44534f0f9021b9c875/skills/proofreading-agent/scripts/proofreading_agent.py#L166-L213)
  从 YAML style profile 拼 preferred/reject 规则；
  [L326-L373](https://github.com/minicoohei/ai-agent-camp/blob/9b99d569cca73cdf84836b44534f0f9021b9c875/skills/proofreading-agent/scripts/proofreading_agent.py#L326-L373)
  调 Gemini 并解析 JSON；
  [L654-L733](https://github.com/minicoohei/ai-agent-camp/blob/9b99d569cca73cdf84836b44534f0f9021b9c875/skills/proofreading-agent/scripts/proofreading_agent.py#L654-L733)
  的 test mode 是预置 issues，不是真跑模型。
- **它怎样做 consistency**：五遍审校中的一遍，profile 可配置，输出行号 / 原文 / 建议 / severity。
- **值得借入**：按检查面分 sweep、允许 scope profile；可用于材料类型差异和误报抑制。
- **Light 强 / 弱**：其 API 异常或 JSON 失败直接 `return []`，存在“失败看起来像零问题”的 fail-open；
  Light 的 gate 异常会 critical fail。对方有日文风格面，Light 不冒充文风裁判。

### A5 · WILLOSCAR/research-units-pipeline-skills — terminology-normalizer

- **当日整仓 star**：474★；repo：
  [`WILLOSCAR/research-units-pipeline-skills`](https://github.com/WILLOSCAR/research-units-pipeline-skills)；
  commit `54c3bdd15e4804ea6230a799b2b589e76f20bb43`。
- **精确路径 / 复验点**：
  [`.codex/skills/terminology-normalizer/SKILL.md` L18-L41](https://github.com/WILLOSCAR/research-units-pipeline-skills/blob/54c3bdd15e4804ea6230a799b2b589e76f20bb43/.codex/skills/terminology-normalizer/SKILL.md#L18-L41)
  分 Taxonomist / Integrator；
  [L61-L71](https://github.com/WILLOSCAR/research-units-pipeline-skills/blob/54c3bdd15e4804ea6230a799b2b589e76f20bb43/.codex/skills/terminology-normalizer/SKILL.md#L61-L71)
  把 taxonomy 当只读 canonical 上游；
  [L77-L95](https://github.com/WILLOSCAR/research-units-pipeline-skills/blob/54c3bdd15e4804ea6230a799b2b589e76f20bb43/.codex/skills/terminology-normalizer/SKILL.md#L77-L95)
  先 harvest 10–30 个候选，再定 canonical/synonym policy。
- **它怎样做 consistency**：从稿件收集候选，以 taxonomy 节点名优先，保守替换正文且保护 citation。
- **值得借入**：**harvest candidate → 人定 canonical** 两阶段，以及“不要把真正不同机制归成同义词”。
- **Light 强 / 弱**：Light 不 autofix、可阻断且有项目级数值 / claim；对方候选生成流程更清楚。
  本轮只借“两阶段”，不借其原地改 `DRAFT.md`。

### A6 · terrylica/cc-skills — glossary-management

- **当日整仓 star**：56★；repo：[`terrylica/cc-skills`](https://github.com/terrylica/cc-skills)；
  commit `1097db1b8a5248ac239b4d61756d95cb35469c74`。
- **精确路径 / 复验点**：
  [`SKILL.md` L11-L23](https://github.com/terrylica/cc-skills/blob/1097db1b8a5248ac239b4d61756d95cb35469c74/plugins/doc-tools/skills/glossary-management/SKILL.md#L11-L23)
  定义 glossary SSoT、跨项目冲突与 Vale 同步；
  [`posttooluse-terminology-sync.ts` L55-L68](https://github.com/terrylica/cc-skills/blob/1097db1b8a5248ac239b4d61756d95cb35469c74/plugins/itp-hooks/hooks/posttooluse-terminology-sync.ts#L55-L68)
  把 file / line / project 放入 term 与 conflict；
  [L216-L285](https://github.com/terrylica/cc-skills/blob/1097db1b8a5248ac239b4d61756d95cb35469c74/plugins/itp-hooks/hooks/posttooluse-terminology-sync.ts#L216-L285)
  真检测 definition / acronym / acronym collision；
  [L467-L490](https://github.com/terrylica/cc-skills/blob/1097db1b8a5248ac239b4d61756d95cb35469c74/plugins/itp-hooks/hooks/posttooluse-terminology-sync.ts#L467-L490)
  虽写 BLOCK，却返回 `exitCode: 0`。
- **它怎样做 consistency**：扫描配置路径中的 CLAUDE.md，汇入全局 glossary，再生成 Vale vocabulary。
- **值得借入**：可配置 scan set、每条冲突保 file/line/project、definition 与 acronym collision 分型。
- **Light 强 / 弱**：Light 的 critical 真 exit 1；对方所谓 BLOCK 实际是可见提醒。对方有自动 glossary→Vale
  广播，Light 目前只在执行审计时消费 `.light/`，没有长期 delta 历史。

### A7 · wordflowlab/novel-writer-skills — story-consistency-monitor

- **当日整仓 star**：232★；repo：
  [`wordflowlab/novel-writer-skills`](https://github.com/wordflowlab/novel-writer-skills)；
  commit `5bc9b373ff609e8910e0e8d179e4a697bf2b1268`。
- **精确路径 / 复验点**：
  [`SKILL.md` L34-L65](https://github.com/wordflowlab/novel-writer-skills/blob/5bc9b373ff609e8910e0e8d179e4a697bf2b1268/templates/skills/quality-assurance/consistency-checker/SKILL.md#L34-L65)
  跨角色档案、世界设定、timeline、旧章节回查并给“改当前材料还是改设定”选项；
  [L98-L137](https://github.com/wordflowlab/novel-writer-skills/blob/5bc9b373ff609e8910e0e8d179e4a697bf2b1268/templates/skills/quality-assurance/consistency-checker/SKILL.md#L98-L137)
  有 strict/flexible/minimal 与 intentional contradiction 抑制；
  [`check-consistency.ps1` L31-L93](https://github.com/wordflowlab/novel-writer-skills/blob/5bc9b373ff609e8910e0e8d179e4a697bf2b1268/templates/scripts/powershell/check-consistency.ps1#L31-L93)
  真查 tracker 文件完整性、章节号、timeline、角色状态；
  [L130-L137](https://github.com/wordflowlab/novel-writer-skills/blob/5bc9b373ff609e8910e0e8d179e4a697bf2b1268/templates/scripts/powershell/check-consistency.ps1#L130-L137)
  真在 error 时 exit 1。
- **它怎样做 consistency**：小说域的多事实源状态一致性；核心机制与科研跨材料同构。
- **值得借入**：intentional exception / scope profile 必须显式登记，不能靠全局降敏。
- **Light 强 / 弱**：Light 的科研事实维度更深；对方有 tracker 文件完整性检查和持久化历史，提醒了
  “registry 缺文件”本身也应成为 finding。

### A8 · aspi6246/Claude-Code-Skills-for-Academics — glossary

- **当日整仓 star**：138★；repo：
  [`aspi6246/Claude-Code-Skills-for-Academics`](https://github.com/aspi6246/Claude-Code-Skills-for-Academics)；
  commit `723235eeac6ed41b24d6681e93f8c148d729889b`。
- **精确路径 / 复验点**：
  [`glossary/SKILL.md` L36-L55](https://github.com/aspi6246/Claude-Code-Skills-for-Academics/blob/723235eeac6ed41b24d6681e93f8c148d729889b/glossary/SKILL.md#L36-L55)
  小表全载、大表只载 headword、按需 grep；
  [L72-L107](https://github.com/aspi6246/Claude-Code-Skills-for-Academics/blob/723235eeac6ed41b24d6681e93f8c148d729889b/glossary/SKILL.md#L72-L107)
  明确主动发现时只 offer、不 auto-add，并用 durable/non-obvious/recurring/project-specific 四条件准入；
  [L184-L193](https://github.com/aspi6246/Claude-Code-Skills-for-Academics/blob/723235eeac6ed41b24d6681e93f8c148d729889b/glossary/SKILL.md#L184-L193)
  要求先读后写、保留用户措辞。
- **它怎样做 consistency**：项目级 glossary 的采纳、读取、瘦身与跨会话使用。
- **值得借入**：harvest 候选准入门和“**offer，不自动加入**”。
- **Light 强 / 弱**：Light 有审计器；对方把 glossary 生命周期与上下文成本处理得更细。

### A9 · tpitsunov/obsidian-skills — Glossary / Terminology Builder

- **当日整仓 star**：14★；repo：
  [`tpitsunov/obsidian-skills`](https://github.com/tpitsunov/obsidian-skills)；
  commit `fef1bf0399c67df9851eb3ff7ef9399c680ac2b6`。
- **精确路径 / 复验点**：
  [`glossary_builder/SKILL.md` L8-L23](https://github.com/tpitsunov/obsidian-skills/blob/fef1bf0399c67df9851eb3ff7ef9399c680ac2b6/glossary_builder/SKILL.md#L8-L23)
  扫目录、抽 recurring terms、跨笔记推断定义、记录 primary sources、生成 source backlink。
- **它怎样做 consistency**：从真实语料 harvest glossary，并把术语回链到来源文件。
- **值得借入**：候选必须保留来源 locator；但“context-inferred definition”只能是候选，不能自动成为项目真值。
- **Light 强 / 弱**：Light 的 ownership 更安全；弱在原实现完全不 harvest，用户要手工从零填表。

### A10 · majiayu000/claude-skill-registry-data — ux-nomenclature

- **当日整仓 star**：12★；repo：
  [`majiayu000/claude-skill-registry-data`](https://github.com/majiayu000/claude-skill-registry-data)；
  commit `6d3690d88506f83355f081edab817833a2484390`。
- **精确路径 / 复验点**：
  [`data/ux-nomenclature/SKILL.md` L9-L25](https://github.com/majiayu000/claude-skill-registry-data/blob/6d3690d88506f83355f081edab817833a2484390/data/ux-nomenclature/SKILL.md#L9-L25)
  把中央产品文档当 glossary authority 并列 forbidden→canonical；
  [L90-L109](https://github.com/majiayu000/claude-skill-registry-data/blob/6d3690d88506f83355f081edab817833a2484390/data/ux-nomenclature/SKILL.md#L90-L109)
  明列 5 个系统与数据文件的 impact set；
  [L111-L124](https://github.com/majiayu000/claude-skill-registry-data/blob/6d3690d88506f83355f081edab817833a2484390/data/ux-nomenclature/SKILL.md#L111-L124)
  给 grep 回扫命令。
- **它怎样做 consistency**：中央 glossary 驱动全系统术语替换和 PR 阻断。
- **值得借入**：定义变更后先形成明确 impact set，再全量回扫。
- **Light 强 / 弱**：Light 支持多类科研事实且不自动改写；对方 scope 清单具体，但规则写死在 skill，
  没有独立 schema / findings / 可验证 gate。

### 0.A 小结：旧结论为何必须改

旧笔记称“consistency-as-skill field 空”，现在证据不支持。更诚实的结论是：

- **直接同构 peer 不多但绝非 0**：跨文档矩阵、跨 scanner 聚合、术语 glossary、项目 nomenclature、
  学术 proofreading、叙事 consistency 都已有 callable `SKILL.md`。
- 头部 peer 也不是没有：本轮读到 1,277★、474★、348★、344★；不能再用 Vale/Xbench 工具替代 skill 调研。
- Light 的差异不是“别人没有术语一致性”，而是组合：
  **科研项目 `.light/` 权威源 + 指标 / claim 专属检测 + canonical findings + checkpoint 真阻断**。

## 0.B 机制锚（工具 / 标准 / 商业产品，不计入 10 个 skill）

| 锚点 | 2026-07-01 可复验证据 | 借什么 / 不借什么 |
|---|---|---|
| **Vale** | [`vale-cli/vale`](https://github.com/vale-cli/vale) 5,518★，commit `24e9634bf4520ee58158079f7fd61b039050a043`；源码有 `internal/check/substitution.go`、`existence.go`、`scope.go` | 借 YAML 受控替换和 markup scope；不把 prose style 当项目事实 |
| **RedPen** | [`redpen-cc/redpen`](https://github.com/redpen-cc/redpen) 605★，commit `875029898b36d9dd4a053a0f925cf7c1a726c6af`；`ValidatorFactory` + document/section validators | 借 validator 组合与 CI；没有项目指标真值 / claim 证据档 |
| **textlint-rule-prh** | [`textlint-rule/textlint-rule-prh`](https://github.com/textlint-rule/textlint-rule-prh) 95★，commit `e625c860e493ba1f9c80b274968d8994521523c9` | 借 expected/actual 词典；不借默认 autofix |
| **DTCG** | [`design-tokens/community-group`](https://github.com/design-tokens/community-group) 2,038★，commit `191bf0b157cd9d254e992975471a64f90d960a78` | 是视觉 token 的正确老师；当前 Light 只指路，不冒充已核像素 |
| **Style Dictionary** | [`style-dictionary/style-dictionary`](https://github.com/style-dictionary/style-dictionary) 4,713★，commit `9a9cca0413c51be65030067c611124194babdf54` | 借 token 多平台广播；不把它当科研 claim SSOT |
| **ApSIC Xbench / Verifika** | 闭源 / 无官方 GitHub star（unknown） | 借 number mismatch、key-term deviation、case / alphanumeric 变体；它们主场是双语 segment |
| **Trinka Consistency Check** | 商业 SaaS、无官方 GitHub star（unknown） | 借全文候选归并 + 人选 canonical；不能成为 Light 完成前提 |
| **Acrolinx** | 商业 SaaS、无官方 GitHub star（unknown） | 借 corpus term discovery / governance；不声称其闭源算法细节 |

外部 style guide、ISO 术语管理原则、期刊 author guidelines 只能定义**表达规范或候选来源**；
不能覆盖项目自己的实验真值。

## 0.C 横向机制提炼（直接驱动 Round 2）

### 1. harvest 与 authority 必须是两个状态

A5/A8/A9 都证明真实用户不会凭空手填完整 glossary：先从稿件 / 笔记 harvest 候选。但 A8 的
“offer、不 auto-add”更适合科研。Light 固定：

```text
file-reading locator/coverage
  → harvest candidate（带 source + locator + confidence）
  → 人确认
  → memory-pm 写入 .light/ canonical
  → consistency 只读回扫
```

候选不得与 canonical 混在同一 registry 后参与阻断。

### 2. “有 YAML”不等于“有权威链”

A2/A3/A6 都把 source、file、line 或页码放入事实 / 冲突结构。Light 原四份 YAML 多数条目只有值，
一旦值错，报告只能说“以 `.light/` 为准”，却不能帮用户复核“`.light/` 为什么对”。

**本轮落地**：新增 warn-only `AUTHORITY_COVERAGE`：

- 四份 registry 缺文件 → warn；
- Markdown-only → 明说只能做部分检查；
- registry 缺 `authority.owner / updated_at` → warn；
- canonical / metric record / claim 缺 `provenance.status=confirmed + source + locator` → warn；
- 不改变原十类检测的 critical 映射。

### 3. 扫描集合本身也是证据

A1 的 incomplete scanner 声明、A6 的 `SCAN_PATHS`、A10 的 5 系统 impact set 指向同一件事：
没读到的文件不能被“零 finding”洗成一致。当前本轮先把这条写入执行资源地图，并以 file-reading
coverage + 明确材料清单执行；后续若要脚本化，优先新增 material manifest，而不是猜仓库里哪些文件算交付物。

### 4. false-positive suppression 要显式、局部、可回查

A4/A7 有 sweep/profile/intentional exception。Light 保留现有 scope-aware code block，
未来 exception 应绑定 `rule + material/section + reason + owner + expiry`，不能全局关掉某类检查。

### 5. 变更要能看 delta

A1 的 Fixed/New/Persistent/Regressed 与 A7 的历史追踪值得补，但本轮不扩代码面：
E2E 记录 before/after findings 与 checkpoint exit code；长期 history 后续归 memory-pm / passport。

### 6. 真“阻断”看 exit code，不看文案

A6 文案说 BLOCK，代码却 `exitCode: 0`；A4 API 失败返回空 issues；A7 才真有 error→exit 1。
Light 必须继续以 `light.findings.v1 → run_checkpoint → exit 1` 为唯一阻断证据。

## 1. Round 2 已落地

1. **R1 纠偏**：从“同类 skill 0”改为 10 个逐份读码 peer；工具另列，不混名额。
2. **小而硬机制**：`AUTHORITY_COVERAGE` warn-only，修复缺 registry / provenance 的静默未覆盖。
3. **R2 入口**：[`consistency-resource-map.md`](../../skills/light-consistency/references/consistency-resource-map.md)
   给真实研究者的 authority→材料清单→全量回扫→人裁→checkpoint 闭环。
4. **仍不动核心**：原十类检测、`.light/` ownership、`light.findings.v1`、critical→checkpoint exit 1
   均保留。

## 2. 诚实边界

1. 同类 skill 的 star 是整仓热度，不代表单个 skill 质量；所以每条同时给路径、commit、行号和代码判读。
2. 很多 peer 只有 prompt；有脚本者也可能 fail-open。不能从 README / SKILL 承诺推断实现。
3. `AUTHORITY_COVERAGE` 只证明 provenance 字段是否齐，不证明来源内容真的正确；source/locator 仍要人回看。
4. 离线 `semantic_sim` 仍会漏纯同义漂移；视觉一致性仍需人工签字。
5. Light 不自动 harvest、不自动改材料、不自动改 `.light/`；这不是功能缺失的掩饰，而是科研权威裁定边界。

## 3. 复核命令

```powershell
# 当日 star / commit
gh api repos/aipoch/medical-research-skills --jq .stargazers_count
gh api repos/WILLOSCAR/research-units-pipeline-skills --jq .stargazers_count
gh api repos/Community-Access/accessibility-agents --jq .stargazers_count
gh api repos/minicoohei/ai-agent-camp --jq .stargazers_count
gh api repos/terrylica/cc-skills --jq .stargazers_count
gh api repos/wordflowlab/novel-writer-skills --jq .stargazers_count

# 本地落地
$env:PYTHONUTF8 = "1"
python skills/light-consistency/scripts/consistency_audit.py --selftest
```

> star、文件内容与服务能力会变；引用前当天重核。查不到写 unknown，绝不编。

## 4. Round 3 主执行者回读与稳定 delta 身份（2026-07-05）

本轮不把 Round 2 的“已读”当作完成，重新 clone 并亲读五个机制最贴近对象：

- `Community-Access/accessibility-agents@0872b4a`（349★）：完整读取
  cross-document-analyzer；其 Fixed/New/Persistent/Regressed 与 incomplete
  scanner 声明仍是最直接的跨文档 delta 参照；
- `aipoch/medical-research-skills@d924410`（1,291★）：完整读取
  content-proofreading SKILL，并读 terminology manager 的 term provenance、
  variant/abbreviation/capitalization、import/export 实现；确认多行缩写首现将
  行内 offset 用于切全文，可能误判；
- `WILLOSCAR/research-units-pipeline-skills@9d27fdb`（479★）：完整读取
  terminology-normalizer；harvest→canonical 两阶段有价值，但它原地改稿且无
  机器 gate；
- `minicoohei/ai-agent-camp@9b99d56`（344★）：完整读取 proofreading skill，
  并读 style-profile、Gemini 调用/JSON 解析/test-mode 实现；API 或 JSON 失败返回
  空 issues，测试又是预置结果，属于 fail-open 反例；
- `wordflowlab/novel-writer-skills@5bc9b37`（233★）：完整读取 consistency
  monitor 与 138 行 PowerShell checker；intentional exception、tracker 完整性和
  error→exit 1 可迁移，小说域内容不可迁移。

当前真同类中仅 AIPOCH 父仓超过 1k stars；没有把 Vale、Style Dictionary 或商业
校对工具伪装成另外四个高星同功能 skills。stars 仍只作采用度线索。

回读 Light 发现 `consistency_delta.py` 的 fingerprint 原来包含 `issue` 自然语言。
同一个冲突只要报告措辞变化，就会被拆成一个 FIXED 和一个 NEW，导致 Persistent /
Regressed 历史失真。现改为：

1. 稳定身份只用 `gate + rule + loc`，issue 文案不参与；
2. 同一身份出现两条 finding 时 fail-closed，要求细化 locator，避免静默覆盖；
3. delta 输出记录 fingerprint version 及 before/after canonical JSON SHA-256；
4. 自测新增“仅改文案仍为 PERSISTENT”、重复身份阻断和输入 digest。

主执行者亲跑 consistency 4/4 selftests，均 exit 0；compileall、ruff、
quick_validate 与 `git diff --check` 通过。准确边界：locator 自身若不稳定或过粗，
仍需生产者提供更稳定、更精确的位置；本门不凭语义猜测两个不同 locator 是否同一问题。
