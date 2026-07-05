# paper-writing Round 2 活体 E2E

> 执行日：2026-07-02。临时运行件位于 `.upgrade/_e2e`，收尾前已删除；本页保留可复验来源、命令、hash、首跑失败、修稿、复跑、reroute 与下游消费事实。

## 真实数据与实验

- 数据：UCI Breast Cancer Wisconsin (Diagnostic)，DOI `10.24432/C5DW2B`，CC BY 4.0；官方页列 569 instances、30 features、无 missing。
- 下载：`https://archive.ics.uci.edu/static/public/17/breast%2Bcancer%2Bwisconsin%2Bdiagnostic.zip`。
- `wdbc.data` SHA-256：`d606af411f3e5be8a317a5a8b652b425aaf0ff38ca683d5327ffff94c3695f4a`。
- 实验：40 个 stratified repeated-holdout seeds，75/25 split；每个 seed 的 logistic、RBF SVC、DummyClassifier 共享同一 split。
- raw results：120 行；SHA-256 `ed962e9e56c321cb94355f66cac652a99ab940ed8c9d7c8f75f416ead27717a0`。
- 环境：Python 3.11.13、NumPy 2.0.0、pandas 2.2.3、scikit-learn 1.5.2。

重复 holdout 的 test sets 会重叠；40 seeds 是 paired sensitivity repetitions，不是 40 个独立外部复现。稿件明确限制为单公共数据集 benchmark，不做临床部署、因果或普遍优越性 claim。

## 上游真实工件

重跑：

```powershell
python skills/light-result-analysis/scripts/analyze_results.py `
  .upgrade/_e2e/raw_results.csv --group method --metric accuracy `
  --outdir .upgrade/_e2e/analysis --paired-by seed `
  --emit-claim-table --emit-evidence
```

真实 `evidence_strength.json`：

| evidence claim ID | q | paired effect | 95% CI(mean diff) | n | grade |
|---|---:|---:|---:|---:|---|
| `accuracy:dummy_prior_vs_logistic:paired` | 3.81e-59 | d_z=-30.301 | [-0.3495,-0.3425] | 40 | strong |
| `accuracy:dummy_prior_vs_rbf_svc:paired` | 2.73e-12 | d_z=-30.974 | [-0.3474,-0.3407] | 40 | strong |
| `accuracy:logistic_vs_rbf_svc:paired` | 0.3466 | d_z=0.151 | [-0.0021,0.0059] | 40 | none |

均值 accuracy：logistic 0.9753、RBF SVC 0.9734、dummy 0.6294。显著性按三条 paired comparisons 一次 BH-FDR。

## Claim / section plan

`claim_plan_good.json` 使用 `light.paper_claims.v1`：

- 同一科学 claim 在 abstract/introduction/results/conclusion 的每个实际句子分别登记稳定 occurrence ID；
- `text` 是草稿中唯一的精确 span；
- `locator` 指真实 section/paragraph；
- `evidence_claim_ids` 指上表具体 claim ID；
- `source_locators` 至少保留 evidence artifact + claim ID/row；
- null claim 带“failure to reject is not proof of equivalence” boundary；
- figure 只登记 requirement，未在 paper-writing 顺手画图；
- DOI 只作为 citation candidate，真实性归 citation。

## 首跑：现实写作错误被 critical 门拦

坏稿同时写：

1. 有 strong evidence 的 dummy comparison：“logistic 比 prior dummy 平均高 34.6 accuracy points”；
2. 完全不受证据支持的：“logistic 显著优于 RBF SVC，并建立新 SOTA”。

坏 claim plan 故意只登记第 1 条。旧实现 `_best_grade()` 会取整份证据的 strong 档给全文兜底；第 2 条因此可能漏过 critical。

Round 2 逐 claim 门首跑：

```powershell
python skills/light-paper-writing/scripts/claim_binding.py `
  --draft .upgrade/_e2e/draft_bad.md `
  --evidence .upgrade/_e2e/analysis/evidence_strength.json `
  --claim-map .upgrade/_e2e/claim_plan_bad.json

python skills/light-paper-writing/scripts/claim_evidence_gate.py `
  --draft .upgrade/_e2e/draft_bad.md `
  --evidence .upgrade/_e2e/analysis/evidence_strength.json `
  --claim-map .upgrade/_e2e/claim_plan_bad.json `
  --report .upgrade/_e2e/bad_findings.json
```

结果：

- `claim_binding.unregistered_assertion` 命中坏句的 `significantly/demonstrate/establish/outperform`；
- `claim_evidence` = fail/critical；
- `claim_evidence_gate` exit 1；
- `draft_lint --final --evidence --claim-map` exit 1；
- contribution consistency 另报坏稿 SOTA 贡献未在 conclusion 呼应；
- raw results 与 evidence 未修改。

## Stage-8 checkpoint 与 reroute

用相对路径初始化 passport 并 append stage 8 后：

