# competitors — light-memory-pm（记忆与项目管理 · 常驻横切）

> 铁律 1+2 对标笔记:动手前深读最强同类,**机制上网核实(非凭记忆)**,落地可借机制 + 标清超越点与
> 诚实边界。本技能**不是机读门**(C1 research-ethics / C2 consistency 才是);它是**项目运行时记忆与
> 项目管理的归属方**——把项目卡 / 决策日志 / 版本史 / 跨会话交接 / 受控事实源落到每个项目自己的
> **`.light/`**,**复用(不重造)** `light-orchestrator/scripts/passport.py` 引擎。
>
> **Round 2 重做(R1,2026-06-23)**:批 0 初版把"同类 skill"与"机制对标"混在一张表,真·同类记忆
> **skill** 只列了 ~3 个(Cline/Roo/superpowers),其余 8 条是框架/方法论/原生特性(ADR/Keep a
> Changelog/PARA/mem0/Cursor/CLAUDE.md/git/LangGraph)。本轮按 R1 硬指标把真·同类 skill **补到 10 个**
> (7 个本轮新读、优先高 star),与"机制对标"分表;新增 **§0.C 全域五问机制提炼**(自动捕获 / 会话开头
> 续上 / 检索 / 压缩 / 跨 harness)直接驱动续跑设计。star 均 **2026-06-23 联网核 GitHub repo 页**
> (外部可变事实,带 snapshot;star 会涨,以仓库页为准)。
>
> 初版:批 0 第三块 C3(2026-06-17)。Round 2 R1:2026-06-23。作者 Light0305 + Claude。

---

## 0.A 真·同类记忆 SKILL（≥8 真同类 · R1 硬指标 · star=[snapshot 2026-06-23, src=GitHub repo 页]）

> 判据:别人把"记忆/续跑"做成一个**技能/插件/约定**(可被 agent 发现并调用),而非通用框架/库/方法论。

