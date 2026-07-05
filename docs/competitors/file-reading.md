# competitors — light-file-reading（多格式文件理解 · 常驻横切）

> **Round 2 R1 重做（2026-07-01）**：旧表把 11 个解析库/规范/产品几乎都算成“同类”，没有拆出
> 真正可被 agent 调用的 file/PDF/paper-reading **skill**，属于本轮“高 star 同类漏检 + skill/机制混表”
> 系统病。现拆为：§0.A **12 个真同类 skill（来自 8 个独立 repo）**、§0.B 解析器/规范/服务机制锚、
> §0.C 横向机制提炼。star 均由
> `gh api repos/<owner>/<repo> --jq .stargazers_count` **当天一手核**；文件路径、行号与 commit
> 可复验。大技能包的 star 是整仓 star，已明确写出，不冒充单 skill star。
>
> **门型一手核结论（不改架构）**：本技能是 off-DAG 常驻读取工具，`metadata.emits=none`；
> `run_checkpoint.py::STAGE_GATES` 与 `reroute.py::ROUTES` 均无 file-reading。现有
> `pdf_ops verify-tables` 只打印低置信度 advisory，**不产 `light.findings.v1`、不 hard-fail**。
> 这是正确边界：文件是否读全/表是否可疑归本技能提示；引用真伪归 citation critical 门；跨材料术语/
> 指标/claim 漂移归 consistency 横切门。
>
> **关键诚实校正**：旧稿把市场概括成“同类都是抽取器，只有 Light 是理解器”过满。ResearchClaw、
> DeerFlow 等真同类已经做 CRGP、claim↔evidence、结构化论文笔记；Waza 也按用户意图产摘要。
> Light 不是唯一想到“理解”的技能。Light 的真增量应重述为：
> **多格式输入分级 + 页级覆盖/定位 + 五面理解笔记 + 表抽取低置信度显式 advisory + 明确下游边界**
> 的组合，并守零 MCP、零付费 key、可本地审计。

---

## 0.A 真·同类文件/PDF/论文阅读 SKILL（12 个，8 独立 repo）

> 判据：仓库内存在可发现、可调用的 `SKILL.md`，职责直接包含文件/PDF/论文的读取、解析、深读或
> 结构化理解。通用解析库、OCR 引擎、SaaS 和论文进入 §0.B，不占本节名额。
>
> star 快照：`[snapshot 2026-07-01, src=GitHub API]`。

