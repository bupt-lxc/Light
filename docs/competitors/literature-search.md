# competitors — light-literature-search（科研主线 stage 1 · 文献调研 → 领域地图）

> 铁律 1+2 对标笔记:动手前深读最强同类,**机制上网核实(star=[snapshot 2026-06-26, src=GitHub repo 页一手核]),非凭记忆**,落地可借机制 +
> 标清超越点与诚实边界。本技能是**科研主线 DAG 第 1 节点(非横切常驻)**:在线多源检索 → 产**"领域地图"
> (研究脉络 + 方法谱系 + 未解问题地图),不是论文列表**;下游喂 idea-generation⇄idea-critique。**接 `_shared`**
> ——产 `light.findings.v1` 的是**信号/预警型 findings(撞车预警 + 覆盖度,warn 为主)**,critical 撞车判决归
> idea-critique(stage 4)。port 自 v1 `light-literature-search`(10 脚本 + references API 真相源,byte-copy 再 Edit)。
>
> 写作:批 1 第一技能(2026-06-17);**Round 2 R1 重做(2026-06-26)**——治"高 star 同类 skill 漏检"系统病。作者 Light0305 + Claude。

---

## ⚠ Round 2 R1 系统病诚实校正（先认错,再对标）

批 1 旧版本 §0 把 17 行**混排成"数据源 + SaaS 工具 + 论文"**,真·同类 **Claude/agent skill 只有 2-3 个**(borghei 307★ / lingzhi227 162★ + K-Dense 一句带过)。这正中审计点名的系统病:**高 star 同类 skill 漏检**。Round 2 一手核 GitHub 后实情 = **文献调研是 Claude skill 生态最拥挤的赛道之一**,≥10 个**千 star 级**真同类各自完整:

- **imbad0202/academic-research-skills 34,628★** / **K-Dense scientific-agent-skills 29,381★** / **davila7/claude-code-templates 28,307★** / **alirezarezvani/claude-skills 19,112★** / **wanshuiyin/ARIS 12,659★** / **Galaxy-Dawn/claude-scholar 4,415★** / **Weizhena/Deep-Research-skills 1,335★** ……

**结论:旧版"litreview 同类稀疏"的隐含判断 = 漏检,推翻**(同 figure scipilot / frontend ui-ux-pro-max 实证的同一系统病)。**诚实重述超越点**(防做偏):PRISMA/PICO、多源去重、引用核真、覆盖度诚实、novelty-as-downstream——**全是同类强共识,Light 一个都不是"唯一想到"**;Light 的真增量 = **机读 findings 接线 + `_shared` 复用 + 三层确定性分层 + 离线降级 + 跨 harness**(见 §0.C / §2)。**新落地(R1→脚本):借 imbad0202 的分布偏斜预警**(详 §0.C ④)。

---

## 0.A 真·同类文献调研 SKILL（13 个真同类 · R1 硬指标 · star=[snapshot 2026-06-26, src=GitHub repo 页一手核]）

> 判据:每条**已读其 SKILL.md/脚本/agent**(带可复验点:文件名/常量/行为),非列名字。优先千 star。

