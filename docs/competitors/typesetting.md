# 对标笔记 · typesetting Round 2

> 核查日：2026-07-03（Asia/Shanghai）。Star 来自当日 GitHub API；
> commit 固定到当日 HEAD；文件/行均按固定 commit 读取。真同类 skill 与编译器、
> lint、bibliography、venue 规范、论文/评测集严格分表，后五类不占 skill 名额。

## 0. 旧结论复核

旧表“同类稀疏、真编译命令门/多轮收敛/错误翻译/desk-reject 独特”的结论不成立：

- `lingzhi227/agent-research-skills` 已把 page/anonymization/required sections/TODO
  做成 `latex_checker.py`；`flonat/claude-research` 的 pre-submission skill 把
  TODO、citekey、broken refs、双盲、页数与编译列为 hard gate。
- `ndpvt-web/latex-document-skill`、flonat `/latex`、`b1rd33/pdflatex-skill`、
  terrylica `latex-build` 都做多轮/latexmk；前两者还做错误解释/修复循环。
- renocrypt `compile_paper.py` 已跑 latexmk 或
  pdflatex→bibtex→pdflatex×2，并从 log/aux 分正文与参考文献页。
- flonat `/latex` 与 pre-submission、ndpvt citation extractor 都做
  `\cite`↔BibTeX；并非 Light 独有。
- wanshuiyin `paper-compile` 明确检查页数、匿名、font embedding、undefined
  cite/ref、PDF 视觉；ChineseResearchLaTeX 还做 PDF 字体/页边距与像素 diff。

因此不能再把真编译、多轮收敛、citekey、双盲、页数或错误翻译写成独占。Light
可证的组合差异是：上游 provenance 快照 + citation delivery 消费边界 + 四态
compile contract + source-located canonical report/failure + profile-driven
desk-reject findings + stage-11 checkpoint + venue handoff，并且
`UNAVAILABLE` 不冒充论文 `ERROR/PASS`。

## 1. 真同类 skill（11 个；8 个独立 repo）

