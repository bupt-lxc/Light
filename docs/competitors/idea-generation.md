# competitors — light-idea-generation（科研主线 stage 3 · 提 idea ⇄ stage 4 审 idea）

> 铁律 1+2 对标笔记:动手前深读最强同类,**机制上网核实(star=[snapshot 2026-06-26, src=GitHub repo 页/`gh api`
> stargazers_count 当天核],非凭记忆)**,落地可借机制 + 标清超越点与诚实边界。本技能是**科研主线 DAG 第 3 节点**
> (与 4 双向回环 3⇄4):结构化发散,产**"值得做且做得成"的分层候选 idea**(moonshot/solid/safe),每个自带
> why/创新点/**撞车前置自查**。**接 `_shared`** —— 产 `light.findings.v1` 的是**信号/自查型 findings(撞车前置
> 预警 + 发散覆盖,warn 为主)**,**critical 一票否决判决归 idea-critique(stage 4)**:Si et al(2409.04109)实测
> "LLM 不能可靠评 idea 质量",故生成端只产信号、不自评 novel。
>
> 写作:批 1 第二技能·gen 侧(2026-06-18);**Round 2 R1 重做(2026-06-26)**——治"高 star 同类 skill 漏检"系统病。
> 作者 Light0305 + Claude。下游成对件见 `competitors/idea-critique.md`。

---

## ⚠ Round 2 R1 系统病诚实校正（先认错,再对标）

批 1 旧版 §0 把 16 行**混排成"论文 + 学术系统 + 少量 skill"**,真·同类 **Claude/agent ideation skill 只正式拆了
约 3 个**(Orchestra brainstorming-research-ideas、research-companion、Creative Director),其余 13 行是 Si et al /
AI-Scientist / co-scientist / ResearchAgent 等**论文/系统**。这正中审计点名的系统病:**高 star 同类 skill 漏检**。
Round 2 一手核 GitHub(`gh api`)后实情 = **提 idea/查新是 Claude skill 生态相当拥挤的赛道**,≥9 个真·同类 ideation
skill 各自完整,**6 个千 star 级**:

- **imbad0202/academic-research-skills 34,638★**(idea-discovery 模式 + 7 失败模式点名 frame-lock) /
  **K-Dense scientific-agent-skills 29,386★**(scientific-brainstorming + hypothesis-generation 双子) /
  **davila7/claude-code-templates 28,308★** / **alirezarezvani/claude-skills 19,115★** /
  **wanshuiyin/ARIS 12,663★**(idea-creator + novelty-check + patent-novelty-check 套件) /
  **Galaxy-Dawn/claude-scholar 4,415★**(research-ideation:5W1H + 5 型 gap + falsification) /
  **andrehuang/research-companion 686★** / **lingzhi227/agent-research-skills 162★**(**同名 idea-generation** +
  novelty_check.py) / **lyndonkl/claude 127★**(brainstorm-diverge-converge + check-analogy-novelty)……

**结论:旧版"ideation 同类稀疏"的隐含判断 = 漏检,推翻**(同 figure scipilot / frontend ui-ux-pro-max /
lit-search 实证的同一系统病)。**诚实重述超越点**(防做偏):结构化发散算子(类比/反转/尺度/约束)、撞车/novelty 查重、
数量漏斗(diverge→converge)、分层、可证伪——**全是同类强共识,Light 一个都不是"唯一想到"**;Light 的真增量 =
**机读 findings 接线 + `_shared` 复用 + 反 frame-lock 机检门(exit 1 非建议清单) + 生成端不自评 novel(按 Si et al)
+ 离线降级 + 跨 harness**(见 §0.C / §2)。**新落地(R1→脚本):借 K-Dense testability + Galaxy-Dawn falsification 给
`card_gate` 加可证伪/可测量阈值 warn-only advisory**(详 §0.C ⑥)。

---

## 0.A 真·同类 ideation SKILL（9 个真同类 · R1 硬指标 · star=[snapshot 2026-06-26, `gh api` 当天核]）

> 判据:每条**已读其 SKILL.md/脚本/agent**(带可复验点:文件名/常量/行为),非列名字。优先千 star。

| # | 同类 skill（star） | 它怎么做（已读 SKILL/脚本,带可复验点） | 我借进哪个能力 | 我诚实差在哪 |
|---|---|---|---|---|
| 1 | **lingzhi227/agent-research-skills**（**162★**,`skills/idea-generation/SKILL.md`+`scripts/novelty_check.py`) | **与本技能同名 idea-generation**;3 维评分 Interestingness/Feasibility/Novelty(1-10,"Be cautious and realistic");`novelty_check.py`(注释"Adapted from AI-Scientist's check_idea_novelty"):迭代 S2 `paper/search`,`FIELDS="title,authors,venue,year,abstract,citationCount"`,`--max-rounds`,429 退避 `2**(attempt+1)`;输出 `{novel:true/false, most_similar_papers:[...]}`;workflow Generate 3-5→iterative refine(≤5 轮)→novelty assess→rank | `most_similar_papers`→撞车自查 most_similar;3 维快评印证 idea_card 自评 triage;"harsh novelty critic"印证查新先于宣称 | **它在生成端直接下 binary `novel:true/false` 判决**——这正是 Light 按 Si et al **拒绝**做的(生成端只产 warn,novel 判归 idea-critique)。**真分水岭**(§0.C ①)。它单源 S2(限速 429)、无机读 findings/`_shared`、无 frame-lock 覆盖门 |
| 2 | **wanshuiyin/ARIS**（**12,663★**,`skills/idea-creator`+`novelty-check`+`idea-discovery`+`patent-novelty-check`) | 完整 ideation 套件;idea-creator 常量 `PILOT_MAX_HOURS=2`/`MAX_PILOT_IDEAS=3`/`MAX_TOTAL_GPU_HOURS=8`/`OUTPUT_DIR=idea-stage/`;`REVIEWER_MODEL=gpt-5.5`+`REVIEWER_BACKEND=codex`(Codex MCP xhigh);**cross-model invariant**:"pasting into any Claude product makes Claude judge Claude and **voids the cross-model invariant**";novelty-check Phase A 抽 3-5 claims→Phase B 多源(WebSearch arXiv/Scholar/S2 + ICLR/NeurIPS/ICML known DB)→Phase C cross-model Codex 验 | 阶段化 landscape→generate→check→pilot 印证 lit→idea→critique 接线;Phase A 抽 claims→撞车 facet;PILOT 预算意识→数据/算力可行性卡 | **cross-MODEL novelty(gpt-5.5)比 Light 离线 `semantic_sim` 强**——但要 OpenAI key + Codex MCP(违 Light 零 key/零 MCP);它跑真 pilot(GPU 预算)=Light 下游 experiment-coding 不在本技能;它 `AUTO_PROCEED` 自动取最优,**Light 绝不自动选/投** |
| 3 | **K-Dense-AI/scientific-agent-skills**（**29,386★**,MIT,`skills/scientific-brainstorming`+`hypothesis-generation`) | 双子 ideation:scientific-brainstorming(开放发散,5 阶段 context→divergent→connection→critical→synthesis,4 技法 **Cross-Domain Analogies/Assumption Reversal/Scale Shifting/Constraint Removal-Addition** + `references/brainstorming_methods.md`);hypothesis-generation(可检验假设 + competing explanations;**`references/hypothesis_quality_criteria.md` testability 要可测量结果**,例 `">30%"`/`"50% reduction within 4 weeks"`;**MANDATORY 1-2 AI schematic** via Nano Banana Pro;`OPENROUTER_API_KEY`) | **★R1 落地源**:hypothesis_quality_criteria 的 testability(可测量结果)→`card_gate` 可证伪 advisory(§0.C ⑥);4 技法印证 provocation 算子;competing explanations→idea_card 竞争性解释 | 它**强制 AI 生成图**(Nano Banana Pro)——Light figure 红线**绝不 AI 生图**(真分歧);要 `OPENROUTER_API_KEY`;开放发散是对话引导,Light 是 exit-1 机检覆盖门 |
| 4 | **Galaxy-Dawn/claude-scholar**（**4,415★**,`skills/research-ideation/SKILL.md`+`references/gap-analysis-guide.md`) | "vague idea→**traceable research contract**"(research question/hypothesis/evidence needs/**falsification criteria**/method/next action);**5W1H**(What/Why/Who/When/Where/How);**5 型 gap analysis**(literature/methodological/application/interdisciplinary/temporal);Zotero DOI 集成;可 invoke superpowers:brainstorming | **★R1 落地源**:falsification criteria→`card_gate` 可证伪 advisory(§0.C ⑥);5 型 gap→R2 找 gap 工作流 + provocation gap-driven;"vague→contract"=Light Level 1/2 分级 + idea_card 可逐字段复核契约 | Zotero(本地库),Light 零本地库按需 lit-search 在线取数;5W1H 是引导框,Light 7 角度是机检覆盖门;无机读 findings |
| 5 | **lyndonkl/claude**（**127★**,`skills/brainstorm-diverge-converge`+`check-analogy-novelty`+`concept-rediscovery-walk`) | brainstorm-diverge-converge(5 步 Gather→**Diverge 30 ideas no judgment**→Cluster 6 themes→Converge against criteria→Document&Validate;`resources/evaluators/rubric_*.json` 评分器);check-analogy-novelty(每 analogy 对 `analogy-catalog.md` grep,**分 new / reused-from-catalog / adjacent-to-catalog 三档防复用**,"Close variant"=same source domain) | Diverge30→Converge 印证数量漏斗 ≥15→3-6;check-analogy-novelty 的**确定性 catalog-grep 防复用**=Light `candidate_dedup`(semantic_sim 变体对)同源思想(查重防换皮) | 它 analogy 防复用查**持久 catalog**(跨会话历史),Light `candidate_dedup` 只查**批内**变体对(跨会话历史靠 memory-pm,本技能暂不接);它 rubric 建议性,Light 是 exit-1 机检门 |
| 6 | **imbad0202/academic-research-skills**（**34,638★**,CC BY-NC,`deep-research/` idea 模式) | 13-agent 编队含 `devils_advocate_agent`;8 模式含 idea-discovery/Socratic;`DISTRIBUTIONAL_SKEW_ADVISORY`(语料时间/方法/地域集中度 warn + 补救检索式);**7 失败模式点名 `frame-lock`(锁死单一框架)** + 引用幻觉 | **frame-lock 失败模式**印证 Light `provocation --coverage` 反 frame-lock 门设计正确(同名同病);devils_advocate→idea-critique 对抗;skew advisory(lit-search 已借年代轴) | LLM-agent 散文式,无机读 findings/`_shared`;CC BY-NC(非商用);idea 散在 deep-research,非独立 ideation 脚本编排 |
| 7 | **andrehuang/research-companion**（**686★**,`agents/brainstormer`+`idea-critic`+`research-strategist`) | "Strategic research thinking — **idea evaluation, project triage, structured brainstorming**. Helps you decide **which papers to write**, not just how";brainstormer + idea-critic(下游审)+ research-strategist 三 agent | brainstormer→idea-critic 双 agent 印证 Light gen→critique 双子 3⇄4 接线;"decide which papers to write"=Light 分层(moonshot/solid/safe)+ 院士思维"下一突破口" | 偏决策三连(idea/triage/frame),无 findings/`_shared` 机读交接,无撞车 semantic_sim/覆盖度门 |
| 8 | **alirezarezvani/claude-skills**（**19,115★**,337 skills,`.claude/.codex/.gemini` 三 harness 镜像) | 跨 8+ harness 超大包,含 `autoresearch-agent`/`research`/`product-research` 等研究类;30+ agents/70+ commands | 跨 harness 兼容(同一 skill 镜像到 .codex/.gemini)印证 Light 跨 harness 定位 | 广而非深,ideation 是一个抽屉,无三层/findings/撞车门;product/market-research 偏商业 |
| 9 | **davila7/claude-code-templates**（**28,308★**,`components/agents/data-ai/simple-app-idea-generator`+`deep-research-team`) | simple-app-idea-generator(**产品 app idea** 生成);deep-research-team 编队(academic-researcher+query-clarifier+fact-checker) | query-clarifier 先澄清→Light ASK 输入分级决策点;fact-checker→撞车留痕核真 | **app idea 生成器是产品向非科研向**(诚实:davila7 的 ideation 是其弱项,真科研 ideation 不及上面几家);deep-research-team 偏检索非 ideation |