| # | 同类 skill（star） | 它怎么做（已读 SKILL/脚本,带可复验点） | 我借进哪个能力 | 我诚实差在哪 |
|---|---|---|---|---|
| 1 | **imbad0202/academic-research-skills**（**34,628★**,`deep-research/SKILL.md` v2.11.0） | **13-agent 编队** + **8 模式**(full/quick/paper-review/lit-review/fact-check/**3W(WHY-HOW-WHAT)文献扫**/Socratic 引导/systematic+meta);agents 含 `source_verification_agent`/`risk_of_bias_agent`/`devils_advocate_agent`/`bibliography_agent`;**`DISTRIBUTIONAL_SKEW_ADVISORY`**——对检出语料按**时间/方法/地域集中度**出 warn-only 预警 + **具体补救检索式**(读 `examples/idea_diversity_coverage_gap_advisory.md`:time 92%/method 87.5%/geo 90% 三维实例) | **R1 新落地**:借其分布偏斜预警思路 → `domain_map.py` 加**年代集中度**advisory(warn-only,产进 findings,见 §0.C ④);Socratic 决策点对齐我的 ASK 决策点 | 它是 **LLM-agent 散文式**多 agent;无机读 findings/`_shared` 跨技能交接;其 13 agent 跨我整条 DAG(我只 stage 1) |
| 2 | **K-Dense-AI/scientific-agent-skills**（**29,381★**,`skills/literature-review/SKILL.md` v1.2,MIT） | PICO 框架 + **强制 PRISMA + 强制 1-2 张 AI schematic**;`search_databases.py`(PubMed/arXiv/bioRxiv/S2 聚合) + `verify_citations.py`;thematic synthesis;输出 md+PDF 多引用风格(APA/Nature/Vancouver) | PICO/PRISMA 思路印证我的 `prisma_flow.py`;thematic synthesis → 我的方法谱系三件套 | **可复验差距**:其 `search_databases.py` 实读=**纯 `format_search_results` 聚合+格式化**(无逐层排序/无相关度过滤/无近三年vs经典分离)——**我三层分别排序 + require-terms 过滤确定性更强**(诚实"我强"点);它依赖 `parallel-cli`(付费)+ OPENROUTER_API_KEY |
| 3 | **davila7/claude-code-templates**（**28,307★**,`components/agents/deep-research-team/`） | **deep-research-team agent 编队**:`academic-researcher`+`query-clarifier`+`fact-checker`+`report-generator`+`nia-oracle`+`competitive-intelligence-analyst`;query-clarifier 先澄清再检索 | query-clarifier 先澄清 → 对齐我 ASK「检索范围/深度」决策点;fact-checker → 我 `verify_citations.py` | 是通用 deep-research 编队(非科研专精);无三层时间分层、无 findings 机读交接 |
| 4 | **wanshuiyin/ARIS（Auto-Research-In-Sleep）**（**12,659★**,`skills/idea-discovery/SKILL.md`） | **自动管线** `/research-lit→/idea-creator→/novelty-check→/research-review→/research-refine`;**跨模型 novelty 验证**(`REVIEWER_MODEL=gpt-5.5` 经 Codex MCP);**`AUTO_PROCEED` checkpoint**(用户不应答则自动取最优);多源(Zotero+Obsidian+本地 PDF+arXiv/Scholar) | **lit→idea 管线**印证我 stage1→idea 接线;其 checkpoint=我 ASK 决策点(但我**绝不 AUTO_PROCEED 自动选/投**) | 其 novelty=**跨模型**(gpt-5.5),我=facet+`semantic_sim`(离线档弱,见 §3);它要 Codex MCP / OpenAI key(违我硬约束) |
| 5 | **alirezarezvani/claude-skills**（**19,112★**,337 skills 含 research 类） | 跨 8+ harness(Claude/Codex/Gemini/Cursor) 的超大技能包,含 research/literature 类;30+ agents/70+ commands/330+ skills | 跨 harness 兼容印证我「跨 harness」定位 | 广而非深;文献检索是其一个抽屉,无在线免 key 取数/三层/findings |
| 6 | **Galaxy-Dawn/claude-scholar**（**4,415★**,`agents/literature-reviewer.md`+`agents/paper-miner.md`+`commands/kb-literature-review.md`) | 半自动全流程研究助理(ideation→coding→exp→writing→publication);**`paper-miner` agent** 从论文挖**venue 专属写作信号**入持久写作记忆;跨 Claude/Codex/Kimi/OpenCode | paper-miner 的"挖结构信号入记忆"→ 对齐 memory-pm 横切;`kb-literature-review` 印证地图式而非列表 | 偏写作知识挖掘(喂 paper-writing),非检索召回引擎;无三层排序/覆盖度门 |
| 7 | **Weizhena/Deep-Research-skills**（**1,335★**,结构化 deep research,human-in-the-loop) | 结构化 deep research + **human-in-the-loop 控制**(每阶段停下让人确认),跨 Claude Code/OpenCode/Codex | human-in-the-loop = 我 ASK 决策点的强佐证(检索深度/方向窄/撞车都该停下问) | 通用 deep research(非学术专精);无免 key 学术源编排、无 findings |
| 8 | **borghei/Claude-Skills litreview**（**307★**,`research/litreview/SKILL.md`) | PRISMA/PICO;**6 维 source-quality scorer**(方法/样本/同评/可复现/时效/被引);thematic synthesis 出簇+证据强度+gap | 6 维质量分 + thematic synthesis 出 gap → 领域地图未解问题层 | **它零在线数据源**(假设人工/机构库)——**我做实在线免 key 取数 = 我的边** |
| 9 | **Aperivue/medsci-skills**（**167★**,医学科研,MIT,医师作者真刊实测) | 医学科研专精:文献检索 + 报告规范(CONSORT/PRISMA) + 统计 + 出版图;**"tested on real publications"** | 真刊实测纪律 = 我活体 E2E 的同道;报告规范指针 | 医学垂域(我领域无关);其检索深度不及我三层,但**真刊实测**值得学(我 E2E 照做) |
| 10 | **lingzhi227/agent-research-skills**（**162★**,31 skills,从 17 个 LLM-agent-research repo 萃取) | 6 阶段 frontier→survey→deep-dive→code→synthesis→report;S2/arXiv/OpenAlex/Crossref;**novelty-assessment 单列为独立 skill**;多视角 persona | 阶段化骨架(前沿映射→综述→深读);印证"撞车/新颖性是我**喂**的下游关切" | 无机读 findings/`_shared` 交接;我**产 light.findings.v1 跨技能机读交接 = 我的边** |
| 11 | **ykdojo/paper-search**（**33★**,Claude Code plugin) | OpenAlex 250M works 免 key;关键词检索 + DOI 查 + 按被引/日期排序 + 分页 | 印证 OpenAlex 免 key 主源选型正确 | 只做单源检索/分页;无三层、无地图合成、无覆盖度门、无 findings |
| 12 | **yy/claude-scholar**（**28★**,Claude Code 学术工具集) | 文献检索 + 引用管理 + LaTeX 检查 + 数学验证 + 投稿准备一条龙 | 全流程定位印证 Light 多技能编排思路 | 检索仅其一环;无三层分层/findings;偏个人工具集非编排契约 |
| 13 | **shiquda/openalex-skill**（**2★**,OpenAlex CLI) | human-friendly OpenAlex CLI:检索/被引/agent workflow | 印证 OpenAlex CLI 化可行 | 单源工具;无多源去重/三层/地图/findings |

