# venue-matching Round 2 对标证据

核查日：2026-07-03（Asia/Shanghai）。star 是当天 GitHub repository
star；commit 固定到核查时 HEAD。行号均指该固定 commit。技能、数据/API、
商业指标/风险服务、publisher finder/CFP、论文/评测数据严格分表，后四类不顶
“真同类 skill”名额。

## 0. 旧结论复核

Round 1 的“同类 skill field 近乎空，分层推荐、风险信号、决策点独特”不成立：

- `zero565656/journal-recommender` 已有 challenge/target/safety（SKILL
  16–21）、检索前用户 preference checkpoint（60–72）、scope/type/APC/risk
  多维评分（`references/scoring-rubric.md` 32–66）和带来源的转投顺序模板
  （`references/output-templates.md` 64–121）。
- `Aperivue/medsci-skills/find-journal` 已把 scope fit 与 manuscript
  acceptance-readiness 分轴（SKILL 158–202），输出 reject-fallback cascade
  （351–370）并在作者选择后落 submission 目录（443–458）。
- `aipoch` 的多个 skill 已实现 topic/method/evidence/article-type 分层和
  PubMed venue-frequency discovery；`queelius/papermill` 已有 stateful
  ranked shortlist + submission strategy。

所以 scope matching、venue ranking、APC/deadline filtering、predatory
warning、author/paper fit、解释性推荐、冲稳保和决策暂停都不是 Light 独有。
Round 2 只主张一个更窄组合差异：**消费真实 stage-11
PDF/hash/pages/profile/compliance + 逐字段 source/access/status + unavailable
不归罪 + canonical `chosen=null` 到 user-selection handoff 的可执行转移**。

## 1. 真同类 skill（10 个，9 repo）

