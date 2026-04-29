# Build v1 — Learning Vehicle

**Status:** 🟡 In design — parts ordering pending
**Goal:** Fly a 4-waypoint autonomous mission within 7 days of parts arrival
**Mission spec:** 18m × 18m square at 5m AGL, 2 m/s cruise, AUTO takeoff and land

## Quick links

- [Requirements](./requirements.md) — locked v0.3
- [BOM](./bom.md) — parts and SKUs to order
- [Tooling](./tooling.md) — tools to order
- [Assembly notes](./assembly/notes.md) — populated as we build
- [Firmware](./firmware/) — ArduCopter parameters and flashed binaries
- [Flight logs](./flight-logs/) — per-flight artifacts

## Test plan summary

| Gate | Status | Date |
|---|---|---|
| G1: Bench power-on | ⚪ | — |
| G2: RX bind + arming | ⚪ | — |
| G3: Motor direction + ESC cal | ⚪ | — |
| G4: IMU + compass cal | ⚪ | — |
| G5: GPS lock | ⚪ | — |
| G6: Tethered hover | ⚪ | — |
| G7: Free hover (STABILIZE) | ⚪ | — |
| G8: GPS position hold (LOITER) | ⚪ | — |
| G9: RTH test | ⚪ | — |
| G10: AUTO mission | ⚪ | — |

Update this table as gates pass. ⚪ = not yet, 🟡 = in progress, ✅ = passed, ❌ = failed.

## Week-1 schedule (estimate, parts-arrival-relative)

| Day | Activity |
|---|---|
| Day 0 | Order all parts (BOM + tooling). FAA registration + TRUST cert. Identify flight site. |
| Day 1–3 | Parts ship. Set up Mission Planner on Toughbook. Watch soldering primers. Print accessory parts. |
| Day 4 (parts arrive) | Solder motors to ESC, install RX, install GPS+compass. G1, G2 on bench. |
| Day 5 | G3 (motor direction), G4 (compass cal), G5 (GPS lock). Configure ArduCopter params. |
| Day 6 | G6 (tethered hover) → G7 (free STABILIZE) → G8 (LOITER). Field site. |
| Day 7 | G9 (RTH) → G10 (AUTO mission). 🎯 Target met. |

## Open work for owner

- [ ] FAA recreational registration ($5)
- [ ] TRUST certificate (free)
- [ ] Verify flight area is Class G airspace via B4UFLY
- [ ] Order parts per BOM
- [ ] Order tools per tooling.md
- [ ] Set up GitHub repo
