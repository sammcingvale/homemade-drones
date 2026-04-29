# v1 — CAD

Printed parts for the v1 airframe.

## Parts list

| Folder | Part | Filament | Status |
|---|---|---|---|
| `canopy/` | Top canopy + GPS/RX mount | PETG | ⚪ Not designed |
| `gps-mast/` | GPS mast (≥80mm tall, RF-transparent) | PETG | ⚪ Not designed |
| `antenna-mounts/` | ELRS receiver antenna tubes (×2) | TPU 95A | ⚪ Not designed |
| `battery-tray/` | Battery tray + Velcro strap loop | PETG | ⚪ Not designed |
| `motor-soft-mounts/` | Vibration-isolating motor mounts | TPU 95A | ⚪ Not designed |
| `standoffs/` | M3 frame standoffs (optional, can buy aluminum) | TPU 95A | ⚪ Not designed |

## Folder structure (per part)

Following `docs/repo-conventions.md`:

```
<part-name>/
├── README.md                              # design intent, mounting, fit notes
├── <part-name>-v1.step                    # source of truth (parametric CAD export)
├── <part-name>-v1.3mf                     # slicer-ready file (with profile baked in)
├── <part-name>-v1.stl                     # mesh export (optional, for non-Bambu printers)
├── <part-name>-v1.slicer-profile.json     # exported Bambu Studio profile
└── notes.md                               # print orientation, supports, lessons
```

Increment the version (`v2`, `v3`) for any geometry change. Old versions stay — we keep history.

## CAD tool recommendation

Any parametric tool works. Suggested: **Autodesk Fusion 360** (free for personal use, good ecosystem) or **OnShape** (free, browser-based, great Git-like versioning). FreeCAD is OK but rougher. Avoid mesh-only tools (Tinkercad, Blender) for structural parts — STEP export matters for reuse.

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
