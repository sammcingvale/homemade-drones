# safety checklist

read before every assembly session and every flight session. violation of any rule = stop work.

## workshop / assembly

- [ ] smoke stopper between battery and PDB on first power-up of any airframe revision.
- [ ] multimeter checks: continuity on all solder joints, no shorts between VCC and GND, before first power-up.
- [ ] props OFF for all bench tests (G1–G5). props go on at G6 (tethered hover).
- [ ] LiPo bag in use any time a battery is connected and unattended (charging, storage, transport).
- [ ] Class D fire extinguisher or sand bucket within reach during any LiPo charging.
- [ ] no charging unattended. period.
- [ ] eye protection during any soldering or first power-up.
- [ ] soldering iron returned to stand between joints, not laid on bench.
- [ ] storage charge LiPos to 3.8V/cell if not flying within 48h.

## pre-flight

- [ ] FAA registration current (>250g recreational drones).
- [ ] remote ID broadcasting (FC firmware-based or external module).
- [ ] TRUST certificate on operator.
- [ ] flight area is Class G airspace (verified with B4UFLY app).
- [ ] no people, animals, or property inside the planned flight envelope + 20m buffer.
- [ ] wind <8 m/s sustained for 5" airframe.
- [ ] battery storage voltage checked, packs are at 4.20V/cell ±0.05V before flight.
- [ ] props inspected — no nicks, cracks, or imbalance.
- [ ] motors free of debris, spin freely by hand.
- [ ] all M3 frame screws thread-locked and tight.
- [ ] GPS lock acquired (≥10 sats, HDOP <1.5) before arming for autonomous mission.
- [ ] failsafe behavior verified by simulating RC loss before any autonomous flight.
- [ ] geofence configured and uploaded.
- [ ] kill switch tested on the bench before flight.
- [ ] observer present and aware of flight plan.

## in-flight

- [ ] pilot keeps hand on kill switch for entire flight.
- [ ] autonomous mode never engaged on first flight of a build — always start in STABILIZE/LOITER and earn AUTO.
- [ ] abort criteria pre-agreed: any unexpected behavior → switch to STABILIZE → land manually.

## post-flight

- [ ] battery disconnected before approaching the airframe.
- [ ] flight log downloaded and saved to `/builds/vN/flight-logs/<date>_<id>/` before next flight.
- [ ] visual inspection: motors, props, frame, electronics for damage.
- [ ] battery temp checked — if >50°C, allow to cool before recharging.

## after a crash

- [ ] **do not recharge the crash battery for 30 min.** watch for puffing/smoke.
- [ ] photograph crash site and damage before moving anything.
- [ ] record crash conditions in flight log directory (`crash-notes.md`).
- [ ] disposition the LiPo: if puffed, dented, or hot — saltwater discharge + safe disposal. don't reuse.
- [ ] no further flights until root cause identified and documented.
