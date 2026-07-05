from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parents[1]
PANELS = ROOT / "figures" / "panels"


COLORS = {
    "ink": "#0F172A",
    "muted": "#64748B",
    "grid": "#E2E8F0",
    "cyan": "#256D85",
    "violet": "#6D5BA6",
    "emerald": "#4F8A72",
    "amber": "#B08A4F",
    "rose": "#A75D5D",
}


def style_axis(ax: plt.Axes) -> None:
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color("#CBD5E1")
    ax.spines["bottom"].set_color("#CBD5E1")
    ax.tick_params(colors="#475569", labelsize=8)
    ax.grid(True, color=COLORS["grid"], linewidth=0.75, alpha=0.72)
    ax.set_axisbelow(True)


def save(fig: plt.Figure, name: str) -> None:
    PANELS.mkdir(parents=True, exist_ok=True)
    fig.tight_layout(pad=1.15)
    fig.savefig(PANELS / name, dpi=220, facecolor="white")
    plt.close(fig)


def panel_a_design_frontier() -> None:
    rng = np.random.default_rng(1001)
    x = np.linspace(0, 1, 70)
    y = np.linspace(0, 1, 70)
    xx, yy = np.meshgrid(x, y)
    z = 0.42 + 0.22 * xx + 0.26 * yy + 0.18 * xx * yy
    z += 0.06 * np.exp(-((xx - 0.72) ** 2 + (yy - 0.58) ** 2) / 0.035)
    z -= 0.04 * np.exp(-((xx - 0.18) ** 2 + (yy - 0.82) ** 2) / 0.02)
    z += rng.normal(0, 0.006, size=z.shape)

    fig, ax = plt.subplots(figsize=(4.5, 3.35))
    im = ax.contourf(xx, yy, z, levels=16, cmap="cividis")
    ax.contour(xx, yy, z, levels=7, colors="white", linewidths=0.55, alpha=0.65)
    ax.scatter([0.72], [0.58], s=62, color="white", edgecolor=COLORS["ink"], linewidth=1.1, zorder=4)
    ax.set_title("A  Design frontier", loc="left", fontsize=11.5, weight="bold", color=COLORS["ink"])
    ax.set_xlabel("evidence depth", fontsize=8.5, color=COLORS["muted"])
    ax.set_ylabel("replication budget", fontsize=8.5, color=COLORS["muted"])
    cbar = fig.colorbar(im, ax=ax, shrink=0.74, pad=0.02)
    cbar.ax.tick_params(labelsize=7, colors="#475569")
    save(fig, "panel_a_design_frontier.png")


def panel_b_signal_screen() -> None:
    rng = np.random.default_rng(1002)
    effect = rng.normal(0, 0.72, 520)
    strength = np.abs(effect) * 2.15 + rng.gamma(1.4, 0.45, 520)
    y = np.clip(strength, 0, 7.2)
    sig = (np.abs(effect) > 0.72) & (y > 2.4)

    fig, ax = plt.subplots(figsize=(4.5, 3.35))
    ax.scatter(effect[~sig], y[~sig], s=15, color="#CBD5E1", alpha=0.86, linewidths=0)
    ax.scatter(effect[sig & (effect > 0)], y[sig & (effect > 0)], s=24, color="#4F8A72", alpha=0.88, linewidths=0)
    ax.scatter(effect[sig & (effect < 0)], y[sig & (effect < 0)], s=24, color="#8E6C8A", alpha=0.84, linewidths=0)
    ax.axhline(2.4, color="#94A3B8", linewidth=0.9, linestyle="--")
    ax.axvline(0, color="#94A3B8", linewidth=0.9)
    ax.set_title("B  Signal screen", loc="left", fontsize=11.5, weight="bold", color=COLORS["ink"])
    ax.set_xlabel("standardized effect", fontsize=8.5, color=COLORS["muted"])
    ax.set_ylabel("evidence weight", fontsize=8.5, color=COLORS["muted"])
    style_axis(ax)
    save(fig, "panel_b_signal_screen.png")