| # | skill / repo（2026-07-03 star；固定 commit） | 真读文件/行与配套资源 | 具体机制 | 借入 Light | 仍有差距/风险 |
|---:|---|---|---|---|---|
| 1 | `journal-recommender` · `zero565656/journal-recommender`（37★；`407aff106677aac090bf2d177155db15e3593126`） | `SKILL.md:10-29,31-110`；真读 `references/scoring-rubric.md:32-66`、`risk-checks.md:1-52`、`output-templates.md:64-137`；无脚本 | 先问约束，再查 current web；challenge/target/safety；scope 证据不可达时 cap；冲突优先官方 | 检索前约束卡、source conflict、每项 because | 把可信名单命中当 hard exclusion；没有 canonical JSON/handoff；不消费真实 PDF |
| 2 | `target-journal-matcher` · `aipoch/medical-research-skills`（1281★；`d92441066ea6259967469be8e0c8c7b6587928ab`） | `awesome-med-research-skills/Academic Writing/target-journal-matcher/SKILL.md:21-86,102-114`；真读 `scripts/main.py:31-76,203-278` 与 `references/scoring_weights.json` | topic/method/impact/practical 四面；Tier 1/2/3；Jaccard-based script 产解释 | 明拆 article type/method/data 与 scope | 内嵌 journal JSON/训练知识和 approximate IF；脚本 tier 阈值不等于编辑门槛；会给 top single recommendation |
| 3 | `journal-skills` · 同 repo（1281★；同 commit） | `scientific-skills/Evidence Insight/journal-skills/SKILL.md:1-145`；真读 `scripts/pubmed_journal_recommender.py:79-236`、`assets/journal_recommendation_template.csv`、`references/guide.md` | 从 title/abstract 抽词，经 PubMed ESearch/ESummary 聚合 container frequency，落 JSON/CSV | 相似 works 的 venue 频次只做 recall discovery；保存 query/example work | AND query 易过窄；频次不是 scope/质量；脚本无 HTTP failure 状态契约 |
| 4 | `journal-recommender` · 同 repo（1281★；同 commit） | `scientific-skills/Other/journal-recommender/SKILL.md:10-78,98-136`；真读 `scripts/journal_ranker.py:1-51` | Sprint/Robust/Safe 输出骨架；deterministic IF sort；要求 warning note | 保留档内 deterministic order 与验证摘要 | 示例写“near-certain acceptance”、强制每档 5 个、旧 IF/acceptance 格；不诚实且会为了凑数 |
| 5 | `find-journal` · `Aperivue/medsci-skills`（179★；`940412bee17fcb09f1a35fa3fa0e03a5cb11c489`） | `skills/find-journal/SKILL.md:52-126,130-229,304-370,443-475`；真读 `POLICY.md:15-96`、`references/acceptance_signals_schema.md:1-126`、`scripts/assess_acceptance_readiness.py:40-228` 和 `journal_profiles/JAMA.md:1-40` | 两遍 profile loading；scope × acceptance-readiness 分轴；profile promotion 需当天官网/ISSN；coverage gap advisory；fallback cascade | paper strength 与 scope 分开；source promotion bar；unknown coverage 显式化；下游 context | 大型本地 journal profile 库易腐，且 JAMA profile 无逐字段 check date；部分 design-ceiling 会越过 paper-writing/claims 边界 |
| 6 | `venue` · `queelius/papermill`（0★；`4f492e913391997e67e8d6409f1620f838bb62a3`） | `skills/venue/SKILL.md:16-109`；真读 `commands/venue.md:1-4`；无脚本/模板 | 从 thesis/prior art/review history 取上下文；reference venues + contribution type + web/CFP；top-down/calibrated/dual-track；写 state file | 保存上游上下文与决策日志；会议 CFP 作为一等来源 | 第 85–99 行直接写 target，未要求真实 user-selection artifact；接受率/时效无来源状态 |
| 7 | `publication-strategist` · `brycewang-stanford/Awesome-Agent-Skills-for-Empirical-Research`（2553★；`e16c5ab4708196fcbcb6ec16bc733e1f8b670695`） | `skills/26-Data-Wise-scholar/skills/writing/publication-strategist/SKILL.md:18-63,368-411`；真读内嵌 decision tree、cover-letter/rejection 模板；无脚本 | contribution-type decision tree；拒稿后按 desk/post-review 原因处理；预先读近期论文和建 cascade | contribution type→candidate family；转投不是只按指标降档 | 内嵌期刊 IF/周期已腐；venue/rebuttal/cover letter 边界过宽；无 provenance |
| 8 | `paper-writer` 的 journal-selection · `kgraph57/paper-writer-skill`（36★；`68dfe216fd27b54bc5f07212ee1ca029edb4afa8`） | 主 skill 配套 `references/journal-selection.md:1-270`、`journal-reformatting.md:1-152`；真读 cascade/recording template；skill 自带 31 templates + 5 scripts，但无专用 matcher script | 150 分 decision matrix；近 6–12 月目录/3+ similar papers；提前建 reach→target→safety cascade；重投改版清单 | recent comparable works、真实规则对照、submission plan | 大量内嵌 medical-AI venue/IF/APC/周期；Beall/DOAJ 表述会被误当 whitelist/blacklist；跨越 typesetting |
| 9 | `academic-writing-publication` · `a5c-ai/babysitter`（1468★；`44a5d58b47b93962f143914e0652d9e3ae5dcf2c`） | `library/.../academic-writing-publication/SKILL.md:1-91`；无配套 matcher 脚本/模板 | 把 journal selection、timing、OA、impact 与 submission/review 串成简短 SOP | 提醒 venue 决策必须放进完整出版路径 | 只有能力清单，无取数、证据、失败态或可执行输出；Light 不借其薄层 |
| 10 | `academic-paper` submission slice · `imbad0202/academic-research-skills`（36021★；`d3c287658e547c65106a9cbe45e4a01110ff2145`） | `academic-paper/SKILL.md:85-143,374-396`；真读 `references/journal_submission_guide.md:5-24`、`shared/contracts/submission/venue_profile.schema.json`、`scripts/check_preprint_venues_consistency.py` | intake 先收 target journal；配置确认后才推进；venue profile schema 串 formatter/reviewer；submission checklist | user-confirmed profile 与下游 consumer contract | 不是专职 matcher；guide 内嵌易腐 venue 长度/impact；predatory check 仍只列 Beall/DOAJ/Cabells |

补充核对但不计入 10：`majiayu000/claude-skill-registry`
`publication-prep`（469★；`cb6f0807c71f2ee440cd89b9b9d8ae0488a2c543`）
只有 `skills/data/publication-prep/SKILL.md:69-89` 的 scope/impact/OA/speed/
acceptance checklist，无配套脚本/模板，是 registry copy，机制不足以独立计名额。

## 2. 开放数据与 API（不计 skill）

| 资源 | 当天权限层 | 能证明 | 不能证明 / Light 处理 |
|---|---|---|---|
| OpenAlex Sources/Works | 免费 key；缺 key `UNAVAILABLE` | source identity、topics、recent works、coverage signals | 非官方 author rules/acceptance/JCR；key 口径只指向 literature-search 真相源 |
| Crossref REST `/works`,`/journals` | 免费公开、无需注册 | DOI/container/ISSN、candidate discovery、example works | container frequency 不是 fit/rank/safety；`venue_discovery.py` 保存 query/URL/time |
| DOAJ v3/site | 免费公开 | 当前 OA journal listing 的正面证据 | 查询失败或未命中不等于 predatory；failure 与 negative 分开 |
| ISSN Portal | 公共网页，部分功能受限 | title/ISSN identity 与 hijack 交叉核 | 不评编辑质量；受限即 unavailable |

## 3. 指标、风险与封闭资源（不计 skill）

