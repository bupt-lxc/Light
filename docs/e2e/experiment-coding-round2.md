# experiment-coding Round 2 活体 E2E

执行日：2026-07-02。工作树基线 `8962b797c53c63f78aa35b4c166476286101ba1d`；实验发生在未提交升级
worktree，因此每个 manifest 如实记录 `dirty=true`、基线 commit、dirty diff SHA256 和运行源码 hash，没有把 WIP
冒充已提交代码。

## 冻结输入与实现

- 数据：Hugging Face `scikit-learn/breast-cancer-wisconsin`
- revision：`e41c086f1614397ce7a5660980aac421047cef5e`
- raw SHA256：`27f219231dbb30eecbfc1361407ed641ea01be43316e2c707a1baf82c9795e23`（下载后实算一致）
- clean：569 行；仅删除尾部全空 `Unnamed: 32`
- confirmation：`id % 5 != 0`，483 patients；统计单位 patient
- baseline：9 个 size 特征（radius/perimeter/area 的 mean/se/worst）
- candidate：baseline + `texture_mean/texture_se/texture_worst`
- 公平常量：同 patients、RepeatedStratifiedKFold 10×5 schedule、StandardScaler、`C=1`、`liblinear`、
  CPU/float64；唯一变化是 3 个 texture 特征

预处理和 logistic regression 放入 sklearn `Pipeline`，每折只在 training fold `fit`。固定 seed 用于同环境复跑；
另一 seed 只验证“可变但可追溯”，不当患者样本量。

## 测试先行与真实暴露的问题

scaffold 先加测试，后加实现：

1. gold Brier；
2. Hypothesis 概率范围 property；
3. 同步置换 metamorphic；
4. RecordingTransformer 证明 train-only fit。

红灯是真红灯：

- 第一次因 `example.experiment_contracts` 不存在而 `ModuleNotFoundError`；
- 实现后 gold fixture 把手算结果错写成 `0.075`，pytest 实得 `0.125`，复算后修 fixture；
- `hypothesis>=6.156` 当天解析不到，uv 只找到 `6.155.7`，改为可解析范围并生成 lock。

最终 scaffold：`14 passed, 2 skipped`；ruff lint/format、mypy 均 exit `0`。skip 是未安装的可选 torch 后端，
不是伪报通过。

## 坏实现先使真实 checkpoint 失败

真实坏代码在 `StratifiedKFold.split` 前对全量 `X` 做 `StandardScaler.fit_transform`。旧 `review_gate` 只认识
`train_test_split`：

- 旧门：`verdict=pass`，exit `0` —— 暴露真实 CV 扫描盲区；
- 最小修复：只把已知 sklearn CV splitter、`cross_val_score/cross_validate/cross_val_predict` 加为划分边界，
  并避免把普通字符串 `.split()` 当数据划分；
- 修后同一坏代码：`DATA-LEAKAGE fail/critical`，exit `1`；
- `repro_gate`：leakage fail，reproducible skip，overall fail，exit `1`；
- `run_checkpoint --stage 6`：`status=gate_failed`、exit `1`，证据
  `sha:02d17750@2026-07-02T18:10:00+08:00`。

坏 findings SHA256：
`87e48383962ddade164a88b161d5a88df2f334c9aac364a3767bc9685692be59`。

这是 stage 6 自身门失败，故只在 stage 6 修代码，没有制造 `ROUTES[6]` 出边。

## 修复后真实运行

三次 confirmation run 的 raw 汇总（这里只记录运行事实，不替 result-analysis 下统计结论）：

| run | seed role/value | size-only Brier | size+texture Brier | paired improvement | predictions SHA256 |
|---|---|---:|---:|---:|---|
| fixed-a | fixed_repro / 20260305 | 0.05492281297 | 0.03964832881 | 0.01527448416 | `336ffa06d3b37f3f8bdc673fd4e82cd23333a9a29f09ef27b6ac568bc5fdbffe` |
| fixed-b | fixed_repro / 20260305 | 0.05492281297 | 0.03964832881 | 0.01527448416 | `336ffa06d3b37f3f8bdc673fd4e82cd23333a9a29f09ef27b6ac568bc5fdbffe` |
| alternate | randomness_estimation / 20260702 | 0.05439241331 | 0.03905111097 | 0.01534130233 | `36d7df45e86e8a9ea601f4844abf4b025dc8f70605d2db7973365d6dfc1b0572` |