| # | 真同类 skill（repo star） | 它怎么做（已读 SKILL/脚本，可复验点） | 借进 Light | Light 诚实差在哪 |
|---|---|---|---|---|
| 1 | **anthropics/skills · pdf**（**157,014★**，整仓） | `skills/pdf/SKILL.md@35414756ca55`：L81 `pdfplumber` 保版面抽文、L91 抽表、L233 扫描 PDF 走 `pytesseract+pdf2image`；按操作选 pypdf/pdfplumber/OCR | 保留“按格式/任务选解析器”，并把**先分 born-digital/scan 再决定 OCR**落进 `pdf_ops triage` | 官方 skill 覆盖创建/编辑更广；但读取链没有页级覆盖报告，也没有表结构置信度 advisory |
| 2 | **anthropics/skills · docx**（**157,014★**，整仓） | `skills/docx/SKILL.md@35414756ca55`：L29-40 读内容走 `pandoc --track-changes=all`、裸 XML、转 PDF→图片；L74-76 创建后 validate→fix→repack | 继续用 pandoc 读修订；把“文本读 + 渲染看”双通道写入资源工作流 | 它对 Word 创建/编辑/红线保真强于 Light；Light 只读结构，不内置完整 unpack/edit/pack 工具链 |
| 3 | **anthropics/skills · pptx**（**157,014★**，整仓） | `skills/pptx/SKILL.md@35414756ca55`：L19-26 `markitdown` 抽文 + thumbnail 看全局；L141-203 强制内容 QA、占位符 grep、渲染→检查→修→再验 | 明确 PPT/复杂 PDF 必须**文本层 + 视觉层**双读；只抽文字不算读懂版面 | 它有完整视觉 QA/fix-loop；Light 当前只能调用宿主看渲染图，不自带 PPT 渲染校验脚本 |
| 4 | **anthropics/skills · xlsx**（**157,014★**，整仓） | `skills/xlsx/SKILL.md@35414756ca55`：L76 起 pandas 读表；L137-145 强制 LibreOffice 重算并修错误；L209-224 扫全表公式错误；L273-276 明示 `data_only=True` 保存会丢公式 | 保留“公式字符串≠计算值”红线；公式/缓存值双视图写进工作流 | 它有 recalc+错误扫描闭环；Light 只读公式和缓存值，不能证明公式正确 |
| 5 | **bytedance/deer-flow · academic-paper-review**（**75,639★**，整 harness） | `skills/public/academic-paper-review/SKILL.md@2453718acdee`：L55 深读 Abstract→Related Work→Method→Results→Limitations；L66-73 显式抽 claim/evidence/strength；L243 按论文类型换审查重点 | 论文理解笔记加入**claim→evidence→locator**，按 empirical/theoretical/survey/systems 分重点 | 它做到审稿评价而非纯读取；该职责在 Light 归 idea-critique/review-rebuttal，file-reading 只提取证据结构、不下审稿 verdict |
| 6 | **langchain-ai/deepagents · gpu-document-processing**（**25,463★**，整仓） | `.../gpu-document-processing/SKILL.md@42aeec1ecd40`：L13 以 50+ 页、L14 以 10+ 文件触发重处理；L72 先抽 metadata；L83-84 要求页码与质量问题 | 借“**规模先分级、metadata first、逐页 locator、质量问题显式报**” | 它只有 prose，无配套解析脚本；且依赖 GPU/NVIDIA NIM，与 Light 轻依赖、零 key 目标不合 |
| 7 | **tw93/Waza · read**（**6,152★**） | `skills/read/SKILL.md@ac1cc9d68571`：L16-20 Outcome Contract 明定 source/fetch tier/失败信号；L40-45 本地/代理隐私分层；L113 文件内容视为不可信数据；`fetch_local.py` 有 readability→stdlib 降级及 `<4` 非空行失败底线 | 理解笔记补**读取路径、覆盖范围、失败/降级状态**；延续防文件注入 | 它只覆盖 URL/PDF，且 PDF 主要转 Markdown；Light 多格式与科研下游更完整 |
| 8 | **opendatalab/MinerU-Document-Explorer · mineru-document-explorer**（**596★**） | `skills/.../SKILL.md@a7e9c6cc25b7`：L50-55 大文档必须 `doc_toc→doc_read`，地址连接导航与阅读；L62-63 source 支撑 provenance/stale；`extract_pdf.py` 逐页输出 `page_idx/text/tokens`，local VLM 逐页失败不静默 | 借**先导航后局部深读**、页级地址与来源定位；长文不整份灌上下文 | 它需 qmd/MCP 或重模型（约 2-3GB），默认 PyMuPDF 还带 AGPL 合规判断；Light 不做全文索引/向量检索 |
| 9 | **AlphaLab-USTC/ResearchClaw · paper-reader**（**130★**） | `skills/paper-reader/SKILL.md@9d64c4bda738`：L55 聚焦五大 section；L63-65 CRGP/图/实验；L169-170 真数字+图 URL；L213 对 50+ 页聚焦关键段并诚实跳过 | 论文 R2 工作流采用“结构地图→CRGP/claim-evidence→表图→局限→下游动作” | 它假定 arXiv HTML，结构化强但无抽取覆盖机检；评分仍由模型判断，可能漂移 |
| 10 | **run-llama/llamaparse-agent-skills · liteparse**（**68★**，整仓） | `skills/liteparse/SKILL.md@a8d8b34ad6a8`：L19 **parse once**；L26 born-digital 用 `--no-ocr`；L59 两次 grep 不够再 BM25；L78-98 scan 才 OCR、截图仅最后手段且单页 150dpi；`scripts/search.py` 以 BM25 返回带行号窗口 | **本轮 R1 直接落地**：`pdf_ops triage` 分 text/mixed/scan；SKILL 加“解析一次→按目录/关键词定位→局部视觉读” | LiteParse 有 bbox JSON/OCR/Office 统一 CLI，Light 没有；它需 Node/LibreOffice/ImageMagick |
| 11 | **run-llama/llamaparse-agent-skills · llamaparse**（**68★**，整仓） | `skills/llamaparse/SKILL.md@a8d8b34ad6a8`：L103-112 按 simple/complex 选 tier；L114-124 只 `expand` 所需 text/MD/items/images；L178 custom prompt 控提取 | 借“输入复杂度→解析层级”和“只请求所需产物”，但改成本地免费路线 | 它要求 `LLAMA_CLOUD_API_KEY`、上传云端且可能付费，违反 Light 零 key/不依赖注册；仅列受限备选 |
| 12 | **PSPDFKit-labs/nutrient-agent-skill · nutrient-document-processing**（**11★**） | `nutrient-document-processing/SKILL.md@4d150575a5bb`：L88 scan 要先 OCR 再抽取；L96-98 明禁对 born-digital 盲 OCR；`extract-table.py` 强制显式 input/out/pages | 借 OCR 顺序与显式输出/页范围；triage 只给路线、不替 OCR 成功背书 | DWS 要 API key/联网/额度，违反零 key；商业服务的表抽取也不能替代 Light 的本地可审计路径 |