| # | 同类 skill（star） | 它怎么做（已读代码/SKILL/README，带可复验点） | 我借进哪个能力 | 我诚实差在哪 |
|---|---|---|---|---|
| 1 | **thedotmack/claude-mem**（**83.8K★**，记忆类最高 star） | **5 个生命周期 hook**(SessionStart/UserPromptSubmit/PostToolUse/Stop/SessionEnd)**自动捕获**;存 **SQLite(全文)+Chroma(向量)** 混合检索,4 个 MCP 工具(search/timeline/get_observations…);AI 生**语义摘要**;**3 层渐进披露**(紧凑索引~50-100 tok→时间线→详情~500-1000 tok);跨 harness 靠**每平台独立安装目录**(`.claude-plugin`/`.codex-plugin`/`cursor-hooks`/`openclaw`)+ `npx claude-mem install --ide opencode\|gemini-cli` | **3 层渐进披露**思想(对齐我"会话开头给紧凑续跑摘要、要细节再翻 .light/")+ **每平台适配**思路(我的三 harness 注入层) | **它用了我硬约束禁止的全套重机械**(MCP+向量库+AI 压缩=要 key/要常驻进程);我零 MCP/零 key,故无自动捕获、无向量检索——这是**约束下的刻意取舍**,不是没本事(见 §0.C①③) |
| 2 | **rohitg00/agentmemory**（**23.7K★**） | **15 个 SKILL.md 技能**:8 个可调(`/recall` `/remember` `/session-history` `/forget` `/recap` `/handoff` `/commit-context` `/commit-history`)+ 7 个按需 reference(含 `agentmemory-architecture`/`write-agentmemory-skill`);SQLite + **混合检索**(BM25 + 向量 all-MiniLM-L6-v2 + 知识图,RRF 融合);**SessionStart hook** 载"项目画像"(top concepts/files/patterns);`agentmemory connect <agent>` 适配 15+ agent | **把记忆拆成命名能力**的设计(对照我 `pm.py` 子命令 init/audit/broadcast/**resume**);`/handoff` + `/session-history` 分离 = 我的交接卡 + passport 阶段史分离 | 它检索靠向量+图(要本地模型/可选 key);我靠 Grep 字面。它无台账机检(无日期/链路/版本校验) |
| 3 | **coleam00/claude-memory-compiler**（**1.2K★**） | **SessionEnd + PreCompact hook** 自动抓会话→ `flush.py` 调 **Claude Agent SDK** 抽"决策/教训/模式/坑"→ `compile.py`(**LLM 编译器**,Karpathy LLM-KB 架构)整理成交叉引用知识库 `knowledge/{concepts,connections,qa}/` + `index.md`;**SessionStart 注入 index**;`daily/YYYY-MM-DD.md` | **PreCompact 兜底**思想(压缩前抢救=我"上下文将尽主动交接"的机制对应);"决策/教训/坑"分类 ≈ 我 decision_log + 去偏科化教训回写 | 它自动抽取靠 Agent SDK(要 key/要 SDK 进程);我显式写。它无机器校验台账自洽 |
| 4 | **Digital-Process-Tools/claude-remember**（**126★**，Anthropic 官方 marketplace） | **plugin**;3 hook:`session-start-hook.sh`("载记忆文件+**恢复漏掉的会话**")、`user-prompt-hook.sh`(注时间戳)、`post-tool-hook.sh`("工具调用增量超阈值即**自动存**");**Haiku 分层压缩**:原始→一行(`extract.py`)→每时压成 `today-YYYY-MM-DD.md`→日合并 `recent.md`(7 天)+`archive.md`(更久);SessionStart 注入 identity/remember/now/today/recent/archive;**357 测试** | **分层时效压缩**(recent 7 天 vs archive)**验证我 `archived:` 归档设计**;"恢复漏掉的会话"≈ 我续跑汇报"上次断哪" | 它用 Haiku 自动分层摘要(要 key);我不自动摘要,靠 append-only decision_log/version_history(见 §0.C④) |
| 5 | **hanfang/claude-memory-skill**（**33★**，**我的哲学双胞胎**） | `~/.claude/commands/mem.md` + `~/.claude/memory/{core.md,me.md,topics/<t>.md,projects/<p>.md}`;原话 **"No databases. No embeddings. No semantic search. Just markdown files… Deterministic, grep-based retrieval"**;`core.md`+`me.md` **会话开头常载**、卡住时**顺指针**到 topics;`load`/`save`/`recall` 非阻塞 + `/mem show` `/mem forget` | **"核心常载 + 顺指针检索"**(强化我 MEMORY.md 索引→`.light/` 指针的检索路径);**验证"纯 markdown+grep" 是正当学派**,不是我能力不足 | 它无项目 DAG/状态/门/版本对齐;我多这一层(超越点),但同样无向量召回 |
| 6 | **jayzeng/agentmemory**（**7★**，**跨 agent + 确定性 context 命令 = 我 resume 最近原型**） | 纯 markdown(`MEMORY.md`/`SCRATCHPAD.md`/`daily/YYYY-MM-DD.md`/`topics/*.md` 带回链);**单一共享目录 `~/.agent-memory/` + 每 harness 各自 SKILL.md**(`~/.claude/skills`、`~/.codex/skills`、`~/.cursor/skills`、`~/.agents/skills`);**确定性命令 `agent-memory context`**(CC 里 `!agent-memory context --no-search`)每回合前注入;`qmd` 可选语义检索(本地 all-MiniLM,**无需 key**)/默认 BM25 关键词(~30ms);CLI+skill+core(`src/core.ts`),**非 MCP** | **确定性 context 命令** = 我 **`pm.py resume`** 的直接原型(每 harness SKILL.md/AGENTS.md 调同一条命令,不靠 hook);**`--no-search` 降级**思想 = 我"读不到台账降级仍出纪律" | 它 context 是"记忆 dump + 搜索",我 resume 报**DAG 阶段/门/stale 重验范围**(科研项目态);它无台账机检 |
| 7 | **WeirdSky924/agent-handoff-skill**（**18★**，**跨 Codex+CC 续跑 = R4.e 活教材**） | **靠 repo-local 文件约定而非 harness hook**:`AGENT_HANDOFF.md`(根索引)+ `.agent-handoff/{snapshot,decisions,validation,risks,backlog}.md`;把**幂等 marker 块**并进 Codex `AGENTS.md` + CC `.claude/CLAUDE.md`,指令 **"startup 读 AGENT_HANDOFF.md"**;**固定恢复顺序**(index→snapshot→risks→backlog→源码);`scripts/bootstrap_handoff.py`、`agents/openai.yaml`(Codex) | **"AGENTS.md/CLAUDE.md 约定 + startup 确定性读单文件"**正是我 R4.e 跨 harness 方案的骨架;固定恢复顺序 ≈ 我 handoff_prompt 的"按序读" | **它零机器校验**(无链检查/无日期/无 stale);我 HANDOFF_CHAIN + check_project_card + stale-check 机检 = 超越点 |
| 8 | **Cline Memory Bank**（约定型 `.clinerules/`,非独立 repo;批 0 已读原 prompt） | 6 份 md 分层(projectBrief/productContext/systemPatterns/techContext/**activeContext**/**progress**);硬规则 **"I MUST read ALL memory bank files at the start of EVERY task"**;`update memory bank` 时"**review every file 即便没改**" | "会话开头读全量"→我落成 hook 注入 + **`pm.py resume` 确定性命令**(非靠模型自觉);项目卡 = activeContext+progress 合体 | Cline 纯 **prose 纪律**(叫模型"必须读/必须准"),**零机器校验**;无 DAG/状态机/指纹/证据门 |
| 9 | **Roo Code Memory Bank**（GreatScottyMac,约定型;批 0 已读 README） | 4 份 md(activeContext/**decisionLog**/productContext/progress);**实时事件驱动更新**(architect→decisionLog,code→progress);**UMB("update memory bank")** 会话异常中断时强同步 | **decisionLog = 我 decision_log**(ADR 式追加,事件触发);**UMB 兜底** = 我"上下文将尽主动交接 + 被动断点恢复双轨" | 同 Cline:prose 纪律、无机器校验;按 mode 触发靠模型判断,我按"触发→写入对照表"+ 脚本核 |
| 10 | **obra/superpowers handoff**（大技能包内的 handoff skill;批 0 已核 issue #931 + RELEASE-NOTES） | `/create_handoff`+`/resume_plan`;handoff 落 `thoughts/shared/handoffs/`;"写**具体 next steps**";resume **自动接回** executing-plans(不需用户手动选技能) | **handoff_card + handoff_prompt 两件套**(落 `.light/handoff/S<NN>-*.md` + 打印启动提示词);"写具体下一步" + resume 接回总控 | superpowers handoff **不校验链结构**;我 HANDOFF_CHAIN 查 parent_session 可达/无悬挂/无环 = 超越点。(注:superpowers"连续执行不停问人"与 Light"停下问人"哲学相反,属总控域) |

