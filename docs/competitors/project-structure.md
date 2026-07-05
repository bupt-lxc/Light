# project-structure Round 2 对标真相源

核查日：2026-07-03。Stars 为核查当日 GitHub API
`stargazers_count`；机制锚固定到 commit，不用漂移的 `main` 行号。skills.sh
安装量只作发现线索，不拿工具主页或 README 顶“真同类 skill”数量。

## 结论先行

旧结论不成立：

- Cookiecutter 本体偏生成，但不能把 Cookiecutter、Copier、Cruft、
  PyScaffold、CCDS 全写成“只生成”。Copier 有 update/check-update、
  migrations 与冲突策略；Cruft 有 check/diff/update/link；PyScaffold 有
  `putup --update`、`pretend` 与 update/force 写入规则。
- “生成 + 审计”不是 Light 独有。下面的
  `ln-646-project-structure-auditor` 真做已有代码库结构审计；Patina
  `scaffold-repository` 对现有仓逐项 audit、diff preview、accept/skip/defer；
  `harness-init` 先 discovery，再为已有违规建 ratchet baseline。
- raw 不可变、DAG、标准目录、命名、`.gitignore`、README、pre-commit、
  小数据可入 Git、大数据走远端/DVC，早已是 CCDS、DVC、科研软件规范和多项
  skill 的常见能力。
- “23 目录 + 7 模板”是固定意见树，不是通用能力。CCDS 自己也说目录名称不如
  数据流重要，并鼓励按项目删、增、重组。对 R、mixed Python/R/LaTeX、
  paper-only 与 monorepo 强套该树会误导。

Light Round 2 的可验证窄增量是：**一个纯本地 stdlib 生命周期把 Git/非
Git/monorepo-subroot intake、canonical inventory、显式 policy、plan digest
授权、逐文件 hash move、rollback/reapply 证据与 `.light/` 所有权边界捏在一起**。
各组成能力并不独有，组合也不宣称全球唯一。

Round 3 续补（2026-07-05）：后续复核发现 applied manifest 虽记录
`plan_sha256` 与 authorization canonical digest，但没有记录当次 `apply` 实际读入的
migration-plan 文件和 authorization 文件的 raw 字节哈希。新机制在
`applied-manifest.json` 写入 `plan_binding` 与 `authorization_binding`
（locator + file SHA-256 + plan/authorization digest），并让 governance gate 在
apply 交付包中强制看到这些绑定。这个补丁不证明目录结构更优，只防止移动证据脱离当时那份计划/授权文件。

Round 3 五席纠偏（2026-07-05）：105 项矩阵原第 5 席把 Copier + Cruft +
PyScaffold 三个工具拼成一席，只能证明模板演进成熟，不能算同功能 agent skill。现替换为
`Gizele1/harness-init`：父仓当前 47★、MIT，固定
`71d48b2ec74768d6bcd96afb68376e0d5c9c4fea`。本轮重新完整读取 260 行 SKILL、
65 行 stack-routing、250 行 boundary-test-template 与 54 行 gc-patterns，确认它直接覆盖
mandatory discovery、现有仓 stack/monorepo 识别、KNOWN_VIOLATIONS baseline/ratchet、
逐 phase checkpoint 和“文件存在不等于完成”。

这些机制已被 Light 的 observed signatures、existing-custom profile、report-only intake、
plan/hash authorization、apply manifest 与 rollback 覆盖。harness-init 会进一步创建 CI、
边界测试和 GC 工件，超出 project-structure 的安全整理边界，因此不照搬；本轮只纠正五席口径，
不为凑改动重复造 baseline。

## A. 真同类 skills（10 项，工具不计入）

### 1. folder-structure-blueprint-generator

