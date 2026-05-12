# Print notes — battery tray

## Orientation

Print **flat on the bed, plate side down**. Lips and end-stop wall face up. No supports.

The strap slots are vertical holes through the plate — no bridging required since they're cut all the way through. The lips and end stop are short (3 mm tall) and prismatic, so no overhangs.

## Filament and slicer settings (Bambu P2S, 0.4 mm stock nozzle)

PETG defaults from `builds/v1/cad/README.md` apply unmodified. Starting recipe:

| Setting | Value |
|---|---|
| Filament | Bambu PETG Basic, black (`cat-009`) |
| Nozzle | 240 °C |
| Bed | 70 °C |
| Layer height | 0.2 mm |
| Walls | 4 |
| Top/bottom layers | 5 |
| Infill | 30 % gyroid |
| Supports | **None** |
| Brim | 5 mm |

Estimated print time: ~1 h per `requirements.md` §8. The plate is the bulk of the print time.

## After-print fit-check

When the LiPo pack arrives:

1. Battery slides into the cradle from the open (XT60) end with ~0.5 mm clearance per side. Should not be tight.
2. End-stop wall fully stops the battery at the closed end (the XT60 lead has clearance through the open end).
3. Velcro strap (15–20 mm wide) passes through both slots without forcing.
4. With strap tightened, the battery is held firmly against the floor with no lateral wobble.

## VHB mounting procedure

When the frame's bottom plate arrives:

1. Clean both surfaces with isopropyl alcohol; let dry.
2. Apply two strips of 3M VHB (`cat: solder-6040` adjacent — VHB is uncataloged but in the BOM hardware list) to the **top face** of the tray, running long-axis, **between** the strap slots (do not cover the slots).
3. Press tray firmly to the underside of the frame's bottom carbon plate. Hold under firm pressure for 60 s.
4. Let cure 24 h before flying — VHB reaches full bond strength slowly.

## Known assumptions to verify on first physical fit

- **Battery dimensions: 76 × 36 × 33 mm.** Verified against multiple CNHL Black V2.0 1500mAh 4S 130C distributor listings 2026-05-11. Verify on receipt with calipers — pack-to-pack manufacturing variance can be ±1–2 mm.
- **No M3 bolt-through.** Reconsider only if the VHB mount turns out to be unreliable in flight. Probably won't.
- **Strap-slot positions (18 and 59 mm from closed end).** Chosen for roughly quarter/three-quarter placement along the battery. If the strap doesn't sit well, adjust `SLOT_MARGIN` in the `.py`.

## Lessons

(Empty — fill in after the first print.)
