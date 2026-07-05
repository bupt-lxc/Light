# Orchestrator Round 2 与 21 技能集成验收

日期：2026-07-03 至 2026-07-04

基线：`77434950fdfad8369ecb797061ea01b3bd15c65b`（`main`，开工时 clean）

范围：只改 orchestrator 契约、脚本、resident、对标、设计规范与本证据；未改 20 个已收口技能实现。

## 结论

- orchestrator Round 2 完成。canonical state 升级为 `light.passport.v3`，带版本、
  显式迁移、内容 hash、证据状态、freshness、交付授权和 hash-bound handoff。
- 21 技能机械集成审计通过：13 个科研 stage、5 个常驻角色、2 个按需工程
  off-DAG、1 个 controller；实时 `STAGE_GATES` 与 `ROUTES` 和契约一致。
- `frontend-design`、`system-design` 没有 stage/findings/gate/route；`project-structure`
  与 `file-reading` 是 overlay/off-DAG 边界，不被塞进主线。
- 真实生命周期 E2E 完整闭环：critical → checkpoint fail → reroute
  suggestion → 停下问用户 → 用户授权 8→7 → 修复 → checkpoint pass → stale/
  resume/handoff → 再次停下取得最终交付授权 → `DELIVERED`。
- 最终声明 selftest 在正确 harness 下 `124/124` 通过；orchestrator 的
  skill-creator quick validation 通过。

## R1：真同类重学

star 固定于 2026-07-03，commit 为当天仓库 HEAD。每项均读了完整 `SKILL.md`；
有配套 reference/script/template 的也实际读取，不用框架或文章凑数。

| 真同类 skill | repo / star / fixed commit | 已读配套资源 | 落地机制 |
|---|---|---|---|
| dispatching-parallel-agents | obra/superpowers · 245,221★ · `d884ae04edebef577e82ff7c4e143debd0bbec99` | 仅 SKILL | 独立分支才并行，join 后验冲突 |
| subagent-driven-development | obra/superpowers · 245,221★ · `d884ae04edebef577e82ff7c4e143debd0bbec99` | implementer/reviewer prompts、`task-brief`、`review-package`、workspace | durable ledger 与 hash handoff |
| executing-plans | obra/superpowers · 245,221★ · `d884ae04edebef577e82ff7c4e143debd0bbec99` | 仅 SKILL | blocker/重复失败时停下，不猜 |
| task-coordination-strategies | wshobson/agents · 37,472★ · `5cc2549a50fc672230efd0a0307e2fd27ffba792` | dependency graphs、task decomposition | blockedBy、critical path、fork/join |
| team-communication-protocols | wshobson/agents · 37,472★ · `5cc2549a50fc672230efd0a0307e2fd27ffba792` | messaging patterns | approval ID、shutdown/handoff |
| parallel-feature-development | wshobson/agents · 37,472★ · `5cc2549a50fc672230efd0a0307e2fd27ffba792` | file ownership、merge strategies | producer/consumer 单归属 |
| using-agent-skills | addyosmani/agent-skills · 68,718★ · `8c6530305396f341b5da7201cf1f7e390fdb863f` | 仅 SKILL | task-phase routing 与 verify |
| planning-and-task-breakdown | addyosmani/agent-skills · 68,718★ · `8c6530305396f341b5da7201cf1f7e390fdb863f` | 仅 SKILL | dependency graph、human checkpoint |
| memory-lifecycle | basicmachines-co/basic-memory-skills · 22★ · `6d2b1d426d0dacf020aef45f029768c9d8c1e5e5` | 仅 SKILL | new/partial/paused/completed/revert |
| mastering-langgraph | SpillwaveSolutions/mastering-langgraph-agent-skill · 36★ · `a6069daa9b11e58f98057a5ce49b87a4ae799082` | workflow、HITL、persistence、multi-agent refs | checkpoint/resume/interrupt 语义 |

框架/SDK/产品另表研究了 LangGraph、OpenAI Agents SDK、Microsoft Agent
Framework、Temporal、Claude Code Agent Teams；论文/经验另表研究了
AI-Scientist、ResearchAgent、Agent Laboratory、co-scientist、MetaGPT、Co-STORM。
它们只作机制锚，不占上述十个 skill。

