# Battery tray

PETG cradle for the v1 LiPo (CNHL Black V2.0 1500mAh 4S 130C, `cat-008`). Mounts to the underside of the Source One V5 bottom carbon plate via 3M VHB tape, constrains the battery laterally with two side lips and one end stop, and passes a Velcro strap through two slots in the floor so the strap wraps over the top of the battery.

## Geometry summary

| Dimension | Value | Notes |
|---|---|---|
| Plate footprint | 79 × 40 mm | sized to battery 76 × 36 mm + 1 mm slop + lip thicknesses |
| Total height | 6 mm | 3 mm plate + 3 mm lip/end-stop walls |
| Cradle interior | 77 × 37 mm | with 3 mm-tall walls on 3 sides (XT60 end is open) |
| Strap slots | 5 × 20 mm × 2 | through-cuts at 18 mm and 59 mm from the closed end |
| Volume | ~9.8 cm³ | ≈ 12 g in PETG at 30 % infill |

## Battery dimensions (verified)

| Spec | Value | Source |
|---|---|---|
| Length | 76 mm | CNHL Black V2.0 1500mAh 4S 130C product listings, 2026-05-11 |
| Width | 36 mm | same |
| Height | 33 mm | same |
| Weight | 164 g | same |

Note: 33 mm height exceeds `cat-008`'s 30 mm envelope spec by 3 mm. The envelope was too tight; the actual pack fits the build but the catalog spec line is worth a refresh on the next catalog revision.

## Mounting interface

**Top face (up):** flat, prepared for **3M VHB tape**. Apply two strips (~half-width each, running long-axis) under the plate floor, between the strap slots. Press onto the underside of the Source One V5 bottom carbon plate.

No M3 bolt-through holes by design. Source One V5 brandings (TBS / RDQ / Pyrodrone) have slightly different bottom-plate hole patterns; VHB is frame-agnostic and removable for v2 iteration.

**Cradle (in):** battery slides in from the open (XT60) end, butts against the end-stop wall on the closed end. Velcro strap passes up through the rear slot, over the battery, and back down through the front slot.

## Why these choices

- **Sized to verified pack dimensions, not the catalog envelope.** The cat-008 envelope (≤90 × 35 × 30 mm) under-specs the actual 76 × 36 × 33 mm pack on two axes. Designing to envelope would have produced a tray the battery couldn't sit in.
- **One end stop, not two.** The XT60 lead has to exit somewhere; the open end is that side. A second end stop would require feeding the battery in through a slot.
- **PETG, not TPU.** The tray is rigid by design — it transfers the battery's mass through to the frame and keeps the pack from sliding under maneuver. Soft mounting belongs on the motors (cat: motor-soft-mounts), not the battery.
- **Two through-slots, not strap loops.** Slots cut clean through the plate. Loops would need extra TPU material on the underside and would interfere with the VHB adhesion plane.

## Files

| File | Role |
|---|---|
| `battery-tray-v1.py` | source of truth (CadQuery) |
| `battery-tray-v1.step` | exported STEP |
| `battery-tray-v1.stl` | exported STL |
| `battery-tray-v1-preview.svg` | isometric preview |
| `notes.md` | print orientation, slicer notes, lessons |

## Re-export

```bash
.venv/bin/python builds/v1/cad/battery-tray/battery-tray-v1.py
```