### R1 结论

1. **同类不稀疏**：仅本轮就找到 12 个真 skill；旧表的“11 同类”其实多数是库/工具，分类失真。
2. **“理解而非抽取”不是独创**：DeerFlow/ResearchClaw 已做结构化论文理解，Waza 已按意图摘要。
3. **市场共识**：先分输入类型、解析一次、长文先导航、页/表/图留 locator、失败显式降级、扫描件才 OCR。
4. **Light 可验证增量**：在零 MCP/零付费 key 下，把上述共识与五面理解笔记、表置信度 advisory、科研下游边界捏成一条
   本地可审计闭环；不是宣称解析精度超过 Docling/MinerU。

### Round 3 五槽重新认证（2026-07-05）

原 Unstructured/PyMuPDF 与 Papers We Love 是解析器/资源槽，不再冒充五个同功能 skill。当前五槽为：

1. `anthropics/skills:pdf`，父仓 158,286★，`9d2f1ae`；
2. `anthropics/skills:docx`，同一父仓、独立 skill，`9d2f1ae`；
3. `bytedance/deer-flow:academic-paper-review`，76,121★，`0016181`，MIT；
4. `langchain-ai/deepagents:gpu-document-processing`，25,695★，`59a665f`，MIT；
5. `tw93/Waza:read`，6,206★，`ff037c6`，MIT。

这是五个直接 skill，但只有四个独立父仓；不得写成“五个独立高星仓库”。五项均已读 SKILL，Waza 还读
`fetch_local.py` fallback；Light 借输入分诊、metadata-first、页级 locator、失败显式化与不可信内容隔离，
不搬 GPU/NIM、MCP、云上传或 paper-review 的下游 verdict。

---

## 0.B 机制锚（解析器 / OCR / 论文结构服务 / 规范；不占 skill 名额）

