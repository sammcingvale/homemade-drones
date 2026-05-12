# v1 — CAD

Printed parts for the v1 airframe.

## Parts list

| Folder | Part | Filament | Status |
|---|---|---|---|
| `canopy/` | Top canopy + GPS/RX mount | PETG | ⚪ Not designed |
| `gps-mast/` | GPS mast (≥80mm tall, RF-transparent) | PETG | 🟡 v1 designed, awaiting print + fit-check |
| `antenna-mounts/` | ELRS receiver mount for BetaFPV ELRS Lite V1.2 Flat (×1) | TPU 95A | 🟡 v1 designed, awaiting print + fit-check |
| `battery-tray/` | Battery tray + Velcro strap loop | PETG | ⚪ Not designed |
| `motor-soft-mounts/` | Vibration-isolating motor mounts | TPU 95A | ⚪ Not designed |
| `standoffs/` | M3 frame standoffs (optional, can buy aluminum) | TPU 95A | ⚪ Not designed |

## Folder structure (per part)

Following `docs/repo-conventions.md`:

```
<part-name>/
├── README.md                              # design intent, mounting, fit notes
├── <part-name>-v1.py                      # source of truth (CadQuery / Python)
├── <part-name>-v1.step                    # exported from .py — kept in git for non-Python reviewers
├── <part-name>-v1.stl                     # exported from .py — direct slice in Bambu Studio
├── <part-name>-v1.3mf                     # slicer-ready, profile baked in (from Bambu Studio)
├── <part-name>-v1.slicer-profile.json     # exported Bambu Studio profile
└── notes.md                               # print orientation, supports, lessons
```

Increment the version (`v2`, `v3`) for any geometry change. Old versions stay — we keep history.

## CAD tool

[CadQuery](https://cadquery.readthedocs.io/) (parametric Python). `.py` files are source of truth, STEP and STL are exported artifacts. See `tools/cad/README.md` for env setup.

Why: plain-text, diff-friendly, branch-mergeable, AI-editable. STEP export is reusable in Fusion 360 / OnShape / FreeCAD if a part graduates later.

## Print parameters (Bambu P2S, 0.4mm stock nozzle)

### PETG defaults
- Nozzle: 240°C
- Bed: 70°C
- Layer: 0.2mm
- Walls: 4
- Infill: 30% gyroid
- Top/bottom layers: 5

### TPU 95A defaults
- Nozzle: 230°C
- Bed: 50°C
- Layer: 0.2mm
- Walls: 3
- Infill: 25% gyroid
- Print speed: ≤30 mm/s (TPU is slow, don't fight it)
- Retraction: minimize (stringy filament)

These are starting points. Tune per part; commit the tuned profile to the part's folder.