> 另:**findalexli/ai-scientist-v3**(17★,`.claude/skills/search-papers/SKILL.md`)、**ultimatile/arxiv-skills**(34★)、**shandley/research30**(0★,30 天多源 OpenAlex/S2/PubMed/arXiv/HF=tracker 同类)——同类但机制重叠,不再单列,合并入 §0.C 提炼。

### Round 3 五槽重新认证（2026-07-05）

原 21×5 清单中的 Papers We Love / Google Research 是资源集合，不再占“同功能 skill”名额。当前五槽改为：

| 对象 | 当前采用度与固定版本 | 本轮复核 |
|---|---|---|
| `imbad0202/academic-research-skills` · `deep-research` | 36,288★；`f86d68a` | 亲读 548 行 SKILL；13-agent、source verification、RoB、三次 DA checkpoint 与跨 session passport 都有明确契约，但仍跨越 Light 多阶段 |
| `K-Dense-AI/scientific-agent-skills` · `literature-review` | 30,185★；`26fd7a8`；MIT | 亲读 710 行 SKILL 与 search/verify 路径；PICO/PRISMA/多库/citation verify 可借；强制 AI schematic 与 Light 永久底线冲突，不迁移 |
| `wanshuiyin/Auto-claude-code-research-in-sleep` · `research-lit` | 12,999★；`7421d2e`；MIT | 旧称 `wanshuiyin/ARIS` 已失效；当前 owner/repo、research-lit skill 与多源 D2/fallback 路径已重新定位 |
| `Galaxy-Dawn/claude-scholar` · `literature-reviewer` | 4,498★；`2f7766f`；MIT | 亲读 agent；scope clarification、Zotero 去重、abstract-only guard、full-text fallback 与 batch checkpoint 可借，但默认依赖 MCP/Zotero |
| `Weizhena/Deep-Research-skills` · `research` | 1,502★；`e5479f8`；MIT | 亲读 Codex skill/validator；对象框架、时间范围、字段、并行批量逐项问用户。Light 据此把 scope decision 下沉为协议硬门 |