```powershell
python skills/light-orchestrator/scripts/run_checkpoint.py `
  --file .upgrade/_e2e/passport.yaml --stage 8 `
  --findings .upgrade/_e2e/bad_findings.json --write `
  --ts 2026-07-02T08:30 --out .upgrade/_e2e/checkpoint_bad.md
```

真实 exit 1。随后：

```powershell
python skills/light-orchestrator/scripts/reroute.py `
  --findings .upgrade/_e2e/bad_findings.json --stage 8 `
  --passport .upgrade/_e2e/passport.yaml --json
```

真实输出：

- decision point = true；
- 默认建议 root cause stage 7 / result-analysis；
- evidence pointer = `paper-writing:claim_evidence@line 6,...`；
- carry 明写“默认 8→7；若属实现/复现缺口则改 8→6”；
- quota 0/2。

诚实边界：`ROUTES[8]` 只有默认 target 7；8→6 是作者判断“实验根本未产出”后的用户 override，不是 reroute 自动语义分类。本轮按约定不改 orchestrator，也未擅自落 back edge。

## 真修稿

没有改 raw results，也没有伪造 evidence。修稿做了三件事：

1. 删除 unsupported SOTA/显著优于断言；
2. 按 none evidence 改为 “no significant difference”，并保留 q/effect/CI/n；
3. 给 abstract/introduction/results/conclusion 的每个实际 claim span 绑定自己的 evidence ID 与 source locator。

另把 conclusion 的主贡献改为可被 contribution extractor 识别且与摘要数字/强度/覆盖一致；不是用 E2E 断言遮门。

## 复跑：全链转绿

```powershell
python skills/light-paper-writing/scripts/claim_binding.py `
  --draft .upgrade/_e2e/draft_good.md `
  --evidence .upgrade/_e2e/analysis/evidence_strength.json `
  --claim-map .upgrade/_e2e/claim_plan_good.json
python skills/light-paper-writing/scripts/claim_evidence_gate.py `
  --draft .upgrade/_e2e/draft_good.md `
  --evidence .upgrade/_e2e/analysis/evidence_strength.json `
  --claim-map .upgrade/_e2e/claim_plan_good.json `
  --report .upgrade/_e2e/good_findings.json
python skills/light-paper-writing/scripts/draft_lint.py `
  .upgrade/_e2e/draft_good.md --final `
  --evidence .upgrade/_e2e/analysis/evidence_strength.json `
  --claim-map .upgrade/_e2e/claim_plan_good.json
python skills/light-paper-writing/scripts/contribution_consistency.py `
  --in .upgrade/_e2e/draft_good.md --json
python skills/light-paper-writing/scripts/mechanical_check.py `
  --file .upgrade/_e2e/draft_good.md `
  --evidence-map .upgrade/_e2e/analysis/evidence_strength.json
```

结果：

- claim binding：7 个 span，0 coverage error，0 overclaim，0 traceability warning，exit 0；
- canonical findings：claim_evidence / overclaim / claim_traceability / contribution_consistency 全 pass，verdict=pass，exit 0；
- draft lint final：exit 0；
- contribution consistency：0 drift，exit 0；
- mechanical check：仅 3 条被动语态表层建议，exit 0；
- `run_checkpoint --stage 8`：exit 0。

## 下游真实消费

真实运行：

```powershell
python skills/light-research-ethics/scripts/claim_evidence_bind.py `
  --draft .upgrade/_e2e/draft_good.md `
  --evidence .upgrade/_e2e/analysis/evidence_strength.json `
  --target wdbc-paper-writing --json
```

research-ethics 读取稿件 + 同一 evidence artifact，`conclusion_overclaim` pass，exit 0，证明接口确实可消费。

同时用坏稿实跑同一命令也得到 pass。原因是该下游现状仍写明 `strongest grade=strong`，没有消费 paper-writing 的 per-claim map；strong A 仍可能遮住 unsupported B。这是活体发现的下游语义边界，不得伪称“research-ethics 已逐 claim”。本轮范围明确禁止顺手改 research-ethics；paper-writing 的 stage-8 critical 已在交下游前阻断坏稿，后续应由 research-ethics 专属 Round 2 处理。

## 活体发现的其他边界

1. `_shared/evidence_contract` 对英文 “did not differ significantly” 仍会命中 `significantly`；改成它明确允许的 “no significant difference” 后通过。本轮不改共享契约。
2. `draft_lint` 首跑会把句末 `.` / `;` 带进 DOI 候选，导致同一 DOI 两种字符串；收口复核已把 regex 改为 DOI 必须以字母、数字或右括号结束，并补重复候选回归。
3. passport 把 Windows 绝对路径写进双引号 YAML 时，反斜杠会触发 unknown escape；E2E 改用仓库相对路径后 checkpoint 正常。本轮不改 orchestrator。
4. `mechanical_check --evidence-map` 是语义启发式表层建议；canonical 逐 claim 判定来自 `claim_binding`，两者不能互换。
5. 这次统计说明 benchmark 差异，不证明临床有效性、因果机制、外部泛化、模型最优或论文会被录用。
