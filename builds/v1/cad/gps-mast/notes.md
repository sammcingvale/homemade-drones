# Print notes — gps-mast

## Orientation

Print **upright**, base flange flat on the bed.

- All vertical walls of the shaft print without supports.
- The 45° taper from shaft to top platform stays at or under the support-free angle (Bambu defaults are fine).
- The `+Y` cable slot is a vertical opening, so it doesn't need bridging.

Do not lay it on its side. The square cross-section becomes a horizontal overhang and one of the wall faces ends up unsupported.

## Filament and slicer settings (Bambu P2S, 0.4 mm stock nozzle)

PETG defaults from `builds/v1/cad/README.md` apply unmodified. Starting recipe:

| Setting | Value |
|---|---|
| Filament | PETG, generic |
| Nozzle | 240 °C |
| Bed | 70 °C |
| Layer height | 0.2 mm |
| Walls | 4 |
| Top/bottom layers | 5 |
| Infill | 30 % gyroid |
| Supports | **None** (design is support-free) |
| Brim | 5 mm (small base footprint, prevents detachment on a 100 mm-tall print) |

Estimated print time: ~30 min per the requirements doc; verify on first slice.

## After-print fit-check

Before unboxing the rest of the build:

1. M3 screws fit through both the base and top hole patterns without forcing.
2. Mounting pattern aligns with the Source One V5 top plate (base) and the GPS module (top).
3. GPS UART cable + connector pass through the 10×10 mm channel.
4. `+Y` slot is wide enough to lay the cable in without flexing the shaft.

## Known assumptions to verify on first physical fit

- **Top hole pattern is 26 mm.** Assumed from typical Holybro M10 module pinouts; not measured. If wrong, edit `TOP_HOLE_PATTERN` in the `.py` and bump to `gps-mast-v2`.
- **Base hole pattern is 30.5 mm.** Standard FC stack pattern, also used by Source One V5 top plate. Verified from the requirements doc, not measured against the actual frame.
- **PETG creep is acceptable for this part.** Mast lives away from heat sources; ambient operation only. PETG creep onset is around 75 °C, well above any temperature this part sees.

## Lessons

(Empty — fill in after the first print.)
