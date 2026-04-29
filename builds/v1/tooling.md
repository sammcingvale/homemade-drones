# v1 — Tooling

**Status:** Ready to order
**Total estimated cost:** ~$235 (one-time)

This list assumes zero existing tools. If you already own some of these, skip them.

## Soldering

| # | SKU | Vendor | Qty | Unit | Notes |
|---|---|---|---|---|---|
| 1 | Pinecil V2 soldering iron | Pine Store / Amazon | 1 | $30 | Tiny, fast, PD-powered. Industry standard for budget. |
| 2 | USB-C PD power supply, 65W (if not already owned) | Amazon | 1 | $25 | Pinecil needs PD; phone chargers may not deliver enough. 65W is plenty. |
| 3 | Solder, lead-free or 60/40 leaded, 0.6mm rosin-core, 100g | Amazon | 1 | $15 | Leaded solders easier and cheaper to learn with. Lead-free is greener but harder. Your call. |
| 4 | Rosin flux paste | Amazon | 1 | $10 | A pea-sized amount makes joints flow. |
| 5 | Solder wick (desolder braid) | Amazon | 1 | $5 | For when joints go wrong. |
| 6 | Helping hands w/ magnifier + LED | Amazon | 1 | $25 | Critical for FC pad work. |
| 7 | Brass sponge tip cleaner | Amazon | 1 | $8 | Wet sponge wears tips down. Brass doesn't. |
| 8 | Heat-resistant silicone work mat | Amazon | 1 | $15 | Protects your bench, catches solder splash. |
| | | **Soldering subtotal** | | **$133** | |

**Soldering technique note for first time:** practice on cheap perfboard or a dead PCB before touching the FC. Get a feel for tinning the iron, applying flux, and how solder flows. Watch Joshua Bardwell's "How to Solder a Quadcopter" video — 30 min, the canonical primer.

## Measurement & test

| # | SKU | Vendor | Qty | Unit | Notes |
|---|---|---|---|---|---|
| 9 | AstroAI digital multimeter (or Klein MM320) | Amazon | 1 | $30 | Continuity, voltage, resistance. Don't need a Fluke for v1. |
| 10 | IR thermometer (gun-style) | Amazon | 1 | $20 | Check ESC/motor temps after first power-up and after flights. |
| | | **Measurement subtotal** | | **$50** | |

## Mechanical

| # | SKU | Vendor | Qty | Unit | Notes |
|---|---|---|---|---|---|
| 11 | Wera 2.5mm hex driver (or full set 1.5–3mm) | Amazon | 1 | $25 | Frame standoffs are M3 hex. Wera doesn't strip. |
| 12 | Wire strippers (16–26 AWG) | Amazon | 1 | $15 | Hakko CHP-170 or generic. |
| 13 | Side cutters (flush) | Amazon | 1 | $10 | For zip ties + wire trimming. |
| 14 | Needle-nose pliers (small) | Amazon | 1 | $10 | |
| 15 | Tweezers, ESD-safe, set of 3 | Amazon | 1 | $10 | For SMT work and small fasteners. |
| 16 | Rubber prop wrench (or M5 nut driver) | RDQ / Amazon | 1 | $5 | Don't strip prop nuts with pliers. |
| 17 | Loctite 243 (medium-strength threadlocker, blue) | Amazon | 1 | $8 | Motor screws. **NOT** Loctite Red — that's permanent. |
| | | **Mechanical subtotal** | | **$83** | |

## Safety

| # | SKU | Vendor | Qty | Unit | Notes |
|---|---|---|---|---|---|
| 18 | Safety glasses | Amazon | 1 | $5 | Soldering + first power-up. |
| 19 | LiPo bag | (in BOM, line 11) | — | — | |
| 20 | Class D fire extinguisher OR sand bucket | Local hardware store | 1 | $40 / $5 | Sand is cheaper and works. Bucket of dry sand near the LiPo charging area. |
| | | **Safety subtotal** | | **$45** | |

---

## Cost breakdown

| Category | Cost |
|---|---|
| Soldering | $133 |
| Measurement & test | $50 |
| Mechanical | $83 |
| Safety | $45 |
| **Tools subtotal** | **$311** |

(Note: rounded up vs. earlier $235 estimate — included threadlocker, IR thermometer, ESD tweezers, and rubber prop wrench which I'd initially assumed were optional. They're not.)

## What we're NOT buying for v1

These are real tools, but defer until proven needed:

- Bench power supply (~$80) — smoke stopper covers v1 needs.
- Hot-air rework station (~$80) — only if reflowing SMT components, which we're not.
- Oscilloscope — overkill for v1.
- Hakko FX-888D station ($110) — Pinecil is sufficient.
- Crimping tools for JST connectors — most peripherals come pre-wired.

## Workflow tips

- **Lay out a static workspace** before assembly. Soldering at a kitchen table with cats around is how parts disappear.
- **Photograph every step.** Drop photos in `builds/v1/assembly/photos/`. Future builds will reuse this as the assembly guide.
- **Tin everything before joining.** Pre-tin the wire, pre-tin the pad, then join. 80% of bad joints come from skipping this.
