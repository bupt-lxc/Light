# Light IP Round2：软著方向逐篇深读报告

检查日期：2026-07-05。软著登记系统、表单、材料要求和地方初审口径可能变化；真实申请前必须重新核查官方页面。本报告只用于提升 Light 的“中国软件著作权材料准备”能力，不构成法律意见，不保证登记结果。

## 总结结论

软著技能的顶级能力不是“自动生成一套漂亮 Word”，而是“从真实项目中提取可追溯、名称版本一致、无密钥泄露、经用户确认的登记材料草稿”。这轮学习后，Light 需要把三类事情变成硬门：

1. 源代码选择计划：先列候选源码、行数、哈希、密钥风险、选择理由，再确认；不能直接抽全库，也不能补假代码。
2. 业务理解门：申请表和操作手册必须来自真实 README/页面/路由/API/产品文档，手册面向普通用户，不写研发说明书。
3. 权属与第三方代码审查：独立/委托/合作/继受、开源依赖、第三方素材、预训练模型或生成代码都要记录，不可默认为“全部原创”。

## 逐项深读

### 1. Fokkyp/SoftwareCopyright-Skill

- 类型：同功能高星开源 skill。
- 来源：<https://github.com/Fokkyp/SoftwareCopyright-Skill>
- 本地学习版本：`0a27d1143eca253b7b7e953794a24ef6e5488b0d`
- GitHub 信号：2026-07-05 通过 GitHub API 核查约 4185 stars、MIT。
- 核心做法：固定输出目录 `软件著作权申请资料/`；先 Markdown 草稿，确认后正式 Word/TXT；正式资料只放 `正式资料/`；必须先形成业务理解；候选代码清单由脚本收集，模型填写选择理由，用户确认；操作手册需真实、段落化、去模板味；截图方式必须询问；硬件/系统环境需用户确认。
- Light 采用：源代码候选清单、业务理解先行、代码选择确认、正式输出目录约束、手册反 AI 套话、截图方式门。
- Light 不采用：内置 docx-toolkit 大包作为 Light 基线；不采用“必须停等用户”的所有交互强制，因为 Light 还有批处理场景，但材料正式化前必须有确认记录。

### 2. na57/chinese-copyright-application-skill

- 类型：中国软著材料生成 skill。
- 来源：<https://github.com/na57/chinese-copyright-application-skill>
- 本地学习版本：`04081d07d052e929dc0f3b768c046e49cee03c32`
- GitHub 信号：2026-07-05 通过 GitHub API 核查约 151 stars。
- 核心做法：申请表、设计文档、用户手册、源代码文档模板较完整；字段覆盖较直接。
- Light 采用：作为字段清单和普通用户文档骨架参考。
- Light 不采用：模板化生成、弱证据绑定、可能诱导“凑材料”的写法。

### 3. jaccen/AI-Copyright-Skill：AI 软著指南

- 类型：AI 项目软著相邻 skill。
- 来源：<https://github.com/jaccen/AI-Copyright-Skill>
- 本地学习版本：`20908b7943ff96983274c1646103f6c1d9e6a124`
- GitHub 信号：2026-07-05 通过 GitHub API 核查约 6 stars。
- 核心做法：对 AI 服务、训练、推理、3D、生成式、Agent、RAG、AI4Science 等项目给出源码优先级和手册侧重点；提醒开源代码、模型权重、知识库版权、隐私数据。
- Light 采用：作为 `domain_scope` 参考思路，尤其是“第三方模型/开源依赖/知识库内容不属于软件表达本身”的边界意识。
- Light 不采用：不把 AI 项目作为默认场景；不采纳“2026 审查指南”类未核查强宣称。

### 4. 国家版权局《计算机软件著作权登记办法》

- 类型：官方部门规章。
- 来源：<https://www.ncac.gov.cn/xxfb/flfg/bmgz/202410/t20241015_869486.html>
- 核心做法：登记申请材料包括申请表、软件鉴别材料及相关证明文件；程序和文档鉴别材料通常为前后各连续 30 页，不足 60 页提交全部；程序每页不少于 50 行、文档每页不少于 30 行。
- Light 采用：gate 强制检查页数模式、50/30 行规则、材料类型和异常说明。

### 5. 国家版权局 DOCX 版本

- 类型：官方可下载文件。
- 来源：<https://www.ncac.gov.cn/xxfb/flfg/bmgz/202410/P020241015604759474834.docx>
- 核心做法：与网页版本配套，便于真实办理时核对条款文本。
- Light 采用：资源图中保留为下载核对点；不直接把 docx 内容复制进 skill。

### 6. 北京市政务服务：计算机软件著作权登记初审

