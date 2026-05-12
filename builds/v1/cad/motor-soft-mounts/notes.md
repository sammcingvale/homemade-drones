# Print notes — motor soft-mount

## Orientation

Print **flat on the bed**, pad face down. No supports, no overhangs (it's a disc).

Pack 4 copies onto the bed for a single print job — each is 28 mm OD and the parts are independent. Bed plate easily fits all 4 with brim spacing.

## Filament and slicer settings (Bambu P2S, 0.4 mm stock nozzle)

TPU 95A defaults from `builds/v1/cad/README.md` apply unmodified.

| Setting | Value |
|---|---|
| Filament | Bambu TPU 95A HF, black (`cat-010`) |
| Nozzle | 230 °C |
| Bed | 50 °C |
| Layer height | 0.2 mm |
| Walls | 3 |
| Top/bottom layers | 4 |
| Infill | 25 % gyroid |
| Print speed | ≤ 30 mm/s |
| Retraction | minimize |
| Supports | None |
| Brim | 3 mm (small part — extra adhesion margin) |

**External-spool feed required.** Bambu TPU 95A HF is not AMS-compatible (per `cat-010`).

Estimated print time: ~5 min per pad → ~20 min for the v1 set of 4.

## After-print fit-check

When motors and frame arrive:

1. M3 SHCS passes through the 3.4 mm holes without forcing.
2. Pattern aligns to motor's M3 holes and arm's M3 holes (both should be 16 × 16 mm).
3. Motor base sits flush on the pad (pad's 28 mm OD matches motor base).
4. Bearing boss / shaft on motor underside clears the 10 mm center bore.
5. With all 4 M3 screws hand-tight, motor sits firmly on the arm with the TPU slightly compressed (1.8 mm gap, down from 2.0 mm nominal). No wobble.

## Known assumptions to verify on first physical fit

- **Hole pattern 16 × 16 mm.** Per `cat-003` abstract spec, both the EMAX ECO II 2207 and Source One V5 arms use this pattern. Verify on receipt — some 2207 motors are 19 × 19 mm and some arms support both. If the actual motor or arm uses 19 × 19, change `HOLE_PATTERN` to 19 in the `.py` and re-export.
- **Motor base 28 mm OD.** Typical for 2207-class motors. Measure with calipers when motors arrive; if smaller, the pad will overhang slightly (cosmetic, not functional). If larger, the pad will undersize and may not fully cushion — reduce `MOUNT_OD` to match.
- **Bearing boss < 10 mm.** Generous. Verify by visual inspection that nothing protruding from the motor base hits the pad inside the 10 mm bore.

## Lessons

(Empty — fill in after the first print.)