> **结论(诚实)**:记忆 skill 这一类**真存在且高 star**(claude-mem 83.8K、rohitg00 23.7K、compiler 1.2K)——批 0 说"top 仅 50★"是**漏检头部**,本轮 R1 已纠。但**头部全靠重机械**(hook 自动捕获 + 向量/图检索 + LLM 压缩 + MCP),与 Light"零 MCP/零 key/三 harness/可审计"硬约束正交;**与 Light 同约束的真同类是 hanfang(33★)与 jayzeng(7★)**——两者都印证"纯 markdown + 确定性命令 + grep"是一条正当且可行的路。

---

## 0.B 机制对标（框架 / 方法论 / 原生特性 —— 不占 skill 名额，仍是有价值的机制源）

| 机制 | 取什么 | 与 §0.A 的区别 |
|---|---|---|
| **ADR / MADR / Y-Statement**（已读 adr.github.io+模板） | `decision_log.md` = 轻量 ADR 时间线(`[日期] 决策 — 理由 — 来源`,一行一决策、只追加、`superseded` 语义) | 是**记录格式方法论**,非可调用技能 |
| **Keep a Changelog 1.1 + SemVer**（已读 keepachangelog.com） | `version_history.md` = changelog;`version_tag_reconcile.py` 机检 ↔ git tag 双向失配 | 是**风格指南零执行**;我把"版本必对齐 tag"落成脚本 |
| **PARA**（Tiago Forte） | 项目归档协议(`archived:` 不删目录,会话开头跳过)+"读 next_actions 优先"=按可执行性组织 | 是**手工归档方法论**,无状态机/校验 |
| **mem0**（已读 DeepWiki+arXiv **2504.19413**） | "作用域分层"(项目 namespace vs 会话);**反例确立我方哲学**:关键事实**显式写**(不靠 LLM 抽取) | 是**记忆框架/库**(LLM 抽取→向量召回→ADD/UPDATE/DELETE);非技能 |
| **Cursor Rules**（`.cursor/rules/*.mdc`） | `.light/` = 版本控制、随仓库走的项目记忆;分层(项目 vs 用户级) | 是 IDE **原生特性**,非独立技能 |
| **Claude Code 原生 CLAUDE.md**（code.claude.com/docs/en/memory） | 共存不替代:CLAUDE.md=耐久指令/偏好,`.light/`=演化项目状态;SSOT 边界表照此切 | 是 harness **原生记忆机制**,非技能 |
| **git-as-memory**（tag/log/notes） | version_history ↔ **annotated** `git tag -a` 对齐 | 是**工具用法**,非技能 |
| **LangGraph checkpointer/Store**（总控 competitors 已深读） | **两层记忆**:thread 级(短期)vs 跨 thread Store(长期 namespace 持久) | 是**运行时框架**(要起进程/写代码),我是纯文件式 |

