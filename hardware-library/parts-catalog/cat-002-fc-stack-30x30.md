# 30×30mm FC + 4-in-1 ESC Stack (ArduPilot-supported)

**Catalog ID:** cat-002
**Status:** active
**Last verified:** 2026-05-11

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
| 1 | Kakute H7 v1.5 + Tekko32 F4 4in1 50A ESC Stack | Holybro direct | https://holybro.com/products/kakute-h7-v1-stacks | $124.99 | **promoted from rank-3 on 2026-05-11** after SpeedyBee F405 V4 went OOS across all distributors. Variant selector at checkout: pick "Kakute H7 v1.5 / Tekko32 F4 4in1 50A ESC". 65A "Metal" variant exists at $149.99 — overkill for v1's 5"/4S build. |
| 2 | SpeedyBee F405 V4 BLS 55A 30x30 Stack | GetFPV | https://www.getfpv.com/speedybee-f405-v4-stack-f4-v4-fc-55a-blheli-s-esc-30x30.html | $93.99 | cheaper but OOS at GetFPV and Pyrodrone as of 2026-05-11. Earlier rank-1; demoted when stock disappeared. |
| 3 | SpeedyBee F405 V3 BLS 50A 30x30 Stack | GetFPV / Pyrodrone | (verify at order time) | ~$80–90 | older revision, same form factor and ArduPilot family. Use if V4 stays OOS and Kakute is also unavailable. |

## Reorder guidance

Suggested trigger: on hand ≤ 1. Suggested order qty: 1.

## Notes

- ArduCopter target name depends on the SKU. Verify the target before flashing:
  - Kakute H7 v1.5 (rank-1): `KakuteH7` — `https://firmware.ardupilot.org/Copter/stable/KakuteH7/`
  - SpeedyBee F405 V4 (rank-2): `SpeedyBeeF4V4` — `https://firmware.ardupilot.org/Copter/stable/SpeedyBeeF4V4/`
  - SpeedyBee F405 V3 (rank-3): `SpeedyBeeF4V3`
- First-flash procedure differs by vendor. SpeedyBee stacks ship with Betaflight and need DFU + STM32CubeProgrammer for the first ArduCopter flash. Holybro Kakute stacks typically ship with a bootloader pre-installed; verify what firmware (if any) is on the board on receipt before deciding the flash path. See `builds/v1/firmware/README.md`.
- Tekko32 4in1 ESCs ship with AM32 firmware (modern open-source successor to BLHeli_32). Supports DSHOT600 and bidirectional DSHOT out of the box.
- Spare stack recommended for first-builders (cooked pads happen). v1 BOM includes one.
- 6S-capable (Kakute H7) but we run 4S in v1. Don't mismatch motor KV with battery S-count.
