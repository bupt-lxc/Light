# research-plan Round 2 对标深读（R1 真同类 + 机制锚）

> 科研主线 stage 5。真同类与 GitHub star 于 **2026-07-02** 由 GitHub API 一手复核；star 是整仓
> 指标，不伪装成单 skill 使用量。所有源码锚固定到表中 commit，`main` 后续漂移不影响复验。
> 本轮纠正旧表：DVC、MLflow、论文、checklist 和功效软件不是“同类 skill”，不能顶名额。

## 0. 先核旧“独特性”

旧结论“实验设计同类 skill 近乎空，所以 Light 的计划/power 很独特”不成立。头部科研技能包已经分别做了：

- 研究问题、可证伪性、estimand/统计单位和 outcome 锁定；
- 随机化、blocking、DOE、negative/control、baseline 与 ablation；
- pilot/先验效应量、MDE、simulation-based power 和 sensitivity；
- confirmatory/exploratory 分轨、预注册、停止规则与版本时间戳；
- 资源预算、实验矩阵、逐步执行和复现实验日志。

因此，**“会写研究计划”“会做 power”“会建议预注册”“会列 baseline/ablation”都不是 Light 独有**。
在本轮审计集合中，Light 可验证的组合差异是：

> **公平对照 critical + 可证伪 critical + 功效/ablation advisory + canonical
> `light.findings.v1` + stage-5 checkpoint 真阻断 + 7→5/13→5 根因回炉落点。**

这只是对下表审计集合的比较，不宣称穷尽全网；科学有效性仍由研究者、统计专家和领域专家终判。

## 0.A 真同类 research planning / preregistration / experimental-design skills