| 资源 | 权限层 | 用法 | 边界 |
|---|---|---|---|
| Clarivate Master Journal List | 免费公开 lookup | WoS collection membership | JIF/quartile 要 JCR |
| JCR | 机构/付费 | JIF/JCR category/quartile | 无订阅不填；不由聚合站代写 |
| Scopus Sources/CiteScore/API | 免费登录/key + 机构完整权限 | Scopus source/CiteScore | 401/403/key 缺失=`UNAVAILABLE`，不是未收录 |
| SCImago SJR | 免费网页，未假设稳定 REST API | 年度 SJR/quartile 辅证 | 不混写 JCR；403/robots 不绕 |
| Cabells Journalytics/Predatory Reports | 付费闭源 | 用户有合法访问时作多指标证据 | 核心路径不得依赖；不编“未命中” |
| Think.Check.Submit | 免费公开 | 身份/peer review/费用/透明度人工清单 | 不是 whitelist 或自动 verdict |
| Retraction Watch hijacked checker | 免费公开 | hijack lead | 需 ISSN/domain/publisher 多源终判 |
| Beall archives | 历史存档 | 历史线索 | 非当前权威名单 |

## 4. Publisher finder 与官方 CFP（不计 skill）

| 资源 | 机制 | 借入点 | 偏差/边界 |
|---|---|---|---|
| Elsevier Journal Finder | title/abstract 对 Scopus-indexed Elsevier journal relevance；展示 publisher fields | abstract discovery + 决策列 | 只覆盖 Elsevier；每字段回官方页核 |
| Springer Nature Journal Suggester | abstract/description/sample text→SN journals | 文本匹配产生候选 | 只覆盖 SN |
| Wiley Journal Finder | keyword/abstract；可展示 first decision/acceptance/APC/JIF | 同一 publisher 内比较 current fields | 只覆盖 Wiley；高时效字段逐项记录当天 URL |
| IEEE Publishing Portal / Publication Recommender | journal/conference，scope/metrics/OA/time | conference+journal 双轨候选 | 只覆盖 IEEE；conference deadline 仍回当年 CFP |
| 当年官方 conference CFP | track、article type、page limit、deadline、notification、presentation | conference 当前规则唯一主源 | 去年页面不得复用；找不到即 UNKNOWN |

## 5. 论文、系统与评测数据（不计 skill）

| 项目 | 类型 | 可借机制 | 限制 |
|---|---|---|---|
| Schuemie & Kors, JANE（`10.1093/bioinformatics/btn006`） | journal suggestion system/paper | 用 title/abstract 与 PubMed 相似文献的 journals/keywords/authors | 生医域；候选频次不等于最终 fit |
| OpenAlex（arXiv `2205.01833`） | scholarly graph paper/dataset | sources/works/topics 的开放发现面 | 非 author guideline/付费指标真相源 |
| “Publication Venue Recommendation Based on Paper Title and Co-authors Network” | venue recommendation paper | 文本与作者网络分开建模 | 模型预测不等于当前作者约束或官方规则 |
| Rs4rs（arXiv `2409.05570`） | recent top-venue publication retrieval | recent venue corpus 支撑 scope/recent-comparable 检查 | 面向 recommender-systems 领域，不是通用选刊 benchmark |
| Crossref public works sample / OpenAlex snapshot | 可复验 discovery 数据 | 固定 query/example DOI 做候选发现回归 | 没有 ground-truth“最佳 venue”标签 |

本轮未找到可作为通用 gold truth 的公开、持续维护“稿件→最佳 venue + 作者约束 +
当前规则”评测集；因此不伪称有 benchmark。E2E 以真实 PDF facts、当天来源、
可解释 hard mismatch、unknown/unavailable 和用户决策纪律验收。

## 6. R1 落地点

- `SKILL.md`：推翻独特性吹法；固定 scope/type/method/format/constraint/risk
  分面、同日 freshness、user-selection artifact。
- `venue-resource-map.md`：八步作者闭环和五层访问权限。
- `references.md`：source role/authority/failure/risk/finder policy，不存 venue 值。
- `references/workflow_contract.md`：field envelope、六 canonical prepare 工件、
  三 selected 工件。
- `venue_discovery.py`：借 JANE/PubMed-frequency 类机制，但用 Crossref current
  metadata，只做 recall。
- `venue_workflow.py`：借 profile verification、two-axis explanation、cascade、
  checkpoint 思路，落实 stage-11 handoff 与 enforced human choice。
- `templates/venue_input.json`、`venue_compare_table.md`、`user_selection.json`：
  空白 provenance/status/decision 骨架，不内嵌易腐 venue 库。

## 7. Round 3 高星对象回读与选择证据绑定（2026-07-05）

本轮重新 clone 并固定源码，不把 Round 2 表格当作完成证据：