---

## 0.C 全域五问机制提炼（读完 10 个真同类后的横向归纳 —— 直接驱动 Round 2 续跑设计）

**① 自动捕获 vs 显式写**:**分两派**。自动捕获派(claude-mem/claude-remember/compiler/rohitg00)= hook(PostToolUse/Stop/SessionEnd/PreCompact)静默抓 + LLM 压缩;显式派(hanfang/Light)= 关键事实人/agent 显式写。**Light=显式派**(hanfang 印证可行)。claude-remember 的"工具增量超阈值自动存"是中间路,但仍要后台 LLM(要 key)。诚实:**自动捕获是高 star 主流**;Light 选显式因**零 key + 可审计 + 不被 LLM 误删/误并**,代价是要人维护。

**② 会话开头续上(核心,对标第 2 件)**:**人人都做**,但两种机制——(a) **hook 式**(仅 CC:claude-mem/remember/compiler/rohitg00 的 SessionStart);(b) **命令/约定式**(跨 harness:jayzeng `agent-memory context` 命令、agent-handoff 的 AGENTS.md/CLAUDE.md→读文件约定)。**这是 R4.e/落后项 #4 的钥匙**:跨 harness 玩家**都不靠 hook**——要么一条确定性命令、要么"约定读单文件"。Light 批 0 只有 CC hook + 对 Codex/OpenCode 一句模糊的"模型自己读 passport"。**Round 2 改造**:学 jayzeng 加 **`pm.py resume` 确定性命令** + 学 agent-handoff 把"startup 跑该命令"写进 AGENTS.md/CLAUDE.md 约定 → 三 harness 跑**同一份**确定性续跑报告(CC hook 自动调它 / Codex·OpenCode 显式调它)。

