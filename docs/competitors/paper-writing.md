# paper-writing Round 2 对标真相源

> 核验日：2026-07-02。GitHub star 来自当天 API，均标“整仓”；commit 为核验时仓库 HEAD。逐项读取真实 `SKILL.md` 与可用的配套 reference/script，不把写作产品、论文、博客或 alias 计入同类名额。
>
> 结论先说：旧表把 Writefull、Paperpal、CARS、Hyland、Boutron、SciFact、venue guidance 与真 skill 混列，又声称“没有一个竞品做 claim 绑定”，结论过满。Round 2 找到的 GapForge 已有真实 claim-use → evidence locator / result artifact 追踪，Nature-Paper-Skills 也明确做 claim-to-evidence map。Light 的诚实差异化应重述为：**result-analysis 统计证据档 + 逐 claim 写作绑定 + canonical findings/checkpoint + 8→7/8→6 回炉 + 下游交接**的组合，而不是“只有我想到 claim-evidence”。

## 0.A 真同类 agent skill（8 个）

### 1. NousResearch/hermes-agent · research-paper-writing

- Star：**207,280（整仓）**。
- 复验点：`skills/research/research-paper-writing/SKILL.md`，commit `2f7c51a3e2d270bda2f519b521b6b3b2cc17330f`。
- 真做写作：L62–68 定“单一贡献、实验服务 claim、git 记实验史”；L140–147 先定 What/Why/So What；L356–370 显式 Claim→Experiment→Expected Evidence 表；L778–823 从实验日志与上下文包进入 section drafting；L740–774 有 critic/author/synthesizer/judges 迭代。
- 配套资源：同目录 `references/{checklists,reviewer-guidelines,writing-guide,citation-workflow,experiment-patterns}.md` 与多 venue LaTeX templates；无独立 claim gate 脚本。
- 可借机制：**写前冻结一句话贡献 + claim→实验预期证据表**，而不是 prose 写着写着发明贡献。
- 对 Light：Hermes 的全研究周期、上下文压缩与 reviewer loop 更完整；Light 的优势是统计档、逐 claim critical findings 和 DAG 回炉。Light 旧版用全局最高证据档，反而在 claim 绑定上名实不符，Round 2 已修。

### 2. K-Dense-AI/scientific-agent-skills · scientific-writing

- Star：**29,764（整仓）**。
- 复验点：`skills/scientific-writing/SKILL.md`，commit `1e024ea8547ada12039edbe8197aaa959d97763f`。
- 真做写作：L14–18 规定 literature-backed manuscript 与“outline→full prose”两阶段；L128–176 定 IMRAD section contract；L265–304 把每节 main arguments/findings/data/citations 先列成 outline；L608–635 给完整 manuscript sequence。
- 配套代码：`scripts/generate_{image,schematic,schematic_ai}.py` 服务图，不验证 claim；写作方法在 `references/{imrad_structure,writing_principles,reporting_guidelines}.md`。
- 可借机制：**section outline 必须列 data points / statistics / citations，再转 prose**。
- 对 Light：K-Dense 的跨学科 reporting guideline 与 section 教程更宽；Light 不应照搬其“每篇都必须 AI 图”的扩张规则，且要保持 figure 专属边界。Light 的 claim gate 更硬，但资源说明旧版更碎。

### 3. Imbad0202/academic-research-skills · academic-paper

- Star：**35,747（整仓）**。
- 复验点：`academic-paper/SKILL.md`，commit `96e4f98b6e7a8b59be3f062bf854b0499e02b092`。
- 真做写作：L40–44 明确 architecture→claim-evidence argument→section drafting；L122–138 产 Paper Outline + Evidence Map，并设用户确认与最大两轮 review；L420–446 要求 claim 有 citation/own data、五维 reviewer、未决项进 limitations。
- 配套代码：`scripts/ars_anchorize_draft.py` + `ars_apply_revision_patch.py`；SKILL L324–333 描述稳定 block ID/hash、stale hash 整包拒绝、未触碰 block 字节保持，测试文件同目录存在。另有 12 agents、contracts、templates、examples。
- 可借机制：**revision patch 的稳定 anchor + fail-closed apply** 很硬，但超出本轮最小范围；本轮借其“outline/Evidence Map 先于 draft”的契约思想。
- 对 Light：该仓库的流程、模式与 revision safety 显著更成熟；Light 的优势是科研 DAG 的 stage-8 canonical findings 和统计证据桥。旧表把它漏掉是实质性失误。

### 4. labarba/sciwrite · sciwrite

