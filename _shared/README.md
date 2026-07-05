# `_shared` —— Light v2 跨技能地基契约层

机读交接地基:技能之间靠**结构化产物**(findings/gate、语义相似度、证据强度、视觉回看)
交接,而非聊天总结。这是批 0 第一块,后续 21 个技能的挂靠面。

来源:评估搬运 v1(`../../Light/skills/_shared/`,已 selftest 验证)+ 按 v2 架构调整。
七个契约纯 Python stdlib,三 harness(Claude Code / Codex / OpenCode)共用同一套。

## 五个契约

| 文件 | schema / 角色 | 一句话 |
|------|------|------|
| `findings_schema.py` | `light.findings.v1` | Finding/GateResult/FindingsReport 三数据类 + JSON 往返 + 校验 + **SARIF 导出** |
| `gate_runner.py` | gate 聚合执行器 | 多 gate → 一份报告;异常转 critical fail 不静默;**总控确认点的接线处** |
| `semantic_sim.py` | 三档降级语义相似度 | embedding/LLM/离线;离线档纯 stdlib,正确处理倒装,诚实标语义边界 |
| `evidence_contract.py` | `light.evidence_strength.v1` | q/效应量/CI → 措辞档(**中英双语**),对齐 GRADE 词表 |
| `visual_qa.py` | `light.visual_qa.v1` | 几何检测 + **WCAG 对比度门** + 渲染回看协议;诚实标 pixel_review_done |
| `status_contract.py` | `light.status.v1` | PASS/WARN/FAIL/ERROR/UNAVAILABLE/PARTIAL/UNRESOLVED/SKIPPED + 未覆盖范围与结构化问题 |
| `decision_contract.py` | `light.decision.v1` | 选项/风险/可逆性/授权主体/scope；高风险或不可逆动作强制用户授权 |
| `__init__.py` / `__main__.py` | 包入口 | 对外稳定 import 面 + **健壮 `_shared` 定位器** `find_shared_root` |

## 消费方怎么 import(规范 bootstrap)

把下面 5 行放到技能脚本顶部(向上走目录树找仓库根,治硬编码 `parents[N]` 之脆,
三 harness + 全局/项目安装、任意嵌套深度都可靠):

```python
import sys, pathlib
_r = pathlib.Path(__file__).resolve()
while _r != _r.parent and not (_r / "_shared" / "__init__.py").exists():
    _r = _r.parent
sys.path.insert(0, str(_r))
from _shared.findings_schema import FindingsReport, GateResult, Finding
from _shared.gate_runner import run_gates
from _shared.evidence_contract import grade_evidence, lint_wording
from _shared.semantic_sim import similarity, is_near_duplicate
from _shared.visual_qa import detect_geometry_issues, check_contrast, qa_report
from _shared.status_contract import StatusIssue, StatusRecord
from _shared.decision_contract import validate as validate_decision
```

机读交接约定:产出方填 `producer`(技能名)/`target`(被检工件)/`fresh_evidence`;
消费方只读 `verdict` 做判定、读 `gates[].findings[]` 做定位修正,不解析 prose;
跨进程/跨会话一律走 `to_json()` / `from_json()`,不传 Python 对象。

## 增量边界(名实对齐:哪些是真增量,哪些是裸模型/v1 既有)

**裸模型本就会的(不吹成卖点)**:写一句"措辞别太强""注意对比度""标题别撞车"这类
建议,裸 Opus 本就会。本层的价值**不是知道这些,而是把它们落成可机检、可阻断、
可跨技能复用的确定性门**(脚本兑现,而非 SKILL 里喊口号)。

**v2 对 v1 的真增量(本轮新增,已 selftest + e2e 实测)**:
1. **健壮 `_shared` 定位器**:向上走目录树,治 v1 硬编码 `parents[N]` 在三 harness/全局
   安装下必断的脆(e2e 实测 4 层嵌套通过)。
2. **findings → SARIF 导出器**:与 GitHub code scanning 等外部工具互通,v1 完全没碰。
3. **证据契约中英双语**:v1 仅英文动词档;v2 加中文断言/hedge + 否定守卫(治"无显著
   差异"假阳性),覆盖中文论文场景。四档对齐 GRADE 词表。
4. **WCAG 对比度门**:v1 把对比度全甩给 VLM;v2 确定性算对比度、分两档卡 AA,不渲染
   就能抓最高频可读性 fail。
5. 修了 v1 semantic_sim 一处 ZeroDivisionError 隐患(全停用词输入)。

**沿用 v1(已验证,近乎原样搬,非本轮原创)**:findings/gate 三数据类与聚合逻辑、
语义离线档混合算法、证据分档规则、几何检测器、渲染回看协议。

## 诚实落后项(已知没做到的)

- **证据分档只吃统计强度**:未实现 GRADE 另四域(偏倚/不一致/间接/发表偏倚)系统降级,
  留给 result-analysis 做域降级。不假装 full GRADE。
- **语义离线档做不了纯同义**:无共词的同义词(running shoes↔athletic footwear)必须注入
  embedding 档;离线档诚实标注此边界,不假装能做。
- **WCAG 对比度需颜色输入**:对已是位图、无法取色的外部图,对比度门不适用,只能走 VLM。
- **几何检测需 AABB 坐标**:扫描图/外部 PNG 无 AABB 时几何门不适用。
- **显式推迟(非本层职责)**:① 在线免 key 取数 helper(OpenAlex/arXiv/Crossref)→ 留给
  首个消费者 literature-search(批 1),批 0 无模块需要它;② 项目台账 schema(项目卡/决策
  日志/版本史)→ 归 memory-pm/orchestrator(批 0 后续),不在本层。

## 自测(每个都亲手 run 到 exit 0)

```bash
set PYTHONUTF8=1
python _shared/findings_schema.py   --selftest   # 10 组断言(含 SARIF 导出)
python _shared/gate_runner.py       --selftest   # 7 组断言(含异常捕获)
python _shared/semantic_sim.py      --selftest   # 倒装/中文/档位切换
python _shared/evidence_contract.py --selftest   # 双语 + 否定守卫 + GRADE 映射
python _shared/visual_qa.py         --selftest   # 几何 + WCAG 对比度两档
python _shared/status_contract.py   --selftest   # 状态枚举 + 覆盖缺口 + 非静默失败
python _shared/decision_contract.py --selftest   # 用户/自动权限 + scope + 拒绝/撤销
python -m _shared                                 # 包级:定位器(含 4 层嵌套合成测试)
```

> `__init__.py` 用相对 import,需包上下文,故包级 selftest 走 `python -m _shared`
> (而非 `python _shared/__init__.py`)。

## 依赖降级矩阵

| 依赖项 | 要求 | 缺失/降级时行为 |
|--------|------|----------------|
| Python | 3.10+（使用 `X | None` 类型语法） | 实测 3.11+ 全绿 |
| 第三方包 | 无 | 仅 stdlib;embedding/LLM 档为可选注入,缺则降级离线档 |
| 网络 | 不需要 | 纯本地,无网络调用 |
| gate 抛异常 | —— | 不中断:转记 critical fail + traceback,整体 verdict=fail |
| 无渲染器(视觉) | —— | 仅几何+对比度检测,标 `pixel_review_done=False`,不假装做了回看 |
| stdout 非 UTF-8(Win 控制台) | —— | 脚本顶部 `reconfigure(encoding="utf-8")`,中文不乱码 |

competitors 笔记见 `../docs/competitors/_shared.md`。