**③ 检索**:重派(claude-mem/rohitg00 向量+图+RRF、jayzeng 语义模式)vs 字面派(hanfang grep、jayzeng 关键词 BM25)。**对落后项 #1 的关键校正**:本地 embedding 语义检索**可以无 key**(jayzeng 的 `qmd` 用本地 all-MiniLM,"no API keys needed")——故批 0 把"无向量"归因于"对标 mem0 要 key"**不够准**;真正原因是**向量模型/二进制是重的非-stdlib 依赖**,破坏"stdlib 优先 + 三 harness 零额外装"。Light 仍走 Grep 字面,但诚实理由要更新为"避重依赖"而非"避 key"。

**④ 压缩/摘要长历史**:claude-remember 分层(原始→每时→日→recent 7 天→archive)、claude-mem/compiler LLM 编译。**Light 不自动压缩**:靠 append-only `decision_log`/`version_history` + 交接卡 + `archived:` 归档。claude-remember 的 recent/archive 分层**验证我 `archived:` 设计**。诚实差:无自动摘要(要 LLM);长历史靠人写的交接卡 + 渐进披露(会话开头只给紧凑续跑摘要,要细节再翻文件——学 claude-mem 3 层)。

**⑤ 跨工具/跨 harness 可移植**:三种范式——每平台装+MCP(claude-mem/rohitg00,重)/ 共享目录+每 harness SKILL+确定性命令(jayzeng)/ repo-local 文件+AGENTS.md·CLAUDE.md 约定(agent-handoff)。**Light 的合成**:取 jayzeng 的**确定性命令模型** + agent-handoff 的**约定模型** + Light 独有的**机器校验层**(10 个真同类**无一**机检台账自洽——日期/链路/版本对齐/快照/孤儿产物)。这就是 Light 在"约束内"能比它们更顶的点。

---

## 1. 横切可借机制（已落进 v2 memory-pm；★=Round 2 新增/强化）

1. **"会话开头读全量项目记忆 + 确定性续上"**(Cline "read ALL at start" / Roo / jayzeng / agent-handoff):→ CC 复用 **SessionStart hook** 确定性注入;**★ Round 2 新增 `pm.py resume`**——把续跑汇报抽成 memory-pm 自有的**确定性命令**(纯 passport 依赖),hook 反过来调它(DRY,单一真相源),Codex/OpenCode 经 AGENTS.md 约定显式调它 → **三 harness 同一份报告**。`project_card.next_actions` 是"上次到哪/下一步"首读字段。
2. **"决策发生即追加、不可变时间线"**(Roo decisionLog + ADR):→ `decision_log.md` 单行 ADR,只追加;`check_project_card.py` 的 LINE_FORMAT + ABS_DATE 机检。
3. **"版本史 ↔ git tag 必对齐"**(Keep a Changelog + git):→ `version_tag_reconcile.py` 双向失配,`--tags` 可离线/CI。
4. **"先定义后生产 + 单一事实源 + 变更广播"**(SSOT/docs-as-code):→ `terminology.md` + `consistency/*.yaml` 归 memory-pm 维护;`pm.py broadcast` 算受影响材料 + 发 consistency 回扫。
5. **"两件套交接 + 自传播 + 链可追溯"**(superpowers handoff / agent-handoff):→ `handoff_card.md`(`.light/handoff/S<NN>-*.md` 带 parent_session 链)+ `handoff_prompt.md`;**HANDOFF_CHAIN** 机检链可达——比它们多"链结构校验"。
6. **"两层记忆作用域"**(LangGraph Store / mem0 scoping):→ 会话级(短期、随压缩可丢)vs 项目级(`.light/` 长期持久);**SSOT 决策表**治"两头都写造成漂移"。
7. **"完结归档防膨胀 + 分层时效"**(PARA Archives / claude-remember recent·archive):→ 项目归档协议(`archived:` 字段、会话开头跳过、回写 lessons)。
8. **★ "渐进披露"**(claude-mem 3 层):→ 续跑汇报会话开头只给**紧凑摘要**(项目/阶段/卡门/下一步),要细节再翻 `.light/` 具体文件——不一次灌爆上下文。

---

## 2. 超越点（v2 相对裸模型 / 竞品 / v1 的真增量）

