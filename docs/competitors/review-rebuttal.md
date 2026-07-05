# review-rebuttal Round 2 对标证据

核查日：2026-07-03（Asia/Shanghai）

范围：peer-review response、rebuttal drafting、review triage、revision
planning、commitment tracking、meta-review/author response、pre-submission
reviewer simulation。GitHub star 为核查日仓库页面精确值；commit 为当天浅克隆
HEAD。skill 与 API/平台、规则、LLM 写作工具、论文/数据集分表，后四类不计入
“真同类 skill”数量。

## 旧结论复核

旧表的下列“差异点”全部作废，不得再称 Light 独有：

- reviewer clustering / reviewer priority；
- 原子化与 major/minor/question 分类；
- point-by-point reply 与 tone polish；
- word/character budget；
- change locator；
- revision plan 与 promise/commitment tracking；
- venue-rule adaptation；
- 多 reviewer、meta-review、返修复审。

ARIS rebuttal 已同时做原子 issue board、pivotal reviewer、字符预算、三种
provenance/commitment/coverage gate、revision plan 与多轮 follow-up；academic
research skills 已做 re-review、commitment ledger 和 paper-blind sprint
contract；Nature response 已做 reviewer 原话保真、`AUTHOR_INPUT_NEEDED` 与
package readiness。旧“同类 field 空”也失效。

Light Round 2 的可证差异缩窄为：

1. 真校验 venue-matching 的用户授权选择、venue rule envelope 和 stage-11
   PDF/hash/pages/page-size/profile/compliance；
2. reviewer 原话/decision/meta-review 为不可变 source layer，atom/分类/草稿为
   派生层；
3. 每 issue 真绑定 paper claim、result evidence、citation work、change locator、
   run provenance，并机械阻止 `PLANNED` 写成 `DONE`；
4. stage 13 仅有显式 rejection-driving evidence 的 novelty/experiment/writing
   根因可 critical；`reviewer_classify`/`reroute` 只建议，必须等用户选择后才能
   `add-back-edge`。

这些差异已落入 `SKILL.md`、resource map、workflow contract、JSON 模板与五个
脚本，不只留在本笔记。

Round 3 续补（2026-07-05）把第 2/3 条再收紧：`review_workflow.py` 现在会为每个
AVAILABLE review source 写入并核对 `raw_sha256`，要求 `captured_at` 带时区且不来自未来；
DONE 的 experiment/analysis 不再接受“本机路径存在”作为 provenance，必须有匹配 SHA-256。
这对齐 OpenReview note/reply 级原始对象和 Paper2Rebuttal/RebuttalAgent 的 evidence-centric
planning 思路：先冻结原话/运行证据，再生成 response letter；但仍不宣称自动判断回应是否 persuasive。

## 真同类 skill（12 个 / 8 repo）

