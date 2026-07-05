# research-plan Round 2 活体 E2E（2026-07-02）

## 场景与真实数据

研究问题：对公开 WDBC 患者，给 size-only logistic regression 增加
`texture_mean/texture_se/texture_worst`，是否能降低 patient-level Brier loss？

复用 data-engineering Round 2 固定血缘：

- provider/id：Hugging Face `scikit-learn/breast-cancer-wisconsin`
- revision：`e41c086f1614397ce7a5660980aac421047cef5e`
- file：`breast_cancer.csv`
- source URL：`https://huggingface.co/datasets/scikit-learn/breast-cancer-wisconsin/resolve/e41c086f1614397ce7a5660980aac421047cef5e/breast_cancer.csv`
- raw SHA256：`27f219231dbb30eecbfc1361407ed641ea01be43316e2c707a1baf82c9795e23`
- clean rows：569；仅删除可逐字确认的尾部全空导出列，`id` 只作 split/provenance

为避免用同一 outcome 同时定方案和确认：

- pilot：`id % 5 == 0`，86 人（M=32/B=54）
- confirmation：`id % 5 != 0`，483 人；pilot 脚本不读取其 outcome
- 统计/分析单位：patient；fold/seed 只是 repeated OOF prediction 的排程，不是独立 n

## 真实 pilot 与 estimand

两个模型使用相同 patient、fold schedule、`StandardScaler`、`C=1`、`liblinear` 与算力；唯一变化是
三个 texture 特征。10× repeated stratified 5-fold 只在 pilot 上生成每位患者的平均 OOF probability。

pilot 实得：

| 指标 | size-only | size + texture |
|---|---:|---:|
| AUROC | 0.988426 | 0.990162 |
| Brier | 0.040539 | 0.037981 |

patient-paired Brier improvement：

- mean：`0.00255822`
- raw paired `dz`：`0.044729`
- 5,000 次 patient bootstrap 95% CI：`[-0.01007475, 0.01378234]`

confirmation estimand 冻结为 483 位患者上
`mean(Brier_size_only - Brier_size_plus_texture)`。支持门为 mean ≥0.0075 且 95% patient-bootstrap
CI lower >0；mean ≤0 或 CI upper <0.0075 为反证；其余为 inconclusive。

## 活体抓到并修复的真实问题：伪精确 power

把 pilot raw `dz=0.044729` 和 10 个 seeds 直接喂现有工具：

```powershell
python skills/light-research-plan/scripts/power_check.py --effect 0.044729 --n 10
```

真实输出：

- actual power=`0.051`
- min n=`7847` per group
- exit `0`（工具正常完成计算）

数字本身对 `TTestIndPower` 没错，**研究设计映射错**：本研究是同一 patient 的 paired prediction，
10 个 seeds/folds 相关且重复使用同一 outcome，不能当两个独立组。若照旧模板把 7,847 写成“所需 seeds”，就是
正式功效分析伪装。

修法没有迁就工具：

1. `power_check` 保持原码，只作双独立样本均值近似；
2. confirmation N 固定 483，改用 paired `statsmodels.stats.power.TTestPower` 做 sensitivity；
3. 80% power、双侧 alpha=.05 的 MDE 为 `dz=0.127731`；
4. 按 pilot paired-difference SD 映射为 Brier MDE=`0.00730544`；
5. 冻结 low/base/high 情景 `0.003 / 0.0075 / 0.012`，不把 noisy pilot 单点当真值；
6. `plan_gate` spec 不伪填 `power.n_seeds`，statistical_power 诚实 `skip`；正式 paired sensitivity 留在计划与预注册。

这也促成永久修文：SKILL、references、research-plan/experiment-matrix/preregistration 模板均显式禁止把
seeds/folds/cluster 内行数当独立 n，并把复杂设计路由到匹配方法或 simulation。

## 坏计划真阻断

先把同一研究写成真实坏计划：

- candidate 给 100-search tuning，baseline 只用默认配置；
- H1 写“texture makes prediction better”，无任何 falsifier；
- 无 ablation；
- statistical power 因未提供适用参数而 skip，不拿它掩盖 critical。

`plan_lint` 对形式齐全 exit `0`，但明确给“无 ABL” warning——坐实 lint 绿不等于科学有效。

`plan_gate` 实得：

- `fair_baseline=fail/critical`
- `falsifiable=fail/critical`
- `ablation_isolation=warn/major`
- overall `verdict=fail`
- exit `1`

把 `workflow_findings.json` 交：

```powershell
python skills/light-orchestrator/scripts/run_checkpoint.py `
  --file .upgrade/_e2e/research-plan-round2/workflow_passport.yaml `
  --stage 5 --findings workflow_findings.json --write `
  --ts 2026-07-02T15:40:00+08:00
```

checkpoint 真 exit `1`；passport stage 5 真变：

- `status=gate_failed`
- `gate.result=FAIL`
- evidence=`sha:7a8b42df@2026-07-02T15:40:00+08:00`

## 按根因真修后 delivered

在同一路径修复方案：

- baseline 与 candidate 同 patients/splits、同 scaler/C/solver/fold/compute，唯一变化是三个 texture 特征；
- 写出成功/失败/inconclusive 与量化 falsifier；
- 补 single-variable texture ablation、permuted-texture negative control 与 jitter robustness；
- primary F1 只有一个 comparison；secondary/robustness 不得 rescue 失败的 F1；
- 固定 N=483，无 optional stopping、无 outcome 后排除；
- power 改 patient-paired sensitivity，不再冒充 seed power；
- 预注册状态写 `LOCAL-DRAFT`，明确未提交 OSF/AsPredicted、无 registry ID。

复跑实得：

- `plan_lint`：3 行、rigor 100/100、exit `0`
- `plan_gate`：fair/falsifiable/ablation pass，power skip，overall pass，exit `0`
- stage-5 checkpoint：exit `0`
- passport：`status=delivered`、`gate.result=PASS`
- evidence=`sha:73fb0a72@2026-07-02T16:00:00+08:00`
- `passport validate`：`verdict=PASS`、exit `0`

## 回炉边界

本 E2E 是 research-plan 自身门 fail，故只在 stage 5 内修，不伪造 `ROUTES[5]` 出边，也不演示 7→5。
只有未来 result-analysis 产“哪条假设未被结果支撑 + effect/CI”的真实 root-cause finding 时，才可让
`reroute --stage 7` 建议 7→5；建议后必须停下让用户拍板，再决定是否落 back edge。

## 审计结论

本 E2E 只证明：

1. 固定 revision/lineage 能进 question→estimand→design；
2. 公平对照/可证伪 critical 会真阻断；
3. 机器 lint 形式绿不会掩盖科学缺口；
4. 真实 pilot 能暴露 power 的单位/方法错配；
5. 修方案后 checkpoint 与 passport 真交付。

它不证明 texture 在 confirmation 上有效；confirmation outcome 在本 E2E 中未运行。临时产物执行时位于
`.upgrade/_e2e/research-plan-round2`，已在收口时删除；本文件保留永久证据。
