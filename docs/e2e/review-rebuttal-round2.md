# review-rebuttal Round 2 活体 E2E

日期：2026-07-03（Asia/Shanghai）
基线：`77133aa0a797fcf830b901230daf152023f40799`
范围：只改 `review-rebuttal`、本证据文档与总进度/记忆；未改其他技能实现。

## 1. R1 真同类重学

逐文件重学 12 个真同类 skill / 8 个 repo；GitHub star、固定 commit、
文件行、配套模板/脚本、机制与差距见
`docs/competitors/review-rebuttal.md`。核查结论：

- reviewer clustering/priority、意见原子化、point-by-point、tone、预算、
  change locator、promise tracking、venue adaptation、meta-review/re-review
  都已有同类实现，不再宣称 Light 独有；
- ARIS 已有 issue board、pivotal reviewer、三种 gate、revision plan 和
  follow-up；Nature response 已有原话保真、输入缺口与 readiness；
- Light 的可证差异只保留为：跨 stage 真契约、source/interpretation 分层、
  `PLANNED/DONE` 与 run provenance 机械门、证据驱动且须用户授权的 stage-13
  回边。

R1 机制已实际落入 `SKILL.md`、resource map、workflow contract、JSON 模板、
response/rereview 模板和五个脚本。

## 2. 上游 handoff 与真实 PDF

用 venue-matching Round 2 契约重新执行 `prepare` 和已授权的 `choose`：

| 字段 | 实测值 |
|---|---|
| selected venue | Journal of Open Research Software (`jors`) |
| selection status | `SELECTED_WITH_USER_AUTHORIZATION` |
| decision authority | `user` |
| typesetting status | `DELIVERED` |
| PDF SHA-256 | `23d5709c84571fadf8a363aa1bffdb4622445e5bcfbc78e7f6d82d851891b3f2` |
| pages / page size | `2` / `612 x 792 pts (letter)` |
| profile | `JORS-source-profile-before-expansion` |
| compliance | `PASS`, critical `0` |
| manuscript requirement | official selected contract retains approximate 4–6 pages; current 2 pages need expansion |
| response length/new material | both `UNKNOWN`; manuscript page rule was not borrowed |

第一次真实 typesetting build 以 exit 1 暴露
`BIB_BACKEND_MISMATCH`：profile 写了 BibTeX，但 fixture 无 bibliography
command。把本 fixture 的真实 backend 改为 `none` 后重跑 exit 0；没有绕过
preflight。

## 3. 真实公开 review/decision 与不可用状态

实时 OpenReview API v2 请求返回 HTTP 403，捕获为 `UNAVAILABLE`，records
为空但不解释成“无审稿”。公共 v1 对新式 forum 返回 200/空结果，因此没有
被拿来冒充可用 review。

可用组改用固定公开快照：

- `allenai/PeerRead` commit
  `9bb37751781a900cee9e74ec3105997732c8e8e5`；
- 文件 `data/iclr_2017/test/reviews/554.json`；
- 论文 *Investigating Recurrence and Eligibility Traces in Deep Q-Networks*；
- `accepted=false`，含 reviewer、meta-review 与 committee final decision；
- 源文件 16 个对象中有 8 个完整重复对象。第一次运行因此暴露虚增计数问题；
  修复后原对象仍保真，派生计数显式记录
  `source_record_count=16`、`duplicate_records_removed=8`，最终
  Decision 1 / Meta_Review 1 / Review 6。

`fetch_openreview.py --peerread-url <fixed-commit-url>` 现在可重现上述路径，
并明确标注这是历史快照而非 live API。

## 4. 原子意见、修改与证据

canonical package 产出：

- `review-registry.json`
- `issue-matrix.json`
- `revision-plan.json`
- `evidence-change-map.json`
- `response-draft.md`
- `commitment-ledger.json`
- `unknowns.json`
- `failure.json`
- `delivery.json`

