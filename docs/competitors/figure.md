# figure 对标深读（图表 · 视觉诚实门 + 图服务论点 + 出版级 + 程序化生成）

> 设计真相源 = 蓝图 §4.3-9 + spec §4.2（stage 9 Critical=**不诚实(截 y 轴/双 y 轴伪相关)**；warn=误差棒缺失、
> 集合超预算；消费 **`visual_qa`**+findings）/§5（回边 **9→7**：图把不显著当主图/图文不一致 → result-analysis）。
>
> **Round 2 重做（R1，2026-06-23，上网一手核，铁律 2）**：批 1 初版**只列了"机制对标"**（样式库 SciencePlots/cnsplots、
> 生成 agent PlotGen/ReLook、学术锚 Cairo/Cumming/Frontiers），真·同类**绘图 skill** 一个没正经列——审计据此判
> "figure 同类 field 稀疏，可辩护 ✅"（审计报告 §9 line 201："同类 ~1，field 稀疏 top 130★"）。**本轮上网实搜直接推翻**：
> 绘图/出图 **skill** 既多又高 star——**deer-flow 73.6K★、K-Dense 29.1K★、davila7 28.2K★、scipilot 530★、antvis 372★、
> ntcoding 318★**……审计的"稀疏"是**同类漏检系统病**（与 lit-search/paper-writing 同病），不是真稀疏。本轮按 R1 硬指标
> 补 **10 个真·同类绘图 skill**（§0.A，多渠道搜：GitHub/skills.sh/awesome-claude-skills/大技能包，优先高 star、真读
> 代码），与"机制对标"（§0.B 样式库/agent/论文/书/引擎/规格）**分表**；新增 §0.C 读完 10 个真同类后的横向机制提炼。
> star 均 **2026-06-23 联网核 GitHub repo 页**（外部可变事实，带 snapshot；star 会涨，以仓库页为准）。
>
> **核心哲学（不变）**：图服务论点（每图支撑哪条 claim、删了缺什么）+ 出版级规格（栏宽/字号/色盲安全/误差棒+n+显著性）
> + 视觉诚实（不偷偷截 y 轴/不双 y 轴伪相关/不 jet-rainbow）+ 渲染后多模态"真看一眼" + 论文数据图程序化生成绝不 AI
> 生图（永久底线）。**本轮关键校正（诚实）**：上述哲学**不是 Light 独创**——头部同类 skill 大多覆盖同一"诚实 catalog"
> （scipilot 18-pitfall、davila7 13-pt checklist 都查截轴/双轴/rainbow/误差棒）；**Light 的真增量是把它做成"确定性机读
> critical 门 + 绑 result-analysis 证据档 + 9→7 回炉 + 集合预算"**，而非"别人没想到截轴会骗人"。见 §0.C④⑥ + 超越点。

---

## 0.A 真·同类绘图/图表 SKILL（10 个真同类 · R1 硬指标 · star=[snapshot 2026-06-23, src=GitHub repo 页]）

> 判据：别人把"绘图/出图/数据可视化"做成一个**可被 agent 发现并调用的技能/插件**（SKILL.md / plugin），
> 而非通用绘图库/引擎/论文/书（那些进 §0.B 机制对标）。按 star 降序；大技能包的 star 是**整包**的，已注明。