- Star：**743（整仓）**。
- 复验点：根目录 `SKILL.md`，commit `8a57fa73d541bdcf7d8501db61c018cb454e9afa`。
- 真做写作：完整 manuscript/section review，按 Pass 1 organization、Pass 2 voice/verbs、Pass 3 concision/clarity 输出带 locator 的问题；要求数值/百分比与 tables 对齐，并在 L240–244 明确不擅改科学内容、保留作者声音。
- 配套代码：无；只有 `SKILL.md`、`HOW-TO-USE.md`，所以是可调用 rubric skill，不是确定性门。
- 可借机制：**review 输出按 pass 分层，先结构再 voice，且每条建议定位到 span**。
- 对 Light：sciwrite 的微观写作 review 更集中、更克制；Light 有机读门与 provenance，但旧 `style_fingerprint` 只能统计表面特征，不能自称完整保护作者声音。

### 5. hanlulong/econ-writing-skill · econ-write

- Star：**427（整仓）**。
- 复验点：`.claude/skills/econ-write/SKILL.md`，commit `d2a57f05948c4fd87dbec91cd00d761b761db926`。
- 真做写作：L22–26 锁单一贡献并要求具体系数/量级；L81–121 规定 introduction 的 hook→question→results→literature/value-added；L382–426 区分 main/null/robustness/mechanism 并禁止无识别的因果；L460–474 要求引用核对、可复现目录、每表/图映射程序。
- 配套资源：`identification-strategies.md`、`review-checklist.md`、`specialized-tasks.md`、`latex-tips.md`；无执行脚本。
- 可借机制：**null result 正面、具体、带 CI/power 地叙述；mechanism 必须测试 channel 而非猜**。
- 对 Light：经济学 section/identification 细节更深；Light 更通用且能机读绑定。Light 资源图应显式吸收“结果与讨论分工、null/negative 不藏”。

### 6. Runchuan-BU/BioClaw · bio-manuscript-pipeline

- Star：**389（整仓）**。
- 复验点：`container/skills/bio-manuscript-pipeline/SKILL.md`，commit `a79b8c4aa585c9af9c9f654528ed982be3e84c44`。
- 真做写作：L85–180 从结构化研究输入建 manuscript plan；L208–309 要求 figure 变更立即同步 Results、每个 task/main claim 对应 Figure 与 Results section；L312–426 进行 editor/computational/biological 三 reviewer 多轮 refine；L467–521 固化输出目录和 review log。
- 配套机制：由 sibling skills `bio-manuscript-text`、`bio-manuscript-refine`、`bio-human-feedback` 等阶段消费工件；主 skill 自己不含 runtime dispatcher，L10–13 诚实说明须逐阶段显式调用。
- 可借机制：**figure/Results 双向同步表 + reviewer 分角色回合日志**。
- 对 Light：BioClaw 在生物稿件与图文联动更强；Light 本轮不越界画图，只把 claim/data/evidence requirements 交 figure。

### 7. Boom5426/Nature-Paper-Skills · manuscript-optimizer

- Star：**338（整仓）**。
- 复验点：`skills/core/manuscript-optimizer/SKILL.md`，commit `44cff42ac22a5ac4dcfb7ba01b2e81c21d689ea6`。
- 真做写作：L32–41 强制 direction→logic→visual evidence→terminology→language；L85–117 从 abstract/introduction/discussion 抽 substantive claims，逐条指 exact result/figure/table/supplement，标 fully/partially/not supported；L98–104 做 reverse outline；L119–128 做五维 adversarial self-review。
- 配套 skill：`paper-workflow` L14–50 先冻结 current story/supported findings/unresolved decisions/figure list，再路由 optimizer/results revision/citation/submission；无确定性代码。
- 可借机制：**reverse outline 的 paragraph job + evidence + transition relation**，小而硬，且与现有脚本不重复。
- 对 Light：它的结构诊断与 figure-text sync 更成熟；Light 的优势是可执行 findings/checkpoint。Round 2 将 reverse-outline 作为人判工件写入 claim/argument plan 参考。

### 8. Ostailor/gapforge · claim-traceability

- Star：**0（整仓）**；star 低不等于不是真同类，代码与测试可复验。
- 复验点：`skills/claim-traceability/SKILL.md`，commit `d31a3ba5f3fd4bdab1f780c3fb9b4b4cc7bc4def`。
- 真做写作：SKILL L8–31 要每个 nontrivial claim 可审计，输入含 evidence locator/result artifact/limitation，且 no result claim without artifact、no SOTA without benchmark+leaderboard。
- 配套代码：`src/gapforge/api.py` L1202–1274 的 `draft_manuscript()` 接收 `claim_id/claim_text/use_type/support_status/evidence_locators/citation_keys`；L1312–1319 调 traceability auditor。`src/gapforge/manuscript/traceability.py` L47–68 逐 claim 统计 unsupported；L109–203 分别查 basic trace、result artifact、SOTA、pilot/smoke、novelty、citation；L208–228 查隐藏 limitation。
- 可借机制：**claim-use 记录必须带 evidence locator / artifact ID，并把 hypothesis/speculation 显式标注**。这是本轮 per-claim binding 的最近公开实现锚。
- 对 Light：GapForge 的 artifact-backed manuscript traceability 比 Light 旧版“取整份最高档”更名实相符；Light 的统计档、`light.findings.v1`、checkpoint 与 8→7/8→6 更紧，但只能在修复后这样说。