> 另(低 star/支撑,不占名额):**itshussainsprojects/Claude-Council-Skill**(61★,多 archetype 议会辩论)、
> **ashrafkahoush-ux/claude-consciousness-skills**(3★,what-if-oracle 精确 IF / consciousness-council 多视角)——
> 批 1 references 已研究,机制(多视角议会 / 精确 IF 反事实)并入 §0.C ⑤。批 1 曾列"Orchestra
> brainstorming-research-ideas / Creative Director / claude-brainstorm":本轮 `gh search` 仅命中 prompt 合集/同名异物,
> **未能定位可验证 repo(无 star 可核)→按可复验铁律不计入**,改以上 9 个一手核同类替代(诚实:批 1 名字可能源自已删/改名 repo)。

### Round 3 五席纠偏（2026-07-05）

105 项矩阵原第 4 席写 DeerFlow，只能证明长程编排，不是科研创意生成。现替换为
`K-Dense-AI/scientific-agent-skills/scientific-brainstorming`：父仓 GitHub API
30,189★、MIT，固定 `26fd7a84512acdb6f00b40a4f4675cacf22cb2df`。本轮重新完整读取
188 行 `SKILL.md` 与 326 行 `references/brainstorming_methods.md`，确认其直接覆盖：

- 先理解研究者的 field、method、constraints 与隐含假设；
- divergent exploration 中使用 cross-domain analogy、assumption reversal、
  scale shifting、constraint removal/addition；