| skill | 当日 star / repo / 固定 commit | 真读文件与行 | 真读配套资源 | 具体机制 | 可借点 | Light Round 2 前的真实差距 |
|---|---|---|---|---|---|---|
| `latex-document-skill` | 551★ · `ndpvt-web/latex-document-skill` · `d14e133` | `SKILL.md:157-219` | `scripts/compile_latex.sh:217-334,438-620`; `validate_latex.py:155-354`; `assets/templates/academic-paper.tex:1-100` | 引擎探测、manual multi-pass/latexmk、BibTeX/Biber、日志翻译、PNG preview、pre-assembly validation | 预检先于编译；输出可视预览 | Light 无 canonical source snapshot/manifest；旧错误只有泛化文本 |
| `latex` | 104★ · `flonat/claude-research` · `4de335b` | `skills/latex/SKILL.md:37-105,128-178` | `references/known-errors.md:5-109`; `references/templates.md` | 最多 5 次 compile-fix、同错 3 次熔断、clean build 后 cite audit、页数/warning/box 报告 | 把 `UNRESOLVED` 做成终态；错误修复留痕 | Light 旧版没有重复签名熔断和真实轮次报告 |
| `latex-health-check` | 104★ · 同 repo/commit | `skills/latex-health-check/SKILL.md:23-110,113-162` | `references/evolution-log.md`; `references/troubleshooting.md` | 多项目发现、3 轮修复、ERROR/FIXED/OK、共享 BibTeX/template drift、outputs manifest verifier | manifest 先验证文件真实存在 | Light 旧版只交 PDF/日志，无 canonical output manifest |
| `pre-submission-report` | 104★ · 同 repo/commit | `skills/pre-submission-report/SKILL.md:47-110,137-140,150-228` | 指向的 `_shared/double-blind-anonymity-checklist.md` 在固定 tree 中不存在；这是实核缺口 | TODO/citekey/sections/`??`/anonymity hard gate；compile、page-limit、review 汇总 | integrity gate 应先跑；失败仍产报告 | Light 旧版双盲只扫少量正则，未明确“指针不存在/检查未跑”的不可用态 |
| `latex-template` | 104★ · 同 repo/commit | `skills/latex-template/SKILL.md:39-105,152-182` | `references/comparison-checklist.md:7-73,77-138` | 语义比较 package/options/load order/backend/.latexmkrc；Adopt/Keep/Conflict/Drop；Conflict 必问人 | backend/template 冲突在编译前定位 | Light 旧版未把 profile 与 source backend/class mismatch 做成 preflight root cause |
| `arxiv-paper-writer` | 371★ · `renocrypt/latex-arxiv-SKILL` · `6ca1b48` | `SKILL.md:24-75,90-111,133-159` | `scripts/compile_paper.py:20-111,115-173`; `assets/template/main.template.tex`; `references/bibtex-guide.md` | 固定 IEEE scaffold、早编译、verified BibTeX、latexmk fallback、多轮链、按 bibliography-start label 报页 | 正文/参考文献页作用域须来自明确 label/profile | Light 旧版只数总页，未记录 page scope |
| `latex-formatting` | 177★ · `lingzhi227/agent-research-skills` · `9e6c085` | `skills/latex-formatting/SKILL.md:20-58` | `scripts/latex_checker.py:21-29,82-152,170-226`; `references/venue-templates.md:1-75` | required sections、TODO、匿名作者/自引/URL/致谢、page override | desk-reject 检查是同类常见能力 | 它把 venue limits 硬编码；Light 应反向坚持 external profile |
| `paper-compile` | 12,941★ · `wanshuiyin/Auto-claude-code-research-in-sleep` · `82076e5` | `skills/paper-compile/SKILL.md:14-18,22-123,125-256` | `skills/paper-write/templates/neurips2025.tex:1-55` 与同目录多 venue 模板 | latexmk、3 次修复、file/line、pdfinfo、视觉 scan、page scope、匿名、pdffonts、stale file | font embedding 与 rendered-PDF review 纳入交付 | 它内嵌多届页限；Light 不能复制这种腐烂模式 |
| `pdflatex` | 1★ · `b1rd33/pdflatex-skill` · `eda0e17` | `SKILL.md:20-68,115-205` | `scripts/compile_latex.sh:82-145`; `references/journal-submission.md:1-159`; `examples/.latexmkrc` | 显式 BibTeX/Biber 4-pass、engine guide、shell-escape warning、journal checklist | backend 必须显式且不可混 | Light 旧版依赖 latexmk 猜 backend，没先报 mismatch |
| `make-latex-model` | 2,463★ · `huangwb8/ChineseResearchLaTeX` · `33451b6` | `skills/make-latex-model/SKILL.md:63-128,130-151` | `scripts/analyze_pdf.py:50-156,212-268`; `compare_pdf_pixels.py:34-127,161-200` | PDF font/layout 参数抽取、baseline pixel diff、改共享包先跑受影响模板回归 | “能编译”不等于视觉/模板一致；公共模板改动需回归面 | Light 旧版只有 source/log 静态扫，无 PDF page-box/font 事实 |
| `latex-build` | 56★ · `terrylica/cc-skills` · `1097db1` | `plugins/doc-tools/skills/latex-build/SKILL.md:24-32,36-95,118-138` | `references/configuration.md`; `multi-file-projects.md`; `troubleshooting.md` | latexmk dependency graph、正确轮数、watch/SyncTeX、clean/force rebuild | 多文件依赖交给 latexmk，命令仍需留存 | 证明“多轮收敛”是基础能力，绝不能写成 Light 独有 |

## 2. 编译器、发行版与构建工具（不占 skill 名额）

| 类 | 当日核查 | 机制与边界 |
|---|---|---|
| latexmk | 本机 4.88（2026-03-09）；`https://ctan.org/pkg/latexmk` | 依赖驱动多轮、BibTeX/Biber rule、`.fdb_latexmk`；Light 记录 rule/run 与 exact command |
| Tectonic | 本机 0.16.9；`tectonic-typesetting/tectonic` 4,942★ | bundle/按需资源、自动多轮；Biber 路径不能假定等价 latexmk |
| MiKTeX | 本机 25.12，pdfTeX 4.23、XeTeX 4.16 | Windows 核心实测环境；缺包/首次初始化可能阻塞，PATH 命中不等于可用 |
| TeX Live | `https://tug.org/texlive/` | 跨平台发行版与 `tlmgr/kpsewhich`；Light 只探测，不自动改系统安装 |
| pdfLaTeX/XeLaTeX/LuaLaTeX | 本机三者均在 PATH | 字体/Unicode/Lua 触发选择；profile 可锁定，冲突报根因 |

## 3. lint / compile diagnostics（不占 skill 名额）

| 工具 | 当日状态 | 可借机制 | 不纳入原因/边界 |
|---|---|---|---|
| ChkTeX | 本机 1.7.9；`https://www.nongnu.org/chktex/` | typographic lint 与 `.chktexrc` | 可选增强；不能替代真编译 |
| lacheck | 本机可执行；`https://ctan.org/pkg/lacheck` | 轻量结构 lint | 诊断面窄，仅 advisory |
| TeXtidote | `sylvainhalle/textidote` 1,050★ · `433ee34` | source mapping、LanguageTool/ChkTeX 汇总 | Java 重依赖，不进核心 |
| CheckMyTex | `d-krupke/CheckMyTex` 15★ · `f8e8848` | whitelist/baseline 棘轮 | 外部解析依赖；可选 |
| ACM SIGSOFT submission-checker | 69★ · `3ffa1eb` | rendered PDF submission checks | Java/Maven 且面向特定生态；不冒充通用终判 |

