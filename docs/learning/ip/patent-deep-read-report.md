# Light IP Round2：专利交底方向逐篇深读报告

检查日期：2026-07-05。法律、审查指南、官方办事材料会变化；真实案件使用前必须重新核查官方来源。本报告只用于提升 Light 的“专利交底材料准备”能力，不构成法律意见。

## 总结结论

Light 的专利技能不能定位成“自动写专利/可直接提交”，而应定位成“把真实项目证据变成代理人可审阅的高密度交底包”。这轮学习后，最该吸收的不是某个模板，而是五个机制：

1. 发明人访谈先于写作：问题、失败替代方案、关键洞见、边界条件、公开披露、构思/完成时间、发明人贡献都必须单列。
2. 查新与发明人已知现有技术分离：前者是当日公开检索记录，后者是用户/团队已知事实；不能混在一起伪装成完整法律检索。
3. 权利要求阶梯：一个“最宽但可支撑”的核心点，加多个从属/备选落点，且每个要素回链到证据。
4. 说明书支撑与可实施性是硬门：没有实施例、变体、参数范围、失败模式和支持证据，就不得宣称可供代理人审阅。
5. QC 应模仿“技术审查员 + 代理人 + 怀疑者”三视角：查术语一致、支持映射、过宽要素、图源可审计、开放问题。

## 逐项深读

### 1. handsomestWei/patent-disclosure-skill

- 类型：同功能高星开源 skill。
- 来源：<https://github.com/handsomestWei/patent-disclosure-skill>
- 本地学习版本：`c4b843e2037376ce65a63f8db09b0cf635002b8f`
- GitHub 信号：2026-07-05 通过 GitHub API 核查约 3536 stars、MIT。
- 核心做法：按 intake、项目扫描、专利点挖掘、查新、交底书预览、定稿、自检、迭代合并拆成步骤；Step 5 对 CNIPA 检索词要求拆成 2–8 个语义块，且要求读取摘要后再概括；定稿用 Mermaid；迭代时另存新稿并留修订记录。
- Light 采用：专利点候选 3–5 个、查新检索词分解、摘要消化后再写、交底书不暴露内部工具名、迭代不覆盖旧稿。
- Light 不采用：Playwright/CNIPA 爬虫作为基线依赖、强制生成 docx、把“查新成功”暗示为专业新颖性意见。

### 2. trilogy-group/cc-skill-patent-disclosure

- 类型：同功能工程师到代理人交底 skill。
- 来源：<https://github.com/trilogy-group/cc-skill-patent-disclosure>
- 本地学习版本：`b109a13d295abed32296fb8fa3eed9c9038c9d10`
- GitHub 信号：2026-07-05 通过 GitHub API 核查约 13 stars；星数低但流程设计很强。
- 核心做法：先深度分析代码，列候选发明，再对单个发明做“新颖性深挖”；访谈工程师关于问题、试过的替代方案、关键洞见、边界条件、发明人、外部披露/销售、构思和实现时间；用 IDS JSON 中间结构分节生成；QC 采用技术价值、替代方案、公司价值、侵权可发现性四轴。
- Light 采用：发明人访谈清单、候选发明信心分级、IDS/packet 中间结构、QC 四轴中的技术价值/替代方案/可发现性思路。
- Light 不采用：beads 跨会话数据库、Google Docs 发布链路、把专利交底写成“可直接被律师最少往返地提交”的过强宣称。

### 3. RobThePCGuy/Claude-Patent-Creator

