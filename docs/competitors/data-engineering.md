# competitors — light-data-engineering（科研主线 stage 2 · 数据可行性、获取、质量与泄漏）

> **Round 2 R1（2026-07-02）**：旧表 11 行全部是论文、库或标准，真同类 skill 近乎 0；审计所谓
> “data-engineering field 真空”是漏检，不成立。本轮按固定 commit 深读 **11 个真同类 skill**
> （数据发现、下载前审计、EDA、质量、数据集策展与 ML pipeline），与论文/工具/标准拆表。
> star 均为 2026-07-02 GitHub API 快照；大技能包 star 属整仓，已注明。
>
> **不动的已验证核心**：`split_leakage.py` 继续产泄漏 critical findings；
> `data_feasibility_gate.py` 继续产 idea-killing critical findings；二者由
> `run_checkpoint --stage 2` 聚合，数据不足走 **2⊣3**。Round 2 新增的是这两门之前的
> **“发现 → 下载前核许可/版本/大小/split → 抽样体检”**，不扩大 critical 面。

---

## 0.A 真·同类数据工程 / 数据集 SKILL（11 个）

> 判据：别人把数据发现、获取、画像、质量、策展或防泄漏做成可被 agent 调用的 SKILL/plugin；
> Deepchecks、GX、Croissant、论文与门户本身不占名额。相邻技能只借其覆盖的生命周期阶段，不伪称完全同构。