| # | 真同类 skill | repo star / fixed commit | 真读文件、行与配套资源 | 具体机制 | 可借点 | Light 真实差距 |
|---|---|---|---|---|---|---|
| 1 | ARIS `rebuttal` | `wanshuiyin/Auto-claude-code-research-in-sleep` **12,952★** · `82076e5e2dc200144622e6a52ceae070a7c1f384` | `skills/rebuttal/SKILL.md:81-92,104-132,216-256`；`skills/shared-references/review-tracing.md:5-23,32-50` | 明确 venue rules；原话归档；issue board；pivotal reviewer；provenance/commitment/coverage 三门；revision plan；follow-up trace | 三门分离、issue→revision 双向覆盖、真实多轮状态 | Light 没有其多后端压力测试、per-reviewer thread 与自动 follow-up；ARIS 反而缺 Light 的 stage-12/11/claim/evidence/citation 契约真校验 |
| 2 | `academic-paper-reviewer` | `Imbad0202/academic-research-skills` **36,031★** · `d3c287658e547c65106a9cbe45e4a01110ff2145` | `academic-paper-reviewer/SKILL.md:199-216,234-257,406-412`；`references/re_review_mode_protocol.md:23-52`；`templates/revision_response_template.md:1-64` | 五 reviewer + EIC/DA；paper-blind sprint contract；re-review 四态；commitment ledger；calibration FNR/FPR | 预注册评价标准、复审必须跳到实际修改、panel cardinality | Light 无 reviewer calibration、五人 panel 和完整预审合同；Light 的优势只在跨 stage 机器契约与用户确认回边 |
| 3 | `rebuttal-writing` | `lingzhi227/agent-research-skills` **179★** · `9e6c085d65e313e475e921fdfe795ac11eb7589e` | `skills/rebuttal-writing/SKILL.md:22-66`；`references/rebuttal-prompts.md:5-34,60-69` | 逐点抽取、证据回应、section/table/equation locator、变更摘要 | 小而清楚的 parse→respond→format 流 | “只写做过、不写将做”本身会诱导把未做动作伪装完成；Light 用显式状态而不是强迫过去时 |
| 4 | dotfiles `rebuttal` | `mrilikecoding/dotfiles` **0★** · `92f4ae128967e774749cf7556c4649d541c9a778` | `home/.claude/skills/rebuttal/SKILL.md:29-77,125-145,205-213`（分类/triage/letter 模板均内嵌） | 原话、major/minor、难度、must/should/push-back/cannot、用户确认后再写 | 把 author agency 放在 triage gate，不让模型替作者 push back | 无机器 provenance/状态/coverage；Light 已补，但其“先确认 parsing”不是 Light 独有 |
| 5 | dotfiles `peer-review` | 同 repo/star/commit | `home/.claude/skills/peer-review/SKILL.md:15-23,44-62,228-238,348+`（review/response/revision 模板内嵌） | 3–5 独立 reviewer、汇总、author response、修稿、重投 ensemble | reviewer independence + revision 后复审闭环 | Light 当前无自动独立 panel 与 score update；不能把“投前模拟”吹成机器闭环 |
| 6 | `aer-rebuttal` | `brycewang-stanford/aer-skills` **22★** · `22c7f604d8f04d1730a17ba2f8e9e6892e551dbc` | `skills/aer-rebuttal/SKILL.md:10-42,62-73,127-189`；`examples/rebuttal-example.md:1-30,57-115` | AER/AEJ R&R；editor-first；concede/clarify/push-back；先改稿再据修订稿写信 | 把 response letter 定位为 editor verification package；处理 reviewer 冲突 | Light 是通用框架，缺 AER 领域规范；venue-specific judgment 必须来自当次官方规则，不能内嵌 AER 经验 |
| 7 | `aer-referee-sim` | 同 repo/star/commit | `skills/aer-referee-sim/SKILL.md:3-44,68-126`；与上列 worked response 配套 | 10 分钟 desk screen + 三种 reading order；major 必须 manuscript-anchored 且 resolvable | desk screen 与 referee 层分开；要求“怎样才会改变判断” | Light 没有 AER-specific calibrated desk simulation；只保留通用投前审查指导 |
| 8 | `reviewer-2-simulator` | `48Nauts-Operator/opencode-baseline` **4★** · `1efc5d36b9d523c7e9cb1620847c9d1c2767580d` | `.opencode/skill/reviewer-2-simulator/SKILL.md:15-40,90-147,199-225`（killer questions、score、rebuttal priority 模板内嵌） | 5-minute skim→deep read→killer questions→scores→rebuttal priorities | 模拟“审稿人会略读”的现实失败面 | 无 provenance/commitment/venue source；只适合投前 stress test |
| 9 | `paper-review` | `Ne1ther/paper-workbench` **2★** · `836d858e532fe4fc3896bb0cd34fe5d68613e529` | `templates/paper-review/SKILL.md:43-55,80-103,126-160`；`references/review-panel.md:45-77`；`review-feedback-checklist.md:8-46` | reviewer panel→author rebuttal→reviewer update→AC meta-review；匿名汇总 | reviewer response 后允许更新判断，meta-review 独立 | Light 没有 reviewer update/AC scoring loop；Light stage-13 critical 只处理可证根因 |
| 10 | `review-response` | `Galaxy-Dawn/claude-scholar` **4,479★** · `2f7766fd541a723d4ddc6230b3277f948d61b093` | `skills/review-response/SKILL.md:14-46`；`references/review-classification.md:7-43,110-130`；`response-strategies.md:41-126` | Major/Minor/Typo/Misunderstanding；Accept/Defend/Clarify/Experiment；tone/templates | 分类→策略映射与误解处理 | priority、tone、point-by-point 都已覆盖，绝非 Light 独有；其模板含“正在做/预计结果”风险，Light 状态门更严 |
| 11 | `nature-response` | 同 repo/star/commit | `skills/nature-response/SKILL.md:18-61,92-123`；其 `references/intake-and-routing.md`、`action-mapping.md`、`qa-checklist.md` 路由表 | editor-first IDs；原话保真；`AUTHOR_INPUT_NEEDED`；readiness 四态；Nature source hierarchy | 输入不全时输出 readiness 而不是补写事实 | 与 Light Round 2 很接近；Light 缺 Nature-specific difficult-case depth，优势仅是上游契约与 stage-13 route |
| 12 | `paper-self-review` | 同 repo/star/commit | `skills/paper-self-review/SKILL.md:38-47,65-89,102-128`；`references/FINAL-VERDICT.md` 与 `SECTION-CHECKLIST.md` | claim audit、overclaim、post-revision verification、final checklist | 明确不替 result/citation，保持分工 | Light 同样必须承认投前 claim audit 非独有；当前无该 skill 的 section-level checklist 丰度 |