| # | 真同类 skill | 当天 star / repo / 固定 commit | 一手代码锚 | 具体机制 | 可借进 Light | Light 的真实差距 |
|---|---|---|---|---|---|---|
| 1 | `experimental-design` | **29,869★** · `K-Dense-AI/scientific-agent-skills` · `1e024ea8547ada12039edbe8197aaa959d97763f` | `skills/experimental-design/SKILL.md:51-81,155-196`; `scripts/randomization.py:41-147`; `scripts/doe_designs.py:43-160` | 先按研究问题与统计单位选 randomized block / crossover / cluster / factorial / RSM；把 pseudoreplication 当结构性错误；脚本真生成 seeded allocation 与 DOE run order | 研究计划先锁**统计单位、随机化单位、分析单位**；将 blocking/negative control/运行顺序写入矩阵 | Light 现有模板偏 ML benchmark，对 cluster、repeated measure、pseudoreplication 和 run-order blocking 不够显式 |
| 2 | `statistical-power` | **29,869★** · 同仓 · 同 commit | `skills/statistical-power/SKILL.md:54-59,100-143,168-183`; `scripts/power.py:186-263`; `scripts/simulate_power.py:40-97` | 效应量优先 SESOI，其次收缩后的 pilot；固定 N 时算 MDE；复杂 GLM/mixed/cluster 用 simulation；输出 Monte Carlo CI；禁止 observed power | 把“一个 d→一个 n”升级为**来源 + plausible range + sensitivity**；复杂设计不硬套双样本 t | Light `power_check` 只覆盖双样本均值近似；旧文案还会把随机种子误当独立样本，容易伪精确 |
| 3 | `framing-research-questions` | **227★** · `K-Dense-AI/science-superpowers` · `3150a27c9a08c10709007243d6a29199f22c5244` | `skills/framing-research-questions/SKILL.md:12-30,79-113` | 看 outcome 前先锁 framing；给 2–3 种 association/causal、连续/阈值等表述并说明 trade-off；显式 population、unit、operationalization 与 disconfirming result | 从 idea/data feasibility 生成 question 时先给备选 framing，再由人定 estimand 与 claim 强度 | Light 原方案直接从“总目标”跳假设，缺 population/unit/estimand 的显式桥 |
| 4 | `designing-the-analysis` | **227★** · 同仓 · 同 commit | `skills/designing-the-analysis/SKILL.md:24-57,61-76,135-144` | raw→cleaned→derived→results 单向流；每个 confound 写处理策略；固定 N 算 MDE；复杂 estimator 强制 simulated ground-truth pipeline validation；关闭 researcher degrees of freedom | 把 primary analysis、exclusion、transform、comparison family 和 fallback 在执行前锁死 | Light 有复现清单但缺“每个开放分析选择必须关闭”的专门清点 |
| 5 | `preregistering-analysis` | **227★** · 同仓 · 同 commit | `skills/preregistering-analysis/SKILL.md:21-32,70-94,100-136,190-201` | LOCK→falsifier→FREEZE(commit/timestamp)→EXECUTE→SEPARATE；primary/secondary、stopping、multiplicity、deviation 全锁；窥视过 outcome 的分析只能标 exploratory | 预注册模板必须带 registry URL/ID、version/hash、冻结时点、偏离日志与 confirmatory/exploratory 分轨 | Light 旧 references 只“建议 OSF/AsPredicted”，没有可交付模板与 provenance 字段 |
| 6 | `deep-research` 的 Research Architect / preregistration | **35,833★** · `Imbad0202/academic-research-skills` · `95a7a94f225315a96d5f3fb3cf4a27a7dd058dfa` | `deep-research/SKILL.md:103-106,155-165,443-461`; `references/preregistration_guide.md:8-32,64-118`; `templates/preregistration_template.md:1-12` | Research Question Brief→Methodology Blueprint；按研究类型选择 OSF/AsPredicted/PROSPERO/clinical registry；21 项 prereg checklist 含 sample rationale 与 stopping | 资源地图按研究类型路由 registry，不把 OSF 当所有研究唯一答案 | Light 旧预注册说明不区分通用研究、临床试验、系统综述和机构注册义务 |
| 7 | `experiment-design` | **305★** · `fcakyon/phd-skills` · `1a44aeb830dcf629096863882ac142c0c44948f7` | `plugin/skills/experiment-design/SKILL.md:14-87` | 每个 ablation 单变量隔离；≤3 因素 full factorial，多因素先 sequential elimination；先算 run/GPU/storage，再生成 config 和 analysis plan | 把资源预算放到方案定型前；ablation 行声明“唯一变化”和固定项 | Light 有预算表，但矩阵没有“唯一变化”专栏，容易把联合消融误称组件归因 |
| 8 | `experiment-agent` plan mode | **128★** · `Imbad0202/experiment-agent` · `e291e7dc7ca268b2de7e1a9cf23bc2eef5dc0651` | `SKILL.md:113-126,141-169`; `templates/code_experiment_plan.md:1-45`; `templates/study_protocol.md:1-67` | Socratic 一问一答；RQ→变量/confound→design→sample/power→analysis；代码实验和人类研究用不同模板；产 Material Passport | 区分 code benchmark 与 human study，模板按设计类型裁剪而不是一张表包打天下 | Light 主模板偏代码实验；人类研究的 recruitment、IRB、instrument reliability 与 retention 只在 ethics 侧，方案侧承接不足 |
| 9 | `design-ai-experiment` | **0★** · `tenki-labs/public-claude-skills` · `62ce6be95a491602f9dbded66cc3356952fde10c` | `plugins/tenki-public-skills/skills/design-ai-experiment/SKILL.md:23-75,82-120,125-134` | 强制 X/A/B/M/T/W/G/C 假设槽；A/B、switchback、holdout、pre-post、offline 设计选择；guardrail、kill criterion、timeout；变更写 dated amendment | 成功阈值外再锁**失败/伤害 guardrail**与 stop/kill；预注册变更不能静默覆盖 | Light 只写“停止条件”，缺 primary benefit 与 counter-metric/guardrail 的成对决策 |
| 10 | `design-of-experiments` | **129★** · `lyndonkl/claude` · `8747ebc215240a873fe0a8d25eea13e9a63acbed` | `skills/design-of-experiments/SKILL.md:15-48,81-105`; `resources/template.md:24-42,352-397`; `resources/methodology.md:288-326` | screening→steepest ascent→factorial→RSM→confirmation；randomize/block/replicate；用 rubric 复核 design resolution、power、analysis | baseline/ablation 之外补 DOE 选择和 confirmation run；资源紧时先 screen 再精化 | Light 现有 ROB/SEN 行是清单，不会判断 full/fractional/response-surface 的 alias 与 resolution |

### 复验说明

- star：GitHub REST `GET /repos/{owner}/{repo}`，核验日 2026-07-02。
- commit：对每个仓库 `git rev-parse HEAD`；表中行号均来自该固定 commit。
- 读码范围：不只 README；逐个读取 `SKILL.md`，并在存在时读取 randomization/DOE/power/simulation
  脚本、analysis/preregistration reference 与输出模板。
