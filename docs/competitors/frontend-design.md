# frontend-design 对标深读（前端设计 · 在线找灵感 + 反 AI-slop + 可落地 + 视觉无障碍）

> 设计真相源 = 蓝图 §4.4（工程能力 2 个**按需**；frontend「好看≠能用、视觉记忆点、风格统一、适配场景、可落地实现、删本地库改在线找灵感」）。
> **门型（一手核实，非转述）**：`run_checkpoint.py STAGE_GATES` / `reroute.py ROUTES` / `orchestrator-spec.md` **三处 grep `frontend` 零命中**
> ⇒ frontend-design **非 DAG 节点、非 STAGE_GATES 闸门、非回边发起方**，是**按需工程纯工具**。**复用** `_shared/visual_qa`（contrast 门，同 figure），
> 但 **`emits: none`、不产 `light.findings.v1`、不被 run_checkpoint 聚合**（off-DAG 的按需技能套 findings 是死仪式，无消费者）。
> 本笔记 **2026-06-22 上网一手核实**（npm view 真版本 + Awwwards 实测可达 + WCAG 2.2 + AI-slop 竞品，非凭记忆，铁律 2）。
>
> 核心哲学：**好看 ≠ 能用**——给的不是图、是**能跑的 React/Tailwind/shadcn 代码**；有**视觉记忆点**（signature element）、**风格自洽**
> （design tokens 一致）、**适配场景**（学术海报/数据大屏/管理后台/移动端信息密度各不同）、**反「一眼 AI」**（紫蓝渐变/Inter/16px 圆角/
> 巨型 hero/卡片堆叠/居中堆叠）、**视觉无障碍**（WCAG 2.2，复用 `_shared/visual_qa` 不重造）、**零本地设计库**（在线找灵感 + 当天核版本）、
> **绝不替用户拍板设计方向/技术栈/配色**（决策点 AskUserQuestion）。市面分三类：**AI builder**（v0/Lovable/bolt——快但泛 AI-slop）、
> **anti-slop skill**（Hallmark/Anthropic frontend-design——抓痕迹但不落 WCAG 机检门、不接科研 token SSOT）、**组件/token 库**
> （shadcn/Style Dictionary——给料不判可访问/不反 slop）。**没有一个**同时把【反 AI-slop 机检 + WCAG 复用 visual_qa + 可数版面门 +
> 在线找灵感零本地库 + 决策点不替用户拍板】这五件捏在一起——这是 Light frontend 的特化空间。
> （**诚实更正**：v1 曾把前端 token 绑到 `db05` 视觉 SSOT;**一手核 v2 无任何 design_tokens 文件、consistency(a07) 只管
> claims/术语/方法/指标一致性、不管视觉 token**——故 v2 frontend 的 design token 是**用户项目内部自治**,不绑 Light 中央视觉库;下文凡涉 db05 处均按此更正。）

> **Round 2 重做（R1，2026-06-23，上网一手核，铁律 2）**：批 N① 初版把"真·同类设计 **skill**"与"机制锚（库/规范/范本/builder）"**混在一张 12 行表**，真·同类设计 skill 只正经列了 ~2 个（Anthropic frontend-design / Hallmark）。审计 §C4c **已判 ⚠ 漏检高 star 同类**（点名 taste-skill 48878★ / Frontend-Design-Toolkit 376★）——比 figure 好（figure 审计误判"稀疏"），但仍漏。本轮按 R1 硬指标把真·同类设计 **skill** 补到 **≥8**（§0.A，多渠道实搜读码、当天核 GitHub star），与"机制锚"（§0.B）**分表**；新增 §0.C 横向机制提炼。
> **关键诚实发现（与 figure 同型）**：前端设计 skill 这一类**既多又高 star**——**ui-ux-pro-max 95.4K★、taste-skill 49.4K★** 是全市场最高 star 的设计 skill 之一；且头部同类**已覆盖反 slop + a11y 清单 + 组件找料**整套"前端质量 catalog"。Light **非"想到 AI-slop/对比度"独创**；真增量=**把质量做成确定性机检门**（ai_tell_lint 机械抓 T1–T8 + contrast_lint **复用 visual_qa 真算 WCAG 比值**[非 ui-ux-pro-max 的"清单 mandate 4.5:1"] + audit_checklist 可数阈值）+ **零本地库在线找灵感** + **决策点不替用户拍板**。详见 §0.C + 超越点。star 均 **2026-06-23 核 GitHub repo 页**（外部可变，带 snapshot）。
>
> **Round 3 续补（2026-07-05）**：`design_delivery_gate.py` 复查发现旧 READY 门只核三视口 screenshot 文件存在/非空，未绑定截图字节；
> `browser_qa.py` 现为每张截图输出 `screenshot_sha256`，delivery gate 同时核 browser report 的截图 hash 与 render-review 截图 hash。
> 这防止“浏览器 QA/人工回看用的是 A 截图，交付时截图已被替换成 B”的假 READY；仍不宣称自动判断审美顶级。