- 再做 critical reflection、feasibility-preserving synthesis 与 next steps。

这些机制已经在 Light 的 provocation 算子、反 frame-lock 覆盖门、分层收敛和交给用户选择中
落地，因此本轮没有为“看起来有改动”重复造脚本。K-Dense 的开放对话式发散比 Light 更自然，
Light 的增量是覆盖度/伪多样/谱系证据可机检；二者都不证明生成 idea 真正新颖。

---

## 0.B 机制锚（论文 / 学术系统 / 通用技法 —— 不占 skill 名额,仍是有价值的学术/机制锚源）

> 这些是**研究论文 / 自动科研系统 / 通用创意技法**,非"同类 skill";批 1 旧版把它们误塞进 skill 表是漏检的另一面。
> 逐条 2026-06 核;详细逐项研究(端点/参数/复用)见 `references.md`。

| 锚 | 类型 | 机制(一手核) | 我借/我边界 |
|---|---|---|---|
| **Si et al「Can LLMs Generate Novel Research Ideas?」**(arXiv 2409.04109,ICLR 2025,N=104 专家) | 论文(实证地基) | 过量生成数千 seed→pairwise tournament;**①扩规模后 idea 多重复(多样性塌缩)②LLM 当 reviewer 辨优劣弱于人③AI idea 新颖高但可行低** | **整个设计的实证地基**:①→`candidate_dedup` 防伪多样;②→**生成端不自评 novel**(judge 归 idea-critique);③→`card_gate` 强制可行性。不做数千 seed 大池(token 经济) |
| **AI-Scientist v1/v2**(SakanaAI,2408.06292 / 2504.08066) | 自动科研系统 | v1 模板四件套 ideation + S2 查新(`generate_ideas.py` 三维自评 Interestingness/Feasibility/Novelty 1-10);v2 `perform_ideation_temp_free.py`(主题四件套 Title/Keywords/TL;DR/Abstract)+ BFTS 树搜索 | 三维快评→idea_card triage;主题四件套→立项卡范式;**它生成端自评 novel,Light 不自评**(lingzhi227 即移植其 `check_idea_novelty`) |
| **Google co-scientist**(2502.18864,Nature 2026) | 多 agent 系统 | Generation/Reflection/**Ranking**/Evolution/Proximity/Meta-review + **Elo pairwise tournament**(辩论定优劣) | **pairwise>绝对自评**坐实→`swiss_rank.py` ELO 两两配对;evolve→被毙 idea 带方向回炉(⇄4) | 单模型扮多 agent,非真异质多模型 |
| **ResearchAgent**(2404.07738,NAACL 2025) | 论文 | **实体中心知识库**(共现矩阵)+ 引文子图增广;ReviewingAgent 5 维(Clarity/Relevance/Originality/Feasibility/Significance)迭代 | 实体抽取→`provocation_gen` 跨域强配;5 维→自检清单;迭代→⇄idea-critique | **无本地实体 KG**(零本地库),靠按需 lit-search + semantic_sim |
| **SciMuse**(2405.17044,ICML 2024) | 论文 | 58M 论文 KG(123k 概念)选概念对喂 GPT-4;**冷门概念对(低 degree/PageRank)→idea 更"有趣"**;训练有趣度预测器 | **冷门概念对=有趣度信号**(provocation 偏好不常配对实体) | **无训练好的有趣度预测器**(它有 4000 标注;Light 自检分是启发式无数据背书) |
| **Facet Recombination + Novelty Eval / Idea Novelty Checker / OpenNovelty**(2409.14634 / 2506.22026 / 2601.01576) | 论文 | idea 拆 **facet**(application_domain/purpose/mechanism/evaluation)重组 + 沿 facet 评 novelty;检索→SPECTER2 top-100→RankGPT facet 重排→≥1 核心 facet 不同即 novel | **facet 槽位**撞车自查→吃上游 lit-search facet 拆 delta;**novel 判决不自做**(归 idea-critique) |
| **IdeaBench / AI Idea Bench 2025**(KDD 2025 / 2504.14191) | benchmark | 高影响论文 + 参考构情境;BERTScore + idea-overlap;**"LLM 善新颖、苦于可行"** | 再坐实可行性软肋→`card_gate` 数据/算力必答;不做 benchmark 相对排名 |
| **MAGenIdeas / Combinatorial Creativity**(2410.14255 / 2412.14141) | 论文 | 迭代规划检索"该检索什么外部知识";组合创新跨域重组;Swiss Tournament 选 top | 跨域重组→provocation combination 角度;瑞士轮→`swiss_rank.py`;**v1 误引"×3.4 倍/×2.5 倍"具体数字本轮未独立核实→剥离不引** |
| **CHIMERA / AI 评判随时间漂移**(2505.20779 / 2511.04964) | 论文 | 科学 idea 重组 KB;**AI ideation 评判随时间漂移**(同 idea 不同时判不同) | 漂移=诚实边界:撞车自查带 HTTP 码 + 时点留痕,非一次定终身 |
| **OpenAlex concept/topic graph**(API,免 key) | 数据源 | `group_by=primary_topic.id` 出主题计数看方向饱和/稀疏;`referenced_works`/`related_works` | 撞车检索经 lit-search `domain_map`(不在本技能直连);接入口径以 lit-search references 为唯一真相源 |

