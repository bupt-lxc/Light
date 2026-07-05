#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Light 跨技能运行状态契约 ``light.status.v1``。

区分科研门失败、程序错误、依赖不可用、部分完成和证据未决。它不替代
``light.findings.v1``；findings 回答“发现了什么”，本契约回答“操作完成到哪”。
纯标准库；运行 ``python status_contract.py --selftest`` 自测。
"""
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass, field
from typing import Any

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

SCHEMA_ID = "light.status.v1"
VALID_STATUS = (
    "PASS", "WARN", "FAIL", "ERROR", "UNAVAILABLE",
    "PARTIAL", "UNRESOLVED", "SKIPPED",
)


@dataclass
class StatusIssue:
    code: str
    message: str
    locator: str = ""
    retryable: bool = False

    def to_dict(self) -> dict[str, Any]:
        if not self.code.strip() or not self.message.strip():
            raise ValueError("issue.code 与 issue.message 均不能为空")
        result: dict[str, Any] = {
            "code": self.code,
            "message": self.message,
            "retryable": self.retryable,
        }
        if self.locator:
            result["locator"] = self.locator
        return result


@dataclass
class StatusRecord:
    operation: str
    status: str
    checked: list[str] = field(default_factory=list)
    unchecked: list[str] = field(default_factory=list)
    issues: list[StatusIssue] = field(default_factory=list)
    note: str = ""
    schema: str = SCHEMA_ID

    def __post_init__(self) -> None:
        if self.status not in VALID_STATUS:
            raise ValueError(f"非法 status={self.status!r}，应属 {VALID_STATUS}")
        if not self.operation.strip():
            raise ValueError("operation 不能为空")
        if self.status == "PASS" and self.unchecked:
            raise ValueError("PASS 不得仍含 unchecked；应改 PARTIAL 或 UNRESOLVED")
        if self.status != "PASS" and not (
            self.issues or self.note
        ):
            raise ValueError(f"{self.status} 必须说明 issue 或 note，禁止无理由状态")

    def to_dict(self) -> dict[str, Any]:
        result = {
            "schema": self.schema,
            "operation": self.operation,
            "status": self.status,
            "coverage": {
                "checked": list(self.checked),
                "unchecked": list(self.unchecked),
            },
            "issues": [item.to_dict() for item in self.issues],
        }
        if self.note:
            result["note"] = self.note
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=2)


def validate(data: dict[str, Any]) -> None:
    if not isinstance(data, dict):
        raise ValueError("status 必须是 JSON object")
    if data.get("schema") != SCHEMA_ID:
        raise ValueError(f"schema 必须为 {SCHEMA_ID}")
    coverage = data.get("coverage")
    if not isinstance(coverage, dict):
        raise ValueError("coverage 必须是 object")
    for key in ("checked", "unchecked"):
        if not isinstance(coverage.get(key), list):
            raise ValueError(f"coverage.{key} 必须是 list")
    raw_issues = data.get("issues")
    if not isinstance(raw_issues, list):
        raise ValueError("issues 必须是 list")
    issues = []
    for item in raw_issues:
        if not isinstance(item, dict):
            raise ValueError("issues[] 必须是 object")
        issue = StatusIssue(
            code=str(item.get("code", "")),
            message=str(item.get("message", "")),
            locator=str(item.get("locator", "")),
            retryable=bool(item.get("retryable", False)),
        )
        issue.to_dict()
        issues.append(issue)
    StatusRecord(
        operation=str(data.get("operation", "")),
        status=str(data.get("status", "")),
        checked=[str(x) for x in coverage["checked"]],
        unchecked=[str(x) for x in coverage["unchecked"]],
        issues=issues,
        note=str(data.get("note", "")),
    )


def _selftest() -> int:
    failures: list[str] = []

    def check(condition: bool, message: str) -> None:
        if not condition:
            failures.append(message)

    passed = StatusRecord("citation existence", "PASS", checked=["doi"])
    validate(json.loads(passed.to_json()))
    check(passed.to_dict()["status"] == "PASS", "PASS 往返")

    partial = StatusRecord(
        "pdf extraction",
        "PARTIAL",
        checked=["pages:1-3"],
        unchecked=["pages:4"],
        issues=[StatusIssue("PAGE_TIMEOUT", "第 4 页超时", "page:4", True)],
    )
    validate(json.loads(partial.to_json()))
    check(partial.to_dict()["issues"][0]["retryable"] is True, "issue 保真")

    for factory, message in (
        (lambda: StatusRecord("bad pass", "PASS", unchecked=["tables"]),
         "PASS 含 unchecked 应拒绝"),
        (lambda: StatusRecord("bad", "DONE"), "未知状态应拒绝"),
        (lambda: StatusRecord("missing reason", "UNAVAILABLE"),
         "UNAVAILABLE 无原因应拒绝"),
        (lambda: StatusRecord("silent skip", "SKIPPED"),
         "SKIPPED 无原因应拒绝"),
        (lambda: StatusIssue("", "message").to_dict(),
         "空 issue code 应拒绝"),
    ):
        try:
            factory()
            check(False, message)
        except ValueError:
            pass

    unresolved = StatusRecord(
        "claim support",
        "UNRESOLVED",
        checked=["abstract"],
        unchecked=["full text"],
        note="全文不可访问，不能判断直接支持",
    )
    validate(unresolved.to_dict())
    check(unresolved.status == "UNRESOLVED", "UNRESOLVED 合法")

    if failures:
        print("status_contract selftest FAILED")
        for failure in failures:
            print(" -", failure)
        return 1
    print("status_contract selftest PASS: 8 组状态/覆盖断言通过")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=SCHEMA_ID)
    parser.add_argument("--selftest", action="store_true")
    parser.add_argument("--validate")
    args = parser.parse_args()
    if args.validate:
        with open(args.validate, encoding="utf-8-sig") as handle:
            validate(json.load(handle))
        print(f"OK: {args.validate} 是合法 {SCHEMA_ID}")
        return 0
    return _selftest()


if __name__ == "__main__":
    raise SystemExit(main())
