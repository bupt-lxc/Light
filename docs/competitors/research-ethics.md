# competitors — light-research-ethics

> Round 2 R1 真相源。先把“别人怎样把科研伦理做成 agent skill”与规范、工具、数据库分开，再决定 Light 借什么。
> GitHub star 是外部可变事实，均为 `[snapshot 2026-07-02, source=GitHub REST API]`；复核命令：
> `gh api repos/<owner>/<repo> --jq .stargazers_count`。维护者：Light0305。

## 0.A 真同类 skill（10 个技能 / 8 个 repo）

判据：存在可被 agent 发现并调用的 `SKILL.md`，且核心任务包含研究伦理评估、IRB/伦理申请、知情同意或科研诚信审查。
peer-review、实验管理等只在伦理模块与本技能直接重叠时列入；法规、数据库、R 包不占名额。

| # | 同类 skill（star） | 已读文件与可复验机制 | 借进 Light | Light 诚实差在哪 |
|---|---|---|---|---|
| 1 | `beita6969/ScienceClaw` · `research-ethics`（856★） | `skills/research-ethics/SKILL.md` 把任务拆成 7 步：法域→风险→protocol→consent→数据保护→诚信→持续合规；输出协议、同意书、风险表、DMP。 | R2 采用“先判法域与项目阶段，再选资源/工件”的顺序；硬闸门不再只看投稿末端。 | 对方覆盖全生命周期但纯 prose、无脚本、无 findings/exit code；Light 的统计重算与阻断更硬。 |
| 2 | `AlterLab-IEU/AlterLab-Academic-Skills` · `alterlab-research-ethics`（37★） | `skills/research-tools/.../SKILL.md` 覆盖伦理委员会、consent、DMP、2024 Helsinki、GDPR/HIPAA、脆弱人群、欺骗、COI、dual use，并明确法域化分流。 | 资源图加入“国际原则不能替代本机构表单/本地法”的 authority ladder；把 dual-use 与 COI 纳入项目分诊。 | 内容全面但主要靠清单；无撤稿三态、统计复算或 claim 级证据门。 |
| 3 | 同 repo · `alterlab-tr-research-ethics`（37★，独立 skill） | `scripts/consent_form_check.py:49` 定义最低要素表，`:132` 逐项 lint，`:151` 输出 checked/pass/missing；docstring 明写 PASS 仅代表要素出现、不是委员会签字。 | 借“官方最小要素→确定性 completeness lint→仍需机构裁定”的三段边界；R2 明确表单级检查应优先复用机构模板。 | Light 暂无法域化 consent linter；不冒充已有。现阶段登记为人工/机构表单核。 |
| 4 | `WafaJohal/academic-skills` · `ethics-reviewer`（0★） | `ethics-skills/ethics-reviewer/SKILL.md` 用 6 域审查与 4 级严重度；把 application、PLS、consent、附件一致性与常见 reviewer hotspots 放进一轮。 | 把“主申请表↔同意书↔招募材料↔数据计划”跨附件一致性加入 R2 收口；输出按 BLOCK/WARN/NOTE 排序。 | 强依赖澳洲 HREC/Infonetica 与本机构 boilerplate；Light 不复制法域专属条款。 |
| 5 | 同 repo · `ethics-writer`（0★，独立 skill） | `ethics-skills/ethics-writer/SKILL.md` 用 4 阶段访谈逐轮确认，再产 Infonetica 申请、PLS、consent；明确不一次倾倒所有问题。 | 借“分阶段访谈 + 每段确认”的交互手艺；事实缺口先 ASK，不用模板替用户编。 | 对方擅长申请写作；Light 当前主场是审查/阻断，不宣称能生成任何机构的 submission-ready 表单。 |
| 6 | `MattArtzAnthro/AI-Anthropology-Toolkit` · `irb-protocol`（19★） | `skills/irb-protocol/SKILL.md:112-154` 生成 13 节 protocol；`:201-232` 要求非 boilerplate、区分 consent process/documentation、处理 deductive disclosure、ongoing consent、digital ethnography、amendment plan。 | 补“动态同意、可搜索引文导致再识别、社区伤害、方案变更需 amendment”四个真实盲区。 | 专注定性/人类学，统计诚信与出版后状态不是其主场；Light 需保持跨学科而不照搬方法专属模板。 |
| 7 | `ccashwell/qualitative-research-pro` · `research-ethics`（0★） | `skills/research-ethics/SKILL.md` 强调 process consent、小社区即使去名仍可识别、敏感话题再确认和 community harm。 | 数据伦理不再等同“删姓名”：分离 anonymity、confidentiality、deductive disclosure 与社区层面风险。 | 纯 prose、无法域路由和机器门。 |
| 8 | `FW1201/tw-research-skills` · `tw-research-ethics-reviewer`（6★） | `tw-research-ethics-reviewer/SKILL.md` 依对象/数据类型/敏感度分诊，产风险报告、文件清单、IRB 准备指引。 | 借中文用户入口与“先给材料清单再写”的交互；明确机构确认权。 | 其 Exempt/Expedited/Full Board 映射过于简化，且把“所有人体研究必须通过 IRB”说得过满；Light 不借这两处。 |
| 9 | `dedy45/QuantLab` · `ethics-review`（0★） | `.agent/skills/ethics-review/SKILL.md` 用 protocol deconstruction→五类风险→逐风险 mitigation→法域复核→风险矩阵，并把 participant welfare 放在科学收益之前。 | R2 风险登记必须是“风险、受影响者、可能性/严重性、缓解、owner、证据”，不接受“已采取适当措施”。 | 无可执行检查、未处理出版诚信与 post-publication 状态。 |
| 10 | `faizalhaini958/igris` · `ethics-checker`（0★） | `skills/ethics-checker/SKILL.md` 给 consent、匿名/保密、脆弱人群、incident/referral、批准前不得开工的 10 步流程，并显式落马来西亚语境。 | 借“批准前不采集”“incident/adverse event 是进行中义务”，加入生命周期复查点。 | 法域内容较粗且无官方链接快照；只能借工作流，不能借其法律结论。 |

