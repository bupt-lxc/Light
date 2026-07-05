# E2E Research Demo：从问题到交付的一条完整链路

> This is a reproducible synthetic demo. It is designed to show the Light Skills workflow, not to claim a real scientific finding.

这个示例展示一个用户进入 Light Skills 后最关心的事情：它到底怎么把“一个研究/产品想法”推进成可检查的交付物？

场景是一个合成项目：评估一个“研究助手工作流”是否能提升用户在文献阅读、实验复现和论文写作中的证据质量。数据是脚本生成的，不对应真实受试者、真实论文或真实产品效果。

## 你会看到什么

- `data/synthetic_experiment.csv`：可复现实验数据。
- `figures/research_figure_gallery.png`：九宫格科研图廊；每个 panel 使用独立合成数据，图面不写工具名。
- `figures/panels/`：九宫格的 9 个单图 panel，其中一部分由 Python/matplotlib 生成，一部分由 R/ggplot2 生成。
- `artifacts/light_e2e_case.md`：把 Light Skills 的 23 个技能如何接力写成一个端到端案例。

## 一键复现

Windows PowerShell：

```powershell
cd examples\e2e-research-demo
$env:PYTHONUTF8="1"
python scripts\run_demo.py
```

如果机器上没有 R 或没有 `ggplot2` / `scales`，脚本会明确提示；不会把降级结果伪装成 R 图。

## 这条链路对应哪些技能

1. `light-orchestrator`：问清目标、阶段、交付门和授权点。
2. `light-literature-search`：做关键词、证据地图和相关工作边界。
3. `light-idea-generation` / `light-idea-critique`：生成并严审可验证 idea。
4. `light-research-plan`：把 idea 变成实验设计、指标和最小可验证版本。
5. `light-data-engineering` / `light-experiment-coding`：生成、清洗、记录和复现实验数据。
6. `light-result-analysis` / `light-figure`：分析效应、负结果、稳健性，并程序化出图。
7. `light-paper-writing` / `light-citation` / `light-typesetting`：写作、引用真实性和投稿前格式检查。
8. `light-frontend-design` / `light-system-design` / `light-patent-disclosure` / `light-software-copyright`：如果项目要做成 demo、系统或 IP 材料，继续接力。
9. `light-memory-pm` / `light-file-reading` / `light-consistency` / `light-research-ethics`：跨阶段常驻护栏。

## 诚实边界

- 这里的图表是展示 Light Skills 工作流能力的合成样例，不是论文结果。
- 如果你把这个示例改成真实项目，`light-citation` 必须重新核验每条引用；`light-research-ethics` 必须检查真实数据和人类受试者风险。
- 图表可以作为视觉和流程参考，但真实研究需要你自己的数据、方法和统计假设。
