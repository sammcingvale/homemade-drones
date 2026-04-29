# Drone Requirements — v1 build

**Version:** v0.3
**Status:** LOCKED for parts ordering
**Build target:** v1 (learning vehicle)
**Constraint:** flight-capable in <7 days from parts arrival
**Long-term:** scaled printing + assembly of identical units, eventually swarm-coordinated

---

## 0. Locked decisions

| # | Decision | Value | Status |
|---|---|---|---|
| 0.1 | Frame size (prop diameter) | 5" | LOCKED |
| 0.2 | Sub-250g target? | No (v1). Will target lower weights in subsequent builds. | LOCKED |
| 0.3 | Indoor / outdoor / both | Outdoor, GPS-available | LOCKED |
| 0.4 | Structural main plate | Purchased CF (Source One V5). Print accessories. | LOCKED |
| 0.5 | Autonomy scope for v1 | L1 — GPS waypoint mission (see §2.5) | LOCKED |
| 0.6 | Companion computer in v1? | No — defer to v3 | LOCKED |
| 0.7 | Onboard pilot-view video link? | **No, in any build.** Cameras allowed only for autonomy/mission data inputs. | LOCKED |
| 0.8 | FC firmware | ArduCopter (latest stable, ≥4.5) | LOCKED |
| 0.9 | Ground station | Mission Planner on Windows (used Toughbook CF-54) | LOCKED |
| 0.10 | Radio (TX) | RadioMaster Pocket (ELRS built-in) | LOCKED |
| 0.11 | Number of airframes for week 1 | 1 | LOCKED |
| 0.12 | Jurisdiction | US (FAA) | LOCKED |

---

## 1. Design principles

See `docs/design-principles.md` for cross-build principles. Build-specific notes:

- v1 prioritizes **time-to-flight** over manufacturability or performance.
- v1 uses standard, well-documented components so help is one Google query away.
- v1 builds the workflow: order → assemble → flash → bench-test → tethered → free flight → autonomous. Same workflow scales to v2+.

---

## 2. Mission profile

| Parameter | Value | Notes |
|---|---|---|
| Operating environment | Outdoor, open field, daylight | Park adjacent to operator |
| GPS available | Yes | Drives autonomy stack |
| Operating altitude (AGL) | <120m (US Part 107 ceiling) | v1 mission flies at 5m |
| Range from operator | <500m line-of-sight | ELRS easily covers |
| Endurance per sortie | 8–12 min hover max | Sets battery sizing |
| Mission payload (carried) | None | LOCKED |
| Speed envelope | 0–20 m/s typical | v1 mission flies at 2 m/s |
| Wind tolerance | <8 m/s sustained | Hard ceiling on 5" airframe |
| Weather | Dry only | No conformal coating in v1 |
| Day/night | Day only | No nav lights in v1 |
| Temperature | 0°C to 35°C ambient | LiPo limits |

**v2+ deferred:** rain/dust ingress, night ops, BVLOS, cold-soak, payload drop.

---

## 2.5 Autonomy roadmap

| Build | Level | Capability | Stack additions |
|---|---|---|---|
| **v1** | **L1 — Pre-programmed mission** | **GPS waypoint mission, manual abort, auto RTH on failsafe** | **ArduCopter AUTO mode, Mission Planner mission upload** |
| v2 | L1+ | Geofence, smart RTH, optical-flow position hold | + downward optical flow sensor |
| v3 | L2 — Reactive | Obstacle avoidance, GPS-denied hover (VIO), dynamic re-plan | + companion computer (RPi 5 / Jetson Orin Nano), ROS2, depth camera |
| v4 | L3 — Multi-vehicle | Swarm: formation, leader-follow, distributed task allocation | + mesh comms, ROS2 DDS, coordination logic |

### v1 mission spec

- **Pattern:** 4-waypoint square, 18m × 18m (≈ 20 yd × 20 yd)
- **Altitude:** 5m AGL, constant
- **Cruise speed:** 2 m/s (slow, observable, easy to abort)
- **Sequence:** Manual arm → AUTO-takeoff to 5m → WP1→WP2→WP3→WP4 (CCW from takeoff) → AUTO-RTH → AUTO-land
- **Total flight time:** ~90s

