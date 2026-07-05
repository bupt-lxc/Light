from __future__ import annotations

from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
PAPER = ROOT / "paper"


def main() -> None:
    pdf = PAPER / "main.pdf"
    doc = fitz.open(pdf)
    page = doc.load_page(0)
    pix = page.get_pixmap(matrix=fitz.Matrix(2.0, 2.0), alpha=False)
    pix.save(PAPER / "main-preview.png")
    print(f"Wrote {PAPER / 'main-preview.png'}")


if __name__ == "__main__":
    main()
