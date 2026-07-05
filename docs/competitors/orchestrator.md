# orchestrator(科研总控)对标笔记 —— Round 2

> 铁律 8 的产物:动手设计前,联网真读 ~10 个最强同类,抓"它强在哪 / 什么机制可借 /
> 什么是坑 / Light 怎么超越"。**本笔记的主轴是蓝图 §5 最看重的那一点:"什么时候停下来
> 问人(human-in-the-loop)"**——这正是 v2 总控("会问用户、不黑箱自动"=决策 H)的灵魂。
>
> **诚实声明(铁律 2/10)**:
> - 下列 11 个系统是本对话**一手搜读过机制**的(WebSearch/WebFetch 结果在对话记录里)。
>   其中 LangGraph、AI-Scientist「隐患」论文为深读;Agent Laboratory 的 alphaXiv 概览页
>   返回 403、PDF 二进制不可解,机制来自其检索摘要 + arXiv 卡,标注为"二手摘要"。
> - **本对话联网触及额度上限**(reset 14:50 Asia/Shanghai),**Google AI co-scientist、
>   MetaGPT** 仅扫到检索结果、未及一手深读,列入文末「待补深读」,不充数、不编造细节。
> - 凡未亲核的具体数字/字段,宁写"待核查"也不臆造。

---

## Round 2 重学结论（2026-07-03；优先于下方批 0 历史表）

本轮推翻“编排同类 skill 稀疏、主要老师只能是框架”的旧判断。下面 10 个条目都是真
`SKILL.md`。star 为 2026-07-03 GitHub API `stargazers_count`；commit 为当日固定 HEAD。
配套 script/template/reference 已逐文件读取；没有配套资源的条目明确写“仅 SKILL”。

### A. 真同类 agent skill（10）