- **裸模型本就会**写"记住项目背景""会话开头先读上次进度""相对日期转绝对""决策留痕"——**近零增量,不吹**。
- **相对全部 10 个真同类的真增量 = 机器可验证的台账纪律(它们无一有)**:claude-mem/rohitg00 检索华丽但**零台账校验**;agent-handoff 结构化但**零校验**;hanfang/jayzeng 轻量但**无项目状态/门/版本校验**。Light 独有:
  1. **`check_project_card.py`**:绝对日期 / current_stage 枚举 / 行格式 / **HANDOFF_CHAIN**(parent_session 可达·无悬挂·无环)——它们只"叫模型保持准确",我**机检准确**。
  2. **`version_tag_reconcile.py`**:version_history ↔ git tag 双向失配——Keep a Changelog 没有执行。
  3. **`check_bfact_freshness.py`**:外部可变事实裸数值无快照报 `BARE_NUMBER`、超期报 `STALE`——把"用前重核"从口头变机检。
  4. **复用 passport 指纹/stale-check**:孤儿/缺失 artifact、上游变动需重验,从"人肉记"变"可计算"。
  5. **`memory_items.py` / `memory_governance_gate.py` 隐私边界**:公开可传播的 `.light/` ledger 拒绝 restricted/secret、疑似 PII、邮箱/电话/身份证、本机绝对路径、原始多轮对话和过长原文式 value——把"别把私人内容写进仓库"从提醒变成可失败的闸门。
- **★ 跨 harness 确定性续跑(Round 2 新增)**:jayzeng 有确定性 `context` 命令(近),但它是"记忆 dump + 搜索";**Light 的 `pm.py resume` 报的是机器校验过的 DAG 项目态**(当前阶段/卡哪门/最小 stale 重验范围/下一步),且**三 harness 同一份**——"续跑"从"装了 CC hook 才有"变成"建了 `.light/` + 一条命令就有"。**确定性续跑 × 机器校验台账,二者合一,10 个真同类无一兼得**。
- **相对 v1 的真增量**:去知识库(db09→`.light/`)、复用 passport 引擎(不重造)、变更广播落成机制、产 `light.findings.v1` 但仅限"台账自洽门"。

---

## 3. 诚实边界（已知做不到 —— 写进 SKILL 名实对齐，绝不掩饰）

1. **无向量语义检索 / 无自动记忆抽取**:跨会话记忆靠 `.light/` 显式文件 + hook/命令注入 + **Grep 字面**检索,不做 embedding 召回——"同义不同词"会漏召回(如"级联误差抑制"↔"逐级不确定性消除");也**不自动抽取**(关键事实必须显式写)。**★ 校正(Round 2)**:本地 embedding 语义检索**可无 key**(jayzeng `qmd` 用本地 all-MiniLM 实证),故真正不做的原因是**向量模型/二进制是重的非-stdlib 依赖**,破坏"stdlib 优先 + 三 harness 零额外装 + 可审计",**不是"避 key"**。这是刻意取舍:可审计、不被 LLM 误删/误并,代价是要人维护。
2. **状态覆盖式更新会丢演化轨迹**:`project_card` 的 `*_status` 覆盖式改写,A→B 转移只在 `decision_log` 留痕(非结构化);未做 mem0 式"每次状态变更结构化保留"。
3. **校验是正则启发式,会漏/误报**:`check_bfact_freshness` 按关键词+数字识"可变事实";隐私/PII/原始对话识别也只是安全启发式,不能替代人工判断;行格式/枚举校验同此局限;阈值(90/365 天)是经验默认可调。
4. **跨会话"会话开头确定性续上"——Round 2 已大幅缩小,但仍有 harness 差**:
   - **★ 已做到**:`pm.py resume` 是**三 harness 通用的确定性命令**,仅凭 `.light/` 即出正确续跑汇报(项目/阶段/卡门/重验/下一步),**已活体 E2E 验**(不依赖 CC hook,见 `references/cross_harness_resume.md` + selftest)。
   - **仍诚实标的差**:① CC 由 **SessionStart hook 自动**调 `pm.py resume`(harness 强制、零人力);Codex/OpenCode **无 session-start hook**,要靠 AGENTS.md 约定让模型**在会话开头主动跑**该命令——命令本身确定性,但"何时触发"在 Codex/OpenCode 仍是**模型读约定**(非 harness 强制),故 CC 的"自动"程度更高。② Codex/OpenCode 的真机实测受限于本地无该 harness;**已验**的是"仅凭 `.light/` + 该命令能产出正确续跑"(harness 无关),**未能在真 Codex/OpenCode 进程里端到端验**的部分如实标注,绝不声称"三 harness 都已实测自动续跑"。