### Round 3 五席纠偏（2026-07-05）

105 项矩阵原第 4 席是“公开 rebuttal 案例 + NeurIPS checklist”，属于案例/规范，不是
同功能 skill。现替换为 ARIS `rebuttal`：父仓当前 13,000★、MIT，固定
`7421d2e5a24c1b090cd1efd8b9b39ac77056aa92`。本轮重新完整读取 368 行
`skills/rebuttal/SKILL.md` 与 185 行 `skills/shared-references/review-tracing.md`，
确认其直接覆盖 per-reviewer thread、多轮 follow-up、pivotal reviewer、venue mode/budget，
以及 provenance、commitment、coverage 三道门和逐次 reviewer trace。

可借机制此前已在 Light 的原话层、动作状态、证据 provenance、coverage 与用户授权回边中落实。
ARIS 的多后端 reviewer 压力测试更丰富，但依赖 Codex/Oracle/manual-review MCP，且默认 venue
常量需要覆盖；Light 不引入这些依赖，也不把 agent reviewer 的报告当机器真实性证明。

### R1 落地映射

| 学到的机制 | Light 落点 |
|---|---|
| ARIS 原话/atom/三门/issue↔revision 双向覆盖 | `review_workflow.py`、review registry、issue matrix、revision plan、commitment ledger |
| academic reviewer 的复审四态与实际 locator 核验 | `templates/rereview_checklist.md`、`check_commitments.py` |
| dotfiles/AER 的 author agency 与 editor-facing triage | SKILL 的策略集合与 stage-13 用户停顿 |
| Nature response 的 source/interpretation 分层与 readiness | workflow contract、`UNKNOWN/UNAVAILABLE/STALE`、failure/delivery |
| reviewer simulation 的 skim/deep/AC 分层 | resource map 的投前路径；诚实标为人判主场，不宣称自动校准 |
| peers 的 venue budget | `rebuttal_budget.py` 改成只消费 selected context，删全部 venue preset |

## API / 公开评审数据（不计 skill）

| 资源 | 访问层 | 真读机制 | Light 使用边界 |
|---|---|---|---|
| OpenReview API v2 | 免费公开；私有 forum 可能需登录 | 官方文档说明 `forum`/`details=replies|directReplies`；review/rebuttal/meta/decision 是 per-paper reply | `fetch_openreview.py` 保存 raw content/signature/invitation/time；失败写 `UNAVAILABLE` |
| PeerRead 固定 OpenReview 快照 | 免费公开；GitHub 固定 commit | paper/reviews/meta/decision JSON；同一文件可能含重复对象 | 只作历史公开数据；`--peerread-url` 保留原文并显式报告去重数，不冒充 live API |
| 用户 portal export / decision email | 本地免费（用户提供）或免费登录 | 是真实作者材料的优先源 | 不尝试绕过登录；原文与附件保真 |
| JORS 官方 submissions/editorial policies | 免费公开 | 文章类型、稿件格式、review outcome；本次未找到 response limit/new-material 明文 | manuscript 4–6 页不当作 response limit；相关字段保持 `UNKNOWN` |
| Scopus/WoS/机构全文 | 机构受限 | 可增强先行工作/证据核对 | 不在核心路径；无权限为 `UNAVAILABLE` |

