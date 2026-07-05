# project-structure Round 2 活体 E2E

日期：2026-07-03
平台：Windows 11 / Python stdlib / Git
临时根：`<repo>\.upgrade\_e2e`（收口前删除）

## 1. 场景

在临时 Git 仓 `messy-mixed` 建真实 mixed Python/R/LaTeX 杂乱项目：

- tracked 小型 `data/raw/public_fixture.csv`，policy 明确为 public test fixture；
- tracked `tests/golden/expected.txt`，policy 明确为 reviewed golden file；
- tracked 1,240-byte `results/model.bin`，本 E2E 将 large threshold 调到
  1,000 bytes，policy 明确为 recomputable + DVC；
- tracked Python/R/LaTeX 源散落在 `legacy_analysis/` 与 `drafts/`；
- `legacy_analysis/conflict.py` 的建议目标 `python/src/conflict.py` 已存在；
- 两份同 hash 笔记位于 `docs/` 与 `Old Results/`；
- untracked `user-draft.md`；
- ignored `.env` 与 `scratch/cache.tmp`；
- tracked `README.md` 有用户未提交修改；
- `.light/` 由真实
  `python skills/light-memory-pm/scripts/pm.py init --dir ... --project messy-mixed-e2e`
  创建并跟踪。

Windows 当前账户创建 symlink 返回
`Administrator privilege required for this operation`。因此活体分支诚实记录
`UNAVAILABLE`，不伪造 symlink；`scaffold.py --selftest` 同样输出
`symlink=skipped`。脚本仍用 `is_symlink` 盘点并阻断 symlink move。

## 2. 只读 intake

命令：

```text
python skills/light-project-structure/scripts/scaffold.py intake \
  .upgrade/_e2e/messy-mixed \
  --out .upgrade/_e2e/evidence \
  --profile mixed-research \
  --policy .upgrade/_e2e/policy/mixed-policy.json \
  --large-bytes 1000
```

exit 0，产八件：

1. `project-profile.json`
2. `source-inventory.json`
3. `structure-audit.json`
4. `migration-plan.json`
5. `conflict-unknown-report.json`
6. `rollback-plan.json`
7. `intake-integrity.json`
8. `delivery.md`

`intake-integrity.source_unchanged=true`。before/after 全文件 SHA-256 集合及
Git status 均相等：

```text
 M README.md
?? user-draft.md
```

ignored 文件另由 `git status --ignored` 证实仍在：

```text
!! .env
!! scratch/
```

关键 inventory：

| locator | Git state | classification | policy |
|---|---|---|---|
| `data/raw/public_fixture.csv` | tracked | test-fixture | track |
| `tests/golden/expected.txt` | tracked | golden-file | track |
| `results/model.bin` | tracked | large-model / recomputable | dvc |
| `user-draft.md` | untracked | UNKNOWN | UNKNOWN |
| `.env` | ignored | UNKNOWN / sensitive-path | UNKNOWN |
| `.light/project_card.md` | tracked | memory-ledger | preserve |

fixture 与 golden 均未误报。模型产生
`tracked-policy-conflict: tracked but policy requires dvc`；按用户授权只记录
DVC policy，不运行 `git rm --cached`、不初始化 DVC。

## 3. 计划、冲突与真实决策

最终 dry-run：

```text
plan_sha256=5f68c51b4fc6002b316991e6511ea12ddfd8624b64f8329af33a4f5199f7546e
actions=4
blocked=1
conflicts=3
```

动作：

| ID | source → target | 状态 |
|---|---|---|
| `move-0001` | `drafts/paper.tex` → `paper/paper.tex` | safe |
| `move-0002` | `legacy_analysis/conflict.py` → `python/src/conflict.py` | blocked: target exists |
| `move-0003` | `legacy_analysis/main.py` → `python/src/main.py` | safe |
| `move-0004` | `legacy_analysis/report.R` → `R/report.R` | safe |

另报 duplicate-content：

```text
0d3169bab25b7831f24c7ca2cd9f7b277b155382db13432b0e4c4a32c21b7fb8
Old Results/notes-copy.md
docs/notes.md
```

duplicate 只作证据，未自动删除。

助手在此真实停下。用户回复：`按推荐授权`。授权文档绑定上方 plan digest，
只含 `move-0001`、`move-0003`、`move-0004`；`move-0002` 保持 blocked，
模型只记 DVC policy。

