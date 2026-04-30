# design principles

cross-build principles that apply to every drone build.

## scaled-manufacturing posture (from v1)

even though v1 is a learning vehicle, we bake in habits that scale.

- **no exotic sourcing.** every part available from ≥2 distributors. eventually target US-based distributors and vertically integrated where possible.
- **no hand-tuned firmware per unit.** firmware flash is a script. parameters are version-controlled per airframe revision, not per serial number.
- **print times scale.** no part exceeds 4h on a stock 0.4mm nozzle.
- **standard fasteners.** M3 for structure, M2 for electronics. single thread pitch only.
- **connector discipline.** XT60 battery, MR30 / PH 2.0 accessories, ELRS-standard pinout receiver.
- **replaceable wear items.** props, motors, FC swappable in <10 min field repair.
- **identical units.** two airframes of the same revision must be functionally interchangeable.

## build progression philosophy

| build | bias |
|---|---|
| v1 | **fly ASAP.** hybrid (purchased CF + printed accessories). standard parts, well-documented stack. |
| v2 | **iterate on print.** move structural parts to printed PA-CF. tighten assembly time. |
| v3 | **add autonomy depth.** companion computer, vision stack, GPS-denied. |
| v4 | **multiply.** swarm comms, coordination. optimize manufacturability. |

## test gating discipline

every build runs through the same 10 gates (G1–G10). a failed gate is always a debug step, never a "we'll fix it later."

## versioning

- requirements doc: `requirements.md` per build, with a `## changelog` section at the bottom.
- CAD: `/cad/<part>/v<n>/` — increment `n` for any geometry change. old versions stay.
- firmware params: `/firmware/params/<airframe_serial>.params` — committed before each flight.
- flight logs: `/flight-logs/<YYYY-MM-DD>_<flight_id>/` — bin file, telemetry, post-flight notes.

## decision logs

substantive design decisions get logged. format: short markdown file in `/docs/decisions/` titled `NNNN-decision-name.md` with date, context, options considered, decision, consequences. inspired by ADRs (Architecture Decision Records).
