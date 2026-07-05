#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""用户/系统决策授权契约 ``light.decision.v1``。

本契约只证明“谁有权决定、选择了什么、授权范围是什么”，不执行动作。
高风险或不可逆动作只能由用户授权；自动决策只允许低风险且可逆的动作。
"""
from __future__ import annotations

import argparse
import json
import sys
from typing import Any

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

SCHEMA_ID = "light.decision.v1"
STATUSES = {"PROPOSED", "AUTHORIZED", "REJECTED", "REVOKED", "EXPIRED"}
RISKS = {"low", "medium", "high"}
AUTHORITIES = {"user", "automatic"}


def _nonempty(value: Any, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{label} 必须是非空字符串")
    return value


def validate(data: dict[str, Any]) -> None:
    if not isinstance(data, dict):
        raise ValueError("decision 必须是 JSON object")
    if data.get("schema") != SCHEMA_ID:
        raise ValueError(f"schema 必须为 {SCHEMA_ID}")
    _nonempty(data.get("decision_id"), "decision_id")
    _nonempty(data.get("question"), "question")

    status = data.get("status")
    risk = data.get("risk")
    authority = data.get("authority_required")
    reversible = data.get("reversible")
    if status not in STATUSES:
        raise ValueError(f"status 必须属于 {sorted(STATUSES)}")
    if risk not in RISKS:
        raise ValueError(f"risk 必须属于 {sorted(RISKS)}")
    if authority not in AUTHORITIES:
        raise ValueError(f"authority_required 必须属于 {sorted(AUTHORITIES)}")
    if not isinstance(reversible, bool):
        raise ValueError("reversible 必须是 JSON boolean")
    if authority == "automatic" and (risk != "low" or not reversible):
        raise ValueError("automatic 只允许 low-risk 且 reversible 的决策")
    if (risk == "high" or not reversible) and authority != "user":
        raise ValueError("高风险或不可逆决策必须由用户授权")

    scope = data.get("scope")
    if not isinstance(scope, list) or not scope or not all(
        isinstance(item, str) and item.strip() for item in scope
    ):
        raise ValueError("scope 必须是非空字符串列表")

    options = data.get("options")
    if not isinstance(options, list) or len(options) < 2:
        raise ValueError("options 至少需要两个可区分选项")
    option_ids: list[str] = []
    for index, option in enumerate(options):
        if not isinstance(option, dict):
            raise ValueError(f"options[{index}] 必须是 object")
        option_id = _nonempty(option.get("id"), f"options[{index}].id")
        _nonempty(option.get("label"), f"options[{index}].label")
        evidence = option.get("evidence")
        risks = option.get("risks")
        if not isinstance(evidence, list) or not all(
            isinstance(item, str) and item.strip() for item in evidence
        ):
            raise ValueError(f"options[{index}].evidence 必须是字符串列表")
        if not isinstance(risks, list) or not all(
            isinstance(item, str) and item.strip() for item in risks
        ):
            raise ValueError(f"options[{index}].risks 必须是字符串列表")
        option_ids.append(option_id)
    if len(option_ids) != len(set(option_ids)):
        raise ValueError("options.id 必须唯一")

    recommendation = data.get("recommendation")
    selected = data.get("selected")
    if recommendation is not None and recommendation not in option_ids:
        raise ValueError("recommendation 必须引用 options.id 或为 null")
    if selected is not None and selected not in option_ids:
        raise ValueError("selected 必须引用 options.id 或为 null")

    authorization = data.get("authorization")
    if status == "AUTHORIZED":
        if selected is None:
            raise ValueError("AUTHORIZED 必须记录 selected")
        if not isinstance(authorization, dict):
            raise ValueError("AUTHORIZED 必须记录 authorization")
        _nonempty(authorization.get("id"), "authorization.id")
        _nonempty(authorization.get("at"), "authorization.at")
        actor = authorization.get("actor")
        expected = "user" if authority == "user" else "system"
        if actor != expected:
            raise ValueError(f"authorization.actor 必须为 {expected}")
    elif authorization is not None:
        raise ValueError(f"{status} 不得携带 authorization；旧授权应另记历史")

    if status == "PROPOSED" and selected is not None:
        raise ValueError("PROPOSED 尚未拍板，selected 必须为 null")


def _selftest() -> int:
    base = {
        "schema": SCHEMA_ID,
        "decision_id": "D-001",
        "question": "是否启动高成本远程实验？",
        "status": "PROPOSED",
        "risk": "high",
        "reversible": False,
        "authority_required": "user",
        "scope": ["remote-job:exp-7"],
        "options": [
            {"id": "run", "label": "启动", "evidence": ["预算已估算"], "risks": ["产生费用"]},
            {"id": "hold", "label": "暂缓", "evidence": [], "risks": ["进度延迟"]},
        ],
        "recommendation": "hold",
        "selected": None,
        "authorization": None,
    }
    validate(base)

    authorized = dict(
        base,
        status="AUTHORIZED",
        selected="run",
        authorization={
            "id": "AUTH-001",
            "actor": "user",
            "at": "2026-07-04T12:00:00+08:00",
        },
    )
    validate(authorized)

    automatic = dict(
        base,
        decision_id="D-002",
        question="是否重跑本地只读 lint？",
        status="AUTHORIZED",
        risk="low",
        reversible=True,
        authority_required="automatic",
        scope=["local:lint"],
        selected="run",
        authorization={
            "id": "AUTO-001",
            "actor": "system",
            "at": "2026-07-04T12:00:00+08:00",
        },
    )
    validate(automatic)

    failures = 0
    for bad in (
        dict(base, authority_required="automatic"),
        dict(base, options=[base["options"][0]]),
        dict(authorized, authorization=None),
        dict(base, selected="run"),
    ):
        try:
            validate(bad)
            failures += 1
        except ValueError:
            pass
    if failures:
        print(f"decision_contract selftest FAIL: {failures} 个坏样例未拒绝")
        return 1
    print("decision_contract selftest PASS: proposed/user/automatic + 4 个拒绝路径")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=SCHEMA_ID)
    parser.add_argument("--validate")
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    if args.validate:
        with open(args.validate, encoding="utf-8-sig") as handle:
            validate(json.load(handle))
        print(f"OK: {args.validate} 是合法 {SCHEMA_ID}")
        return 0
    return _selftest()


if __name__ == "__main__":
    raise SystemExit(main())