旧结论逐条撤回：

- 非线性 DAG、回边、fork/join、checkpoint 在同类中都常见，不独有。
- passport、resident、memory lifecycle 与 HITL 也不是独有。
- critical gate 和用户 decision stop 普遍存在。Light 的实际增量收窄为：
  科研 stage 契约、findings producer/consumer、合法早向边、用户授权 ID、revision
  budget、证据状态与本地文件式跨 harness 降级。

完整行号、链接及分表见
[`docs/competitors/orchestrator.md`](../competitors/orchestrator.md)。

## R2：canonical 生命周期

### 状态与角色

- intake 七态：`new|resume|partial|dirty|failed|stale|delivered`；可同时保留 flags，
  但 dirty、failed、stale 的恢复动作有明确优先级。
- `.light/passport.yaml` 是唯一 canonical project state；聊天、文件存在或
  resident 文本都不能覆盖它。
- v1/v2 只可显式 `migrate` 到 v3。legacy 回边缺授权时写 `UNKNOWN`，不伪造授权。
- `state_revision` 每次保存递增；`state_hash` 对规范化内容做 SHA-256，支持 YAML
  `date` 类型；artifact freshness 对路径与实际字节做 SHA-256，不再信 mtime。
- pipeline node、resident overlay、engineering off-DAG 三类角色分开；passport
  stage 的 `node_kind` 只允许 `pipeline`。
- 证据词表固定为
  `VERIFIED|PLANNED|UNKNOWN|UNAVAILABLE|FAILED`。

### gate、路由与用户权限

- findings 由各技能生产，`run_checkpoint.py` 聚合并把新鲜 hash/timestamp、状态、
  artifact、上游 fingerprint 与 `next_action` 写回。
- reroute 始终只建议；`passport.py add-back-edge` 要求
  `authorization_id`，且只允许 `to < from`。
- `2⊣3` 是 `admission_hold`，不是 2→3 或 3→3 back-edge。
- 根因 stage 的 `revision_rounds` 真正随回边写回；超过 2 轮拒绝落账，转
  known limitation 决策。
- `delivery_status=DELIVERED` 必须同时有 `delivery_authorization_id`；只有
  recorded stages 都 delivered 不足以宣称项目已交付。

### resident 与 access

- resident discipline budget 4,200 字符，resume 5,400，总上限 9,800。
- harness 不支持 hook、passport 损坏或读取失败时注入 `UNAVAILABLE`/修复指针，
  不冒充三种 harness 能力相同。
- 本地免费核心路径只依赖 Python 与仓库文件；公开 API、需登录、机构订阅、付费
  资源分层，缺失时保持 `UNAVAILABLE`。

## 21 技能机械 integration inventory

由 `integration_audit.py` 从每个 `SKILL.md`、resource map、实际脚本与
`--selftest` 声明抽取，再对照 `integration-contract.json` 和实时 gates/routes。

| skill | role | stage | findings | consumer / decision stop |
|---|---|---:|---|---|
| light-literature-search | pipeline | 1 | yes | idea generation/critique；方向选择 |
| light-data-engineering | pipeline | 2 | yes | stage 2/3 admission；数据不足停下 |
| light-idea-generation | pipeline | 3 | yes | idea critique；候选选择 |
| light-idea-critique | pipeline | 4 | yes | checkpoint/reroute；idea 放行或 4→3 |
| light-research-plan | pipeline | 5 | yes | checkpoint；方案授权 |
| light-experiment-coding | pipeline | 6 | yes | checkpoint/result；不安全或不可复现 |
| light-result-analysis | pipeline | 7 | yes | checkpoint/writing/figure；7→5/6 |
| light-paper-writing | pipeline | 8 | yes | checkpoint/citation/figure；8→7 |
| light-figure | pipeline | 9 | yes | checkpoint/typesetting；9→7 |
| light-citation | pipeline | 10 | yes | checkpoint/typesetting；stage 内修 |
| light-typesetting | pipeline | 11 | yes | checkpoint/venue；stage 内修 |
| light-venue-matching | pipeline | 12 | yes | 用户决策包；无 gate/route |
| light-review-rebuttal | pipeline | 13 | yes | checkpoint/reroute；13→3/5/8 |
| light-memory-pm | overlay | — | yes | handoff/delivery ledger |
| light-project-structure | overlay-off-dag | — | no | 本地树；授权 move/rollback |
| light-consistency | overlay | — | yes | 当前 stage checkpoint |
| light-research-ethics | overlay | — | yes | 当前 stage checkpoint |
| light-file-reading | overlay-off-dag | — | no | requesting skill；覆盖限制 |
| light-frontend-design | engineering-off-dag | — | no | 软件项目；设计/技术栈选择 |
| light-system-design | engineering-off-dag | — | no | 软件项目；架构/变更授权 |
| light-orchestrator | controller | — | no | 用户与 passport；所有方向/交付决策 |

