from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUTPUTS = ROOT / "outputs"


def fit_rate(group: pd.DataFrame) -> dict[str, float | str]:
    clean = group[(group["time_min"] > 0) & (group["C_over_C0"] > 0)].copy()
    x = clean["time_min"].to_numpy(dtype=float)
    y = np.log(clean["C_over_C0"].to_numpy(dtype=float))
    slope, intercept = np.polyfit(x, y, 1)
    pred = slope * x + intercept
    ss_res = float(np.sum((y - pred) ** 2))
    ss_tot = float(np.sum((y - y.mean()) ** 2))
    r2 = 1.0 - ss_res / ss_tot if ss_tot else float("nan")
    k = -float(slope)
    return {
        "k_obs_min-1": round(k, 5),
        "half_life_min": round(float(np.log(2) / k), 2),
        "r2_loglinear": round(r2, 4),
        "intercept": round(float(intercept), 4),
    }


def bootstrap_ci(values: np.ndarray, seed: int = 95050705) -> tuple[float, float, float]:
    rng = np.random.default_rng(seed)
    boot = []
    for _ in range(5000):
        sample = rng.choice(values, size=values.size, replace=True)
        boot.append(float(np.mean(sample)))
    lo, hi = np.percentile(boot, [2.5, 97.5])
    return float(np.mean(values)), float(lo), float(hi)


def main() -> None:
    OUTPUTS.mkdir(parents=True, exist_ok=True)
    time_df = pd.read_csv(DATA / "synthetic_uvvis_timeseries.csv")
    design_df = pd.read_csv(DATA / "synthetic_design_table.csv")
    fits = []
    for keys, group in time_df.groupby(["condition_id", "catalyst", "loading_g_L", "pH", "irradiance_mW_cm2", "scavenger"]):
        condition_id, catalyst, loading, ph, irradiance, scavenger = keys
        record = {
            "condition_id": condition_id,
            "catalyst": catalyst,
            "loading_g_L": loading,
            "pH": ph,
            "irradiance_mW_cm2": irradiance,
            "scavenger": scavenger,
        }
        record.update(fit_rate(group))
        fits.append(record)
    fit_df = pd.DataFrame(fits).merge(design_df, on=["condition_id", "catalyst", "loading_g_L", "pH", "irradiance_mW_cm2", "scavenger"], how="left")
    fit_df.to_csv(DATA / "fitted_rate_constants.csv", index=False, encoding="utf-8")

    no_scavenger = fit_df[fit_df["scavenger"] == "none"].copy()
    best = no_scavenger.loc[no_scavenger["k_obs_min-1"].idxmax()].to_dict()
    catalyst_summary = []
    for catalyst, sub in no_scavenger.groupby("catalyst"):
        mean, lo, hi = bootstrap_ci(sub["k_obs_min-1"].to_numpy())
        catalyst_summary.append({"catalyst": catalyst, "k_mean": mean, "ci_low": lo, "ci_high": hi, "n": int(len(sub))})
    catalyst_summary = sorted(catalyst_summary, key=lambda d: d["k_mean"], reverse=True)

    scavenger = fit_df[fit_df["scavenger"] != "none"].copy()
    control = float(no_scavenger[(no_scavenger["catalyst"] == "N-TiO2/H2O2") & (no_scavenger["loading_g_L"] == 0.75) & (no_scavenger["pH"] == 7.0) & (no_scavenger["irradiance_mW_cm2"] == 105)]["k_obs_min-1"].mean())
    scavenger["relative_activity"] = scavenger["k_obs_min-1"] / control
    scavenger.to_csv(OUTPUTS / "scavenger_summary.csv", index=False, encoding="utf-8")

    summary = {
        "n_time_points": int(len(time_df)),
        "n_conditions": int(fit_df["condition_id"].nunique()),
        "best_condition": {
            "catalyst": best["catalyst"],
            "loading_g_L": float(best["loading_g_L"]),
            "pH": float(best["pH"]),
            "irradiance_mW_cm2": float(best["irradiance_mW_cm2"]),
            "k_obs_min-1": float(best["k_obs_min-1"]),
            "half_life_min": float(best["half_life_min"]),
            "r2_loglinear": float(best["r2_loglinear"]),
        },
        "catalyst_summary": catalyst_summary,
        "scavenger_relative_activity": [
            {
                "scavenger": str(row["scavenger"]),
                "relative_activity": float(row["relative_activity"]),
                "k_obs_min-1": float(row["k_obs_min-1"]),
            }
            for row in scavenger.to_dict(orient="records")
        ],
        "honesty_note": "Synthetic UV-vis data for a reproducible science-demo paper; not a real photocatalyst claim.",
    }
    (OUTPUTS / "analysis_summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {DATA / 'fitted_rate_constants.csv'}")
    print(f"Wrote {OUTPUTS / 'analysis_summary.json'}")


if __name__ == "__main__":
    main()
