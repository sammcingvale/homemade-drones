# Parts Catalog

The parts catalog is the canonical source of truth for **what parts are acceptable** for builds in this project. It defines abstract specifications, ranks SKUs that meet each spec, and captures reorder rationale.

## Catalog entry format

One file per entry: `cat-NNN-short-description.md`. Every entry follows this structure:

```markdown
# [Part name]

**Catalog ID:** cat-NNN
**Status:** active | retired | deferred
**Last verified:** YYYY-MM-DD

## Abstract spec
- requirement 1
- requirement 2
- ...

## Ranked SKUs

| Rank | Mfr part | Vendor | URL | Unit price | Notes |
|---|---|---|---|---|---|
| 1 | ... | GetFPV | ... | $X | preferred |
| 2 | ... | RDQ | ... | $X | fallback |

## Reorder guidance
[rationale paragraph + suggested trigger / order quantity]

## Notes
[design notes, gotchas, replacement strategy]
```

## Field semantics

**Abstract spec** — the requirements that distinguish "this catalog entry" from a different one. If a candidate SKU doesn't meet the spec, it shouldn't be in the ranked list — open a new catalog entry instead. Specs change rarely; SKU rankings change often.

**Ranked SKUs** — preference order. Procurement workflows try rank 1 first, fall back through the list. Prices are last-verified snapshots (re-checked at order time). URLs link to the product page on the vendor's site when known.

**Reorder guidance** — advisory text for procurement workflows. May suggest a trigger threshold and order quantity, but these are recommendations, not enforced state.

## Status field

- `active` — currently used in shipping builds
- `deferred` — spec'd but not yet used (e.g., parts only needed for v3+)
- `retired` — superseded by another entry; kept for historical reference

## When to add a new entry

When a new requirement emerges that no existing entry satisfies. **Don't fork an entry just because a SKU is OOS** — add the alternative as a lower-ranked SKU in the existing entry.

When you legitimately need a new entry (e.g., a 7" frame for a different build), copy the template above and increment the `cat-NNN` ID.

## When to update an entry

- A new SKU emerges that meets the spec → add it to the ranked list at the appropriate rank.
- A SKU goes EOL → strike it from the list with a strikethrough or remove and note in the catalog entry's commit message.
- Vendor URL changes → update.
- Prices drift significantly (>20%) → update with a fresh `Last verified` date.
- The abstract spec needs to change → consider whether this is the same part with a tightened/loosened spec, or a new part that warrants a new entry.

## Vendor preference

Single-vendor consolidation, GetFPV preferred. Fallback order: RDQ → manufacturer-direct → Amazon (non-flight items only). Revisit if GetFPV stops carrying core SKUs or has persistent stock problems.