| skill | repo star / fixed commit / 一手定位 | 真机制与配套资源 | 落进 Light |
|---|---|---|---|
| `dispatching-parallel-agents` | obra/superpowers **245,221★** · [`d884ae0`](https://github.com/obra/superpowers/blob/d884ae04edebef577e82ff7c4e143debd0bbec99/skills/dispatching-parallel-agents/SKILL.md#L14) · L14/L79+/L129+ | 只并行无共享状态的问题；返回后查冲突并跑全套。仅 SKILL。 | integration contract 明分 dependency/fork/join；overlay 不伪装 stage。 |
| `subagent-driven-development` | obra/superpowers **245,221★** · [`d884ae0`](https://github.com/obra/superpowers/blob/d884ae04edebef577e82ff7c4e143debd0bbec99/skills/subagent-driven-development/SKILL.md#L219) · L219–264 | 文件 handoff + durable ledger；读 `implementer-prompt.md`、`task-reviewer-prompt.md`、[`task-brief` L27+](https://github.com/obra/superpowers/blob/d884ae04edebef577e82ff7c4e143debd0bbec99/skills/subagent-driven-development/scripts/task-brief#L27)、[`review-package` L17–40](https://github.com/obra/superpowers/blob/d884ae04edebef577e82ff7c4e143debd0bbec99/skills/subagent-driven-development/scripts/review-package#L17)。 | hash-bound handoff；passport 不信聊天记忆。 |
| `executing-plans` | obra/superpowers **245,221★** · [`d884ae0`](https://github.com/obra/superpowers/blob/d884ae04edebef577e82ff7c4e143debd0bbec99/skills/executing-plans/SKILL.md#L39) · L39–56 | blocker/歧义/重复验证失败时停下，不猜。仅 SKILL。 | failed intake + checkpoint + reroute ASK。 |
| `task-coordination-strategies` | wshobson/agents **37,472★** · [`5cc2549`](https://github.com/wshobson/agents/blob/5cc2549a50fc672230efd0a0307e2fd27ffba792/plugins/agent-teams/skills/task-coordination-strategies/SKILL.md#L62) · L62–101 | blockedBy、critical path、wide/shallow graph；读 [`dependency-graphs.md` L42–82](https://github.com/wshobson/agents/blob/5cc2549a50fc672230efd0a0307e2fd27ffba792/plugins/agent-teams/skills/task-coordination-strategies/references/dependency-graphs.md#L42) 与 `task-decomposition.md`。 | stage 依赖、join、环/死依赖审计。 |
| `team-communication-protocols` | wshobson/agents **37,472★** · [`5cc2549`](https://github.com/wshobson/agents/blob/5cc2549a50fc672230efd0a0307e2fd27ffba792/plugins/agent-teams/skills/team-communication-protocols/SKILL.md#L77) · L77–137 | plan approval、shutdown save state、deadlock；读 [`messaging-patterns.md` L37–63](https://github.com/wshobson/agents/blob/5cc2549a50fc672230efd0a0307e2fd27ffba792/plugins/agent-teams/skills/team-communication-protocols/references/messaging-patterns.md#L37)。 | back-edge 绑定 `authorization_id`；handoff 保存 blocker/next action。 |
| `parallel-feature-development` | wshobson/agents **37,472★** · [`5cc2549`](https://github.com/wshobson/agents/blob/5cc2549a50fc672230efd0a0307e2fd27ffba792/plugins/agent-teams/skills/parallel-feature-development/SKILL.md#L60) · L60–110/L165+ | one owner/file、interface contract、integration；读 `file-ownership.md`、`merge-strategies.md`。 | producer/consumer 单归属；join 不凭单个文件宣称完成。 |
| `using-agent-skills` | addyosmani/agent-skills **68,718★** · [`8c65303`](https://github.com/addyosmani/agent-skills/blob/8c6530305396f341b5da7201cf1f7e390fdb863f/skills/using-agent-skills/SKILL.md#L12) · L12–48/L109–156 | task-phase routing + lifecycle + verify-don't-assume。仅 SKILL。 | 21 角色机械 inventory；按契约路由。 |
| `planning-and-task-breakdown` | addyosmani/agent-skills **68,718★** · [`8c65303`](https://github.com/addyosmani/agent-skills/blob/8c6530305396f341b5da7201cf1f7e390fdb863f/skills/planning-and-task-breakdown/SKILL.md#L35) · L35–55/L106–130/L218–230 | dependency graph、阶段 checkpoint、human approval。仅 SKILL。 | checkpoint 与用户 decision stop 分开。 |
| `memory-lifecycle` | basicmachines-co/basic-memory-skills **22★** · [`6d2b1d4`](https://github.com/basicmachines-co/basic-memory-skills/blob/6d2b1d426d0dacf020aef45f029768c9d8c1e5e5/memory-lifecycle/SKILL.md#L60) · L60–81/L145–177 | completion/paused/cancelled/revert；partial completion 不整项 archive。仅 SKILL。 | intake 七态；delivered 保留历史/limitation/hash。 |
| `mastering-langgraph` | SpillwaveSolutions/mastering-langgraph-agent-skill **36★** · [`a6069da`](https://github.com/SpillwaveSolutions/mastering-langgraph-agent-skill/blob/a6069daa9b11e58f98057a5ce49b87a4ae799082/SKILL.md#L81) · L81–101/L167+ | 真读 [`workflow-patterns.md` L89–128](https://github.com/SpillwaveSolutions/mastering-langgraph-agent-skill/blob/a6069daa9b11e58f98057a5ce49b87a4ae799082/references/workflow-patterns.md#L89)、[`hitl-patterns.md` L29–60](https://github.com/SpillwaveSolutions/mastering-langgraph-agent-skill/blob/a6069daa9b11e58f98057a5ce49b87a4ae799082/references/hitl-patterns.md#L29)、[`persistence-memory.md` L125–190](https://github.com/SpillwaveSolutions/mastering-langgraph-agent-skill/blob/a6069daa9b11e58f98057a5ce49b87a4ae799082/references/persistence-memory.md#L125)、`multi-agent-patterns.md`。 | v3 checkpointer/hash resume/HITL/back-edge；不引 LangGraph 依赖。 |

### B. 框架 / SDK / workflow 产品（机制锚，不占 skill）

| 类型 | 对象 | 借用 | 不借用 |
|---|---|---|---|
| 框架 | LangGraph | checkpointer、interrupt/resume、条件边、time travel、幂等副作用 | 不引运行时，不把 LLM router 当 Critical 裁定 |
| SDK | OpenAI Agents SDK | handoff/guardrail/session 的显式状态 | 不依赖付费 API，不把通用 guardrail 冒充科研门 |
| 框架 | Microsoft Agent Framework | workflow 与自由 agent 分离、checkpoint/resume | 不声称三 harness 都有同一 hook |
| 产品 | Temporal durable workflow | retry/compensation/versioned recovery | retry 不等于科研返修；不重放用户决策 |
| harness | Claude Code Agent Teams | dependency/plan approval/graceful shutdown | worker 不共享写 canonical state |

### C. 论文 / 经验文章（证据锚，不占 skill）

| 对象 | 用途 | 纪律 |
|---|---|---|
| AI-Scientist 与自动科研批判论文 | 自评/统计/引用/可见性风险 | 只解释为何要人工 checkpoint |
| ResearchAgent / Agent Laboratory / co-scientist | review loop、co-pilot、目标/反馈/纠偏 | 自评分只作软信号 |
| MetaGPT / Co-STORM | SOP 中间产物、共享概念空间、主动拉人 | free-form message 不当机读状态 |

### D. 旧结论复核与落地

- “非线性 DAG/回边独有”撤回：同类已有 dependency/pass-fail loop/fork/join/checkpoint。
  Light 的差异收窄为科研 stage + 合法早向边 + 用户授权 + budget + findings。
- “passport/resident 独有”撤回：ledger/checkpointer/memory lifecycle/session 注入都已有。
  真增量是 v3 schema/migration/content hash/freshness/evidence state 与诚实 harness 降级。
- “critical gate/用户决策独特”撤回：verify/HITL/plan approval 普遍存在。Light 的硬约束是
  reroute 只建议、back-edge 必带授权，2⊣3 不伪造成边。
- dependency/fork/join/dead gate → `integration-contract.json` + `integration_audit.py`；
  durable ledger/handoff → passport v3 + `lifecycle.py`；HITL → `authorization_id`；
  context budget → resident 4200/5400/9800 + `UNAVAILABLE` 降级。

---

## 0. 对标矩阵速览

| 系统 | 类型 | 何时停下问人(HITL) | 反馈/回炉机制 | 给 Light 最该偷的一招 |
|---|---|---|---|---|
| **LangGraph** | 编排框架(状态机) | `interrupt()` 在节点内暂停、把 payload 抛给人,`Command(resume=)` 续跑 | 条件边按 state 路由,可回边、可循环 | interrupt/resume + checkpointer 持久化;**回炉=条件边回指上游节点** |
| **AI-Scientist v1/v2** | 端到端全自动科研 | 几乎不停(全自动是卖点也是病) | 自评→迭代(agentic tree search) | 反面教材:**无人监督会出致命错且自己看不出** |
| **「隐患」论文 2509.08713** | 对全自动科研的批判 | 主张在 5 个脆弱点插人工 | 按阶段给 pitfall 分类 | **按阶段的 pitfall 清单≈Light 各阶段质量门的判据** |
| **ResearchAgent** | idea 生成⇄审 | 默认自动,但 ReviewingAgents 模拟人审 | idea⇄review 迭代,~3 轮收敛 | **回炉要收敛上限**(3 轮后递减→转已知局限) |
| **Agent Laboratory** | 端到端科研 co-pilot | **预设检查点**让人给反馈(co-pilot 模式) | mle-solver 迭代自改 | **co-pilot 模式实测优于全自动**——印证决策 H |
| **AutoGen** | 多 agent 对话 | `human_input_mode`= ALWAYS/TERMINATE/NEVER | GroupChatManager 选下一个发言者 | **三档人类介入开关**(按风险选档) |
| **CrewAI** | 多 agent 角色团队 | task 设 `human_input=True` 即暂停确认 | sequential / hierarchical(经理 agent 复核) | **经理 agent=守门**,但判断别交给它 |
| **Co-STORM** | 人机协作知识策展 | 轮次策略:人可随时插话/打断;连续专家轮后 Moderator 介入 | 动态 mind map 作共享概念空间 | **"连续 N 轮无人介入就主动问人"的轮次策略** |
| **obra/superpowers** | Claude 技能方法论 | brainstorm 分节给人确认;subagent 批次留人工 checkpoint | plan→execute→**verify(完工前必验)** | **verification-before-completion**=确认点落地 |
| **Claude Code 原生** | harness 自身编排 | **plan mode→ExitPlanMode** 是天然人工闸门 | 主会话=orchestrator,Task 派子 agent | **复用宿主的 plan 闸门**,别另造一套 |
| **skills.sh/mcpmarket 系** | orchestrator/PM 技能 | 多为全自动并行,人工弱 | 任务图分解 + 派并行 worker | 协调与执行分离;**但它们正缺"会问人"** |
| **Google AI co-scientist** | 多 agent + Supervisor | **scientist-in-the-loop**:人给目标/种子/反馈/纠偏 | Elo 锦标赛 + generate-debate-evolve | **科学家在环四通道**=交互确认点范本 |
| **MetaGPT** | 多 agent 软件公司 | 弱(偏自动) | 共享 message pool + 角色复核 | **"SOP 编码成 prompt"=SKILL.md 本质** |

---

## 1. LangGraph —— human-in-the-loop 的事实标准(最该深学)

- **定位**:把 agent 流程建成**状态图**(节点=步骤,边=转移,state 贯穿);LangGraph 把
  "暂停等人"做成了一等公民。**这是离 v2 总控最近的工程范式**。
- **HITL 机制(重点)**:
  - `interrupt()`:在节点内**暂停执行**,把一段 payload(要人看的东西)抛出;人给的值
    成为它的返回值、写回 state。
  - `Command(resume=value)`:把人的决定灌回去,**从中断点续跑**。
  - 静态断点 `interrupt_before` / `interrupt_after`:在某节点前/后强制停。
  - **持久化是前提**:必须配 checkpointer + `thread_id`,否则停了就丢 state。
  - 四类经典 HITL 模式:**批准/否决、编辑 state、复核并改工具调用、多轮取输入(+校验)**。
- **关键坑(必须记)**:resume 时**整个节点从头重跑**——`interrupt()` 之前的代码会再执行
  一遍。所以**有副作用的动作要放在 interrupt 之后或做成幂等**。Light 的"确认点"若用类似
  机制落地,写回台账这种副作用必须幂等(passport 的 `--write` 已是显式、可重入,正好)。
- **给 Light**:① 总控的"科研 DAG + 条件边 + 回边"几乎是 LangGraph 心智模型的科研特化;
  ② 但 Light **不引入 LangGraph 依赖**(零第三方、三 harness、纯文件式技能)——我们借的是
  **设计语义**(节点/条件路由/中断点/检查点持久化),用 SKILL.md 指令 + passport(台账即
  checkpointer)+ `_shared` 闸门**手工实现等价物**。③ HITL 不是"事事问",是"在分叉/不可逆
  处 `interrupt`",与决策 H 完全同构。

## 2. AI-Scientist v1 / v2(Sakana)—— 全自动的高峰,也是反面教材

- **定位**:端到端**全自动**科研——出假设→设计→跑实验→分析→写整篇手稿。v2 用 agentic
  tree search,有手稿过了 workshop 同行评审(均分约 6.33,据称可被接收)。
- **HITL**:几乎没有——**"无人值守"是它的卖点**。
- **坑(对 Light 极重要)**:
  - **不能批判性自评**:检不出自己方法的硬伤/逻辑矛盾(这条被多篇独立评测点名)。
  - v2 未必比 v1 强:有强模板时 v1 套模板成功率更高,v2 更发散但成功率更低。
  - **安全**:执行 LLM 自写代码,可能引危险包/失控联网/乱起进程。
- **给 Light**:**正是 v2 总控存在的理由**——不做"自己酷酷全自动",在它最会翻车的地方
  (方法设计、结果解释、投稿)**停下来问人**。把"AI 不能自评"变成总控的硬约束:**关键裁定
  不靠总控自夸,靠 `_shared` 机读闸门 + 用户确认**(灭 v1 的"自报分喂客观脚本"病)。

## 3.「The More You Automate, the Less You See」(arXiv 2509.08713)—— 直接喂质量门

- **定位**:专门批判全自动科研的论文,**核心论点:自动化越多、人能看见的错越少**。
- **它给的 pitfall 清单(≈Light 各阶段质量门的判据来源)**:六类——① 方法学缺陷 ②**数据
  泄漏** ③ 过度宣称/过度解读 ④ 编造或挑樱桃结果 ⑤ 统计错误(p-hacking 等) ⑥ **无法自我
  批判**;外加引用造假。
- **它建议的人工插点(≈Light 确认点选址)**:设计核验、结果验证、解释复核、统计审计、
  自洽性检查。
- **按阶段的坑(直接映射 Light DAG 节点的门)**:

  | 阶段 | 主要风险 |
  |---|---|
  | 问题定义 | 目标错位、夸大重要性 |
  | 方法 | 设计缺陷、统计错误、**数据泄漏** |
  | 执行 | 挑樱桃、编造、调参偏置 |
  | 解释 | 过度解读、逻辑不自洽 |
  | 报告 | 引用错误、细节缺失、无据宣称 |

- **给 Light**:这张表**几乎可直接当 Light 各阶段"阻断级 Critical 判据"的蓝本**(data-
  engineering 门=数据泄漏;result-analysis 门=统计/过度解读;paper-writing 门=无据宣称/
  引用;idea 门=夸大重要性/伪缺口)。Light 的增量是**把这些从"论文里的呼吁"落成 `_shared`
  的机读 gate + 总控按 `blocking_gates()` 定位回炉根因**。

## 4. ResearchAgent —— idea 生成⇄审 的回炉范式

- **定位**:自动定义问题、提方法、设计实验,**靠 ReviewingAgents 反馈迭代精修**。
- **机制**:① **entity-centric 知识库**——跨论文聚合实体,撑"跨学科有意义的新意";② 5 个
  ReviewingAgents,评审标准**从真实研究者判断里归纳**;③ 每轮 5 个 agent 给打分+反馈→聚合
  →精修,**一般 ~3 轮收敛,再多边际递减**。
- **给 Light**:① **回炉不是"重来",是"带具体缺口定向迭代"**(与蓝图回边设计一致);
  ② **回炉要有收敛上限**——v1 passport 已有 `revision_rounds`(2 轮上限 + 跨会话防刷新),
  ResearchAgent 的"3 轮后递减"佐证这个设计;③ 审稿标准"从真人归纳"提醒:Light 的 idea-
  critique 阈值要诚实标"经验默认可调",别假装权威(v1 已踩过并纠正)。

## 5. Agent Laboratory —— "co-pilot 优于全自动"的实证(印证决策 H)

- **定位**:端到端科研助手(文献综述→实验→写报告),**可全自动、也可 co-pilot**。
  角色:PhD / Postdoc / ML Engineer agents。
- **HITL(重点)**:**co-pilot 模式在预设检查点让人给反馈**,人来微调 agent 决策、精修产物,
  保留"有条件的自治"。
- **实证结论(对 Light 最有力的外部背书)**:**co-pilot(有人反馈)整体质量高于全自动**,
  多数指标更优;用户评测 co-pilot 可用性高、多数人愿继续用。
- **机制**:mle-solver 等"求解器"做迭代代码生成 + 自改良(打分/修复循环)。
- **给 Light**:① "**预设检查点 + 人给反馈**"=Light 确认点/决策点的同义词,且**有数据证明它
  更好**——直接写进 SKILL 当"为什么要停下问你"的依据;② 角色分工(PhD/Postdoc/Eng)≈Light
  的技能分工,但 Light 的总控**不亲自扮演角色**,只调度+守门。
- **诚实**:本条机制为二手检索摘要(一手页 403),数字级细节待补核。

## 6. AutoGen —— 三档"人类介入开关"

- **定位**:微软多 agent **对话式**编排;为"人参与"而设计。
- **HITL(重点)**:`human_input_mode` 三档——**ALWAYS**(每步都问人)/ **TERMINATE**(仅在
  要终止时问)/ **NEVER**(全自动);`UserProxyAgent` 代表人坐在 agent 对话里;终止条件=最大
  连续自动回复数 或 命中终止消息。
- **坑**:`GroupChatManager` 默认 `NEVER`,且有已知问题——**非 ALWAYS 档的人类介入不一定被
  正确尊重**(GitHub discussion #5022)。提醒:**"会问人"若只是软配置,很容易名存实亡**。
- **给 Light**:① 把"何时问人"显式分档的思路很好,但 Light **不做可一键关成 NEVER 的全自动
  档**(那就背叛决策 H);Light 的分档是**按"分叉/不可逆/门没过"判据**触发,而非全局开关。
  ② AutoGen 的坑反向证明:Light 的"问人"必须**写死在确定性逻辑里(闸门 exit code 阻断 +
  SKILL 红线)**,不能只靠模型自觉(正是 v1 常驻触发缺口的教训)。

## 7. CrewAI —— 经理 agent 守门 + 任务级 human_input

- **定位**:角色化 agent 团队;**sequential**(顺序)或 **hierarchical**(经理 agent 委派+
  复核)两种 process。
- **HITL**:在 task 上设 `human_input=True` 即在该步**暂停等人确认**。
- **给 Light**:① "经理 agent 复核"≈总控守门,但 **CrewAI 让经理 agent 替你做研究判断,
  Light 明确不这么做**(总控只判断"调谁/过哪个门/下一步",研究决策交用户=蓝图边界);
  ② 任务级 `human_input` 颗粒度好,Light 的确认点也是**挂在具体阶段**而非全局。

## 8. Co-STORM(Stanford)—— "轮次策略"主动把人拉进来

- **定位**:人机**协作知识策展**;LLM 专家 + Moderator + 人,多方对话。
- **HITL(重点)**:① **轮次管理策略**——人可随时打断专家、注入自己的话来**steer**方向;
  ② **连续若干轮专家发言后,系统让 Moderator 介入**抛出引导性问题,防止跑偏/原地打转;
  ③ **动态 mind map**把信息组织成层级概念图,作"人机共享的概念空间"。
- **给 Light**:① **"连续 N 步无人介入→主动问一次人"**是极好的**主动诊断触发器**(防总控
  闷头自动跑太久);② mind map≈总控该给用户的**项目状态图可视汇报**(常驻触发开头那份
  "上次断哪/卡哪个门/下一步")——让用户随时有"共享概念空间",零成本接续。

## 9. obra/superpowers —— plan→execute→verify,完工前必验

- **定位**:跨多 harness 的**Claude 技能方法论框架**(Claude Code/Codex/OpenCode 等都适配,
  与 Light 同生态)。
- **机制/HITL**:① **brainstorm**:写码前先用提问精修想法、**分节给人确认**再存设计文档;
  ② git worktree 隔离;③ **writing-plans**:拆成 2–5 分钟可验证小任务(给确切路径+验证步);
  ④ **subagent-driven**:每任务派新 subagent,两段式复核(先合规、再质量),**批次间留人工
  checkpoint**;⑤ **TDD** RED-GREEN-REFACTOR;⑥ **verification-before-completion**:宣布完成
  前必须真验过。
- **给 Light**:① **verification-before-completion = Light 确认点的精神**——"别口头说跑了闸门"
  (v1 run_checkpoint 正是把它落成 exit code);② "brainstorm 分节确认"≈idea/方案定稿前的
  交互确认;③ Light 与 superpowers 同为文件式技能、同跨 harness,**适配层可互为参照**(三
  harness 注入)。④ 区别:superpowers 偏软件工程流程,Light 偏**科研**流程 + **科研专属诚信
  门**(数据泄漏/统计/幻觉引用/过度宣称),这是 Light 的领域纵深。

## 10. Claude Code 原生编排 —— 复用宿主的 plan 闸门,别另造

- **定位**:主会话即 orchestrator,用 **Task 工具**派**子 agent**(独立上下文、可限工具);
  **plan mode**(EnterPlanMode/ExitPlanMode)处理规划+执行编排;Explore 子 agent 扫仓库。
- **HITL(重点)**:**`ExitPlanMode` 是一个天然的人工审批闸门**——出计划→用户批准→才执行。
- **给 Light**:① 总控**不重造一套 agent 运行时**,在 Claude Code 上**借 plan/ExitPlanMode
  做"方案确认点"**、借 Task 做并行只读核实(但铁律 1:写代码不靠 agent);② 在 Codex/
  OpenCode 上没有完全对应物→Light 的确认点要有**不依赖 plan mode 的纯指令+脚本兜底**(三
  harness 一致),plan mode 有则增强、无则降级。③ 子 agent"独立上下文"提醒:跨阶段交接必须
  走**机读工件(`_shared` findings)**,不靠聊天记忆(灭"prose 交接"病)。

## 11. skills.sh / mcpmarket 上的 orchestrator·project-manager 技能群

- **定位**:一批"把 Claude 变项目总指挥"的技能——**任务图分解 + 派并行 worker**,强调
  **协调与执行分离**;PM 类把大目标拆给 spec/impl/review/doc 子 agent。
- **给 Light**:① "协调与执行分离"与 Light"总控不亲自干活、只判断+路由+守门"完全一致,
  可放心采用;② **但它们的共性短板正是 Light 的机会**——几乎都奔着**并行全自动**去,**"会
  停下来问人"很弱、科研诚信门为零**。Light 不拼"并行多快",拼"**在对的地方停下来问 + 机读
  闸门守诚信 + 按根因回炉**"。

---

## 12. Google AI co-scientist —— "科学家在环"四通道(决策 H 的最佳范本)

- **定位**:多 agent + **Supervisor**,围绕"加速科学发现"的人机协作系统(2025)。
- **机制**:6 个 worker agent——**Generation**(出假设)/ **Reflection**(评估)/ **Ranking**
  (比质量)/ **Evolution**(改良)/ **Proximity**(保持贴合目标)/ **Meta-review**(综合评议);
  **Supervisor** 把研究目标解析成配置、分配资源、管 agent workflow。改进循环=**test-time
  compute scaling**:自我博弈辩论生成竞争假设 → **Elo 锦标赛**排序 → Evolution 改良 top →
  递归自我批判 + 工具反馈。称"Elo 越高、答对概率越高"。
- **HITL(重点)**:**科学家保持中枢控制的四条通道**——① 自然语言给**研究目标**;② 贡献
  自己的**种子想法/假设**;③ 对产物用自然语言给**反馈**;④ 直接交互**纠偏**。research-plan
  configuration 把人定的目标翻成可执行 agent 分配,**"让人类专长导向算力,而非自治乱探"**。
- **给 Light**:① **这四通道几乎逐条对应 Light 的交互确认点**(目标=方向选择、种子=用户已有
  idea、反馈=回炉缺口、纠偏=随时喊停改向)——直接当 SKILL 里"总控如何与你协作"的骨架;
  ② Supervisor"目标→配置"≈总控规划 pipeline;③ **取舍**:Elo/自评锦标赛仍是 LLM 评 LLM,
  与 AI-Scientist"不能自评"教训对冲——Light 把 Elo 这类**自评只当软信号/排序,不当 Critical
  裁定**;裁定靠 `_shared` 机读闸门 + 用户确认。
- **坑**:自评锦标赛在缺金标时会自我强化偏差;Light 不把它放进阻断判据。

## 13. MetaGPT —— "Code = SOP(Team)":点破 SKILL.md 的本质

- **定位**:模拟软件公司的多 agent 框架,核心公式 **"Code = SOP(Team)"**——质量不来自单点
  聪明,来自**专职角色执行良定义的标准作业流程(SOP)**。
- **机制**:5 角色(PM / 架构 / 项目经理 / 工程 / QA),每角色一份 profile(名/目标/约束/
  上下文/技能);PM 出 PRD(用户故事+需求池)→ 架构出设计(文件清单/数据结构/接口)→ 工程
  实现 → QA 测试。**共享 message pool**:每个 agent 观察环境/别人的消息。**SOP 被编码成 prompt
  序列**,规定职责与"中间产物标准"。
- **给 Light**:① **"把 SOP 编码成 prompt"正是 Light 的 SKILL.md 本质**——SKILL 就是把科研
  SOP 写成给模型的子提示词;MetaGPT 用公式点破了 Light 一直在做的事,**佐证铁律 12 的提示词
  工程手艺**(具体数字/中间产物标准/职责单一)。② "规定中间产物标准"≈Light 阶段工件契约
  (`_shared` findings + 落盘工件);③ message pool ≈ Light 的台账 + 机读交接,但 Light 用
  **结构化机读(findings)**而非自由文本消息,更可机检。④ **坑**:MetaGPT 重流程自动、轻
  "问人",Light 反之——SOP 要固化,但不可逆决策必须停下问用户。

## 14. 横切总结:可借的最强机制(按"何时停下问人"主轴归并)

1. **中断/续跑 + 检查点持久化**(LangGraph):停在分叉点、把决定权交人、从断点续跑;
   持久化靠**台账(passport)= Light 的 checkpointer**。副作用幂等(passport `--write` 已是)。
2. **条件路由 + 回边**(LangGraph 条件边 / ResearchAgent idea⇄review):**下一步由 state +
   门结果决定,不是 1→2→3**;回炉 = 条件边回指上游节点 + 带具体缺口。
3. **回炉收敛上限**(ResearchAgent ~3 轮 / v1 `revision_rounds` 2 轮):**回炉要有配额、跨
   会话防刷新**,到顶转"已知局限"诚实记录,不假装修好。
4. **按阶段的 pitfall→门判据**(隐患论文 / AI-Scientist 不能自评):各阶段 Critical 判据
   (数据泄漏/统计错/过度宣称/幻觉引用/夸大重要性)→落成 `_shared` 机读 gate。
5. **co-pilot 检查点 + 科学家在环 + 实证更优**(Agent Laboratory / Google co-scientist):
   有人反馈的产物质量更高(实证背书决策 H);**科学家在环四通道**(给目标/种子/反馈/纠偏)
   = 总控与用户协作的标准接口,写进 SKILL 当"为什么 & 怎么停下问你"的骨架。
6. **分档/主动触发问人**(AutoGen 三档 / Co-STORM 连续轮后 Moderator 介入):问人不是事事问,
   是**按判据触发**(分叉/不可逆/门没过/连续 N 步无人介入)。
7. **完工前必验**(superpowers verification-before-completion / Claude Code ExitPlanMode):
   确认点 = 机器先验出报告 + 人确认,**不口头说"跑过了"**(v1 run_checkpoint 已落地)。
8. **协调与执行分离 + 机读交接**(Claude Code 子 agent / skills.sh):总控只判断+路由+守门,
   交接走 `_shared` findings 工件,不靠 prose。
9. **SOP 编码成 prompt + 中间产物标准**(MetaGPT "Code = SOP(Team)"):Light 的 SKILL.md 就是
   把科研 SOP 写成提示词;各阶段"中间产物标准"落成 `_shared` findings 工件契约。

## 15. 它们共同的坑 / 没做好的(= Light 的超越点)

- **几乎都偏"全自动炫技",真正"会停下来问人"的少、且常是软配置(AutoGen 坑印证)。**
  → Light 把"问人"写进**确定性逻辑**:门 exit code 阻断 + SKILL 红线 NON-NEGOTIABLE,
  不可一键关成全自动。
- **科研诚信门基本为零**(通用编排框架不懂数据泄漏/p-hacking/幻觉引用/过度宣称)。
  → Light 消费 `_shared` 的领域门 + 按 `blocking_gates()` **定位回炉根因**,这是领域纵深。
- **回炉多为"重来",少有"按根因定向 + 带配额"。**
  → Light:拒稿/门没过 → 按根因分发(创新性回 idea、实验回方案、写作回写作)+ `revision_
  rounds` 配额防刷新。
- **跨阶段交接多靠对话/记忆,缺机读契约。** → Light 走 `light.findings.v1` 机读工件。
- **多依赖某框架运行时/付费 key/MCP。** → Light 零第三方、零 MCP、零 key、三 harness、
  纯文件式;借的是**语义不是依赖**。
- **AI 不能自评却让 AI 自评/自报分。** → Light 关键裁定靠**机读闸门 + 用户确认**,不自夸。

**一句话超越点**:别人做"并行更快的全自动总指挥";Light 做"**在对的地方停下来问你、用机读
闸门守科研诚信、按根因定向回炉**的科研 mentor 式总控"——这三件正是上面 11 个系统集体最弱处。

## 16. 待补深读(诚实,本对话未及一手核实)

> 下对话或后续按需补;**不在没读透前写进设计依据**。

- AgentRxiv(协作自治研究)、OpenAI Agents SDK(Swarm 的继任,handoffs/guardrails 的"护栏"
  设计值得看)、Cline/Roo 的 plan/act 双模、LangGraph 的 `Send` 动态分支与子图(map-reduce
  式并行,对应 Light 的图表∥引用并行段)。

---

## Round 3 补强：WAITING_USER 不能只是状态标签

复核 `workflow_ledger.py` 后发现一个与“会问用户”直接相关的名实缺口：账本可以把任务标成
`WAITING_USER`，但只要求 decision id/scope/expiry，不要求真正写出用户要回答的问题、选项和后果。
这会让总控在数据上看似“停下问人”，实际交给下个会话时没有可回答的问题。

本轮把 WAITING_USER 改成可执行交互契约：

- decision 必须有非占位 `question`；
- 必须给至少两个 option，每个 option 有唯一 id、label，并说明 consequence/impact/tradeoff；
- workflow digest、resume state hash、evidence artifact hash 必须是真实 `sha256:<64hex>`；
- evidence path 必须是安全相对路径，拒绝模板、本机绝对路径和 `..` 越界；
- 缺失时 ledger 直接 FAIL，而不是把空心等待伪装成可恢复的 HITL。

这不替用户选择；它只保证总控暂停时真的带着一个可回答、可比较、可恢复的问题。

## Round 3 五席重认证：用直接 skill 替换框架切片（2026-07-05）

原五席中的 AutoGen、CrewAI、MetaGPT、DeerFlow 虽然已读到持久化、交接与恢复代码，
但它们是框架/产品，不是“总控 skill”。本轮不抹掉这些机制证据，只把 105 项学习矩阵的
四个席位改为真正可直接调用的同功能 skill：

| 席位 | 直接 skill | 当前父仓热度 / 固定 commit | 本轮亲读范围 | 对 Light 的校验 |
|---:|---|---|---|---|
| 2 | `obra/superpowers/subagent-driven-development` | 246,428★ / `d884ae04edebef577e82ff7c4e143debd0bbec99` | 完整 418 行 SKILL；`task-brief`；`review-package` | 每任务 fresh worker、任务级复核、最终广域复核；交接与复核包必须落文件，不能靠聊天记忆 |
| 3 | `wshobson/agents/task-coordination-strategies` | 37,530★ / `5cc2549a50fc672230efd0a0307e2fd27ffba792` | 完整 163 行 SKILL；完整 97 行 `dependency-graphs.md` | `blockedBy`、critical path、菱形 join、环依赖和伪依赖；Light 已有依赖闭包、cycle 与提前 join 门 |
| 4 | `wshobson/agents/team-communication-protocols` | 37,530★ / 同上 | 完整 180 行 SKILL；完整 112 行 `messaging-patterns.md` | plan approval、shutdown、deadlock、消息最小充分性；Light 用授权 checkpoint 与哈希交接替代 harness 专属消息 API |
| 5 | `addyosmani/agent-skills/planning-and-task-breakdown` | 68,989★ / `8c6530305396f341b5da7201cf1f7e390fdb863f` | 完整 234 行 SKILL | 依赖图、2–3 任务 checkpoint、human review、顺序/并行边界；Light 进一步把科研 stage、风险授权和失败回边机器化 |

star 只记录 2026-07-05 GitHub API 的父仓采纳度，不冒充单个 skill 的 star。三个父仓
当日 API 均报告 MIT；固定 commit 与本节链接对象一致。AutoGen 等框架仍留作机制锚，
但不再计入“五个同功能学习对象”。

本轮回读还发现 `workflow_ledger.py` 的另一处名实缺口：`SUCCEEDED` 虽有产物哈希，
却仍可由 owner 自填 `completion_status=PASS`。已补成哈希绑定的独立验证包：
`verifier_id` 不能等于 owner，验证方法、时间、报告哈希必填，且
`subject_sha256s` 必须与当前 `evidence_artifacts` 的哈希集合完全一致。产物变化即旧验证
失效；human review 另需授权 ID。该门只证明当前字节版本经过可定位复核，不虚称内容正确。

---

## Sources(本对话一手检索/抓取)

- LangGraph HITL:[concepts 摘要](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/)、[Interrupts and Commands in LangGraph (dev.to)](https://dev.to/jamesbmour/interrupts-and-commands-in-langgraph-building-human-in-the-loop-workflows-4ngl)、[LangGraph 201: Adding Human Oversight (TDS)](https://towardsdatascience.com/langgraph-201-adding-human-oversight-to-your-deep-research-agent/)
- AI-Scientist:[AI-Scientist-v2 (GitHub)](https://github.com/sakanaai/ai-scientist-v2)、[Evaluating Sakana's AI Scientist (arXiv 2502.14297)](https://arxiv.org/html/2502.14297v2)
- 隐患论文:[The More You Automate, the Less You See (arXiv 2509.08713)](https://arxiv.org/pdf/2509.08713)
- ResearchAgent:[arXiv 2404.07738](https://arxiv.org/abs/2404.07738)、[NAACL 2025 长文](https://aclanthology.org/2025.naacl-long.342/)
- Agent Laboratory:[arXiv 2501.04227](https://arxiv.org/pdf/2501.04227)、[项目页](https://agentlaboratory.github.io/)
- AutoGen:[GroupChatManager human_input_mode discussion #5022](https://github.com/microsoft/autogen/discussions/5022)、[AG2 GroupChatManager API](https://docs.ag2.ai/0.8.1/docs/api-reference/autogen/GroupChatManager/)
- CrewAI / 框架对比:[ZenML: CrewAI vs AutoGen](https://www.zenml.io/blog/crewai-vs-autogen)
- Co-STORM:[stanford-oval/storm (GitHub)](https://github.com/stanford-oval/storm)、[Co-STORM (DeepWiki)](https://deepwiki.com/stanford-oval/storm/3-co-storm-collaborative-system)、[Into the Unknown Unknowns (arXiv 2408.15232)](https://arxiv.org/pdf/2408.15232)
- superpowers:[obra/superpowers (GitHub)](https://github.com/obra/superpowers/)、[writing-plans SKILL.md](https://github.com/obra/superpowers/blob/main/skills/writing-plans/SKILL.md)
- Claude Code 原生:[The Task Tool (dev.to)](https://dev.to/bhaidar/the-task-tool-claude-codes-agent-orchestration-system-4bf2)、[subagents & orchestrator pattern](https://www.channel.tel/blog/claude-code-subagents-orchestrator-pattern)
- skills 生态:[Orchestrator skill (mcpmarket)](https://mcpmarket.com/tools/skills/orchestrator-agent-coordinator)、[Engineering Project Manager skill](https://mcpmarket.com/tools/skills/engineering-project-manager)
- Google AI co-scientist:[Google Research blog](https://research.google/blog/accelerating-scientific-breakthroughs-with-an-ai-co-scientist/)
- MetaGPT:[arXiv 2308.00352](https://arxiv.org/html/2308.00352v6)、[ICLR 2024 (OpenReview)](https://openreview.net/forum?id=VtmBAGCN7o)
