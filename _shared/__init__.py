# -*- coding: utf-8 -*-
"""
_shared —— Light v2 技能包的跨技能地基契约层(机读交接地基)。

把"一句聊天 prose 交接"换成机器可读的结构化契约,让技能之间靠**结构化产物**交接,
而非聊天总结。批 0 第一块。七个契约:

    findings_schema   light.findings.v1  —— 统一 findings/gate 报告 + SARIF 导出
    gate_runner       gate 聚合执行器(总控确认点的接线处)
    semantic_sim      三档降级语义相似度(治"该用语义处全用词面 Jaccard")
    evidence_contract light.evidence_strength.v1 —— 证据强度→措辞档(中英双语)
    visual_qa         几何 + WCAG 对比度 + 渲染回看(治"视觉技能从不回看")
    status_contract   light.status.v1 —— 操作状态 + 覆盖缺口 + 结构化失败原因
    decision_contract light.decision.v1 —— 选项、风险、授权、范围与撤销状态

对外稳定接口(写技能脚本时按此 import 消费):

    # 推荐:健壮 bootstrap(向上走目录树找仓库根,治硬编码 parents[N] 之脆;
    # 三 harness + 全局/项目安装都可靠)。把下面 5 行放到消费脚本顶部:
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

依赖:纯 Python stdlib,无网络、无外部数据、无第三方包。三 harness 共用同一套。
"""
import pathlib

from .findings_schema import (
    Finding,
    GateResult,
    FindingsReport,
    validate,
    SCHEMA_ID,
    VALID_STATUS,
    VALID_VERDICT,
    VALID_SEVERITY,
)
from .gate_runner import run_gates, run_gates_to_json, GateFn
from .evidence_contract import (
    grade_evidence,
    grade_to_grade_level,
    allowed_verb_tier,
    lint_wording,
    build_evidence_json,
    GRADE_LEVEL,
)
from .semantic_sim import (
    similarity,
    most_similar,
    is_near_duplicate,
    set_embed_fn,
    set_llm_scorer,
)
from .visual_qa import (
    detect_geometry_issues,
    detect_contrast_issues,
    relative_luminance,
    contrast_ratio,
    check_contrast,
    visual_qa_rubric,
    qa_report,
)
from .status_contract import (
    StatusIssue,
    StatusRecord,
    validate as validate_status,
    SCHEMA_ID as STATUS_SCHEMA_ID,
    VALID_STATUS as VALID_OPERATION_STATUS,
)
from .decision_contract import (
    validate as validate_decision,
    SCHEMA_ID as DECISION_SCHEMA_ID,
)


def find_shared_root(start=None) -> pathlib.Path:
    """从 start(默认本文件)向上走目录树,返回**包含 _shared 包的目录**(即仓库根)。

    治 v1 硬编码 `parents[N]` 之脆:不依赖嵌套深度,三 harness + 全局/项目安装下,
    只要脚本在 Light-Skills 树内就能可靠定位 _shared。找不到抛 RuntimeError。
    """
    p = pathlib.Path(start or __file__).resolve()
    if p.is_file():
        p = p.parent
    while True:
        if (p / "_shared" / "__init__.py").exists():
            return p
        if p == p.parent:
            raise RuntimeError(
                "向上未找到 _shared 包目录(请确保消费脚本在 Light-Skills 树内)")
        p = p.parent


__all__ = [
    # findings 契约
    "Finding", "GateResult", "FindingsReport", "validate", "SCHEMA_ID",
    "VALID_STATUS", "VALID_VERDICT", "VALID_SEVERITY",
    "run_gates", "run_gates_to_json", "GateFn",
    # 证据强度契约
    "grade_evidence", "grade_to_grade_level", "allowed_verb_tier",
    "lint_wording", "build_evidence_json", "GRADE_LEVEL",
    # 语义相似度契约
    "similarity", "most_similar", "is_near_duplicate",
    "set_embed_fn", "set_llm_scorer",
    # 视觉 QA 契约
    "detect_geometry_issues", "detect_contrast_issues", "relative_luminance",
    "contrast_ratio", "check_contrast", "visual_qa_rubric", "qa_report",
    # 操作状态契约
    "StatusIssue", "StatusRecord", "validate_status", "STATUS_SCHEMA_ID",
    "VALID_OPERATION_STATUS",
    # 决策授权契约
    "validate_decision", "DECISION_SCHEMA_ID",
    # 健壮定位器
    "find_shared_root",
]

__schema_version__ = SCHEMA_ID  # "light.findings.v1"


# ──────────────────────────── selftest ────────────────────────────
def _selftest() -> int:
    import sys as _sys
    import shutil
    if hasattr(_sys.stdout, "reconfigure"):
        _sys.stdout.reconfigure(encoding="utf-8")
    ok = True

    def check(cond, msg):
        nonlocal ok
        if not cond:
            ok = False
        print(f"  [{'PASS' if cond else 'FAIL'}] {msg}")

    print("_shared/__init__ selftest")
    # 1. 全部对外符号都已导出且可用
    check(all(s in globals() for s in __all__), "__all__ 全部符号已导出")
    check(callable(run_gates) and callable(similarity)
          and callable(check_contrast) and callable(lint_wording)
          and callable(validate_status) and callable(validate_decision),
          "跨契约关键函数可调用")
    # 2. 契约间能协同(语义 + findings 同时可用)
    rep = FindingsReport(producer="orchestrator", target="t")
    rep.gates.append(GateResult("g", "pass", "info"))
    check(rep.finalize().verdict == "pass", "findings 报告可构造")
    status = StatusRecord("shared-smoke", "PASS", checked=["contract"])
    validate_status(status.to_dict())
    check(status.schema == STATUS_SCHEMA_ID, "状态契约可构造并校验")

    # 3. find_shared_root 从本文件定位到真实仓库根
    root = find_shared_root(__file__)
    check((root / "_shared" / "__init__.py").exists(), "定位到真实仓库根")

    # 4. find_shared_root 从合成的深层嵌套路径也能向上找到(治硬编码 parents[N])
    base = find_shared_root(__file__) / ".upgrade" / "_e2e" / "locate_test"
    try:
        fake_root = base / "fake_repo"
        deep = fake_root / "skills" / "some-skill" / "scripts" / "sub"
        deep.mkdir(parents=True, exist_ok=True)
        (fake_root / "_shared").mkdir(parents=True, exist_ok=True)
        (fake_root / "_shared" / "__init__.py").write_text("# marker", encoding="utf-8")
        found = find_shared_root(deep / "foo.py")
        check(found == fake_root.resolve(),
              "从 4 层嵌套脚本路径向上正确定位到 fake_repo 根")
    finally:
        if base.exists():
            shutil.rmtree(base, ignore_errors=True)

    # 5. 找不到时抛 RuntimeError(诚实失败,不静默)
    try:
        find_shared_root(pathlib.Path(base.anchor) / "no_such_dir_xyz" / "x.py")
        check(False, "无 _shared 时应抛 RuntimeError")
    except RuntimeError:
        check(True, "无 _shared 时抛 RuntimeError(诚实失败)")

    print("ALL PASS" if ok else "SOME FAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    import sys as _sys
    _sys.exit(_selftest())