---

## 0.C 读完 9 个真同类后的横向机制提炼（直接驱动 Round 2 加厚）

1. **"生成端是否自评 novel"是真分水岭(诚实最关键一条)**:lingzhi227(`novel:true/false`)、AI-Scientist(`check_idea_novelty`)、ARIS(cross-model gpt-5.5 判)——**多数同类在生成端就下 novel 判决**。Light 按 Si et al(N=104 实证"LLM 不能可靠自评 idea")**只产 warn 信号、judge 归 idea-critique**。这是 Light 的**设计选择**(选了 Si et al 这条路),诚实**不吹"只有 Light 想到不自评"**——而是"Light 选择不自评,且把它做成 gen/critique 接线分离"。
2. **撞车/novelty 查重是同类标配,非 Light 独创**:lingzhi227 `novelty_check.py`、ARIS `novelty-check`/`patent-novelty-check`、lyndonkl `check-analogy-novelty` 全做查重。Light **不吹独创撞车检测**;增量 = 接 `_shared/semantic_sim` + 吃上游 lit-search 领域地图 facet + 产**机读 findings**(9 同类无一产编排器可读 findings)。
3. **发散算子(类比/反转/尺度/约束)是强共识**:K-Dense 4 技法(Cross-Domain Analogies/Assumption Reversal/Scale Shifting/Constraint Removal-Addition)与 Light 7 角度算子**几乎一一对应**,Creative Director SCAMPER/TRIZ 同源。Light **不吹独创算子**;增量 = **机检覆盖门**(某角度 0→exit 1),非建议性清单。
4. **数量漏斗(diverge 多→converge 少)是共识**:lyndonkl Diverge30→Converge、Si tournament、brainstorm-diverge-converge。Light ≥15→3-6 **对齐底线**,诚实不吹。
5. **frame-lock / 多视角是公认机制**:imbad0202 7 失败模式**点名 frame-lock**;Claude-Council/consciousness 多 archetype 议会;Perspectra 选异质专家。印证 Light 反 frame-lock 门 + 多角度发散设计正确(**同名同病=设计被同类背书**),非 Light 凭空。
6. **【R1 新落地】可证伪 / 可测量阈值 advisory**:借 **K-Dense `hypothesis_quality_criteria`(testability:可测量结果 ">30%")** + **Galaxy-Dawn research-ideation(falsification criteria)**。审查发现 `card_gate` **原本完全不校验**模板的「最小验证实验」「风险与失效条件」两节——卡可留空模板仍过门。R1 给 `card_gate` 加 **warn-only 机检**:两节缺可测量阈值(数字+比较符/指标/单位)或量化失效条件→警示(顶会无可证伪预测=常见 desk-reject)。**只 warn 绝不阻断**(真判归 idea-critique)。诚实:**可证伪是同类共识**(K-Dense/Galaxy-Dawn/Hypothesis Generation 都强制),Light 增量 = **确定性机检 + 顶会 reviewer 视角**,不是"想到了可证伪"。
7. **机读 findings 跨技能交接 = Light 全市场独有**:9 个真同类 + 0.B 所有系统**无一**产编排器可读的机读 findings(全散文/JSON 自用/md)。`light.findings.v1` 被 `run_checkpoint --stage 3` 聚合 = Light 接线面,真差异化(非吹)。

