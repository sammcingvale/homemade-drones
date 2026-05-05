# homemade-drones

at-home, at-scale drone swarms. drones, lots of drones.

## repo layout

```
drone-program/
├── docs/                    # cross-build documentation
│   ├── design-principles.md
│   ├── safety-checklist.md
│   └── repo-conventions.md
├── tools/                   # scripts shared across builds
├── hardware-library/        # reusable parts catalog, kits, CAD
│   ├── parts-catalog/       # abstract part specs + ranked SKUs + reorder guidance
│   └── kits/                # packing lists for field/bench operations
└── builds/
    ├── v1/                  # build #1 — learning vehicle, fly ASAP
    │   ├── README.md        # build summary + status
    │   ├── requirements.md  # frozen requirements doc for this build
    │   ├── bom.md           # bill of materials (references catalog by cat-NNN)
    │   ├── tooling.md       # tools required to assemble
    │   ├── cad/             # 3D models — one folder per part
    │   ├── firmware/        # ArduCopter firmware + parameters
    │   ├── assembly/        # assembly notes + build photos
    │   ├── flight-logs/     # per-flight logs and post-flight notes
    │   └── post-mortem.md   # written after build is retired
    ├── v2/                  # (future)
    └── v3/                  # (future)
```

## build status

| build | goal | status | flight count |
|---|---|---|---|
| v1 | L1 autonomy — GPS waypoint mission | 🟡 in design | 0 |
| v2 | L1+ — geofence, optical-flow position hold | ⚪ not started | — |
| v3 | L2 — vision-based autonomy, GPS-denied | ⚪ not started | — |
| v4 | L3 — swarm coordination | ⚪ not started | — |

## per-build philosophy

each `builds/vN/` folder is a complete, self-contained snapshot of that drone build. requirements, BOM, CAD, firmware, and flight logs live with the build they belong to. when v2 starts, we copy v1's contents as a starting point and iterate — old builds stay frozen for reference and post-mortem analysis.

components that prove themselves across multiple builds graduate to `hardware-library/`.

## getting started

if you're cloning fresh:
1. read `docs/design-principles.md` and `docs/safety-checklist.md`.
2. open the most recent active build's `README.md` for current status.
3. never skip a gate in the test plan. failed gate → debug, don't push through.