## 0.B 机制锚（不占同类名额）

- Writefull / Paperpal / Grammarly / LanguageTool / Overleaf：产品或通用语言工具，只用于理解语言层、隐私、配额、协作边界。
- Swales CARS、Hyland hedge/booster、Boutron spin、SciFact：论文/理论/数据集，是机制依据，不是 agent skill。
- NeurIPS / ACL / ICLR / CVPR author/reviewer guidance：venue 当年规范，不是 skill；必须按目标 venue 现查，不能硬编码成永久事实。
- CRediT、COPE、ICMJE、EQUATOR：作者贡献、出版伦理与 reporting guideline 权威源，按适用范围使用。
- 公开优秀论文、OpenReview review/rebuttal：学习结构和 reviewer concern，不复制措辞、不当证据来源替代品。

## 0.C 横向机制提炼

| 机制 | 真同类覆盖 | Light Round 2 取舍 |
|---|---|---|
| 先锁一句话贡献/argument，再写 prose | Hermes、econ-write、Imbad | 纳入六步资源流；planned/post-hoc 分开 |
| claim→experiment/evidence map | Hermes、Imbad、Nature optimizer、GapForge | 落为 `light.paper_claims.v1`，逐 claim evidence ID |
| section outline→full prose | K-Dense、Imbad | section contract 写入资源图 |
| reverse outline | Nature optimizer | 写入 `references/claim_argument_plan.md`，人判为主 |
| Results/Discussion 分工、null/negative | K-Dense、econ-write | 明确观察、解释、替代解释与边界 |
| reviewer loop | Hermes、Imbad、BioClaw、Nature optimizer | soundness/significance/originality/clarity + reverse outline |
| figure/text 同步 | BioClaw、Nature optimizer | 只交 figure requirements，不越界绘图 |
| author voice / 修改边界 | sciwrite、Imbad、econ-write | style fingerprint 降格为表面统计；科学内容不由 polish 改 |
| artifact/provenance | Hermes git log、GapForge artifact IDs | claim plan 保留 artifact/run/commit/hash，缺什么就标缺 |

### 本轮落地的“小而硬”机制

借 GapForge 的 claim-use/evidence locator、Nature optimizer 的 exact-support map / reverse outline，以及 econ-write 对 null result / mechanism / causal language 的硬边界，新增：

1. `scripts/claim_binding.py`：`draft_sha256 + claim_id + 精确 text + locator + evidence_claim_ids + source_locators`；
2. 修稿后旧 `draft_sha256`、未登记强断言、未知 evidence ID、只绑定 `none` → `claim_evidence` critical；
3. overclaim 只对该 claim 自己的 evidence grade 判；
4. `source_locators` 缺失 → `claim_traceability` warn，不扩 blocking 面；
5. `argument_contract.py`：`claim_type + paragraph role`，对 causal/mechanism/null/post-hoc 的设计、测试、精度/功效和披露缺口 fail closed；
6. Round 3 续补：实证 claim 必须在 claim plan 中携带 result-analysis `light.result_card.v1` 的 locator/SHA-256、`decision=CLAIM_READY`、
   `language_strength` 与 `guardrail_summary`；guardrail `FAIL/UNKNOWN` 或 `WARN` 未写 limitations 会被 `result_card_guardrail` 阻断；
7. `draft_lint --claim-map` 复用同一绑定。

这直接修复旧实现的 critical 漏报：claim A 的 strong evidence 不再能放过 claim B 的无证据 SOTA/因果/显著提升断言；result-analysis
的 guardrail/counter-metric `claim_impact` 也不能在写论文时丢掉。

## Light 的诚实比较

### 真优势

- result-analysis 真算 `q/effect/CI/n` 并 emit evidence strength；
- writing 侧逐 claim 精确绑定当前 draft hash、证据 ID、来源与 result-card/guardrail handoff，产 canonical `light.findings.v1`；
- stage-8 checkpoint 确定性阻断；
- 8→7 / 8→6 根因回炉与 citation/figure/ethics/consistency/typesetting 下游交接。

### 仍弱

- claim `text` 采用精确 span，`draft_sha256` 可挡旧稿绑定；但过宽 span、同义改写和 claim 边界仍需人审。
- `evidence_strength` 是统计强度，不是完整 provenance、证据真伪或 full GRADE。
- reverse outline、原创性、论证充分性、替代解释仍是人/领域专家主场。
- contribution consistency、mechanical/style 检查均为启发式；中英混写和同义改写会漏/误报。
- lint 通过不证明会被录用。

## 可复验命令

```bash
python skills/light-paper-writing/scripts/claim_binding.py --selftest
python skills/light-paper-writing/scripts/claim_evidence_gate.py --selftest
python skills/light-paper-writing/scripts/draft_lint.py --selftest
```

R1 的克隆核验只用于当次研究，不是完成 paper-writing 的运行依赖。