### v1 failsafe matrix

| Trigger | Response |
|---|---|
| RC link loss | RTH, then land |
| Battery <30% | RTH |
| Battery <20% | Land at current position |
| GPS loss >5s | Land at current position |
| Geofence breach | RTH to fence center |
| Pilot kill switch | Disarm immediately (motors stop) |

Failsafes configured in ArduCopter parameters (`firmware/params/v1-001.params`) and version-controlled.

---

## 3. Vehicle spec

| Slot | Spec |
|---|---|
| Class | Quadcopter, X-config |
| Frame | Source One V5 5" Base Kit |
| Motor-to-motor diagonal | 220mm |
| AUW target | 600–700g w/ 4S 1500mAh |
| AUW max (structural) | 900g |
| FC stack mounting | 30.5×30.5mm |

---

## 4. Propulsion

| Slot | Spec | Selection |
|---|---|---|
| Motors | 2207, ~1950KV (4S) | EMAX ECO II 2207 1900KV ×4 |
| Props | 5×4.3×3 (5-inch tri-blade) | HQProp T5x4.3x3 ×4 sets |
| ESC | 4-in-1, 55A, BLHeli_S | Bundled with FC stack |

Any 2207 motor in 1750–2000KV works. EMAX ECO II picked for cost + ubiquity. Don't agonize.

---

## 5. Power

| Slot | Spec | Selection |
|---|---|---|
| Chemistry | LiPo | |
| S-count | 4S | |
| Capacity | 1500 mAh | ~10 min hover |
| C-rating | 100C | |
| Connector | XT60 | |
| Charger | ToolkitRC M7 (built-in AC) | |
| Storage | LiPo bag, 3.8V/cell storage charge | |
| Field kit | 4× packs minimum | |

---

## 6. Avionics