| 机制锚 | 一手核机制 | 怎么用进 Light | 诚实边界 |
|---|---|---|---|
| **pdfplumber 10,476★ / pypdf** | pdfplumber(MIT)给 char/line/image bbox、layout text、tablefinder；pypdf 做元数据/合并拆分旋转 | 当前 `pdf_ops.py` 本地轻路径 | 都无 OCR/语义版面模型；表格会静默错，故必须 `verify-tables` |
| **GROBID 4,964★（Apache-2.0）** | `grobidOrg/grobid` README L19/L23-39：科研 PDF→TEI，抽 header、references、citation context、section/figure/table/formula； serious work 建议自建 Docker 服务 | 论文 PDF 要精确章节/引用结构时的免费本地重路径；TEI locator 再喂 citation/literature-search | Java/Docker 服务重；不是通用 Office 解析器；输出仍需抽样核 |
| **Docling 62,409★（MIT）** | README L35-42：多格式、reading order、table structure、formula、image classification、OCR，导出 MD/HTML/JSON | 复杂版面/嵌套表/公式的本地重路径 | 模型依赖重；不能把模型输出当 ground truth，数字/表格仍需 locator 复核 |
| **OCRmyPDF 34,037★（MPL-2.0）+ Tesseract 75,030★（Apache-2.0）** | OCRmyPDF README L14-40：扫描 PDF 加可搜索文本层，支持 rotate/deskew，尽量无损保原内容；100+ 语言 | `triage=scanned/mixed` 后的免费本地 OCR 主路径；OCR 后再跑文本抽取并抽样核数字 | Windows 还需 Ghostscript/Tesseract；OCR 会混淆 0/O、1/l、负号/小数点 |
| **PyMuPDF 10,118★ / PyMuPDF4LLM（AGPL-3.0 或商业授权）** | 快速页面渲染、reading order、page chunks、图片/表格抽取；官方许可页明确 AGPL/商业双授权 | 已有环境且合规时可作高速可选路径，不设默认 | 不替用户下法律结论；**嵌入并分发闭源/网络应用前**核 AGPL 义务或商业授权，不能笼统说“处理一个文件就传染输出” |
| **markitdown 161,779★（MIT）** | 多格式→Markdown，适合 LLM 文本分析 | PPTX/Office 轻任务的快速归一入口 | Markdown 不是高保真版面；只转文不算读懂 |
| **unstructured 15,044★（Apache-2.0）** | `partition()` 产 Title/NarrativeText/Table 等 elements，PDF 有 fast/hi_res/ocr_only/auto | 元素分类与按文档特征选策略的机制锚 | 主要面向 RAG chunk；hi_res/OCR 依赖重，不是五面理解笔记 |
| **pandoc** | docx `--track-changes=all` 保增删/批注作者时间；通用 AST 转换 | 读修订稿、模板内容与媒体 | 转换有损；精确 OOXML 结构仍需解包核 |

---

## 0.C 横向机制提炼（直接驱动 R1+R2）

### ① 输入先分级，不要盲选 parser

真同类的共同分水岭是：**born-digital / mixed / scanned / sparse-or-unknown**。LiteParse 与 Nutrient
都明确“文本层存在就不 OCR”；MinerU/LlamaParse 再按复杂版面升级重解析器。Light 原 SKILL 只有 prose，
脚本无确定性分级。本轮给 `pdf_ops.py` 加 `triage`：

- 每页统计非空白文本字符数与图片 bbox 覆盖率；
- 产 `light.file_reading.input_profile.v1`，列 text pages / image-only candidates / sparse pages；
- mixed PDF 明确两路处理并按原页号合并；
- 这是**启发式 advisory，不是 findings 门**；封面/海报/矢量字形会误分，必须抽样看。

### ② 解析一次，先导航再局部深读

LiteParse 的“parse once”、MinerU 的 `doc_toc→doc_read`、ResearchClaw 对 50+ 页聚焦关键 section 是同一
原则：不要每个问题重跑整份 PDF，也不要把全文一次灌进上下文。Light 的 R2 流程固定为：
**triage→一次抽取到临时文件→大纲/关键词定位→只读目标页窗→必要时单页视觉复核**。

### ③ 页/表/图 locator 与覆盖范围必须成为交付物

Waza 要 source/fetch tier，MinerU 用 address，LangChain 要 page references，DeerFlow 要 exact
section/figure/table。理解笔记必须记录：

- 读了哪些页/章节、没读哪些；
- 数字/claim 来自 `p.N / Table N / Figure N / sheet!cell`；
- 低置信度表/OCR 数字列为待复核，不得无定位地进入下游。

### ④ 论文 PDF 要走结构专线，但别把结构抽取误当事实核验

轻路径可用宿主 Read/pdfplumber；要 header/section/reference/citation-context 用 GROBID TEI；复杂表/公式/
reading order 用 Docling/MinerU。无论哪条路，**解析器只告诉“抽到了什么”**：

