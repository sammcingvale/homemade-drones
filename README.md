# drone-program

Self-built autonomous drone program. Long-term goal: drone swarms.

## Repo layout

```
drone-program/
├── docs/                    # Cross-build documentation
│   ├── design-principles.md
│   ├── safety-checklist.md
│   └── repo-conventions.md
├── tools/                   # Scripts shared across builds
├── hardware-library/        # Reusable CAD components (populated as we go)
└── builds/
    ├── v1/                  # Build #1 — learning vehicle, fly ASAP
    │   ├── README.md        # Build summary + status
    │   ├── requirements.md  # Frozen requirements doc for this build
    │   ├── bom.md           # Bill of materials (electronics + frame)
    │   ├── tooling.md       # Tools required to assemble
    │   ├── cad/             # 3D models — one folder per part
    │   ├── firmware/        # ArduCopter firmware + parameters
    │   ├── assembly/        # Assembly notes + build photos
    │   ├── flight-logs/     # Per-flight logs and post-flight notes
    │   └── post-mortem.md   # Written after build is retired
    ├── v2/                  # (future)
    └── v3/                  # (future)
```

## Build status

| Build | Goal | Status | Flight count |
|---|---|---|---|
| v1 | L1 autonomy — GPS waypoint mission | 🟡 In design | 0 |
| v2 | L1+ — geofence, optical-flow position hold | ⚪ Not started | — |
| v3 | L2 — vision-based autonomy, GPS-denied | ⚪ Not started | — |
| v4 | L3 — swarm coordination | ⚪ Not started | — |

## Per-build philosophy

Each `builds/vN/` folder is a complete, self-contained snapshot of that build. Requirements, BOM, CAD, firmware, and flight logs live with the build they belong to. When v2 starts, we copy v1's contents as a starting point and iterate — old builds stay frozen for reference and post-mortem analysis.

Components that prove themselves across multiple builds graduate to `hardware-library/`.

## Getting started

If you're cloning fresh:
1. Read `docs/design-principles.md` and `docs/safety-checklist.md`.
2. Open the most recent active build's `README.md` for current status.
3. Never skip a gate in the test plan. Failed gate → debug, don't push through.