---

## 1. 横切可借机制（已设计进 v2 脚本/能力；★=Round 2 R1 新增/强化）

1. **结构化发散 = 激发算子 × 核心实体(非泛泛头脑风暴)**:7 角度(gap-driven/method-transfer/data-driven/
   problem-reframe/combination/theory-gap/efficiency)由结构化算子(空白直击/技术外推/尺度切换/假设反转/失效驱动/
   约束增删 + 跨域强配)**机械生成发散提问**(`provocation_gen.py`)。借 **K-Dense 4 技法** + ResearchAgent 实体抽取 +
   Combinatorial Creativity 跨域重组。**提问是脚手架,洞察靠人/宿主 + 文献(GIGO)。**
2. **反 frame-lock = 机检覆盖门(本技能真增量,强于同类的"镜头清单/失败模式清单")**:imbad0202 把 frame-lock 列为
   失败模式(**清单式**)、lyndonkl/Council 给建议性发散清单;Light 落成**可机检门**——候选 <15 或**某角度 0
   候选 → exit 1 拦在收敛前**。"别在一条思路上死磕"从口头变可执行。
3. **防伪多样 = semantic_sim 两两去重(治 Si 实测的多样性塌缩)**:`candidate_dedup.py` 复用 `_shared/semantic_sim`
   按批内 mean+1σ 自动标"疑似变体对"。**lyndonkl `check-analogy-novelty` 的 catalog-grep 防复用是同源思想**(确定性查重防换皮),
   差别:它查持久 catalog,Light 查批内(跨会话历史靠 memory-pm)。
