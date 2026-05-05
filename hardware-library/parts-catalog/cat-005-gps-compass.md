# GNSS + Compass Module (mast-mountable)

**Catalog ID:** cat-005
**Status:** active
**Last verified:** 2026-05-05

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
| 1 | Holybro M10 GPS V2 (IP67, 10-pin JST GHR) | GetFPV | https://www.getfpv.com/ | ~$45 | verify exact SKU and stock |
| 2 | Holybro M10 GPS V2 | Holybro direct | https://holybro.com/products/m10-gps | ~$45 | manufacturer-direct fallback |
| 3 | Holybro M9N GPS | GetFPV | https://www.getfpv.com/ | ~$40 | older chip, identical interface, fine for v1 |

## Reorder guidance

Suggested trigger: on hand ≤ 1. Suggested order qty: 1.

## Notes

- **Replaced Matek M10Q-5883 (EOL as of 2026 per Matek).** Holybro M10 V2 is the current-production equivalent with bonus IP67 rating.
- Cable connector: confirm pinout matches SpeedyBee F405 V4 GPS pads. Holybro ships with bare-end or JST GHR depending on SKU; expect to clip and resolder for our FC.
- Compass orientation: ArduPilot may require `COMPASS_ORIENT=6 (Yaw270)` per Holybro docs.
- Mast height ≥80mm. **Non-negotiable for clean fix and low mag interference.**
- v3 may upgrade to RTK-capable module (Holybro H-RTK F9P) for cm-precision positioning.