采用度来自 2026-07-05 GitHub API，只作生态信号。五项均读到直接 skill/agent/脚本切片；不把父仓 star 冒充单 skill star。

---

## 0.B 机制锚（数据源 / SaaS 检索引擎 / 论文 / 规范 —— 不占 skill 名额,仍是有价值的机制/学术锚源）

> 这些是**取数端点 / 商业产品 / 学术方法**,非"同类 skill";批 1 旧版把它们误塞进 skill 表是漏检的另一面。逐条 2026-06 一手核(端点真相源见 `references.md`)。

| 锚 | 类型 | 机制 | 我借/我边界 |
|---|---|---|---|
| **OpenAlex**(2.5 亿+ works) | 数据源(免 key) | `search`/`filter`/`group_by`/`cursor`;`referenced_works`+`cited_by_count`;倒排摘要 | `search_normalize.py` 主源 + `group_by` 年度脉络 + `referenced_works` 算文献耦合;官方 2026 起称需免费 key——**不硬依赖** |
| **Crossref**(DOI 注册局) | 数据源(免 key) | `query.bibliographic`/`cursor`;`is-referenced-by-count`(低估);`reference[]` | DOI 去重真相源 + 中文刊按 ISSN 检 |
| **arXiv API** | 数据源(免 key) | Atom feed,布尔检索;`sortBy=submittedDate`;间隔≥3s | 第 1 层"近三年前沿"主力(**须 https**,http 今天 301) |
| **Europe PMC**(EMBL-EBI) | 数据源(**完全免 key**) | `query`+`cursorMark`;直接返 `abstractText`+`citedByCount`+`/citations`·`/references` | `biomedical_search.py` 生医免 key 主力 + 滚雪球端点 |
| **Semantic Scholar/S2AG** | 数据源 | SPECTER2 768 维嵌入;`influentialCitationCount`;`tldr` | `snowball.py` 引用滚雪球;嵌入档可注入 `_shared/semantic_sim`;匿名限速严(429) |
| **DOAJ** | 数据源 | 开放获取相关度排序 | 补盲;**今天 403**(疑 WAF)——降级,不假设可用 |
| **undermind.ai** | SaaS agent 检索 | 多轮迭代 + GPT-4 triage;**统计模型估"该主题总相关文数"** 给"没漏"信心(命中递减→召回估计) | 借召回估计思路标 coverage caveat;不做 3-5 分钟逐篇 triage |
| **PaperQA2**(FutureHouse) | SaaS/开源 RAG | 三阶段 agentic RAG:解析→嵌入→agent 取证→带引用合成;引用图遍历;LitQA2 超人类 | 引用图遍历→`snowball.py`;**全文 RAG 需 PDF**,我守合规只取元数据/摘要 |
| **OpenScholar**(Ai2,Nature) | 学术系统 | RAG over 4500 万 OA;自反馈迭代;实测 **GPT-4o 幻觉引用 78-90%** | 防幻觉纪律→`verify_citations.py`;无自有 8B+4500 万库 |
| **STORM**(Stanford OVAL) | 学术系统 | **多视角提问**:发现多视角→模拟"写手↔专家"对话→curate 大纲 | 领域地图多视角结构化(脉络/谱系/gap 三视角) |
| **Elicit** | SaaS | PRISMA 可审计筛选:每准则打分+排除理由+支撑引文;Cochrane 召回 95%+ | `prisma_flow.py` 计数勾稽 + screen/extract 协议;它读全文表,我到摘要级 |
| **Connected Papers / ResearchRabbit** | SaaS | 力导向图;**共被引 + 文献耦合**聚相关(不靠直接引用) | 文献耦合从 OpenAlex `referenced_works` **零额外 API** 算;我出结构化簇表非交互图 |
| **scite.ai** | SaaS | 深度学习把 12 亿+ 引用句分 **supporting/contrasting/mentioning** | 概念借 contrasting→争议/伪热点识别;**硬边界**:无全文+专有分类器,我只 count-based+提请人工 |
| **Consensus** | SaaS | claim 级证据方向聚合(support/oppose/mixed) | 借"已成定论 vs 争议"作地图信号;不做 claim 共识表 |
| **Idea Novelty Checker / OpenNovelty**(arXiv 2506.22026 / 2601.01576) | 论文 | **facet 分解**(application-domain/purpose/mechanism/evaluation);检索→SPECTER2 top-100→RankGPT facet 重排→**≥1 核心 facet 不同即 novel** | **撞车 findings producer**:`semantic_sim` 找最像前作 + facet 槽位 delta;**novel 判决不自做**(归 idea-critique) |