| # | 同类 skill（star 快照） | 已读机制与可复验点（固定 commit / 文件行） | 借进 Light | 诚实差距 |
|---|---|---|---|---|
| 1 | **wshobson/agents · data-quality-frameworks**（**37,421★**，整仓） | commit `5cc2549a50fc`；`SKILL.md:21-30` 把质量拆 completeness/uniqueness/validity/accuracy/consistency/timeliness，`:32-42` 给 schema→unit→integration testing pyramid，`:116-119` 任表失败就 fail pipeline，`:126-137` 强调 source-first、版本化 contract、freshness 与动态 baseline | 保留 `quality_gate` 的轻量 contract；R2 工作流把“下载后先 source-level 门、再变换”写死 | 它覆盖 dbt/GX 生产数仓，Light 面向科研数据；它没有数据可行性 2⊣3、泄漏 findings 或科研许可 intake |
| 2 | **K-Dense-AI/scientific-agent-skills · exploratory-data-analysis**（**29,862★**，整仓） | commit `1e024ea8547a`；`SKILL.md:14-21` 声称自动格式检测、质量、统计与下游建议，`:33-61` 按化学/组学/显微/光谱等格式分诊；`eda_analyzer.py:14+` 是真实扩展名→领域路由表 | 借“先分格式/模态再画像”，R2 明确 tabular 脚本不假装覆盖科学专有格式 | 它能认 200+ 格式，Light 现有 `data_doctor` 主要是 CSV；Light 强在 downstream critical 门与回边，不在格式广度 |
| 3 | **alirezarezvani/claude-skills · data-quality-auditor**（**19,631★**，整仓） | commit `1bd5b1a0b51c`；`SKILL.md:12-35` 分 full audit / targeted scan / monitoring 三模式，`:110-125` 给 DQS 五维权重，`:177-185` 给 Verified/Likely/Assumed 置信层且禁止自动修 Assumed；`data_profiler.py:62-75` 将空串/`N/A` 等 silent null 归缺失 | 借三模式入口与“声明置信度”；`dataset_intake` 只叫 metadata-ready/review，不说 usable | 它的固定 DQS 权重与 85/65 阈值未经任务校准，容易制造假精确；Light 不引入单一总分 |
| 4 | **ScienceClaw · ml-pipeline**（**856★**） | commit `7f5e65691672`；`SKILL.md:12-14` 明确 Data→Clean→Features→Split→Train；`:42-55` 先 split 再把 scaler 放 Pipeline；`:120-126` 要 stratify、nested CV、leakage 与 seed | 作为相邻下游印证先 split 再 fit；保留 `safe_split` 折内 refit 断言 | 它把 data→model 一条龙但无机读泄漏门，且本机 venv 路径写死（`:8`）；Light 将训练留给 experiment-coding |
| 5 | **MigoXLab/dingo · ClawHub skill**（**718★**） | commit `0b11be0ba98b`；`clawhub/SKILL.md:217-225` 有免 key rule evaluators（null/repeat/PII 等），`:242-270` 将 good/bad 与 metric detail 落 JSON，`:293-301` 要先写 config、先核字段、默认 rule-based；`:320-379` 另有 MCP 路径 | 借“免费规则优先 + 结构化 summary”；Light 继续零 MCP、规则输出接 canonical findings | Dingo 偏文本/RAG 数据质量，完整能力可依赖 key/MCP；Light 不搬其重运行时 |
| 6 | **oaustegard/claude-skills · exploring-data**（**127★**） | commit `b2fe13742b32`；`SKILL.md:25-45` 同时出 HTML 与 JSON，并要求 agent 读压缩 summary 而非整份巨 JSON；`:68-79` minimal 默认、显式请求才 full；`summarize_insights.py:10+` 真抽 overview/quality/correlation | 借“默认轻量抽样、需要时升级 full”与渐进披露；资源工作流先抽样而非整库下载 | 依赖 ydata + bash，Light 的 stdlib/pandas 路更轻；它不查许可、版本、split 泄漏 |
| 7 | **eddiebelaval/squire · dataset-curator**（**17★**） | commit `8c974b2c36fd`；`SKILL.md:31-58` 先 profile 再找 exact/near duplicate、mislabel、leakage、bias；`:60-76` 清洗后再次 validate；`:108-136` 要保留 provenance、测试 cleaning impact、按 group/time split；`:219-228` 列过度去重/误增广等坑 | 借“原始↔清洗映射 + 每次清洗后复验”；补进数据卡与 R2 闭环 | 主要是 prose/伪代码；`:145-148` cleanlab 示例用训练内概率，反而违反 out-of-sample 前提，Light 保留更严红线 |
| 8 | **Bhanunamikaze/AI-Dataset-Generator**（**15★**） | commit `b78e4c95f2fc`；`SKILL.md:91-103` 批次构建后持续写 coverage/drift，`:117-141` 强调 effective count、group minima、required provenance，不以 raw count 宣布完成，`:210-220` corpus audit 查 split disjointness/coverage/context leakage；`coverage.py:512+` 真算 provenance | 借“候选/记录的 provenance 必填 + split disjointness + coverage 不以总量冒充”；数据卡补 revision/hash/source locator | 它为 LLM SFT/DPO 数据设计且有 SQLite 大流水线；Light 不把它的生成数据逻辑搬进一般科研数据 |
| 9 | **NVIDIA/nurec-skills · physical-ai-datasets**（**14★**） | commit `1fba8e7a240d`；`SKILL.md:75-97` 每候选先列 size/format/license/gating/downstream，`:140-177` 给整库/子目录/sparse 三种下载，`:181-200` 133TB 数据必须先按平台过滤；`:291-321` 按任务选候选 | **R1 直接落地源**：新增 `dataset_intake.py`，下载前核 access/license/revision/size/split；R2 要“先 shortlist/过滤再下载” | 它是 NVIDIA 单域目录且需 HF token；Light 的 scout 只覆盖公开 HF 元数据，不能替代领域目录 |
| 10 | **taimo3810/kaggle-with-ai-template · kaggle-datasets**（**11★**） | commit `92e2f6783e8f`；`SKILL.md:15-33` 搜索支持 relevance/usability/downloads/格式/大小，`:35-81` 先看 info/column/file tree，`:83-120` 再按全量/单文件/版本下载，`:168-173` 下载后落 raw | 借“搜索→元数据→文件树→单文件抽样→整库”的节流顺序；资源地图诚实标 Kaggle 需登录/token | 它强依赖 Kaggle MCP，违反 Light 零 MCP；热度/usability 不等于科学适用性 |
| 11 | **sitammeur/ml-agent-skills · hugging-face-datasets**（**1★**） | commit `5e1c2538d4b0`；`SKILL.md:25-52` 覆盖 repo lifecycle/SQL/schema/sample/QA，`:68-88` 先 describe/sample/count，`:144-177` 过滤后可 push/export；`sql_manager.py:14-16` 真用 DuckDB `hf://` 直接查询 | 借“远端 describe/sample/filter，确认后才落地”；Light resource map 给 DuckDB/HF 的按需路径 | 它需要 HF token、DuckDB、datasets 且偏 Hub 管理；Light 只用公开 API 做 discovery，不上传 |

### R1 结论

