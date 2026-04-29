# tools/

Cross-build scripts and utilities.

Empty for v1. Candidates as they emerge:

- `flash-firmware.sh` — automate ArduCopter flash via DFU + STM32CubeProgrammer CLI.
- `upload-mission.py` — pymavlink-based mission upload for repeatable test patterns.
- `param-diff.py` — compare two `.params` files and produce a diff report.
- `log-convert.sh` — wrap mavlogdump for batch `.bin` → `.csv` conversion.
- `bench-test.py` — automated G1–G5 checks via MAVLink.

When something gets done by hand more than twice, it gets a script here.
