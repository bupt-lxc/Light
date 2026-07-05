from __future__ import annotations

import os
import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = ROOT.parents[1]


def run_python(script: str) -> None:
    env = os.environ.copy()
    env["PYTHONUTF8"] = "1"
    subprocess.run([sys.executable, str(ROOT / "scripts" / script)], check=True, cwd=ROOT, env=env)


def find_rscript() -> str | None:
    found = shutil.which("Rscript")
    if found:
        return found
    candidates = [
        Path(r"C:\Program Files\R\R-4.6.1\bin\Rscript.exe"),
        Path(r"C:\Program Files\R\R-4.6.1\bin\x64\Rscript.exe"),
        Path(r"C:\Program Files\R\R-4.5.0\bin\Rscript.exe"),
        Path(r"C:\Program Files\R\R-4.4.0\bin\Rscript.exe"),
    ]
    for candidate in candidates:
        if candidate.exists():
            return str(candidate)
    return None


def run_r() -> None:
    rscript = find_rscript()
    if not rscript:
        print("Rscript not found; skipped R/ggplot2 figure. Python figure is still valid.")
        return
    env = os.environ.copy()
    user_lib = Path(os.environ.get("LOCALAPPDATA", str(Path.home()))) / "R" / "win-library" / "4.6"
    if user_lib.exists():
        env["R_LIBS_USER"] = str(user_lib)
    try:
        subprocess.run([rscript, str(ROOT / "scripts" / "r_gallery_panels.R")], check=True, cwd=ROOT, env=env)
    except subprocess.CalledProcessError:
        print("R panels failed. Install/check ggplot2 and scales, then rerun scripts/r_gallery_panels.R.")
        raise


def main() -> None:
    run_python("generate_synthetic_data.py")
    run_python("python_gallery_panels.py")
    run_r()
    run_python("compose_figure_gallery.py")
    print("E2E demo complete.")


if __name__ == "__main__":
    main()
