# typesetting Round 2 活体 E2E

日期：2026-07-03（Asia/Shanghai）
开工基线：`93c566b`（citation Round 2 收口）

## 闭环结论

本轮用 citation Round 2 当前脚本在线核验 NumPy DOI，真实消费其
`light.citation_delivery.v1`、`references.bib` 与 `citekey-audit.json`；再把
paper-writing 形态的 LaTeX 正文和 figure 当前导出器产生的 88×55 mm PDF 图件
冻结进 build snapshot。稿件包含引用、图、表和交叉引用，latexmk 实际执行
3 次 pdfLaTeX + 2 次 BibTeX 后收敛。

最终产物状态为 `DELIVERED`：PDF 2 页、letter page box、6 个字体均嵌入，
PDF SHA-256 为
`4780f2c161798a1093379a16a75fd270382fdc30d7bab79716dc2e4ac4c860aa`。
临时输入和运行件均在 `.upgrade/_e2e`，收口前删除；本页保存永久证据。

## 真实输入与 provenance

```text
citation_registry.py --draft paper-good.tex --refs-spec citation_input.json
  --online --project typesetting-round2 --out-dir citation-delivery
→ work_count=1, CONFIRMED=1, chimeric=0, citekey audit ok=true
```

canonical citation delivery 明示：

```json
{
  "consume": ["references.bib", "citekey-audit.json"],
  "truth_boundary": "typesetting checks citekeys/compilation; citation owns authenticity"
}
```

figure 由当前 `light-figure/scripts/figure_export.py::save_for_journal` 真导出
PDF/PNG；typesetting 用 `pdfinfo MediaBox` 实测 staged PDF 为 88.0×55.0 mm，
与 figure manifest/输入声明一致。typesetting 没有重判 DOI、claim relevance、
DPI 规范或图的科学/视觉诚实。

venue/profile 是本次 E2E 的用户输入，带 `checked_at=2026-07-03`，明示
BibTeX、article、double blind、4 页、letter 和字体嵌入；它不被声称为任何
真实 venue 的通用规则。

## fail → fix 场景

| 场景 | 真运行结果 |
|---|---|
| bibliography backend 错配 | source 检出传统 `\bibliography`=BibTeX，profile 故意声明 Biber；preflight `ERROR/BIB_BACKEND_MISMATCH`，未等编译器连锁报错。把 profile 修为 BibTeX 后 preflight `PASS` |
| 真 LaTeX 根因 | 第 4 行 `\definitelyUndefinedCommand`；latexmk exit 1，compile=`ERROR`，报告定位 `paper-error.tex:4 Undefined control sequence` |
| 工具链不可用 | 仅对该子进程把 `LIGHT_TYPESETTING_PATH` 指向空目录；latexmk 不可达，compile=`UNAVAILABLE`、exit 0、无 PDF，未冒充稿件 critical 或 delivered |
| desk-reject 命中 | 真 PDF 与源稿含作者名/PDF Author；`BLIND_IDENTITY`、`PDF_AUTHOR_META` 两项 critical，TODO 保持 warning；findings exit 1/verdict=fail |
| 修后交付 | 作者改为 Anonymous、清 PDF Author 与 TODO；compile=`PASS`，desk findings verdict=pass，build=`DELIVERED` |

坏 build 虽已成功编译 PDF，仍因 2 个 desk-reject critical 为 `FAILED`；
这证明“能编译”不等于“可投稿”。成功 build 的 `compile-report.json` 保存绝对
latexmk 路径、cwd、完整 argv、5 条 rule/round 记录、PDF/log 哈希和页数。

## stage 11 与下游

命令门使用 locale-neutral 的 `--quiet`，完整诊断写 JSON：

```text
run_checkpoint.py --stage 11
  --gate "compile=...compile_driver.py ...paper-error.tex
          --json-out stage11-bad-compile.json --quiet"
  --findings bad-findings.json --write
→ exit 1, passport stage[11].status=gate_failed

run_checkpoint.py --stage 11
  --gate "compile=...compile_driver.py ...build-good/source/paper.tex
          --json-out stage11-good-compile.json --quiet"
  --findings good-findings.json --write
→ exit 0, passport stage[11].status=delivered
```

`reroute.py --stage 11 --findings bad-findings.json` 返回
`root_cause_stage=-1/action=manual`，证明 `ROUTES` 没有伪造 stage-11 出边；
根因按约束在 typesetting 内修。

`venue-handoff.json` 随后被当前
`light-venue-matching/scripts/venue_fit_rank.py --manuscript` 真读取。输出完整
保留 `status=DELIVERED`、PDF 路径/hash、`pages=2`、letter page size、
profile/source、compliance report 与 `critical_count=0`，同时仍停在 venue
决策点，没有自动投稿。

## 真运行暴露并修复的非预设问题

1. Windows PATH 首项是已经失效的 runtime `pdfinfo.cmd`，但后面有可用的
   MiKTeX/Poppler `pdfinfo.exe`。原实现只用 `shutil.which()`，导致 figure
   尺寸无法实测。现会枚举候选并优先真实 exe；回归实测 88.0×55.0 mm。
2. `pdffonts` 的字体 type 可为 `Type 1` 或 `CID TrueType`。原固定 split
   列号把 encoding 误读成 embedded，曾把 6 个已嵌入字体全部误报 critical。
   现从行尾 `emb/sub/uni/object ID` 结构解析；同一 PDF 复核为 6/6 嵌入。
3. stage command gate 的父进程按 Windows 本地代码页解码，而编译器人读报告是
   UTF-8，坏稿首次聚合触发 reader decode exception。compile driver 新增
   `--quiet`；gate 只读 exit code，完整 UTF-8 诊断写 `--json-out`，随后同一
   fail→pass 流程无异常。
4. 五个 bundled template 真回归时，中文模板注释里同时示例 BibLaTeX 与
   BibTeX，旧探测把注释当活代码并误报 backend conflict。engine/backend、
   preflight 和 desk scan 现先去除未转义 LaTeX 注释；五模板最终全部真编译
   `PASS`（中文模板走 XeLaTeX，其余走 pdfLaTeX）。

这些问题均由真实链路首先暴露，不是预设 selftest 场景。

## Round 3 追加硬化：readiness 同一 PDF 证据绑定

2026-07-05 复审发现，旧 `submission_readiness.py` 已要求“每页 render hash +
review PASS”，但视觉、metadata、compliance 与用户批准证据没有机器强制绑定到
同一个编译产物。理论上可能把 A PDF 的 compile hash、B PDF 的视觉复核、C
profile 的 compliance 报告拼成一个假闭环。

现已将 readiness 门改为：

- `compile` 必须有 `pdf_sha256` 与 `page_count`；
- `visual.source_pdf_sha256` 必须等于 `compile.pdf_sha256`，且
  `visual.page_count` 必须等于 `compile.page_count`；
- 每页视觉行必须有页码、`render_sha256`、`render_tool`、`review_status=PASS`、
  `reviewer`/`reviewer_id` 与不晚于 `--as-of` 的 `reviewed_at`；
- `metadata.source_pdf_sha256`、`compliance.source_pdf_sha256` 与
  `user_approval.pdf_sha256` 均必须等于 `compile.pdf_sha256`；
- compliance 还必须声明与 `venue_profile` 相同的 `venue` 与 `article_type`。

回归命令：

```powershell
$env:PYTHONUTF8=1
python skills\light-typesetting\scripts\submission_readiness.py --selftest
```

结果：exit 0，并覆盖 PDF hash mismatch、逐页 review evidence gap 与
compliance profile mismatch。
