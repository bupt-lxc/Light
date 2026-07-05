# -*- coding: utf-8 -*-
"""视觉 QA 回看闭环 (visual_qa) — Light v2 / _shared 地基契约 5。

目的
----
消灭"视觉技能从不把渲染图喂回多模态模型"的病。模型本就是多模态的——渲染成图
再让它自己看,是最大的免费质量胜点(对标 ReLook, arXiv 2510.11498:多模态 critic
看截图打分的 generate→diagnose→refine 闭环)。本契约补三块能力:

1. 确定性几何检测器(纯数学,无需模型):
   输入元素的 AABB(轴对齐包围盒)坐标——figure(matplotlib shape)与 frontend
   (DOM/canvas)本就能读出——检测重叠/溢出画布/超边距/对齐偏差。

2. 确定性 WCAG 对比度检测器(v2 增量,纯数学,无需模型):
   按 WCAG 2.x 相对亮度公式算前景/背景对比度,卡 AA(正文 4.5:1 / 大字 3:1)
   或 AAA(7:1 / 4.5:1)。最高频的可读性/色盲不安全 fail,不渲染就能确定性抓出来。
   v1 把对比度全甩给 VLM,本契约把它落成可机检的门。

3. 渲染回看协议(供 agent 执行的结构化流程):
   render → 喂多模态模型按 rubric 打分 → 出结构化 findings。无渲染器时降级为仅
   几何+对比度检测并明确标注"未做像素级回看",不静默假成功。

render_then_review 协议
-----------------------
消费技能应:
  (a) 把成品渲染为 PNG(figure→matplotlib savefig; frontend→playwright 截图;
      file-reading→已是图直接读);
  (b) 把 PNG 连同 visual_qa_rubric() 一起喂回多模态模型,要求按 rubric 各维度
      打分 + 列出具体缺陷(loc/issue/severity);
  (c) 用 qa_report() 合并几何/对比度检测与 VLM 回看结果;
  (d) 任一 critical 缺陷 → 修 → 重渲染重看,直到无 critical(fix-and-verify 循环)。

被谁消费(v2)
-------------
figure(图规划草图 + 绘图) / frontend-design(前端布局) / file-reading(读图理解)

纯 stdlib(几何/对比度纯数学)。`python visual_qa.py --selftest` 自测。
"""
from __future__ import annotations
import sys


# ── 几何工具 ──────────────────────────────────────────────────────
def _overlap_area(a: dict, b: dict) -> float:
    ax2, ay2 = a["x"] + a["w"], a["y"] + a["h"]
    bx2, by2 = b["x"] + b["w"], b["y"] + b["h"]
    ix = max(0.0, min(ax2, bx2) - max(a["x"], b["x"]))
    iy = max(0.0, min(ay2, by2) - max(a["y"], b["y"]))
    return ix * iy


def _area(r: dict) -> float:
    return max(0.0, r["w"]) * max(0.0, r["h"])