## 0.A 真·同类前端/UI 设计 SKILL（8 真同类 · R1 硬指标 · star=[snapshot 2026-06-23, src=GitHub repo 页]）

> 判据：别人把"前端/UI 设计"做成**可被 agent 发现并调用的技能/插件**（SKILL.md / plugin）。按 star 降序；builder/库/规范/范本进 §0.B。

| # | 同类 skill（star） | 它怎么做（已读 README/SKILL/脚本，带可复验点） | 我借进哪 | 我诚实差在哪 |
|---|---|---|---|---|
| 1 | **nextlevelbuilder/ui-ux-pro-max-skill**（**95.4K★**，全市场最高 star 设计 skill） | v2.0 旗舰 = AI Design System Generator；**`.claude/skills/ui-ux-pro-max/scripts/search.py` 跑 5 路并行 BM25 检索**(161 行业 reasoning rules × 67 styles × 57 字体配对，CSV 数据库)；anti-slop 黑名单("No emojis as icons"/"避 AI 紫粉渐变"/"harsh animations"/prefers-reduced-motion)；**PRE-DELIVERY CHECKLIST**(文本对比 4.5:1/焦点态/responsive 375·768·1024·1440)；25 图型 + 8 landing 风格；出可跑码(React/Vue/Svelte/SwiftUI/Flutter)；多 harness 装(.claude/.cursor/.windsurf/.agents)；`design-system/MASTER.md`+页覆盖跨会话一致 | **search.py BM25 选型**印证"维护知识库+机检索≠凭记忆"(对照我零本地库在线找)；**行业 reasoning rules**结构化定方向(我 ASK 决策点)；**MASTER.md 跨会话一致**≈ design token 自治 | **它最强但机检在"搜索/生成"非"校验"**：对比 4.5:1 是 **checklist mandate(人核)非真算颜色比值的门**；anti-slop 是黑名单 prose 非可复现 lint;无 render-then-look。Light contrast_lint **真算 WCAG 比值**(复用 visual_qa)+ai_tell_lint 可复现+audit_checklist 可数=机检门增量 |
| 2 | **Leonxlnx/taste-skill**（**49.4K★**，审计点名的漏检头部） | "Anti-Slop Frontend Framework for AI Agents"：**纯 prose SKILL.md**(§0 brief 推断/§2 brief→design system map/§8 dark-mode dual-mode 对比&层级 parity/§14 hard pre-flight check)；`npx skills add` 装；强调"读 brief→推断设计方向→不模板化"(variance/motion/density 旋钮)；8 harness(CC/Cursor/Codex/Gemini/v0/Lovable/OpenCode/AI Studio) | **"brief→推断方向→旋钮(variance/density)"**结构化创意方向(强化我 ASK 档)；§8 dark-mode 对比 parity 思路；多 harness SKILL.md 可移植 | **纯 prose 设计意图、无 WCAG 工具**(原话"focuses on design intent rather than WCAG compliance tooling")；无机械 slop lint、无可数版面门、无对比度真算——正是我三脚本机检门空间 |
| 3 | **wilwaldon/Claude-Code-Frontend-Design-Toolkit**（**376★**，审计点名） | "让 CC 输出更好看前端"的**精选合集**：skills+plugins+MCP+CLAUDE.md tricks；含 shadcn+Tailwind+表单一体 skill(themed config/@layer/dark-mode/react-hook-form+zod) | **"合集策展+落地栈组合"**视角(对照我落地默认栈 Vite/Next+Tailwind v4+shadcn) | 是**资源策展**非单一质量门；不机检 slop/对比度、不绑诚实门 |
| 4 | **superdesigndev/superdesign-skill**（**313★**） | "找灵感 + 无限画布迭代设计稿"：CLI 画布(create→iterate draft[branch/replace]→fetch HTML)；`.superdesign/design-system.md`+`replica_html_template/*.html` 提供 UI 上下文；design-to-code 交给 CC 写进码 | **"先找灵感再迭代稿"工作流** + design-to-code 思路(我 R2 找料工作流参照) | **HTML 进出无视觉回看**(无截图/Playwright,与传言不符,实测 repo 无)；**无 a11y/anti-slop/对比度门** |
| 5 | **anthropics/skills · frontend-design**（官方 Claude Code plugin） | 官方反 AI-slop：**principle-based direction**——写码前先想四维(purpose/tone/constraints/differentiation)；**显式 ban** Inter/Roboto/Arial/system/Space Grotesk("AI 过用") | **创意方向方法论锚**(SKILL 的 ASK 档把"定方向"结构化) + ban 清单喂 ai_tell_lint | prose 指导**无机检门**(不机械抓 slop、不判对比度、无可数版面门)、不接 visual_qa |
| 6 | **Hallmark**（开源 anti-slop skill，"one command"） | 一条命令抓 AI-slop：机械标 Inter/紫渐变/nested cards 等 generic 痕迹 | **`ai_tell_lint` 的直接对标**(印证"机械抓 slop"有人走通) | 只抓字体/渐变/卡片几类；Light ai_tell_lint 早有 T1–T8(scroll-cue/eyebrow 编号/version footer/em-dash/orb/玻璃拟态)，且**额外**复用 visual_qa 落 WCAG 门 + audit_checklist 可数门 |
| 7 | **masonjames/shadcnblocks-skill**（**17★**，R2 组件找料直参） | 给 CC "**1,338 blocks(71 类)+1,189 components(60+ 组)**"目录知识(landing/dashboard/ecommerce)；`references/{block,component}-catalog.md`；装 `npx shadcn add @shadcnblocks/hero125`；"价值=目录知识，知道每个 block 干嘛、该荐哪个" | **R2 头牌——"维护组件目录→按需选→装→改"**正是真实用户找料工作流(我 R2 资源地图直接学此范式) | 无算法选型(纯目录知识)；**无 a11y/anti-slop 校验**；找料≠去 slop≠配 token≠过门(Light 补这闭环) |
| 8 | **capraidev/shadcn-claude-skill**（**1★**） | Next.js+Shadcn 知识包：references(CLI/Component Catalog/Forms/Data Tables/Charts/Theming/Blocks/**Accessibility**)+examples(表单校验/数据表/dashboard/图表)；a11y 靠 Radix 内置 + "开发者责任"指引 | **"Radix 内置 a11y + 显式开发者责任"**分工(印证 a11y 部分靠组件库、部分靠校验) | **rules-based 无机械校验**(原话"compliance depends on Claude's adherence")；a11y 是文档指引非机检对比度门 |

> **结论（诚实）**：前端设计 skill 真存在且**高 star**(ui-ux-pro-max 95.4K、taste-skill 49.4K)——审计 §C4c 判 ⚠ 漏检是对的，本轮 R1 补齐 8 真同类。**更要紧**：头部(尤其 ui-ux-pro-max)**已覆盖反 slop 黑名单 + a11y 清单 + 组件找料 + 跨会话一致**整套——Light **不是"唯一想到 AI-slop/对比度"**；差在**机检焦点**：它们机检在"搜索/生成设计知识"(search.py BM25)，质量校验仍是 **prose 黑名单 + 人核 checklist**；**Light 机检在"输出质量校验"**——ai_tell_lint 可复现机标 slop、contrast_lint **复用 visual_qa 真算 WCAG 比值**(非"清单写 4.5:1")、audit_checklist 可数阈值。这"输出质量机检门 + 零本地库在线找 + 决策点不替用户拍板"是 Light frontend 的真增量(§0.C)。

### Round 3 五槽重新认证（2026-07-05）

原 “Sleek/nextlevelbuilder” 复合槽拆除，五个直接 skill 固定为：

1. `nextlevelbuilder/ui-ux-pro-max-skill:ui-ux-pro-max`，100,908★，`4baa399`，MIT；
2. `Leonxlnx/taste-skill:taste-skill`，56,721★，`b177427`，MIT；
3. `anthropics/skills:frontend-design`，父仓 158,286★，`9d2f1ae`；
4. `vercel-labs/agent-skills:web-design-guidelines`，父仓 28,678★，`f8a72b9`；
5. `vercel-labs/agent-skills:react-best-practices`，同一父仓、独立 skill，`f8a72b9`。

前 3 项负责设计方向/反模板化/设计系统，后 2 项负责 UI review 与 React/Next 性能实现；后者是部分同功能，
不冒充纯视觉设计。当前源码复核确认 Vercel web guidelines 运行时抓最新规则，React skill 有 70 条、8 类优先级；
Light 仍需真实 Chromium、截图 hash、WCAG 比值与人工 render review 才能交付，不能只靠规则清单。

## 0.B 机制锚（builder / 库 / 规范 / 范本 —— 不占 skill 名额，仍是有价值的机制/学术锚）

| 机制锚 | 是什么 / 机制 | 取什么（落进哪） | 与 §0.A 区别 |
|---|---|---|---|
| **v0 / Lovable / bolt.new** | prompt→站点 AI builder；按最高频 token 生成 | **反面教材锚**(Inter+蓝紫渐变+16px 圆角卡+"Build the future"巨 hero=ai_tell_lint 抓的特征) | 是**产品/builder**非可调 skill；产物泛 AI-slop |
| **shadcn/ui CLI v4**（@2026-03） | 项目自持 Radix 组件源码；Tailwind v4 `@theme`、HSL→OKLCH、`registry:base` 整套分发、fonts 一等 registry | **落地栈首选**(组件自持可访问可改，铁律 6 例外不重造) | **组件库**非门；不判 slop/对比度/密度 |
| **Tailwind v4**（真 **4.3.1**@2026-06-22） | CSS-first 原子化，`@theme` 定 token、OKLCH、容器查询 | **样式引擎锚** + token 落 CSS 变量载体 | 引擎非门 |
| **WCAG 2.2**（W3C 一手核） | **1.4.3** 文本 4.5:1/大字 3:1；**1.4.11** 非文本 3:1；**2.4.11** 焦点 ≥2px 周长+≥3:1；阈值不四舍五入 | **可访问门硬学术锚**；Light **复用 `_shared/visual_qa`** check_contrast/detect_contrast_issues，不重造数学 | **规范**非工具 |
| **Style Dictionary v4 / Terrazzo（DTCG）** | 单一 token 源→CSS/SCSS/JS/原生多端 | **token 工程化锚**(用户项目内部单源多端；**v2 无 Light 中央视觉 SSOT**) | **工具**非门 |
| **Awwwards**（WebFetch 实测可达 ✓） | 获奖站画廊 SOTD/趋势/filter | **"在线找灵感"一手取数源**(零本地库落地证明) | **灵感画廊**非门 |
| **Mobbin / Dribbble** | 真实 App 截图 / 概念稿画廊 | 移动端/真实产品流程灵感；**诚实分级取数**(login/JS 受限→标 unavailable 走 WebSearch) | 受限画廊非门 |
| **Vercel web-design-guidelines** | 设计规则集(a11y/性能/UX 状态/响应式) | **可用性清单锚**(audit_checklist R1–R7 同源) | prose 规则；Light 落**可数**门 |
| **Linear / Vercel / Stripe** | 顶级产品官网(克制=premium，留白当 feature，1–2 字体清晰字阶，每 section 一主 CTA) | **审美高线锚**(反 slop 正面参照：有记忆点的克制) | **范本**非门 |
| **Motion 12.40 / GSAP 3.15**（真版本核） | 动效库，仅当传达层级用，尊重 prefers-reduced-motion | 动效参考(assets 港 .tsx 片段给用户项目) | **库**非门 |

## 0.C 读完 8 个真同类后的横向机制提炼（驱动 Round 2 frontend 加厚）

**① 反 AI-slop**：**强共识**——ui-ux-pro-max(黑名单"No emojis as icons/避 AI 紫粉渐变")、taste-skill(variance/density 旋钮)、Anthropic(ban Inter/Roboto/Space Grotesk)、Hallmark(机标 Inter/紫渐变/nested cards)。**全是 prose 黑名单/refusal**。Light `ai_tell_lint` 增量=**可复现机标 T1–T8**(标痕迹供人核非 prose)。**校正措辞**：不说"没人反 slop"(假)，说"没人做成可复现 lint"。

**② 可访问/对比度**：ui-ux-pro-max 有 PRE-DELIVERY checklist(4.5:1 mandate)、capraidev 靠 Radix 内置+指引——**但都是清单/组件兜底，无一真算颜色对比比值**。Light `contrast_lint` **复用 `_shared/visual_qa` 真算 WCAG 比值**(从 token/CSS 抽色→算 ratio→判 AA/AAA)=真机检门，**这是硬增量**(头部 95.4K 也只到 checklist)。

**③ 组件找料（R2 头牌）**：shadcnblocks(1338 blocks 目录)、ui-ux-pro-max(搜索生成)、superdesign(找灵感画布)——**"维护目录/资源→按需选→装→改"是真实用户工作流共识**。Light R2 要补的资源地图(21st.dev/React Bits/组件库)直接学此范式，**但加 Light 独有闭环**：找料→**去 slop(ai_tell_lint)→配 token→过 contrast/audit 三门**(同类找完料不校验质量)。

**④ 创意方向结构化**：taste-skill(§0 brief 推断+map)、Anthropic(四维 purpose/tone/constraints/differentiation)、ui-ux-pro-max(161 行业 rules)——**共识=先定方向再产**。Light 落进 **ASK 决策点 AskUserQuestion**(且**绝不替用户拍板**方向/栈/配色，比同类"自动推断"更克制守边界)。

**⑤ 落地栈/可移植**：ui-ux-pro-max/taste-skill 多 harness 装(.claude/.cursor/...)；shadcn/Tailwind v4 是共识落地栈。Light 同栈(Vite/Next+Tailwind v4+shadcn 自持组件)，**增量=零本地库当天 npm view 核版本**(references 不内嵌易腐版本)。

**⑥ render-then-look**：**同类几乎都没有**(superdesign HTML 进出无回看、ui-ux-pro-max checklist 无视觉回看)——Light 批 N① 已有 preview 真截图回看(抓到三门漏的徽章折行)，是真差异化(同 figure 把 render-then-look 接进流程)。

## 逐项一手核要点

### 1. 真实栈版本——当天 `npm view` 核（铁律 2 活教材，v1 内嵌快照已腐）
2026-06-22 实跑 `npm view <pkg> version`（**真在线，非凭记忆**）：

| 包 | 真版本 @2026-06-22 | v1 ecosystem.md 内嵌（2026-06-10） | 漂移 |
|---|---:|---:|---|
| `next` | 16.2.9 | 16.2.9 | — |
| `react` | 19.2.7 | 19.2.7 | — |
| `tailwindcss` | **4.3.1** | 4.3.0 | **+0.0.1（漂了）** |
| `shadcn` | 4.11.0 | 4.11.0 | — |
| `motion` | 12.40.0 | 12.40.0 | — |
| `gsap` | 3.15.0 | 3.15.0 | — |
| `lucide-react` | **1.21.0** | 1.17.0 | **+0.4.0（漂了）** |
| `vite` | 8.0.16 | 8.0.16 | — |

**结论**：12 天内 8 包里 2 个版本漂移。→ v2 references **绝不内嵌版本真相**，只留 `npm view` 复检命令 + 标 `last_checked`；安装前当天核。这正是「零本地库」对栈版本的具体落法。

### 2. AI-slop 特征 + 竞品（`ai_tell_lint` 的对标）
一手核（925studios / prg.sh / Hallmark / Anthropic plugin）：AI builder 按最高频 token 生成 → 默认 **Inter/system 字体 + 蓝紫渐变 + 16px 统一圆角 + 巨型 hero（"Build the future" 空话标题）+ 卡片堆叠**。
- **Hallmark**（开源，"stop AI slop in one command"）与 **Anthropic 官方 frontend-design plugin** 是直接同类——印证「机械抓 slop」与「principle-based direction」两条路都成立。
- Light `ai_tell_lint` 的**增量**：T1–T8 已覆盖 scroll-cue / 装饰性 section 编号 eyebrow / version-footer / 英文 em-dash（避开中文破折号假阳）/ **紫粉渐变** / **emoji 当图标** / **gradient-orb 光斑** / **玻璃拟物**；且**纯启发式非终判**（标痕迹供人核，不当 critical 硬阻）。差异化：Light 不止抓 slop，还**复用 visual_qa 落 WCAG 机检门** + **可数版面门** audit_checklist，三件套自查。
- **正面方向**（principle-based）：告诉模型「想什么」（目的/调性/约束/差异化 + 显式点名不要的默认值），而非「产什么」——落进 SKILL 的 ASK 档 + AskUserQuestion。

### 3. shadcn/ui + Tailwind v4——落地栈（一手核 @2026-06-22）
shadcn CLI **v4（2026-03）**：scaffold Next/Vite/Laravel/React-Router/Astro/TanStack；Tailwind v4 `@theme` + `@theme inline` 全支持，**HSL→OKLCH**；`registry:base` 一次分发整套 design system（组件+CSS 变量+字体+config）；**fonts 成一等 registry 类型**。→ Light 落地默认栈：**Vite+React**（dashboard/工具/原型）或 **Next App Router**（要路由/SSR/SEO/auth）、**Tailwind v4 + CSS 变量 token**、**shadcn/ui** 自持可访问组件、**Motion/GSAP** 仅当动效传达层级时。组件不重造（标准件可用，铁律 6 例外）。

### 4. Awwwards 实测可达——「在线找灵感」可落地（零本地库铁律的证明）
2026-06-22 `WebFetch https://www.awwwards.com/websites/` **真返回**：当前 SOTD（digitalists/RPA/Balmoral/Gucci 等）、趋势（motion/3D/WebGL/minimal/typography）、filter（UI/交互/排版/技术栈）。→ **「在线找灵感」非空话**：当场看获奖站学审美/动效/配色，替代 v1 本地陈旧库。
**取数可达性诚实分级**（须人判、不假装）：Awwwards ✓ WebFetch 可达；**Mobbin** login-gated、**Dribbble** JS-heavy → WebFetch 多受限 → 诚实标 unavailable + 转 WebSearch 摘要（同 venue DOAJ 403 / review-rebuttal OpenReview SSL 降级范式）。设计「事实」（趋势/字体/版本）查到标 `last_checked`，查不到标 unknown，**绝不编**。

### 5. WCAG 2.2——复用 `_shared/visual_qa` 不重造（contrast_lint 的核心改造）
一手核 W3C：**1.4.3** 文本 4.5:1 / 大字 3:1；**1.4.11** 非文本（UI 组件/图标/边框/焦点指示）3:1；**2.4.11**（2.2 新增）焦点外观 ≥2 CSS px 周长 + ≥3:1；阈值**不四舍五入**。→ 这与批 0 `visual_qa.py` 的 `check_contrast(large, level)`（AA 4.5/3.0、AAA 7.0/4.5）**完全同口径**。
**v1 债**：`contrast_lint.py` 自己重写了一遍 `relative_luminance`/`_channel_lin`/`contrast_ratio`/阈值表——**与 visual_qa 重复**。**v2 改造**（同 figure_visual_qa 复用 visual_qa 先例）：规范 bootstrap → `from _shared.visual_qa import check_contrast, detect_contrast_issues, qa_report` → **删本地 WCAG 数学**，只留 v1 真增量 = **token 抽取**（DTCG `$value` 树 / flat map / `pairs` 显式配对 / CSS `--var:#hex`）；role（body/large/ui）映射成 visual_qa 的 `large` 档（body→False、large/ui→True=3:1）。`_shared` 不可达 → **诚实硬报错退出**，绝不偷偷退回本地实现（否则又把债借回来）。

### 6. 适配场景——信息密度按场景分（好看≠能用的硬落点）
一手核（UXPin / Pencil&Paper / Gartner）：**信息过载是头号 dashboard 病（46.7% 用户）**。
- **数据大屏/dashboard**：progressive disclosure（概要先行、下钻见细节）；桌面可比移动密；「快速一瞥」用紧凑、「深度分析」用呼吸；每个数据点须回溯到某个决策（无 actionable insight 的图=废）。2026 移动 BI >60%（Gartner）。
- **营销 landing**：单一转化目标 → attention ratio 1:1（一个 CTA、常**砍导航**减干扰）；不是炫创意是劝转化。
- **管理后台 admin**：效率与完成任务优先，非「停留时长/engagement」；高密度表格/批量操作/键盘可达。
- **学术海报/科研系统**：信息密度高但层级须清（标题→方法→结果→结论），配色克制、图表诚实（与 figure 同口径）。
→ SKILL 必问「**目标场景是什么**」再定密度/审美，不把营销 hero 那套套到 dashboard。

### 7. 高端对标——克制是 premium 信号（反 slop 的正面锚）
一手核（Onething/DigitalSilk/Flux）：**留白当 feature 非剩余**（分组、聚焦、premium 感）；**typography 是质量最清晰的信号**——1–2 字体 + 清晰字阶（如 12-16-20-28）、**typography 不当装饰**；**每 section 一个主 CTA**；minimalism=高端（Apple/Tesla 路线）。→ 反 AI-slop 不是「不许渐变」而是「**有记忆点的克制**」：敢留白、敢非对称、signature element 一处、风格自洽。

### 8. 分工边界（诚实，别越界）
- **与 figure（stage 9）**：figure = 论文里的**数据图表**（matplotlib，诚实性/视觉 QA/绑证据档/critical 门/回炉）；frontend = **交互界面/网页/应用 UI**（React/Tailwind/shadcn，审美/可用/可访问）。**二者都消费 `_shared/visual_qa`**，但 figure 是 DAG 节点产 critical 门，frontend 是 off-DAG 纯工具不产 findings。
- **与设计 token（v2 诚实定位)**：v1 设想「论文图/PPT/前端同取 db05 一份 token」;**一手核 v2 既无 design_tokens 文件、consistency(a07) 也只管 claims/方法/指标一致性,无视觉 token SSOT**。故 v2 frontend 的 token **用户项目内部自治**:DTCG 单源→多端的工程化方法论照用,但**不绑 Light 中央视觉库**;若同项目也用 figure 出论文图,配色/字体由用户/总控**人工对齐**(无中央文件可同取)。
- **与 system-design（批 N②）**：frontend = 界面/前端；system-design = 架构分层/接口/数据流/schema。
- **增量诚实**：「留白好/对比要够/别滥用渐变」是**强 Opus 自带常识，近零增量**。本技能真超出裸模型的是：① **机械抓 AI-slop**（ai_tell_lint T1–T8，可核可复现）；② **复用 visual_qa 把 WCAG 落成机检门**（contrast_lint，非「看着还行」）；③ **可数版面门**（audit_checklist R1–R7 带阈值）；④ **在线找灵感零本地库**（Awwwards 实测可达 + 当天核版本）；⑤ **决策点纪律**（绝不替用户定方向/栈/配色，AskUserQuestion）。

## 取数端点与复检命令（零本地库——值当天核，标 last_checked）

```powershell
# 栈版本（安装前当天核，绝不信内嵌快照）
npm view next version ; npm view react version ; npm view tailwindcss version
npm view shadcn version ; npm view motion version ; npm view gsap version
npm view lucide-react version ; npm view vite version
```

- 灵感（在线找，非本地库）：Awwwards `https://www.awwwards.com/websites/`（✓ WebFetch 可达）· shadcn registry directory `https://ui.shadcn.com/docs/directory` · Mobbin/Dribbble（login/JS 受限→WebSearch 摘要）
- 规范：WCAG 2.2 `https://www.w3.org/TR/WCAG22/`（1.4.3/1.4.11/2.4.11）
- token：Style Dictionary / Terrazzo（DTCG）——用户项目内部单源→多端，**v2 无 Light 中央视觉 SSOT**（不绑 db05）
- 竞品雷达：`npx skills find "frontend design"` / Hallmark / Anthropic frontend-design plugin（依赖前先复验克隆可用性）

> **唯一真相源声明**：本文件是 frontend-design 的对标判据 SSOT；SKILL.md 的 `truth_source` 指向此。版本/趋势/取数可达性随时间变，引用前按上方命令当天复检；查不到标 unknown，绝不编。
