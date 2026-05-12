# Print notes — antenna mount

## Orientation

Print **flat on the bed** — base face down. The entire part is essentially a flat L-shaped extrusion; no overhangs steeper than the cradle's 4 vertical walls. No supports needed.

The cradle's open top and open bottom both face the Z-axis when printed flat (open top → +Z; open bottom → bed). The 11×11mm internal pocket of the cradle prints as a vertical hole — no bridging.

## Filament and slicer settings (Bambu P2S, 0.4 mm stock nozzle)

TPU 95A defaults from `builds/v1/cad/README.md` apply unmodified. Starting recipe:

| Setting | Value |
|---|---|
| Filament | Bambu TPU 95A HF, black (`cat-010`) |
| Nozzle | 230 °C |
| Bed | 50 °C |
| Layer height | 0.2 mm |
| Walls | 3 |
| Top/bottom layers | 4 |
| Infill | 25 % gyroid |
| Print speed | ≤30 mm/s |
| Retraction | minimize (1 mm or less) |
| Supports | **None** |
| Brim | 5 mm (small footprint + TPU benefits from extra bed adhesion) |

**External-spool feed required.** Bambu TPU 95A HF is **not** AMS-compatible (per `cat-010`). Load from the side spool holder on the P2S, not the AMS.

Estimated print time: ~20 min per part (from `requirements.md` §8). Tiny part, low mass.

## After-print fit-check

Before the canopy + RX are wired up:

1. M3 screw drops through the base hole without forcing. PETG-style hole sizing applies (3.4 mm hole + ~0.5% shrinkage).
2. The 11 × 10 × 3 mm BetaFPV ELRS Lite V1.2 RX (when received) slides into the cradle with light friction. Should hold the RX during gentle shaking but pop free with deliberate finger pressure. If too loose: reduce `RX_SLOP` in the `.py` and re-export. If too tight: increase it.
3. The 4-wire RX cable can pass through the open bottom of the cradle without getting pinched.

## Known assumptions to verify on first physical fit

- **RX module dimensions: 11 × 10 × 3 mm** (BetaFPV ELRS Lite V1.2 Flat). Confirmed from BetaFPV's product page on 2026-05-11. Verify on receipt — RFI shielding or solder pads can add a fraction of a millimeter that the spec sheet glosses over.
- **Source One V5 corner-standoff M3 pattern.** Standard 30.5 mm or arm-corner spacing varies slightly across Source One V5 manufacturer brandings (TBS / RDQ / Pyrodrone). The single center M3 hole is forgiving — anywhere a corner bolt sticks up, this mounts on it.
- **22 mm boom length.** Eyeballed from the Source One V5 top plate dimensions; may want to grow to 28–30 mm if the carbon edge ends up closer to the corner than I expect. Trivial parametric edit.

## Lessons

(Empty — fill in after the first print.)