data-engineering skill **并不稀疏**：高 star 大包里至少有质量 contract、科学 EDA、质量审计三个强同类，
中小技能又覆盖 dataset discovery/curation/lifecycle。旧审计把“库和论文是正确老师”说成“同类不存在”，低估了市场。

也不能反向过满宣称：上述技能大多只覆盖生命周期的一段。Light 的真组合差异不是“会 profile/会查 license”，而是：

1. 下载前的候选 intake 与来源快照；
2. 下载后的质量/泄漏/可行性门；
3. critical findings → checkpoint → **2⊣3** 回 idea 的科研 DAG。

### Round 3 五槽重新认证（2026-07-05）

原 Datalumina/Azure TDSP 模板不再占同功能槽。五个直接对象固定为：

1. `wshobson/agents:data-quality-frameworks`，37,530★，`5cc2549`，MIT；
2. `K-Dense-AI/scientific-agent-skills:exploratory-data-analysis`，30,185★，`26fd7a8`，MIT；
3. `alirezarezvani/claude-skills:data-quality-auditor`，20,250★，`1bd5b1a`，MIT；
4. `beita6969/ScienceClaw:ml-pipeline`，861★，`7f5e656`，MIT；
5. `MigoXLab/dingo:clawhub`，720★，`0b11be0`，Apache-2.0。

前三项满足千星采用度信号；后两项低于 1k，但分别覆盖 split-before-fit 科研流水线与免费 rule-based
数据质量落 JSON 的直接机制，相关性高于高星通用模板。无法找到更同功能且源码可核的千星替代时，诚实保留低星，
不拿项目模板凑数。旧报告中无 owner 的 “ScienceClaw” 已校正为可复验的 `beita6969/ScienceClaw`。

---

## 0.B 机制锚（不占 skill 名额）

| 机制锚 | 一手可核机制 | Light 取用 |
|---|---|---|
| **Kaufman 2012 / Kapoor & Narayanan 2023** | learn-predict separation；后者综述 17 领域 329 篇、8 类泄漏 | `safe_split` + `split_leakage` 的理论根；机检不到的非法特征/采样偏差继续人判 |
| **Deepchecks** | train/test samples mix、date/index leakage、feature-label correlation change | 泄漏 catalog 参照；不引入重依赖 |
| **Great Expectations / Frictionless / dbt tests** | 可版本化数据 contract、schema/row/cell 校验 | `quality_gate.py` 的轻量 YAML contract |
| **ydata-profiling / Dingo** | 画像与 rule-based 质量检查 | `data_doctor` 先轻量画像；不是 scientific-format 通吃 |
| **Cleanlab** | out-of-sample 预测概率定位疑似错标 | 只给候选、人裁定，不自动删；不把训练内概率当真 |
| **Datasheets / HF Dataset Cards / Croissant** | 动机、构成、采集、用途、偏差、许可与机器可读元数据 | 数据卡 + `croissant_export`；Round 2 补 revision/hash/source locator |
| **HF Hub API** | 官方开放端点可搜 dataset 元数据；公开搜索不要求 key，受全站 rate limit | `dataset_intake.py` 的唯一联网端点；失败报 UNAVAILABLE，不伪造 |
| **OpenML** | 按规模/类型/格式细筛，稳定 dataset id/version，可下载 Croissant | R2 免费主力；用前仍核版本/许可/质量 |
| **Kaggle** | 搜索、metadata、file tree、单文件/版本下载 | 登录/token 级资源，不作为完成依赖 |
| **Papers with Code archive** | 原站已于 2025-07-24 停止服务；现有备份是历史快照 | **只作历史 benchmark 线索，不作 live 数据源**；回论文/官方数据主页核 |

---

## 0.C 横向机制提炼（直接驱动 Round 2）

### ① 真实工作从“数据需求卡”开始，不从下载开始

NVIDIA 与 Kaggle skills 都先按任务、大小、格式、许可和 gating 选候选；AI-Dataset-Generator 又要求
coverage/provenance。Light 因此先冻结：研究任务、target、观察单位、时间点、group、最小规模、所需字段、
允许许可、磁盘/带宽预算。缺这些时，downloads 再高也不能进 shortlist。

### ② 下载前必须做 resource preflight

候选至少要有 source URL、provider id、revision/version、last checked、license locator、access/gating、
size、splits、collection/provenance。`dataset_intake.py` 把公开 HF 元数据归一为
`light.data_candidates.v1`；缺项标 `review`，**不产 critical、不替用户选**。

