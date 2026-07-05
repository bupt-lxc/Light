# competitors — light-idea-critique（科研主线 stage 4 · 审 idea ⇄ stage 3 提 idea）

> 铁律 1+2 对标笔记：动手前深读最强同类，**机制上网核实(star=[snapshot 2026-06-27, src=GitHub repo 页/`gh api`
> 一手核]，非凭记忆)**，落地可借机制 + 标清超越点与诚实边界。本技能是**科研主线 DAG 第 4 节点**(与 3 双向回环
> 3⇄4)：顶会审稿人标准严审，**撞车/无创新 fatal flaw 一票否决(critical)**，逼出真能发表的 idea。**接 `_shared`**
> —— 产 `light.findings.v1` 的是 **critical 否决型 findings**(producer=idea-critique)，被总控
> `run_checkpoint --stage 4` 聚合 **Critical fail exit 1**，`reroute` 建议回边 **4→3**(带"具体缺口 + 最像的前作")。
> **与 gen 侧的诚实分工**：idea-generation 产撞车 **warn 自查信号**(producer=idea-generation，非 critical)；
> **本技能是 critical 门**——消费 gen 的 `most_similar`+facet 槽位做 target/background 分解、下 novel/撞车的一票否决
> 判决。依据：Si et al(2409.04109)实测"LLM 不能可靠评 idea 质量"，故 judge 集中在本技能，用**可计算闸门**
> (否决引擎 + 反谄媚 + 密度先验)对抗单模型过度背书，而非裸自评。
>
> port 自 v1 `light-idea-critique`(score_aggregate/novelty_audit/sycophancy_guard/novelty_density/calibration/
> critique_self_audit，byte-copy 再 Edit)。**v2 净新增 = `fatal_flaw_gate.py` 撞车/否决 critical findings producer**
> (v1 否决引擎全部零接 `_shared`/`light.findings.v1`，grep 实证)。
>
> 写作：批 1 第二技能·crit 侧(2026-06-18)。**Round 2 R1 重做(2026-06-27)**——治"高 star 同类 skill 漏检"系统病。
> 作者 Light0305 + Claude。上游成对件见 `competitors/idea-generation.md`。

---

## ⚠ Round 2 R1 系统病诚实校正（先认错，再对标）

批 1 旧版 §0「对标矩阵」13 行里**真·同类 Claude/agent skill 只有 1 个**(第 13 行"academic-paper-reviewer /
peer-review 类 skill(GitHub)"，且写得含糊)，其余 12 行全是**论文/系统/基准**(GraphMind/OpenNovelty/PRISM/
Pitfalls/AI-Scientist/CycleReviewer/OpenReviewer/SEA/TreeReview/Si et al/OpenReview-bias)。这正中审计点名的系统病：
**把论文当同类、漏检高 star 同类 skill**(审计明确点名漏了 **paperjury 345★**)。Round 2 一手核 GitHub 后实情 =
**"审稿/评审/查新"是 Claude skill 生态最拥挤的赛道之一**，≥10 个真·同类各自完整，含多个**万 star 级**：

- **paperjury(u7079256，453★，审计点名漏检，今天已涨到 453)** / **imbad0202/academic-research-skills 34,827★**
  (`academic-paper-reviewer` v1.10.0) / **K-Dense scientific-agent-skills 29,444★**(`peer-review`+`scholar-evaluation`
  +`scientific-critical-thinking`+`consciousness-council` 四个评审/批判 skill) / **ARIS 12,693★**(`novelty-check`+
  `research-review`+`patent-novelty-check`) / **Galaxy-Dawn 4,426★**(`paper-self-review`) / **mattpocock/skills
  148,028★**(`grill-me`/`grill-with-docs`) / **obra/superpowers 239,843★**(`verification-before-completion`) ……

**结论：旧版"idea-critique 同类只有 ~1 个"的隐含判断 = 漏检，推翻**(同 figure scipilot / frontend taste-skill /
lit-search 实证的同一系统病)。**诚实重述超越点**(防做偏 figure scipilot 教训)：多视角 persona 互怼、Devil's Advocate
对抗挑刺、反谄媚、拒稿预演、校准严格度、binary novel 判——**全是同类强共识，Light 一个都不是"唯一想到"**；Light 的
真增量 = **机读 critical findings + 确定性阻断 + 跨技能反哺(13 真同类零覆盖) + 可计算否决闸门(同类多靠 persona prose)
+ 全程零 key/零 MCP**(K-Dense 需 OPENROUTER_API_KEY、ARIS 需 Codex MCP+OpenAI key)。**新落地(R1→脚本)：借
paperjury 的"两面庭审/可争辩路由"** → `critique_self_audit` 加**拒稿预演完整性 warn-only advisory**(详 §0.C ④)。