- 类型：专利创建/检索/审查工具包。
- 来源：<https://github.com/RobThePCGuy/Claude-Patent-Creator>
- 本地学习版本：`afee44612a468cb6a56e8cb650ad894dffac5c91`
- GitHub 信号：2026-07-05 通过 GitHub API 核查约 148 stars、MIT。
- 核心做法：把 MPEP/法规检索、BigQuery 专利检索、权利要求分析、说明书充分性、形式审查、Graphviz 图示拆成工具；权利要求分析强调 antecedent basis、definiteness、主观/相对词、过长/嵌套复杂度，但也明确正则检查会误报。
- Light 采用：权利要求“宽核心 + 从属 fallback”策略、术语一致/主观词/过宽要素自审、图示使用 Graphviz/Mermaid/SVG 的可审计源。
- Light 不采用：BigQuery/MCP/500MB 法规索引/GPU 作为公开技能包基线；不采用“USPTO-ready / filing-ready”措辞。

### 4. jaccen/AI-Copyright-Skill

- 类型：AI 项目 IP 材料相邻 skill。
- 来源：<https://github.com/jaccen/AI-Copyright-Skill>
- 本地学习版本：`20908b7943ff96983274c1646103f6c1d9e6a124`
- GitHub 信号：2026-07-05 通过 GitHub API 核查约 6 stars、MIT。
- 核心做法：对 AI/RAG/Agent/3D/生成式/具身/AI4Science 等项目给出专利权利要求展开方向，尤其强调“方法 + 系统 + 存储介质”三件套和从属权利要求递进。
- Light 采用：领域不内嵌，但保留“按技术类型选择 claim ladder”的方法；AI 项目作为 domain_scope 示例，不能污染通用技能。
- Light 不采用：把 AI 场景模板当作所有项目默认输出。

### 5. WIPO Patent Drafting Manual, 2nd edition, 2023

- 类型：官方/国际组织高可信写作手册。
- 来源：<https://www.wipo.int/publications/en/details.jsp?id=4706>
- 核心做法：强调发明公开、权利要求、说明书、实施例、变体和支持关系；发明交底表应收集发明人、商业意义、公开/销售日期、现有技术、实施方式。
- Light 采用：交底包必须包含变体、替代实施、限制、公开/销售日期和商业/技术背景，但商业价值只作为代理人理解上下文，不当作技术贡献。
- Light 不采用：不将 WIPO 手册中的正式撰写规则直接转成某一国家提交格式。

### 6. CNIPA《专利申请文件撰写》

- 类型：中国国家知识产权局培训/官方材料。
- 来源：<https://www.cnipa.gov.cn/2020-04/20200402105538938313.pdf>
- 核心做法：权利要求应编号、术语与说明书一致；权利要求可含公式但不能依赖附图表达；说明书需要支持权利要求。
- Light 采用：gate 增加术语一致、权利要求要素支持映射、附图只作为辅助而非 claim 必要要素的审查项。
- Light 不采用：不假装自动满足所有 CNIPA 正式格式。

### 7. CNIPA 说明书/附图培训材料

- 类型：中国官方培训材料。
- 来源：<https://www.cnipa.gov.cn/attach/0/820a120a48be4e9e911f74c0dcd2bb45.pdf>
- 核心做法：从公开内容转成申请文件时，要扩展实施例，借助检索确认区别特征；说明书公开不足会成为后续修改和授权障碍。
- Light 采用：交底必须写“支持实施例 + 备选实施例 + 失败/边界条件 + 参数范围”，否则不能走 READY_FOR_ATTORNEY_REVIEW。

### 8. CNIPA 权利要求/说明书支持材料

- 类型：中国官方培训材料。
- 来源：<https://www.cnipa.gov.cn/attach/0/c513e14f87634134a9ddd61a28d385eb.pdf>
- 核心做法：权利要求以说明书为依据；说明书对权利要求的概括必须有足够支持。
- Light 采用：每个 claim element 必须引用 source artifact；宽 claim 缺支持时降级为开放问题或 fallback。

### 9. USPTO MPEP 608

- 类型：美国专利局审查手册。
- 来源：<https://www.uspto.gov/web/offices/pac/mpep/s608.html>
- 核心做法：说明书、摘要、附图、权利要求的结构和形式要求均有细则；正式提交要求会随规则更新。
- Light 采用：美国路线仅做意识提醒，要求当日核查 MPEP/USPTO；交底包不声称正式性。