| # | 同类 skill（star） | 它怎么做（已读 SKILL/README/脚本，带可复验点） | 我借进哪个能力 | 我诚实差在哪 |
|---|---|---|---|---|
| 1 | **bytedance/deer-flow**（**73.6K★**，star=整 harness） | 超级 agent harness，`skills/public/chart-visualization/SKILL.md` 是其公开技能；**license 标注源自 antvis/chart-visualization-skills**（=第 5 行 vendored）。机制：`scripts/generate.js` 收 JSON payload(`{tool,args}`)→ 出**图片 URL**；按 taxonomy 决策树选型（`generate_line_chart`/`generate_bar_chart`/`generate_sankey_chart`…26+ 型）；`references/generate_*.md` 每型 schema | **高 star = 绘图 skill 真主流的铁证**（推翻"稀疏"）；taxonomy 决策树印证 recommend_chart 选型路径 | 它出**图片**不出可复现代码（与我"程序化生成可核"红线相反）；**零诚实/证据检查**；与 antvis 同机制（不重复计独立增量） |
| 2 | **K-Dense-AI/scientific-agent-skills**（**29.1K★**，star=整包） | "把 AI agent 变 AI Scientist"，**147 个科研 skill + 160K+ 科学家用**；含 `matplotlib`/`seaborn`/`scientific-visualization`/`plotly` 绘图 skill；每 skill 独立 SKILL.md（metadata.version + license） | **"出版级图作为一类可调 skill 嵌进科研工作流"**印证 Light 把 figure 做成 DAG 节点；多 harness 标准（Cursor/CC/Codex）对齐 | 它是**通用科研 skill 集**不绑统一 DAG/证据档；绘图 skill 各自独立无 critical 门、无回炉、无集合预算 |
| 3 | **davila7/claude-code-templates**（**28.2K★**，star=整目录；`.../skills/scientific/scientific-visualization`） | **本轮最完整的 prose 同类**：matplotlib/seaborn/plotly；**栏宽**(Nature 89/183mm·Science 55/175mm·Cell 85/178mm)、DPI(线稿 600-1200/位图 300-600)、矢量(never JPEG)、Okabe-Ito+viridis/plasma/cividis、**禁 red-green/jet/rainbow**、**灰度可读测试**、误差棒(SD/SEM/CI 注明 caption)、**"never truncate axes：bar 从 0 除非有科学理由"**、去 3D/chartjunk；脚本 `figure_export.py`/`style_presets.py`；**13 点交付前 checklist** | **印证 figure_export(JOURNAL_SPECS)/color_palettes 同口径**；"灰度测试""画原始点"两条可补进 self-check；**13-pt checklist 范式**对照我交付前 self-check | **关键诚实**：它把截轴/双轴/rainbow/误差棒**全覆盖了**，但**是 prose 规则 + checklist 人工核**，**非机读门**——不 emit findings、不阻 DAG、不绑证据档、无回炉。我的增量正在此（§0.C④） |
| 4 | **Haojae/scipilot-figure-skill**（**530★**，**最近-mission 直接竞品，深读**） | **哲学双胞胎**："thinks first, plots second"；8 步：`profile_data.py`(列型/样本量/分布/离群/相关)→`chart_selection.md`(按数据形+**论点意图**选型)→`viz_pitfalls.md`(**18 条拦截**：P2 双轴/P4 截轴/P3 3D/P14 jet/P9 误差类型未交代/P1 均值柱掩盖分布 n<10 拒画…)→渲染。**5 条硬规**(最终尺寸不缩放/矢量不 JPEG/Okabe-Ito/字号达标/**"Errors must be explained"caption 标 SD/SEM/CI+n+检验**)；**render-then-audit(v2.1)**：`visual_qa.audit_layout()` 测缺字/裁切/标签重叠 + AI 图像复审(图例遮挡/panel a/b/c 对齐/灰度可辨)+`layout_tools.add_panel_labels`；`check_figure.py --min-dpi 300 --strict`；`journal_specs.md`(figsize=(3.5,2.625) Nature 单栏)+CJK 字体自配 | **独立印证 Light 全套**：①问"这图要论证什么"=图服务论点 ②viz_pitfalls 18 条≈figure_integrity_lint catalog ③visual_qa.audit_layout=render-then-look ④journal_specs=figure_export ⑤"先说明问题再给替代不默默照做"=我 ASK 决策点。**它是"我没瞎想"的最强外证** | **它最像我，但差三处**(viz_pitfalls.md 明文)：**(e) 把不显著当主图—零覆盖**；**(f) 绑统计证据档—零覆盖**(只 P15 显著性符号滥用沾边)；**18 条全是 prose+refusal**(原话"先说明问题…不要默默照做")**非机读 critical verdict**，自动化仅 visual_qa 查渲染(P16-18)不查统计有效性。我的 misrepresent_evidence + 机读门 + 9→7 是它没有的 |
| 5 | **antvis/chart-visualization-skills**（**372★**，AntV 官方/阿里） | 生成**可跑 G2 v5 JS 代码**(非图片)，Spec Mode(stackY/dodgeX/binX/fold + 极坐标/theta)，**26+/30+ 型**(interval/sankey/chord/treemap/wordCloud/gauge…)；防 v4→v5 迁移坑(弃用链式 API/非法色板名)；**Harness Engineering 评测**：174 例对 Context7 基线，qwen3-coder-480b 98.2%(+17.7%)；`eval/harness/playground` 全套 | **eval harness 量化"图代码对不对"**思路(对照我 selftest)；Spec Mode 声明式=可复现代码理念 | Web 图(G2/JS)非论文出版图；**零诚实/证据/出版规格**(无栏宽/误差棒/色盲门)；评的是"代码跑不跑对"非"图诚不诚实" |
| 6 | **ntcoding/claude-skillz**（**318★**，`data-visualization` skill；概览读） | 多 skill 仓里的 data-viz skill：覆盖视觉执行/技术实现/**感知基础**/图型选择/布局算法/库推荐；`@` 引用组合范式 | "感知基础(Cleveland-McGill)驱动选型"印证 recommend_chart 的感知精度排序 | 概览级读(未深扒内部规则文件)；通用 dashboard/图非论文诚实门；无证据绑定/回炉 |
| 7 | **tvhahn/matplotlib-skill**（**19★**，eval 驱动） | "**50 轮自动评测—AI 精修自己的视觉品味**"建成；色盲友好/去脊/DejaVu Sans/cubehelix+ColorBrewer/whitegrid；**9 个图型 P1(横柱)-P9(PR/ROC)**；`scripts/evaluate_skill.py --check-renders`+`chart-test-container.sh`(Docker 可复现出图测)；`data/datasets.yaml`(10 真项目+29 公开数据集) | **Docker 可复现出图测 + eval 硬化图型**思路(对照 selftest 真出图)；"AI 精修视觉品味"=render-then-look 的另一形态 | "50 轮精修品味"是**美学优化**非诚实门；无证据绑定、无 critical、无集合预算；P1-P9 是模板非机检 |
| 8 | **dazhiyang/scientific-plotting-skill**（**6★**，**R3 双路径直接参照**） | **唯一同时 R/ggplot2 + Python/plotnine 的出版图 skill**：栏宽 85mm 单/180mm 双、Wong 离散(≤8)、viridis **等计数分位**连续、Times 衬线**全局单字号**、画布无标题、矢量 PDF/EPS、scattermore 稠密散点；纯 SKILL.md(无脚本) | **R3 的 ggplot2 出版配方直接拿**(85/180mm + Wong + viridis 分位 + Times 单字号)；"plotnine=python 里的 ggplot 语法"备选 | **python/R 选择是用户手填 prompt 不自动**——我 R3 增量=**探测 Rscript+ggplot2 自动选、不可用诚实降级 matplotlib**(无同类做自动探测降级)；它**零诚实校验/无 validation pipeline**(纯 prose) |
| 9 | **danielrosehill/Claude-Data-Visualisation-And-Publishing-Plugin**（**1★**，工具选择范式） | `tool-inventory`+`choose-tool`+`setup-environment`+`data-storytelling` 四 skill + `/dataviz-pick`/`/dataviz-setup`/`/dataviz-story` 命令；**choose-tool 决策协议**：呈现目的+数据形+运行时+受众 → 从 16 库(Matplotlib/Bokeh/ECharts/D3/visx/Vizzu/VChart/Plotly Dash…)选工具，反"模型凭记忆乱选库" | **"维护一份工具清单 + 决策协议选型 ≠ 凭记忆"**=我 recommend_chart 不臆造、figure_export 不内嵌期刊库的同理；区分叙事 vs 探索式 dashboard | 它选的是**库/工具**不查图诚实/不绑证据/无出版规格门；纯选型助手 |
| 10 | **Pirat83/claude-code-skills**（**0★**，render-then-look 极简实现） | `matplotlib-render-review` skill：Claude 写独立 py 脚本 → `render_review.py` harness 跑出 PNG → **多模态 Read 工具读回图** → self-review checklist(**布局/数据正确性/颜色/坐标轴**)→ 检出问题最多再迭 2 轮 | **"渲染→读回→checklist→有限迭代"= render-then-look 的最小骨架**，印证 figure_visual_qa 协议(渲染回看是同类共识非独创) | checklist 是 prose 人判非机读门；无出版规格/证据绑定/集合预算；0★ 但机制干净 |

> **结论（诚实，推翻审计"稀疏"判）**：绘图/出图 skill 这一类**真存在且高 star**（deer-flow 73.6K、K-Dense 29.1K、davila7
> 28.2K、scipilot 530、antvis 372、ntcoding 318）——审计 §9 说"同类 ~1、field 稀疏 top 130★"是**漏检头部**，与
> lit-search/paper-writing 同型系统病，本轮 R1 已纠。**但更要紧的诚实**：头部同类（尤其 scipilot 18-pitfall + davila7
> 13-pt checklist）**已覆盖 Light 的整个"视觉诚实 catalog"**（截轴/双轴/rainbow/3D/误差棒/色盲/栏宽）——所以 Light
> **不是"唯一想到截轴会骗人的"**；它们差在**全是 prose 规则 + refusal 启发 + 人工 checklist**，**无一**把诚实做成
> **emit findings 的机读 critical 门 + 绑 result-analysis 证据档(misrepresent_evidence) + 9→7 回炉 + 集合预算**。
> 这条"机读门 + 证据绑定 + DAG 回炉"链才是 Light figure 经得起查的真增量（§0.C④⑥ + 超越点）。

---

## 0.B 机制对标（样式库 / 生成 agent / 论文 / 书 / 引擎 / 规格 —— 不占 skill 名额，仍是有价值的机制/学术锚源）

> 这些是**库/引擎/论文/书/出版规格**，非可被 agent 调用的"绘图 skill"，但提供 figure 各门的**判据硬锚**（铁律 2 上网核）。

| 机制锚 | 是什么 / 机制 | 取什么（落进哪个门/脚本） | 与 §0.A 的区别 |
|---|---|---|---|
| **SciencePlots**(garrettj403) | matplotlib 出版样式包；**v2.2.1@2026-02-25、v2.2.0@2025-11-20 活跃维护**(GitHub releases 实测) | 出版级样式锚（figure 港运 nature/science/publication mplstyle 的同类参照） | 是**样式库**不是技能；不查诚实、不绑 claim |
| **cnsplots**(faridrashidi) | Cell/Nature/Science 出版图工具，预置 CNS 风格 + 内置统计检验/显著性标注 + 像素级尺寸 | 显著性标注 + 精确栏宽印证（figure_export 同口径） | **样式+标注库**；不判措辞/图强于证据 |
| **PlotGen**(arXiv 2502.00988, WWW'25) | 多 agent LLM 绘图：Query-Planning + Code-Gen + 三反馈 agent(Numeric/Lexical/**Visual** 多模态看图自反思)，+4-6% MatPlotBench | **render-then-look 学术锚**（Visual Feedback Agent=喂渲染图回多模态精修） | **论文/agent 系统**非可调 skill；不绑证据档、不产 critical |
| **ReLook**(arXiv 2510.11498) | 多模态 critic 渲染回看闭环：generate→截图喂 critic 打分→diagnose→refine | `_shared/visual_qa` render-then-look 的学术锚（批 0 已锚） | **论文**非 skill；通用视觉非论文诚实 |
| **matplotlib 3.10.9 / seaborn 0.13.2** | 程序化绘图引擎（viridis 自 2015 默认 cmap；seaborn 统计图） | **程序化生成底座**（铁律 6 例外：科学绘图标准件可用不重造） | **引擎**非门/技能 |
| **Okabe-Ito**(Wong 2011 *Nat Methods*) + **viridis/cividis** | 色盲安全色板：Okabe-Ito 8 色对三类色盲可辨（离散首选）；viridis 感知均匀（连续首选），灰度可印 | **色盲安全硬锚**（color_palettes 港运对象） | **色板规范**非技能 |
| **Cairo《How Charts Lie》(2019)** | y 轴截断="最普遍的图表谎言"；零基线规则：编码为高度/长度(柱)须零基线，位置/角度(折线)可非零 | **截 y 轴 critical 判据硬学术锚**（figure_integrity_lint 只对柱类强判） | **通俗书**非技能 |
| **《Truncating Y-Axis: Threat or Menace?》**(Correll+ 2019, arXiv 1907.02035) | 截断**并非永远是错**（放大真实小差异有时合理），但读者会高估被截差异 | **诚实边界硬证据**：lint 只标"可疑"，真误导终判需 caption+人 → 可授权 FAIL→PASS | **学术研究**非技能 |
| **Cumming《Error bars》**(*JCB* 2007) | SD≠SE≠CI；重叠推断(SEM 棒重叠→p>.05；95%CI 重叠半臂→p≈.05)；须注明类型与 n | **误差棒 warn 门 + caption 标类型/n 硬锚**（ERRBAR_NO_TYPE） | **规范论文**非技能 |
| **Tufte data-ink/chartjunk**(1983) | 最大化 data-ink、擦冗余；chartjunk=不传新信息的墨（3D 饼/伪装饰） | 反冗余 panel + PIE_3D 理念锚（2013/15 实证 chartjunk 非总有害→不硬判美学只判诚实/冗余） | **设计理念**非技能 |
| **Frontiers AI-鼠图撤稿**(2024-02) | Midjourney 生成"巨鼠+乱码标签"过审→撤稿；准则：AI 须披露**且图必须准确** | **"绝不 AI 生图"永久底线硬案例锚**（NEVER 红线 + 程序化生成铁律） | **事故案例**非技能 |
| **venue 显示项上限**(NeurIPS 2025=9 正文页含图表 / CVPR=8 页) | 顶会版面硬约束，超页不送审 | **集合级 display-item 预算门硬锚**（audit_figure_set --cap） | **会议准则**非技能 |
| **Nature figure guidelines 2025-26** | 单栏≈89mm/双栏≈183mm、最小字号、矢量/位图 dpi、CVD 友好 | **栏宽/字号/格式规格锚**（figure_export JOURNAL_SPECS） | **出版商规格**非技能 |

---

## 0.C 读完 10 个真同类后的横向机制提炼（直接驱动 Round 2 figure 加厚 + R3 设计）

**① 图型选择**：**人人都做**——scipilot `profile_data.py`+`chart_selection.md`(数据剖面+论点意图)、antvis Spec Mode(26+ 型决策)、deer-flow taxonomy 树、ntcoding 感知基础、tvhahn P1-P9 模板。**共识=数据形→图型启发式**。Light `recommend_chart` 同款（Cleveland-McGill 感知精度），诚实标"启发式、最终人定"——不落后。

**② 出版级规格**：**强共识**——栏宽 mm（davila7 Nature89/183·Science55/175·Cell85/178；scipilot figsize=(3.5,2.625)；dazhiyang 85/180）+ 最小字号 + 矢量(never JPEG) + DPI（线稿 600-1200/位图 300-600）。Light `figure_export` JOURNAL_SPECS **同口径**，**印证非独创**——把它当"达标项"而非"亮点"。

**③ 色盲安全**：**强共识**——Okabe-Ito 离散（scipilot 默认/davila7）、viridis 连续、禁 jet/rainbow、**灰度可读测试**（davila7 明文）、Wong（dazhiyang）。Light `color_palettes` 同款；**davila7 的"灰度测试 + 画原始点"两条可补进 self-check**（本轮加厚点）。

**④ 视觉诚实（最关键校正）**：**头部同类已覆盖整个 catalog**——scipilot 18-pitfall（P2 双轴/P4 截轴/P3 3D/P14 jet/P9 误差类型/P1 均值柱 n<10 拒画）、davila7（"never truncate axes，bar 从 0"）。**但全是 prose 规则 + refusal 启发 + 人工 checklist**（scipilot 原话"先说明问题再给替代方案，不要默默照做"；自动化仅查渲染版面 P16-18 不查统计）。**没有一个**把同一 catalog 做成 **emit `light.findings.v1` 的机读 critical 门 + run_checkpoint 聚合 exit 1**。→ **Light 的增量不是"想到截轴"而是"确定性机读门"**（figure_integrity_lint + visual_honesty_gate）。诚实修正超越点措辞：不再说"没人查截轴"（假），改说"没人把它做成机读门 + 绑证据 + 回炉"。

**⑤ render-then-look**：**已是同类共识非 Light 独创**——scipilot `visual_qa.audit_layout()`、Pirat83 render→Read→checklist→2 轮、tvhahn 50 轮 eval、PlotGen/ReLook（§0.B）。Light `figure_visual_qa` 消费 `_shared/visual_qa` 同款；**增量=接进科研 DAG**（产 `light.visual_qa.v1` → 汇 visual_honesty_gate findings → run_checkpoint stage 9 聚合），非"渲染回看本身"。

**⑥ 图↔证据绑定 + 把不显著当主图（真独有空间）**：**10 个同类无一做**——scipilot viz_pitfalls.md 明文 **(e) 把不显著当主图=零覆盖、(f) 绑统计证据档=零覆盖**（只 P15 显著性符号滥用沾边）。这是 Light `misrepresent_evidence`（消费 `evidence_strength.json`，must 图绑 grade=none claim→critical）+ **9→7 回炉**的**真差异化**——因为同类都是**单机绘图工具**，不在"result-analysis 定证据档→figure 卡措辞"的 DAG 里。

**⑦ python vs R 双路径（R3 设计依据）**：**dazhiyang 同时 ggplot2/plotnine 但用户手填 prompt 选、不自动**；scipilot/davila7/tvhahn 纯 python。**无一做"探测 R 可用→自动选 ggplot2→不可用诚实降级 matplotlib"**。→ Light R3 增量明确：**Rscript 全路径探测 + `requireNamespace("ggplot2")` → 可用走 ggplot2(`.R`+`ggsave`)、不可用降级 matplotlib 并诚实标注**；ggplot 出版配方直接学 dazhiyang（85/180mm + Wong + viridis 分位 + Times 单字号 + 矢量 PDF）。

---

## 机制对标逐项一手核要点（§0.B 锚的深读，gate 判据来源）

### 1. SciencePlots — 维护状态当场核（铁律 2）
GitHub `garrettj403/SciencePlots`：**v2.2.1@2026-02-25、v2.2.0@2025-11-20** —— 活跃维护非停更。`plt.style.use(['science','ieee'])` 套刊风格。
→ figure 港运 `nature/science/publication.mplstyle` 是同类自有样式（精确栏宽+最小字号锁定，不依赖 LaTeX）；**SciencePlots 是样式库不是诚实门**，与 figure 的 `visual_honesty_gate` 互补（样式负责"像该刊"，门负责"不撒谎"）。

### 2. PlotGen / ReLook — render-then-look 的学术锚
- **PlotGen**(WWW'25)：三反馈 agent(Numeric/Lexical/**Visual**)多模态看渲染图自反思，MatPlotBench +4-6%。Visual Feedback Agent=render-then-look。
- **ReLook**(2510.11498)：generate→截图喂 critic→diagnose→refine。→ 二者 + §0.A 的 scipilot/Pirat83/tvhahn 共同印证：**render-then-look 是绘图领域共识**；figure 经 `figure_visual_qa` 消费 `_shared/visual_qa`（抽 matplotlib AABB 喂几何引擎 + 打包回看），**不重造**。增量=接进 DAG（§0.C⑤）。

### 3. 色盲安全 — Okabe-Ito / viridis（一手核）
Okabe-Ito(Wong 2011 *Nat Methods*)：8 色对三类色盲可辨，离散首选(≤8 类)；连续用 **viridis/cividis**（感知均匀、色盲安全、灰度可印，自 2015 matplotlib 默认）。反例 **jet/rainbow**：非感知均匀（绿黄处对比骤升、深蓝压平），色盲糊成一片→伪边界/夸大梯度。~8% 男/0.5% 女色觉缺陷，Nature/Science/PNAS 要求或强建议 CVD-safe。
→ color_palettes 港运 Okabe-Ito/viridis；figure_integrity_lint RAINBOW_CMAP 抓 jet/rainbow（**warn**：分不清有序 vs 类别，定 critical 会假阳硬阻）。**davila7 的灰度测试**可补进 self-check。

### 4. 截 y 轴 / 双 y 轴 — Cairo + 截轴实证（critical 判据 + 诚实边界）
- **Cairo(2019)**：截断是"最普遍的图表谎言"；零基线规则——编码为高度/长度(柱)须零基线，位置/角度(折线)可非零。→ AXIS_TRUNCATE 只对"ylim 起点≠0 且无断轴标注"报，对柱类更强判。
- **Correll+(2019, 1907.02035)**：截断**并非永远是错**（放大真实小差异有时合理），但读者会高估被截差异。→ 静态 lint 只标"形态可疑"，真误导终判需 caption+人；有断轴标注/正当理由可授权 FAIL→PASS（spec §6）。
- **双 y 轴(twinx)**：两轴各自缩放制造伪相关 → TWIN_AXIS 提示拆 panel。
- **同类印证**：scipilot P2/P4、davila7"never truncate"——**catalog 共识**；Light 增量=机读门（§0.C④）。

### 5. 误差棒规范 — Cumming（warn 门硬锚）
Cumming(*JCB* 2007)：SD（个体离散）≠SE（均值精度，随 n 缩）≠95%CI；选错改变含义。重叠推断：等 n 下 SEM 棒重叠→p>.05；95%CI 重叠半臂→p≈.05。**铁律：图/caption 必标类型(SD/SEM/CI)+n**。
→ figure_integrity_lint：BAR_NO_ERR（柱图无误差棒=掩盖不确定性）、ERRBAR_NO_TYPE（有棒无类型字样）——均 **warn**。**注意 scipilot P9 只查"未交代类型"不查"缺失"**——Light 的 BAR_NO_ERR 查缺失是小边际增量。选型与"重叠是否显著"终判仍需人。

### 6. 程序化生成 vs AI 生图 — Frontiers 撤稿（永久底线硬案例）
2024-02 Frontiers 一文含 Midjourney 生成"巨鼠生殖器+乱码标签"，疯传后撤稿。准则：AI 须披露**且图必须准确**。
→ **"论文数据图必须程序化生成、绝不 AI 生图"是 NEVER 红线**：实验数据图绝禁生成式模型造/改；matplotlib/seaborn/**R** 代码生成=可复现可核不造数据。**注意 §0.A 第 1 行 deer-flow/antvis 出"图片 URL"**——那是 web 图场景，论文数据图走 Light 的程序化红线（出代码不出图片）。

### 7. venue 显示项上限 — NeurIPS/CVPR（集合预算门硬锚）
**NeurIPS 2025**：正文 9 内容页含所有图表；camera-ready +1。**CVPR**：8 页不含参考。超页不送审。
→ audit_figure_set `--cap N`（取目标刊作者指南权威值）机检 F#+T# 计数对照 cap，超则砍序裁定（可删→可做降附录→必做不动）；**不内嵌某刊上限臆测**（易腐，须用户给权威值）。**danielrosehill 的"维护清单不凭记忆"同理**。

---

## 横切可借机制（已落进 v2；★=Round 2 校正/强化）

1. **图↔证据档 + result card provenance + paper claim context 机读绑定**（**§0.A 实证：10 同类无一做**，scipilot 明文 (f) 零覆盖）：每张主图须指向 result-analysis `evidence_strength.json` 与 result card；must 图绑 grade=none claim="把不显著当主图"→critical→**9→7 回炉**；交付契约还要求 result card/evidence_strength locator + SHA-256，并要求 paper-writing claim plan locator/SHA-256、guardrail status/claim_impact 与 caption 是否反映限制。← `visual_honesty_gate` 的 `misrepresent_evidence` + `figure_contract.py`。**★这是真独有，非 catalog 共识**。
2. **视觉诚实静态判据**（Cairo 零基线 + 双轴伪相关）：截/双轴→critical 阻断。← figure_integrity_lint。**★校正：catalog 同类已覆盖（scipilot P2/P4/davila7），增量=机读门非 catalog**。
3. **render-then-look**（PlotGen/ReLook + scipilot/Pirat83/tvhahn）：渲染→多模态按 rubric 挑缺陷。← figure_visual_qa 消费 `_shared/visual_qa`，**不重造**。**★校正：同类共识，增量=接进 DAG**。
4. **集合级 display-item 预算 + 反冗余**（NeurIPS/CVPR + Tufte）：计数对照 cap + 砍序。← audit_figure_set。**10 同类无一做集合预算**（都是单图工具）。
5. **出版级规格 + 色盲安全**（davila7/scipilot/dazhiyang + Okabe-Ito/viridis + Cumming）：栏宽/字号/dpi + CVD 色板 + 误差棒标类型/n。← figure_export + color_palettes + figure_integrity_lint。**★校正：强共识达标项非亮点；补灰度测试/画原始点进 self-check**。
6. **程序化生成绝不 AI 生图**（Frontiers）：matplotlib/seaborn/**R** 代码生成。← SKILL NEVER 红线。
7. **★R3 python+R 双路径**（dazhiyang 配方 + §0.C⑦）：探测 R→自动选 ggplot2/不可用诚实降级 matplotlib；ggplot 出版配方学 dazhiyang（85/180mm+Wong+viridis 分位+Times 单字号+矢量 PDF）。**无同类做自动探测降级**。

---

## 超越点（Light figure 相对全市场的差异，Round 2 诚实重述）

> **批 1 旧措辞过满**（"没有一个查截轴/双轴诚实"）——§0.A 实证 scipilot 18-pitfall + davila7 checklist **都查**。本轮按一手核重述：

- **不是 catalog 独创**：截轴/双轴/rainbow/3D/误差棒/色盲/栏宽这套"诚实+出版 catalog"，头部同类（scipilot/davila7）**已覆盖**；render-then-look、图型选择、journal specs 也都是**共识**。承认这点才诚实（铁律 2）。
- **真差异化（四条，§0.A/§0.C 实证）**：① 把诚实 catalog 做成 **emit findings 的确定性机读 critical 门**（figure_integrity_lint + visual_honesty_gate → run_checkpoint exit 1），同类全是 **prose+refusal+人工 checklist**；② **绑 result-analysis 证据档、result-card provenance 与 paper-writing claim context**，把"把不显著当主图"和"guardrail WARN 限制没进 caption"做成可阻断契约，并在交付契约里要求 result card/evidence_strength/claim plan locator + SHA-256（`misrepresent_evidence` + `figure_contract.py`，**10 同类零覆盖**）；③ 产 **根因回炉 9→7**（带该图对应证据强度），同类是单机工具不在 DAG；④ **集合级 display-item 预算 + 反冗余机检门**（venue cap），同类无一做。
- **一句话**：**同类比谁画得对/画得好/像该刊**；**Light 比"这图诚不诚实、撑不撑得起它绑的 claim"，且做成机器能判、能阻断、能回炉的门**。这是科研 DAG 节点 vs 单机绘图助手的差异。

---

## 诚实边界（名实对齐，写进 SKILL，铁律 2）

- **静态 lint 只抓"形态可疑"非"证明误导"**：AXIS_TRUNCATE 抓"ylim≠0 无断轴标注"，但截断**可能完全合理**（Correll 实证）；TWIN_AXIS 抓 twinx 存在，双轴有时正当。→ critical 默认阻断，**用户可授权 FAIL→PASS 记 notes**；真误导终判需 caption+人/审稿人。
- **图↔claim 绑定是启发式**：优先 `claim_id` 精确匹配，否则 claim 文本语义相似（≥0.6）；无匹配→证据档未知→不 flag（保守少误报 critical）。精确逐图需规划卡写 `claim_id`。
- **misrepresent_evidence / figure_contract 核"图对应证据强度、result-card provenance 与 paper claim context"非"证据真伪"**：只核"主图绑的 claim 达没达显著"、"图交付能否追到 result-analysis result card"和"guardrail 限制是否进入 caption"，不核结论对不对（那要复现/同行）。
- **rainbow 定 warn 非 critical**：静态 lint 分不清"有序数据（该禁）vs 类别数据（+caption 可辩护）"，降 warn（诚实降级），不假阳硬阻。
- **误差棒/色盲检测有边界**：抓"没写类型/用了 jet"，但该用 SD/SE/CI 哪种、重叠是否显著、类别 rainbow 是否真误导仍需人。
- **render-then-look 须真喂回多模态模型才算验证**：几何层只抓可计算的版面硬错；视觉品味/层次/可读性细节须人/多模态看，未做如实标 `pixel_review_done=False`。
- **程序化生成绝不 AI 生图是永久底线**，非"建议"：figure 不调用任何生成式图像模型画论文数据图。
- **R 路径有环境前提**：ggplot2 须本机装 R + 包；探测不到时**诚实降级 matplotlib 并标注**，不假装出了 ggplot 图（R3 名实对齐）。
- **venue cap 须用户给权威值**：不内嵌某刊 display-item 上限臆测（易腐）；无 --cap 时只报计数 + 顶会常 6-8 件软参考。
- **竞品 star 是 snapshot**：§0.A star=2026-06-23 GitHub repo 页，外部可变会涨；大技能包 star 是整包非绘图 skill 单独的，已注明。

## 诚实待补深读（未及一手核，留痕）
- **ntcoding/claude-skillz** data-viz skill 只读概览（感知基础/布局算法/库推荐），**未深扒内部规则文件**（是否含截轴判据等），留待按需补。
- **K-Dense / deer-flow** 绘图 skill 的逐脚本未全读（big pack，读了定位 + 机制归属），star 是整包。
- MatPlotBench / 科学绘图 benchmark 具体指标口径未逐一核；不编造。
- ~~R/ggplot2 出版级规格的港运留 citation 之后按需补~~ → **本轮 R3 正在做**（dazhiyang 配方 + 探测降级，见 §0.C⑦ + 横切机制 7）。