def detect_geometry_issues(shapes: list, canvas_wh: tuple,
                           margins: dict | None = None,
                           overlap_frac_thresh: float = 0.12,
                           align_tol: float = 2.0) -> list:
    """对一组 AABB 元素做确定性几何体检。

    shapes: [{id, x, y, w, h, kind?, text?}]  坐标同一单位(px/EMU/pt 皆可)
    canvas_wh: (W, H)
    margins: {left,right,top,bottom} 或 None
    返回 issues: [{type, severity, elements, detail, suggestion}]
    """
    W, H = canvas_wh
    issues = []

    # 1. 两两重叠(忽略极小重叠;按较小元素面积的占比判严重度)
    for i in range(len(shapes)):
        for j in range(i + 1, len(shapes)):
            a, b = shapes[i], shapes[j]
            ov = _overlap_area(a, b)
            if ov <= 0:
                continue
            small = min(_area(a), _area(b)) or 1.0
            frac = ov / small
            if frac >= overlap_frac_thresh:
                sev = "critical" if frac >= 0.5 else "important"
                issues.append({
                    "type": "overlap",
                    "severity": sev,
                    "elements": [a.get("id", i), b.get("id", j)],
                    "detail": f"重叠面积占较小元素 {frac:.0%}",
                    "suggestion": "拉开间距或调整层级/尺寸,避免内容遮挡",
                })

    # 2. 溢出画布
    for k, r in enumerate(shapes):
        out = []
        if r["x"] < 0:
            out.append("左")
        if r["y"] < 0:
            out.append("上")
        if r["x"] + r["w"] > W:
            out.append("右")
        if r["y"] + r["h"] > H:
            out.append("下")
        if out:
            issues.append({
                "type": "overflow_canvas",
                "severity": "critical",
                "elements": [r.get("id", k)],
                "detail": f"元素超出画布边界: {'/'.join(out)}",
                "suggestion": "缩小或移动元素使其完全落在画布内",
            })

    # 3. 超边距
    if margins:
        for k, r in enumerate(shapes):
            viol = []
            if r["x"] < margins.get("left", 0):
                viol.append("左")
            if r["y"] < margins.get("top", 0):
                viol.append("上")
            if r["x"] + r["w"] > W - margins.get("right", 0):
                viol.append("右")
            if r["y"] + r["h"] > H - margins.get("bottom", 0):
                viol.append("下")
            if viol:
                issues.append({
                    "type": "margin_violation",
                    "severity": "important",
                    "elements": [r.get("id", k)],
                    "detail": f"侵入安全边距: {'/'.join(viol)}",
                    "suggestion": "保持在安全边距内,留出呼吸空间",
                })

    # 4. 对齐偏差(本应对齐却轻微错位:左/顶边缘聚类,发现 0<差<align_tol 的成对)
    edges_left = [(r.get("id", k), r["x"]) for k, r in enumerate(shapes)]
    edges_top = [(r.get("id", k), r["y"]) for k, r in enumerate(shapes)]
    for label, edges in (("左对齐", edges_left), ("顶对齐", edges_top)):
        for i in range(len(edges)):
            for j in range(i + 1, len(edges)):
                d = abs(edges[i][1] - edges[j][1])
                if 0 < d <= align_tol:
                    issues.append({
                        "type": "misalignment",
                        "severity": "minor",
                        "elements": [edges[i][0], edges[j][0]],
                        "detail": f"{label}边缘相差 {d:.1f}(疑似本应对齐却错位)",
                        "suggestion": "对齐到同一基线,或拉开到明显不同的位置",
                    })
    return issues


# ── WCAG 对比度检测(v2 增量,确定性,无需模型) ───────────────────────
def _parse_rgb(color) -> tuple:
    """接受 '#rrggbb' / '#rgb' / (r,g,b)[0-255] / (r,g,b)[0-1],归一为 (r,g,b)∈[0,1]。"""
    if isinstance(color, str):
        s = color.strip().lstrip("#")
        if len(s) == 3:
            s = "".join(ch * 2 for ch in s)
        if len(s) != 6:
            raise ValueError(f"非法颜色: {color!r}(应为 #rrggbb/#rgb)")
        return tuple(int(s[i:i + 2], 16) / 255.0 for i in (0, 2, 4))
    if isinstance(color, (tuple, list)) and len(color) >= 3:
        r, g, b = color[0], color[1], color[2]
        if any(v > 1.0 for v in (r, g, b)):   # 视为 0-255
            return (r / 255.0, g / 255.0, b / 255.0)
        return (float(r), float(g), float(b))
    raise ValueError(f"无法解析颜色: {color!r}")


def _linearize(c: float) -> float:
    return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4


def relative_luminance(color) -> float:
    """WCAG 2.x 相对亮度 L = 0.2126R + 0.7152G + 0.0722B(sRGB 线性化后)。白=1 黑=0。"""
    r, g, b = (_linearize(x) for x in _parse_rgb(color))
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast_ratio(color1, color2) -> float:
    """两色对比度 (L1+0.05)/(L2+0.05),L1 为较亮者。范围 1:1 ~ 21:1。"""
    l1, l2 = relative_luminance(color1), relative_luminance(color2)
    hi, lo = max(l1, l2), min(l1, l2)
    return round((hi + 0.05) / (lo + 0.05), 3)


# WCAG 2.x 最低对比度阈值: level → (正文, 大字≥18pt或14pt粗)
_WCAG_THRESH = {"AA": (4.5, 3.0), "AAA": (7.0, 4.5)}


def check_contrast(fg, bg, large: bool = False, level: str = "AA") -> dict:
    """检查前景/背景对比度是否达 WCAG。返回 {ratio, required, pass, level, large}。"""
    ratio = contrast_ratio(fg, bg)
    normal_req, large_req = _WCAG_THRESH.get(level, _WCAG_THRESH["AA"])
    required = large_req if large else normal_req
    return {"ratio": ratio, "required": required, "pass": ratio >= required,
            "level": level, "large": large}