补充读过但不占 10 个名额：

- `Imbad0202/experiment-agent`（128★）的 human-study `manage` 模式只碰元数据、不碰 raw participant data，并在 resume 时重核 IRB 状态；这是“批准不是一次性文件”的好机制，但该 skill 核心是实验执行。
- `davila7/claude-code-templates`（28,405★）的 scientific peer-review 检查 IRB、consent、vulnerable population、IACUC 与图像诚信；它证明伦理应嵌入审稿，但核心任务是 peer review。
- `Aperivue/medsci-skills`（174★）把 `write-protocol` 与 `fill-protocol` 分开：先写科学内容，再原位填机构 Word 模板并报告 unmatched labels；它是 IRB 工件工程的强锚，但不等于横切科研诚信门。

## 0.B 机制锚（不占 skill 名额）

| 权威资源 / 工具 | 可复验机制 | Light 怎样用 |
|---|---|---|
| OHRP 45 CFR 46 + 2018 Requirements decision charts | 先判是否 human-subjects research，再判 exemption/expedited/full review；机构 Terms of Assurance 与本地 IRB 有最终约束力。 | `references/ethics-resource-map.md` 的涉人分诊入口；不让模型自行宣布 exempt。 |
| ORI 42 CFR Part 93（2024 rule） | 对 2026-01-01 后收到的 allegation 适用新版程序；调查认定不是作者/LLM 职权。 | 保留“信号≠定罪”，资源图按 allegation date 与法域路由。 |
| COPE Core Practices / flowcharts | 把 misconduct、authorship、COI、data、corrections 分成程序路径，重点是下一步找谁与保全什么。 | `decision_trees.md` 的升级路径，不把 COPE 当自动判罪器。 |
| ICMJE Recommendations（2026-01 更新）+ CRediT Z39.104-2022 | ICMJE 管作者资格与责任；CRediT 的 14 角色只描述贡献，不能决定谁是作者。AI 不可列作者，使用须按目标刊政策披露。 | 署名表必须同时保留 qualification 与 contribution 两层；venue 政策当天核。 |
| WMA Declaration of Helsinki 2024 | 2024 是唯一现行官方版本；旧版只供历史引用。 | 医学研究原则层；不能替代本地伦理委员会审批。 |
| ARRIVE 2.0 Essential 10 + Recommended Set | 动物研究报告最低信息与完整最佳实践分层。 | 涉动物路线联动 research-plan/figure/paper-writing；报告合规不等于已获 IACUC。 |
| Crossref production REST + Retraction Watch dataset | 原文记录用 `updated-by` 指向撤稿/更正通知，通知记录用反向 `update-to` 指回原文；RW CSV 每工作日更新，Labs API 已停止更新。 | `check_retractions.py` 只用适用于“被查原文”的 `updated-by` + 标题兜底；CLEAN 仅表示该源未见信号，UNRESOLVED 不放行。 |
| statcheck / GRIM / PPS | 报告统计量可重算；均值粒度可检查；tortured phrase 只能作为筛查信号。 | 保留既有 4 个已验证脚本，不重写核心。 |
| 中国卫健委 2023 人体研究伦理办法 | 官方原文覆盖以人为参与者或使用人的样本/信息数据；伦理委员会有批准/不批准/修改/暂停/终止等决定权。 | 更新 `cn_compliance.md`，不再声称官网不可访问；具体项目仍回查机构 SOP。 |
| 科技部 2023 科技伦理审查办法（试行）+ 2022 科研失信调查规则 | 范围包含人、实验动物及可能影响生命健康/生态/公共秩序的活动；失信调查第一责任主体是有关单位。 | 中国法域分流与 dual-use/广义科技伦理入口；不得由技能直接认定。 |

