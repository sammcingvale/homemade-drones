# Design Principles

Cross-build principles that apply to every drone we build. Updated when learnings warrant — but discipline matters more than perfection.

## Mass-manufacturing posture (from v1)

Even though v1 is a learning vehicle, we bake in habits that scale.

- **No exotic sourcing.** Every part available from ≥2 distributors. Eventually target US-based + vertically integrated where possible.
- **No hand-tuned firmware per unit.** Firmware flash is a script. Parameters are version-controlled per airframe revision, not per serial number.
- **Print times scale.** No part exceeds 4h on a stock 0.4mm nozzle.
- **Standard fasteners.** M3 for structure, M2 for electronics. Single thread pitch only.
- **Connector discipline.** XT60 battery, MR30 / PH 2.0 accessories, ELRS-standard pinout receiver.
- **Replaceable wear items.** Props, motors, FC swappable in <10 min field repair.
- **Identical units.** Two airframes of the same revision must be functionally interchangeable.

## Build progression philosophy

| Build | Bias |
|---|---|
| v1 | **Fly ASAP.** Hybrid (purchased CF + printed accessories). Standard parts, well-documented stack. |
| v2 | **Iterate on print.** Move structural parts to printed PA-CF. Tighten assembly time. |
| v3 | **Add autonomy depth.** Companion computer, vision stack, GPS-denied. |
| v4 | **Multiply.** Swarm comms, coordination. Optimize manufacturability. |

## Test gating discipline

Every build runs through the same 10 gates (G1–G10). A failed gate is a debug step, never a "we'll fix it later." Pushing through a failed gate is how drones crash and people get hurt.

## Versioning

- Requirements doc: `requirements.md` per build, with a `## Changelog` section at the bottom.
- CAD: `/cad/<part>/v<n>/` — increment `n` for any geometry change. Old versions stay.
- Firmware params: `/firmware/params/<airframe_serial>.params` — committed before each flight.
- Flight logs: `/flight-logs/<YYYY-MM-DD>_<flight_id>/` — bin file, telemetry, post-flight notes.

## Decision logs

Substantive design decisions get logged. Format: short markdown file in `/docs/decisions/` titled `NNNN-decision-name.md` with date, context, options considered, decision, consequences. Inspired by ADRs (Architecture Decision Records).
