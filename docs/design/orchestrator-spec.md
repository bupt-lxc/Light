# 总控(orchestrator)设计 spec —— Light v2 Round 2 集成真相源

> 用途:这是总控大脑的**设计唯一真相源**,供本块的对话②(确定性引擎+selftest)、对话③
> (SKILL.md 灵魂+常驻触发+E2E)无缝实现。蓝图 §5 是上位真相源;本 spec 把 §5 落到可实现的
> schema / 接线 / 判据 / 交互契约。对标依据见同目录 `../competitors/orchestrator.md`。
>
> 初稿写于批 0（2026-06-16）；Round 2 于 2026-07-03 将其升级为已实现的 v3 生命周期与
> 23 技能集成契约。`skills/light-orchestrator/references/integration-contract.json` 是角色/
> gate/route 的机读真相源；本文件解释语义。旧批 0 章节保留设计来路，若与下方 Round 2
> 规范冲突，以 Round 2 规范为准。

---

## 0. Round 2 规范（优先于后文批 0 历史设计）

### 0.1 生命周期 intake

`lifecycle.py intake` 必须把项目归入
`new|resume|partial|dirty|failed|stale|delivered`，并同时保留共存 flags：

- `dirty` 是 mutation blocker，保护 tracked/untracked 用户改动；
- `failed` 是 progression blocker，必须读 blocking findings；
- `stale` 由上游文件内容 SHA-256 变化传播到依赖闭包；
- `delivered` 不是文件存在，而是 schema/hash/checkpoint/limitation/handoff/用户决策共同成立。

### 0.2 canonical state

- `.light/passport.yaml` 是唯一 pipeline state；memory-pm 管项目卡/决策/版本/历史 handoff。
- 当前 schema 为 `light.passport.v3`；v1/v2 只经显式 `migrate` 升级。
- `state_hash` = 排除自身字段后的 canonical JSON SHA-256；每次保存增加 `state_revision`。
- `inputs_fingerprint` 哈希路径与文件字节，不用 mtime 充当内容新鲜度。
- legacy 回边无授权证据时迁移为 `authorization_id=UNKNOWN`，不得伪造。

### 0.3 三类角色

1. pipeline：stage 1–13；
2. resident overlay：memory-pm / project-structure / consistency /
   research-ethics / file-reading；
3. engineering/IP off-DAG：frontend-design / system-design / patent-disclosure / software-copyright。

project-structure 与 file-reading 同时是 off-DAG overlay；它们不产 findings。memory-pm 仅按需产
账本自洽 findings；consistency/research-ethics 可附着当前 stage checkpoint。system-design、
frontend-design、patent-disclosure 与 software-copyright 不进入 `STAGE_GATES`/`ROUTES`，不产科研 findings。

### 0.4 gate 与 findings

`STAGE_GATES` 是真实 producer/script contract，不得保留死名字。当前 key =
`2,3,4,5,6,7,8,9,10,11,13`；stage 1 是下游信号，stage 12 是用户 venue 决策点。
每个 findings producer 必须有显式 consumer；总控只聚合，不重判领域事实。

checkpoint 写回必须带 ISO-8601 时间、SHA-256、`fresh=true` 与证据态。无时间戳的
`--write` 非法。

### 0.5 route、admission hold 与授权

机读 route 只有：

- admission hold：2⊣3；它禁止进入 stage 3，不写 back-edge；
- back-edge：4→3、7→6、7→5、8→7、9→7、13→3/5/8。

`ROUTES[3]` 自指 3→3 非法并已删除。8→6 只能由用户对根因作 override，非自动规则。
reroute 永远只建议。`add-back-edge` 要求 `to < from` 和 `authorization_id`，并原子递增目标
`revision_rounds`；最多两轮，第三轮拒绝写入并要求用户选择 known limitation。

### 0.6 evidence state、resident 与 recovery

全仓总控证据只用 `VERIFIED|PLANNED|UNKNOWN|UNAVAILABLE|FAILED`。
SessionStart 常驻预算为 discipline 4200 + resume 5400，总上限 9800 字；超限降级到
SKILL/passport 指针。Claude Code 触发为 harness 强制；Codex/OpenCode 调同一 resume 实现，
但触发靠 instruction/model-read，不能宣称同等自动。

handoff 只保存 passport hash、intake、blocker/limitation 与一个 next action。resume 先
`verify-handoff`；hash 变化即 stale，回 canonical passport 恢复。

