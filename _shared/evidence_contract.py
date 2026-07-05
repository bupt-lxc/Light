# -*- coding: utf-8 -*-
"""证据强度契约 (light.evidence_strength.v1) — Light v2 / _shared 地基契约 4。

目的
----
把 result-analysis 已经算出的 q 值 / 效应量 / 置信区间,从"只存自己的表"升级为
**全包共享的措辞校准源**,消灭"正文措辞强于证据"这一通病。统计强度 → 允许的断言
措辞档做机械映射,写作/润色/图注/引用/PPT 全部据此卡上限。

被谁消费(v2)
-------------
- result-analysis : 产出方,emit evidence_strength.json
- paper-writing   : 写作/润色时按 grade 卡措辞上限(含审稿人视角循环)
- citation        : 引用支撑度 → 措辞
- figure          : 图注统计标注
- consistency     : 证据↔措辞一致性维度
- research-ethics : "结论夸大"红线门装上可执行工具
- orchestrator    : 写作发现 claim 无证据 → 回拉实验的判据

措辞档的依据 + 与 GRADE 对齐
----------------------------
学术写作的 hedging 阶梯(Hyland 1998《Hedging in Scientific Research Articles》):
强证据才可用 demonstrate/establish 这类高确定性 factive 动词;弱证据须用
suggest/may/appear 等 hedge;不显著只能报 "no significant difference"。

四档与 GRADE(Cochrane 证据确定性四级 high/moderate/low/very-low)对齐(见 GRADE_LEVEL):
  strong↔high · moderate↔moderate · weak↔low · none↔insufficient(very-low/不足)。
诚实落后项:本契约的分档目前只吃**统计强度**(q/效应量/CI/n,≈GRADE 的"不精确"+效应量),
未实现 GRADE 另四域(偏倚/不一致/间接/发表偏倚)的降级——那留给 result-analysis 在拿到
多数据集/多种子结果时做域降级。这里不假装做了 full GRADE。

v2 增量:**中英双语**动词档(v1 仅英文)。中文无词边界,用直接子串匹配 + 否定守卫
(无/不/未/没"显著" 不算违规,那是 none 档的合规表述),避免假阳性。

纯 Python stdlib,无第三方依赖。`python evidence_contract.py --selftest` 自测。
"""
from __future__ import annotations
import json
import re
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

SCHEMA_ID = "light.evidence_strength.v1"

# 四档 → GRADE 证据确定性词表(对外用统一词汇,见 docstring)
GRADE_LEVEL = {"strong": "high", "moderate": "moderate",
               "weak": "low", "none": "insufficient"}

# ── 措辞档:grade → 允许/禁止的断言动词 + 是否强制 hedge(中英双语) ──────
# 高确定性断言动词全集(lint 时据此判断"是否在做强断言")。英文 + 中文。
_ASSERTIVE_VERBS = [
    # 英文
    "prove", "proves", "proven", "proved",
    "demonstrate", "demonstrates", "demonstrated",
    "establish", "establishes", "established",
    "confirm", "confirms", "confirmed",
    "show", "shows", "showed", "shown",
    "significantly", "significant improvement", "substantially",
    "outperform", "outperforms", "outperformed",
    "superior", "best", "state-of-the-art", "sota",
    # 中文(高确定性)
    "证明", "证实", "确证", "显著", "显著优于", "显著提升", "显著改善",
    "优于", "超过", "超越", "最佳", "最优", "领先", "达到最先进", "刷新",
]
# hedge 动词(弱证据应当使用)。英文 + 中文。
_HEDGE_VERBS = ["suggest", "suggests", "may", "appear", "appears", "seem",
                "seems", "could", "might", "tend", "potentially", "preliminary",
                "可能", "或许", "也许", "似乎", "看似", "倾向于", "有望",
                "初步", "推测", "提示", "一定程度"]
# 中文否定词(出现在断言词前 → 该断言被否定 → 非违规,如"无显著差异")
_CJK_NEGATORS = ("无", "不", "未", "没", "非", "难以", "尚未", "并未")


def _is_cjk_term(t: str) -> bool:
    return any("一" <= ch <= "鿿" for ch in t)


