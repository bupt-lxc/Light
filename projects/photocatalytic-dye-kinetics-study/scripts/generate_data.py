from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"


CATALYSTS = ["TiO2", "N-TiO2", "N-TiO2/H2O2"]
TIME_MIN = np.array([0, 5, 10, 20, 30, 45, 60, 90, 120], dtype=float)


def rate_constant(catalyst: str, loading: float, ph: float, irradiance: float, scavenger: str) -> float:
    base = {"TiO2": 0.0105, "N-TiO2": 0.0175, "N-TiO2/H2O2": 0.0235}[catalyst]
    load_term = np.exp(-((loading - 0.78) ** 2) / 0.28)
    ph_term = np.exp(-((ph - 6.5) ** 2) / 8.5)
    light_term = 0.74 + 0.32 * (irradiance / 100.0)
    scavenger_penalty = {
        "none": 1.00,
        "IPA": 0.58,   # hydroxyl radical scavenger surrogate
        "BQ": 0.70,    # superoxide scavenger surrogate
        "EDTA": 0.82,  # hole scavenger surrogate
    }[scavenger]
    return float(base * (0.72 + 0.46 * load_term) * (0.78 + 0.35 * ph_term) * light_term * scavenger_penalty)


def generate(seed: int = 95050705) -> tuple[pd.DataFrame, pd.DataFrame]:
    rng = np.random.default_rng(seed)
    rows: list[dict[str, object]] = []
    design_rows: list[dict[str, object]] = []
    condition_id = 0
    loadings = [0.25, 0.50, 0.75, 1.00, 1.25]
    ph_values = [4.0, 5.5, 7.0, 8.5]
    irradiances = [55, 80, 105]

    for catalyst in CATALYSTS:
        for loading in loadings:
            for ph in ph_values:
                for irradiance in irradiances:
                    condition_id += 1
                    k_true = rate_constant(catalyst, loading, ph, irradiance, "none")
                    design_rows.append(
                        {
                            "condition_id": f"C{condition_id:03d}",
                            "catalyst": catalyst,
                            "loading_g_L": loading,
                            "pH": ph,
                            "irradiance_mW_cm2": irradiance,
                            "scavenger": "none",
                            "k_true_min-1": round(k_true, 5),
                        }
                    )
                    for replicate in range(1, 4):
                        dark_offset = rng.normal(0.012, 0.004)
                        path_length_noise = rng.normal(1.0, 0.015)
                        for t in TIME_MIN:
                            c_ratio = np.exp(-k_true * t)
                            instrument_noise = rng.normal(0, 0.018 + 0.004 * (t / 120))
                            measured = float(np.clip(c_ratio * path_length_noise + dark_offset + instrument_noise, 0.025, 1.08))
                            absorbance = 1.05 * measured + rng.normal(0, 0.008)
                            rows.append(
                                {
                                    "condition_id": f"C{condition_id:03d}",
                                    "catalyst": catalyst,
                                    "loading_g_L": loading,
                                    "pH": ph,
                                    "irradiance_mW_cm2": irradiance,
                                    "scavenger": "none",
                                    "replicate": replicate,
                                    "time_min": int(t),
                                    "C_over_C0": round(measured, 5),
                                    "absorbance_664nm": round(float(absorbance), 5),
                                }
                            )

    # Mechanistic scavenger panel at the response-surface optimum.
    for scavenger in ["IPA", "BQ", "EDTA"]:
        condition_id += 1
        k_true = rate_constant("N-TiO2/H2O2", 0.75, 7.0, 105, scavenger)
        design_rows.append(
            {
                "condition_id": f"C{condition_id:03d}",
                "catalyst": "N-TiO2/H2O2",
                "loading_g_L": 0.75,
                "pH": 7.0,
                "irradiance_mW_cm2": 105,
                "scavenger": scavenger,
                "k_true_min-1": round(k_true, 5),
            }
        )
        for replicate in range(1, 5):
            for t in TIME_MIN:
                c_ratio = np.exp(-k_true * t)
                measured = float(np.clip(c_ratio + rng.normal(0, 0.018), 0.025, 1.08))
                rows.append(
                    {
                        "condition_id": f"C{condition_id:03d}",
                        "catalyst": "N-TiO2/H2O2",
                        "loading_g_L": 0.75,
                        "pH": 7.0,
                        "irradiance_mW_cm2": 105,
                        "scavenger": scavenger,
                        "replicate": replicate,
                        "time_min": int(t),
                        "C_over_C0": round(measured, 5),
                        "absorbance_664nm": round(float(1.05 * measured + rng.normal(0, 0.008)), 5),
                    }
                )

    return pd.DataFrame(rows), pd.DataFrame(design_rows)


def main() -> None:
    DATA.mkdir(parents=True, exist_ok=True)
    time_df, design_df = generate()
    time_df.to_csv(DATA / "synthetic_uvvis_timeseries.csv", index=False, encoding="utf-8")
    design_df.to_csv(DATA / "synthetic_design_table.csv", index=False, encoding="utf-8")
    print(f"Wrote {DATA / 'synthetic_uvvis_timeseries.csv'} ({len(time_df)} rows)")
    print(f"Wrote {DATA / 'synthetic_design_table.csv'} ({len(design_df)} rows)")


if __name__ == "__main__":
    main()