6 个 atom 覆盖 novelty、experiment/evidence、writing/clarity、
misunderstanding、clarification 与新增 citation：

| issue | 处理 |
|---|---|
| `PC-NOVELTY` | committee decision 明确 novelty concern；critical；claim 已降级为 bounded contract，真实 locator 为 `revised-paper.md#preliminary-result` |
| `PC-EXPERIMENT` | decision 明确 evaluation not compelling；critical；扩大项目/重复 seed 实验严格保持 `PLANNED`，无结果、locator 或 run provenance |
| `R4-WRITING` | 正面 clarity 意见；非 rejection-driving，只作 `NOT_APPLICABLE` |
| `R4-GENERALITY` | 合理 scope 意见；真实补写 limitations，状态 `DONE` 且有 locator |
| `E2E-MISUNDERSTANDING` | 明确标为 synthetic E2E fixture；用既有 manuscript locator 澄清“不声称 venue acceptance”，不虚构改稿 |
| `E2E-CITATION-CLARITY` | 明确标为 fixture；新增 reviewer-anchoring 边界与真实 citation locator |

新增引用 `10.1371/journal.pone.0301111` 由 citation 真核：
DOI RA 200、Crossref 200、PubMed 200，最终 `CONFIRMED`；Semantic Scholar
429 与 OpenAlex 无 key 仍保留不可用。此前两个候选分别因作者字段冲突和缺少
第二独立字段源保持 `UNRESOLVED`，没有手改绿。

`rebuttal_budget.py` 对响应草稿实数为 283 words / 2184 characters，但
JORS rule status 为 `UNKNOWN`，所以 verdict 仍为 `UNKNOWN`。

## 5. commitment 与 stage 13

故意把 `PC-EXPERIMENT` 的 `PLANNED` response 写成
“We have conducted ...”：

- 坏账本：`PLANNED_AS_DONE`，verdict `FAIL`，exit 1；
- 修复后的 canonical ledger：6 issues / 6 commitments / 0 finding，
  verdict `PASS`，exit 0。

`reviewer_classify.py` 只把有 committee decision locator 的 novelty 和
experiment 标为 critical；另外 4 条均为 warn。`run_checkpoint --stage 13
--write` 真实 exit 1，将 stage 13 写成 `gate_failed`。

`reroute.py` 只建议：

- 13→3：novelty；
- 13→5：experiment。

建议前后 passport SHA-256 相同
`ABD6CB6F16CBD80D4452DDDC491CD53291622F0D9E508BD445AD0797794633B1`，
证明 reroute 没有自动写台账。用户随后明确回复“同意”，授权推荐的 13→5。
执行 `passport add-back-edge --to 5 --from 13 ... --by user` exit 0：
stage 5=`needs_rework`、round=1，stage 13 仍为 `gate_failed`，passport
validate exit 0。

## 6. 回归

逐个亲眼确认：

- review-rebuttal 5/5 selftest exit 0；
- venue-matching 5/5、paper-writing 7/7、result-analysis 8/8、
  citation 6/6、typesetting 5/5、orchestrator 3/3 selftest exit 0；
- result-analysis 的 Python wrapper 找到 R 4.6.0，R cross-check 也 exit 0；
- `python -m _shared`、compileall、skill quick validation、JSON parse、
  `git diff --check` 均在最终清理后重跑并记录为通过。

## 7. 真实暴露并修复的问题

本轮至少真实暴露并修复四项非预设问题：

1. fixture bibliography backend 与源码不符，被 typesetting preflight 拦住；
2. OpenReview v2 当前 403，必须保留 `UNAVAILABLE` 并使用可复现公共快照；
3. PeerRead 单文件重复整组 records，派生计数需要保真去重与显式计数；
4. 新增 citation 的首批候选未满足双源确认，必须更换到真正
   `CONFIRMED` 的支持文献。

所有 `.upgrade/_e2e` 与 R1 clone 临时件在提交前删除；本文件是永久证据。