- DOI/引用是否真实 → citation；
- 多材料术语/指标/claim 是否一致 → consistency；
- 统计是否支持 claim → result-analysis/research-ethics；
- file-reading 不抢这些门，也不替它们下 verdict。

### ⑤ “理解器”要诚实重述为组合能力

ResearchClaw/DeerFlow 已证明结构化理解不是 Light 独创。Light 的组合增量是：
**多格式路由 + 输入分级 + locator/coverage + 五面理解笔记 + 下游动作映射**。其中“读懂内容”本身是
裸模型能力；脚本兑现的是确定性脏活和诚实边界。

### ⑥ advisory 与 hard gate 分开

- `pdf_ops triage`：输入路由 advisory；
- `verify-tables`：表结构风险 advisory（默认阈值 0.6）；
- 两者都 `emits:none`，不进 `run_checkpoint`；
- 只有交给下游后，citation/consistency/research-ethics 等技能才按自己的 findings 契约阻断。

这避免两种错：把“解析器不确定”误判成科研失败；或把“解析成功”冒充引用/claim 已核真。

### ⑦ 隐私、访问与许可先于便利

本地公开工具优先；云上传/代理/付费 key 必须显式征得用户同意并说明数据离开本机。PyMuPDF 的 AGPL
风险只在具体分发/网络使用方式下判断，不能笼统宣称“使用即传染”；不确定时标需合规复核。

---

## 1. R1 落地点（Round 2）

1. **`pdf_ops.py triage`**：新增 PDF 输入分级与逐页路线，借 LiteParse/Nutrient 的 OCR 纪律；
   输出独立 schema，不产 findings。
2. **理解笔记补 coverage/locator**：把“读到哪、没读哪、数字在哪”变成标准字段，借 Waza/MinerU/LangChain。
3. **SKILL 固化 parse-once + navigate-first**：大文档不整份灌上下文，借 MinerU/LiteParse。
4. **论文专线资源地图**：GROBID/Docling/OCRmyPDF/PyMuPDF 分 access/依赖/许可，接到现有脚本与下游门。

---

## 2. 诚实边界

1. `triage` 用文本字符数 + 图片 bbox 比例，**不是扫描件分类模型**；含大背景图的封面会误报，矢量字形/
   加密内容会漏报。
2. 表 confidence 仍是几何启发式；它只提示人工复核，不能证明表结构正确。
3. Light 无 TableFormer/DocLayNet/VLM，也不自带 OCR；复杂版面精度不宣称超过 Docling/MinerU/GROBID。
4. 五面理解笔记由宿主模型填写，质量取决于读取覆盖与 locator；脚本不能证明“已理解”。
5. 不自动建立全文向量索引；跨问复用靠一次抽取文件 + 目录/grep，语义同义词可能漏。
6. PDF 结构专线只抽论文结构；引用真伪、claim 一致性与统计正确性分别交 citation/consistency/
   research-ethics/result-analysis。
7. 云服务（LlamaParse/Nutrient/Mathpix）仅列受限备选，不成为 Light 完成任务的必要条件。

---

## 3. 复核命令

```powershell
# star 当天核（示例；其余同理）
gh api repos/anthropics/skills --jq .stargazers_count
gh api repos/bytedance/deer-flow --jq .stargazers_count
gh api repos/langchain-ai/deepagents --jq .stargazers_count
gh api repos/tw93/Waza --jq .stargazers_count
gh api repos/opendatalab/MinerU-Document-Explorer --jq .stargazers_count

# 真 skill 路径/commit
gh api repos/tw93/Waza/contents/skills/read/SKILL.md --jq .sha
gh api repos/run-llama/llamaparse-agent-skills/contents/skills/liteparse/SKILL.md --jq .sha
gh api repos/AlphaLab-USTC/ResearchClaw/contents/skills/paper-reader/SKILL.md --jq .sha
```

> **唯一真相源声明**：本文件是 file-reading 对标判据 SSOT；`SKILL.md` 只保执行规则与指针。
> star、可达性、版本与服务额度会变，引用前当天重核；查不到写 unknown，绝不编。