4. **撞车前置自查 = semantic_sim + 吃上游 facet 槽位(本技能的机读 findings 灵魂)**:提 idea 时即带"最像前作 +
   facet delta",**吃 `literature-search` 领域地图**(most_similar + application_domain/purpose/mechanism/evaluation
   空槽)。借 Idea Novelty Checker/Facet Recombination 的 facet 分解 + lingzhi227 `most_similar_papers`。**只产 warn 信号
   + facet 待拆,不下 novel 判决**(Si:LLM 不能自评)→ light.findings.v1 喂 idea-critique。
5. **立项卡完整性门 + 反敷衍 + ★可证伪 advisory**:`card_gate.py` 校验硬字段非空且非敷衍占位(填"无/更好/有数据"冒充→
   拦下);最近邻 ≥3 带留痕、新颖性归三档。**★Round 2:加可证伪/可测量阈值 warn-only advisory**(借 K-Dense testability +
   Galaxy-Dawn falsification,校验「最小验证实验」「失效条件」两节)。借 IdeaBench/Si"可行性是软肋"→数据/算力必答。
6. **Round 3 证据可交接门**:`idea_genealogy.py` 原已把证据根→机制 delta→资源账→最小判别实验做成 critical 门；本轮补上
   证据"能不能交给陌生用户复核"的缺口：`VERIFIED` source evidence 需要公开 locator+SHA-256+非未来 `checked_at`，
   `AVAILABLE` resource 需要 `evidence_locator + checked_at`，并拒绝模板占位、本机绝对路径、UNC/根路径、`../` 越界和 `file:`。
   这使 Light 的"可扩展/可用资源"不再靠私有电脑、口头承诺或未来日期支撑。