### 10. USPTO MPEP 2164 Enablement

- 类型：美国专利局审查手册。
- 来源：<https://www.uspto.gov/web/offices/pac/mpep/s2164.html>
- 核心做法：enablement 关注本领域技术人员是否能据公开内容实施发明，过度实验会成问题。
- Light 采用：gate 增加 `claim_strategy.enablement_support_summary`，要求列明支持实施方式。

### 11. USPTO MPEP 2163 Written Description

- 类型：美国专利局审查手册。
- 来源：<https://www.uspto.gov/web/offices/pac/mpep/s2163.html>
- 核心做法：written description 要求申请文本显示发明人在申请日拥有所主张发明。
- Light 采用：交底包强调证据时间线、构思/实现日期、支持源文件 SHA，不把聊天描述当证据。

### 12. EPO Guidelines：objective technical problem

- 类型：欧洲专利局官方指南。
- 来源：<https://www.epo.org/en/legal/guidelines-epc/2026/g_vii_5_2.html>
- 核心做法：问题-解决方案法中，实际客观技术问题可能要根据最接近现有技术和区别特征重新表述。
- Light 采用：把“技术问题”写成可被最近现有技术校准的版本；查新后必须回写 problem/difference。

### 13. EPI：Problem-solution approach case law

- 类型：欧洲专利律师协会文章。
- 来源：<https://information.patentepi.org/4-16/the-problem-and-solution-approach-basic-case-law-and-recent-development-%28ii%29/>
- 核心做法：问题-解决方案法要求围绕最接近现有技术、区别特征和客观技术问题组织创造性分析。
- Light 采用：差异表不是“我们更好”，而是“D1 缺少的技术特征 + 产生的技术效果 + 技术启示缺口”。

### 14. Saul Ewing：Best Practices for Drafting Invention Disclosure Forms

- 类型：律师事务所实务文章。
- 来源：<https://www.saul.com/insights/article/best-practices-drafting-invention-disclosure-forms>
- 核心做法：高质量交底表应鼓励发明人说明问题、技术方案、替代方案、公开事件、商业重要性和联系人；表格过长会降低填写质量。
- Light 采用：访谈清单要短而尖锐；缺项以 NEEDS_USER_INPUT 记录，不用长问卷淹没用户。

### 15. Mintz：EPO AI/ML patent strategies

- 类型：律师事务所/实务文章。
- 来源：<https://www.mintz.com/insights-center/viewpoints/2231/2019-01-17-key-strategies-obtaining-patents-under-epos-new-ai>
- 核心做法：AI/ML 发明在 EPO 下要强调技术目的、技术效果、训练/推理管线与具体约束，避免只写抽象算法。
- Light 采用：对软件/AI 发明，必须把业务效果翻译成技术效果，如延迟、吞吐、准确率、资源、鲁棒性、可观测输出。

### 16. Harness IP：Enablement guidance

- 类型：实务文章。
- 来源：<https://www.harnessip.com/blog/2024/01/22/uspto-guidelines/>
- 核心做法：强调充分公开、可实施性、样例和参数范围对抗 enablement 风险。
- Light 采用：要求实施例和参数范围不能只放“可选”；必须绑定到证据或标为待补。

## 对 Light 的具体升级要求

1. 新增 `references/patent-interview-and-search.md`，把访谈、查新、claim ladder、QC 变成可加载规则。
2. `disclosure_gate.py` 新增硬校验：风险三联/四联、发明人已知现有技术、检索覆盖、权利要求阶梯、QC 布尔门。
3. 模板新增对应字段；示例不能使用 0 哈希代表真实通过，只做结构示例。
4. `SKILL.md` 收紧表述：只输出 `DRAFT`、`NEEDS_USER_INPUT`、`READY_FOR_ATTORNEY_REVIEW`。
5. 保留“官方/公开源当日核查”要求，避免法律规则过期。
