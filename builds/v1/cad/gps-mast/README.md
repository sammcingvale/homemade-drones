# GPS mast

Holds the GNSS+compass module (`cat-005`, currently Holybro M10 GPS V2) ≥80 mm above the FC stack to clear high-current wiring and carbon RF shadow.

## Geometry summary

| Dimension | Value | Notes |
|---|---|---|
| Total height | 100 mm | base bottom → top platform top |
| Effective antenna height above base flange top | 97 mm | exceeds the 80 mm RF/EMI floor by 17 mm |
| Base flange | 38 × 38 × 3 mm | 4 × M3 clearance holes on 30.5 mm pattern |
| Shaft | 14 × 14 mm OD, 2 mm walls, 85 mm tall | `+Y` face open as a cable slot |
| Taper | 9 mm tall, 14×14 → 32×32 | 45° loft, prints support-free |
| Top platform | 32 × 32 × 3 mm | 4 × M3 clearance holes on 26 mm pattern |
| Volume | ≈ 17 cm³ | ≈ 6 g in PETG at 30% infill |

## Mounting interfaces

**Base (down):** 30.5 × 30.5 mm M3 pattern. Matches Source One V5 frame top plate / FC stack standard. Bolts pass through the canopy first if a printed canopy goes between mast and frame.

**Top (up):** 26 × 26 mm M3 pattern. **Assumed for Holybro M10 V2 — not yet measured against the physical part.** Verify on receipt; if wrong, edit `TOP_HOLE_PATTERN` and re-export. This is parametric so the change is one-line.

## Cable routing

Cable enters through the 10 × 10 mm hole in the base flange, travels up the hollow shaft, and exits through the 10 × 10 mm hole in the top platform to the GPS connector.

The `+Y` face of the shaft is fully open along its height. This is intentional: it means the cable does not have to be threaded through a closed tube during assembly, and the slot prints with no internal supports. The slot also lets the shaft be printed support-free upright.

## Why these choices

- **Square cross-section over round.** Easier to print upright (vertical walls), aligns naturally with M3 hole patterns, simpler parametric model.
- **Hollow with a slot, not solid.** Mass matters; an 80 mm solid PETG mast is wasted weight.
- **45° taper rather than a flat cantilever.** A 32 mm-wide platform overhanging a 14 mm shaft would need supports under the platform. The 9 mm taper is exactly tall enough to keep the underside at ≤45° and prints cleanly without supports.
- **PETG, not PA-CF.** RF-transparent (PA-CF would attenuate L-band GPS signals); structural strength isn't the constraint here, mass and antenna clearance are.

## Files

| File | Role |
|---|---|
| `gps-mast-v1.py` | Source of truth (CadQuery / Python). Edit this and re-export. |
| `gps-mast-v1.step` | STEP export — reusable in any CAD package. |
| `gps-mast-v1.stl` | Mesh export — direct slice in Bambu Studio. |
| `gps-mast-v1-preview.svg` | Quick isometric preview, regenerable from the `.py`. |
| `notes.md` | Print orientation, slicer settings, lessons learned. |

## Re-export

```bash
.venv/bin/python builds/v1/cad/gps-mast/gps-mast-v1.py
```

See `tools/cad/README.md` for the venv setup.