def grade_evidence(q_fdr, effect_size, ci95, n) -> str:
    """把统计证据归一成四档之一: strong | moderate | weak | none。

    规则(保守,宁可低估证据强度):
    - none     : 不显著(q>=.05) 或 CI 跨 0 或 q 缺失
    - strong   : q<.01 且 |effect|>=0.5 且 CI 不跨 0 且 n>=30
    - moderate : 显著(q<.05) 且 |effect|>=0.5(中等以上效应),但未达 strong 的全部条件
    - weak     : 显著但小效应(|effect|<0.5) 或 小样本(n<30)
    """
    # 不显著优先判定
    if q_fdr is None or q_fdr >= 0.05:
        return "none"
    if ci95 is not None and len(ci95) == 2:
        lo, hi = ci95
        if lo is not None and hi is not None and lo <= 0 <= hi:
            return "none"  # CI 跨 0 → 差异方向不确定
    eff = abs(effect_size) if effect_size is not None else None
    nn = n if n is not None else 0
    if q_fdr < 0.01 and eff is not None and eff >= 0.5 and nn >= 30:
        return "strong"
    if nn and nn < 30:
        return "weak"  # 小样本封顶 weak,即便效应中等(估计不稳)
    if eff is not None and eff >= 0.5:
        return "moderate"
    return "weak"


def grade_to_grade_level(grade: str) -> str:
    """四档 → GRADE 证据确定性词(high/moderate/low/insufficient)。"""
    return GRADE_LEVEL.get(grade, "insufficient")


def allowed_verb_tier(grade: str) -> dict:
    """grade → {allowed, forbidden, hedge_required}(中英双语)。"""
    if grade == "strong":
        return {"allowed": ["demonstrate", "establish", "show", "confirm",
                            "证明", "证实", "表明", "确证"],
                "forbidden": [],  # 强证据基本不禁(prove 仍建议克制但不硬禁)
                "hedge_required": False}
    if grade == "moderate":
        return {"allowed": ["show", "indicate", "improve", "support", "find",
                            "表明", "说明", "改善", "支持", "发现"],
                "forbidden": ["prove", "demonstrate", "establish", "confirm",
                              "证明", "证实", "确证"],
                "hedge_required": False}
    if grade == "weak":
        return {"allowed": ["suggest", "may", "appear", "seem", "could", "might",
                            "可能", "或许", "似乎", "倾向于"],
                "forbidden": ["prove", "demonstrate", "establish", "confirm",
                              "show", "significantly", "outperform", "superior",
                              "证明", "证实", "确证", "显著", "优于", "超过",
                              "最佳", "最优", "领先"],
                "hedge_required": True}
    # none
    return {"allowed": ["no significant difference", "not significant", "did not differ",
                        "无显著差异", "差异不显著", "未见显著差异"],
            "forbidden": _ASSERTIVE_VERBS[:],
            "hedge_required": True}


def _iter_term_hits(text_low: str, term: str):
    """在 text_low 中找 term 的出现位置(yield start index)。
    英文用词边界 + 常见词形;中文用直接子串 + 否定守卫(否定式不算命中)。"""
    if not _is_cjk_term(term):
        if " " in term or "-" in term:
            pat = r"\b" + re.escape(term) + r"\b"
        else:
            pat = r"\b" + re.escape(term) + r"(?:s|es|ed|d|ing)?\b"
        for m in re.finditer(pat, text_low):
            yield m.start()
    else:
        start = 0
        while True:
            i = text_low.find(term, start)
            if i < 0:
                break
            start = i + len(term)
            # 否定守卫:前两字含否定词 → 跳过(如"无显著""并未证明")
            window = text_low[max(0, i - 2):i]
            if any(neg in window for neg in _CJK_NEGATORS):
                continue
            yield i


def _contains_any(text_low: str, terms) -> bool:
    for t in terms:
        if next(_iter_term_hits(text_low, t), None) is not None:
            return True
    return False