- star 低不等于机制差。tenki 0★ 仍提供了明确 guardrail/kill/amendment 机制；按机制先进性保留，不用
  popularity 替代代码判断。

## 0.B 机制锚（不计入真同类 skill 名额）

| 机制锚 | 类别 | 一手机制 | 借进 Light 的位置 | 边界 |
|---|---|---|---|---|
| OSF Registrations | 官方注册平台 | preregistration 是 outcome/data analysis 前发布的 time-stamped、read-only 计划；提交后附件不可直接改，后续以 update/新 registration 留版本；可 embargo | `references/research-plan-resource-map.md` 的 freeze/provenance 路径；`templates/preregistration.md` 的 registry/version/hash | 免费但需登录；不能由 agent 代替用户提交；提交前必须去标识化 |
| AsPredicted | 官方注册平台 | 单页时间戳 PDF + unique verification URL；coauthor approval；公开后不可修改，变更应在论文/新版中披露 | 轻量验证性研究的 registry 备选；保留 PDF SHA256 与 URL | 免费登录；表单会变，提交当天重核；不是核心路径依赖 |
| SPIRIT 2025 / CONSORT 2025 | 试验方案/报告规范 | SPIRIT 34 项 protocol checklist；CONSORT 30 项 results checklist；outcome 须预先说明 variable、analysis metric、aggregation、timepoint | outcome registry、participant flow、harms/guardrail、protocol→report trace | 面向随机试验；非临床 ML benchmark 不机械套全表 |
| ICH E9(R1) | estimand / sensitivity 规范 | 研究目标先翻成“要估计什么”的 estimand，再让 design、data、analysis、sensitivity 与其对齐 | question→estimand→analysis 的第一步；robustness 与同一 estimand 对齐 | 临床规范提供通用结构，不替代各领域因果识别 |
| statsmodels 0.14.6 | 功效工具 | `TTestIndPower` 仅两独立样本 t；另有 paired/one-sample、ANOVA、normal/chi-square 类 | `power_check` 适用范围与降级说明 | 不能把 repeated CV seeds、患者内重复或 cluster 当独立 n |
| G*Power 3.1 | 免费 GUI 功效工具 | 多类经典检验的 a priori/compromise/sensitivity power | 无 Python 环境时人工复核 | 闭源桌面 GUI；不作为自动化核心依赖 |
| Dacrema et al. 2019 (1907.06902) | 公平比较论文 | 18 个推荐算法仅 7 可合理复现，其中 6 被简单方法打败；优化过的方法不能和未优化 baseline 公平比较 | `fair_baseline` critical 的方法学根 | 证据来自推荐系统域，原则可迁移但具体预算需领域化 |
| NeurIPS checklist | 会议透明性规范 | 报环境、超参、数据划分、误差棒/CI、代码与复现条件 | reproducibility checklist 与结果交接 | checklist 不是科学有效性的机器证明 |
| AI-Scientist-v2 / EXP-Bench | 系统/基准论文 | 分阶段 baseline→research→ablation 与显式停止；实验设计与结论是高失误环节 | 四要素矩阵与阶段停止条件 | agent 自动化不替代研究者设计判断 |

一手入口：

- OSF：`https://help.osf.io/article/330-welcome-to-registrations`
- AsPredicted：`https://aspredicted.org/`
- SPIRIT–CONSORT：`https://www.consort-spirit.org/`
- ICH E9(R1)：`https://www.ema.europa.eu/en/ich-e9-statistical-principles-clinical-trials-scientific-guideline`
- statsmodels power：`https://www.statsmodels.org/stable/stats.html#power-and-sample-size-calculations`
- Dacrema：`https://arxiv.org/abs/1907.06902`

## 0.C 横向机制提炼

1. **先定义问题与 estimand，再选设计。** 研究对象、population、统计单位、对比、outcome、summary measure、
   treatment/intercurrent-event strategy 不明确时，power 数字没有对象。
2. **设计和分析必须同构。** cluster/randomized block/repeated measure 的分配结构必须出现在模型和功效方法中；
   把 seed、fold、同一患者的多次测量当独立 n 是 pseudoreplication。
3. **功效应输出假设族，而非单点神谕。** 记录 effect-size 来源与 shrinkage，给 plausible range、MDE 或
   simulation CI；固定公开数据优先 sensitivity，不做 observed power。
