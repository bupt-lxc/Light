# Light IP Round2：专利与软著最终升级汇总

检查日期：2026-07-05。本汇总将专利和软著两份深读报告转成 Light 技能升级清单。

## 产品定位

新增的 IP 技能是科研/工程项目的“成果转化材料准备”能力，不进入 Light 科研主 DAG，不写 `light.findings.v1`，不接九库，不调用 MCP/私有知识库。它们只帮助用户把真实项目证据整理成可交给律师、代理机构、单位科研管理或专业服务方审阅的本地材料草稿。

## 三条共同红线

1. 不提供法律意见、不提交、不承诺授权/登记/下证。
2. 不伪造事实：无真实源代码、无公开检索、无权属确认、无发明人确认时，写 `UNKNOWN/PLANNED/NEEDS_USER_INPUT`。
3. 所有正式材料都必须有证据链：相对路径、SHA-256、日期、用户确认依据、开放问题。

## 专利技能吸收点

| 来源 | 吸收机制 | 落地位置 |
|---|---|---|
| handsomestWei/patent-disclosure-skill | 查新语义块、摘要消化、迭代不覆盖 | `patent-interview-and-search.md`、`SKILL.md` |
| cc-skill-patent-disclosure | 工程师访谈、IDS 中间结构、QC rubric | `patent-disclosure-packet.example.json`、`disclosure_gate.py` |
| Claude-Patent-Creator | claim ladder、112 支撑/明确性、图源可审计 | `disclosure_gate.py`、`patent-interview-and-search.md` |
| WIPO/CNIPA/USPTO/EPO | 说明书支持、可实施性、问题-解决方案 | `SKILL.md`、`disclosure_gate.py` |

专利技能最终应能回答：

- 这个发明到底解决什么技术问题？
- 哪个技术特征是新贡献，不是业务愿望？
- 每个特征由哪个真实 artifact 支撑？
- 最近的公开技术是什么，检索覆盖多深，缺什么？
- 最宽 claim 和 fallback claim 分别靠什么实施例支撑？
- 律师/代理人还必须问哪些问题？

## 软著技能吸收点

| 来源 | 吸收机制 | 落地位置 |
|---|---|---|
| Fokkyp/SoftwareCopyright-Skill | 业务理解、候选源码、确认门、手册去模板味 | `materials-workflow.md`、`source_deposit_plan.py` |
| 国家版权局/政务服务 | 前后 30 页、不足 60 页全交、50/30 行规则 | `materials_gate.py` |
| 软件保护条例 | 保护表达不保护思想/算法 | `SKILL.md` |
| AI-Copyright-Skill | AI/Agent/RAG/AI4Science 的 domain_scope 边界 | `materials-workflow.md` |

软著技能最终应能回答：

- 软件名称、版本、申请主体和开发方式是否一致且确认？
- 源码材料是否来自真实项目，是否无密钥/隐私/无关第三方代码？
- 为什么选择这些代码文件？全量/前后 30 页模式由哪些行数决定？
- 操作手册是否像真实用户手册，而不是研发说明或 AI 套话？
- 权属、第三方依赖、开源许可证、委托/合作/继受事实是否留下开放问题？

## 这轮必须改的文件

### 专利

- `skills/light-patent-disclosure/SKILL.md`
- `skills/light-patent-disclosure/references/patent-resource-map.md`
- `skills/light-patent-disclosure/references/patent-interview-and-search.md`
- `skills/light-patent-disclosure/templates/patent-disclosure-packet.example.json`
- `skills/light-patent-disclosure/scripts/disclosure_gate.py`

### 软著

- `skills/light-software-copyright/SKILL.md`
- `skills/light-software-copyright/references/software-copyright-resource-map.md`
- `skills/light-software-copyright/references/materials-workflow.md`
- `skills/light-software-copyright/templates/software-copyright-materials.example.json`
- `skills/light-software-copyright/scripts/materials_gate.py`
- `skills/light-software-copyright/scripts/source_deposit_plan.py`

## 自测口径

1. `python skills/light-patent-disclosure/scripts/disclosure_gate.py --selftest` 必须 exit 0。
2. `python skills/light-software-copyright/scripts/source_deposit_plan.py --selftest` 必须 exit 0。
3. `python skills/light-software-copyright/scripts/materials_gate.py --selftest` 必须 exit 0。
4. 如果仓库有技能 validator，应对两个技能跑一遍；没有则至少检查 YAML frontmatter、无额外私密内容、无 MCP/九库依赖。