def lint_wording(text: str, claim_evidence: dict) -> list:
    """扫一段正文的断言动词,对照该 claim 的证据 grade,超档即报 violation。

    claim_evidence: 单条 claim 的证据 dict,至少含 evidence_grade(或可由
    q_fdr/effect_size/ci95/n 现算)。返回 violations 列表,每条含定位与降级建议。
    """
    grade = claim_evidence.get("evidence_grade")
    if grade is None:
        grade = grade_evidence(claim_evidence.get("q_fdr"),
                               claim_evidence.get("effect_size"),
                               claim_evidence.get("ci95"),
                               claim_evidence.get("n"))
    tier = allowed_verb_tier(grade)
    forbidden = tier["forbidden"]
    violations = []
    low = text.lower()
    seen = set()
    # 长词优先,避免子串重复报(如 significant improvement 与 significantly)
    for verb in sorted(forbidden, key=len, reverse=True):
        vlow = verb.lower()
        for start in _iter_term_hits(low, vlow):
            line_no = text.count("\n", 0, start) + 1
            key = (vlow, line_no)
            if key in seen:
                continue
            seen.add(key)
            suggest = (tier["allowed"][0] if tier["allowed"] else "(remove claim)")
            violations.append({
                "loc": f"line {line_no}",
                "matched": verb,
                "grade": grade,
                "grade_level": grade_to_grade_level(grade),
                "issue": f"措辞 '{verb}' 强于证据档 '{grade}'(GRADE {grade_to_grade_level(grade)})",
                "suggestion": f"降级为 '{suggest}'" + ("，并加 hedge" if tier["hedge_required"] else ""),
            })
    # hedge 强制但全文无 hedge 词(中英都查)
    if tier["hedge_required"] and not _contains_any(low, _HEDGE_VERBS):
        violations.append({
            "loc": "whole",
            "matched": None,
            "grade": grade,
            "grade_level": grade_to_grade_level(grade),
            "issue": f"证据档 '{grade}' 要求 hedge,但正文无任何 hedge 措辞",
            "suggestion": "加入 suggest/may/可能/或许 等 hedge,或报 'no significant difference / 无显著差异'",
        })
    return violations


def build_evidence_json(claims: list) -> dict:
    """把一组 claim(含 q_fdr/effect_size/ci95/n)产出为 light.evidence_strength.v1。

    自动补 evidence_grade / grade_level / allowed_verbs / forbidden_verbs / hedge_required。
    """
    out_claims = []
    for c in claims:
        grade = c.get("evidence_grade") or grade_evidence(
            c.get("q_fdr"), c.get("effect_size"), c.get("ci95"), c.get("n"))
        tier = allowed_verb_tier(grade)
        out_claims.append({
            "claim_id": c.get("claim_id"),
            "text": c.get("text", ""),
            "q_fdr": c.get("q_fdr"),
            "effect_size": c.get("effect_size"),
            "effect_kind": c.get("effect_kind", "cohens_d"),
            "ci95": c.get("ci95"),
            "n": c.get("n"),
            "evidence_grade": grade,
            "grade_level": grade_to_grade_level(grade),
            "allowed_verbs": tier["allowed"],
            "forbidden_verbs": tier["forbidden"],
            "hedge_required": tier["hedge_required"],
        })
    return {"schema": SCHEMA_ID,
            "source": "result-analysis:claim_evidence_table",
            "claims": out_claims}


def save(report: dict, path: str) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)


def load(path: str) -> dict:
    with open(path, encoding="utf-8") as f:
        return json.load(f)