### ③ 先看 card/schema/sample，再拉全量

同类共识是 describe/sample/full 三级。Light 的闭环：候选卡 → 官方卡/文件树 → 小样本 → `data_doctor`
→ 许可与质量仍可接受才整库下载；大数据优先 streaming/range/subset/sparse。这样不会为了一个不合适的
133TB 数据集先付出下载成本。

### ④ “质量”不能压成一个漂亮总分

alirez skill 的 DQS 提供沟通便利，但固定权重会制造假精确。Light 保留分项证据：
completeness/duplicates/type/label balance/leakage/representativeness 分开报；只有可机检红线进 critical，
其余 advisory + 人判。

### ⑤ 清洗必须保留 lineage，且清洗后重过门

squire 与 AI-Dataset-Generator 都强调 provenance、版本、effective coverage。Light 要记录 raw hash、
cleaned hash、变换脚本/commit、移除行映射、split seed/group/time；清洗后重新跑 quality/leakage，
不能只看“行数变少了”宣布更干净。

### ⑥ Light 的诚实超越点

- 同类已会 EDA、质量 contract、dataset card、发现/下载；这些不是独创。
- Light 的真增量是把 **download preflight × leakage critical × feasibility critical × 2⊣3 回边**
  捏成科研闭环。
- `dataset_intake` 只是 advisory；真正“可用”必须经过样本/许可人核、`data_doctor`、
  `split_leakage`、`data_feasibility_gate` 与 checkpoint。

---

## 1. Round 2 落地

1. 新增 `scripts/dataset_intake.py`：公开 HF API 搜索/详情 → `light.data_candidates.v1`；
   核 access/license/revision/size/split/card，缺项 `review`，API 失败 exit 2 + `UNAVAILABLE`。
2. 新增 `references/data-resource-map.md`：数据需求卡 → 多源发现 → 下载前审计 → 抽样体检 →
   获取/lineage → 泄漏/可行性/checkpoint → 数据卡/发布；资源按免 key、登录、付费分级。
3. 数据卡补 source snapshot、license locator、gating、下载 hash/bytes、候选取舍与 raw→clean lineage。
4. 保持 `split_leakage`、`data_feasibility_gate`、`safe_split` 与 2⊣3 核心零改。

## 1.1 Round 3 复审增量

复核发现下载前 intake 仍有名实缝隙：文档说“来源快照”，但报告没有保存 API 原始响应 hash；`metadata-ready`
也没有显式区分 tag-only license、缺 file tree/lastModified、非 40 位 HF revision 或医疗/隐私/人类等敏感标签。
本轮将 `raw_response_sha256`、`candidate_manifest_sha256`、`license_source/license_locator`、敏感信号与
file tree/last_modified/revision format review 写入 `dataset_intake.py`。这仍是 warn-only/advisory，不把缺项扩大成
critical；真正阻断仍由 `data_identity_fitness`、`split_leakage` 与 `data_feasibility_gate` 承担。

---

## 2. 诚实边界

- `dataset_intake` 当前只自动接 **Hugging Face 公共元数据**；OpenML/UCI/Zenodo/Kaggle 走资源地图与
  harness 联网，不伪称统一搜索。
- `metadata-ready` 只表示下载前字段较齐；不表示数据质量、任务匹配、无隐私风险、无泄漏或许可结论。
- license/card 是上传者声明，必须回官方条款/原始发布者核；unknown 绝不推定允许。
- HF API 有 rate limit，网络/结构变化时 exit 2 + UNAVAILABLE；技能不得用缓存结果冒充当天真值。
- `data_doctor` 主要覆盖表格 CSV；科学专有格式、图像/组学/时序需领域工具与 file-reading 分诊。
- 经验样本量阈值不是 formal power analysis；四问输入可能 GIGO。
- 泄漏检测仍是签名启发式，测试集非目标分布、非法特征、采样偏差与复杂 lineage 多需人工。
- 隐私、伦理、许可的最终判断归数据 owner / IRB / research-ethics，不由脚本代签。

> **SSOT**：本文件是 data-engineering 的 R1 对标真相源；实时资源与执行闭环见
> `skills/light-data-engineering/references/data-resource-map.md`，工具 API 细节见既有 `references.md`，
> 三者互补不重复。star、API 与资源可达性会变化，引用前当天复核。
