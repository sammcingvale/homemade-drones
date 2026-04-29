# Safety Checklist

Read before every assembly session and every flight session. Violation of any rule = stop work.

## Workshop / assembly

- [ ] Smoke stopper between battery and PDB on first power-up of any airframe revision.
- [ ] Multimeter checks: continuity on all solder joints, no shorts between VCC and GND, before first power-up.
- [ ] Props OFF for all bench tests (G1–G5). Props go on at G6 (tethered hover).
- [ ] LiPo bag in use any time a battery is connected and unattended (charging, storage, transport).
- [ ] Class D fire extinguisher or sand bucket within reach during any LiPo charging.
- [ ] No charging unattended. Period.
- [ ] Eye protection during any soldering or first power-up.
- [ ] Soldering iron returned to stand between joints, not laid on bench.
- [ ] Storage charge LiPos to 3.8V/cell if not flying within 48h.

## Pre-flight

- [ ] FAA registration current (>250g recreational drones).
- [ ] Remote ID broadcasting (FC firmware-based or external module).
- [ ] TRUST certificate on operator.
- [ ] Flight area is Class G airspace (verified with B4UFLY app).
- [ ] No people, animals, or property inside the planned flight envelope + 20m buffer.
- [ ] Wind <8 m/s sustained for 5" airframe.
- [ ] Battery storage voltage checked, packs are at 4.20V/cell ±0.05V before flight.
- [ ] Props inspected — no nicks, cracks, or imbalance.
- [ ] Motors free of debris, spin freely by hand.
- [ ] All M3 frame screws thread-locked and tight.
- [ ] GPS lock acquired (≥10 sats, HDOP <1.5) before arming for autonomous mission.
- [ ] Failsafe behavior verified by simulating RC loss before any autonomous flight.
- [ ] Geofence configured and uploaded.
- [ ] Kill switch tested on the bench before flight.
- [ ] Observer present and aware of flight plan.

## In-flight

- [ ] Pilot keeps hand on kill switch for entire flight.
- [ ] Autonomous mode never engaged on first flight of a build — always start in STABILIZE/LOITER and earn AUTO.
- [ ] Abort criteria pre-agreed: any unexpected behavior → switch to STABILIZE → land manually.

## Post-flight

- [ ] Battery disconnected before approaching the airframe.
- [ ] Flight log downloaded and saved to `/builds/vN/flight-logs/<date>_<id>/` before next flight.
- [ ] Visual inspection: motors, props, frame, electronics for damage.
- [ ] Battery temp checked — if >50°C, allow to cool before recharging.

## After a crash

- [ ] **Do not recharge the crash battery for 30 min.** Watch for puffing/smoke.
- [ ] Photograph crash site and damage before moving anything.
- [ ] Record crash conditions in flight log directory (`crash-notes.md`).
- [ ] Disposition the LiPo: if puffed, dented, or hot — saltwater discharge + safe disposal. Don't reuse.
- [ ] No further flights until root cause identified and documented.
