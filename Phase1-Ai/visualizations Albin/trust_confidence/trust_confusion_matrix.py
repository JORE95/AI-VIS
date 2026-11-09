import csv
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt

CLASSES = ["call", "dislike", "fist", "four", "like"]

def repo_root():
    for parent in Path(__file__).resolve().parents:
        if (parent / ".git").exists():
            return parent
    raise RuntimeError("repo root not found")

repo = repo_root()
BASE = repo / "phase1-Ai/split_preprocess-train/base results and setup/test_set_merged.csv"
FLIP = repo / "Phase1-Ai/split_preprocess-train/visualizations Jakub/test_results_flipped_horizontal.csv"
OUT = Path(__file__).resolve().parent / "figures"
OUT.mkdir(parents=True, exist_ok=True)

def row(p):
    with open(p, newline="") as f:
        return list(csv.DictReader(f))

def confusion(rs):
    idx = {c:i for i,c in enumerate(CLASSES)}
    m = np.zeros((len(CLASSES), len(CLASSES)), dtype=int)
    for r in rs:
        t, p = r.get("true_label"), r.get("pred_label")
        if t in idx and p in idx:
            m[idx[t], idx[p]]+=1
    return m

def row_norm(m):
    s = m.sum(axis=1, keepdims=True)
    return np.divide(m, s, out=np.zeros_like(m, dtype=float), where=s != 0)

data = [("normal", row(BASE)), ("side flip", row(FLIP))]

fig, axes = plt.subplots(1, 2, figsize=(12, 5))
for ax, (name, rs) in zip(axes, data):
    m = confusion(rs)
    pct = row_norm(m)
    im = ax.imshow(pct, cmap="Blues", vmin=0, vmax=1)
    ax.set_title(name)
    ax.set_xticks(range(len(CLASSES))); ax.set_xticklabels(CLASSES, rotation=45, ha="right")
    ax.set_yticks(range(len(CLASSES))); ax.set_yticklabels(CLASSES)
    ax.set_xlabel("predicted"); ax.set_ylabel("true")
    for i in range(len(CLASSES)):
        for j in range(len(CLASSES)):
            ax.text(j, i, f"{pct[i, j] * 100:.0f}%\n({m[i, j]})",
                    ha="center", va="center", fontsize=8,
                    color="white" if pct[i, j] > 0.5 else "black")

fig.colorbar(im, ax=axes, fraction=0.046, pad=0.04, label="row-normalised share")
plt.suptitle("Confusion matrix: normal vs side flip")
plt.tight_layout()
plt.savefig(OUT / "fig5_confusion_trust.png", dpi=150)
plt.close()

for name, rs in data:
    m = confusion(rs)
    acc = np.trace(m) / m.sum() * 100
    dislike_share = m[:, CLASSES.index("dislike")].sum() / m.sum() * 100
    print(f"{name:10s} accuracy {acc:5.1f}% | predicted 'dislike' {dislike_share:5.1f}%")