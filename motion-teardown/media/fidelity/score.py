from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
from PIL import Image
from skimage.color import rgb2gray
from skimage.filters import sobel
from skimage.metrics import structural_similarity

MEDIA = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description="Score private original/rebuild captures; never commit original-site images.")
parser.add_argument("--originals", type=Path, required=True, help="private original captures outside this repository")
parser.add_argument("--rebuilds", type=Path, required=True, help="full-resolution private rebuild captures used for the published measurement")
parser.add_argument("--out", type=Path, required=True, help="local JSON output; use a private path to preserve the published fidelity.json")
args = parser.parse_args()
ORIGINALS = args.originals
REBUILDS = args.rebuilds
SECTIONS = [
    ("hero", 0, 450),
    ("ai-pre", 450, 3150),
    ("title + hand", 3150, 4950),
    ("glow hold", 4950, 7200),
    ("fade", 7200, 8100),
    ("out of scope", 8100, 9000),
]


def grayscale(path: Path) -> np.ndarray:
    with Image.open(path) as image:
        resized = image.convert("RGB").resize((480, 300), Image.Resampling.LANCZOS)
        return rgb2gray(np.asarray(resized, dtype=np.float32) / 255.0)


def score_pair(original: Path, rebuilt: Path) -> tuple[float, float]:
    first = grayscale(original)
    second = grayscale(rebuilt)
    luminance = structural_similarity(first, second, data_range=1.0)
    first_edges = sobel(first)
    second_edges = sobel(second)
    edge_range = max(float(first_edges.max()), float(second_edges.max()), 1e-8)
    structure = structural_similarity(first_edges, second_edges, data_range=edge_range)
    return float(structure), float(luminance)


def section_for(y: int) -> str:
    for index, (name, start, end) in enumerate(SECTIONS):
        if start <= y < end or (index == len(SECTIONS) - 1 and y == end):
            return name
    raise ValueError(f"No section for y={y}")


rows = []
for index in range(101):
    y = index * 90
    original = ORIGINALS / f"step-{index:03}.jpg"
    rebuilt = REBUILDS / f"step-{index:03}.jpg"
    if not original.is_file() or not rebuilt.is_file():
        raise FileNotFoundError(f"Missing pair: {original} or {rebuilt}")
    structure, luminance = score_pair(original, rebuilt)
    rows.append({"y": y, "structure": round(structure, 6), "luminance": round(luminance, 6), "section": section_for(y)})

means = {
    name: {
        "structure": round(float(np.mean([row["structure"] for row in rows if row["section"] == name])), 6),
        "luminance": round(float(np.mean([row["luminance"] for row in rows if row["section"] == name])), 6),
        "steps": sum(row["section"] == name for row in rows),
    }
    for name, _, _ in SECTIONS
}
result = {
    "method": "480x300 grayscale; Sobel gradient magnitude SSIM (primary) and grayscale luminance SSIM (secondary)",
    "overall": {
        "structure": round(float(np.mean([row["structure"] for row in rows])), 6),
        "luminance": round(float(np.mean([row["luminance"] for row in rows])), 6),
    },
    "sections": means,
    "steps": rows,
}
args.out.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps({"overall": result["overall"], "sections": means}, indent=2))
