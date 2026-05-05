# Telemetry Radio Pair — 915MHz SiK

**Catalog ID:** cat-007
**Status:** active
**Last verified:** 2026-05-05

## Abstract spec

- 915MHz band (US-legal). EU/UK builds use 433MHz instead.
- 100mW RF output (range ~1km, sufficient for v1 mission at <500m)
- SiK firmware (Silicon Labs Si1000-based or compatible STM32 reimplementation)
- USB end for ground station connection (Mission Planner / QGC)
- TTL UART end for FC connection (3.3V or 5V tolerant)
- MAVLink 2 protocol
- Sold as matched pair (pre-bound)
- ≤8g per radio

## Ranked SKUs

| Rank | Mfr part | Vendor | URL | Unit price (pair) | Notes |
|---|---|---|---|---|---|
| 1 | Holybro SiK Telemetry Radio V3 915MHz 100mW (pair) | GetFPV | https://www.getfpv.com/ | ~$60 | verify wattage variant |
| 2 | Holybro SiK Telemetry Radio V3 915MHz 100mW (pair) | Holybro direct | https://holybro.com/ | ~$59 | manufacturer-direct |
| 3 | RFD900x (US 915MHz) | mfr-direct | https://store.rfdesign.com.au/ | ~$200/pair | overkill for v1 — consider for v3+ long-range |

## Reorder guidance

Sold as a pair (one air radio + one ground radio). Reorder one full pair when pair is destroyed or lost.

Suggested trigger: on hand ≤ 0. Suggested order qty: 1.

## Notes

- **100mW is the right pick for v1.** 500mW costs more and runs hotter without range benefit at <500m. 1W is single-radio (you'd need to buy two), different product.
- Air radio mounts on the airframe; ground radio plugs into the Toughbook USB port.
- Antenna should be vertical and clear of carbon fiber for best link.
- For v3+ swarm work this won't be the comm link — swarm needs a mesh-capable radio. SiK is point-to-point only.