## 4. Apply

命令：

```text
python skills/light-project-structure/scripts/scaffold.py apply \
  --plan migration-plan.json \
  --authorization authorization.json \
  --manifest-out applied-manifest-first.json
```

exit 0，applied=3。逐项证据：

| ID | before SHA-256 | after SHA-256 |
|---|---|---|
| `move-0001` | `dd7306cd5233a2cbb1261577ae2584631498aa1fbddc0a3d110f0457fc7fcf63` | 相同 |
| `move-0003` | `dbcdb7ab14e79ac397f42a3d5eb22a8662f376bb6e5da5c7b44dc13eddd885b4` | 相同 |
| `move-0004` | `2d6ce3c1b5ab4bddcaae06b711e5263bf77498940fe7222726cfb01c0bcbeebc` | 相同 |

未动对象：

| 对象 | SHA-256 / 证据 |
|---|---|
| untracked `user-draft.md` | `3b2294c2297d0ebb3c2a56ce50a52c3155d413fff18bfacfd287b64088dc896d` |
| `.light/project_card.md` | `687a2856994d98f1de55a7973a503e3356334f57ebefa7c199297f1552a2f858` |
| dirty `README.md` | `d89a90d145d1e249dd1df5dc8cc624523fe1a42422724dd72bf3679ec2c1a391` |
| blocked target `python/src/conflict.py` | `15d89786b936c3dc6a7a0d0026f642ca65877de318bda7dc5cd310b4a07fe50e` |
| tracked `results/model.bin` | `58a158082a44e0abb9c88c89657d2fd4eae891299018bbed75df7079c012edcb` |

`legacy_analysis/conflict.py` 仍存在，目标未覆盖。

## 5. Rollback 与 reapply

命令：

```text
python skills/light-project-structure/scripts/scaffold.py rollback \
  --manifest applied-manifest-first.json \
  --rollback-out rollback-manifest.json
```

exit 0，restored=3。将 rollback 后整仓与 intake before 比较：

```json
{
  "missing": [],
  "extra": [],
  "changed": [],
  "git_status": [" M README.md", "?? user-draft.md"],
  "expected_status": [" M README.md", "?? user-draft.md"],
  "snapshot_restored": true
}
```

随后用同一未变化 plan + authorization reapply，exit 0，applied=3，
`all_move_hashes_match=true`。最终迁移状态仍保留冲突源/目标、草稿、
`.light/`、dirty README 与 tracked model。

## 6. Empty Git / non-Git / monorepo 子根

三个额外 intake 均 exit 0 且 `source_unchanged=true`：

| case | repo_mode | Git evidence |
|---|---|---|
| empty Git root | `git-root` | branch `master`，零文件也诚实产 inventory |
| non-Git | `non-git` | `available=false`, reason=`not a git work tree` |
| `monorepo/packages/study` | `monorepo-subroot` | git scope=`packages/study` |

临时件必须放在外层 Light Git worktree 内；为走真实 non-Git 降级，运行该 case
时把 `GIT_CEILING_DIRECTORIES` 设为 `...\.upgrade\_e2e\edge-cases`，阻止 Git
向上误认外层仓。未设置时将其识别为外层 monorepo subroot，亦是正确行为。

## 7. 活体发现并修复的问题

第一次把 large threshold 调到 1,000 bytes 后，约 1.9KB 的
`.light/project_card.md` 被误列为 `large-policy-review`。这违反 memory-pm
所有权边界。修复为：

```text
classification == memory-ledger → preserve；不进入 large-artifact review
```

重跑后 conflicts 从 4 降到真实 3 项：tracked DVC policy、duplicate-content、
target-exists。selftest 与活体 intake 均 exit 0。

## 8. 诚实边界

- 结构符合 profile 不证明数据、实验、统计、论文或复现质量。
- 本技能不执行 `git rm --cached`、DVC 初始化、对象存储上传、配置重写或删除。
- 没有 Copier/Cruft 的模板三方更新；greenfield 只记录一次性 provenance。
- symlink 在本机因权限未实建，已标 unavailable；没有把工具暂不可用写成资源不存在。
- project-structure 仍是 off-DAG overlay：未改 `_shared`、`STAGE_GATES`、
  `ROUTES`，未产 findings 或 back-edge。