5. **账本自洽门 ≠ 科研内容门**:`pm.py audit` 产的 findings 只判台账自洽,不判科研质量;不进 STAGE_GATES 常开阻断,只在交接/投稿前按需聚合。
6. **变更广播只算"该回扫谁"+ 发指令,不自己审计**:查不一致是 consistency 的事(职责分离)。
7. **不替用户拍板归档/教训去偏科化**:归档点、lessons 是否回写、去偏科化措辞,都起草 + 停下问用户(决策点)。
8. **无项目目录的轻对话不落交接卡**:只打印启动提示词(记忆无处安放,靠提示词单件传状态)。

---

## Round 3 五席纠偏与未决问题置顶（2026-07-05）

105 项矩阵原第 2 席 Khoj 是通用个人知识库/检索产品，不是专职跨会话项目记忆 skill。
现替换为 `rohitg00/agentmemory`：父仓当前 24,565★、Apache-2.0，固定
`93ae9bc04f3ab5042f982aaadf11f1e3f5137531`。本轮重新完整读取五个直接入口：

- `recall`（60 行）：BM25 + vector + graph hybrid search；零结果时不猜；
- `session-history`（61 行）：逐 session 真实时间线，不合并或虚构；
- `handoff`（68 行）：按目录边界选最近 session，**先呈现未回答问题**；
- `commit-context`（64 行）：commit 找不到 session link 就明确 unknown；
- `agentmemory-architecture`（33 行）：capture/compress/consolidate/forget 生命周期。

Light 不迁移它的 SQLite/embedding/graph/MCP/server，但其“resume 时先处理未回答问题”暴露了
真实缺口：旧交接卡只有 blockers/next steps，没有机器可读的 user-facing question。现把
`contract_version: 2`、decision id、完整问题、两个带后果选项写进 handoff contract，并让
`pm.py resume` 与 SessionStart resident 从最新卡置顶显示。旧 v1 卡只给兼容性 warning，
不会因升级突然失效；新卡缺该节则 fail。

## 4. 待补深读（诚实，非已读充分）

- **claude-mem(83.8K★)的 SessionStart hook 源码**(`src/` / `cursor-hooks/`)逐行——已读 README+5 hook 名+安装命令,未逐行读其注入实现;其"3 层渐进披露"的 token 预算控制可再深挖,但重机械(MCP/Chroma)我不搬。
- **jayzeng `agent-memory context` 的 SKILL.md 全文**(本轮分类器 flapping 未取到逐行;已从仓库总览核到命令 `agent-memory context` / `!agent-memory context --no-search` + 每 harness 安装路径)——其"每回合前注入"的触发措辞可参照优化我 AGENTS.md。
- **rohitg00 的 `write-agentmemory-skill` reference skill**——"怎么写一个记忆 skill"的元技能,可对照我 SKILL 手艺,低优先。
- Cline `temporal-memory-bank.md`、Roo `memory_bank_strategy_*.yml`(已定位未逐行)、MADR 完整字段、MemMachine(arXiv **2604.04853**,后截止)状态保留实现——批 0 已列,维持低优先。
- DVC/MLflow/W&B 实验版本血缘——属"管理工具映射",memory-pm 只做指针登记不接 API(零 MCP/key)。