最终交付只允许通过 `passport.py authorize-delivery`：全部已选 stage 必须
`delivered + VERIFIED`，无 stale/incomplete，且命令必须带用户
`authorization_id`。已知限制随授权写入；文件存在或局部 stage 完成不能触发该转移。

### 0.7 免费核心与受限资源

核心只依赖本地项目文件、Git、Python stdlib、passport/findings。公开免登录资源可增强事实核验；
登录、机构、付费资源只能是可选覆盖，缺失标 `UNAVAILABLE`，不得阻断本地核心或伪装成“没有”。

---

## 1. 院士级深挖(铁律 9):统筹一个科研项目,专家群体真正需要总控做什么、最怕它在哪自作主张

> 不是教科书"先调研再实验"的流程罗列,是"一屋子院士统筹这个项目时,会争论什么、坚持什么、
> 最怕 AI 在哪替他们拍板"。这决定了总控的能力边界与"何时停下问人"。

### 1.1 院士群体真正需要总控做的 8 件事(超出裸模型默认)

1. **"现在到底在哪"要有证据,不靠记忆。** 长项目最大痛点是丢线:啥做完了、啥验过了、啥
   卡住了、啥已陈旧。总控的价值是**证据锚定的状态**(git / passport / 门结果 / CI),不是
   "我觉得到第 X 步了"。→ 落:断点恢复探针 + passport 台账 + stale-check。

2. **守住不可逆/高代价决策,并让人来拥有它。** 院士最怕自动驾驶把他们绑死在:一个研究方向
   (押上几个月)、一个其实撞车的 idea 过审、投错 venue(重投=数月)、带着数据泄漏/过度宣称
   发表(被撤稿=声誉灾难)。**这些恰是要停下问人的点**,总控绝不自动冲过。

3. **抓单阶段专家看不到的跨阶段陷阱。** 最深的价值不在做好某一步,而在看见**接缝**:这 idea
   其实是"换个数据集的纯增量";这图把不显著结果当主图;论文里这条 claim 没有实验支撑;数据
   撑不起这 idea 要的统计功效;baseline 放了水。院士群体争的正是这些跨切问题。→ 落:主动诊断
   (**只提示+问,不自主拍板**——因为"判定是不是纯增量"本身就是 AI 易错的判断)。

4. **诚实于证据强度,绝不让润色跑赢证据。** 院士最硬的纪律:**措辞强度必须匹配证据强度**。
   总控要把 claim↔证据绑定(消费 `_shared/evidence_contract`),拦住写作过度宣称。这正是
   AI-Scientist 翻车处(不能自评)——所以总控用**机读门 + 用户确认**,不靠自夸。

5. **可证伪 + 对照公平 + 消融隔离。** 院士必问:实验能否证伪你的假设?baseline 公平吗(没放
   水)?消融能干净隔离贡献吗?总控要把这些路由进 research-plan 的门,不让项目在"作弊对照"上
   推进。

6. **按根因回炉,不是"重来一遍"。** 拒稿时院士先诊断根因:是创新性问题(→idea)、实验问题
   (→方案)、还是写作问题(→写作)?总控的回边必须**按根因定向**,且**有返修配额**(不无限
   反复刷)。

7. **数据可行性前置于 idea 定稿。** 院士会枪毙"数据根本不够/不可得/质量差"的 idea。总控要把
   数据可行性门**前置到 idea 定稿之前**(回边:数据不够 → 拦在 idea 前)。

8. **跨会话/跨人无缝接续。** 真实项目跨数月、多人/多 agent。总控要让交接零成本(passport +
   交接卡),且**绝不重做已验证/已提交的阶段**(stale-check 给最小重验范围)。

### 1.2 院士群体最怕总控自作主张的 8 件事(= NEVER 红线的来源)

| # | 最怕它自主做的事 | 为什么是红线 | 总控该怎么做 |
|---|---|---|---|
| a | **替你定研究方向 / 定稿 idea** | 这是科研的智识内核,押上数月 | 给推荐+理由+备选,**停下问你**(决策点) |
| b | **自称"门过了/这步完成了"**(尤其诚信门) | AI 不能自评(多篇证实) | 必须**机读闸门 exit code + 用户确认**,不口头说 |
| c | **静默回炉/丢弃成果,或静默带病冲过失败门** | 两头都隐瞒了关键判断 | 两者都**浮出来问你** |
| d | **以你的名义过度宣称** | "证明">"暗示"=声誉风险 | 措辞绑证据强度,过度即拦 |
| e | **替你选 venue / 直接点投稿** | 不可逆、战略性 | 停下问你 |
| f | **编造填空**(造引用/数字/结果) | 不可逾越底线 | 写"待核查/GAP",**绝不编** |
| g | **把"判断"当"事实"**(如断言"这 idea 新") | AI 在新颖性/显著性判断上易错 | 主动诊断措辞="我怀疑 X、值得核,**你定**" |
| h | **覆盖你未提交的改动 / 无授权副作用** | 难撤销 | 先读 diff 辨来源,副作用先确认 |