审计确认没有：

- stage 缺失/重复/错位；
- 无消费者 findings；
- system-design findings 或 gate/route；
- overlay/engineering off-DAG 混入主线；
- self/forward back-edge；
- gate/route 指向非 pipeline 角色。

实时 gates：

| stage | gates |
|---:|---|
| 2 | `split_leakage,data_feasibility` |
| 3 | `idea_collision,pseudo_diversity,frame_lock` |
| 4 | `collision,fatal_flaw,anti_sycophancy` |
| 5 | `fair_baseline,falsifiable` |
| 6 | `leakage,reproducible` |
| 7 | `stat_validity,evidence_strength` |
| 8 | `claim_evidence,overclaim` |
| 9 | `visual_honesty,misrepresent_evidence` |
| 10 | `citation_verify` |
| 11 | `compile,desk_reject` |
| 13 | `reviewer_classify` |

实时 routes：`2⊣3 admission_hold`；back-edge 为 `4→3`、`7→6`、`7→5`、
`8→7`、`9→7`、`13→3`、`13→5`、`13→8`。

## 真实生命周期 E2E

项目：`.upgrade/_e2e/orchestrator-round2/lifecycle`（提交前删除）。

1. 新建 cropped stage 7→8 passport；stage 7 有 evidence artifact，stage 8
   依赖 7。
2. 调用 consistency overlay，得到 `AUTHORITY_COVERAGE` warn；调用
   system-design off-DAG `contract_validate.py`，6 个 example 为 `VERIFIED`，
   因 `openapi-spec-validator` 不可用整体诚实为 `STRUCTURE_ONLY`/exit 2。
   二者都没有成为 stage。
3. paper-writing 对“significantly outperforms/proves”且无逐 claim 绑定的草稿产生
   `claim_evidence` critical；stage 8 checkpoint exit 1、status=`gate_failed`。
4. `reroute.py` 建议 8→7，quota 0/2，passport 回边数仍为 0；在对话中停下。
5. 用户于 2026-07-04 回复“授权”。随后才以
   `authorization_id=user-message-2026-07-04-authorized-8-to-7`
   落账；stage 7=`needs_rework`、revision 1/2。
6. `stat_rigor_gate.py` 真消费 9-seed CSV，产 result findings 与
   `evidence_strength.json`。证据为 weak，因此把 draft 改成 `may suggest` 并用
   `light.paper_claims.v1` 精确绑定，未伪装 strong。
7. stage 7 checkpoint exit 0；paper gate exit 0；stage 8 checkpoint exit 0。
8. 修改上游结果并重产 evidence 后，stage 8 被内容 hash 判 `stale`，
   intake 给 `need_reverify=[8]`；置 in-progress 后 flags 同时含 resume/stale。
   重验后 stage 8 `fresh`。
9. 旧 handoff 因 passport hash 变化验证 `FAILED`；刷新后的 handoff
   `VERIFIED`，next action 为准备下一 dependency-ready stage 或 delivery decision。
10. delivery 不能从两个 cropped stage 的文件/状态推断；再次停下后，用户于
    2026-07-04 明确回复“授权”，随后才用
    `authorization_id=user-message-2026-07-04-final-delivery-authorized`
    执行 `authorize-delivery`。intake=`delivered`，旧 handoff 因 hash 改变失效，
    最终 clean handoff 验证通过并保留 weak evidence 已知限制。