- Repo：[`github/awesome-copilot`](https://github.com/github/awesome-copilot)，
  **36,122★**；skills.sh 当日 9,009 installs。
- 固定锚：
  [`e986f49/skills/folder-structure-blueprint-generator/SKILL.md`](https://github.com/github/awesome-copilot/blob/e986f49695491311df2774030ebe11efabd0fb77/skills/folder-structure-blueprint-generator/SKILL.md#L1-L82)。
- 真读机制：先以项目标志文件自动识别 .NET/Java/React/Angular/Python/
  Node/Flutter，再识别 monorepo、microservices 与 frontend；后续生成结构
  blueprint、命名/文件放置/扩展模板。
- 可借点：profile 必须从现状探测，不从单一 Python 模板出发。
- 差距：它产文档，不产 canonical hash inventory、授权 move 或 rollback。

### 2. python-project-structure

- Repo：[`wshobson/agents`](https://github.com/wshobson/agents)，
  **37,461★**；skills.sh 当日 10,074 installs。
- 固定锚：
  [`5cc2549/.../python-project-structure/SKILL.md`](https://github.com/wshobson/agents/blob/5cc2549a50fc672230efd0a0307e2fd27ffba792/plugins/python-development/skills/python-project-structure/SKILL.md#L1-L83)。
- 真读机制：既触发新建也触发 reorganizing existing codebase；在 flat、
  layered、domain-driven、colocated/parallel tests 之间给选择，而非只给一棵树。
- 可借点：profile 是决策空间，不是目录数量 KPI。
- 差距：指导性 skill，无盘点脚本与安全迁移证据。

### 3. monorepo-management

- Repo 同上，**37,461★**；skills.sh 当日 10,873 installs。
- 固定锚：
  [`5cc2549/.../monorepo-management/SKILL.md`](https://github.com/wshobson/agents/blob/5cc2549a50fc672230efd0a0307e2fd27ffba792/plugins/developer-essentials/skills/monorepo-management/SKILL.md#L1-L58)
  与
  [`references/details.md`](https://github.com/wshobson/agents/blob/5cc2549a50fc672230efd0a0307e2fd27ffba792/plugins/developer-essentials/skills/monorepo-management/references/details.md)。
- 真读机制：覆盖 multi-repo→monorepo 迁移、workspace、依赖图、缓存、发布；
  将 apps/packages 与包级 README/test/release 策略分开。
- 可借点：审计子根时必须记录 Git root 与 scope，不能把根仓路径误当项目相对路径。
- 差距：以 JS/TS monorepo 为主，不处理科研数据 policy 或文件级回滚。

### 4. ln-646-project-structure-auditor

- Repo：
  [`levnikolaevich/claude-code-skills`](https://github.com/levnikolaevich/claude-code-skills)，
  **506★**；skills.sh 当日 367 installs。
- 固定锚：
  [`2b1b61c/.../SKILL.md`](https://github.com/levnikolaevich/claude-code-skills/blob/2b1b61c7f69db746f7e160438f18f2a3379f92a2/plugins/codebase-audit-suite/skills/ln-646-project-structure-auditor/SKILL.md#L18-L67)，
  配套
  [`structure_rules.md`](https://github.com/levnikolaevich/claude-code-skills/blob/2b1b61c7f69db746f7e160438f18f2a3379f92a2/plugins/codebase-audit-suite/skills/ln-646-project-structure-auditor/references/structure_rules.md)
  与
  [`two_layer_detection.md`](https://github.com/levnikolaevich/claude-code-skills/blob/2b1b61c7f69db746f7e160438f18f2a3379f92a2/plugins/codebase-audit-suite/skills/ln-646-project-structure-auditor/references/two_layer_detection.md)。
- 真读机制：已有仓库两层检测（candidate scan→context verification），按已探测
  stack 才套框架规则；输出带 evidence/location/action/effort 的报告，明确
  report-only、绝不 move/delete。
- 可借点：先识别 intended structure，再判断 drift；小项目/混合布局允许例外。
- 差距：依赖其 audit suite/MCP 契约，无本地 move/rollback。

### 5. project-init

- Repo：
  [`a-green-hand-jack/ml-research-skills`](https://github.com/a-green-hand-jack/ml-research-skills)，
  **8★**；skills.sh 当日 55 installs。
- 固定锚：
  [`a761250/skills/project-init/SKILL.md`](https://github.com/a-green-hand-jack/ml-research-skills/blob/a7612508c3de6526814be790e6748c519c0619bd/skills/project-init/SKILL.md#L17-L115)。
- 真读机制：研究项目 control root 下 paper/code/slides 可为独立 repo，显式问
  new/connect/skip、root Git、submodule、worktree、环境、可见性与远端策略；
  根 Git 可选，避免意外提交 nested repos。
- 可借点：mixed research 不能简化成一个 Python package；交付物与协作者可见性
  决定树。
- 差距：其 memory/board 所有权与 Light 不同，不能抄进 project-structure；
  本轮 `.light/` 内容仍归 memory-pm。

### 6. init-python-project

- Repo 同上，**8★**；skills.sh 当日 51 installs。
- 固定锚：
  [`SKILL.md:L56-L77`](https://github.com/a-green-hand-jack/ml-research-skills/blob/a7612508c3de6526814be790e6748c519c0619bd/skills/init-python-project/SKILL.md#L56-L77)、
  [`L273-L328`](https://github.com/a-green-hand-jack/ml-research-skills/blob/a7612508c3de6526814be790e6748c519c0619bd/skills/init-python-project/SKILL.md#L273-L328)；
  配套脚本
  [`scaffold_new_project.py:L35-L77`](https://github.com/a-green-hand-jack/ml-research-skills/blob/a7612508c3de6526814be790e6748c519c0619bd/skills/init-python-project/scripts/scaffold_new_project.py#L35-L77)
  和 `templates/`、`template_manifest.json`。
- 真读机制：new 与 fork/existing 分流；existing 先 inspect，批准后 surgical edit，
  不强套全 ML layout，不替换已有健康 toolchain。新建脚本通过 manifest 物化模板，
  非空目标直接拒绝。
- 可借点：greenfield 的 profile/template 与 existing migration 必须是两条路径。
- 差距：existing 路径主要靠 agent 操作，未给文件级 plan digest/hash rollback。

### 7. init-latex-project

- Repo 同上，**8★**；skills.sh 当日 56 installs。
- 固定锚：
  [`a761250/skills/init-latex-project/SKILL.md`](https://github.com/a-green-hand-jack/ml-research-skills/blob/a7612508c3de6526814be790e6748c519c0619bd/skills/init-latex-project/SKILL.md)；
  真读配套
  [`scripts/init.sh`](https://github.com/a-green-hand-jack/ml-research-skills/blob/a7612508c3de6526814be790e6748c519c0619bd/skills/init-latex-project/scripts/init.sh)
  与 `templates/venues/{acl,acm,cvpr,eccv,emnlp,iccv,iclr,icml,naacl,neurips}`。
- 真读机制：paper repo/venue template/宏/agent guidance 是一条独立 scaffold；
  不是 Python 树里的 `paper/` 空目录。
- 可借点：paper-only/mixed profile 只表达边界，具体投稿模板归 typesetting。
- 差距：只建 LaTeX 项目，不审全仓数据/代码迁移。

### 8. scaffold-repository

- Repo：
  [`patinaproject/skills`](https://github.com/patinaproject/skills)，**1★**；
  skills.sh 当日 97 installs。
- 固定锚：
  [`f59153f/.../SKILL.md:L45-L63`](https://github.com/patinaproject/skills/blob/f59153fd3fc19b2d4893c2214c3fb76227778786/skills/scaffold-repository/SKILL.md#L45-L63)，
  配套
  [`audit-checklist.md`](https://github.com/patinaproject/skills/blob/f59153fd3fc19b2d4893c2214c3fb76227778786/skills/scaffold-repository/audit-checklist.md)
  与 `agent-spawn-template.md`、`pr-body-template.md`。
- 真读机制：existing repo 将 baseline 项分类为 missing/stale/divergent；每项先
  diff preview，再让用户 accept/skip/defer；明说无 overwrite escape hatch；
  分批独立应用。
- 可借点：真实决策应绑定具体 diff/action，不问一句笼统的“要不要整理”。
- 差距：面向 Patina 工程基线，不做科研数据分类和 rollback manifest。

### 9. harness-init

- Repo：[`Gizele1/harness-init`](https://github.com/Gizele1/harness-init)，
  **47★**。
- 固定锚：
  [`71d48b2/skills/harness-init/SKILL.md:L60-L111`](https://github.com/Gizele1/harness-init/blob/71d48b2ec74768d6bcd96afb68376e0d5c9c4fea/skills/harness-init/SKILL.md#L60-L111)，
  配套
  [`gc-patterns.md`](https://github.com/Gizele1/harness-init/blob/71d48b2ec74768d6bcd96afb68376e0d5c9c4fea/skills/harness-init/references/gc-patterns.md)
  与
  [`boundary-test-template.md`](https://github.com/Gizele1/harness-init/blob/71d48b2ec74768d6bcd96afb68376e0d5c9c4fea/skills/harness-init/references/boundary-test-template.md)。
- 真读机制：Phase 0 永不跳过；读取实际 import 判断层；existing repo 用
  `KNOWN_VIOLATIONS` baseline + ratchet，不因历史债务立刻打爆 CI；monorepo
  分包适配；每 phase 有 checkpoint/evidence。
- 可借点：existing migration 应先 baseline，再渐进收敛；“文件存在”不是完成证据。
- 差距：会创建架构/CI/GC 工件，超出本技能只管可见树的边界。

### 10. folder-organization / file-organizer

- Repos：
  [`delphine-l/claude_global`](https://github.com/delphine-l/claude_global)
  **15★**，skills.sh 136 installs；
  [`composiohq/awesome-claude-skills`](https://github.com/composiohq/awesome-claude-skills)
  **66,683★**，skills.sh 4,436 installs。
- 固定锚：
  [`folder-organization/SKILL.md`](https://github.com/delphine-l/claude_global/blob/71c292e8aa6f5f53759ad5fe2a71069fd8163d1c/skills/project-management/folder-organization/SKILL.md#L1-L116)、
  [`reorganization-guide.md:L7-L80`](https://github.com/delphine-l/claude_global/blob/71c292e8aa6f5f53759ad5fe2a71069fd8163d1c/skills/project-management/folder-organization/reorganization-guide.md#L7-L80)、
  [`file-organizer/SKILL.md:L74-L183`](https://github.com/composiohq/awesome-claude-skills/blob/92568c1edaff1bde5371154f036d959346c145a8/file-organizer/SKILL.md#L74-L183)。
- 真读机制：前者分 research/development/bioinformatics/notebook profiles，迁移后
  搜硬编码路径、核文件数；后者先 scope/inventory/hash duplicates，再呈计划和
  “files needing decision”，批准后 move 并记录 undo。
- 可借点：duplicate hash 只是决策证据；move 后还要验证引用路径。
- 真实风险：两者示例含 shell 拼接、通配删除与 POSIX-only 命令，不能照搬到
  Windows 或用户仓。Light 因此把 mutation 收进 Python、绝对 containment、
  no-overwrite 与 manifest rollback。

## B. 工具/模板/规范（另表，不计 skill 数）

| 项目 | 当日 star / 固定 commit | 一手核机制 | 对旧说法的裁决 |
|---|---:|---|---|
| Cookiecutter | 24,980★ / `c88fbe9` | 生成、replay、pre/post hooks、`--overwrite-if-exists`、`--skip-if-file-exists` | 本体仍偏生成；skip/overwrite 不是三方 safe merge |
| Copier | 3,444★ / `454ec42` | `update` 三方演化比较、`check-update`、before/after migrations、inline 或 `.rej` 冲突 | 已覆盖 template lineage/update/migration/conflict；旧表“只生成”错误 |
| Cruft | 1,576★ / `33f6b72` | `.cruft.json` 记录 template/commit/context；`check`/`diff`/`update`/`link`，更新前 review | 已覆盖 Cookiecutter 漂移和更新；Light 不应伪装独有 |
| PyScaffold | 2,259★ / `157223e` | `putup --update`、`pretend`、update/force 写规则；大版本迁移要求 clean tree + diff/manual adjust | 已审/更已有 PyScaffold 项目；并非 generate-only |
| CCDS v2 | 9,928★ / `0f6b163` | 参数化 DS tree、raw immutable、DAG、notebook 命名、README/.gitignore、环境/存储选项 | Light 旧“三铁律/23目录”多为常见意见，不是差异 |
| DVC | 15,716★ / `8131c32` | Git 跟 `.dvc`/`dvc.yaml` 元数据，数据/模型走 cache/remote；pipeline deps/outs | DVC DAG/大产物边界不是 Light 独有 |
| uv | 87,017★ / `51a283b` | app/lib/package/bare profiles、workspace、lock/sync；已有 `pyproject.toml` 时 `uv init` 拒绝 | Python 环境脚手架与 monorepo workspace 已很成熟 |

一手文档：
[Cookiecutter](https://cookiecutter.readthedocs.io/)，
[Copier update](https://copier.readthedocs.io/en/stable/updating/)，
[Cruft](https://cruft.github.io/cruft/)，
[PyScaffold update](https://pyscaffold.org/en/stable/updating.html)，
[CCDS structure](https://cookiecutter-data-science.drivendata.org/)，
[CCDS opinions](https://cookiecutter-data-science.drivendata.org/opinions/)，
[DVC](https://dvc.org/doc)，
[uv init](https://docs.astral.sh/uv/concepts/projects/init/)。

CCDS 的细节尤其推翻旧 heuristics：官方明确 raw 不可变，但也明确“小量且少变的
数据可能适合进仓”；目录名/数量不如数据流重要；项目可按需简化、扩展、重组。

## C. 研究软件/FAIR/经验规范（仍不计 skill）

- Wilson et al., *Good Enough Practices in Scientific Computing*：
  [PLOS DOI](https://doi.org/10.1371/journal.pcbi.1005510)。数据、软件、协作、
  项目组织和 manuscript 的常规基线，不是产品差异。
- Noble, *A Quick Guide to Organizing Computational Biology Projects*：
  [PLOS DOI](https://doi.org/10.1371/journal.pcbi.1000424)。目录隔离、raw/derived、
  README/脚本化是经典经验。
- FAIR Principles：
  [GO FAIR](https://www.go-fair.org/fair-principles/)。FAIR 约束元数据和可发现/
  可访问/互操作/可复用，不等于采用某棵目录树。
- Research Software Engineering：
  [The Turing Way](https://the-turing-way.netlify.app/reproducible-research/reproducible-research.html)。
  结构只是可复现的一小部分；环境、数据、代码、许可、测试、文档和计算证据仍需
  各自验证。

## D. Round 2 落地映射

| 学到的机制 | Light 落点 |
|---|---|
| detect stack/monorepo before rules | `technology-signatures.json` separates observed locators from policy declarations; `git_context` records root/scope |
| new 与 existing 分流；非空拒绝生成 | `scaffold` 只接空目录；existing 必走 `intake` |
| report-only audit before mutation | source snapshot + `intake-integrity.json` |
| diff preview + accept/skip/defer | action IDs + `plan_sha256` authorization |
| template manifest/provenance | `structure-profiles.json` + `.project-structure-provenance.json` |
| mixed research/control-root thinking | Python/R/mixed/paper/custom 五个最小 profile |
| baseline/ratchet, unknown 不硬判 | explicit policy + every absent fact `UNKNOWN` |
| hash duplicate evidence | inventory SHA-256 + duplicate groups；绝不 auto-delete |
| move log/undo | applied manifest + verified rollback + reapply |
| data Git policy is contextual | fixture/golden/DVC pointer/large-sensitive 分开判 |

## E. 诚实差异与落后项

### 可验证窄差异

1. 一个 stdlib 脚本在同一 artifact contract 下处理 Git root、monorepo subroot、
   non-Git、tracked/untracked/ignored、symlink、大文件、敏感路径信号。
2. plan digest 与用户 action IDs 绑定；blocked action 不能借 flag 绕过。
3. 每个 applied move 有 before/after locator/hash；rollback 真验证 hash。
4. `.light/` 被机械分类为 memory-pm-owned 并排除迁移，而不是只靠文案提醒。
5. profile 选择不能反过来充当项目类型证据；observed/policy 信号、推荐 profile、
   用户 override reason 与环境 doctor 形成同一证据链。

### 已知落后

1. 无 Copier/Cruft 的三方 template update/merge；只有一次性 scaffold provenance。
2. 无 AST/语言服务器级引用重写；move 后硬编码路径仍需专项测试。
3. 不执行 `git rm --cached`、DVC init、对象存储上传或配置 rewrite；只把它们列为
   单独决策。
4. sensitivity/owner/producer/recomputability 不能可靠自动推断；未知保持
   `UNKNOWN`，依赖项目 policy。
5. symlink 只盘点并阻断自动 move；Windows 无权限创建 symlink 时 selftest
   诚实 skip。
6. 结构 audit 不证明数据、实验、统计、论文或复现质量。

## F. 门型一手核

`light-orchestrator/scripts/run_checkpoint.py::STAGE_GATES` 与
`reroute.py::ROUTES` 均无 project-structure；orchestrator spec 将其列为
overlay。故本技能 `emits: none`、不接 `_shared`、不产 findings、不造 stage
或 back-edge。本文件与 E2E 都只验证工具自身退出码和迁移证据。
