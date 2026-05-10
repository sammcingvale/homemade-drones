# GNSS + Compass Module (mast-mountable)

**Catalog ID:** cat-005
**Status:** active
**Last verified:** 2026-05-10

## Abstract spec

- u-blox M9N or M10 GNSS chip (M10 preferred for v3+ vision-augmented autonomy)
- Multi-constellation: GPS + GLONASS + Galileo + BeiDou
- Onboard magnetometer (IST8310, QMC5883L, or RM3100 acceptable)
- ≥25×25mm patch antenna
- Rechargeable backup battery (warm-start support)
- ArduPilot-supported (PX4 1.14+, ArduPilot 4.3+, INAV 5.0+)
- UBlox UBX protocol over UART, I²C for compass
- Compatible with mast-mounting (≥80mm above FC required for clean signal + low mag interference)
- Sub-15g preferred for 5" airframe

## Ranked SKUs

| Rank | Mfr part | Vendor | URL | Unit price | Notes |
|---|---|---|---|---|---|
| 1 | Holybro M10 GPS V2 (IP67, 10-pin JST GHR) | Holybro direct | https://holybro.com/products/m10-gps | ~$45 | **GetFPV does not carry the V2** — manufacturer-direct is the only V2 source as of 2026-05-10 |
| 2 | Holybro M10 GPS Standard (no IP67) | GetFPV | https://www.getfpv.com/ | $61.49 | older SKU, lacks IP67; functionally fine for v1 dry-only ops. OOS at GetFPV 2026-05-10. Verify exact URL at order time. |
| 3 | Holybro M9N GPS | GetFPV | https://www.getfpv.com/ | ~$40 | older chip, identical interface; verify URL at order time |

## Reorder guidance

Suggested trigger: on hand ≤ 1. Suggested order qty: 1.

## Notes

- **Replaced Matek M10Q-5883 (EOL as of 2026 per Matek).** Holybro M10 V2 is the current-production equivalent with bonus IP67 rating.
- **Vendor concentration risk noted.** Rank-1 (Holybro-direct) is single-source for the V2 SKU. The M10 Standard at GetFPV is a viable fallback for v1 since v1 is dry-only and IP67 is not in our abstract spec — but it's a different SKU, not a parallel vendor. If both sources go OOS, the rank-3 M9N is the last fallback. Revisit if the V2 stays single-vendor through v2.
- Cable connector: confirm pinout matches SpeedyBee F405 V4 GPS pads. Holybro ships with bare-end or JST GHR depending on SKU; expect to clip and resolder for our FC.
- Compass orientation: ArduPilot may require `COMPASS_ORIENT=6 (Yaw270)` per Holybro docs.
- Mast height ≥80mm. **Non-negotiable for clean fix and low mag interference.**
- v3 may upgrade to RTK-capable module (Holybro H-RTK F9P) for cm-precision positioning.