E2E 暴露并修复的非预设 orchestrator 问题：

1. `STAGE_GATES` 的 producer 名已过时，且 `ROUTES[3]` 生成非法 3→3；
   同时 2⊣3 被误建成 back-edge。
2. `add-back-edge` 没把 round 写回 target，跨会话可无限刷新 quota。
3. flow YAML 中多 gate 值含逗号未加引号，回读成伪 key，导致 v3 hash 损坏。
4. checkpoint 成功后未刷新 artifact/upstream fingerprint，freshness 无法闭环。
5. checkpoint 后 `next_action` 残留 in-progress，handoff 动作建议过期。
6. PyYAML 把裸日期读成 `datetime.date`，canonical JSON hash 在 memory-pm
   selftest 崩溃；现统一 ISO-8601 规范化。

上游已知限制：合成 paired 数据差值零方差，result-analysis 产出极大
`cohens_dz`；其证据档仍诚实为 weak。本棒未越界改 result-analysis，只降级写作措辞并记录。

## 回归证据

### 首次运行必须保留的失败

- 开工基线共 122 个声明 selftest。Windows 默认编码首跑：
  121 pass / 1 fail；唯一失败是
  `light-frontend-design/scripts/ai_tell_lint.py` 输出 emoji 时
  `UnicodeEncodeError`（GBK）。未改上游；`PYTHONUTF8=1` 重跑为 122/122。
- 最终第一次机械验收为 122/124：
  - `_shared/__main__.py` 被误按普通文件执行；仓库明确要求 `python -m _shared`，
    修验收器调用方式。
  - memory-pm 暴露 YAML `date` 令 passport v3 hash 崩溃；修 canonical normalization。
- 正确 harness 全量重跑：124/124，含
  `C:\Program Files\R\R-4.6.0\bin\Rscript.exe` 的 R selftest 与
  `python -m _shared`。

### 静态与格式验证

| 验证 | 结果 |
|---|---|
| `python -m _shared` | exit 0 |
| `python -m compileall -q skills _shared` | exit 0 |
| 全仓 JSON/YAML parse | 38 files，0 error |
| JSON Schema meta-validation | 2 schemas，0 error |
| passport template 对 v3 schema | valid |
| `integration_audit.py --selftest` | pass |
| orchestrator 六个 selftest | pass |
| skill-creator quick validation：orchestrator | valid / exit 0 |

全 21 技能跑当前 skill-creator quick validator 时为 7 pass / 14 fail。14 项全因
既有顶层 `user-invocable` 已不在当前 validator allowlist；在基线 `7743495` 中这 14/14
已存在，本棒未改。它不是 orchestrator 契约/路由责任，按保护边界不批量改上游。

## 可复跑命令

```powershell
$env:PYTHONUTF8='1'
python skills/light-orchestrator/scripts/integration_audit.py --selftest
python skills/light-orchestrator/scripts/integration_audit.py --markdown
python skills/light-orchestrator/scripts/passport.py --selftest
python skills/light-orchestrator/scripts/passport.py authorize-delivery --help
python skills/light-orchestrator/scripts/run_checkpoint.py --selftest
python skills/light-orchestrator/scripts/reroute.py --selftest
python skills/light-orchestrator/scripts/lifecycle.py --selftest
python skills/light-orchestrator/resident/session_start_resident.py --selftest
python -m _shared
python -m compileall -q skills _shared
python "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" `
  skills/light-orchestrator
git diff --check
```

## 已知限制

- resident 注入依赖 harness 能否提供 SessionStart hook；不能提供时只能降级为显式调用，
  状态为 `UNAVAILABLE`。
- passport 是本地单写者文件台账，没有分布式事务；并行分支必须先分配 ownership，
  join 时由 controller 单点写回。
- quick validator 的 14 个上游 `user-invocable` 兼容问题待后续独立批次处理。
- system-design E2E 的 OpenAPI package 在当前主 Python 环境不可用，仅验证结构/examples，
  未外推完整 OpenAPI 合规。
- known limitation 与最终 delivery 都是用户决策；revision budget 到顶或文件齐全不会自动授权。
