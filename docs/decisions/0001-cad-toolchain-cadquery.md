# 0001 — CAD toolchain: CadQuery

**Date:** 2026-05-05
**Status:** Accepted
**Applies to:** all builds (cross-cutting)

## Context

v1 needs 5–6 printed parts (gps-mast, antenna mounts, battery tray, motor soft-mounts, canopy, standoffs). Future builds will reuse and extend the same parts library. We need a CAD workflow that:

- Is version-controllable in git with meaningful diffs (not opaque binaries).
- Survives "no exotic sourcing" — the toolchain itself should be free, open, no account, no licence keys, no vendor lock-in.
- Plays well with branch-merge workflows (we'll have many overlapping airframe revisions).
- Can be edited by both humans and AI assistants without a GUI.
- Exports a portable interchange format (STEP) so any part can be opened later in Fusion 360, OnShape, or FreeCAD if needed.
- Is parameterized so a single `WIDTH = 38.0` change re-exports the whole part — supports the scaled-manufacturing posture from `docs/design-principles.md`.

## Options considered

| Tool | Source format | Pros | Cons |
|---|---|---|---|
| **CadQuery (Python)** | `.py` (plain text) | Diff-friendly, free, no account, AI-editable, STEP/STL export, real parametric, scriptable | OCP backend pins us to Python 3.10–3.11 (not the latest Python); learning curve if unfamiliar |
| Autodesk Fusion 360 | `.f3d` (binary) | Polished UI, large user base, plenty of tutorials | Binary source → useless in git, requires Autodesk account, free tier may shrink |
| OnShape | cloud doc | Browser-based, real Git-like document versioning | Cloud-dependent, requires account, can't grep the design from a terminal |
| FreeCAD | `.FCStd` (zipped XML, semi-text) | Free, offline, open source | Diffs are noisy, file format historically unstable across versions, GUI required |
| OpenSCAD | `.scad` (plain text) | Diff-friendly, scriptable, free | Mesh-only output, no STEP export → poor reusability for parts that may graduate to other tools |

## Decision

**CadQuery 2.7 in a Python 3.11 venv at the repo root.**

- `.py` files are the source of truth.
- `.step` and `.stl` are exported next to the `.py` and committed so non-Python reviewers can inspect geometry without standing up the toolchain.
- `.3mf` and slicer profile JSON come from Bambu Studio after slicer tuning — they capture print settings, not just geometry.
- Toolchain setup documented in `tools/cad/README.md`. One-time: `uv venv --python 3.11 .venv && uv pip install -r tools/cad/requirements.txt`.

## Consequences

**Positive:**
- Plain-text CAD source means PRs show real diffs and merges work as expected.
- AI assistants can edit geometry directly.
- Parametric block at the top of each part's `.py` lets us flip `BASE_W = 38.0` once and re-export — directly supports the scaled-manufacturing posture.

**Negative:**
- Anyone new joining the build needs the venv set up before they can re-export. Mitigated by committing `.step` and `.stl` so they can read geometry without running anything.
- CadQuery's GUI story is weak. We use the CLI + Bambu Studio for visual review; an SVG preview is exported per part as a sanity-check artifact.

**Known gotcha (worth surfacing here so it doesn't get rediscovered):** `cq.exporters.export(..., '.stl')` mutates the underlying `TopoDS_Compound`'s bounding box (the STL tessellation gets attached). Always read `mast.val().BoundingBox()` *before* the STL export, otherwise reported dimensions inflate by ~1.5 mm per axis. See `builds/v1/cad/gps-mast/gps-mast-v1.py` for the established order: read stats first, export second.

## Validation

First part shipped (`builds/v1/cad/gps-mast/gps-mast-v1.py`, 2026-05-05) — clean STEP and STL export, 38×38×100 mm bounding box matching the parametric inputs. Workflow works end-to-end.