---

## 0.C 读完 13 个真同类后的横向机制提炼（直接驱动 Round 2 加厚）

1. **PRISMA/PICO 是同类底线共识,不是卖点**:K-Dense/borghei/Aperivue/imbad0202 全做 PRISMA,Elicit 做可审计 PICO 筛选。Light 的 `prisma_flow.py` 是**对齐底线**,诚实不吹"独创"。
2. **"建地图而非列表"是头部共识**(STORM 多视角 / borghei thematic synthesis / Galaxy-Dawn kb-review),非 Light 独想。Light 增量 = **三层分别检索分别排序的确定性脚本**(`domain_map.py`)——K-Dense `search_databases.py` 实读=纯聚合格式化,**这一层我确定性更强**(可复验"我强"点)。
3. **覆盖度诚实 = 同类普遍弱项,但 imbad0202 走得比我远**:多数同类(K-Dense/borghei)不标覆盖缺口;Light 的 HTTP 码覆盖门(标哪些**源**可达)已领先大多数,**但 imbad0202 的 `DISTRIBUTIONAL_SKEW_ADVISORY` 更进一步**——对**检出语料本身**按时间/方法/地域集中度预警 + 给补救检索式。**这是 Light 缺的真机制**(诚实"它强"点)→ §0.C ④ 落地。
4. **【R1 新落地】年代分布偏斜 advisory**:借 imbad0202,`domain_map.py` 对检出集**年代集中度**出 warn-only advisory(如"近三年占比 92% → 经典奠基可能不足,建议加 backward 滚雪球";或"全部 ≥8 年 → 可能已饱和/方向冷,建议 cross_domain")。产进 `light.findings.v1`(warn,**绝不 critical**,绝不替用户判)。**只做年代轴**(方法/地域轴需全文元数据,免 key 摘要级拿不全,诚实不做——见 §3)。
5. **novelty/撞车是下游关切,同类都把它单列**(lingzhi227 独立 novelty skill / ARIS `/novelty-check` 跨模型 / Idea Novelty Checker facet)。印证 Light **只产撞车信号、judge 归 idea-critique** 的接线正确;Light 的 facet+`semantic_sim` 离线档弱于 ARIS 跨模型/SPECTER2,**诚实标边界**(§3.2)。
6. **决策点(human-in-the-loop)是同类强共识**:davila7 query-clarifier 先澄清、Weizhena 每阶段停、ARIS checkpoint。印证 Light 五个 ASK 决策点设计正确;**但 Light 绝不学 ARIS `AUTO_PROCEED` 自动取最优**(撞车/选向是用户的,不替决)。
7. **机读 findings 跨技能交接 = Light 全市场独有点**:13 个同类**无一**产编排器可读的机读 findings(全是散文/PDF/md)。`light.findings.v1` 被总控 `run_checkpoint --stage` 聚合 = Light 的接线面,这是真差异化(非吹)。

---

## 1. 横切可借机制（已设计进 v2 脚本/能力；★=Round 2 R1 新增/强化）

1. **三层分别检索分别排序(本技能灵魂,蓝图 §6)**:近三年前沿(arXiv+OpenAlex recency-boost)+ 经典奠基(领域内被引降序,蹭词豁免)
   + 跨领域方法移植(`cross_domain_search` 应用轴×方法轴正交,**不拼词**)。借 undermind 多轮迭代把三层各自检索→滚雪球→再补。**不是一锅 relevance。**