### 1.3 一句话提炼

> 院士要的不是"更快的全自动总指挥",是一个**像顶尖 mentor 一样、在对的地方停下来和你一起想、
> 帮你看见盲区、把不可逆决定权留给你**的总控;它把"AI 结构性不擅长的判断(自评/新颖性/显著
> 性)"一律降级成"机读门 + 问你",把"确定性的脏活(读状态/跑门/聚合/记台账)"自己干净利落做掉。

---

## 2. 决策 H 交互契约(本块的灵魂):ASK / ACT / NEVER

> 总控每个动作前先归类:这是该**问你**、该**自己做**、还是**绝不自主**?这张表是 SKILL.md
> 的脊柱,也是对话③写正文时的判据来源。

### 2.1 ACT —— 确定性执行,自己做(不烦用户)
- 读项目状态(git/passport/todo/CI)、跑断点恢复探针、算输入指纹、stale-check。
- 跑各阶段机读闸门(run_gates 聚合 findings)、出 PASS/FAIL 报告。
- 生成阶段产物草稿(交给对应技能)、把产物落盘到约定路径。
- 派**只读**核实(铁律 1:写代码不靠 agent)。
- 写台账:**默认 dry-run 预览**;真正 `--write` 落盘属"对台账动手",需一次显式授权(见 §4)。

### 2.2 ASK —— 停下来问你,给「推荐 + 理由 + 备选」(决策点)
- **方向选择**(调研后:走哪个方向)。
- **idea 定稿**(审 idea 后:放行哪个 / 回炉重提)。
- **方案定型**(research-plan 后:可执行?对照公平?)。
- **回炉决策**(任一门 Critical fail:回哪个根因阶段 / 带病推进并记录 / 转已知局限)。
- **venue 选择 + 是否投稿**(不可逆战略)。
- **输出格式等不可逆/有副作用动作**(LaTeX/Word、提交、推送、删除、覆盖未提交改动)。
- **主动诊断发现的盲区**(§7):带"怀疑+证据+建议拉哪个技能",问你定。
- 问法纪律:**简明列选项 + 每项后果**,先给推荐和理由,不长篇分析后替你下结论。

### 2.3 NEVER —— 绝不自主(§1.2 的红线,SKILL 标 NON-NEGOTIABLE 且独立成节)
- 绝不替用户定方向 / idea / 结论 / venue。
- 绝不自称门过(诚信门必须机读 + 用户确认),绝不口头"我检查过了"当证据。
- 绝不编造填空(造引用/数字/结果)——写"待核查/GAP"。
- 绝不把判断当事实(新颖性/显著性判断一律降级为"建议核实")。
- 绝不静默回炉、绝不静默带病推进。
- 绝不覆盖未提交改动 / 无授权做难撤销副作用。

---

## 3. 科研项目状态图(DAG):schema 与规范模板

### 3.1 节点(stage)= 13 条主线技能(按需裁剪,非每次全跑)
1 literature-search · 2 data-engineering · 3 idea-generation · 4 idea-critique ·
5 research-plan · 6 experiment-coding · 7 result-analysis · 8 paper-writing ·
9 figure · 10 citation · 11 typesetting · 12 venue-matching · 13 review-rebuttal。

> 5 个常驻技能(memory-pm / project-structure / consistency / research-ethics / file-reading)
> **不是 DAG 节点**,是横切 overlay:consistency=跨阶段一致性门、research-ethics=红线门,挂到
> 各确认点;memory-pm=台账归属;不进 pipeline 序列。

### 3.2 节点状态(v2 显式化,新增)
`not_started`(未开始)/ `in_progress`(进行中)/ `delivered`(已交付:有 artifacts)/
`gate_failed`(门未过)/ `needs_rework`(被下游按根因打回)。
- v1 靠 artifacts+gate 隐式推断,v2 把 `status` 落成显式字段 + 可由(artifacts 存在性 +
  gate.result + 是否有指向它的未消解回边)派生校验,二者冲突即 WARN。