固定 seed pair 的 `run_artifact_check --compare` 实得：

- `same_seed_exact=true`
- predictions hash 相同；
- raw_metrics hash 均为
  `f803bfe0115ee6e2d2139905664249e9b6cc0bf58a1353e0e1855cb6e3af8a4e`；
- errors `[]`，exit `0`。

换 seed 后 predictions 与 raw_metrics hashes 都变化，manifest 的 seed role/value、config hash 与 split ID 同步变化。

## manifest 自身也做了活体验证

第一版 manifest 的汇总与 artifact hashes 都对，但记录的 argv 漏掉 `--data`、`--schema`，不能凭清单重放。
逐字段审查发现后：

- 把运行源码、配置 schema、raw data 一并封进 bundle；
- argv 改为完整参数数组；
- 增加 dirty diff SHA256；
- 删除旧临时 runs 后从头重跑三次。

然后直接读取 `fixed-a/manifest.json` 的 `command` 数组，在该 run dir 原样执行，成功生成独立 replay bundle；
replay 再过单 bundle 校验，并与 fixed-a 做同 seed 比较，predictions/raw_metrics hashes 仍完全相同，三个 exit 均为 `0`。

固定 run 的关键 provenance：

- config SHA256：`e2bf221687fd63a70e62ff11e3c17663d8d7a55ed479c88359990606bad318e2`
- environment SHA256：`354b063aef77f31f42ce970610d2ac1980c294484857abbfd7fce889f1c905d9`
- source SHA256：`04bc63406992658e6e7f428930937dcfa73083887fa3e78040d949687c77c822`
- schema SHA256：`38fb935481a9203651d8a4a5cfebcfec12e63dfe0eea42c63d94822f059ffec9`
- dirty diff SHA256：`f0d574134f9427e725dec769d657c23cbbef9122c22a048db7e0234869ab0e74`

每个 run 实际包含 manifest、config、environment、stdout、stderr、每折+每 patient raw metrics、483 行
patient-level predictions、test evidence、源码/schema/data hashes；completed run 的 failure 为 null。坏实现另保留
gate/checkpoint failure evidence，没有只留一张 summary CSV。

## 修复后门控与下游交接

- `review_gate`：pass，exit `0`
- `seed_audit`：Python hash/random/NumPy 全覆盖，exit `0`
- `repro_gate`：leakage/reproducible pass，exit `0`
- stage-6 checkpoint：delivered，exit `0`，证据
  `sha:accc5a1a@2026-07-02T18:30:00+08:00`
- passport validate：PASS，exit `0`
- result-analysis `analysis_plan_audit` 消费三份 predictions + manifests + commit/hash/coverage：
  `warning_count=0`、verdict pass、exit `0`

good findings SHA256：
`09ff014b56cb12361771b06335e993bd442f217ae24cde663e261ab0930f08de`。

没有演示 7→6：本轮没有 result-analysis 产出的真实 bug/unreproducible root cause。强行造 reroute 会违反接线；
未来若出现真实下游 finding，只让 `reroute` 建议，落 back-edge 前必须停下由用户决定。

## 证据边界与清理

- 静态门通过不证明所有语义泄漏都不存在；
- 同 seed 三次 hashes 一致只支持本次代码/data/config/environment，不能证明跨硬件或跨版本绝对复现；
- confirmation 的科学支持/反证/inconclusive 应由 result-analysis 按冻结 patient-level estimand、bootstrap CI 与门限判定，
  本文不越权下结论；
- 执行期临时 bundle 位于 `.upgrade/_e2e/experiment-coding-round2`，收口时删除；永久保留本文件中的命令结果、
  hashes、退出码和边界。