OpenReview 一手文档：

- https://docs.openreview.net/reference/api-v2
- https://docs.openreview.net/how-to-guides/data-retrieval-and-modification/how-to-get-all-notes-for-submissions-reviews-rebuttals-etc

## Publisher / conference rebuttal rules（不计 skill）

| 类型 | 当次应查 | 纪律 |
|---|---|---|
| 所选 venue | 当前 author/revision/rebuttal 页面 + decision letter | 只用当年/当轮明确规则 |
| Publisher 通用教程 | response-letter 建议 | 只能作写法建议，不能覆盖 venue policy |
| OpenReview conference | 当年 author guide + forum UI limit | 不从另一届/另一会迁移字符数或新材料规则 |
| JORS 本轮 | submissions + editorial policies + 用户 decision letter | 公开页没找到 response 限额/新材料规则，保留 `UNKNOWN` |

JORS 一手页：

- https://openresearchsoftware.metajnl.com/about/submissions
- https://openresearchsoftware.metajnl.com/en/about/editorialpolicies

## LLM 写作工具（不计 skill）

| 工具/系统 | 类型 | 可学机制 | 不能替代 |
|---|---|---|---|
| ChatReviewer | prompt/tool | 逐条抽取与回应格式 | provenance、planned/done、真实修改核验 |
| Paperpal / Writefull / SciSpace | 闭源写作辅助 | tone/clarity/语言编辑 | venue 规则、实验结果、引用真实性、author decision |
| 通用 chat LLM | 生成器 | 草稿与压缩 | 原话层、证据层、commitment gate；不得直出“已改” |

核心路径不依赖这些付费/闭源工具。

## 论文与评测集（不计 skill）

| 论文/数据 | 一手事实 | 借点 | Light 差距 |
|---|---|---|---|
| Paper2Rebuttal / RebuttalAgent, arXiv:2601.14171 v2 | 原子 concern、hybrid context、内外证据、先 plan 后 draft；RebuttalBench | evidence-centric planning | Light 无自动段落检索与 benchmark |
| DEFEND, arXiv:2603.27360 | segment-wise targeted refutation + author-in-loop；扩展 ReviewCritique 标注 action/error | author intent 不可被模型猜 | Light 只记录用户输入，不做其交互式推理模型 |
| Author-in-the-Loop Response Generation, arXiv:2602.11173 | 将作者 expertise/intent 作为核心输入 | action/intent 显式化 | Light 尚无专门 intent elicitation UI |
| Re², arXiv:2505.07920 | full-stage、多轮 reviewer-author 数据与一致性处理 | round/decision/rebuttal 链 | Light E2E 只抓一组公开 discussion，不是全数据训练 |
| Rebuttals Move Peer-Review Scores, arXiv:2606.22166 | 初审结构约束分数移动；2026-06 新工作 | 不夸大 rebuttal 翻盘能力 | 尚未把 outcome model 回灌决策 |

一手页：

- https://arxiv.org/abs/2601.14171
- https://arxiv.org/abs/2603.27360
- https://arxiv.org/abs/2602.11173
- https://arxiv.org/abs/2505.07920
- https://arxiv.org/abs/2606.22166

## 结论

Round 1 把常见 rebuttal 方法误写成 Light 增量；Round 2 后不再成立。Light 的
价值不是“会礼貌逐条回复”，而是把**谁说了什么、这是谁的解释、对应哪条 claim/
证据、动作是否真的完成、venue/PDF 事实来自哪、何时有资格触发 stage-13 critical、
谁有权执行回边**变成可机检契约。仍落后于头部 peers 的多 reviewer 校准、多轮
reviewer update、自动 manuscript grounding 和 author-intent 交互模型。
