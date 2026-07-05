# citation Round 2 活体 E2E

日期：2026-07-03（Asia/Shanghai）
基线：`89e546797744e5a48b689fae09cd51b9c93833d6`

## 闭环结论

本轮用真实在线元数据跑通了“作者输入 → inventory → 多源核验 → canonical
registry/BibTeX/CSL/evidence/failures → citation gate → stage-10 checkpoint →
typesetting 消费”。临时输入与运行产物均放在 `.upgrade/_e2e`，收口时删除；本文只保留
可复核的命令、状态与根因。

| 场景 | 真实结果 |
|---|---|
| 普通 DOI `10.1038/s41586-020-2649-2` | DOI RA 200、Crossref 200、PubMed 200；DataCite 404、Semantic Scholar 429、OpenAlex 无 key。整体 `CONFIRMED`，逐源值和不可用状态均保留 |
| 撤稿关系 `10.1021/am300292v` | 原文 Crossref `updated-by` 指向通知 `10.1021/acsami.9b11759`；通知以 `update-to` 反向指回原文。citation 只记录事实警报，诚信终判交 research-ethics |
| 编造 DOI `10.5555/light-round2-definitely-not-real-20260703` | DOI RA 明确 `DOI does not exist`，Crossref 404，DataCite 404，故为 `CONFIRMED-MISSING`；Semantic Scholar 429 不被伪装为 404 |
| 嵌合引用 | 真实 NumPy DOI 搭配错标题、错作者、1991 年，`title/authors/year` 三字段冲突，`is_chimeric=true` |
| 语义支持边 | “NumPy 保证每个浮点数组计算都精确”与 NumPy 论文标为 `RELATED_ONLY`；元数据命中不升级为 `SUPPORTS`，gate 保留人工复核 warning |
| 网络不可用 | 将本次子进程的 `HTTPS_PROXY` 指到 `127.0.0.1:9`，六个源均为 `UNAVAILABLE`，work 状态为 `UNAVAILABLE`，不是 `CONFIRMED-MISSING` |

## 真运行暴露并修复的问题

1. PubMed ESummary 作者名采用 `Family Name INITIALS`。旧解析取第一个词为姓，
   会把 `van der Walt SJ` 误拆成姓 `van`，令正常 NumPy DOI 产生作者字段冲突。
   修复后保留复姓粒子，并以 Unicode 折叠比较 `Del Río` 等重音姓氏；同一在线记录的
   `field_conflicts` 从作者误报变为空。
2. 新模板是 `light.citation_input.v1` 对象（含 `references[]`），但
   `verify_refs.py --spec` 原先只接受裸数组，实际把 `schema/project/references`
   三个键当成三条 DOI。现已同时接受两种输入，并加离线回归。

这些问题都不是 selftest 预设报错，而是在本轮真实闭环中首先暴露。

## 闸门与交付证据

坏 registry 含一条 `CONFIRMED-MISSING` 和两条嵌合引用：

```text
citation_verify_gate.py ...bad-delivery...  -> exit 1, verdict=fail
run_checkpoint.py --stage 10 ...bad-findings.json --write
                                           -> exit 1, status=gate_failed
```

按根因移除假 DOI并修正 NumPy 元数据后，相关但不支持的 claim edge 仍保留：

```text
citation_registry.py ...clean...            -> work_count=1, CONFIRMED=1
                                                citekey audit ok=true
citation_verify_gate.py ...clean-delivery... -> exit 0, verdict=warn
run_checkpoint.py --stage 10 ...clean-findings.json --write
                                            -> exit 0, status=delivered
```

stage 10 只由 citation 自身 critical 阻断；没有修改 `ROUTES`、没有伪造 stage-10
回边，也没有把网络不可达或语义 warning 扩成 critical。

## Round 3 续补：registry 派生四关

执行日：2026-07-05。

Round 2 虽然已有 `citation_four_gate.py`，但真实运行仍容易回到手写
`templates/citation-four-gate.example.json`。这会让 canonical registry 与四关输入
漂移，尤其是 `publication_updates`、claim edge access、source evidence hash 和
retraction relation 方向。Round 3 为 `citation_four_gate.py` 新增 `--registry`
入口：直接从 `light.citation_registry.v1` 派生 existence、identity、
publication_status 与 claim_support 记录，再执行四关。

新增 selftest 覆盖：

- registry 中 Crossref `updated-by` retraction → 四关 `RETRACTED_DEPENDENCY`；
- 关系方向保留为 `source_work_id=原文 DOI`、`target_work_id=notice DOI`；
- 移除 publication update 且摘要显式支持时，registry 派生四关可 pass；
- 旧的 unavailable、identity conflict、future date、placeholder locator 等测试仍通过。

真实命令：

```powershell
$env:PYTHONUTF8='1'
python skills\light-citation\scripts\citation_four_gate.py --selftest
```

真实结果：exit `0`。

下游使用同一交付的 `references.bib` 与正文真实运行：

```text
desk_reject_gate.py --tex draft.tex --bib clean-delivery/references.bib ...
                                            -> exit 0
                                            -> bib_integrity=pass
```

交付清单为 `citation-registry.json`、`references.bib`、`references.csl.json`、
`citation-evidence.json`、`citation-failures.json`、`claim-citation-review.json`、
`citekey-audit.json` 与 `delivery.json`。typesetting 只消费 BibTeX/citekey 契约；
引用真实性仍由 citation 负责。