2. **领域地图 = 多视角结构化合成(STORM)+ 主题聚类出 gap(borghei/Consensus)**:产**研究脉络 / 方法谱系 / 未解问题地图**三件套结构化槽位,由宿主 LLM 按槽位填,可直接喂 idea。
3. **方法谱系 = 引用网络聚类(Connected Papers/ResearchRabbit)**:文献耦合(共享参考,OpenAlex `referenced_works` 零额外 API)+ 共被引 + 语义相似多信号聚"学派",`snowball.py` 前后向滚雪球建脉络。
4. **撞车/新颖性 = facet 分解 + 语义相似(Idea Novelty Checker / ARIS / lingzhi227)**:用户给 idea 时检索候选→`semantic_sim` 找**最像的那一篇** + 沿 purpose/mechanism/evaluation/application-domain 四 facet 标重合与 delta → 产 `light.findings.v1`(warn 信号)喂 idea-critique。**只给信号+facet,不下 novel 判决。**
5. **覆盖度诚实门(undermind recall + Elicit PRISMA + ★imbad0202 分布偏斜)**:产出标 `covered: ...`、未覆盖源、查不到 DOI/被引写 `unknown`,按命中递减给召回 caveat;**★Round 2 新增:对检出集年代集中度出 warn-only advisory**(借 imbad0202 `DISTRIBUTIONAL_SKEW_ADVISORY`,只做年代轴)。→ light.findings.v1。
6. **防幻觉引用(OpenScholar 78-90% + scite)**:`verify_citations.py` DOI 内容协商核真实存在/标题年份匹配,四态——检索期轻量自检,投稿终审交 light-citation。
7. **机读交接(本技能 vs 13 个同类的独有点)**:撞车信号 + 覆盖度产 `light.findings.v1`,被总控 `run_checkpoint --stage` 聚合 → 喂 idea(3⇄4)阶段门。**13 个同类无一产编排器可读的机读 findings。**

---

## 2. 超越点（v2 相对裸模型 / v1 / 商业同类 / 13 个真同类的真增量,Round 2 诚实重述）

- **裸模型本就会**"上网搜论文 + 总结成综述"——**不吹成卖点**。本技能价值=① **三层分别排序**的确定性编排(裸模型一锅 relevance,老论文淹没新方向);
  ② 产**机读撞车/覆盖度 findings**被下游门消费(裸模型给散文,编排器读不了);③ **诚实标覆盖度/召回 caveat**(裸模型假装查全);
  ④ **免 key + 离线降级 + 跨 harness**(裸模型靠宿主联网随缘)。
- **相对 13 个真同类**(Round 2 诚实定位):PRISMA/PICO/多源去重/引用核真/建地图/novelty-as-downstream 是**全行业共识**,Light **不独占任一**。
  Light 的真差异 = **(a) 机读 findings 跨技能交接(13 同类零覆盖) + (b) 三层分别排序的确定性(K-Dense 实读仅聚合格式化) + (c) 全程零 key/零 MCP/零付费**
  (K-Dense 要 parallel-cli 付费 + OPENROUTER key、ARIS 要 Codex MCP/OpenAI key) **+ (d) 离线降级可验证**。
- **相对 v1 的真增量**:① 把 v1 散件(recency-boost/经典豁免/cross_domain)**组装成三层领域地图编排器**(v1 有零件无总装);
  ② **领域地图三件套结构化合成**(v1 模板是"待人工填"占位);③ **findings 接线** + 接 `_shared` 规范 bootstrap(治 v1 `search_normalize.py` 硬编码脆);
  ④ references.md 按实测更新;**★Round 2:年代分布偏斜 advisory(借 imbad0202)**。
- **Round 3 复审增量**:旧 `search_protocol_gate.py` 已有 query ledger、known-item recall、included-seed
  snowball、计数勾稽和 no-exhaustive 门，但 `raw_sha256` 可以没有 raw artifact locator，停止规则可以只有 prose basis，
  日期没有 `as_of` 非未来检查，source family 也可被大小写/空格伪装成多来源。现已补为受控 source family、
  `raw_locator+raw_sha256`、`observed_locator+observed_sha256` 与 `--as-of` 日期门；这不证明检索穷尽，只证明协议证据
  不是空心哈希/未来日期/来源伪独立。

---

## 3. 诚实边界（已知做不到 —— 写进 SKILL 名实对齐,绝不掩饰）

