# venue-matching Round 2 活体 E2E

日期：2026-07-03（Asia/Shanghai）

开工基线：`d3cb1cd`（typesetting Round 2 收口）

范围：仅 `light-venue-matching`，以及本证据页。

## 结论

本轮把 venue-matching 从“若干启发式分数”改成了可执行的作者选刊闭环：

1. 校验并消费 typesetting 的真实 `light.typesetting_venue_handoff.v1`；
2. 保留 paper-writing、figure、citation、typesetting 的输入哈希与 provenance；
3. 按字段记录来源、查询、检查日、权限层和
   `AVAILABLE|UNKNOWN|UNAVAILABLE|STALE`，不把缺证据当负证据；
4. 输出候选注册表、来源证据、fit/risk、unknown/unavailable、未选择决策包；
5. 先保持 `decision_point=true, chosen=null`，向用户提出真实选择；
6. 用户明确说“都行，你选一个吧”后，诚实记录
   `selected_by=agent, decision_authority=user` 与原话授权，再产 JORS handoff；
7. 作者投稿计划与 review-rebuttal context 真消费所选 venue 规则和 stage-11
   provenance；没有自动投稿。

## R1 真同类复核

`docs/competitors/venue-matching.md` 固定了 2026-07-03 当天 star、repo、
commit、文件/行及真读脚本/模板。主表拆了 10 个 skill、9 个仓库，另把
OpenAlex/Crossref/DOAJ、JCR/Scopus/SJR、Cabells/Think.Check.Submit、
publisher finder/官方 CFP、论文/数据分别列表。

旧说法“分层推荐、风险信号、决策点独特”不成立。真同类已经覆盖
scope matching、venue ranking、APC/deadline filtering、predatory warning、
author-fit、解释性推荐、投稿级联与人为决策点。Light 本轮保留的可证差异是更窄的：

- 真校验 stage-11 PDF/hash/pages/page-size/profile/compliance；
- 每字段 provenance、权限层、时效与缺失状态；
- 429/403/5xx/key/login/subscription 不转成风险；
- 未选择工件与选择后 handoff 分离；
- stage 12 不伪造 gate、route 或 critical finding。

这些机制已分别落入 `SKILL.md`、`venue-resource-map.md`、
`references/workflow_contract.md`、`references.md`、模板和两个 canonical
脚本，不只停留在竞品笔记。

## stage-11 真实输入

E2E 用 paper-writing 形态的 LaTeX 稿、当前 figure 导出 PDF 和 citation
delivery 运行现有 `build_submission.py`，不是手写 venue handoff：

```text
build_submission.py --spec typesetting-input.json --json
exit 0
status=DELIVERED
compliance_status=PASS
critical_count=0
pages=2
page_size=612 x 792 pts (letter)
pdf_sha256=e50006d2dc6a4630d7be13bc75845309c27bdac2cfb6683d570006412639fca7
```

`venue_workflow.py prepare` 重算 PDF SHA-256，核对 compliance report 的页数/
page size，并保存 build manifest 内 paper-writing、figure、citation 的路径和哈希。
它没有重编译、改版或把 stage-11 unavailable 当合规。

## 真实发现、证据与分档

Crossref 当前查询：

```text
query=provenance reproducible research software workflow evidence
rows=50
exit 0
works=44
candidate containers=12
```

随后用当天官方规则、OpenAlex/DOAJ live signal 和作者约束逐候选核验：

| 档位 | 候选 | because |
|---|---|---|
| 冲刺 | Data Intelligence | scope 高；稿件强度为中；APC、OA、审稿周期未知，Scopus 机构源不可用 |
| 稳妥 | Journal of Open Research Software | scope/experience-report/method fit 高；真实 2 页低于官方约 4–6 页，必须扩写；APC £865、full OA |
| 保底 | MethodsX | method article fit；APC US$1,290；官方当前展示首次决定等描述性时长，但接收率未知 |
| 排除 | Journal of Open Source Software | 当前稿不是合格 research-software package，且无公开仓库与所需开发历史 |

JORS 的 OpenAlex 发文量变化保留为 `WARN`；DOAJ listing/Seal 与官方透明费用同时
保留，未据单一软信号判成掠夺。Scopus 与 Cabells 分别因机构权限和付费订阅记
`UNAVAILABLE`，未写成“未收录”或风险。候选接收率没有当天官方公开来源，均保持
`UNKNOWN`，没有从 fit 分数编概率。

