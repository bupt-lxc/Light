# experiment-coding R1 真同类重学

> 核验日：**2026-07-02**。star 是当天 GitHub snapshot，不拿 star 当质量分；commit 固定到表中 SHA。
> 本轮逐个读取了真同类的 `SKILL.md` 及其实际配套 reference/script/template。pytest、PyTorch、sklearn、
> MLflow/DVC、Ruff/Bandit、论文/规范属于**机制锚**，另表列，不再拿来充“同类技能”数量。

## 旧结论复核

旧表“真同类稀疏、Light 的 TDD/设 seed/安全扫描/复现实验独特”不成立。公开技能已普遍覆盖 config-first、
smoke/TDD、seed 重跑、不可变 run、元数据 lineage、baseline/keep-discard 和安全/lint。Light 可诚实主张的差异只在
**组合与接线**：代码级 leakage（含 CV fit 穿越）+ 框架感知 seed audit + 复用数据件 `split_leakage` +
canonical findings/stage-6 checkpoint + result-analysis 真实 bug/unreproducible 才可建议 7→6，且用户批准前不落边。

## 八个真同类（已读 SKILL + 配套件）

| 真同类 | 当天 star / repo / 固定 commit | 真读文件与行 | 具体机制 | 可借点 | Light 的真实差距 |
|---|---|---|---|---|---|
| phd-skills / reproduce | 305★ · [`fcakyon/phd-skills`](https://github.com/fcakyon/phd-skills/tree/1a44aeb830dcf629096863882ac142c0c44948f7/plugin/skills/reproduce) · `1a44aeb830dcf629096863882ac142c0c44948f7` | `SKILL.md:25-57`; `03-gap-analysis.md:3-114`; `04-implement.md:22-117`; `06-smoke.md:7-125`; `07-replicate.md:17-100` | 每个超参带 provenance；config 先于 loop；forward→one-step→20-iter 三级 smoke；full replication 给差异 verdict | 把“测试”分层为低成本可证伪 smoke，并保留每级日志 | Light 还没有论文→缺口表→代码的专用提取器，也不自动调 debug skill |
| phd-skills / launch | 305★ · [`fcakyon/phd-skills`](https://github.com/fcakyon/phd-skills/blob/1a44aeb830dcf629096863882ac142c0c44948f7/plugin/skills/launch/SKILL.md) · 同上 | `SKILL.md:30-75` | 找最近相似 config、做 diff、稳定 run name、路径与 monitoring preflight，未过则不 launch | launch 前把最终 config diff 和路径验证变成证据 | Light 的门偏代码正确性，长任务监控/重启清理协议较弱 |
| experiment-agent | 129★ · [`Imbad0202/experiment-agent`](https://github.com/Imbad0202/experiment-agent/tree/e291e7dc7ca268b2de7e1a9cf23bc2eef5dc0651) · `e291e7dc7ca268b2de7e1a9cf23bc2eef5dc0651` | `SKILL.md`; `agents/code_runner_agent.md:48-95`; `references/reproducibility_protocol.md:9-45`; `templates/output_formats.md:117-130` | 先分 deterministic/stochastic/environment-sensitive；执行器收 exit、stdout/stderr；按 exact/tolerance/distribution 比较 | 不同实验类型使用不同复现判据，失败也留 stderr | Light 新增了 exact artifact hash pair，但 stochastic distribution comparison 仍需 result-analysis |
| ml-experimentation | 35★ · [`ericmjl/skills`](https://github.com/ericmjl/skills/tree/e5a01a606571721bd3f9d7db68a6acbbd61b7f83/skills/ml-experimentation) · `e5a01a606571721bd3f9d7db68a6acbbd61b7f83` | `SKILL.md:18-62`; `experiment-setup.md:8-72`; `logging-guide.md:9-61`; `script-patterns.md:3-193` | 单一假设；<60 秒 de-risk；ISO 不可变 run dir；JOURNAL；失败 run 保留但可从图表排除；PEP723/uv | 不覆盖失败 run、先小跑证伪、日志有 run/seed identity | Light 的 scaffold 是项目型 lock/schema，更重；缺少 JOURNAL 的叙事便利 |
| ml-experiment-tracking | 6★ · [`KentoShimizu/sw-agent-skills`](https://github.com/KentoShimizu/sw-agent-skills/tree/5b7bafb626d3b76fa411a14653d399f20e7c7ae6/skills/ml-experiment-tracking) · `5b7bafb626d3b76fa411a14653d399f20e7c7ae6` | `SKILL.md:16-48`; `assets/experiment-tracking-schema-template.md`; `references/reproducibility-metadata-rules.md:3-5` | code/data/config/artifact 四段 lineage；仅凭元数据重跑；lineage 不全即停 | 把 artifact lineage 完整性当 decision-grade 前提 | Light 现在能 hash 校验 bundle，但还没有跨 run 查询 UI/数据库 |
| ml-pipeline-workflow | 37,435★ · [`wshobson/agents`](https://github.com/wshobson/agents/blob/5cc2549a50fc672230efd0a0307e2fd27ffba792/plugins/machine-learning-ops/skills/ml-pipeline-workflow/SKILL.md) · `5cc2549a50fc672230efd0a0307e2fd27ffba792` | `SKILL.md:30-75,126-144,224-233`；按该 commit 复核其声称的 `references/`/`assets/`，仓库中不存在 | 声称 DVC lineage、MLflow registry、训练 config、漂移监控的一体 MLOps 流程 | 端到端阶段清单与上线后反馈回路 | 它的配套件缺失、机制多为口头；Light 核心脚本更可执行，但部署/监控明显更窄 |
| ScienceClaw / autoresearch | 230★ · [`lamm-mit/scienceclaw`](https://github.com/lamm-mit/scienceclaw/tree/f4a628669d1bcf9702cf29d068716c02f1c9268f/skills/autoresearch) · `f4a628669d1bcf9702cf29d068716c02f1c9268f` | `SKILL.md:24-28,64-79`; `scripts/autoresearch_client.py:49-92`; `scripts/USAGE.md:43-73` | 固定时间预算、单指标、baseline、keep/discard；client 输出 repo/论文 dossier | bounded loop 和明确 keep/discard | 随附 client 只产 clone dossier/stub，真实运行依赖外部 repo；Light 不做自主搜索循环，但会真校验 run |
| research-program-skill | 1★ · [`XWHQSJ/research-program-skill`](https://github.com/XWHQSJ/research-program-skill/blob/2e9ea05cd5d467568357ba9410b51a84942b26fc/skills/research-program/SKILL.md) · `2e9ea05cd5d467568357ba9410b51a84942b26fc` | `SKILL.md:36-54,69-98,146-191` | baseline-first；program 明列 allowed/forbidden files、command、metric、stop；每次只跑一个；`results.tsv` + logs + keep/discard | 修改范围与停止条件显式化，防 agent 失控 | `results.tsv` 比 Light manifest 轻、易读；但不足以保存 predictions/raw metrics/hash/provenance |

## 机制锚（不计入八个同类）

| 机制锚 | 一手机制 | 落点 |
|---|---|---|
| [pytest stable](https://docs.pytest.org/en/stable/reference/reference.html#pytest-approx) / [Hypothesis](https://hypothesis.readthedocs.io/) | `approx` 容差；生成性质与 shrink；gold/property/metamorphic 各抓不同 bug | scaffold `test_experiment_contracts.py`，先红后绿 |
| [PyTorch reproducibility](https://docs.pytorch.org/docs/stable/notes/randomness.html) | Python/NumPy/torch/CUDA、deterministic algorithms、cuDNN、DataLoader worker；跨 release/platform 不保证 | `seed_audit.py` + reproducibility helper + resource map 边界 |
| [sklearn common pitfalls](https://scikit-learn.org/stable/common_pitfalls.html#data-leakage) / [Pipeline](https://scikit-learn.org/stable/modules/compose.html#pipeline) | split first、train-only fit、Pipeline 把 preprocessing 放进每个 CV train fold | `review_gate.py` 新增 known CV splitter 边界；scaffold train-only contract |
| [MLflow tracking](https://mlflow.org/docs/latest/ml/tracking/) | run 记录 params/metrics/code/artifacts；local file store 可用 | 作为可选 viewer；核心仍是本地 manifest，不依赖云 |
| [DVC pipelines](https://dvc.org/doc/user-guide/pipelines/defining-pipelines) | `dvc.yaml` stage DAG + `dvc.lock` data/dependency hashes | data lineage 的可选实现；manifest 仍保存输入 revision/hash |
| [Ruff flake8-bandit rules](https://docs.astral.sh/ruff/rules/#flake8-bandit-s) / [Bandit B608](https://bandit.readthedocs.io/en/latest/plugins/b608_hardcoded_sql_expressions.html) | 通用安全 shape 检查；B608 也是启发式、非完整污点流 | 安全门对照；不冒充 ML leakage/seed audit |
| [Kapoor & Narayanan, Leakage and the Reproducibility Crisis in ML-based Science](https://doi.org/10.1016/j.patter.2023.100804) | 泄漏是研究设计、数据处理、模型评估的跨层问题 | 静态门只作必要非充分证据，保留人工领域审查 |
| `light.findings.v1` / orchestrator spec | canonical producer、stage gate、checkpoint 与 back-edge provenance | stage 6 fail 原地修；7→6 仅由下游真实 root cause 建议 |

## R1 机制落地账

1. config-first + provenance → `configs/experiment.schema.json` 与 resource map 第 1–2 步。
2. gold/property/metamorphic + train-only fit → scaffold 新测试与 `experiment_contracts.py`。
3. immutable raw runs + failure preservation + lineage → `run_manifest.template.json` 与 `run_artifact_check.py`。
4. deterministic/stochastic 分型 → manifest 的 `seed.role`，固定 seed pair 与多-seed estimation 分开。
5. stdout/stderr/exact comparison → run bundle 必填日志，predictions/raw_metrics hash 真比较。
6. bounded preflight → resource map 的门序；stage-6 checkpoint 前不得交下游。
7. Round3 续补：research-plan 的 failure-tree/guardrail handoff → `experiment_execution_contract.py`
   核 `failure_tree.report_locator/report_sha256/status`、row-level `failure_tree_refs` 与 completed run 的 guardrail evidence。

## 诚实边界

- AST seed/leakage 扫描会漏报和误报；本轮 CV 漏报被真实坏实现暴露并补回归，但不等于覆盖所有框架。
- 同 seed 两次 artifact hash 一致只支持同代码/数据/config/环境的契约，不证明跨硬件绝对复现。
- Light 不提供 MLflow 式查询 UI、DVC remote、GPU scheduler 或全自主 experiment search；这些是可选外围，不是核心依赖。
- 真正独特处不是“TDD、设 seed、安全扫描、复现实验”，而是前述五件事的可执行组合与 7→6 人类决策边界。

## R3 续补：执行端消费 failure-tree / guardrail

research-plan 已新增 `failure_tree_gate.py` 后，stage 6 若仍只消费 frozen plan/matrix，就会在执行时丢掉
success/failure/inconclusive、guardrail/counter-metric、kill criterion 与降 claim 动作。本轮把它接进
`experiment_execution_contract.py`：

- `experiment_spec.failure_tree` 必须声明 `.light/failure_tree_report.json` 的 locator、SHA256 与 PASS/WARN 状态；
- failure-tree `FAIL/UNKNOWN` 阻断，`WARN` 必须有 warning decisions，否则不能 RUN_READY；
- 每个 matrix row 必须有 `failure_tree_refs`，绑定 hypothesis_ids、branch_action_ids 与适用的 guardrail_ids；
- completed run 若上游要求 guardrail，completion 必须有 guardrail evidence artifacts，不能只交 raw_metrics/predictions。

边界：这证明执行端没有丢掉上游失败树和守护指标；不证明 guardrail 阈值科学最优，也不替代 result-analysis 对结果的解释。