---

## 0.A 真·同类 审 idea/评审/查新 SKILL（13 个真同类 · R1 硬指标 · star=[snapshot 2026-06-27, src=`gh api` 一手核]）

> 判据：每条**已读其 SKILL.md/agent/脚本**(带可复验点：文件名/常量/行为)，非列名字。优先高 star。

| # | 同类 skill（star） | 它怎么做（已读 SKILL/agent/脚本，带可复验点） | 我借进哪个能力 | 我诚实差在哪 |
|---|---|---|---|---|
| 1 | **u7079256/paperjury**（**453★**，`SKILL.md` v1.2.1，MIT，author Yiran Wang；**审计点名漏检**） | **预投稿对抗式"法庭"审稿引擎**(REVIEW mode)：N 个 **holistic domain reviewer**(默认 3，范围 2-4，program-chair 式按子领域分派)→ **contestability routing(可争辩路由)** → **two-sided trial(两面庭审)** → **three-way verdict(三向裁决)** → clerk-converged 多轮 loop。v3 管线 `assign-reviewers→reading-check→coverage-auditor→merge→{trial(+escalate)‖polish}→recall-audit→drafter→{edit-audit‖meaning-audit}→clerk`。**durable LEDGER.json**(`scripts/ledger.js` 管，跨会话/跨轮存活)，一行一 issue 带 **`close_criterion`**(关闭判据)+ 状态机，severity `blocker>major>minor>nit`。**每轮 reviewer 互相隔离**(冻结正文、剥修订标记、不见 ledger/彼此/前轮 → 反 anchoring，"R2/R3 不锚 R1")。persona 核 "Unflinching Academic Gatekeeper"：**"do not pad with compliments, do not invent problems to look thorough, do not soften a real flaw"**。两遍穿透批判(fatal-flaw 诊断→forensic interrogation：where exactly/why/what evidence settles/fatal-or-fixable)。`AskUserQuestion` 仅 **pre-flight gate**("dead in-loop")。`scripts/ledger.js floor` 显著性门 + Bash 侧确定性 guard(compile-guard/compliance-check/anchor-diff) | **R1 落地**：借 **two-sided trial / contestability** → `critique_self_audit` 加**拒稿预演完整性 warn-only advisory**(NEVER#4 原本只在 prose、零机检)；其 **`close_criterion`** → 对齐我 `reroute` 4→3 带"具体缺口"；**reviewer 跨轮隔离/反 anchoring** → 印证我诚实落后项#2；`AskUserQuestion` pre-loop = 我 ASK 回炉/严线决策点 | 它是 **paper-level**(全文审稿+改稿+durable ledger)，我是 **idea-level**(单卡、定稿前更早)；它真 **workflow fan-out**(并行 agent)+ 跨会话 ledger，我单模型扮多视角(伪多样)+ 单卡无状态；但它是**自硬化 loop 无 score gate / 不产编排器可读 critical findings**——我的机读否决 findings + 确定性阻断是差异点 |
| 2 | **imbad0202/academic-research-skills**（**34,827★**，`academic-paper-reviewer/SKILL.md` v1.10.0，2026-06-01） | 模拟完整国际期刊审稿：动态配 **5 reviewer(EIC + 3 peer + Devil's Advocate)**，**4 个互不重叠视角**(methodology/domain/cross-disciplinary/core-argument-challenge)→ 结构化 Editorial Decision + Revision Roadmap。模式 **full/re-review(查修订是否回应)/quick/methodology-focus/Socratic-guided/calibration(先测自身 FNR/FPR)**。`agents/devils_advocate_reviewer_agent.md` 只挑刺不打分，4 类 CRITICAL：Foundation Collapse / Logic Chain Break(相关≠因果未控混杂) / Evidence Gaps(N<50 单实验室) / Stronger Counter-Narrative。Sprint Contract：看正文前先承诺 failure_conditions。`data_access_level: verified_only` | Devil's Advocate 4 类 CRITICAL → 我 fatal_flaw + 拒稿预演 top-3；Sprint Contract 先立标准 → 我 ASK 严线 + 收尾 self-check；calibration mode → 我 `calibration.py` 三分类；re-review → 我 reroute 后复审；**Revision Roadmap → 我 `templates/Revision_Roadmap.md`** | 5 persona 真多 agent(伪多样我单模型只缓解非消除)；paper-level 非 idea-level；无机读 findings/确定性否决闸门(高均值救不回靠人) |
| 3 | **K-Dense peer-review**（**29,444★**，`skills/peer-review/SKILL.md` v1.2，MIT，K-Dense Inc.） | checklist 评 methodology/statistics/design/reproducibility/ethics + **CONSORT/STROBE/PRISMA** 报告规范核对；路由"判证据质量→critical-thinking、量化分→scholar-evaluation、写 review→peer-review"；**`required_environment_variables: OPENROUTER_API_KEY`**(LLM 步骤) | 报告规范核对 → 我 rubric 否决项；三技能路由分工印证我 stage 分工 | 偏生医临床规范(CONSORT/STROBE)；**需 OpenRouter key**(违我零-key)；无确定性否决闸门/findings |
| 4 | **K-Dense scientific-critical-thinking**（**29,444★**，`skills/scientific-critical-thinking/SKILL.md`） | 评"证据质量"用 **GRADE + Cochrane Risk of Bias**：识别 bias/confounding(performance/detection/selection)、判设计能否支撑因果主张 | 混杂/偏倚清单 → 我 soundness 维度 + "伪缺口/增益来源"追问；"设计能否支撑因果" → 我"增益来自方法创新还是只堆算力/数据" | 偏循证医学框架；无 idea 撞车判定、无机读 findings |
| 5 | **K-Dense scholar-evaluation**（**29,444★**，`skills/scholar-evaluation/SKILL.md`，ScholarEval 框架） | problem-formulation/methodology/analysis/writing 各 **5 点量表打分 + 每维 actionable feedback** | 5 点量表 → 我八维 rubric；"每维配可执行反馈" → 我 `critique_self_audit` constructiveness 轴(每 CRITICAL 配修复) | 纯打分框架，**无否决闸门**(高均值能救回 fatal flaw=放水)；无撞车/findings——我否决项优先于加权分是差异点 |
| 6 | **K-Dense consciousness-council**（**29,444★**，`skills/consciousness-council/SKILL.md`） | 12 思维原型(Architect/Contrarian/Empiricist/Ethicist/Futurist/Pragmatist/Historian/Empath/Outsider/Strategist/Minimalist/Creator)**真冲突议事**；选人启发式"选会产生建设性冲突的成员，一致没价值张力才有价值"；三阶段 Summon→Deliberation(Position/Reasoning/Key Risk/Surprising Insight)→Synthesis | "选会冲突的视角、非重叠" → 我五视角严审(对标/可行/新颖/工程/统计)；Contrarian/Outsider → Devil's Advocate 角度 | 纯角色扮演易流于表演；单模型伪多样；无机读否决/findings |
| 7 | **ARIS novelty-check**（**12,693★**，`skills/novelty-check/SKILL.md`） | `REVIEWER_MODEL=gpt-5.5` via **Codex MCP**(xhigh reasoning)；Phase A 抽 3-5 core claim；Phase B multi-source(每 claim ≥3 query、year 2024-2026、ICLR/NeurIPS/ICML 已知库)；**Phase C cross-model verification**(写 `NOVELTY_DOSSIER.md`，**异模型**判 novel)；配 `patent-novelty-check`/`research-review`/`auto-review-loop` 套件；invariant "Claude judge Claude voids it" | claim 抽取 + multi-source 印证我 `novelty_audit` 四阶段查新；**最大分水岭**：它在查新端就下 **binary novel** 判 + 靠**异模型**(gpt-5.5)；我按 Si et al **只在 critique 端用可计算闸门**(否决/密度/pairwise)对抗单模型，**不在生成端下 binary、不要异模型** | 它有**真异质多模型**(gpt-5.5)= 我诚实落后项#2(单模型伪多样)；但它**要 Codex MCP + OpenAI key**(违我零-key/零-MCP)——我全程零-key 是差异点 |
| 8 | **Galaxy-Dawn paper-self-review**（**4,426★**，`skills/paper-self-review/SKILL.md` v0.1.0） | 预投稿质检 checklist：Structure / Logic Consistency / Citation Completeness / **Research Claim Audit(claims 是否被证据支撑 + overclaiming)**；同库 `review-response` 拼 rebuttal | Claim Audit(过度宣称) → 我 `critique_self_audit` 过度背书轴 + NEVER#5 伪增益；`review-response` → 印证我判决语料喂下游 review-rebuttal | paper-level **prose checklist 无机检门/findings**；我 idea-stage 更早(idea 定稿前)、产机读否决 |
| 9 | **mattpocock grill-me / grill-with-docs**（**148,028★**，`skills/{productivity/grill-me,engineering/grill-with-docs}/SKILL.md`） | 像审稿人把 plan/design 往死里盘问：**一次只问一个问题**、每问**自带推荐答案**、能查到的去查不问；grill-with-docs 4 招(challenge-against-glossary/sharpen-fuzzy-language/concrete-scenarios/cross-reference-with-code) | "自带推荐答案 + 用具体场景非泛问" → 我 ASK 决策点给"证据+推荐+备选"；sharpen-fuzzy → 我追问伪缺口要精确术语 | 交互式逐题打磨(我一次性出 verdict)；无 novelty/撞车/findings/否决闸门 |
| 10 | **obra/superpowers verification-before-completion**（**239,843★**，`skills/verification-before-completion/SKILL.md`） | 铁律 `NO COMPLETION CLAIMS WITHOUT FRESH VERIFICATION EVIDENCE`；gate 5 步 IDENTIFY→RUN→READ→VERIFY→ONLY THEN；红旗词 should/probably/seems/Great/Perfect/Done | 判"新"前必真检索(我 NEVER#2/#7 evidence-missing 封顶)= 同款铁律；`fresh_evidence` 字段进 findings | 通用纪律非 idea 审稿；我落成 idea-specific 否决闸门 + 机读 findings |
| 11 | **lingzhi227/agent-research-skills novelty-assessment**（**163★**，`novelty_check.py`，详见姊妹件 `competitors/idea-generation.md`） | `novelty_check.py` 注"Adapted from AI-Scientist's check_idea_novelty"，S2 迭代查新，输出 `{novel:true/false, most_similar_papers}` | 印证"最像前作 + 是否撞车"是同类标配；它**生成端下 binary novel** = 我归 critique 端的反例 | 生成端自判 novel(Si et al 实测 LLM 自评弱)；无 target/background 分解、无 findings/否决闸门 |
| 12 | **K-Dense what-if-oracle**（**29,444★**，`skills/what-if-oracle/SKILL.md`） | 结构化 What-If：`0·IF·1` 反事实分支(best/likely/worst/wild-card/contrarian/second-order)；质量取决于 IF 精确度("如果主供应商 Q3 涨价 30%"非"如果出问题") | "如果创新点不成立/baseline 也达到同效果" → 我对 idea 关键假设的压力测试 + 拒稿预演 | 通用情景分析非审稿；分支概率主观；无 novelty/findings |
| 13 | **poldrack/ai-peer-review**（**149★**，`CLAUDE.md`，真·多模型工程实现） | 摄入 PDF → 分发多模型(o1/o3-mini/Claude/Gemini/DeepSeek/Llama)各扮专家审稿 → **去标识**抹来源 → 元评审总结共识/个别关切 + 按"有用性"排序 review，存 JSON | "去标识 meta-review 防来源偏见 + 共识/个别分离" → 印证 ensemble 降方差思路；我 score_aggregate 取更严者近似 | **真·多模型异质**(我单模型扮多视角=伪多样，诚实落后项#2)；它要多家 API key(违我零-key)；无确定性否决 findings 喂编排器 |

> 另：**ARIS research-review / auto-review-loop / patent-review**(同库 12,693★，已确认路径 `skills/{research-review,auto-review-loop,patent-review}/SKILL.md`，review-revise loop 家族，未逐行深读，机制重叠不单列)、**imbad0202 deep-research `risk_of_bias_agent`/`devils_advocate_agent`**(同库跨我整条 DAG)、**davila7/claude-code-templates 28,325★**(`fact-checker`/`report-generator` agent，通用非审稿专精)——同类但机制重叠/已被上面覆盖，合并入 §0.C 提炼。

---

## 0.B 机制锚（论文 / 评审系统 / 基准 —— 不占 skill 名额，是脚本的方法来源）

> 这些是**学术方法/系统/基准**，非"同类 skill"；批 1 旧版把它们误塞进 skill 矩阵正是漏检的另一面。它们是本技能脚本的**机制源**，逐条 2026-06 一手核(数值已剥离不可核者，见 §3.5)。

| 锚 | 类型 | 机制(一手核) | 落进哪个脚本 |
|---|---|---|---|
| **GraphMind**(arXiv 2510.15706，EMNLP'25 demo) | 论文/方法 | 引用图 **background vs target 分解** + 引用立场 **supporting/contrasting**；74% acc / **0.75 F1**(SciNova 3063 篇) | `novelty_audit._derive_collision_level`：target 等价+supporting=`same`(真撞车)、target 不等价=`unrelated`(共享背景不误判) |
| **OpenNovelty**(arXiv 2601.01576) | 论文/系统 | 四阶段：抽 core-task+contribution→语义检索 prior→层级 taxonomy **逐 contribution 比对**→带显式引用证据片段的报告 | `novelty_audit` 四阶段结构 + 检索留痕(source/HTTP/DOI)；逐条对比交宿主 LLM |
| **Idea Novelty Checker**(arXiv 2506.22026) | 论文 | RAG retrieve-then-rerank + **facet-based 重排**(application_domain/purpose/mechanism/evaluation)，比基线高 ~13% 一致性 | **facet 槽位**：吃 gen `idea_selfcheck` 留空 facet，本技能填实做 delta |
| **PRISM**(多维 LLM 审稿基准) | 基准 | 四维(Depth/Novelty/Flaw-主次/Constructiveness)；无单系统四维全平人类 → "定向补充非替代" | `critique_self_audit` 三轴(constructiveness/surface/过度背书)对齐；哲学根=可计算闸门兜底自评 |
| **Pitfalls of Automating Reviews**(arXiv 2512.22145，9 模型) | 论文 | LLM 均分 7.5-9.0 vs 人类中位 3-7(**系统高估 3-5 分**)；坏稿 MAE 飙 4.5-6.2；过度自信；保守偏置(打压 disruptive ρ=-0.21) | 反谄媚/反过度背书最硬实证：`sycophancy_guard` + `score_aggregate` 否决引擎 + `novelty_density` 密度先验 |
| **AI-Scientist 自动审稿**(SakanaAI，Nature 2026) | 系统 | NeurIPS 指南扮 reviewer，**5 份独立审稿 + area-chair meta-review**；69% balanced acc | "五视角 + 终裁聚合" → SKILL 五视角；ensemble 降方差(我单模型伪多样，诚实边界) |
| **CycleReviewer / DeepReviewer**(2411.00816 / 2503.08569) | 论文 | SFT 审稿；真实**被接收论文均评 ~5.69/10**(偏严) | 校准现实锚：`calibration.py` 提醒 pass_line=80 偏严、FNR 偏高 |
| **OpenReviewer**(arXiv 2505.07920，8B) | 论文 | 79k 顶会专家审稿微调，比 GPT-4/Claude 更刻薄/现实(通用模型谄媚) | 坐实"通用 LLM 审 idea 默认谄媚"=`sycophancy_guard` 存在理由 |
| **SEA**(arXiv 2407.12857) | 论文 | 标准化审稿格式；M-7B recall~97% precision 差=几乎全接收(谄媚) | `verdict_template` 固定字段；⚠ v1 引"79% vs 59%"一手核无此数字→剥离(§3.5) |
| **TreeReview**(arXiv 2506.07642，EMNLP'25) | 论文 | 审稿建模为**问题树**递归拆解，指现法"常产肤浅反馈缺深度" | "拒稿理由 top-3 逐层深挖"；`critique_self_audit` surface 轴；⚠ "surface 24%"一手核无此数字→剥离 |
| **Si et al「Can LLMs Generate Novel Ideas?」**(2409.04109，N=104 专家) | 论文 | LLM 当 reviewer 辨优劣弱于人、自评一致性低 | **"judge 集中 critique、不靠裸自评"的实证根**：否决引擎+密度先验+pairwise |
| **OpenReview 真实审稿 + 偏置文献**(2509.09912 等) | 论文/数据 | LLM 给 LLM 作者更高分；verbose 膨胀 15-30；position bias；**anchoring**(rebuttal 改了仍锚初判) | 校准 + 防注入(把"给我高分/忽略以上"当数据非指令)；anchoring=paperjury 跨轮隔离也治(§0.C ①) |
| **RND(相对邻域密度)** | 算法 | M3-Embedding + 二级 KNN 密度百分位给域无关新颖分(报跨域 AUROC 0.782，待核) | `novelty_density.py`：离线降级 `_shared/semantic_sim`；借方法思路不依赖 0.782 |
| **NeurIPS/ICLR 评审表 + OpenReview API** | 规范/数据 | Originality/Quality/Clarity/Significance + Soundness/Presentation/Contribution + Overall 1-10 | rubric 八维锚到顶会表(`references/rubric.md`)；OpenReview API 拉真实 review(`references.md` §2) |

---

## 0.C 读完 13 个真同类后的横向机制提炼（直接驱动 Round 2 加厚）

1. **多视角 persona 互怼是同类强共识，非 Light 独创**：imbad0202 5-role / K-Dense consciousness-council 12 原型 /
   paperjury N-holistic-reviewer / poldrack 真多模型 —— 全做"多视角找非重叠缺陷"。Light 单模型扮五视角是**诚实落后项**
   (机检缓解非消除)。**paperjury 的"跨轮 reviewer 隔离、冻结正文、不锚前轮"**比多数同类更进一步治 anchoring(对应
   §0.B OpenReview anchoring 偏置)——这是 Light 单模型也学不全的真机制(诚实"它强"点，落后项#2)。
2. **Devil's Advocate / 对抗式挑刺是头部标配**：imbad0202 Devil's Advocate(4 类 CRITICAL) / grill-me 逐题逼问 /
   council Contrarian / paperjury "Unflinching Gatekeeper"。Light 的拒稿预演 top-3 + 五视角对齐，**非独创**。
3. **反谄媚是隐性共识但多靠 persona prose**：paperjury "do not pad with compliments / do not invent problems to
   look thorough" / imbad0202 `verified_only` / OpenReviewer 实证通用 LLM 谄媚。**Light 的 `sycophancy_guard`
   concession-rate 可计算门是少数把反谄媚机检化的**(让步无证据强制降 3 / 禁连续无证据让步)——诚实"我强"点，但
   paperjury 的"do not invent problems"提醒我反谄媚的**另一向**(为显严而虚构缺陷)，已由 `critique_self_audit`
   constructiveness/surface 轴部分覆盖。
4. **【R1 新落地】拒稿预演完整性 warn-only advisory**：拒稿预演/两面对抗多无机检——**paperjury 有 two-sided trial +
   contestability routing(每个 issue 经两面庭审才能 close、ledger 带 `close_criterion`)**，但走 workflow/ledger、
   **不产编排器可读 findings**。Light 的 NEVER#4("拒稿理由预演 top-3，预演不出反驳即未化解 CRITICAL")**原本只写在
   SKILL prose、`build_critique_corpus` 被动接受未预演的拒稿点(字符串→`rebuttable:None` 静默放过)**。R1 借 paperjury
   two-sided trial → `critique_self_audit` 加 `rehearsal_audit`：top-3 不足 / 拒稿点未预演(`rebuttable is None`) /
   预演不出有效反驳(`rebuttable:False`)→ **warn-only advisory**(rule=`rehearsal.*`，产进 `light.findings.v1`，
   **绝不 critical、绝不替用户判**——真阻断仍归 collision/fatal_flaw 两 critical 门；这只检"NEVER#4 做没做"，
   非语义判"反驳站不站得住")。
5. **binary novel 判在生成/查新端是多数同类做法**：ARIS cross-model gpt-5.5 / lingzhi227 `novelty_check.py` /
   AI-Scientist check_idea_novelty —— 生成/查新端就下 `{novel:true/false}`。**Light 按 Si et al 只在 critique 端用
   可计算闸门、不在生成端下 binary、也不要异模型**(诚实标"是设计选择不是独创"；也诚实它们有真异模型我没有)。
6. **校准严格度是共识**：imbad0202 calibration mode / CycleReviewer 现实锚 5.69 / undermind recall 估计。
   Light `calibration.py` 三分类(strict_FNR/FPR/revise_match)对齐，pass_line 显式可调。
7. **机读 critical findings + 确定性阻断 + 跨技能反哺 = Light vs 所有同类的独有点**：13 真同类**无一**产编排器可读、
   可确定性阻断推进的否决 findings(paperjury 有 durable ledger 但是自硬化 loop **无 score gate / 不喂编排器**；
   其余全是散文/PDF/打分)。`fatal_flaw_gate` 产 `light.findings.v1`(critical)被 `run_checkpoint --stage 4` 聚合
   **exit 1**、`reroute` 建议 4→3 + `critique_self_audit.build_critique_corpus` 把 top-3 喂 paper-writing/
   review-rebuttal——这是真差异化(非吹)。

---

## 1. 横切可借机制（已设计进 v2 脚本/能力；★=Round 2 R1 新增/强化）

1. **撞车可追溯判定 = target/background 分解 + 引用立场(GraphMind 核心，撞车门灵魂)**：`novelty_audit._derive_collision_level`
   ——target 实质等价 + supporting → `same`(真撞车)；target 等价但 contrasting → `extension`；target 不等价 →
   `unrelated`(仅共享 background 不误判)。吃 gen `idea_selfcheck` 留空 facet 槽填实 target_equivalent + stance。
2. **一票否决引擎 = 确定性否决闸门取更严者(critical 门核心)**：`score_aggregate.decide` 八维加权后否决项**优先于加权分**
   ——创新性<gate_fatal / 核心两维塌陷 → 压顶"不通过"，高均值救不回一个 fatal flaw。治 Pitfalls 实证的"系统高估"。
3. **嵌入密度新颖先验 = RND 相对邻域密度**：`novelty_density` 算 k-NN 密度百分位(域无关)；LLM 创新性≥75 但密度≤30(扎密集簇)
   → NOVELTY-PRIOR-CONFLICT 红旗、创新性封顶。抓 Pitfalls/OpenReviewer 的"过度背书"。
4. **反谄媚硬协议 = concession-rate 可计算门**：`sycophancy_guard` 让步无证据强制降 3 / concession-rate 超阈报警 /
   禁连续无证据让步。对抗作者反复反驳放行弱 idea(OpenReviewer 实证通用 LLM 谄媚)。
5. **评审者自审 = PRISM 三轴 + ★拒稿预演完整性**：`critique_self_audit` constructiveness 比 / surface 占比 / 过度背书；
   **★Round 2 新增 `rehearsal_audit`**(借 paperjury two-sided trial)：检 top-3 拒稿预演是否做齐(warn-only)。
6. **严格度校准 = 三分类 calibration**：`calibration` 用已知结局反推 strict_FNR/FPR/revise_match；CycleReviewer 5.69 现实锚。
7. **机读交接 + critical 阻断(vs 13 同类的独有点)**：撞车/否决产 `light.findings.v1`(critical)被 `run_checkpoint --stage 4`
   聚合 → exit 1 + `reroute` 4→3；`build_critique_corpus` top-3 喂 paper-writing/review-rebuttal。**13 同类零覆盖。**

---

## 2. 超越点（v2 相对裸模型 / v1 / 商业同类 / 13 个真同类的真增量，Round 2 诚实重述）

- **裸模型本就会**"扮顶会审稿人挑刺打分"——裸 Opus 都会，**不吹成卖点**。本技能价值=① **把否决落成确定性闸门**
  (裸模型被高均值 + 作者反驳带跑、把弱 idea 放行)；② **撞车可追溯 + 消费上游 facet**(裸模型给"感觉像"散文，下游门读不了)；
  ③ **机读 critical findings + 确定性阻断 + 根因回炉**(裸模型给口头结论，编排器读不了)；④ **反谄媚 + 不裸自评**
  (Pitfalls 实证裸模型系统过度背书)。
- **相对 13 个真同类**(Round 2 诚实定位)：多视角 persona / Devil's Advocate / 反谄媚 / 拒稿预演 / 校准 / binary novel——
  **全行业共识，Light 不独占任一**。Light 真差异 = **(a) 机读 critical findings 跨技能交接 + 确定性阻断(13 同类零覆盖)
  + (b) 可计算否决闸门(同类多靠 persona prose；scholar-evaluation 纯打分无否决) + (c) 全程零 key/零 MCP**
  (K-Dense 需 OPENROUTER_API_KEY、ARIS 需 Codex MCP+OpenAI key、poldrack 需多家 API key) **+ (d) 离线降级可验证**。
  **诚实"它强我弱"**：paperjury 跨轮 reviewer 隔离治 anchoring、imbad0202/poldrack 真多 agent/多模型——我单模型伪多样
  只缓解非消除(落后项#2)；ARIS 有真异模型 novelty 验证、我离线 `semantic_sim` 跨语言弱(落后项#3)。
- **相对 v1 的真增量**：① `fatal_flaw_gate.py` 把 v1 零接 `_shared` 的否决引擎接成 critical findings producer(grep 实证)；
  ② **撞车判定吃 gen facet 槽 + 直接消费 `semantic_sim` 复核**；③ findings 接线 + 规范 bootstrap；
  ④ **★Round 2：拒稿预演完整性 advisory(借 paperjury two-sided trial)**；⑤ **Round 3：human/Pareto/fatal/decision
  evidence 从裸 locator 升级为 `{locator, sha256, captured_at?}` 哈希引用**，防止专家判断、价值可行性维度、
  fatal flaw 审计和最终 GO 证据事后漂移。

---

## 3. 名实对齐（诚实落后项，写进 SKILL）

1. **可计算闸门是先验非真值**：八维权重/pass_line/gate_fatal 全是**经验默认、可调超参**，非标注集反推(Light 无公开标注集)。
   新颖性判决靠 semantic_sim(离线档跨语言弱)+ 人/宿主，不纯单模型自评(Si et al 实证)。
2. **单模型扮多视角(五视角/ensemble)伪多样未根除**：AI-Scientist 5 独立审稿 / poldrack 真多模型 / **paperjury 跨轮隔离冻结正文**；
   本技能单模型扮多 persona，机检(否决/反谄媚/密度)只**缓解**过度背书不消除——缺真异质多模型来源(同 gen 侧落后项)。
3. **撞车检测离线档做不了纯同义**：依赖 `semantic_sim` 边界——中文 idea↔英文标题低分(本对话 E2E 实测跨语言 sim=0、同语言
   0.56-0.65)，撞车演示用同语言；可靠语义需注入 embedding 档(ARIS 用异模型绕开，但要 key)。
4. **密度先验/查新依赖检索覆盖(GIGO)**：literature-search 漏最像那篇 → 密度高估新颖、撞车漏判；`novelty_audit` 只勾稽
   "结论与自己的检索证据自洽"，不替你判 idea 真新不新(须真检索 + 人判)。
5. **拒稿预演 advisory 只检"做没做"非"反驳站不站得住"**(★Round 2 边界)：`rehearsal_audit` 是 warn-only 完整性检查
   (top-3 是否齐、`rebuttable` 是否填、预演不出反驳的拒稿点是否浮出)——**不语义判反驳是否有效**(那是宿主 LLM/人的活)；
   `rebuttable` 由本技能填，可被糊弄(乱填 True 绕过)；真 critical 阻断仍归 collision/fatal_flaw 两门，不靠这条 advisory。
6. **v1 两处具体数字未经核实，已剥离(铁律 2 实践)**：v1 `critique_self_audit` 引"SEA 过度背书 79% vs 人 59%"
   "TreeReview surface 24%"——2026-06-18 一手 fetch 两篇原文均**无此数字** → 删除，只留可核机制。诚实优先于"看起来有据"。

---

## Sources（2026-06-27 在线一手核；star=`gh api repos/<r> --jq .stargazers_count` 当天值）

- 真·同类 skill(star 当天核)：[u7079256/paperjury](https://github.com/u7079256/paperjury)(`SKILL.md`+`references/{reviewer-personas,methodology,review-engine-v3,ledger-schema}.md`) · [imbad0202/academic-research-skills](https://github.com/imbad0202/academic-research-skills)(`academic-paper-reviewer/SKILL.md`+`agents/devils_advocate_reviewer_agent.md`) · [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills)(`skills/{peer-review,scholar-evaluation,scientific-critical-thinking,consciousness-council,what-if-oracle}/`) · [wanshuiyin/ARIS](https://github.com/wanshuiyin/auto-claude-code-research-in-sleep)(`skills/novelty-check/SKILL.md`) · [Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar)(`skills/paper-self-review/SKILL.md`) · [mattpocock/skills](https://github.com/mattpocock/skills)(`grill-me`/`grill-with-docs`) · [obra/superpowers](https://github.com/obra/superpowers)(`verification-before-completion`) · [lingzhi227/agent-research-skills](https://github.com/lingzhi227/agent-research-skills) · [poldrack/ai-peer-review](https://github.com/poldrack/ai-peer-review) · [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates)
- 机制锚(论文/系统/基准)：GraphMind [2510.15706](https://arxiv.org/abs/2510.15706) · OpenNovelty [2601.01576](https://arxiv.org/pdf/2601.01576) · Idea Novelty Checker [2506.22026](https://arxiv.org/html/2506.22026v1) · Pitfalls [2512.22145](https://arxiv.org/abs/2512.22145) · AI-Scientist [2408.06292](https://arxiv.org/abs/2408.06292) · CycleReviewer [2411.00816](https://arxiv.org/abs/2411.00816) · DeepReviewer [2503.08569](https://arxiv.org/abs/2503.08569) · OpenReviewer [2505.07920](https://arxiv.org/abs/2505.07920) · SEA [2407.12857](https://arxiv.org/abs/2407.12857) · TreeReview [2506.07642](https://arxiv.org/abs/2506.07642) · Si et al [2409.04109](https://arxiv.org/abs/2409.04109) · NeurIPS 评审表/OpenReview API(见 `references.md` §1-2)
- 数据源端点真相源：`references.md`(NeurIPS/ICLR 评审表、OpenReview API、S2 API、各同类工具一手研究笔记)