def detect_contrast_issues(pairs: list, level: str = "AA") -> list:
    """对一组前景/背景配色做 WCAG 对比度体检。

    pairs: [{fg, bg, where?, large?}]  fg/bg 为颜色(#rrggbb 或 rgb 元组)
    返回与几何 issues 同构的列表,可直接喂 qa_report。
    """
    issues = []
    for k, p in enumerate(pairs):
        res = check_contrast(p["fg"], p["bg"], large=bool(p.get("large", False)),
                             level=level)
        if not res["pass"]:
            # 比 3:1 还低基本不可读 → critical;否则未达标 → important
            sev = "critical" if res["ratio"] < 3.0 else "important"
            issues.append({
                "type": "low_contrast",
                "severity": sev,
                "elements": [p.get("where", k)],
                "detail": (f"对比度 {res['ratio']}:1 < WCAG {level} "
                           f"要求 {res['required']}:1"
                           + ("(大字)" if res["large"] else "(正文)")),
                "suggestion": "加深前景或调浅背景以提升对比度,保障弱视/色盲可读",
            })
    return issues


def visual_qa_rubric() -> dict:
    """返回视觉评分 rubric,供消费技能塞进喂给多模态模型的 prompt。

    每维 1-5 分(5 最佳)。<4 视为需修。"""
    return {
        "scale": "1-5 (5=优秀, <4=需修)",
        "dimensions": {
            "clarity": "主体信息一眼可读,无歧义,焦点明确",
            "no_overlap": "无元素遮挡、无文字压图、无重叠",
            "contrast": "前景/背景对比充分(正文≥4.5:1),弱视可读",
            "label_legibility": "所有标签/坐标轴/图例字号足够、不截断、不溢出",
            "whitespace": "留白均衡,不拥挤也不空旷,密度恰当",
            "hierarchy": "视觉层次清晰,主次分明,对齐严谨",
            "consistency": "配色/字体/风格统一,无跑题装饰",
        },
        "instruction": ("逐维打分并列出具体缺陷,每条含 loc(在图中的位置描述)、"
                        "issue、severity(critical/important/minor)。任一 critical 必须修。"),
    }


def qa_report(geometry_issues: list, vlm_findings: list | None = None,
              contrast_issues: list | None = None) -> dict:
    """合并几何检测 + WCAG 对比度 + VLM 回看为统一报告。

    vlm_findings: None 表示未做像素级回看(无渲染器/未喂回模型) —— 如实标注。
    contrast_issues: detect_contrast_issues 的结果(确定性,可选)。
    """
    all_issues = list(geometry_issues)
    if contrast_issues:
        all_issues.extend(contrast_issues)
    pixel_review_done = vlm_findings is not None
    if vlm_findings:
        all_issues.extend(vlm_findings)
    n_crit = sum(1 for x in all_issues if x.get("severity") == "critical")
    n_imp = sum(1 for x in all_issues if x.get("severity") == "important")
    verdict = "fail" if n_crit else ("warn" if n_imp else "pass")
    return {
        "schema": "light.visual_qa.v1",
        "verdict": verdict,
        "pixel_review_done": pixel_review_done,
        "pixel_review_note": (None if pixel_review_done else
                              "未做像素级回看(无渲染器或未喂回多模态模型),"
                              "仅几何+对比度检测;视觉品味/层次/可读性细节未经验证"),
        "counts": {"critical": n_crit, "important": n_imp, "total": len(all_issues)},
        "issues": all_issues,
    }


