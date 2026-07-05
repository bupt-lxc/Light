from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw


ROOT = Path(__file__).resolve().parents[1]
PANELS = ROOT / "figures" / "panels"
OUT = ROOT / "figures" / "research_figure_gallery.png"


PANEL_FILES = [
    "panel_a_design_frontier.png",
    "panel_b_signal_screen.png",
    "panel_c_calibration.png",
    "panel_d_evidence_strength.png",
    "panel_e_failure_map.png",
    "panel_f_quality_trajectory.png",
    "panel_g_distribution_shift.png",
    "panel_h_tradeoff_curve.png",
    "panel_i_risk_budget.png",
]


def rounded_panel(panel: Image.Image, size: tuple[int, int]) -> Image.Image:
    panel = panel.convert("RGB").resize(size, Image.Resampling.LANCZOS)
    return panel


def main() -> None:
    missing = [name for name in PANEL_FILES if not (PANELS / name).exists()]
    if missing:
        raise FileNotFoundError(f"Missing gallery panels: {missing}")

    tile_w, tile_h = 760, 566
    gap = 28
    margin = 36
    width = margin * 2 + tile_w * 3 + gap * 2
    height = margin * 2 + tile_h * 3 + gap * 2
    canvas = Image.new("RGB", (width, height), "#F8FAFC")
    draw = ImageDraw.Draw(canvas)

    for index, filename in enumerate(PANEL_FILES):
        row, col = divmod(index, 3)
        x = margin + col * (tile_w + gap)
        y = margin + row * (tile_h + gap)
        shadow = [x + 8, y + 10, x + tile_w + 8, y + tile_h + 10]
        draw.rounded_rectangle(shadow, radius=24, fill="#E2E8F0")
        draw.rounded_rectangle([x, y, x + tile_w, y + tile_h], radius=24, fill="white", outline="#E2E8F0", width=2)
        panel = rounded_panel(Image.open(PANELS / filename), (tile_w - 18, tile_h - 18))
        canvas.paste(panel, (x + 9, y + 9))

    OUT.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(OUT, quality=95)
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
