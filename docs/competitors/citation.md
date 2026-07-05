# R1 对标证据 · citation

> 核验日：2026-07-03（Asia/Shanghai）。star 是当日 GitHub
> `stargazers_count` 快照；代码链接固定到 commit。本文把“真同类 skill”
> 与“API/规范/论文/评测集机制锚”分表，避免拿工具名凑 skill 数。

## 旧结论复核

旧表的“防幻觉引用独特 / 真同类稀疏”不成立。GitHub code search 后逐个
读 SKILL 及配套实现，至少找到下表 9 个真同类。DOI 查询、DataCite
fallback、BibTeX 生成、citekey/文献库管理、多源检索、claim-level
核验、source inventory 都已有公开实现，不能称为 Light 独有。

Light 可主张的差异只能是本次证据支持的**组合闭环**：作者材料 inventory
provenance → 注册源+独立字段源且逐源保值 → DOI RA/Crossref/DataCite
联合的 `CONFIRMED-MISSING` → 多字段嵌合 critical → locator-backed
claim↔citation review → canonical registry/BibTeX/CSL/evidence/failure
→ stage-10 checkpoint → typesetting 真实消费。下表同类各覆盖其中一部分；
未发现一个在固定快照中同时实现全部接线。该表述不把任何单项说成独有。

## A. 真同类 skills（真读 SKILL + 配套脚本/模板）

