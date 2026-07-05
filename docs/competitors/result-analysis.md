# result-analysis · Round 2 竞品与机制对标真相源

> 核验日：2026-07-02。star 来自当日 GitHub API，均为**整仓 star**，不是单技能 star；commit
> 固定到当日读取的 SHA。只有仓库内可发现、可调用的 `SKILL.md` 才进入 §0.A；统计库、论文、
> 规范与商业工具只进 §0.B，不拿来凑同类名额。

## 0.A 真同类 agent skill（8 个，逐份读 SKILL/配套代码）

### A1. K-Dense-AI/scientific-agent-skills · statistical-analysis

- **整仓 star / 固定版本**：29,761★；commit
  [`1e024ea8`](https://github.com/K-Dense-AI/scientific-agent-skills/tree/1e024ea8547ada12039edbe8197aaa959d97763f)。
- **精确入口**：
  [`skills/statistical-analysis/SKILL.md`](https://github.com/K-Dense-AI/scientific-agent-skills/blob/1e024ea8547ada12039edbe8197aaa959d97763f/skills/statistical-analysis/SKILL.md#L104-L143)；
  [`scripts/assumption_checks.py`](https://github.com/K-Dense-AI/scientific-agent-skills/blob/1e024ea8547ada12039edbe8197aaa959d97763f/skills/statistical-analysis/scripts/assumption_checks.py#L409-L517)。
- **它怎么真做分析**：先按 paired/independent、组数、正态性选检验（L104–130），再执行
  assumption check；配套 Python 代码真算 Shapiro、Levene、IQR/z-score 异常值并给失败后的替代建议，
  不是 README 口号。效应量、CI、power/sensitivity 与 APA 报告都有明确流程（L353–460、466–527）。
- **值得借**：假设失败后不能只报“失败”，要给 transformation / robust / non-parametric / model
  路径；把 sensitivity analysis 与低功效解释分开。
- **Light 强 / 弱**：Light 强在 BH-FDR 真重算、critical findings、证据档与 DAG 回炉；旧 Light
  弱在分析计划锁、missing/outlier/exclusion 留痕与复杂设计识别。Round 2 已借入
  `analysis_plan_audit.py` 的设计声明与事后变更审计，但不照搬“看假设结果后自动换检验”。

### A2. aj-geddes/useful-ai-prompts · statistical-hypothesis-testing

- **整仓 star / 固定版本**：282★；commit
  [`3f5182cf`](https://github.com/aj-geddes/useful-ai-prompts/tree/3f5182cfd739fc113f4af5244a1cf342ad7f7911)。
- **精确入口**：
  [`skills/statistical-hypothesis-testing/SKILL.md`](https://github.com/aj-geddes/useful-ai-prompts/blob/3f5182cfd739fc113f4af5244a1cf342ad7f7911/skills/statistical-hypothesis-testing/SKILL.md#L19-L25)；
  可运行示例在 [L27–190](https://github.com/aj-geddes/useful-ai-prompts/blob/3f5182cfd739fc113f4af5244a1cf342ad7f7911/skills/statistical-hypothesis-testing/SKILL.md#L27-L190)。
- **它怎么真做分析**：一份技能内覆盖 independent/paired t、ANOVA、χ²、Mann–Whitney、Welch、
  Levene、bootstrap CI、power、Bonferroni 与 η²；结尾列 assumption/pitfall/deliverable
  （L193–221）。
- **值得借**：把“paired 是同一对象两条件”写在调用点，而不只藏在参考文档；把 power 和 CI 作为
  交付件。
- **Light 强 / 弱**：Light 的选择、FDR 与机读交接更强；该技能的优点是小而直观。其 Bonferroni
  示例没有 comparison-family provenance，也没有 claim→run/commit 定位。

### A3. omicverse/omicverse · data-stats-analysis

- **整仓 star / 固定版本**：1,099★；commit
  [`c4fb9c0e`](https://github.com/omicverse/omicverse/tree/c4fb9c0ed228ed33d861766fce0a06feaab0da71)。
- **精确入口**：
  [`.claude/skills/data-stats-analysis/SKILL.md`](https://github.com/omicverse/omicverse/blob/c4fb9c0ed228ed33d861766fce0a06feaab0da71/.claude/skills/data-stats-analysis/SKILL.md#L7-L21)。
- **它怎么真做分析**：本地 SciPy/statsmodels 路径，真给出逐基因 FDR、Bonferroni 与 q-value 表
  （[L132–160](https://github.com/omicverse/omicverse/blob/c4fb9c0ed228ed33d861766fce0a06feaab0da71/.claude/skills/data-stats-analysis/SKILL.md#L132-L160)）；
  normality、CI、Cohen’s d、非参替代和 NaN/小样本排错均有代码
  （[L182–285](https://github.com/omicverse/omicverse/blob/c4fb9c0ed228ed33d861766fce0a06feaab0da71/.claude/skills/data-stats-analysis/SKILL.md#L182-L285)、
  [L410–452](https://github.com/omicverse/omicverse/blob/c4fb9c0ed228ed33d861766fce0a06feaab0da71/.claude/skills/data-stats-analysis/SKILL.md#L410-L452)）。
- **值得借**：FDR 输出保留 raw p、adjusted p、reject 三列；本地执行、不绑单一模型或云服务。
- **Light 强 / 弱**：Light 已有同等且更强的 BH 验证，但旧流程没有记录 `dropna`/异常值排除究竟
  改了多少样本；该技能也只是“删除 NaN”，没有 missingness 机制和敏感性分析，不能照抄。

### A4. wanshuiyin/Auto-claude-code-research-in-sleep · analyze-results

- **整仓 star / 固定版本**：12,887★；commit
  [`df6162b5`](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/tree/df6162b574fdd6836c7219fc8643666378fe143e)。
- **精确入口**：
  [`skills/analyze-results/SKILL.md`](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/df6162b574fdd6836c7219fc8643666378fe143e/skills/analyze-results/SKILL.md#L12-L46)。
- **它怎么真做分析**：定位多格式结果→表格比较→多 seed 均值±std/显著性/异常值→从 improvement、
  regression、unexpected pattern、failure mode 提炼洞察→回写实验状态。只有 47 行，但职责正中
  “实验结果→结论/下一步”，不是通用 CSV 清洗。
- **值得借**：结果分析不是统计报告终点，必须更新实验状态并明确下一步；失败模式也要留在输出。
- **Light 强 / 弱**：Light 的统计严谨远强；旧 Light 的结果文件 coverage/run manifest 接入主要靠
  提示词，Round 2 将它落进 provenance audit。该技能本身没有效应量、CI、family 校正。

### A5. Imbad0202/experiment-agent · validate mode

- **整仓 star / 固定版本**：128★；commit
  [`e291e7dc`](https://github.com/Imbad0202/experiment-agent/tree/e291e7dc7ca268b2de7e1a9cf23bc2eef5dc0651)。
- **精确入口**：
  [`SKILL.md` validate mode](https://github.com/Imbad0202/experiment-agent/blob/e291e7dc7ca268b2de7e1a9cf23bc2eef5dc0651/SKILL.md#L93-L107)；
  [`statistical_interpretation_guide.md`](https://github.com/Imbad0202/experiment-agent/blob/e291e7dc7ca268b2de7e1a9cf23bc2eef5dc0651/references/statistical_interpretation_guide.md#L19-L75)；
  [`reproducibility_protocol.md`](https://github.com/Imbad0202/experiment-agent/blob/e291e7dc7ca268b2de7e1a9cf23bc2eef5dc0651/references/reproducibility_protocol.md#L12-L54)。
- **它怎么真做分析**：DETECT→逐项解释→11 类 fallacy scan（要求报告 11/11 coverage）→可选真复跑
  → REPORT；只有实际复跑成功才可写 `VERIFIED`，否则只能 `ANALYZED`
  （SKILL L95–107）。复现协议区分 deterministic/stochastic/environment-sensitive，并分别给精确匹配、
  5% 与 10% 默认容差。
- **值得借**：能力状态必须分级，未复跑不能写 verified；fallacy coverage 要显式，不可“看起来检查过”。
- **Light 强 / 弱**：Light 的门/回边更强；旧 Light 对 provenance/coverage 的状态词不够硬。该技能
  固定 5% 容差是经验默认，不能冒充领域通用阈值。

### A6. NousResearch/hermes-agent · research-paper-writing / Phase 4

- **整仓 star / 固定版本**：207,274★；commit
  [`2f7c51a3`](https://github.com/NousResearch/hermes-agent/tree/2f7c51a3e2d270bda2f519b521b6b3b2cc17330f)。
- **精确入口**：
  [`skills/research/research-paper-writing/SKILL.md` Phase 4](https://github.com/NousResearch/hermes-agent/blob/2f7c51a3e2d270bda2f519b521b6b3b2cc17330f/skills/research/research-paper-writing/SKILL.md#L559-L701)；
  [`references/experiment-patterns.md`](https://github.com/NousResearch/hermes-agent/blob/2f7c51a3e2d270bda2f519b521b6b3b2cc17330f/skills/research/research-paper-writing/references/experiment-patterns.md#L337-L416)。
- **它怎么真做分析**：先聚合 raw JSON，再报 CI/effect size；强制回答主发现、意外、失败和待补实验；
  null result 不被抹掉；最后写 `experiment_log.md`，每个 experiment 记录 claim、setup、结果文件、图、
  surprising finding、failed experiment 和 open question。配套参考真给 McNemar、bootstrap CI、
  Cohen’s h 实现。
- **值得借**：这是本轮最有价值的 provenance 机制——写作不应重新猜 raw results，而应消费一份
  “claim→experiment→result file”桥；失败分支也进实验日志。
- **Light 强 / 弱**：Light 的 evidence contract 与 checkpoint 更硬；旧 claim 表只有统计字段，缺
  source file/run/commit。Round 2 的资源地图和 provenance audit 补这条，但不擅自写入
  `.light/consistency` canonical。

### A7. IHKREDDY/agent-skills · data-analysis

- **整仓 star / 固定版本**：0★；commit
  [`38d7a082`](https://github.com/IHKREDDY/agent-skills/tree/38d7a082af6944121336688e9ded10edb0b3e975)。
- **精确入口**：
  [`data-analysis/SKILL.md`](https://github.com/IHKREDDY/agent-skills/blob/38d7a082af6944121336688e9ded10edb0b3e975/data-analysis/SKILL.md#L69-L168)；
  inferential tests at
  [L271–323](https://github.com/IHKREDDY/agent-skills/blob/38d7a082af6944121336688e9ded10edb0b3e975/data-analysis/SKILL.md#L271-L323)。
- **它怎么真做分析**：完整 data load→missing/duplicate/type clean→descriptive/correlation/groupby→
  regression/outlier/t-test/ANOVA/χ²→Markdown report，并显式保存 processed data 与随机种子
  （L395–405）。
- **值得借**：分析前先报告 shape/dtype/missing/duplicate，产出 processed-data 定位。
- **Light 强 / 弱**：它把“缺失超过 50% 删列、均值/中位数填补、z>3 删异常值”写成通用做法
  （L69–97、286–299），没有计划锁与敏感性分析；这恰好证明 Light 必须记录 exclusion/change，
  不能为显著性自动清洗。

### A8. pluginagentmarketplace/custom-plugin-data-analyst · statistics

- **整仓 star / 固定版本**：1★；commit
  [`2150f932`](https://github.com/pluginagentmarketplace/custom-plugin-data-analyst/tree/2150f932b448b967c6ae19f79b1611d712d4097c)。
- **精确入口**：
  [`skills/statistics/SKILL.md`](https://github.com/pluginagentmarketplace/custom-plugin-data-analyst/blob/2150f932b448b967c6ae19f79b1611d712d4097c/skills/statistics/SKILL.md#L41-L86)。
- **它怎么真做分析**：是可发现的 statistics agent skill，覆盖 descriptive/inferential/regression，
  并有参数验证、observability、assumption violated→non-parametric、p-hacking→Bonferroni 的错误表。
- **值得借**：把输入验证与 observability 放在统计知识之前，失败要有机器可追的诊断。
- **Light 强 / 弱**：该技能更像 92 行课程索引，没有执行脚本、效应量/CI 交接或复现定位；Light 不学
  其深度，只借“先验证输入与运行可观测性”的顺序。

### §0.A 结论

旧审计“同类 field 稀疏、top 仅 8★”已被 2026-07-02 的真搜证否。至少存在 8 个可调用同类，
其中 K-Dense 29,761★整仓、Auto-claude-code-research-in-sleep 12,887★整仓、OmicVerse 1,099★整仓。
Light 的差异化不能再写“别人没有 result-analysis skill”，只能诚实写成以下**组合优势**：

1. 统计错误的确定性 critical 门；
2. 共享 evidence contract；
3. stage-7 findings/checkpoint 与 7→5/7→6 回炉；
4. claim→统计量→措辞上限→下游门；
5. Round 2 新增分析计划/设计/family/coverage/provenance 的 warn-only 审计。

## 0.B 机制锚（不计入 8 个真同类）

| 机制锚 | 一手入口 | Light 采用 / 边界 |
|---|---|---|
| SciPy | [`ttest_rel`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_rel.html)、[`mannwhitneyu`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.mannwhitneyu.html) | 统计算子；库不会替用户定义统计单位、family 或 claim |
| statsmodels | [`multipletests`](https://www.statsmodels.org/stable/generated/statsmodels.stats.multitest.multipletests.html) | BH/Bonferroni 真算；family 边界仍须计划/provenance |
| base R | [`t.test`](https://stat.ethz.ch/R-manual/R-devel/library/stats/html/t.test.html) | Round 2 用 base R 真跑 paired/independent cross-check；不假装高级包已装 |
| R 复杂模型生态 | `lme4` / `emmeans` / `effectsize` | 本机 2026-07-01 未安装；只列升级路径，当前不声称可执行 |
| ASA p-value statement | [ASA 官方](https://www.amstat.org/asa/files/pdfs/p-valuestatement.pdf) | p 不等于效应大小/结论概率；不显著不等于证明无效应 |
| NIST/SEMATECH | [统计手册](https://www.itl.nist.gov/div898/handbook/) | assumption/EDA 参考；不能替代领域 estimand |
| GRADE | [Cochrane Handbook](https://training.cochrane.org/handbook/current/chapter-14) | evidence contract 当前只覆盖统计强度，不冒充 full GRADE |
| Simmons / Gelman–Loken / Kerr | p-hacking、forking paths、HARKing | 解释为何 plan lock、完整 family、结果后变更留痕是必要条件 |
| 商业/托管工具 | SPSS / Stata / JMP / Prism / W&B / MLflow | 可选；不得成为完成任务前提，也不得因无账号跳过本地证据链 |

## 0.C 横向机制提炼与本轮落地

| 横向问题 | 竞品最强做法 | Light Round 2 落地 |
|---|---|---|
| 结果前先锁问题 | K-Dense 先选设计/假设；Nous 每实验先映射 claim | `analysis_plan_audit.py` 核 status/locked_at/hypothesis/primary metric/exclusion |
| 设计感知 | K-Dense 明分 paired/repeated；Nous 用 McNemar 处理同题比较 | audit 对 repeated/hierarchical/nested CV/cluster/time-series 明示“简单检验不可终判” |
| assumption 失败 | K-Dense 真脚本给替代路径 | 资源地图要求诊断→预先声明替代/敏感性；禁止为显著性自动换检验 |
| family provenance | OmicVerse 真产 FDR 表，但无 family 来源 | audit 要稳定 `family_id`、planned/reported/correction；重复 family_id 报 warn |
| coverage/provenance | Imbad 报检查覆盖；Nous 写 experiment log/result files | audit 核 expected/observed unit、raw path/hash/owner/time/run manifest/commit |
| R/Python 双路径 | 同类多为 Python；K-Dense 仅提 R/JASP 作为替代 | `r_analysis_crosscheck.R` + Python launcher 真执行 base-R paired/Welch，输出 CSV 可交叉核数 |
| negative result | Nous 明写 null/failed experiments | 资源地图要求全报告，不把 q≥阈值解释成“证明无效应” |
| 机器 / 人边界 | Imbad 区分 ANALYZED/VERIFIED | 统计门只证明必要条件；复杂设计、因果、estimand、外推仍须人判 |

### 本轮选中的“小而硬”机制

`analysis_plan_audit.py` 是 **warn-only**，不扩大 stage-7 critical 面。它机检：

- 计划是否在结果前冻结，事后变更是否诚实标 exploratory/sensitivity；
- `unit_of_analysis` / paired key / complex design 是否说明；
- comparison family 是否有稳定 ID、planned/reported coverage 与 correction；
- seed/fold/sample 是否完整，失败运行是否静默消失；
- raw result 是否带 path/hash/owner/time/run manifest/commit。

它不判“模型选得对不对”，也不把缺 provenance 伪装成统计结论错误；真正的多重比较未校正、
选择性报告、假设不支撑、不可复现仍由既有 `stat_rigor_gate.py` critical 门负责。

## R3 续补：result card 消费 guardrail evidence

research-plan 与 experiment-coding 已把 failure-tree / guardrail / kill criterion 带进计划包和 run bundle 后，
result-analysis 若只解释主指标，就会在写作前丢掉 counter-metric。续补落点：

- `result_card_gate.py` 新增 `guardrail_analysis` 必填显式字段；不适用也必须写 `required=false` 和理由；
- 适用时必须绑定 guardrail evidence locator、SHA-256 和逐项 check；
- guardrail `FAIL` 或 `UNKNOWN` 直接阻断 `CLAIM_READY`；`WARN` 只能限制性推进并要求语言/claim impact 降档；
- `templates/result-card.example.json`、SKILL 与 resource map 同步。

边界：这证明 result card 没有忽略上游 guardrail evidence；不证明 guardrail 阈值科学最优，也不替代复杂设计/因果诊断。

## 诚实边界

1. star 会变；本页数字只代表 2026-07-02 GitHub API 快照。
2. 整仓 star 不代表单技能质量；因此同时给 commit、skill 路径、代码行号和实际机制。
3. `statistical-analysis`/`data-analysis` 中有些是广义同类，但都实际命中“实验/研究结果的统计选择、
   assumption、效应量/CI、多重比较或结论报告”，不是只画图/洗 CSV。
4. Light 仍未提供 mixed-effects、GEE、cluster bootstrap、corrected resampled t、equivalence/
   non-inferiority 的统一执行引擎；复杂设计只会诚实预警并路由到合适方法。
5. `evidence_strength.json` 仍是统计强度契约，不是 full GRADE，也不是 consistency canonical registry。
