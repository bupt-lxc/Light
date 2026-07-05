# research-ethics Round 2 活体 E2E

> 执行日：2026-07-02。临时件位于 `.upgrade/_e2e`，收尾前删除；本文保留可复验来源、命令、首跑失败、真实修复与复跑结果。

## 1. 真实数据与证据工件

数据使用 UCI Breast Cancer Wisconsin (Diagnostic)：

- 官方下载：`https://archive.ics.uci.edu/static/public/17/breast%2Bcancer%2Bwisconsin%2Bdiagnostic.zip`
- UCI DOI：`10.24432/C5DW2B`
- `wdbc.data` SHA-256：`d606af411f3e5be8a317a5a8b652b425aaf0ff38ca683d5327ffff94c3695f4a`
- 活体下载读得 569 instances、30 features、无本地伪造数据；
- 40 个 stratified repeated-holdout seeds；每个 seed 在同一 75/25 split 上跑 logistic、RBF SVC、prior dummy；
- raw results 共 120 行。

真实重跑：

```powershell
python .upgrade/_e2e/research_ethics_wdbc.py
python skills/light-result-analysis/scripts/analyze_results.py `
  .upgrade/_e2e/raw_results.csv --group method --metric accuracy `
  --outdir .upgrade/_e2e/analysis --paired-by seed `
  --emit-claim-table --emit-evidence
```

`evidence_strength.json` 真实得到：

| evidence claim ID | BH q | paired d_z | 95% CI(mean diff) | n | grade |
|---|---:|---:|---:|---:|---|
| `accuracy:dummy_prior_vs_logistic:paired` | 1.30e-60 | -33.045 | [-0.3498,-0.3435] | 40 | strong |
| `accuracy:dummy_prior_vs_rbf_svc:paired` | 2.73e-12 | -26.528 | [-0.3474,-0.3393] | 40 | strong |
| `accuracy:logistic_vs_rbf_svc:paired` | 0.1411 | 0.238 | [-0.0010,0.0073] | 40 | none |

重复 holdout 的测试集会重叠，40 seeds 是 paired sensitivity repetitions，不是 40 个独立外部复现。这个 benchmark 不证明临床有效性、
因果、普遍最优或论文可录用。

## 2. 首跑：strong A 不能再遮住 unsupported B

坏稿有两句：

1. logistic 优于 prior dummy，绑定真实 strong evidence；
2. “logistic 显著优于 RBF SVC 并建立新 SOTA”，但 claim plan 故意不登记。

paper-writing Round 2 已证明旧 research-ethics 会取整份 evidence 的 strongest grade=strong 给全文兜底，使第 2 句错误 pass。本轮改为
复用 `light-paper-writing/scripts/claim_binding.py` 的 `light.paper_claims.v1` evaluator：

```powershell
python skills/light-research-ethics/scripts/claim_evidence_bind.py `
  --draft .upgrade/_e2e/draft_bad.md `
  --evidence .upgrade/_e2e/analysis/evidence_strength.json `
  --claim-map .upgrade/_e2e/claim_plan_bad.json `
  --target uci-wdbc-bad --json
```

真实结果：

- verdict `fail`；
- gate `conclusion_overclaim` = `fail/critical`；
- `state-of-the-art`、`significantly`、`establishes`、`outperforms` 均命中
  `claim_binding.unregistered_assertion`；
- 进程 exit `2`；
- 没有改 raw results/evidence 来迁就稿件。

### 活体抓到的噪声 bug

首跑最初同时报告 `outperform/outperforms`、`establish/establishes`，把 4 个真实信号膨胀成 6 条。原因是共享词表允许词形扩展，
canonical evaluator 又按 matched 字面去重。修复只落在 research-ethics 消费适配层：同 rule/claim/locator 且命中词互为前缀时保留
更长词形；不同信号仍保留。复跑变为 4 条，selftest 加入“`significantly outperforms` 只产 2 个唯一信号”的断言。

## 3. 真修稿与复跑

修稿不补造证据：

- 删除 unsupported SOTA/显著优于断言；
- 按 none evidence 写 `no significant difference`，带 q/d_z/CI/n；
- 两个实际 claim span 分别登记唯一 text/locator、自己的 evidence ID 与 source locator；
- 明写 failure to reject 不是 equivalence，且 repeated holdout 非独立外部复现。

```powershell
python skills/light-research-ethics/scripts/claim_evidence_bind.py `
  --draft .upgrade/_e2e/draft_good.md `
  --evidence .upgrade/_e2e/analysis/evidence_strength.json `
  --claim-map .upgrade/_e2e/claim_plan_good.json `
  --target uci-wdbc-good --json
```

真实结果：2 个 claim、0 integrity finding、verdict `pass`、exit `0`。

另一路防回退也实跑：强断言有 `--evidence` 但无 `--claim-map` 时不再取 strongest grade，直接
`claim_binding.map_missing` critical；无强断言的 hedge 文本仍可通过。

## 4. 真联网撤稿核查：抓到关系方向 bug

Crossref/RW production 文档已从 Labs 迁到正式服务。本轮对真实 DOI 做联网核查：

```powershell
python skills/light-research-ethics/scripts/check_retractions.py `
  10.1021/am300292v `
  10.1021/acsami.9b11759 `
  10.1126/science.aac4716 --json
```