| Slot | Spec | Selection | Notes |
|---|---|---|---|
| Flight controller + ESC | F405 stack, 30.5×30.5mm | SpeedyBee F405 V4 BLS 55A Stack | ArduCopter-supported, [official docs](https://ardupilot.org/copter/docs/common-speedybeef4-v3.html) |
| FC firmware | ArduCopter ≥4.5 | | Board ships with Betaflight — first flash via DFU |
| IMU | ICM-42688P | Onboard FC | |
| Barometer | Onboard FC | | |
| Magnetometer | External (on GPS module) | Bundled with M10Q-5883 GPS | NEVER use FC-internal mag |
| GPS + compass | u-blox M10 + QMC5883L | Matek M10Q-5883 | Mount on printed mast ≥80mm |
| Current/voltage sensor | Onboard ESC | | Required for ArduPilot battery failsafe |

**EMI / RF notes:**
- GPS mast ≥80mm. Non-negotiable.
- Magnetometer ≥150mm from high-current wires (mast-mounted solves this).
- ELRS RX antennas at 90° to each other, both extending past frame edges.
- Carbon fiber blocks RF — antennas must clear the frame in line-of-sight to operator.

---

## 7. Comms

| Link | Purpose | Selection | Range |
|---|---|---|---|
| RC control | Pilot input, failsafe | RadioMaster Pocket (ELRS) ↔ BetaFPV ELRS Lite RX | 2km+ |
| Telemetry | MAVLink ↔ Mission Planner | Holybro SiK Radio 915MHz pair | 1km+ |
| Video | **Not installed** | — | — |
| Swarm mesh | **Deferred to v4** | — | — |

---

## 8. Manufacturing — print plan

### v1 printed parts

| Part | Filament | Print time | Notes |
|---|---|---|---|
| Canopy / top plate | PETG | ~2h | Houses GPS, RX, telem |
| GPS mast (≥80mm) | PETG | ~30min | RF-transparent |
| Antenna mounts (×2) | TPU 95A | ~20min ea | Soft, won't snap |
| Battery tray + strap loop | PETG | ~1h | |
| Motor soft-mounts (×4) | TPU 95A | ~30min total | IMU vibration isolation |
| Standoffs (M3, ×4) | TPU 95A or aluminum | ~15min | Either works |

**Total print time: ~5h** on a Bambu P2S, single bed plate.

### Filament strategy

| Filament | Use case | v1 Required |
|---|---|---|
| **PETG** | Non-structural rigid parts | ✅ |
| **TPU 95A** | Soft mounts, antenna tubes | ✅ |
| **PA-CF** | Structural (v2+) | ❌ |
| **ASA** | Outdoor exposed parts (v2+) | ❌ |
| **PLA** | ❌ Do not use | ❌ |

### Printer config

- Bambu Lab P2S, AMS 2 Pro
- Stock 0.4mm nozzle for v1 (PETG + TPU only)
- Hardened nozzle deferred until v2 (when PA-CF enters)

### Print process discipline

- All parts version-controlled under `cad/<part>/` per repo conventions.
- STEP is source of truth. STL/3MF exported from STEP.
- Slicer profile committed alongside model.
- Print orientation noted in `notes.md` per part.
- No supports on production parts — design them out.

---

## 9. Regulatory & safety

US, FAA jurisdiction.

| Item | Requirement | Status |
|---|---|---|
| FAA recreational registration | Required >250g | Owner action — will complete day 1 |
| Remote ID | Required >250g since Sept 2023 | ArduPilot built-in broadcast |
| Part 107 | Commercial only | Not needed |
| Flight area | TRUST cert + Class G airspace | Owner action — will complete day 1 |
| LAANC | Controlled airspace only | Avoid for v1 |
| Insurance | Optional | AMA membership recommended |

Safety procedures: see `docs/safety-checklist.md`.

---

## 10. Test plan — gates

Each gate must pass before next attempted. Failed gate → debug, don't push through.

| Gate | Pass criterion | Tools | Estimated day |
|---|---|---|---|
| G1: Bench power-on | FC boots, no smoke, no overheat | Smoke stopper, IR thermometer | Day 4 |
| G2: RX bind + arming | All channels move correctly, arming gate passes | Mission Planner | Day 4 |
| G3: Motor direction + ESC cal | All 4 motors spin correct direction, DSHOT telem healthy | Props OFF | Day 5 |
| G4: IMU + compass cal | Cal completes, mag interference <30% | MP cal screens | Day 5 |
| G5: GPS lock | ≥10 sats, HDOP <1.5, position holds within 2m at rest | Open sky, 5+ min | Day 5 |
| G6: Tethered hover | Stable hover, no oscillation, throttle response linear | 2m tether to ground anchor | Day 6 |
| G7: Free hover (manual STABILIZE) | 30s stable hover at 2m, manual landing | Open field, observer | Day 6 |
| G8: GPS position hold (LOITER) | Holds within 3m for 60s | | Day 6 |
| G9: RTH test | Triggers RTH, returns within 5m of takeoff, lands | Manual abort ready | Day 7 |
| **G10: AUTO mission** | **4-waypoint 18m square, autonomous start to finish** | **MP mission upload** | Day 7 |

**G10 = week-1 target.** See `bom.md` for parts and `tooling.md` for required tools.

---

## 11. v2+ deferred items

Cataloged so we don't lose them.

- Printed structural main plate + arms in PA-CF
- Conformal coating for moisture resistance
- Companion computer (RPi 5 / Jetson Orin Nano) for vision-based autonomy
- VIO / SLAM stack (ROS2 + PX4 / ArduPilot + VINS-Fusion)
- Obstacle avoidance sensors (ToF, depth camera)
- Mesh comms for swarm
- Multi-vehicle coordination
- Night ops
- Payload mounts / data collection
- Field-swappable battery (tool-less)
- Production jig for assembly time-tracking

---

## 12. Bill of materials

See `bom.md` (in this folder).

---

## 13. Tooling

See `tooling.md` (in this folder).

---

## Changelog

- **v0.3** — Locked all open decisions from Section 13. Added 0.7 (no pilot-view video, ever), 0.8–0.12 (firmware, ground station, radio, build count, jurisdiction). Specified concrete SKUs in §4–§7. Added day-by-day estimates to test plan. Author: Claude. Status: LOCKED.
- **v0.2** — Added §2.5 autonomy roadmap, v1 mission spec, failsafe matrix. Locked 0.5. Removed crash-survivability driver.
- **v0.1** — Initial draft.