## 0.C 横向提炼与 R1 落地

1. **真实工作不是一张总清单**：同类先判法域、研究对象、数据敏感度、项目阶段，再决定表单与审查路径。落地为
   `references/ethics-resource-map.md` 的五步闭环。
2. **consent 是过程，不只是签字页**：定性研究、长期田野、录音录像、二次使用和方案变更需要 ongoing/layered consent 与
   amendment 触发。落地到 SKILL 的规划、采集、变更三次复核。
3. **去标识不等于无再识别风险**：小社区、可搜索原话、跨表连接、影像/声音会造成 deductive disclosure。落地到数据发布门。
4. **跨附件一致性是委员会真正在抓的错**：申请表、PLS/同意书、招募材料、DMP、分析与分享计划必须一致。现阶段为人工
   checklist + locator，不假装已有自动跨文档语义检查。
5. **表单 completeness 可机检，伦理裁定不可机检**：同类的 consent linter 证明“要素有无”值得确定性检查；但本轮不凭空造
   通用表单 linter，因为字段由法域/机构决定。优先使用机构原模板并登记 `N/A + reason`。
6. **Light 的真差异仍是确定性诚信门**：统计重算、撤稿三态、文本重合、tortured phrase、claim↔evidence 绑定与
   `light.findings.v1` 阻断；本轮修掉“整份 evidence 的 strongest grade 兜底全文”，改为消费
   `light.paper_claims.v1`，一条 claim 只能用自己的 evidence IDs。

## 0.D 诚实边界

### Round 3 五席重认证（2026-07-05）

105 项矩阵原有 The Turing Way、NeurIPS/TOP、Heilmeier 三个规范/方法锚，不能算同功能
agent skill。本轮用已在本报告深读、并重新核对当前固定提交的三个直接对象替换：

| 席位 | 直接 skill | 当前父仓 / 固定 commit | 本轮亲读 |
|---:|---|---|---|
| 1 | `alterlab-research-ethics` | 38★、MIT / `a0064fd54180541785cd1986ad8eb1689b834270` | 完整 398 行 SKILL；法域分流、IRB/consent/DMP、脆弱人群、COI、dual-use、诚信与持续义务 |
| 2 | `alterlab-tr-research-ethics` | 同仓同 commit | 完整 205 行 SKILL + 215 行 `consent_form_check.py`；委员会路由、双语 dossier、TİTCK 最小要素 lint 与“PASS 不等于批准”边界 |
| 5 | `WafaJohal/academic-skills/ethics-reviewer` | 0★ / `d165260248b330b40691c096234249f8f8f5d0ee` | 完整 291 行 SKILL；application、PLS、consent、招募与附件一致性，按域和严重度审查 |

采用度低如实保留；研究伦理 skill 生态没有可验证的千星专职对象，不能拿高星规范或通用
peer-review 凑数。规范仍是 authority/evidence source，但不再占“五个同功能 skill”席位。
三者可借机制已由 authority lifecycle、consent scope、attachment matrix 与 evidence gate
覆盖，因此本轮不重复造法域模板，也不把机器 completeness 冒充伦理批准。

- 同类技能的法域模板只能作为结构参考；机构 IRB/HREC/IACUC、法律顾问、期刊与调查机构才有决定权。
- 本技能没有图像取证、全库查重、法律意见、伦理委员会提交权限，也没有通用 IRB 表单法域 linter。
- `claim_evidence_bind` 核的是“绑定是否存在、措辞是否超档”，不核实验是否真实复现、统计是否正确计算或因果是否成立。
- 远程资源、法规和政策会变；每次高利害交付必须记录 URL、版本/日期、访问状态与机构确认人。

