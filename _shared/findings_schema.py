#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
findings_schema.py —— 跨技能交接的机读 findings 契约 (Light v2 / _shared 地基契约 1)

把"一句聊天总结"式的 prose 交接,换成机器可读的结构化契约 `light.findings.v1`。
技能之间靠**结构化产物**交接(总控守门 / 证据-措辞门 / draft-lint / 引用支撑 /
审稿意见分类 / memory-pm 台账),不再靠自然语言传 verdict。

提供三个数据类 + JSON 序列化/反序列化/校验 + SARIF 导出:
  Finding        单条发现(定位 loc / 问题 issue / 修正 fix / 可选证据 / 触发规则)
  GateResult     单个 gate 的结果(gate 名 / status / severity / findings 列表)
  FindingsReport 一次交接的完整报告(producer/target/verdict/gates/summary)

schema 形如:
  {"schema":"light.findings.v1","producer":"paper-writing","target":"draft.md",
   "verdict":"pass|fail|warn","gates":[
     {"gate":"evidence_wording","status":"fail","severity":"critical",
      "findings":[{"loc":"draft.md:42","issue":"...","fix":"..."}]}],
   "summary":"...","fresh_evidence":true}

为什么不直接用 SARIF(对标 OASIS SARIF 2.1.0 后的取舍,见 docs/competitors/_shared.md):
  SARIF 是业界机读 findings 的事实标准,但为安全工具互操作设计、字段繁重。本契约
  是**技能内交接**用,刻意精简(token 经济 + 作者好写),但字段语义有意识对齐 SARIF
  (loc≈location / rule≈ruleId / severity≈level / fix≈fix),并提供 to_sarif() 在需要
  与外部工具(GitHub code scanning 等)互通时无损导出。不重造标准,也不被它的繁文淹没。

用法:
  python findings_schema.py --selftest        # 合成数据自测, 退出码 0/1
  python findings_schema.py --validate FILE    # 校验一份外部 findings JSON
  消费方 import: from findings_schema import Finding, GateResult, FindingsReport