- 类型：地方政务服务指南。
- 来源：<https://banshi.beijing.gov.cn/pubtask/task/1/110000000000/3e283672-76be-4c8c-98e8-0bebe9bd06bf.html?locationCode=110000000000>
- 核心做法：整合材料、申请表、鉴别材料、证明文件、签章/一致性提醒；适合做当日办理口径核查。
- Light 采用：真实项目应以官方服务指南确认当日表单/附件/签章要求；Light 只准备本地材料，不提交。

### 7. 《计算机软件保护条例》

- 类型：官方法规。
- 来源：<https://xzfg.moj.gov.cn/front/law/detail?LawID=914>
- 核心做法：软件著作权保护软件表达，不保护开发思想、处理过程、操作方法、数学概念等；登记证书通常作为初步证明。
- Light 采用：技能明确“不保护算法思想本身”；手册和源码材料应围绕软件表达、功能界面、运行流程，不把 idea 包装成软著。

### 8. WIPO Lex：计算机软件著作权登记办法

- 类型：国际知识产权组织法规镜像。
- 来源：<https://www.wipo.int/wipolex/zh/text/199387>
- 核心做法：提供稳定法规检索入口，便于国际用户理解中国规则。
- Light 采用：作为辅助核查来源；优先级低于国家版权局/政务服务当日页面。

### 9. 上海软协服务指南

- 类型：服务机构/地方行业服务页面。
- 来源：<https://services.softline.org.cn/RX/home/template?code=RJZZQNew>
- 核心做法：材料准备实务化，常提醒命名、页眉、版本、申请表一致。
- Light 采用：作为实务提醒来源，不能高于官方规则。

### 10. 天津交通职业学院科研处软著指南

- 类型：高校办理说明。
- 来源：<https://kyc.tjtc.edu.cn/info/1036/1088.htm>
- 核心做法：高校内部办理通常强调申请表、源代码、说明书、权属/证明材料。
- Light 采用：提醒不同单位可能有内部流程；Light 应让用户记录单位/委托/合作证明，不假定所有权属简单。

### 11. AlexanderZhou01/China-software-copyright

- 类型：实务模板仓库。
- 来源：<https://github.com/AlexanderZhou01/China-software-copyright>
- 核心做法：提供材料样式和实操经验，强调名称版本一致、代码页数、手册结构。
- Light 采用：一致性和格式提醒。
- Light 不采用：任何“水代码/凑行数/注释填充”思路；这与 Light 的真实源代码原则冲突。

### 12. Zhihu 软著材料文章

- 类型：社区经验文章。
- 来源：<https://zhuanlan.zhihu.com/p/387185182>
- 核心做法：对代码页数、手册、截图、申请表字段有实践解释。
- Light 采用：作为“用户常见误区”参考，不能作为规则依据。

### 13. U.S. Copyright Office Circular 61

- 类型：美国版权局官方 circular。
- 来源：<https://www.copyright.gov/circs/circ61.pdf>
- 核心做法：美国计算机程序登记 deposit 规则和中国不同。
- Light 采用：`jurisdiction` 必须明确；CN 规则不得默默套到 US/EU。

### 14. Fokkyp `propose_code_selection.py`

- 类型：参考 skill 中的脚本。
- 本地路径：`.upgrade/_e2e/ip-round2/SoftwareCopyright-Skill/software-copyright-materials/scripts/propose_code_selection.py`
- 核心做法：脚本只列候选文件，不自动决定；候选包含行数、材料行数、优先级和证据类型；模型填写 `selected/model_reason`，用户确认后抽取。
- Light 采用：实现轻量版 `source_deposit_plan.py`，输出候选、行数、哈希、页数估计、密钥风险和下一步确认。

### 15. Fokkyp `extract_code_material.py`

- 类型：参考 skill 中的脚本。
- 本地路径：`.upgrade/_e2e/ip-round2/SoftwareCopyright-Skill/software-copyright-materials/scripts/extract_code_material.py`
- 核心做法：按确认的选择文件抽取完整文件，去除纯空行，按 50 行分页；不足 60 页时若候选足够补齐则停止让用户补选；否则全量。
- Light 采用：页数模式由真实源代码行数决定；严禁中间任意截取和伪造代码。

## 对 Light 的具体升级要求

1. 新增 `scripts/source_deposit_plan.py`：轻量扫描真实源码、哈希、行数、页数模式、秘密命中、候选文件和确认下一步。
2. `materials_gate.py` 新增硬门：`source_plan` 确认、`rights_basis`、`third_party_code_review`、`code_material.source_plan_sha256`。
3. 新增 `references/materials-workflow.md`：把业务理解、源代码选择、权属/第三方、截图和正式输出拆清楚。
4. `SKILL.md` 明确：不提交、不保证登记、不造代码、不默认 CN 以外规则、不把思想/算法当软著保护对象。