## 0.E Round 3 落地：consent scope 机器门

R2 已经从同类 skill 学到“consent 是过程”“录音/公开引文/二次使用/共享要分别说明”“跨附件一致性是伦理审查常见抓错点”，
但 Light 当时只做到：有 consent process/form 证据、authority scope delta 与人工清单。新的硬缺口是：**一份同意书存在，不等于所有实际用途都被同意范围覆盖**。

2026-07-05 复核的官方依据：

- OHRP Informed Consent FAQ：informed consent 是 investigator 与 prospective subject 的持续交流；签名页本身不等于充分 consent process。
- NIH DMS consent resource：二次研究的数据/生物样本存储与共享需要在 consent 语境中说明，未来研究、机构/商业实体、全球共享与控制主体都应被说清。
- OHRP Withdrawal guidance：寻求 consent 时应说明参与者退出后已收集数据是否仍会保留并分析。
- NIH DMS Final Policy：人类参与者数据的开放共享要与 consent practices、法律和规范一致，并且参与者应被适当告知并事先同意。
- HHS HIPAA de-identification guidance：去标识不只是删姓名；Safe Harbor 仍受“actual knowledge”再识别风险约束，唯一特征、日期、自由文本等都可能造成再识别。

本轮新增 `scripts/consent_scope_gate.py` 与 `assets/consent-scope-packet.example.json`：

- schema 为 `light.consent_scope_packet.v1`；
- 逐项登记 `planned_or_actual_uses[]`：参与、干预、问卷、访谈、录音录像、公开引文、生物样本、可识别数据、二次使用、future reuse、
  data sharing、repository release、跨境传输、model training、withdrawal retention；
- 每项用途必须绑定 `EXPLICIT_CONSENT` / `BROAD_CONSENT` / `ASSENT_AND_PERMISSION` / `WAIVED_BY_AUTHORITY` /
  `NOT_REQUIRED_BY_AUTHORITY` 的 VERIFIED source、locator、checked_at；
- 录音、公开引文、可识别数据、二次使用、共享、发布、跨境、模型训练等敏感用途需要 `specific_scope_locator`，不能由通用 consent 自动兜底；
- 小社区、可搜索原话、声音/影像等 deductive disclosure 风险需要 mitigation locator；
- 数据共享、repository release、跨境传输或模型训练需要 withdrawal boundary locator；
- protocol / consent / recruitment / DMP 跨附件一致性 UNKNOWN 在早期计划阶段 warn，进入采集、分析或发布阶段 fail-closed。

诚实边界：该门仍不做 waiver/exempt 裁定，不检查全球各机构 IRB 表单字段是否完备，不给法律意见；它只把“实际用途是否被已登记同意/豁免/authority 范围覆盖”
从 prose 清单升级为可运行阻断门。

## Sources（R2 当天核）

- GitHub peer files：上表各 repo/path；star 用 GitHub REST API 当天核。
- OHRP：`https://www.hhs.gov/ohrp/regulations-and-policy/regulations/45-cfr-46/`
  · `https://www.hhs.gov/ohrp/regulations-and-policy/decision-charts/`
- ORI：`https://ori.hhs.gov/sites/default/files/2025-06/Implementing%20the%20Final%20Rule_final.pdf`
- COPE：`https://publicationethics.org/core-practices` · `https://publicationethics.org/guidance/Flowcharts`
- ICMJE：`https://www.icmje.org/recommendations/` · CRediT：`https://credit.niso.org/`
- WMA：`https://www.wma.net/what-we-do/medical-ethics/declaration-of-helsinki/`
- ARRIVE：`https://arriveguidelines.org/arrive-guidelines`
- Crossref Retraction Watch：`https://www.crossref.org/documentation/retrieve-metadata/retraction-watch/`
- 中国：`https://www.nhc.gov.cn/qjjys/c100016/202302/6b6e447b3edc4338856c9a652a85f44b.shtml`
  · `https://www.most.gov.cn/xxgk/xinxifenlei/fdzdgknr/fgzc/gfxwj/gfxwj2023/202310/t20231008_188309.html`
  · `https://www.most.gov.cn/xxgk/xinxifenlei/fdzdgknr/fgzc/gfxwj/gfxwj2022/202209/t20220907_182313.html`