def panel_c_calibration() -> None:
    rng = np.random.default_rng(1003)
    pred = np.linspace(0.08, 0.92, 9)
    observed = pred - 0.045 * np.sin(pred * np.pi * 1.7) + rng.normal(0, 0.022, len(pred))
    err = 0.035 + 0.018 * np.cos(pred * np.pi) ** 2

    fig, ax = plt.subplots(figsize=(4.5, 3.35))
    ax.plot([0, 1], [0, 1], color="#CBD5E1", linewidth=1.2, linestyle="--")
    ax.fill_between(pred, observed - err, observed + err, color="#BAE6FD", alpha=0.72, linewidth=0)
    ax.plot(pred, observed, color=COLORS["cyan"], linewidth=2.2)
    ax.scatter(pred, observed, s=46, color="white", edgecolor=COLORS["cyan"], linewidth=1.8, zorder=4)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_title("C  Calibration", loc="left", fontsize=11.5, weight="bold", color=COLORS["ink"])
    ax.set_xlabel("predicted probability", fontsize=8.5, color=COLORS["muted"])
    ax.set_ylabel("observed frequency", fontsize=8.5, color=COLORS["muted"])
    style_axis(ax)
    save(fig, "panel_c_calibration.png")


def panel_d_evidence_strength() -> None:
    rng = np.random.default_rng(1004)
    labels = ["search", "critique", "plan", "code", "analysis", "writing", "review"]
    effect = np.array([0.38, 0.52, 0.43, 0.31, 0.47, 0.28, 0.41]) + rng.normal(0, 0.025, 7)
    width = np.array([0.15, 0.18, 0.14, 0.20, 0.16, 0.19, 0.17])
    lo, hi = effect - width, effect + width
    order = np.argsort(effect)
    y = np.arange(len(labels))

    fig, ax = plt.subplots(figsize=(4.5, 3.35))
    palette = plt.cm.mako if hasattr(plt.cm, "mako") else plt.cm.viridis
    colors = ["#6B7A90", "#5E8C9A", "#4F8A72", "#7A8A5F", "#8E7C5A", "#8E6C8A", "#6D5BA6"]
    for rank, idx in enumerate(order):
        ax.plot([lo[idx], hi[idx]], [rank, rank], color=colors[rank], linewidth=4, solid_capstyle="round", alpha=0.78)
        ax.scatter(effect[idx], rank, s=58, color=colors[rank], edgecolor="white", linewidth=1.3, zorder=3)
    ax.axvline(0, color="#94A3B8", linewidth=0.95)
    ax.set_yticks(y, [labels[i] for i in order])
    ax.set_title("D  Evidence strength", loc="left", fontsize=11.5, weight="bold", color=COLORS["ink"])
    ax.set_xlabel("estimated gain", fontsize=8.5, color=COLORS["muted"])
    style_axis(ax)
    ax.grid(axis="y", visible=False)
    save(fig, "panel_d_evidence_strength.png")


def panel_e_failure_map() -> None:
    rng = np.random.default_rng(1005)
    base = rng.normal(0, 0.12, (9, 9))
    x = np.linspace(-1, 1, 9)
    xx, yy = np.meshgrid(x, x)
    matrix = 0.42 * np.exp(-((xx + 0.45) ** 2 + (yy - 0.35) ** 2) / 0.22)
    matrix += 0.58 * np.exp(-((xx - 0.38) ** 2 + (yy + 0.25) ** 2) / 0.16)
    matrix += base
    matrix = np.clip(matrix, 0, None)

    fig, ax = plt.subplots(figsize=(4.5, 3.35))
    im = ax.imshow(matrix, cmap="cividis", aspect="auto")
    ax.set_title("E  Failure-mode map", loc="left", fontsize=11.5, weight="bold", color=COLORS["ink"])
    ax.set_xlabel("workflow stage", fontsize=8.5, color=COLORS["muted"])
    ax.set_ylabel("risk family", fontsize=8.5, color=COLORS["muted"])
    ax.set_xticks([0, 2, 4, 6, 8], ["S1", "S3", "S5", "S7", "S9"])
    ax.set_yticks([0, 2, 4, 6, 8], ["R1", "R3", "R5", "R7", "R9"])
    cbar = fig.colorbar(im, ax=ax, shrink=0.74, pad=0.02)
    cbar.ax.tick_params(labelsize=7, colors="#475569")
    save(fig, "panel_e_failure_map.png")


def main() -> None:
    plt.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "axes.facecolor": "white",
            "figure.facecolor": "white",
            "axes.titlepad": 8,
        }
    )
    panel_a_design_frontier()
    panel_b_signal_screen()
    panel_c_calibration()
    panel_d_evidence_strength()
    panel_e_failure_map()
    print(f"Wrote Python gallery panels to {PANELS}")


if __name__ == "__main__":
    main()