7. **pairwise > 绝对自评 + 分层组合裁定(co-scientist Elo + Si/MAGenIdeas tournament)**:`swiss_rank.py` 瑞士轮 ELO
   两两配对(压自报分);`rank_ideas.py` 分 moonshot/solid/safe 各自排序再 round-robin——**突破口不被单一性价比榜压杀**。
   Si 实证自评与人一致性仅 ~53%。
8. **机读交接(本技能 vs 所有同类/系统的独有点)**:撞车自查 + 发散覆盖产 `light.findings.v1`,被 `run_checkpoint
   --stage 3` 聚合,与 stage 4 idea-critique 构成 3⇄4 回环。**9 真同类 + 0.B 系统无一产编排器可读 findings。**

---

## 2. 超越点（v2 相对裸模型 / v1 / 9 真同类 / 学术系统的真增量,Round 2 诚实重述）

1. **机检 frame-lock 门**:同类(imbad0202 失败模式清单 / lyndonkl rubric / K-Dense 对话引导 / Council 议会)给**建议性**
   发散/检查清单;Light 给**确定性覆盖门**(角度 0 → exit 1),把"发散够不够"从手感变可阻断判定。
2. **撞车检测接共享语义引擎 + 上游领域地图 facet 并产机读 findings**:lingzhi227/ARIS 查新但**在生成端下 novel 判**
   (违 Si 的"LLM 不能自评");Orchestra/Council 无撞车检测。Light **生成产信号 / 审稿下判决**清晰分离,且撞车信号
   是 `light.findings.v1` 机读件(同类全是散文)。
3. **生成端不自评 novel(按 Si et al 实证)**:多数同类(lingzhi227/AI-Scientist/ARIS)生成端自判 novel;Light 选 Si 的
   实证结论——只产 warn,judge 归 idea-critique。**这是设计分歧非缺陷**,诚实标"是选择不是独创"。
4. **分层组合裁定(moonshot/solid/safe)防突破口被压杀** + **反敷衍立项卡门 + ★可证伪 advisory**:lane-aware 排序 +
   card_gate 抓"填占位假装查过" + 借 K-Dense/Galaxy-Dawn 把可证伪做成机检 warn。
5. **谱系证据和资源可交接**:同类常把"有数据/有算力/有前作依据"写成自然语言；Light 的 genealogy 门要求可交接 locator、
   hash、检查日期和资源证据定位符，公开产品用户可以复核，不必相信作者私有环境。
6. **零 key/零 MCP/零本地库 + 离线降级 + 跨 harness**:ARIS 要 OpenAI key+Codex MCP、K-Dense 要 OPENROUTER、
   ResearchAgent/SciMuse 要本地大 KG;Light 全程零 key/零 MCP/零本地库,撞车检索经 lit-search 在线取数,无网回退合成样本。

---

## 3. 诚实边界（已知做不到 —— 写进 SKILL 名实对齐,绝不掩饰）

1. **生成端不下 novel/质量判决**(设计如此,非偷懒):Si et al 实测 LLM 自评 idea 弱;故只产**撞车 warn 信号 + facet 待拆
   + 启发式自检分**,novel 的 critical 一票否决归 idea-critique(stage 4)。**这是分工不是缺陷。**
2. **撞车信号弱于 cross-model / SPECTER2**:ARIS 用 gpt-5.5 跨模型查新、Idea Novelty Checker 用 SPECTER2 768 维;Light
   离线 `semantic_sim` 对**无共词纯同义/跨语言**(中文 idea↔英文标题)弱(lit-search 实证中文 sim≈0.1)。须注入 embedding 档,
   离线档不假装能做,撞车演示用同语言。
3. **无本地实体 KG / 有趣度预测器**:ResearchAgent(实体 KG)、SciMuse(58M 库 + 训练有趣度预测器)有大库 + 标注;
   Light 守**零本地知识库**,靠按需 lit-search 在线取数 + `semantic_sim`。自检分是启发式、无数据背书。