# ──────────────────────────── selftest ────────────────────────────
def _selftest() -> int:
    ok = True

    def check(cond, msg):
        nonlocal ok
        status = "PASS" if cond else "FAIL"
        if not cond:
            ok = False
        print(f"  [{status}] {msg}")

    print("evidence_contract selftest")
    # 1. grade 分档
    check(grade_evidence(0.001, 0.9, [0.4, 1.3], 120) == "strong", "强证据→strong")
    check(grade_evidence(0.02, 0.7, [0.2, 1.0], 80) == "moderate", "显著中效应→moderate")
    check(grade_evidence(0.03, 0.2, [0.05, 0.4], 200) == "weak", "显著小效应→weak")
    check(grade_evidence(0.01, 0.8, [0.5, 1.1], 20) == "weak", "小样本n<30→weak")
    check(grade_evidence(0.20, 0.9, [-0.1, 1.5], 100) == "none", "不显著→none")
    check(grade_evidence(0.001, 0.9, [-0.2, 1.5], 100) == "none", "CI跨0→none")
    check(grade_evidence(None, 0.9, None, 100) == "none", "q缺失→none")

    # 2. GRADE 词表映射
    check(grade_to_grade_level("strong") == "high"
          and grade_to_grade_level("none") == "insufficient", "四档↔GRADE 词表映射")

    # 3. 措辞档(双语)
    t_strong = allowed_verb_tier("strong")
    check("demonstrate" in t_strong["allowed"] and "证明" in t_strong["allowed"]
          and not t_strong["hedge_required"], "strong 允许 demonstrate/证明 无需 hedge")
    t_weak = allowed_verb_tier("weak")
    check("suggest" in t_weak["allowed"] and "demonstrate" in t_weak["forbidden"]
          and "证明" in t_weak["forbidden"] and t_weak["hedge_required"],
          "weak 允许 suggest/可能 禁 demonstrate/证明 须 hedge")
    t_none = allowed_verb_tier("none")
    check("show" in t_none["forbidden"] and "显著" in t_none["forbidden"],
          "none 禁 show/显著 等所有断言")

    # 4. lint 抓超档(英文)
    weak_claim = {"q_fdr": 0.03, "effect_size": 0.2, "ci95": [0.05, 0.4], "n": 200}
    v1 = lint_wording("Our method demonstrates a significant improvement.", weak_claim)
    check(any(x["matched"] == "demonstrate" for x in v1), "lint 抓到 weak 证据下的 demonstrate")
    # 合规措辞不报(除可能的 hedge 要求)
    v2 = lint_wording("Our method may suggest a modest gain.", weak_claim)
    hard = [x for x in v2 if x["matched"] is not None]
    check(len(hard) == 0, "合规弱措辞无硬性 violation")
    # strong 证据下 demonstrate 合法
    strong_claim = {"q_fdr": 0.001, "effect_size": 0.9, "ci95": [0.4, 1.3], "n": 120}
    v3 = lint_wording("We demonstrate a clear effect.", strong_claim)
    check(len([x for x in v3 if x["matched"] == "demonstrate"]) == 0,
          "strong 证据下 demonstrate 不报")

    # 5. lint 抓超档(中文)+ 否定守卫
    vz = lint_wording("本方法证明了显著优于基线。", weak_claim)
    check(any(x["matched"] == "证明" for x in vz), "中文 lint 抓到 weak 下的'证明'")
    check(any(x["matched"] in ("显著", "显著优于", "优于") for x in vz), "中文 lint 抓到'显著/优于'")
    # 否定式"无显著差异"在 none 档不应被误报为违规(否定守卫)
    none_claim = {"q_fdr": 0.20, "effect_size": 0.1, "ci95": [-0.2, 0.4], "n": 100}
    vneg = lint_wording("两组间无显著差异,差异不显著。", none_claim)
    check(not any(x["matched"] == "显著" for x in vneg),
          "否定守卫:'无显著'不误报为违规(中文 hedging 细节)")

    # 6. 中文 hedge 满足要求(可能)→ 不触发 hedge 缺失
    vzh = lint_wording("本方法可能带来一定程度的提升。", weak_claim)
    check(not any(x["loc"] == "whole" for x in vzh), "中文 hedge'可能'满足 hedge 要求")

    # 7. build_evidence_json + grade_level + 往返
    rep = build_evidence_json([
        {"claim_id": "c1", "text": "A>B", "q_fdr": 0.001, "effect_size": 0.9,
         "ci95": [0.4, 1.3], "n": 120},
        {"claim_id": "c2", "text": "C~D", "q_fdr": 0.3, "effect_size": 0.1,
         "ci95": [-0.2, 0.4], "n": 50},
    ])
    check(rep["schema"] == SCHEMA_ID, "schema id 正确")
    check(rep["claims"][0]["evidence_grade"] == "strong"
          and rep["claims"][0]["grade_level"] == "high", "c1 强证据 + GRADE high")
    check(rep["claims"][1]["evidence_grade"] == "none", "c2 不显著")
    s = json.dumps(rep, ensure_ascii=False)
    check(json.loads(s)["claims"][0]["allowed_verbs"], "JSON 往返保真")

    print("ALL PASS" if ok else "SOME FAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(_selftest())
    print(__doc__)
    print("用法: python evidence_contract.py --selftest")
