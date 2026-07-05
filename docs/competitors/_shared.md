# Competitors 笔记 · 共享契约层(_shared)

> 铁律 8 交付物:每个模块开做第一道工序——联网真搜最强同类、读机制、写笔记。
> 对"地基契约层"这类基础设施,"同类"= 各契约族背后的业界最强机制/标准。
> 调研日期 2026-06-16。下面每条:强在哪 / v2 借了什么 / v2 的超越点或诚实落后。

---

## 1. findings/gate 机读交接 —— 对标 SARIF + 多 agent 交接

**最强同类**
- **SARIF 2.1.0(OASIS 标准)** <https://docs.oasis-open.org/sarif/sarif/v2.1.0/sarif-v2.1.0.html>:业界静态分析结果交换的事实标准。结构:`runs[]`(tool.driver + results)、`results[]`(ruleId/level/message/locations/fixes)、`rules[]`、`artifacts[]`。GitHub code scanning、Sonar、checkov 等都吃它。
- **多 agent 框架交接**:LangGraph(有向图 + 条件边,显式控制权转移)、CrewAI(角色 crew)、AutoGen、OpenAI Swarm。2026 业界共识:agent 间交接 = "双方都能消费的结构化 JSON 对象 + 携带上下文",而非自然语言。

**v2 借了什么**
- `light.findings.v1` 字段语义有意识对齐 SARIF:`loc`≈location、`rule`≈ruleId、`severity`≈level、`fix`≈fix、`evidence`≈SciFact rationale。
- 新增 `FindingsReport.to_sarif()`:无损导出为 SARIF 2.1.0,原 Light 字段进 `properties` 不丢,可与 GitHub code scanning 等外部工具互通。

**v2 的取舍/超越**
- **不直接用 SARIF**:它为安全工具互操作设计、字段繁重(token 不经济、作者难写)。本契约是**技能内交接**,刻意精简(producer/target/gates/verdict + finding 五字段),保留 SARIF 没有的 `gate` 分组(按质量门聚类)与 `verdict` 聚合裁定(总控守门直接读),并提供 to_sarif 兜底互通。**精简版 + 标准兜底**优于"硬塞 SARIF"。
- 诚实纪律:gate 抛异常转 critical fail 携 traceback,不静默吞——SARIF 规范不规定此行为,是本契约对"agent 写代码不可靠"的防御。

---

## 2. 证据强度→措辞 —— 对标 GRADE + Hyland + SciFact

**最强同类**
- **GRADE(Cochrane 证据确定性分级)** <https://training.cochrane.org/handbook/current/chapter-14>:四级 high/moderate/low/very-low,经 5 域评估(风险偏倚 / 不一致 / 间接性 / 不精确 / 发表偏倚);RCT 起评 high,观察性起评 low。
- **Hyland 1998《Hedging in Scientific Research Articles》**:学术写作 hedging 阶梯——强证据用 factive 动词(demonstrate/establish),弱证据须 hedge(suggest/may)。
- **SciFact(EMNLP 2020)** <https://aclanthology.org/2020.emnlp-main.609/>:claim 验证 = SUPPORTS / REFUTES / NEI(Not Enough Info)+ rationale 句。

**v2 借了什么**
- 四档 strong/moderate/weak/none 对外**对齐 GRADE 词表**(`GRADE_LEVEL`:high/moderate/low/insufficient),措辞档以 Hyland 阶梯为据(已在 docstring 标注出处)。
- Finding 的 `evidence` 字段 = SciFact 式 rationale(支撑该发现的原文/证据),为下游 claim-binding 留接口。

**v2 的超越点(对 v1 的真增量)**
- **中英双语动词档**:v1 evidence_contract 仅英文。v2 加中文断言词(证明/证实/显著/优于…)与中文 hedge(可能/或许/倾向于…),并解决中文无词边界 + "无显著差异"否定式假阳性(否定守卫:断言词前两字含 无/不/未/没 则不算违规)。这是中文论文场景的院士级 hedging 细节。

**诚实落后项**
- 分档目前**只吃统计强度**(q/效应量/CI/n,≈GRADE 的"不精确"+效应量),**未实现 GRADE 另四域**(偏倚/不一致/间接/发表偏倚)的系统降级。留给 result-analysis 在拿到多数据集/多种子结果时做域降级——本契约不假装做了 full GRADE。

---

## 3. 语义相似度 —— 对标 sentence-transformers / RapidFuzz

**最强同类**
- **sentence-transformers**:本地 embedding 模型,真语义("running shoes"↔"athletic footwear" 高分)。最佳但需下载模型/依赖。
- **RapidFuzz**:极快的字符串模糊匹配(比同类快 ~40%),但**纯字面、不懂语义**(上例只给 0.267)。
- 实测结论(多篇 2025 对比):无共词同义必须靠 embedding,字面匹配做不了。