# ──────────────────────────── selftest ────────────────────────────
def _selftest() -> int:
    ok = True

    def check(cond, msg):
        nonlocal ok
        if not cond:
            ok = False
        print(f"  [{'PASS' if cond else 'FAIL'}] {msg}")

    print("visual_qa selftest")
    canvas = (100, 100)

    # 1. 重叠检出
    overlapping = [
        {"id": "A", "x": 10, "y": 10, "w": 40, "h": 40},
        {"id": "B", "x": 30, "y": 30, "w": 40, "h": 40},  # 与 A 重叠
    ]
    iss = detect_geometry_issues(overlapping, canvas)
    check(any(x["type"] == "overlap" for x in iss), "检出重叠")

    # 2. 溢出画布检出
    overflow = [{"id": "C", "x": 80, "y": 80, "w": 40, "h": 40}]  # 超右下
    iss2 = detect_geometry_issues(overflow, canvas)
    check(any(x["type"] == "overflow_canvas" and x["severity"] == "critical"
              for x in iss2), "检出溢出画布(critical)")

    # 3. 正常布局无重叠/溢出误报
    clean = [
        {"id": "D", "x": 5, "y": 5, "w": 30, "h": 30},
        {"id": "E", "x": 50, "y": 5, "w": 30, "h": 30},
    ]
    iss3 = detect_geometry_issues(clean, canvas)
    check(not any(x["type"] in ("overlap", "overflow_canvas") for x in iss3),
          "正常布局无重叠/溢出误报")

    # 4. 超边距检出
    margins = {"left": 10, "right": 10, "top": 10, "bottom": 10}
    iss4 = detect_geometry_issues([{"id": "F", "x": 2, "y": 50, "w": 20, "h": 20}],
                                  canvas, margins)
    check(any(x["type"] == "margin_violation" for x in iss4), "检出超边距")

    # 5. 对齐偏差检出(两元素左边缘差 1.5)
    misalign = [
        {"id": "G", "x": 10.0, "y": 5, "w": 20, "h": 20},
        {"id": "H", "x": 11.5, "y": 40, "w": 20, "h": 20},
    ]
    iss5 = detect_geometry_issues(misalign, canvas)
    check(any(x["type"] == "misalignment" for x in iss5), "检出对齐偏差")

    # 6. WCAG 对比度:黑白=21:1 上限、白白=1、相对亮度边界
    check(abs(relative_luminance("#ffffff") - 1.0) < 1e-6, "白色相对亮度=1")
    check(relative_luminance("#000000") == 0.0, "黑色相对亮度=0")
    check(contrast_ratio("#000000", "#ffffff") >= 20.9, "黑白对比≈21:1")
    check(contrast_ratio("#ffffff", "#ffffff") == 1.0, "同色对比=1:1")
    # 元组输入(0-255)与 hex 一致
    check(abs(contrast_ratio((0, 0, 0), (255, 255, 255))
              - contrast_ratio("#000", "#fff")) < 1e-6, "元组与hex输入一致")

    # 7. check_contrast:#999 正文在白底上 fail AA(≈2.85),黑字 pass
    bad = check_contrast("#999999", "#ffffff", large=False, level="AA")
    check(not bad["pass"] and bad["ratio"] < 4.5, "灰#999正文/白底 fail AA")
    good = check_contrast("#000000", "#ffffff", level="AA")
    check(good["pass"], "黑字/白底 pass AA")
    # 大字阈值更宽:#999 大字仍 fail(2.85<3),但 #777 大字可过
    check(not check_contrast("#999999", "#ffffff", large=True)["pass"],
          "灰#999大字仍 fail(<3:1)")

    # 8. detect_contrast_issues:两档分级(<3 不可读=critical, 3~4.5 未达标=important)
    cissues_crit = detect_contrast_issues([
        {"fg": "#999999", "bg": "#ffffff", "where": "正文段落"},  # ≈2.85 → critical
    ])
    check(len(cissues_crit) == 1 and cissues_crit[0]["severity"] == "critical",
          "对比度<3:1 判 critical(不可读)")
    cissues_imp = detect_contrast_issues([
        {"fg": "#888888", "bg": "#ffffff", "where": "正文段落"},  # ≈3.55 → important
        {"fg": "#000000", "bg": "#ffffff", "where": "标题"},      # 合格,不报
    ])
    check(len(cissues_imp) == 1 and cissues_imp[0]["severity"] == "important",
          "对比度 3~4.5 判 important(未达 AA),合格项不报")

    # 9. rubric 结构
    r = visual_qa_rubric()
    check("dimensions" in r and "no_overlap" in r["dimensions"], "rubric 含维度")

    # 10. qa_report 合并 + verdict + 诚实标注
    rep = qa_report(iss2)  # 仅几何(有 critical),无 VLM
    check(rep["verdict"] == "fail" and not rep["pixel_review_done"]
          and rep["pixel_review_note"], "report: critical→fail 且标注未做像素回看")
    rep2 = qa_report(iss3, vlm_findings=[], contrast_issues=cissues_imp)  # 对比度 important
    check(rep2["verdict"] == "warn" and rep2["pixel_review_done"],
          "report: 干净几何+做回看+对比度important→warn")
    rep_cc = qa_report([], contrast_issues=cissues_crit)  # 对比度 critical
    check(rep_cc["verdict"] == "fail", "report: 对比度critical→fail")
    rep3 = qa_report([], vlm_findings=[
        {"type": "low_contrast", "severity": "important", "loc": "标题",
         "issue": "对比不足"}])
    check(rep3["verdict"] == "warn", "report: VLM important→warn")

    print("ALL PASS" if ok else "SOME FAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(_selftest())
    print(__doc__)
    print("用法: python visual_qa.py --selftest")