## 4. bibliography backend（不占 skill 名额）

| 系统 | 选择信号 | Light 处理 |
|---|---|---|
| BibTeX | `\bibliography` + venue `.bst` | 要求 `bibtex` executable；记录 latexmk bibtex rule |
| Biber | `biblatex` 默认或 `backend=biber` | 要求 `biber` executable；不与 `\bibliography` 混用 |
| biblatex+BibTeX | `backend=bibtex` 明示 | 允许但记录声明；不能看到 biblatex 就一律判 Biber |
| citation delivery | `light.citation_delivery.v1` | 消费 BibTeX/citekey audit；真实性留在 stage 10 |

本机 `biber --version` 首次核查耗时明显长于其他工具，最终返回 2.21。故
“PATH 存在”不足以证明工具链可用；启动/超时必须进入 `UNAVAILABLE` 证据。

## 5. venue template / 规范（不占 skill 名额）

运行时优先级：用户给定当届 author kit/profile > 当天权威 venue 页面 >
官方 CTAN/template source > bundled 起手骨架。任何 page/anonymity/font/template
规则都要写进 `light.typesetting_venue_profile.v1.source`（kind/URL/date/notes）。
本表不保存跨届页限真值。`templates/acm_sigconf.tex`、`ieee_bare_conf.tex`、
`springer_llncs.tex`、`elsevier_elsarticle.tex`、`ctex_chinese.tex` 只是本地起点。

## 6. 论文、系统与评测集（不占 skill 名额）

| 项目 | 当日固定点 | 学到什么 | Light 差距 |
|---|---|---|---|
| PaperFit / PaperFit-Bench | `OpenRaiser/PaperFit` 325★ · `b9e907d`; arXiv `2605.10341` | 200 papers、10 venue templates、13 defect types；render→diagnose→constrained repair | Light 只做 deterministic PDF facts + 人工视觉复核，不声称有 PaperFit 级视觉优化 |
| TeXpert | `knowledge-verse-ai/TeXpert` 11★ · `32accdb`; arXiv `2506.16990` | 多层 LaTeX generation benchmark 与错误类型 | Light selftest/E2E 不是通用 LaTeX 生成评测 |
| LaTeXpOsEd | arXiv `2510.03761` | 源文件/注释中的身份与秘密泄漏 | Light 静态双盲只覆盖显式模式，语义/隐蔽文件泄漏仍需人工/专用工具 |

## 7. R1 → Light 落地

| 学到的机制 | Round 2 落点 |
|---|---|
| 预检文件/图/label/cite/backend/template | `build_submission.py::preflight` |
| exact command、cwd、真实 rule/run、source line | `compile_driver.py` + `compile-report.json` |
| clean compile 后才算 cite/ref 收敛 | `PASS/UNRESOLVED` 四态契约 |
| 同类常见 anonymity/page/TODO/font checks | `submission_check.py` + profile-driven `desk_reject_gate.py` |
| output manifest 与失败件 | `build-manifest.json` / `failure.json` / `delivery.json` |
| PDF page size/font facts | `pdfinfo`/`pdffonts` 可选本地免费路径 |
| 规则不能硬编码跨届真值 | `light.typesetting_venue_profile.v1` |
| 下游只收真实 PDF/page/compliance | `venue-handoff.json` |

## 8. 诚实结论

Light 不独占 LaTeX 编译、latexmk 多轮、citekey、双盲、页数、错误翻译、font
embedding 或视觉回看。Round 2 的可验证组合增量是将这些能力放进 Light 的作者
artifact contracts 与 stage 11：输入 provenance、citation/figure 边界、四态
compile、canonical reports/failures、profile-driven findings、checkpoint 与
venue-matching handoff。最终版式质量和语义匿名仍必须人工复核。

## 9. Round 3 复审增量

同类热门 skill 常会写“视觉复核/最终检查”，但很少把视觉、metadata、合规报告
和用户授权逐项绑定到同一个编译 PDF。Light 旧 readiness 也有这个缝：每页
`render_sha256` 存在，并不自动证明它来自当前 `compile.pdf_sha256`。Round 3
补上了同一 PDF hash、compile/visual page_count 一致、逐页 reviewer/date/tool、
compliance venue/article_type 绑定和 user approval PDF hash 绑定。这个改动不
宣称自动判断最终版式美学，只防止“证据拼盘式 PASS”。