**v2 借了什么 / 设计正确性确认**
- v1 的**三档降级**(embedding 注入 → LLM-judge 注入 → 纯 stdlib 离线兜底)被上述对比直接背书:离线档做字面/词形,语义靠注入 embedding。
- 离线档混合:字符 3-gram 余弦 + 词干化 token Jaccard + bigram 词序惩罚——比裸 Jaccard 强,正确把倒装("Attention Is All You Need"↔"All You Need Is Attention")判为高相似但 <1.0(裸 Jaccard 误判 1.0)。

**v2 的取舍**
- 离线档保持**纯 stdlib**(硬约束"标准库优先",零依赖),不引 RapidFuzz/embedding 为默认。
- **诚实边界**:离线档显式标注"派生词/纯同义词不可靠,需 embedding 档",`last_mode()` 留痕实际档位,不假装离线能做语义。
- 修了 v1 一处隐患:两串全为停用词时 `sta|stb` 为空会 ZeroDivisionError,加空集守卫。

---

## 4. 视觉回看 —— 对标 ReLook + WCAG + 官方 fix-and-verify

**最强同类**
- **ReLook(arXiv 2510.11498, 2025)** <https://arxiv.org/abs/2510.11498>:多模态 LLM critic 看渲染截图打分 + 给可执行的视觉 grounded 反馈,generate→diagnose→refine 闭环(前端 web 编码)。
- **WCAG 2.x 对比度** <https://www.w3.org/TR/WCAG20-TECHS/G18.html>:相对亮度 L=0.2126R+0.7152G+0.0722B(sRGB 线性化),对比度 (L1+.05)/(L2+.05),正文 AA 4.5:1 / AAA 7:1。**可确定性计算,无需模型。**
- Anthropic 官方 pptx skill 的 render→看→修→重渲染 fix-and-verify 循环。

**v2 借了什么**
- `render_then_review` 协议 = ReLook 的 generate-diagnose-refine,渲染喂回多模态模型按 rubric 打分;无渲染器时诚实标 `pixel_review_done=False`,不静默假成功。

**v2 的超越点(对 v1 的真增量)**
- **确定性 WCAG 对比度门**:v1 visual_qa 把对比度全甩给 VLM。v2 加 `relative_luminance / contrast_ratio / check_contrast / detect_contrast_issues`——最高频的可读性/色盲不安全 fail,**不渲染、不调模型就能确定性抓出来**,且分两档(<3:1 不可读=critical,3~4.5 未达 AA=important)。

**诚实落后项**
- 几何检测需消费方提供 AABB 坐标(figure/frontend 本就能读出);对**已是位图**的图(扫描图/外部 PNG),无 AABB 时只能走 VLM 回看,几何/对比度门不适用。

---

## 5. 跨 harness 形态 —— 对标 Agent Skills 开放标准

**关键发现**
- **Agent Skills 于 2025-12 成为开放标准(agentskills.io)**,已被 Codex、OpenCode(本项目两个目标 harness)+ GitHub Copilot / Cursor / Gemini CLI / Goose 等 ~40 客户端采纳。三级渐进披露(Discovery: name+desc → Activation: SKILL.md → Execution: bundled code),实测省 ~40% token、+15~20% 完成率。

**对 v2 的意义**
- 三 harness 适配风险**大降**:SKILL.md 形态本身已跨 harness 原生可消费。`_shared` 是纯 stdlib Python,被各技能脚本调用,天然 harness 无关。
- **v2 真增量(对 v1)**:健壮 `_shared` 定位器(向上走目录树找仓库根),治 v1 硬编码 `parents[N]` 的脆——三 harness + 全局/项目安装、任意嵌套深度都能可靠 import(已 e2e 实测 4 层嵌套通过)。
- 待 batch 1 写 SKILL 时落地:按三级渐进披露组织 SKILL.md(name+desc 精确触发信号词、正文 if-then、红线独立标 NON-NEGOTIABLE)。

---

## 调研覆盖度(诚实标注)
- 已深读机制/标准:SARIF 2.1.0、LangGraph/CrewAI/AutoGen/Swarm(交接范式)、GRADE、Hyland 1998、SciFact、ReLook、WCAG 2.x、Agent Skills 开放标准、RapidFuzz↔sentence-transformers 对比 —— 共 ~11 个真机制/标准。
- 未逐行读其完整源码(SARIF 规范/ReLook 训练代码体量大),读的是规范要点 + 机制设计 + 我方实现需要的接口面;契约实现以满足消费方需求为准,非复刻其全部。
- 这些是地基**基础设施**对标(标准/范式层),非某个用户可见技能的产品对标——技能级的 ~10 竞品深读放到各自 batch。
