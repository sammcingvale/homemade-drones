# v1 — Flight Logs

One folder per flight. Naming: `<YYYY-MM-DD>_<flight-id>_<short-description>/`.

## Per-flight folder contents

```
2025-12-04_001_first-tethered-hover/
├── notes.md                  # written before + after the flight
├── mission.waypoints         # if it was an AUTO mission
├── log.bin                   # raw ArduPilot dataflash log (gitignored if >10MB)
├── log.csv                   # converted log (committed)
├── log.tlog                  # MAVLink telemetry log (committed)
├── pre-flight.params         # exact param dump used for this flight
└── photos/                   # any post-flight photos (damage, screenshots, etc.)
```

## notes.md template

```markdown
# Flight 001 — first tethered hover

**Date:** 2025-12-04
**Location:** [park name]
**Pilot:** [your name]
**Observer:** [name]
**Wind:** ~3 m/s NW
**Battery:** CNHL #1, started 16.78V, ended 16.12V

## Plan

[what we intended to do]

## Result

[what actually happened]

## Issues

[any anomalies, even minor]

## Action items

[anything to fix before next flight]

## Gates passed

- [ ] G6: Tethered hover
```

## Log conversion

Raw `.bin` → `.csv`:
- Mission Planner: DataFlash Logs → "Create Matlab File" or "Pull This Log via MavLink".
- Or `mavlogdump.py` from pymavlink.

We commit the `.csv` and `.tlog` for grep-ability and small size; `.bin` is gitignored unless we add Git LFS later.