准备阶段 canonical 工件：

```text
candidate-registry.json
source-evidence.json
fit-risk-report.json
unknowns.json
decision-packet.json
delivery.json
```

首次 `prepare` 与修复后复跑均 exit 0。决策包明确：

```json
{
  "stage": 12,
  "decision_point": true,
  "chosen": null,
  "stage_contract": {
    "confirmation_checkpoint": false,
    "in_STAGE_GATES": false,
    "has_ROUTE_out_edge": false
  }
}
```

运行时枚举得到 `STAGE_GATES=[2..11,13]`（无 12），
`ROUTES=[2,3,4,7,8,9,13]`（无 12），断言 exit 0。

## 真实用户决策与下游消费

先向用户展示三档、排除项、费用和 unknown；此时 `chosen` 一直为空。用户回复
“都行，你选一个吧”，形成明确委托。基于最高 scope/article-type fit 选择 JORS，
但保留 2→4–6 页扩写要求：

```json
{
  "status": "SELECTED_WITH_USER_AUTHORIZATION",
  "selected_by": "agent",
  "decision_authority": "user",
  "user_authorization": "都行，你选一个吧",
  "chosen": "jors"
}
```

`venue_workflow.py choose` exit 0，生成：

- `selected-venue-handoff.json`；
- `author-submission-plan.json`，列出需重查 review time、acceptance rate、
  indexing，并停在 portal submit 前；
- `review-rebuttal-context.json`，真含 JORS rules、fit/risk、source IDs、
  manuscript profile 与上述 PDF hash/pages/profile/compliance。

选择不是 stage-12 confirmation gate，也不自动提交。若需要按 JORS 规则扩稿，
应回到相应稿件/排版阶段另做新构建；venue-matching 没有擅改当前 PDF。

## 活体暴露并修复的问题

1. OpenAlex 返回的宽泛 top concepts 让明显匹配的 JOSS/JORS 得到
   `semantic_fit=0`，而旧体量说明又把增长写得像风险。现加入带 source/date 的
   official scope override；体量增长改为中性事实，仍需多源人工终判。
2. 页数比较器只支持“最大页数”，把 JORS 官方约 4–6 页压成 `max=6`，误判真实
   2 页合适。现支持 `{min_pages,max_pages}`；低于最小值为可修 warning，超过最大值
   才 hard exclude。JORS 复跑得到 `page_fit=false`、稳妥档不变、明确要求扩写。
3. 旧 `choose` 只校验 candidate ID 存在，理论上允许选择 `excluded` 候选。现只接受
   non-excluded ID，并有 direct user 与 explicit delegation 两种可审计身份；无授权
   agent、伪委托和 excluded selection 均由 selftest 拒绝。
4. skill-creator 的 `quick_validate.py` 首次在中文 Windows 默认 GBK 下读取 UTF-8
   `SKILL.md`，报 `UnicodeDecodeError`、exit 1。显式 `PYTHONUTF8=1` 后同一校验
   `Skill is valid!`、exit 0；这是校验器启动环境问题，不隐藏首次失败。

## 回归

亲眼确认的最终结果：

| 检查 | 结果 |
|---|---|
| venue-matching 5 个脚本 `--selftest` | 5/5，全部 exit 0 |
| typesetting 5 个脚本 `--selftest` | 5/5，全部 exit 0 |
| paper-writing 7 个脚本 `--selftest` | 7/7，全部 exit 0 |
| citation 6 个脚本 `--selftest` | 6/6，全部 exit 0 |
| review-rebuttal 4 个脚本 `--selftest` | 4/4，全部 exit 0 |
| orchestrator 3 个脚本 `--selftest` | 3/3，全部 exit 0 |
| `python -m _shared` | exit 0 |
| `compileall`（上述技能与 `_shared`） | exit 0 |
| 全仓 JSON 解析（临时件清理后） | 20 个，0 失败，exit 0 |
| stage-12 字典与 selected/downstream 断言 | exit 0 |
| `quick_validate.py`（UTF-8 模式） | valid，exit 0 |
| `git diff --check` | exit 0 |

活体临时输入、PDF、API 响应和选择工件运行时位于
`.upgrade/_e2e/venue-round2`；按约定在收口提交前删除。本页永久保存关键事实、
状态、哈希、真实选择与 exit code。