4. **预注册的价值是时间顺序与分轨。** 锁 primary/secondary、comparison family、exclusion、stopping、fallback，
   冻结 timestamp/hash；新增分析仍可做，但必须标 exploratory 或 dated amendment。
5. **公平对照不仅是“同数据”。** baseline 实现、调参搜索空间/预算、训练时长、early stopping、输入信息、
   重复数和报告规则都要可比；做不到就降 claim，不可用“最新方法”标签掩盖放水。
6. **消融不是删一坨。** 每个机制声明要有单变量隔离、负对照/反事实对照、固定项和 confirmation；
   联合移除只说明组合重要，不能归因单组件。
7. **机器门只守结构和显式声明。** `plan_lint`、`power_check`、`plan_gate` 能暴露缺口并确定性阻断已声明的
   critical 问题，但不判领域合理性、因果可识别性或效应量真伪。

## 0.D R1 落地映射

| 学到的机制 | 永久落点 |
|---|---|
| question→population/unit→estimand→success/failure | `templates/research-plan.md` + `references/research-plan-resource-map.md` |
| randomization unit / analysis unit / blocking / negative control | `templates/experiment_matrix.md` |
| SESOI/pilot shrinkage + sensitivity/MDE + complex-design simulation | `SKILL.md`、`references.md`、resource map；保留 `power_check` 仅作双样本 t 工具 |
| primary/secondary + comparison family + exclusion + stopping | `templates/preregistration.md` + experiment matrix |
| registry timestamp/version/hash/deviation | `templates/preregistration.md` + resource map |
| guardrail/kill + baseline/ablation/robustness/resource budget | research-plan 与 experiment-matrix 模板；Round3 落地 `failure_tree_gate.py` + `failure-tree.example.json` |
| canonical findings/checkpoint/7→5 | 保留已验证 `plan_gate.py` / `run_checkpoint.py` / `reroute.py`，不重写 |

## 0.E 诚实差异与落后项

**Light 真正做成的组合：**

- `plan_gate.py` 把公平对照/可证伪声明转成 canonical critical findings；
- `run_checkpoint --stage 5` 对 critical 真 exit 1，而不是只给 prose checklist；
- `ablation_isolation` 与 `statistical_power` 保持 advisory，不把启发式冒充科学裁判；
- result-analysis/review-rebuttal 可按真实根因建议 7→5/13→5，且只建议，用户拍板后才落回边。

**仍然落后：**

1. 没有 K-Dense 那样的 randomization/DOE layout generator 与 simulation-power harness；
2. `power_check` 只适用双样本均值近似，不能正式 power repeated CV、cluster、mixed model、比例或生存设计；
3. `plan_lint` 不理解 estimand、因果识别或 protocol 的领域合理性；
4. OSF/AsPredicted/registry 提交需要账号和不可逆确认，Light 只生成本地注册包与 provenance，不代提交；
5. stage-5 checkpoint 覆盖 structural critical，不等于 IRB、统计师或领域专家批准。

## 0.F Round3 续补落地：failure tree / guardrail gate

复核 tenki `design-ai-experiment` 的 guardrail/kill criterion、K-Dense preregistration 的 failure/falsifier
分轨和 SPIRIT/CONSORT 的 outcome/harms 思路后，补上 Light 原先主要停留在模板层的缺口：方案不能只写“成功标准”，还必须写
“失败、无结论、质量/安全 guardrail 触发后如何停止、降 claim 或回炉”。

- 新增 `skills/light-research-plan/scripts/failure_tree_gate.py`：要求每条 hypothesis 具备
  success/failure/inconclusive 三分支，且每个分支有可量化 condition、枚举 action_kind、claim_impact。
- guardrail/counter-metric 必须声明 metric、direction、threshold、monitoring stage、kill_action 和 claim impact；
  缺 guardrail 只能给不适用理由并进入 WARN/人工决策。
- 数据后 amendment policy 必须是 `EXPLORATORY_ONLY` 或 `NEW_VERSION_ONLY`，且要求用户/PI 授权；授权态需绑定
  非未来日期与 `sha256:<64 hex>` 计划哈希。
- `research_package_gate.py` 已把 `.light/failure_tree_report.json` 纳入 final package；FAIL 不得交
  experiment-coding，WARN 必须有 `warning_decisions`。

边界：这是结构门，不判断阈值科学最优，也不替代伦理/统计/领域专家批准。
