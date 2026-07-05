from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"


def run(script: str) -> None:
    env = os.environ.copy()
    env["PYTHONUTF8"] = "1"
    subprocess.run([sys.executable, str(SCRIPTS / script)], cwd=ROOT, check=True, env=env)


def main() -> None:
    for script in ["generate_data.py", "analyze.py", "make_figures.py", "build_paper.py", "render_preview.py"]:
        run(script)
    print("Photocatalytic dye kinetics study regenerated.")


if __name__ == "__main__":
    main()
