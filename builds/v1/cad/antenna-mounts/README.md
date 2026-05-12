# Antenna mount

Holds the BetaFPV ELRS Lite V1.2 2.4GHz RX with Flat Antenna (`cat-006`) extended past the Source One V5 carbon frame edge for RF clearance to the operator.

## Quantity

**Quantity: 1.** The BetaFPV ELRS Lite RX (both Flat V1.2 and discontinued Tower variants) uses a single integrated SMD ceramic antenna soldered to the receiver PCB. No diversity pair. One module, one mount.

## SKU history

- v1 originally designed 2026-05-11 for the Tower variant (10×10×6mm).
- Tower variant went out of production at BetaFPV; build switched to Flat V1.2 (11×10×3mm) the same day. Three parameter values updated in the `.py` (`RX_W`, `RX_H`, slop unchanged); design intent unchanged.

## Geometry summary

| Dimension | Value | Notes |
|---|---|---|
| Total length | 52 mm | base center → far edge of cradle |
| Effective antenna offset | ~37 mm | base M3 hole → center of RX in cradle |
| Base | 15 × 15 × 3 mm | single M3 clearance hole at center |
| Boom | 22 × 8 × 4 mm | cantilever between base and cradle |
| Cradle | 15 × 14 × 7 mm outer | 12 × 11 × ∞ interior, walls 1.5 mm, open top and bottom |
| Volume | ~1.9 cm³ | ≈ 0.5 g in TPU 95A at typical 25% infill |

## Mounting interface

**Base (down):** single M3 clearance hole at base center. Designed to piggyback on a Source One V5 corner standoff — share the M3 bolt that holds the canopy down. Tighten the bolt, the antenna mount is held by friction against the canopy or top plate.

**Cradle (in):** friction-fit grip around the 11 × 10 × 3 mm RX module. 1 mm of clearance per axis (0.5 mm per side) — should hold the module firmly in TPU 95A without crushing it. If the fit is loose, reduce `RX_SLOP`; if it's too tight to insert, increase it.

**Top/bottom of cradle (open):** the integrated ceramic antenna points up through the open top. Solder pads on the RX face down through the open bottom. The 4-wire cable (5V, GND, RX, TX) exits the open bottom and routes back to the FC.

## Why this geometry

- **Boom length 22 mm.** Source One V5 top plate edge sits roughly 15–20 mm from a corner standoff; the boom extends the RX another ~10 mm past that edge. Empirically validates on first fit-check.
- **Cradle as a tube, not a box.** Open top is mandatory (the antenna sticks up); open bottom is intentional (cable exit + the print can run with no internal supports). TPU 95A wraps the RX on all 4 sides for friction grip.
- **Single M3 mount, not multi-bolt.** Two-bolt patterns would require a second standoff or a printed base wide enough to span two of them — adds mass and constrains canopy design. The TPU base + single bolt + friction against canopy is sufficient for a 0.47 g RX.
- **TPU 95A throughout.** The mount lives at the edge of the airframe and will be the first thing to hit grass / pavement / fence in any crash. PETG would snap. TPU bends and recovers.

## Files

| File | Role |
|---|---|
| `antenna-mount-v1.py` | source of truth (CadQuery) |
| `antenna-mount-v1.step` | exported STEP |
| `antenna-mount-v1.stl` | exported STL — direct slice in Bambu Studio |
| `antenna-mount-v1-preview.svg` | isometric preview, regenerable |
| `notes.md` | print orientation, slicer notes, lessons |

## Re-export

```bash
.venv/bin/python builds/v1/cad/antenna-mounts/antenna-mount-v1.py
```
