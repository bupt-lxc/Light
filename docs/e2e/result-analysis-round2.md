# result-analysis Round 2 活体 E2E 证据记录

> 执行日：2026-07-01；临时运行件 `.upgrade/_e2e` 已删除。本页只留可复验事实与命令。

## 输入与真实实验

- 数据：UCI [Breast Cancer Wisconsin (Diagnostic)](https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic)，
  DOI `10.24432/C5DW2B`；UCI 页标 569 instances、30 features、无 missing、CC BY 4.0、1995-10-31 donated。
- 下载：
  `https://archive.ics.uci.edu/static/public/17/breast%2Bcancer%2Bwisconsin%2Bdiagnostic.zip`
- hash：archive `bc154869...b05d3af`；`wdbc.data` `d606af41...c3695f4a`。
- 实验：标准化 LogisticRegression vs prior DummyClassifier；12 个 stratified repeated-holdout seeds，
  每个 seed 两方法共享同一 split；test size 25%；主指标 accuracy，次指标 balanced accuracy。
- raw results：24 行，SHA-256 `6faef62f...4a8292d`。
- 环境：Python 3.11.13 / NumPy 2.0.0 / pandas 2.2.3 / scikit-learn 1.5.2。

统计单位是 seed，但不同 seed 的测试集重叠，因此 paired t 只作 sensitivity cross-check，不冒充 12 个
独立外部复现。`analysis_plan_audit` 对 `repeated_holdout` 保留 1 条复杂设计 warn。

## 首跑错误、阻断与新 warn

现实分析错误不是改 raw results，而是：

1. 跑了 accuracy + balanced accuracy 两个比较，只报 accuracy（`comparisons_run=2`,
   `comparisons_reported=1`）；
2. plan 在看结果后才标定且未声明 exploratory；
3. family planned=2/reported=1；
4. raw result 缺 hash、run manifest/commit locator。

首跑结果：

- `stat_rigor_gate`：`phacking.selective_reporting` → critical，exit 1；
- `analysis_plan_audit`：7 条 warn，exit 0（不扩大 blocking 面）；
- `run_checkpoint --stage 7`：整体 FAIL，exit 1。

## 修复与复跑

只修改分析规格/报告：

- 报全两个 planned comparisons；
- 同一 family 一次 BH；
- asserted grade 按 n=12 降为 weak；
- 写回真实 plan 时间线、family、coverage、hash、owner/time、run manifest/commit；
- raw results 不变。

复跑：

- `stat_rigor_gate`：PASS，exit 0；
- `analysis_plan_audit`：原 7 条降为 1 条
  `analysis_design.complex_requires_model` warn；
- `run_checkpoint --stage 7`：WARN，exit 0。

最终 `evidence_strength.json` 只有 2 条 paired claims，均因 n<30 为 weak；没有同一数据再产
2 条 independent duplicate claims。

## E2E 抓到并修复的脚本 bug

旧 `analyze_results --paired-by seed` 会同时把 independent 与 paired 比较写入
`claim_evidence_table.md` / `evidence_strength.json`；本例因此从两个科学比较膨胀成 4 条 claim。
这会把同一 seed 结果又当独立样本，并污染下游。

修复后：

- `primary_comparisons()` 以声明设计选择主比较；
- paired 模式保留 independent 结果仅作 advisory；
- claim/evidence 与 `stat_rigor_gate --results-csv --paired-by` 只消费 paired；
- selftest 断言三组 paired 数据只能产 3 条 claim，且全带 `:paired`。

## R / Python 交叉核验

环境真相：

- `Rscript` 不在 PATH；
- launcher 找到 `C:\Program Files\R\R-4.6.0\bin\Rscript.exe`；
- base R/`boot` 可用；`broom/effectsize/rstatix/emmeans/lme4` 未安装。

accuracy paired comparison：

| 数值 | Python | base R | 差 |
|---|---:|---:|---:|
| mean difference（dummy−logistic） | -0.3444055944055944 | -0.344405594405594 | 3.89e-16 |
| t | -114.90457717458436 | -114.904577174584 | 浮点误差 |
| p | 2.71331231971822e-18 | 2.7133123197182e-18 | 1.73e-32 |
| d_z | -33.17009428143321 | -33.1700942814332 | 浮点误差 |

CI 不要求逐位相等：Python 路径是 percentile bootstrap，R 路径是 t-based CI；两者均完全小于 0，
方向一致。这里可声称“base-R 关键检验 E2E 通过”，不能声称高级 R mixed-effects 路径通过。

## 下游真实消费

`paper-writing/scripts/claim_evidence_gate.py` 真消费修复后的 `evidence_good.json` 与带 hedge 的草稿：

- 识别最强证据档 weak；
- `claim_evidence=pass`、`overclaim=pass`；
- 整体 verdict=pass，exit 0。

未修改 paper-writing/research-ethics/consistency/figure；只验证既有接口。result-analysis 产出的
claim/metric 若要进 consistency，只能作为带 provenance 候选，不能直接写 canonical registry。

## 2026-07-02 收口复核

用 Windows PowerShell `Set-Content -Encoding UTF8` 生成带 BOM 的最小规格，并故意只写
`status=frozen`、省略 `locked_at/results_available_at`、令 `inputs=[]`。旧实现先因 BOM
`JSONDecodeError` 崩溃；去 BOM 后又错误给出零告警 PASS。修复后同一带 BOM 输入稳定返回
`analysis_plan.timeline_missing` 与 `provenance.no_inputs` 两条 warn、exit 0，仍不扩大 stage-7
critical 面；selftest 同时锁住 BOM、缺时间线和零输入工件三条边界。
