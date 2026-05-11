# CAD toolchain

We use [CadQuery](https://cadquery.readthedocs.io/) (Python) for parametric models. `.py` files are the source of truth; STEP and STL are exported artifacts.

## Why CadQuery

- Plain-text source → diff-friendly, branch-mergeable, AI-editable.
- Parametric: every part exposes a single block of variables at the top of its `.py`.
- Free, no account, no licence keys.
- STEP export is reusable in Fusion 360 / OnShape / FreeCAD if a part graduates to a more complex workflow later.

## One-time setup

CadQuery's OCP backend needs Python 3.11. The repo root keeps a venv at `.venv/`.

```bash
# from the repo root
uv venv --python 3.11 .venv
uv pip install --python .venv/bin/python -r tools/cad/requirements.txt
```

`.venv/` is gitignored.

## Generating exports

Each part's `.py` is runnable directly. From the repo root:

```bash
.venv/bin/python builds/v1/cad/gps-mast/gps-mast-v1.py
```

The script writes `*.step` and `*.stl` next to itself. Re-run after any geometry edit.

## What gets committed

| Committed | Source / generated |
|---|---|
| `<part>-v<n>.py` | source — hand-edited |
| `<part>-v<n>.step` | generated — kept in git so reviewers don't need a Python env |
| `<part>-v<n>.stl` | generated — convenience export |
| `<part>-v<n>.3mf` | generated in Bambu Studio with slicer profile baked in |
| `<part>-v<n>.slicer-profile.json` | exported from Bambu Studio after tuning |
| `README.md`, `notes.md` | hand-written |

`.3mf` and the slicer profile come from Bambu Studio, not the Python script — they capture print settings, not just geometry.
