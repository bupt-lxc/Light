from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"


def generate(seed: int = 9505) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    participants = np.arange(1, 97)
    groups = np.array(["Baseline workflow"] * 48 + ["Light-assisted workflow"] * 48)
    rng.shuffle(groups)
    tasks = ["Literature mapping", "Experiment reproduction", "Paper argumentation"]
    task_base = {
        "Literature mapping": 58.0,
        "Experiment reproduction": 53.0,
        "Paper argumentation": 55.0,
    }
    task_time = {
        "Literature mapping": 74.0,
        "Experiment reproduction": 92.0,
        "Paper argumentation": 86.0,
    }
    task_effect = {
        "Literature mapping": 10.5,
        "Experiment reproduction": 7.5,
        "Paper argumentation": 5.0,
    }

    rows: list[dict[str, object]] = []
    for participant_id, group in zip(participants, groups, strict=True):
        skill = rng.normal(0, 5)
        caution = rng.normal(0, 1)
        for task in tasks:
            task_noise = rng.normal(0, 2.2)
            for week in range(5):
                assisted = group == "Light-assisted workflow"
                learning = 2.2 * week + (0.25 * week**2)
                intervention = task_effect[task] * (week / 4) if assisted else 0.9 * week
                quality = task_base[task] + skill + task_noise + learning + intervention + rng.normal(0, 3.8)
                quality = float(np.clip(quality, 35, 98))

                time_delta = -2.8 * week - (8.0 * week / 4 if assisted else 0.8 * week)
                time_minutes = task_time[task] + rng.normal(0, 6.5) + time_delta - skill * 0.18
                time_minutes = float(np.clip(time_minutes, 38, 120))

                error_rate = 3.9 - 0.25 * week - (0.9 * week / 4 if assisted else 0.1 * week) + caution * 0.1
                error_count = int(max(0, rng.poisson(max(error_rate, 0.25))))

                rows.append(
                    {
                        "participant_id": f"P{participant_id:03d}",
                        "group": group,
                        "task": task,
                        "week": week,
                        "evidence_quality_score": round(quality, 2),
                        "time_minutes": round(time_minutes, 2),
                        "error_count": error_count,
                    }
                )
    return pd.DataFrame(rows)


def main() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    out = DATA_DIR / "synthetic_experiment.csv"
    df = generate()
    df.to_csv(out, index=False, encoding="utf-8")
    print(f"Wrote {out} ({len(df)} rows)")


if __name__ == "__main__":
    main()