### 3.3 边
- **依赖边(forward)**:`depends_on:[序号]`(v1 已有,拓扑序校验、环检测、并行 DAG 已实现)。
  规范前向边:1→{2,3}、2→3、3⇄4、4→5、5→6、6→7、7→{8,9}、8→{9,10}、9→11、10→11、11→12、
  12→13。(9 figure ∥ 10 citation 为并行段,皆汇入 11。)
- **回边(back-edge,v2 升为一等公民,新增)**:不是计数器,是**带类型的 rework 记录**:
  `{from, to, root_cause, evidence_ptr, round, by:user, at}`。规范回边(根因路由表见 §5)。

### 3.4 passport schema 增量(对话②实现:port v1 passport.py + 下列扩展)
v1 已有且**保留**:`project/pipeline/created/updated/current_stage`;stage 的 `stage/skill/
input/output/artifacts/depends_on/inputs_fingerprint/gate/gaps/round/revision_rounds`;DAG
拓扑校验 + 环检测 + fingerprint + stale-check + revision_rounds 防刷新 + mini-YAML 降级。

v2 **新增字段**:
- stage 级:`status`(§3.2 枚举)、`back_edges:[{from,to,root_cause,evidence_ptr,round,by,at}]`
  (本阶段作为回炉目标收到的回边记录)、`node_kind`(默认 `pipeline`;为将来扩展留)。
- 顶层:`dag_template`(可选,记本项目裁的链 id,便于汇报)。
- schema 版本:passport 自身打 `schema: light.passport.v2`,校验器认 v1→v2 迁移(缺 status 时
  从 artifacts/gate 派生,不硬报错)。

> **接线纪律(铁律:复用不重造)**:v1 passport.py 近乎原样搬;**唯一硬改 = 接新 `_shared`**。
> v1 run_checkpoint.py 里 `sys.path.insert(.., "..","..","_shared")` 是硬编码脆点;v2 一律用
> `_shared/README.md` 的规范 bootstrap(向上走目录树找仓库根),三 harness/全局安装/任意嵌套
> 都可靠。

---

## 4. 质量门台账:消费 `_shared`,把"确认点"落成可执行闸门

### 4.1 接线(对话②实现:port v1 run_checkpoint.py + 接新 `_shared`)
- 各技能闸门产出机读 `light.findings.v1`(`FindingsReport`)。总控**不读 prose**,只:
  - `report.verdict` → 判定 `pass/warn/fail`(`compute_verdict`:任一 critical fail→fail)。
  - `report.blocking_gates()` → 拿到构成阻断的 gate 列表 → **定位回炉根因**(§5)。
  - `gate_runner.run_gates([...], artifact, producer="orchestrator", target=...)` → 聚合多门
    成一份报告;**gate 抛异常不静默**,转 critical fail。
- 写回 passport:`gate.result(PASS/WARN/FAIL/FAIL→PASS)` + **新鲜证据指针**(sha@ts,证明该
  verdict 来自这次具体输出)。**Critical fail → 退出码 1,确定性阻断推进。**

### 4.2 各阶段 Critical 判据(来源:隐患论文 2509.08713 的按阶段 pitfall 表 + 蓝图 §4.3)
> 这是把"论文里的呼吁"变成"机读阻断门"的判据清单。各门的**实现**归各技能(批 1+),总控只
> **聚合+判定+按根因回炉**;批 0 总控自带合成 gate 用于 selftest/E2E。

| 阶段 | 确认点 Critical(阻断) | 主要 warn | 消费的 `_shared` |
|---|---|---|---|
| data-engineering | **数据泄漏**(标准化早于划分/时序穿越/实体重叠/目标编码穿越) | 划分不合理、样本量不足 | findings |
| idea(3⇄4) | **撞车/无创新**(fatal flaw 一票否决) | 伪缺口、夸大重要性 | semantic_sim(撞车)+findings |
| research-plan | 对照不公平、不可证伪 | 消融不隔离 | findings |
| experiment-coding | **数据泄漏**、不可复现(种子不全) | 浮点==断言 | findings |
| result-analysis | **统计错误/p-hacking** | 过度解读、效应量缺失 | evidence_contract+findings |
| paper-writing | **claim 无证据(诚信门)** | 贡献三处不一致、过度宣称 | evidence_contract+findings |
| citation | **幻觉引用/查无此文(诚信门)** | locator 不支撑、格式 | findings |
| figure | 不诚实(截 y 轴/双 y 轴伪相关) | 误差棒缺失、集合超预算 | visual_qa+findings |
| typesetting | 编译报错、desk-reject(页数/双盲) | 警告 | findings(命令门) |
| 跨阶段 | consistency 术语/指标/创新点不一致 | —— | findings |

