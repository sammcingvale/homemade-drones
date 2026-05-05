# hardware-library/

Cross-build hardware design knowledge: parts catalog, kits, and (eventually) reusable CAD components.

## Subfolders

```
hardware-library/
├── parts-catalog/    # Abstract part specs + ranked SKU lists + reorder guidance
├── kits/             # Packing lists for field/bench operations
└── (cad/)            # Reusable CAD components — populated when parts graduate from a build
```

## What lives here vs. what doesn't

This folder holds **design knowledge** that spans builds: which parts are acceptable, why we picked them, what they're for. It's version-controlled, infrequently mutated, and tied to the project.

It deliberately does **not** hold operational state — current on-hand counts, order history, who-touched-what-when. Those live outside the repo and are owned by tooling that operates across multiple projects.

## Catalog vs. BOM

- **Catalog** (`parts-catalog/`): "what parts are acceptable for builds in this project, ranked by preference."
- **BOM** (`builds/vN/bom.md`): "what was procured for this specific build, at what price, on what date."

A build's BOM references catalog entries by ID. The catalog is the abstract spec; the BOM is the concrete procurement record for one build.
