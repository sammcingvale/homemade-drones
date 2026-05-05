# 30×30mm FC + 4-in-1 ESC Stack (ArduPilot-supported)

**Catalog ID:** cat-002
**Status:** active
**Last verified:** 2026-05-05

## Abstract spec

- 30.5×30.5mm mounting (4mm hole pattern)
- F4 (STM32F405) MCU minimum; F7 or H7 acceptable
- Listed in ArduPilot's [supported autopilots](https://ardupilot.org/copter/docs/common-autopilots.html). Non-negotiable.
- ICM-42688P or equivalent gyro
- Onboard barometer (BMP280 or better)
- 4-in-1 ESC bundled, ≥45A continuous, BLHeli_S or BLHeli_32 / AM32, DSHOT600 minimum
- Bidirectional DSHOT preferred (RPM filtering)
- USB-C connector
- Onboard current sensor (for ArduPilot battery failsafes)
- Dual BEC (5V + 9V) preferred for peripheral powering

## Ranked SKUs

| Rank | Mfr part | Vendor | URL | Unit price | Notes |
|---|---|---|---|---|---|
| 1 | SpeedyBee F405 V4 BLS 55A 30x30 Stack | GetFPV | https://www.getfpv.com/speedybee-f405-v4-bls-55a-30x30-stack.html | ~$94 | OOS as of 2026-05-04 — verify |
| 2 | SpeedyBee F405 V4 BLS 55A 30x30 Stack | Pyrodrone | https://pyrodrone.com/ | ~$90 | check stock |
| 3 | SpeedyBee F405 V4 BLS 55A 30x30 Stack | Amazon (SpeedyBee storefront) | Amazon search | varies | use only if mfr-fulfilled |

## Reorder guidance

Suggested trigger: on hand ≤ 1. Suggested order qty: 1.

## Notes

- Board ships with Betaflight. **First-time flash to ArduCopter requires DFU mode + STM32CubeProgrammer.** See `builds/v1/firmware/README.md`.
- ArduCopter target name: `SpeedyBeeF4V4` (firmware folder name on firmware.ardupilot.org).
- Spare stack recommended for first-builders (cooked pads happen). v1 BOM includes one.
- 6S-capable but we run 4S in v1. Don't mismatch motor KV with battery S-count.