### 4.3 返修配额(防刷新,v1 已有,保留)
- 同阶段最多 **2 轮整体返修**(`revision_rounds`),**跨会话从台账读已用轮次,不重置**(否则
  中断再续就能刷新绕过)。2 轮后仍 Critical → **转 known_limitations 如实记录 + 告知用户**,
  不假装修好。ResearchAgent 的"~3 轮收敛、再多递减"佐证此设计合理。

---

## 5. 反馈回边规则:按根因定向回炉(总控的非线性智能核心)

> 触发:某确认点 `verdict==fail`。总控用 `blocking_gates()` 拿到阻断 gate,**映射到根因阶段**,
> 提出回边 → **这是决策点,停下问用户**(回哪 / 带病推进 / 转已知局限),不自动回。

| 触发(阻断 gate / 事件) | 根因阶段 | 回边 | 回炉带什么 |
|---|---|---|---|
| idea-critique 撞车/无创新 | idea-generation | 4→3 | 具体缺口 + 最像的前作 |
| data-engineering 数据不够 | (拦在 idea 前) | 2⊣3 | idea-generation 前置读 data verdict,不够则先补数据/改 idea |
| result-analysis 不可复现/bug | experiment-coding | 7→6 | 失败的复现证据 |
| result-analysis 结果不支撑假设 | research-plan | 7→5 | 哪条假设没撑住 |
| paper-writing claim 无证据 | result-analysis / experiment-coding | 8→7 / 8→6 | 哪条 claim 缺哪种证据 |
| figure 把不显著当主图/图文不一致 | result-analysis | 9→7 | 该图对应的证据强度 |
| review-rebuttal 拒稿·创新性 | idea-generation | 13→3 | 审稿人创新性质疑原文 |
| review-rebuttal 拒稿·实验 | research-plan | 13→5 | 审稿人实验质疑 |
| review-rebuttal 拒稿·写作 | paper-writing | 13→8 | 审稿人表述质疑 |

- 回炉前检查 `revision_rounds`:到上限则**不再自动提议回炉**,改提"转已知局限",问用户。
- 回边落 passport 的 `back_edges`(带 root_cause + evidence_ptr),供 consistency 回扫与审计。
- **对话②要实现的"根因路由"** = 一个纯函数:输入一份 fail 的 `FindingsReport`,输出
  `[(root_cause_stage, reason, evidence_ptr)]` + 配额检查结果;不替用户执行,只产"建议回边"。

---

## 6. 确认点 / 决策点 分类(两类闸门,都不可静默跳过)

- **决策点 🧑(用户选分支)**:§2.2 ASK 列表。呈现=选项+每项后果+推荐理由。**不替用户决定。**
- **确认点 ✓(机器先验+用户确认)**:§4。机读门出报告 → Critical fail 默认阻断 → 用户确认/
  授权 FAIL→PASS(记 notes)→ 推进。轻任务(单技能闭环)不设显式确认点,常驻门照常后台跑。

---

## 7. 主动诊断(只提示 + 问,绝不自主拍板)

总控扫描跨阶段盲区,命中即**带"怀疑 + 证据 + 建议拉哪个技能"问用户**,NEVER 自己判定:
- "这 idea 可能是换数据集的纯增量" ← idea 与最近邻前作的 semantic_sim + delta 分解(批 1
  literature-search/idea-critique 供数据;批 0 总控先留接口 + 合成演示)。
- "这图把不显著结果当主图" ← figure 的 visual_qa + result-analysis 的证据强度。
- "这条 claim 没有实验支撑" ← evidence_contract 绑定缺口。
- "数据撑不起这 idea 要的统计功效" ← data-engineering 样本量门。
- "baseline 可能放水" ← research-plan 对照门。
> 措辞模板:"⚠ 我怀疑 <X>,依据 <证据指针>。建议拉 <技能> 核一下。**要不要这么做?**(你定)"

---

## 8. 常驻触发方案(三 harness;评估搬 v1,对话③落地)

> 目标:每次会话开头,总控**自动读项目状态 → 主动汇报"上次断哪 / 卡哪个门 / 下一步建议"**,
> 用户零成本接续。机制核实(记忆已查证):Claude Code 技能只有"/调用"和"description 概率匹配"
> 两种触发,常驻=愿望非保证 → 必须 hook + CLAUDE.md 双保险。

