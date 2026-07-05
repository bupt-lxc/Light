from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUTPUTS = ROOT / "outputs"
FIGURES = ROOT / "figures"


COLORS = {
    "ink": "#0F172A",
    "muted": "#64748B",
    "grid": "#E2E8F0",
    "TiO2": "#5E7896",
    "N-TiO2": "#6D5BA6",
    "N-TiO2/H2O2": "#4F8A72",
    "gold": "#B08A4F",
    "rose": "#A75D5D",
}


def setup() -> None:
    FIGURES.mkdir(parents=True, exist_ok=True)
    plt.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "figure.facecolor": "white",
            "axes.facecolor": "white",
            "axes.spines.top": False,
            "axes.spines.right": False,
            "axes.edgecolor": "#CBD5E1",
            "axes.titleweight": "bold",
            "axes.grid": True,
            "grid.color": COLORS["grid"],
            "grid.linewidth": 0.7,
            "grid.alpha": 0.75,
        }
    )


def save(fig: plt.Figure, name: str) -> None:
    fig.tight_layout()
    path = FIGURES / name
    fig.savefig(path, dpi=220, bbox_inches="tight")
    plt.close(fig)
    print(f"Wrote {path}")


def figure1_kinetics() -> None:
    time_df = pd.read_csv(DATA / "synthetic_uvvis_timeseries.csv")
    fit_df = pd.read_csv(DATA / "fitted_rate_constants.csv")
    chosen = fit_df[
        (fit_df["loading_g_L"] == 0.75)
        & (fit_df["pH"] == 7.0)
        & (fit_df["irradiance_mW_cm2"] == 105)
        & (fit_df["scavenger"] == "none")
    ].copy()
    fig, ax = plt.subplots(figsize=(7.2, 4.2))
    for _, row in chosen.iterrows():
        sub = time_df[time_df["condition_id"] == row["condition_id"]]
        summary = sub.groupby("time_min")["C_over_C0"].agg(["mean", "std"]).reset_index()
        ax.errorbar(
            summary["time_min"],
            summary["mean"],
            yerr=summary["std"],
            marker="o",
            lw=1.9,
            capsize=2.5,
            color=COLORS[row["catalyst"]],
            label=f"{row['catalyst']} (k={row['k_obs_min-1']:.3f} min$^{{-1}}$)",
        )
        t_grid = np.linspace(0, 120, 180)
        ax.plot(t_grid, np.exp(-row["k_obs_min-1"] * t_grid), color=COLORS[row["catalyst"]], alpha=0.35, lw=2.2)
    ax.set_title("Photodegradation kinetics under visible light")
    ax.set_xlabel("Irradiation time (min)")
    ax.set_ylabel("Normalized concentration, C/C0")
    ax.set_ylim(0, 1.08)
    ax.legend(frameon=False, fontsize=8.5)
    save(fig, "figure1_kinetics.png")


def figure2_response_surface() -> None:
    fit_df = pd.read_csv(DATA / "fitted_rate_constants.csv")
    sub = fit_df[
        (fit_df["catalyst"] == "N-TiO2/H2O2")
        & (fit_df["irradiance_mW_cm2"] == 105)
        & (fit_df["scavenger"] == "none")
    ].copy()
    pivot = sub.pivot_table(index="pH", columns="loading_g_L", values="k_obs_min-1", aggfunc="mean").sort_index()
    fig, ax = plt.subplots(figsize=(6.6, 4.3))
    im = ax.imshow(pivot.to_numpy(), cmap="cividis", origin="lower", aspect="auto")
    ax.set_xticks(range(len(pivot.columns)), [f"{v:.2f}" for v in pivot.columns])
    ax.set_yticks(range(len(pivot.index)), [f"{v:.1f}" for v in pivot.index])
    ax.set_xlabel("Catalyst loading (g L$^{-1}$)")
    ax.set_ylabel("pH")
    ax.set_title("Response surface for fitted kobs")
    for i in range(pivot.shape[0]):
        for j in range(pivot.shape[1]):
            value = pivot.iloc[i, j]
            ax.text(j, i, f"{value:.3f}", ha="center", va="center", fontsize=8, color="white" if value > pivot.to_numpy().mean() else COLORS["ink"])
    cbar = fig.colorbar(im, ax=ax, shrink=0.82, pad=0.025)
    cbar.ax.set_ylabel("kobs (min$^{-1}$)")
    save(fig, "figure2_response_surface.png")


def figure3_diagnostics() -> None:
    fit_df = pd.read_csv(DATA / "fitted_rate_constants.csv")
    sub = fit_df[fit_df["scavenger"] == "none"].copy()
    fig, axes = plt.subplots(1, 2, figsize=(8.4, 3.8))
    ax = axes[0]
    ax.scatter(sub["k_true_min-1"], sub["k_obs_min-1"], c=sub["r2_loglinear"], cmap="cividis", s=36, edgecolor="white", linewidth=0.5)
    lim = [min(sub["k_true_min-1"].min(), sub["k_obs_min-1"].min()) * 0.92, max(sub["k_true_min-1"].max(), sub["k_obs_min-1"].max()) * 1.08]
    ax.plot(lim, lim, color="#94A3B8", lw=1.2, ls="--")
    ax.set_xlim(lim)
    ax.set_ylim(lim)
    ax.set_xlabel("Generator ktrue (min$^{-1}$)")
    ax.set_ylabel("Fitted kobs (min$^{-1}$)")
    ax.set_title("A  Recovery of rate constants", loc="left", fontsize=11.5)
    ax = axes[1]
    residual = sub["k_obs_min-1"] - sub["k_true_min-1"]
    ax.hist(residual, bins=18, color="#8FA7BF", edgecolor="white")
    ax.axvline(0, color="#475569", lw=1.1)
    ax.set_xlabel("kobs - ktrue (min$^{-1}$)")
    ax.set_ylabel("Conditions")
    ax.set_title("B  Residual distribution", loc="left", fontsize=11.5)
    save(fig, "figure3_diagnostics.png")


def figure4_scavenger_effects() -> None:
    scav = pd.read_csv(OUTPUTS / "scavenger_summary.csv")
    order = ["IPA", "BQ", "EDTA"]
    scav = scav.set_index("scavenger").loc[order].reset_index()
    fig, ax = plt.subplots(figsize=(5.8, 3.8))
    colors = ["#A75D5D", "#B08A4F", "#6D5BA6"]
    ax.bar(scav["scavenger"], scav["relative_activity"], color=colors, alpha=0.82, width=0.62)
    ax.axhline(1.0, color="#64748B", lw=1.1, ls="--")
    for idx, row in scav.iterrows():
        ax.text(idx, row["relative_activity"] + 0.035, f"{row['relative_activity']:.2f}", ha="center", fontsize=9, color=COLORS["ink"])
    ax.set_ylim(0, 1.12)
    ax.set_ylabel("Relative kobs vs no scavenger")
    ax.set_title("Scavenger sensitivity at the optimum condition")
    save(fig, "figure4_scavenger_effects.png")


def main() -> None:
    setup()
    _ = json.loads((OUTPUTS / "analysis_summary.json").read_text(encoding="utf-8"))
    figure1_kinetics()
    figure2_response_surface()
    figure3_diagnostics()
    figure4_scavenger_effects()


if __name__ == "__main__":
    main()