| skill（当日 star；固定 commit） | 真读文件/行 | 具体机制 | 可借点 | Light 开工前真实差距 |
|---|---|---|---|---|
| [OneCite](https://github.com/HzaCode/OneCite)（61★；[`3680552`](https://github.com/HzaCode/OneCite/tree/36805520be762e227673f5225b7337788d2379e2)） | [SKILL L25-L26](https://github.com/HzaCode/OneCite/blob/36805520be762e227673f5225b7337788d2379e2/skills/onecite/SKILL.md#L25-L26)、[L109-L116](https://github.com/HzaCode/OneCite/blob/36805520be762e227673f5225b7337788d2379e2/skills/onecite/SKILL.md#L109-L116)；[identifier L260-L281](https://github.com/HzaCode/OneCite/blob/36805520be762e227673f5225b7337788d2379e2/onecite/pipeline/identifier.py#L260-L281)；[journal template](https://github.com/HzaCode/OneCite/blob/36805520be762e227673f5225b7337788d2379e2/onecite/templates/journal_article_full.yaml) | 原始引用留痕、strict unresolved gate、Crossref 404 后一律 DataCite fallback、多类型模板、离线 benchmark | “格式成功≠真”的显式边界；不靠 DOI prefix 猜 DataCite；原始输入和失败项保留 | 旧 Light 把 Crossref 当单源骨架，DataCite/RA 缺失；没有 canonical registry |
| [CiteCheck](https://github.com/color4-alt/CiteCheck)（50★；[`fae7888`](https://github.com/color4-alt/CiteCheck/tree/fae7888bf7c1ce92bbafad15faf61cf55b7e2bd7)） | [SKILL L17-L20](https://github.com/color4-alt/CiteCheck/blob/fae7888bf7c1ce92bbafad15faf61cf55b7e2bd7/skills/citecheck/SKILL.md#L17-L20)、[L88-L99](https://github.com/color4-alt/CiteCheck/blob/fae7888bf7c1ce92bbafad15faf61cf55b7e2bd7/skills/citecheck/SKILL.md#L88-L99)；[verifier L99-L140](https://github.com/color4-alt/CiteCheck/blob/fae7888bf7c1ce92bbafad15faf61cf55b7e2bd7/src/citecheck/verifier.py#L99-L140)；[matcher L157-L239](https://github.com/color4-alt/CiteCheck/blob/fae7888bf7c1ce92bbafad15faf61cf55b7e2bd7/src/citecheck/matcher.py#L157-L239) | LaTeX/PDF 抽取；Crossref/S2/OpenAlex/PubMed/arXiv/DBLP 顺序查询；正文引用上下文对摘要做 semantic review | existence 与 thematic/semantic accuracy 分层；source unreachable 明示 | 旧 Light 只有论文 A→B edge，claim↔citation 仍停在人工文档，没有机读 edge |
| [citation-assistant](https://github.com/ZhangNy301/citation-assistant)（222★；[`b1fde76`](https://github.com/ZhangNy301/citation-assistant/tree/b1fde7699972e9cedbb6bf16df10aefb18c21769)） | [SKILL L8-L13](https://github.com/ZhangNy301/citation-assistant/blob/b1fde7699972e9cedbb6bf16df10aefb18c21769/SKILL.md#L8-L13)、[L95-L108](https://github.com/ZhangNy301/citation-assistant/blob/b1fde7699972e9cedbb6bf16df10aefb18c21769/SKILL.md#L95-L108)；[S2 L47-L55](https://github.com/ZhangNy301/citation-assistant/blob/b1fde7699972e9cedbb6bf16df10aefb18c21769/scripts/s2_search.sh#L47-L55)；[doi2bib L18-L31](https://github.com/ZhangNy301/citation-assistant/blob/b1fde7699972e9cedbb6bf16df10aefb18c21769/scripts/doi2bibtex.sh#L18-L31) | 语义查询、S2 元数据、429→Crossref fallback、DOI 内容协商 BibTeX | 限流 fallback 是一等路径；不手写 BibTeX | 旧 Light 虽有内容协商，但错误状态没有把 429/5xx 从 missing 完整分开 |
| [AI-Research-Orchestrator citation](https://github.com/jacazjx/AI-Research-Orchestrator)（1★；[`1d6e951`](https://github.com/jacazjx/AI-Research-Orchestrator/tree/1d6e951a360c03f6256acb45cef57b6758fc9077)） | [SKILL L44-L70](https://github.com/jacazjx/AI-Research-Orchestrator/blob/1d6e951a360c03f6256acb45cef57b6758fc9077/skills/citation/SKILL.md#L44-L70)、[L112-L141](https://github.com/jacazjx/AI-Research-Orchestrator/blob/1d6e951a360c03f6256acb45cef57b6758fc9077/skills/citation/SKILL.md#L112-L141)、[L165-L172](https://github.com/jacazjx/AI-Research-Orchestrator/blob/1d6e951a360c03f6256acb45cef57b6758fc9077/skills/citation/SKILL.md#L165-L172)；[extract L77-L95](https://github.com/jacazjx/AI-Research-Orchestrator/blob/1d6e951a360c03f6256acb45cef57b6758fc9077/scripts/citation/extract_citation_needs.py#L77-L95)；[retry codes L76](https://github.com/jacazjx/AI-Research-Orchestrator/blob/1d6e951a360c03f6256acb45cef57b6758fc9077/scripts/citation/fetch_verified_bibtex.py#L76) | citation-gap 抽取、verification ledger、BibTeX provenance fields、claim-citation mapping、跨库冲突上浮、retryable HTTP | provenance 不塞进模糊 prose；用户 `.bib` 不被覆盖；429/5xx 独立重试 | 旧 Light 无作者级 ledger/registry，逐源冲突只散落 warning |
| [workflows cite-check](https://github.com/edwinhu/workflows)（17★；[`dc228a3`](https://github.com/edwinhu/workflows/tree/dc228a3993a47a622d1a32554e2bdea009aa4f41)） | [SKILL L89-L103](https://github.com/edwinhu/workflows/blob/dc228a3993a47a622d1a32554e2bdea009aa4f41/skills/cite-check/SKILL.md#L89-L103)、[L159-L182](https://github.com/edwinhu/workflows/blob/dc228a3993a47a622d1a32554e2bdea009aa4f41/skills/cite-check/SKILL.md#L159-L182)；[source inventory L82-L99](https://github.com/edwinhu/workflows/blob/dc228a3993a47a622d1a32554e2bdea009aa4f41/scripts/cite-fidelity/nlm_source_inventory.py#L82-L99)；[gate L343-L350](https://github.com/edwinhu/workflows/blob/dc228a3993a47a622d1a32554e2bdea009aa4f41/scripts/cite-fidelity/check_section_cites.py#L343-L350) | 每源 inventory（supports/does_not_support）、逐 occurrence claim check、quoted passage 再对 PDF 做 LCS grounding、unsupported gate | “模型说支持”仍要回源 grounding；一源一摘要便于复用 | 旧 Light locator_audit 只有说明文，没有 registry claim edge 或 failure artifact |
| [thesis-citation-audit](https://github.com/ekontoTURBO/thesis-citation-audit)（0★；[`2d8592b`](https://github.com/ekontoTURBO/thesis-citation-audit/tree/2d8592b49024db76a2b6fc327a2601e6a88cd217)） | [SKILL L10-L18](https://github.com/ekontoTURBO/thesis-citation-audit/blob/2d8592b49024db76a2b6fc327a2601e6a88cd217/SKILL.md#L10-L18)、[L195-L201](https://github.com/ekontoTURBO/thesis-citation-audit/blob/2d8592b49024db76a2b6fc327a2601e6a88cd217/SKILL.md#L195-L201)；[extract L213-L252](https://github.com/ekontoTURBO/thesis-citation-audit/blob/2d8592b49024db76a2b6fc327a2601e6a88cd217/scripts/extract_thesis.py#L213-L252)；[section prompt L18-L22](https://github.com/ekontoTURBO/thesis-citation-audit/blob/2d8592b49024db76a2b6fc327a2601e6a88cd217/templates/section_prompt.md#L18-L22) | DOCX 逐 occurrence inventory、paragraph/context provenance、PDF printed-page offset、语义/页码/书目多状态 | 图表/补充材料和页码也是引用 inventory；相关页邻页检查 | 旧 Light 只扫 DOI/.bib，没有统一吃正文、表图、补充材料 |
| [zotero-skill](https://github.com/AkaLiu/zotero-skill)（3★；[`454c5e6`](https://github.com/AkaLiu/zotero-skill/tree/454c5e66bf6571bb77817256526858a37d7daab5)） | [SKILL L14-L18](https://github.com/AkaLiu/zotero-skill/blob/454c5e66bf6571bb77817256526858a37d7daab5/SKILL.md#L14-L18)、[L119-L132](https://github.com/AkaLiu/zotero-skill/blob/454c5e66bf6571bb77817256526858a37d7daab5/SKILL.md#L119-L132)；[API L58-L66](https://github.com/AkaLiu/zotero-skill/blob/454c5e66bf6571bb77817256526858a37d7daab5/scripts/zotero_api.py#L58-L66)、[attachment L118-L131](https://github.com/AkaLiu/zotero-skill/blob/454c5e66bf6571bb77817256526858a37d7daab5/scripts/zotero_api.py#L118-L131) | Zotero 本地 API、附件/笔记/PDF locator、local-first 再 OpenAlex | 先吃作者已有人工笔记和 PDF，不把在线库当唯一真相 | Light 核心不能依赖 Zotero，但应支持其导出作为 inventory 输入并分层标可选 |
| [litdb](https://github.com/jkitchin/litdb)（82★；[`86fdc59`](https://github.com/jkitchin/litdb/tree/86fdc5987a7a8db43a76370503e7a62250483cc9)） | [SKILL L30-L44](https://github.com/jkitchin/litdb/blob/86fdc5987a7a8db43a76370503e7a62250483cc9/SKILL.md#L30-L44)、[L143-L159](https://github.com/jkitchin/litdb/blob/86fdc5987a7a8db43a76370503e7a62250483cc9/SKILL.md#L143-L159)；[bibtex L47-L82](https://github.com/jkitchin/litdb/blob/86fdc5987a7a8db43a76370503e7a62250483cc9/src/litdb/bibtex.py#L47-L82) | DOI/文件入库、OpenAlex metadata、vector/full-text、从统一 work 生成 BibTeX | canonical work → derived BibTeX，而非 `.bib` 反客为主 | 旧 Light 没有 canonical registry，多个脚本各自产局部真相 |
| [codex-citation-audit-zotero](https://github.com/maxrusse/codex-citation-audit-zotero)（0★；[`06998ab`](https://github.com/maxrusse/codex-citation-audit-zotero/tree/06998aba4c4729144c289ff99e157051b4efa4b9)） | [SKILL L19-L33](https://github.com/maxrusse/codex-citation-audit-zotero/blob/06998aba4c4729144c289ff99e157051b4efa4b9/citation-audit/SKILL.md#L19-L33)、[L44-L51](https://github.com/maxrusse/codex-citation-audit-zotero/blob/06998aba4c4729144c289ff99e157051b4efa4b9/citation-audit/SKILL.md#L44-L51)；[prompt L10-L31](https://github.com/maxrusse/codex-citation-audit-zotero/blob/06998aba4c4729144c289ff99e157051b4efa4b9/citation-audit/references/prompt-template.md#L10-L31)；[resolver L1153-L1186](https://github.com/maxrusse/codex-citation-audit-zotero/blob/06998aba4c4729144c289ff99e157051b4efa4b9/citation-resolver/docx_zotero_integrator.py#L1153-L1186) | 原子 claim ID、fully/partially/not supported、claim↔reference 双向表、unmatched numbers 和转换报告 | 每个 DOI 必须能回至少一条 claim，每个修订 claim 必须有 rationale | 旧 Light paper-writing claim map 到 citation 没有真实消费契约 |

## B. 机制锚（不计入真同类 skill 数）

| 机制锚 | 一手来源 | 本次采用的事实/边界 |
|---|---|---|
| Crossref REST | [REST API](https://www.crossref.org/documentation/retrieve-metadata/rest-api/)、[filters](https://www.crossref.org/documentation/retrieve-metadata/rest-api/rest-api-filters/) | `/works/{doi}` 是 Crossref DOI 单记录；REST 无需注册；`has-update` 指“被另一 DOI 更新”，`is-update` 指“是对另一 DOI 的更新” |
| DOI Registration Agency | `https://doi.org/ra/{doi}` 活体响应 | 返回 RA 或明确 `DOI does not exist`；它是 missing 联合证据，不提供完整书目字段 |
| DataCite REST | [single DOI](https://support.datacite.org/docs/api-get-doi)、[API overview](https://support.datacite.org/docs/api) | `GET /dois/{id}` 返回完整 DataCite metadata；公开读取免 key；Crossref 404 不能否定 DataCite DOI |
| PubMed E-utilities | [NCBI API](https://www.ncbi.nlm.nih.gov/home/develop/api/)、[E-utilities](https://www.ncbi.nlm.nih.gov/sites/books/NBK25497/) | ESearch/ESummary 是独立生医字段源；无 key 有速率约束，限流不能当 missing |
| Semantic Scholar Graph | [Academic Graph API](https://api.semanticscholar.org/api-docs/graph) | DOI paper lookup 可作独立索引字段源；404/429 只说明该源状态，不能单源宣判不存在 |
| OpenAlex | [developer overview](https://developers.openalex.org/) | 当前 API 免费但需要免费 key，并有免费日额度；只作可选增强，不能成为无账号核心路径 |
| CSL / styles | [CSL 1.0.2 spec](https://docs.citationstyles.org/en/v1.0.2/specification.html)、[official styles](https://github.com/citation-style-language/styles) | CSL JSON/样式是结构化 metadata → 多格式排版机制；格式成功不证明引用真实或支持 claim |
| Crossmark / Retraction Watch | [Crossmark updates](https://www.production.crossref.org/documentation/crossmark/participating-in-crossmark/)、[RW access](https://www.crossref.org/documentation/retrieve-metadata/retraction-watch/) | 更新通知有独立 DOI 和类型；对具体 DOI 必须核关系方向。活体 `10.1021/am300292v` 原文为 `updated-by`→`10.1021/acsami.9b11759`，通知反向 `update-to`→原文 |
| SciFact / SciFact-Open | [SciFact](https://aclanthology.org/2020.emnlp-main.609/)、[SciFact-Open](https://aclanthology.org/2022.findings-emnlp.347/) | claim verification 需要 SUPPORT/REFUTE 与 evidence rationale；开放域检索存在明显泛化下降，机器 verdict 必须保留人工/locator 边界 |
| ALCE | [paper](https://arxiv.org/abs/2305.14627)、[evaluation code](https://github.com/princeton-nlp/ALCE) | citation quality 与文本流畅/事实回答分开评估；有 citation 不等于 citation entailment |

## C. 借点如何落入 Light（不是只写笔记）

| R1 借点 | 落地 |
|---|---|
| OneCite 原始输入 + unresolved strict + DataCite fallback | `citation_registry.py` inventory provenance；`verify_refs.py` RA/Crossref/DataCite 状态机 |
| ARIS provenance ledger + 跨库冲突上浮 | `light.citation_registry.v1.source_evidence/field_conflicts`；`references/registry_contract.md` |
| CiteCheck / claim audit 的语义层 | registry `claim_edges`；`citation_verify_gate.py` relevance warn |
| workflows 的 source inventory / does-not-support | `templates/claim_citation_review.json`；`claim-citation-review.json` 失败件 |
| thesis audit 的正文/图表/补充材料 occurrence | `citation_registry.py --draft/--figure/--supplement` |
| litdb 的 canonical work → derived BibTeX | registry 为 SSOT；`.bib`/CSL 从 confirmed work 派生 |
| retryable HTTP 独立处理 | `UNAVAILABLE`；429/5xx 永不升级 `CONFIRMED-MISSING` |
| Zotero local-first 可选资源 | `citation-resource-map.md` 资源分层；不进入核心依赖 |

## D. 诚实差异与剩余边界

- 已做差异：逐源值不覆盖、联合 missing 证据、多字段 chimeric critical、
  claim edge + canonical delivery + stage-10/typesetting 接线。
- 没做成全自动：全文语义支持、版本等价、作者音译、出版社错误元数据、
  所有撤稿/更正覆盖都仍需人工与上游事实源。
- `CONFIRMED` 只说明标识和核心书目字段被两个独立源确认，不说明研究
  结论正确、未被撤稿、适合当前 claim 或应当引用。
- research-ethics 仍是撤稿/更正/EoC 的诚信终判；citation 只交事实警报。
- stage 10 只有 citation 自身 confirmed-missing/chimeric critical；网络、
  安全、格式、relevance 不擅自扩大 critical 面。

## E. Round 3 落地：registry 派生四关

R2 已有四关合约（existence → identity → directed publication status →
locator-backed claim support），但执行入口主要是 `templates/citation-four-gate.example.json`，
真实项目容易把 canonical registry 的状态手工重录一遍，造成 drift。尤其是
`publication_updates` 的 `updated-by` 方向、claim edge 的 access/hash/reviewer 和
retraction purpose handling，不应由人工模板再抄一次。

本轮新增 `citation_four_gate.py --registry <citation-registry.json>`：

- 从 `light.citation_registry.v1.works[]` 派生 existence 与 identity；
- 从 `publication_updates[]` 派生 `ACTIVE / CORRECTED / RETRACTED /
  EXPRESSION_OF_CONCERN`，并保留 `source_work_id=原文 DOI` →
  `target_work_id=notice DOI` 的有向关系；
- 从 `claim_edges[]` 派生 DIRECT / PARTIAL / BACKGROUND / CONTRADICTORY /
  UNRESOLVED 与 FULLTEXT / ABSTRACT_ONLY / METADATA_ONLY / UNAVAILABLE；
- 继续让撤稿工作仅可用于 historical record，不能静默支撑当前科学结论；
- selftest 覆盖 registry 中 `updated-by` retraction 转为 `RETRACTED_DEPENDENCY`
  和摘要显式支持 pass。

边界：citation 仍只记录出版更新事实和用途门；“是否构成不端、是否需要撤稿措辞”
归 research-ethics/期刊/机构处理。

## F. Round 3 补强：claim-support 审查防漂移

继续深读自身链路后发现一个更隐蔽的诚信风险：locator-backed review
虽然要求 source locator、source evidence hash、reviewer 和 reviewed_at，
但没有把 review 绑定到“当前这句 claim”。如果论文写作阶段改写了 claim
强度或范围，旧 citation verdict 可能仍被复用。

本轮把 `citation_registry.py`、`citation_four_gate.py` 与
`citation_verify_gate.py` 接到同一约束：

- registry 为每条 claim edge 计算当前 `claim_text_sha256`；
- 人工/流程复核必须写入 `reviewed_claim_sha256`；
- 两者缺失或不一致时，`SUPPORTS/PARTIAL/RELATED_ONLY/UNSUPPORTED` 都降为
  `REVIEW_REQUIRED` 或在四关中阻断 claim-support；
- public templates 保持 fail-closed，防止手写 fixture 绕过 canonical registry。

这不是把语义支持自动化；它只保证人工语义判断没有在 claim 改写后漂移。
