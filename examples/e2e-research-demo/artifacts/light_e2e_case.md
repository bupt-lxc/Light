# Light Skills E2E Case：一个合成研究项目如何被推进

## 0. 用户目标

用户想验证一个研究助手工作流是否能帮助研究者在三个任务中更快、更稳地形成高质量证据：

- 文献阅读：是否能更快找到关键证据与反例？
- 实验复现：是否能降低配置、复现和记录错误？
- 论文写作：是否能提升论证一致性与引用真实性？

## 1. 总控先问什么

`light-orchestrator` 不应该一上来自动狂做，而应该先问：

1. 目标是论文、产品 demo、竞赛项目、课程项目，还是内部工具？
2. 是否有人类受试者、真实用户日志或隐私数据？
3. 结果需要达到什么交付级别：探索报告、可投稿论文、可演示软件、专利/软著材料？
4. 哪些动作需要用户授权：联网检索、安装依赖、生成大量文件、调用外部服务？

## 2. 研究设计怎么落地

`light-research-plan` 把模糊目标拆成：

- 自变量：baseline workflow vs Light-assisted workflow。
- 因变量：evidence_quality_score、time_minutes、error_count。
- 分层任务：literature、experiment、writing。
- 关键风险：学习效应、任务难度不均、评分者偏差、工具熟悉度。
- 最小可验证版本：先用小样本/合成数据跑通分析链路，再进入真实实验。

## 3. 数据与代码如何保证可复现

`light-data-engineering` 和 `light-experiment-coding` 要求：

- 数据由脚本生成或从明确来源读取。
- 每个输出文件都有稳定路径。
- 图表脚本可重复运行。
- 失败时要写明缺失依赖，而不是静默跳过。

## 4. 分析与图表如何讲清楚

`light-result-analysis` 不只报“提升了”，还要问：

- 提升集中在哪些任务？
- 置信区间/不确定性有多大？
- 有没有负结果或不稳定结果？
- 是否存在替代解释？

`light-figure` 在这个示例里生成两类不同图：

- Python/matplotlib：效应量森林图，展示各任务从 baseline 到 assisted 的差异。
- R/ggplot2：时间轨迹图，展示质量分数随阶段变化的趋势。

## 5. 论文、产品与 IP 怎么接力

如果用户要写论文：

- `light-paper-writing`：组织 Introduction / Method / Results / Limitation。
- `light-citation`：逐条核验引用是否真实支持论断。
- `light-typesetting`：检查模板、编号、匿名性和补充材料。

如果用户要做产品或竞赛 demo：

- `light-frontend-design`：设计研究工作台、证据面板、进度和风险提示。
- `light-system-design`：拆 API、数据层、任务队列、权限和部署。

如果用户要准备 IP：

- `light-patent-disclosure`：梳理技术问题、方案、实施例和区别点。
- `light-software-copyright`：整理软件说明、模块、运行环境、源代码清单和材料检查。

## 6. 不能越界的地方

- 合成数据不能写成真实结论。
- 没核验的文献不能写 DOI、年份、作者或链接。
- 没有人类受试者审批时，不能把真实用户实验当作可直接发布研究。
- AI 可以提出候选创新点和验证路径，但用户需要参与关键问题定义与最终取舍。