依赖:纯 Python stdlib。无网络、无外部数据、无第三方包。
"""
import argparse
import json
import sys
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

SCHEMA_ID = "light.findings.v1"

# 受控取值
VALID_STATUS = ("pass", "fail", "warn", "skip")      # 单 gate 状态
VALID_VERDICT = ("pass", "fail", "warn")             # 整体裁定
VALID_SEVERITY = ("critical", "major", "minor", "info")

# severity 排序(数字越大越严重),用于聚合时取最严重
_SEV_RANK = {"info": 0, "minor": 1, "major": 2, "critical": 3}

# Light severity → SARIF level(导出用;有损映射,故 to_sarif 同时把原值放进 properties)
_SEV_TO_SARIF = {"critical": "error", "major": "error",
                 "minor": "warning", "info": "note"}


@dataclass
class Finding:
    """单条发现:定位 + 问题 + 修正建议(+可选证据/规则名)。"""
    loc: str                       # 形如 "draft.md:42" 或 "fig3" 或 "claim:c1"
    issue: str                     # 问题描述
    fix: str = ""                  # 建议修正
    evidence: Optional[str] = None # 可选:支撑该发现的证据/原文片段(SciFact 式 rationale)
    rule: Optional[str] = None     # 可选:触发的规则/启发式名(诚实留痕,≈SARIF ruleId)

    def to_dict(self) -> Dict[str, Any]:
        d = {"loc": self.loc, "issue": self.issue, "fix": self.fix}
        if self.evidence is not None:
            d["evidence"] = self.evidence
        if self.rule is not None:
            d["rule"] = self.rule
        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "Finding":
        if "loc" not in d or "issue" not in d:
            raise ValueError("Finding 必须含 loc 与 issue 字段")
        return Finding(
            loc=str(d["loc"]),
            issue=str(d["issue"]),
            fix=str(d.get("fix", "")),
            evidence=d.get("evidence"),
            rule=d.get("rule"),
        )


@dataclass
class GateResult:
    """单个 gate 的结果。status=fail 且 severity=critical 时会拉整体 verdict 为 fail。"""
    gate: str
    status: str = "pass"
    severity: str = "info"
    findings: List[Finding] = field(default_factory=list)
    note: str = ""                 # gate 的可选说明(如降级标注)

    def __post_init__(self):
        if self.status not in VALID_STATUS:
            raise ValueError(f"非法 status={self.status!r},应属 {VALID_STATUS}")
        if self.severity not in VALID_SEVERITY:
            raise ValueError(f"非法 severity={self.severity!r},应属 {VALID_SEVERITY}")

    def is_blocking(self) -> bool:
        """是否构成阻断(critical 级别的 fail)。"""
        return self.status == "fail" and self.severity == "critical"

    def to_dict(self) -> Dict[str, Any]:
        d = {
            "gate": self.gate,
            "status": self.status,
            "severity": self.severity,
            "findings": [f.to_dict() for f in self.findings],
        }
        if self.note:
            d["note"] = self.note
        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "GateResult":
        if "gate" not in d:
            raise ValueError("GateResult 必须含 gate 字段")
        return GateResult(
            gate=str(d["gate"]),
            status=str(d.get("status", "pass")),
            severity=str(d.get("severity", "info")),
            findings=[Finding.from_dict(x) for x in d.get("findings", [])],
            note=str(d.get("note", "")),
        )


@dataclass
class FindingsReport:
    """一次跨技能交接的完整 findings 报告。"""
    producer: str                          # 产出技能名(如 orchestrator/paper-writing)
    target: str                            # 被检查工件(如 draft.md)
    gates: List[GateResult] = field(default_factory=list)
    verdict: Optional[str] = None          # None 时由 compute_verdict 推导
    summary: str = ""
    fresh_evidence: bool = False           # 证据是否为本轮新算(防陈旧证据复用)
    schema: str = SCHEMA_ID

    def compute_verdict(self) -> str:
        """由 gates 推导整体裁定:
        任一 critical fail -> fail;否则有任意 fail/warn -> warn;全 pass/skip -> pass。"""
        if any(g.is_blocking() for g in self.gates):
            return "fail"
        if any(g.status in ("fail", "warn") for g in self.gates):
            return "warn"
        return "pass"

    def worst_severity(self) -> str:
        """所有非 pass gate 中的最严重 severity(无问题返回 info)。"""
        sevs = [g.severity for g in self.gates if g.status in ("fail", "warn")]
        if not sevs:
            return "info"
        return max(sevs, key=lambda s: _SEV_RANK[s])

    def blocking_gates(self) -> List["GateResult"]:
        """返回构成阻断的 gate 列表(供总控定位回炉根因)。"""
        return [g for g in self.gates if g.is_blocking()]

    def finalize(self) -> "FindingsReport":
        """把 verdict 落定为推导值(若未显式给定)。返回自身便于链式。"""
        if self.verdict is None:
            self.verdict = self.compute_verdict()
        return self

    def to_dict(self) -> Dict[str, Any]:
        v = self.verdict if self.verdict is not None else self.compute_verdict()
        return {
            "schema": self.schema,
            "producer": self.producer,
            "target": self.target,
            "verdict": v,
            "gates": [g.to_dict() for g in self.gates],
            "summary": self.summary,
            "fresh_evidence": self.fresh_evidence,
        }

    def to_json(self, indent: int = 2) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=indent)

    def to_sarif(self) -> Dict[str, Any]:
        """无损导出为 SARIF 2.1.0(OASIS 标准),供与外部工具互通。

        映射: producer→tool.driver.name; 每条 Finding→一个 result;
        rule||gate→ruleId; severity→level(error/warning/note);
        loc("file:line")→physicalLocation; fix→fixes; 原 Light 字段进 properties 不丢。
        """
        rules: Dict[str, Dict[str, Any]] = {}
        results: List[Dict[str, Any]] = []
        for g in self.gates:
            for f in g.findings:
                rule_id = f.rule or g.gate
                rules.setdefault(rule_id, {"id": rule_id})
                # 解析 "file:line" → uri + startLine(无法解析则只放 uri)
                uri, start_line = f.loc, None
                if ":" in f.loc:
                    head, _, tail = f.loc.rpartition(":")
                    if head and tail.isdigit():
                        uri, start_line = head, int(tail)
                region = {"startLine": start_line} if start_line else {}
                phys = {"artifactLocation": {"uri": uri}}
                if region:
                    phys["region"] = region
                res: Dict[str, Any] = {
                    "ruleId": rule_id,
                    "level": _SEV_TO_SARIF.get(g.severity, "note"),
                    "message": {"text": f.issue},
                    "locations": [{"physicalLocation": phys}],
                    "properties": {"gate": g.gate, "light_severity": g.severity,
                                   "status": g.status},
                }
                if f.fix:
                    res["fixes"] = [{"description": {"text": f.fix}}]
                if f.evidence:
                    res["properties"]["evidence"] = f.evidence
                results.append(res)
        return {
            "version": "2.1.0",
            "$schema": "https://json.schemastore.org/sarif-2.1.0.json",
            "runs": [{
                "tool": {"driver": {"name": self.producer or "light",
                                    "rules": list(rules.values())}},
                "results": results,
                "properties": {"light_schema": self.schema,
                               "verdict": self.verdict or self.compute_verdict(),
                               "target": self.target},
            }],
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "FindingsReport":
        validate(d)
        return FindingsReport(
            producer=str(d["producer"]),
            target=str(d["target"]),
            gates=[GateResult.from_dict(x) for x in d.get("gates", [])],
            verdict=d.get("verdict"),
            summary=str(d.get("summary", "")),
            fresh_evidence=bool(d.get("fresh_evidence", False)),
            schema=str(d.get("schema", SCHEMA_ID)),
        )

    @staticmethod
    def from_json(s: str) -> "FindingsReport":
        return FindingsReport.from_dict(json.loads(s))


def validate(d: Dict[str, Any]) -> List[str]:
    """校验一个 dict 是否合法 findings 报告。返回 [] 表示合法;
    schema 不符或缺关键字段直接抛 ValueError(硬错),非法 status/severity 也抛。"""
    if not isinstance(d, dict):
        raise ValueError("findings 报告必须是 JSON 对象")
    if d.get("schema") != SCHEMA_ID:
        raise ValueError(f"schema 必须为 {SCHEMA_ID},实得 {d.get('schema')!r}")
    for req in ("producer", "target"):
        if req not in d:
            raise ValueError(f"缺必填字段 {req}")
    errs: List[str] = []
    v = d.get("verdict")
    if v is not None and v not in VALID_VERDICT:
        errs.append(f"verdict={v!r} 非法")
    for g in d.get("gates", []):
        if g.get("status") not in VALID_STATUS:
            errs.append(f"gate {g.get('gate')!r} status 非法: {g.get('status')!r}")
        if g.get("severity") not in VALID_SEVERITY:
            errs.append(f"gate {g.get('gate')!r} severity 非法: {g.get('severity')!r}")
    if errs:
        raise ValueError("; ".join(errs))
    return errs


# ---------------------------------------------------------------- selftest
def _selftest() -> int:
    failures = []

    def check(cond, msg):
        if not cond:
            failures.append(msg)

    # 1. 基本构造 + verdict 推导
    r = FindingsReport(producer="idea-critique", target="draft.md")
    r.gates.append(GateResult("evidence_wording", "pass", "info"))
    check(r.compute_verdict() == "pass", "全 pass 应推导 pass")

    # 2. critical fail -> 整体 fail
    r.gates.append(GateResult(
        "claim_support", "fail", "critical",
        [Finding("draft.md:42", "断言无证据支撑", "降级措辞或补引用", rule="evidence")]))
    check(r.compute_verdict() == "fail", "critical fail 应推导 fail")
    check(r.worst_severity() == "critical", "worst_severity 应为 critical")
    check(len(r.blocking_gates()) == 1, "blocking_gates 应返回 1 个阻断 gate")

    # 3. 仅 warn / 非 critical fail -> warn
    r2 = FindingsReport(producer="paper-writing", target="sec.md")
    r2.gates.append(GateResult("style", "warn", "minor",
                               [Finding("sec.md:3", "措辞偏口语", "改正式表达")]))
    r2.gates.append(GateResult("ref", "fail", "major",
                               [Finding("sec.md:9", "引用格式错", "改 BibTeX")]))
    check(r2.compute_verdict() == "warn", "无 critical 时应推导 warn")
    check(r2.worst_severity() == "major", "worst_severity 应取最严重 major")

    # 4. JSON 往返(序列化->反序列化)保真
    js = r.finalize().to_json()
    r_back = FindingsReport.from_json(js)
    check(r_back.producer == "idea-critique", "往返后 producer 应保真")
    check(r_back.verdict == "fail", "往返后 verdict 应保真")
    check(len(r_back.gates) == 2, "往返后 gate 数应保真")
    check(r_back.gates[1].findings[0].loc == "draft.md:42", "往返后 finding 定位应保真")

    # 5. 校验:schema 错误必须抛
    try:
        FindingsReport.from_dict({"schema": "wrong", "producer": "x", "target": "y"})
        check(False, "错误 schema 应抛 ValueError")
    except ValueError:
        pass

    # 6. 校验:缺必填字段必须抛
    try:
        FindingsReport.from_dict({"schema": SCHEMA_ID, "producer": "x"})
        check(False, "缺 target 应抛 ValueError")
    except ValueError:
        pass

    # 7. 非法 status/severity 在构造期即抛
    try:
        GateResult("g", "bogus", "info")
        check(False, "非法 status 应抛")
    except ValueError:
        pass

    # 8. Finding 缺字段反序列化抛
    try:
        Finding.from_dict({"loc": "x"})
        check(False, "Finding 缺 issue 应抛")
    except ValueError:
        pass

    # 9. fresh_evidence 默认 False、可设 True 并保真
    r3 = FindingsReport(producer="data-engineering", target="data",
                        fresh_evidence=True).finalize()
    check(FindingsReport.from_json(r3.to_json()).fresh_evidence is True,
          "fresh_evidence 应保真")

    # 10. SARIF 导出:版本/run/result/ruleId/level/location 行号无损
    sarif = r.finalize().to_sarif()
    check(sarif["version"] == "2.1.0", "SARIF 版本应为 2.1.0")
    run = sarif["runs"][0]
    check(run["tool"]["driver"]["name"] == "idea-critique", "SARIF tool.name 应为 producer")
    res = [x for x in run["results"] if x["ruleId"] == "evidence"]
    check(len(res) == 1, "SARIF 应有 evidence 规则的 result")
    check(res[0]["level"] == "error", "critical→SARIF error level")
    check(res[0]["locations"][0]["physicalLocation"]["region"]["startLine"] == 42,
          "SARIF 应从 'draft.md:42' 解析出行号 42")
    check(res[0]["properties"]["light_severity"] == "critical",
          "SARIF properties 应保留原 Light severity 不丢")

    if failures:
        print("findings_schema selftest 失败:")
        for f in failures:
            print("  -", f)
        return 1
    print(f"findings_schema selftest 全绿 ({SCHEMA_ID}): 10 组断言通过 (含 SARIF 导出)")
    return 0


def main():
    ap = argparse.ArgumentParser(description="findings 契约 light.findings.v1")
    ap.add_argument("--selftest", action="store_true", help="运行合成数据自测")
    ap.add_argument("--validate", metavar="FILE", help="校验一个 findings JSON 文件")
    ap.add_argument("--to-sarif", metavar="FILE", help="把一份 findings JSON 导出为 SARIF")
    args = ap.parse_args()
    if args.validate:
        with open(args.validate, encoding="utf-8") as fh:
            d = json.load(fh)
        validate(d)
        print(f"OK: {args.validate} 是合法 {SCHEMA_ID}")
        return 0
    if args.to_sarif:
        with open(args.to_sarif, encoding="utf-8") as fh:
            rep = FindingsReport.from_json(fh.read())
        print(json.dumps(rep.to_sarif(), ensure_ascii=False, indent=2))
        return 0
    # 默认即自测(无参数也跑,符合地基契约约定)
    return _selftest()


if __name__ == "__main__":
    sys.exit(main())