- `aipoch/medical-research-skills@d92441066ea6259967469be8e0c8c7b6587928ab`
  （GitHub API 1,291★）：完整读取 `target-journal-matcher`、`journal-skills`、
  `journal-recommender` 三个 skills，以及 682 行本地 matcher、236 行 PubMed
  recommender、51 行 ranker、权重和 guide；
- `brycewang-stanford/Awesome-Agent-Skills-for-Empirical-Research`
  固定 `7345a559e2e4511b603a2500c6af283406a3ca47`（2,619★）：完整读取 676 行
  `publication-strategist`；
- `a5c-ai/babysitter@44a5d58b47b93962f143914e0652d9e3ae5dcf2c`
  （1,476★）：完整读取 `academic-writing-publication`；它只有 90 行能力清单，
  无 matcher 代码，作为“高星父仓不等于深机制”的反例；
- `imbad0202/academic-research-skills`
  固定 `f86d68a80a6fd05bf51688ff39297ea603eda912`（36,247★）：读取 venue profile
  schema、完整 journal submission guide、preprint venue consistency lint 与
  academic-paper 的 venue/submission 契约切片。

五个主要 skill 对象由前三个 AIPOCH matcher、publication-strategist 和
academic-paper submission slice 构成；前三个来自同一父仓，不能误写成五个独立
高星仓库。skills.sh 也用于补检，但未找到能替代这些对象、同时具备可审计 matcher
代码的更强专职 skill。

### Round 3 五席纠偏（2026-07-05）

105 项矩阵原第 5 席是 `academic-paper` 的 submission 切片，不是专职 matcher。现用
`zero565656/journal-recommender` 替换：父仓当前 39★，固定
`407aff106677aac090bf2d177155db15e3593126`。低星不掩饰，但功能比高星父仓里的投稿切片
更直接。本轮完整读取 110 行 `SKILL.md`，以及 scoring rubric、risk checks、
output templates、data sources 五个文件；确认它真正执行用户约束澄清、current web source、
challenge/target/safety、official scope 优先、source conflict 与 unknown/fallback。

它的缺点也保留：部分 warning-list 规则偏硬，且只有散文协议、无 matcher 脚本和机读交付。
Light 已有更强的 stage-11 manuscript binding、来源状态、unknown/failure 分离和用户选择哈希，
所以本轮只纠正学习对象口径，不重复改代码，也不把 39★包装成热门。

源码反例很明确：AIPOCH matcher 内嵌易腐 IF/期刊库，评分还正向奖励 IF；
PubMed 脚本将精确标题与全部关键词用 AND 串联且无 HTTP 失败状态；另一 skill 强制
每档至少五本并写 “near-certain acceptance”；publication-strategist 内嵌统计学
期刊时效字段；36k 父仓的 venue profile 虽有 declared-only 纪律，仍不负责候选匹配。

回读 Light 后发现新的完整性缺口：用户可以看到一个未选择 decision packet，但
`choose` 原先只凭其中的文件路径重读 registry/source/fit；这些文件在用户选择前被
改写也不会被发现。现已：

1. prepare 将 candidate registry、source evidence、fit report、unknowns 逐一绑定
   相对路径、schema 与 SHA-256；
2. `delivery.json` 暴露 decision packet SHA-256；用户选择必须携带
   `decision_sha256`；
3. choose 重新哈希 decision 和四个工件，拒绝绝对/越界/改名路径、schema 漂移与
   内容漂移；
4. selected handoff 保存 decision/source/registry/fit 绑定；review-rebuttal 再验
   source-evidence SHA-256。

负向自测已覆盖缺 decision digest、篡改 registry、篡改 decision 和篡改下游来源
证据。边界不变：这证明“选择绑定所见证据”，不证明候选就是最佳 venue，也不预测接收。

## 8. Round 3 续补：选刊画像必须绑定 paper-writing claims

继续复核 `venue_workflow.py` 后发现一个 stage-12 入口漂移风险：prepare 会消费
`manuscript_profile`，但旧版没有要求它绑定 paper-writing 的当前 claim/profile
artifact。坏 agent 可以手工改写文章类型、claim 强度或 paper_strength，让 venue 看似更 fit。

本轮把 `manuscript_profile.claims_delivery` 变成必需绑定：

- 只接受安全相对 path，拒绝绝对路径、占位符与 `..` 越界；
- 必须有 schema 与真实 SHA-256；
- JSON artifact 的 schema 必须与声明一致；
- prepare 失败闭合于缺失、hash mismatch 或 schema mismatch；
- candidate registry 与后续 decision binding 会携带该 claims_delivery，从而让用户选择绑定当前稿件画像。

这不让 venue-matching 改写 claim；它只保证选刊推荐读取的是 paper-writing 交出的当前 claim/evidence profile。