- **Claude Code**:`SessionStart` hook(port v1 `session_start_resident.py`,改 v2 的 23 技能名 +
  "会问用户"强调 + 总控触发条件)注入常驻纪律 + 触发清单;`CLAUDE.snippet.md`(marker 块进
  `~/.claude/CLAUDE.md`)做双保险。**技术约束**:`${CLAUDE_PROJECT_DIR}` 指项目非全局→全局
  hook 用绝对路径;`$HOME` 在 stock Windows 不展开→用 `%USERPROFILE%`;SessionStart hook
  stdout 注入 context、exit≠0 不阻断会话、JSON 仅 exit 0 解析。
- **Codex**:`AGENTS.snippet.md` 注入常驻纪律 + 技能索引(文档化手动安装步,沿 v1 先例)。
- **OpenCode**:按其 agent/skill 约定提供入口(对话③核实其最新机制)。
- **纪律**:不擅自动用户全局配置(安装器只链技能 + 文档化注入步);三 harness 共用同一套
  `skills/` + `scripts/`,仅"如何被发现/常驻触发"的注入层不同。

---

## 9. 对话②要建的脚本(港 v1 + v2 增量)+ 名实对齐预判

### 9.1 脚本清单(标准库优先,接 `_shared` 走规范 bootstrap,各带 `--selftest` 亲手到 exit 0)
1. **`scripts/passport.py`**(港 v1 + §3.4 扩展):科研 DAG 台账。新增 `status`、一等 `back_edges`、
   v1→v2 schema 迁移容忍。保留 DAG 拓扑/环检测/fingerprint/stale-check/revision_rounds/mini-YAML。
2. **`scripts/run_checkpoint.py`**(港 v1 + 接新 `_shared`):确认点闸门聚合器。改硬编码路径为
   规范 bootstrap;按 §4.2 阶段判据聚合;Critical fail → exit 1 阻断;写回 gate.result+证据指针。
3. **`scripts/reroute.py`**(v2 新建,或并入 run_checkpoint):**根因回炉路由**(§5)——输入 fail
   的 FindingsReport,输出建议回边 + 配额检查;**只产建议,不执行**(决策点交用户)。
4. 合成 selftest 必须演示:① 一次"门 Critical fail → 建议回边"②一次"配额耗尽 → 转已知局限"
   ③ DAG 含回边的拓扑/状态校验。(真实 E2E 的"回炉+停下问人"演示在对话③。)

### 9.2 名实对齐预判(对话③写进 SKILL 的"增量边界 + 诚实落后项")
- **真增量**:确定性科研 DAG(状态+回边一等公民)+ 消费机读 findings 的阻断门 + 按根因定向
  回炉(带跨会话配额)+ 证据锚定的常驻续跑 + 三 harness 常驻触发。
- **裸模型本就会的(不吹成卖点)**:"大决策前停下问""注意别过度宣称""回炉别无限重来"——裸
  Opus 都会说;Light 的价值是**把它们落成可机检/可阻断/确定性触发**(脚本兑现,非 SKILL 喊话)。
- **诚实落后项**:① 总控**不能自己判新颖性/显著性**(AI 不能自评)→ 一律降级机读门+问用户;
  ② 主动诊断是启发式(会漏报/误报)→ 故只"提示+问",不阻断;③ 撞车检测离线档做不了纯同义
  (依赖 semantic_sim 边界);④ 常驻触发需安装一步(非纯技能,有 hook/CLAUDE.md 文档化步骤);
  ⑤ 各阶段门的**实现**在批 1+ 各技能,批 0 总控用合成 gate 演示接线,不假装门已全实现。

---

## 10. 留给对话②/③ 的待决与核实点(诚实)
- 对话②:`reroute` 独立成脚本还是并入 run_checkpoint?(倾向独立,单一职责、好 selftest)。
- 对话②:`status` 派生与显式冲突时,WARN 还是以显式为准?(倾向:显式优先 + WARN 提示)。
- 对话③:OpenCode 最新常驻/技能机制需上网核实;Claude Code SessionStart hook 行为复核一次。
- 对话③:补 Google co-scientist / MetaGPT 一手深读(competitors §16 已列),按需回灌本 spec。
- 全程:不 push;每脚本 selftest 亲手 exit 0;commit 只署 Light0305、中文标题写用途、无 Co-Authored。