4. **激发算子是脚手架不是洞察(GIGO)**:`provocation_gen` 机械生成发散提问,洞察靠人/宿主 + 喂进的文献/数据质量。
   覆盖门只数角度分布,不判 idea 好坏。
5. **locator 可交接不等于证据内容为真**:`idea_genealogy.py` 能阻断私有路径/模板/未来日期/缺 hash 等假闭合，但不会替你判定
   该 DOI/URL/资源证明的科学含义是否成立；语义与创新性裁决仍归 idea-critique + 人。
6. **★可证伪 advisory 是启发式机检,非语义理解**:`card_gate` 的可证伪门只查"有无数字+比较符/指标/单位 + 量化失效条件"
   的**正则特征**,**不判该阈值是否合理/该实验是否真能证伪**(那需领域判断,归 idea-critique + 人)。可绕过(硬塞数字)、
   可漏报(纯文字但实质可证伪)——只当"顶会级可证伪预测"的最低机检底线 + warn 提醒,绝不阻断。
7. **单模型扮多视角(伪多样未根除)**:co-scientist/Perspectra/Council 用多 agent/选异质专家;Light 机检(覆盖 + dedup)
   只**缓解**伪多样塌缩,**不消除**——缺真异质多模型来源(同 idea-critique 诚实落后项)。
8. **跨会话历史 idea 防重未接**:lyndonkl `check-analogy-novelty` 对持久 catalog 防复用;Light `candidate_dedup` 只查
   **批内**变体对,跨会话"这个 idea 我上个月提过被毙"靠 memory-pm decision_log,本技能暂不直连(诚实 P2)。
9. **AI 评判随时间漂移**(2511.04964):自检分/撞车 sim 随检索覆盖与时点变;故撞车自查**带 HTTP 码 + 时点留痕**,
   不当一次定终身的真值。

---

## Sources（2026-06-26 在线一手核;star=`gh api repos/<r> --jq .stargazers_count` 当天值）

- 真·同类 ideation skill(star 当天核):[lingzhi227/agent-research-skills](https://github.com/lingzhi227/agent-research-skills)(`skills/idea-generation/`+`scripts/novelty_check.py`) · [wanshuiyin/ARIS](https://github.com/wanshuiyin/auto-claude-code-research-in-sleep)(`skills/idea-creator`+`novelty-check`+`patent-novelty-check`) · [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills)(`skills/scientific-brainstorming`+`hypothesis-generation`) · [Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar)(`skills/research-ideation/`) · [lyndonkl/claude](https://github.com/lyndonkl/claude)(`skills/brainstorm-diverge-converge`+`check-analogy-novelty`) · [imbad0202/academic-research-skills](https://github.com/imbad0202/academic-research-skills)(`deep-research/`) · [andrehuang/research-companion](https://github.com/andrehuang/research-companion)(`agents/brainstormer`+`idea-critic`) · [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) · [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates)(`simple-app-idea-generator`)
- 低 star 支撑:[itshussainsprojects/Claude-Council-Skill](https://github.com/itshussainsprojects/Claude-Council-Skill)(61★) · [ashrafkahoush-ux/claude-consciousness-skills](https://github.com/ashrafkahoush-ux/claude-consciousness-skills)(3★)
- 机制锚(论文/系统):Si et al [2409.04109](https://arxiv.org/abs/2409.04109) · AI-Scientist v1/v2 [2408.06292](https://arxiv.org/abs/2408.06292)/[2504.08066](https://arxiv.org/abs/2504.08066) · co-scientist [2502.18864](https://arxiv.org/abs/2502.18864) · ResearchAgent [2404.07738](https://arxiv.org/abs/2404.07738) · SciMuse [2405.17044](https://arxiv.org/abs/2405.17044) · Facet/Novelty [2409.14634](https://arxiv.org/abs/2409.14634)/[2506.22026](https://arxiv.org/html/2506.22026v1) · MAGenIdeas [2410.14255](https://arxiv.org/abs/2410.14255) · 漂移 [2511.04964](https://arxiv.org/abs/2511.04964)
- 目录/发现源:[ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) · `gh search repos` / `gh api .../git/trees/HEAD?recursive=1`(逐 repo 定位 ideation skill 路径)