首跑旧脚本把被撤原文 `10.1021/am300292v` 错报 `CLEAN`。直接检查 Crossref JSON 后确认：

- 被撤原文记录用 `updated-by` 指向撤稿通知；
- 撤稿通知 `10.1021/acsami.9b11759` 用反向 `update-to` 指回原文；
- 旧脚本只读 `update-to`，关系方向反了。

修复：

1. 对被查原文只把 `updated-by` 的 retraction/correction/EoC 当状态信号；
2. 同时兼容 Crossref 返回单 object 或 array；
3. 保留 `RETRACTED:` 标题前缀作 legacy 兜底；
4. 明确忽略通知记录的反向 `update-to`，避免把撤稿通知本身判为“被撤稿”；
5. selftest 覆盖 object/list、反向关系与标题兜底。

复跑真实结果：

- `10.1021/am300292v` → `RETRACTED`，notice DOI=`10.1021/acsami.9b11759`，source=`retraction-watch`；
- 撤稿通知自身 → `CLEAN`（它是通知，不是被撤原文）；
- Open Science Collaboration 论文 → `CLEAN`。

`CLEAN` 只表示 Crossref production relation/title 未见信号，仍非绝对保证；高利害引用交叉 RW CSV/出版商通知。

## 5. R2 资源工作流活体核

R2 新增 `references/ethics-resource-map.md`，把真实研究过程接成：

`法域/机构/对象/数据/阶段分诊 → 设计与批准 → 实施/变更/incident → 分析/逐 claim 门 → 投稿发布/出版后`

当天可访问并核过：

- OHRP 45 CFR 46 与 2018 Requirements decision charts；
- ORI 2024 Part 93 implementing guidance（2026-01-01 allegation 分流）；
- COPE Core Practices/flowcharts；
- ICMJE 2026 Recommendations、CRediT；
- Helsinki 2024、ARRIVE 2.0；
- Crossref production Retraction Watch 文档；
- 中国卫健委 2023 涉人伦理办法、科技部 2023 科技伦理审查办法（试行）与 2022 科研失信调查规则。

因此 `cn_compliance.md` 不再写“政府官网不可访问、全部待核”，改为已核高层事实 + 项目当天复核 + 机构 SOP/有权主体优先。

## 6. 回归

收口要求：

```powershell
$env:PYTHONUTF8='1'
Get-ChildItem skills/light-research-ethics/scripts/*.py |
  ForEach-Object { python $_.FullName --selftest }
python skills/light-paper-writing/scripts/claim_binding.py --selftest
python -m _shared
```

结果：research-ethics 6/6 脚本、canonical claim-binding 与 `_shared` 全绿；临时 `.upgrade/_e2e` 已删除。

诚实边界：citation 当前另有自己的 Crossref relation 消费逻辑；本轮按作者范围只改 research-ethics，不顺手改 citation。

## 7. Round 3 续补：consent scope 用途覆盖门

执行日：2026-07-05。

Round 2 只能核“有 consent process/form 证据”和 authority scope delta，不能机器阻断“有一份同意书，但实际用途超出录音、公开引文、
二次使用、共享、跨境、模型训练或退出边界”的情况。Round 3 新增：

- `skills/light-research-ethics/scripts/consent_scope_gate.py`
- `skills/light-research-ethics/assets/consent-scope-packet.example.json`

公开示例故意 fail-closed：

```powershell
$env:PYTHONUTF8='1'
python skills\light-research-ethics\scripts\consent_scope_gate.py `
  --input skills\light-research-ethics\assets\consent-scope-packet.example.json `
  --as-of 2026-07-05
```

真实结果：exit `1`，`verdict=fail`；阻断 UNKNOWN 法域/机构、录音和 repository release 缺 consent basis、可搜索声音/影像风险缺
mitigation locator、共享/发布缺 withdrawal boundary、退出后保留数据缺给参与者解释、跨附件一致性 UNKNOWN。

新增脚本自测：

```powershell
python skills\light-research-ethics\scripts\consent_scope_gate.py --selftest
```

真实结果：exit `0`，覆盖 pass packet、active use 缺 basis、future checked_at、公开引文 deductive disclosure、repository release
退出边界、withdrawal policy、附件不一致、计划阶段 UNKNOWN 只 warn、NOT_REQUIRED 与 basis 冲突。

全量回归：

```powershell
$env:PYTHONUTF8='1'
Get-ChildItem skills\light-research-ethics\scripts\*.py |
  Sort-Object Name |
  ForEach-Object { python $_.FullName --selftest; if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE } }
python -m compileall -q skills\light-research-ethics
python -m ruff check skills\light-research-ethics
python "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" skills\light-research-ethics
git diff --check
```

真实结果：research-ethics 9/9 selftests、compileall、ruff、quick_validate、diff check 全部 exit `0`。

诚实边界：`consent_scope_gate` 不是全球 IRB 表单 linter，不裁定 waiver/exempt，也不提供法律意见；它只核“每个实际用途是否有 consent/
broad consent/assent+permission/waiver/authority not-required 的真实 locator、checked_at、退出边界和附件一致性”。