1. **无全文 RAG / 深度阅读**:PaperQA2/OpenScholar/K-Dense 读全文,本技能守合规**只取元数据/摘要/链接、不下载付费墙全文**;单篇深读靠宿主多模态 + 仅 OA 版(走 light-citation Unpaywall 口径)。
2. **撞车信号 ≠ 新颖性判决**:只给"最像前作 + facet 重合/delta",**novel 归 idea-critique**;`semantic_sim` 离线档对**无共词纯同义/跨语言**(中文 idea↔英文标题)做不好(实测中文 sim≈0.1/英文≈0.23),弱于 ARIS 跨模型(gpt-5.5)/SPECTER2,须注入嵌入档(同 `_shared` 边界)。
3. **无引用情感分类(scite 级)**:supporting/contrasting/mentioning 需全文引用上下文 + 专有分类器——本技能**无此代码**,只 count-based 启发式 + 提请 scite/人工。
4. **分布偏斜 advisory 只做年代轴**:imbad0202 做时间/方法/地域三维,**Light 只做年代轴**——方法/地域分布需全文元数据,免 key 摘要级拿不全(OpenAlex topics 不等于方法学/地域),诚实不做,不假装三维。
5. **覆盖度是估计非保证**:免 key 接口配额/覆盖限,**不保证召全**;**DOAJ 今天 403**(降级);中文库(CNKI/万方/维普/CSCD)无免费 API、被引订阅墙。
6. **被引数跨库不可比**:OpenAlex/Crossref/S2/Europe PMC 口径各异,入表标来源库、不直接比。
7. **无交互式图谱可视化**:Connected Papers/ResearchRabbit 出力导向交互图;本技能出**结构化簇表/文本**(可入库、可喂下游),非交互可视化。

---

## Sources（2026-06-26 在线一手核;star=GitHub API stargazers_count 当天值）

- 真·同类 skill(star 当天核):[imbad0202/academic-research-skills](https://github.com/imbad0202/academic-research-skills)(`deep-research/SKILL.md`+`examples/idea_diversity_coverage_gap_advisory.md`) · [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills)(`skills/literature-review/`) · [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates)(`components/agents/deep-research-team/`) · [wanshuiyin/ARIS](https://github.com/wanshuiyin/auto-claude-code-research-in-sleep)(`skills/idea-discovery/SKILL.md`) · [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) · [Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar) · [Weizhena/Deep-Research-skills](https://github.com/Weizhena/Deep-Research-skills) · [borghei/Claude-Skills](https://github.com/borghei/Claude-Skills) · [Aperivue/medsci-skills](https://github.com/Aperivue/medsci-skills) · [lingzhi227/agent-research-skills](https://github.com/lingzhi227/agent-research-skills) · [ykdojo/paper-search](https://github.com/ykdojo/paper-search) · [yy/claude-scholar](https://github.com/yy/claude-scholar) · [shiquda/openalex-skill](https://github.com/shiquda/openalex-skill)
- 目录/技能包(发现源):[ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills)(65,996★) · [travisvn/awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills) · [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit)
- 机制锚:undermind.ai [Aaron Tay 2024-04](http://musingsaboutlibrarianship.blogspot.com/2024/04/undermindai-different-type-of-ai-agent.html) · PaperQA2 [FutureHouse](https://github.com/future-house/paper-qa) · OpenScholar [arXiv 2411.14199](https://arxiv.org/abs/2411.14199) · STORM [arXiv 2402.14207](https://arxiv.org/pdf/2402.14207) · Elicit [systematic-review](https://elicit.com/solutions/systematic-review) · Connected Papers [LMU LibGuide](https://libguides.lmu.edu/AIresearchtools/CP) · scite vs Consensus [paperguide](https://paperguide.ai/blog/consensus-vs-scite/) · 撞车 facet 法 [arXiv 2506.22026](https://arxiv.org/html/2506.22026v1) · [OpenNovelty 2601.01576](https://arxiv.org/pdf/2601.01576)
- 数据源端点真相源:port 自 v1 `references.md`(OpenAlex/Crossref/arXiv/S2/Europe PMC/DOAJ/bioRxiv,2026-06 逐条 curl 核;arXiv 须 https、DOAJ 403、OpenAlex 匿名+mailto 仍 200)
