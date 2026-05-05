# Repo Conventions

Lightweight rules so that files end up in predictable places.

## Naming

- Files and folders: lowercase, hyphenated. `gps-mast`, not `GPS_Mast` or `gpsMast`.
- Markdown extensions: `.md`.
- CAD: `<part>-v<n>.step`, `<part>-v<n>.3mf`. STEP is the source of truth; export STL/3MF from STEP.
- Slicer profiles: `<part>-v<n>.slicer-profile.json` next to the model.
- Firmware params: `<airframe-serial>.params` (e.g. `v1-001.params`).
- Flight logs: `<YYYY-MM-DD>_<flight-id>_<short-description>/` (e.g. `2025-12-04_001_first-tethered-hover/`).

## CAD versioning

For every printed part:
```
builds/v1/cad/<part-name>/
├── README.md                    # what the part does, design intent
├── <part-name>-v1.step          # source of truth
├── <part-name>-v1.3mf           # slicer-ready (with profile baked in)
├── <part-name>-v1.stl           # exported, optional
├── <part-name>-v1.slicer-profile.json
└── notes.md                     # print orientation, supports, lessons
```

Increment version on any geometry change. **Never edit a versioned file in place** — copy to v2 and edit there.

## Commits

- Imperative, present tense: "add v1 GPS mast STEP", not "added" or "adds".
- Reference the build in the subject if scoped to one: `[v1] update bom — switch to T-Motor F40`.
- One logical change per commit. Don't bundle "fix typo" with "redesign canopy".

## Branches

- `main` is always known-good. Pushing broken code there delays the next flight.
- Work on `vN/<short-feature>` branches. Merge to main when the change has been validated (printed and fitted, or flashed and tested).

## Catalog entries

`hardware-library/parts-catalog/cat-NNN-name.md` files follow the format documented in `hardware-library/parts-catalog/README.md`. Key rules:

- `cat-NNN` IDs are immutable. Don't renumber.
- A catalog entry is design knowledge: abstract spec, ranked SKUs, reorder guidance, last-known prices.
- Update `Last verified` whenever prices or SKU rankings change.

## What to commit, what not to

| Commit | Don't commit |
|---|---|
| STEP, 3MF, slicer profile | Slicer scratch files, autosaves |
| Firmware `.apj` actually flashed (under `firmware/flashed/`) | Random `.hex` downloads |
| Param files used for flight | Mission Planner cache |
| Flight log `.csv` and `.tlog` | Raw `.bin` files (>10MB; large + recoverable from .csv) |
| Build photos in `assembly/photos/` | Anything containing API keys, GPS home coords for your house |
