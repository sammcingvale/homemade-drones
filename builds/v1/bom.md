# v1 — Bill of Materials

**Status:** Ready to order
**Version:** v1.1
**Last verified:** 2026-05-05
**Vendor policy:** GetFPV preferred → RDQ → mfr-direct → Amazon (non-flight only)

> **Note on freshness:** Vendors and prices change. Verify each line at order time using the linked catalog entry (which holds the ranked SKU list and last-known prices). After ordering, this file becomes a frozen procurement record.

> **Note on stock:** As of 2026-05-04, several core SKUs were OOS at GetFPV (frame, FC stack, motors). Verify stock or be prepared to fall back to rank-2 SKUs in each catalog entry.

---

## Airframe + electronics (per airframe)

| # | Catalog | Description | Qty | Unit (last seen) | Subtotal | Notes |
|---|---|---|---|---|---|---|
| 1 | [cat-001](../../hardware-library/parts-catalog/cat-001-frame-5in.md) | 5" frame (Source One V5) | 1 | $39 | $39 | TBS-branded at GetFPV preferred |
| 2 | [cat-002](../../hardware-library/parts-catalog/cat-002-fc-stack-30x30.md) | F405 V4 BLS 55A 30×30 stack | 1 | $94 | $94 | ArduCopter-supported |
| 3 | [cat-003](../../hardware-library/parts-catalog/cat-003-motor-2207.md) | 2207 1900KV motors | 4 | $20 | $80 | Order set of 4 |
| 4 | [cat-004](../../hardware-library/parts-catalog/cat-004-prop-5in-tri.md) | 5×4.3×3 tri-blade props | 16 | $1 | $16 | 4 sets of 4 |
| 5 | [cat-005](../../hardware-library/parts-catalog/cat-005-gps-compass.md) | M10 GPS + compass (Holybro) | 1 | $45 | $45 | **Replaced Matek M10Q-5883 (EOL)** |
| 6 | [cat-006](../../hardware-library/parts-catalog/cat-006-rx-elrs-24ghz.md) | ELRS 2.4GHz RX (Tower antenna) | 1 | $9 | $9 | Tower variant for canopy-mount build |
| 7 | [cat-007](../../hardware-library/parts-catalog/cat-007-telem-radio-915mhz.md) | SiK V3 915MHz pair, **100mW** | 1 pair | $60 | $60 | 100mW chosen — range margin sufficient |
| 8 | [cat-002](../../hardware-library/parts-catalog/cat-002-fc-stack-30x30.md) | Spare FC + ESC stack | 1 | $94 | $94 | Hedge against first-build solder mistakes |
| | | **Airframe + electronics subtotal** | | | **$437** | |

## Power & charging

| # | Catalog | Description | Qty | Unit | Subtotal | Notes |
|---|---|---|---|---|---|---|
| 9 | [cat-008](../../hardware-library/parts-catalog/cat-008-battery-4s-1500.md) | 1500mAh 4S 100C XT60 LiPo (CNHL Black) | 4 | $28 | $112 | Bought via GetFPV per vendor policy |
| 10 | (uncataloged) | ToolkitRC M7AC charger | 1 | $70 | $70 | One-time |
| 11 | (uncataloged) | LiPo charge/transport bag | 1 | $15 | $15 | One-time |
| 12 | (uncataloged) | Smoke stopper (XT60 inline) | 1 | $15 | $15 | One-time |
| | | **Power subtotal** | | | **$212** | |

## Radio (TX) — one-time

| # | Catalog | Description | Qty | Unit | Subtotal | Notes |
|---|---|---|---|---|---|---|
| 13 | (uncataloged — fixed asset) | RadioMaster Pocket (ELRS, M2 sticks) | 1 | $80 | $80 | EdgeTX firmware |
| | | **Radio subtotal** | | | **$80** | |

## Ground station — one-time

| # | Catalog | Description | Qty | Unit | Subtotal | Notes |
|---|---|---|---|---|---|---|
| 14 | (uncataloged — fixed asset) | Used Panasonic Toughbook CF-54 (daylight-readable screen, Win 10/11, ≥8GB) | 1 | $400 | $400 | eBay; verify "outdoor" variant |
| 15 | (uncataloged) | USB-A extender 6ft | 1 | $8 | $8 | |
| | | **Ground station subtotal** | | | **$408** | |

## Filament

| # | Catalog | Description | Qty | Unit | Subtotal | Notes |
|---|---|---|---|---|---|---|
| 16 | [cat-009](../../hardware-library/parts-catalog/cat-009-filament-petg.md) | PETG Basic, 1kg, black (Bambu) | 1 | $20 | $20 | Watch for sale ($13 recent) |
| 17 | [cat-010](../../hardware-library/parts-catalog/cat-010-filament-tpu95a.md) | TPU 95A HF, **1kg**, black (Bambu) | 1 | $42 | $42 | **Corrected from BOM v1.0 (was 0.5kg, doesn't exist)** |
| | | **Filament subtotal** | | | **$62** | |

## Hardware

| # | Catalog | Description | Qty | Unit | Subtotal | Notes |
|---|---|---|---|---|---|---|
| 18 | [cat-011](../../hardware-library/parts-catalog/cat-011-m3-shcs-kit.md) | M3 SHCS assortment kit | 1 | $15 | $15 | |
| 19 | [cat-012](../../hardware-library/parts-catalog/cat-012-m3-nyloc-nuts.md) | M3 nyloc nuts ×50 | 1 | $8 | $8 | |
| 20 | [cat-013](../../hardware-library/parts-catalog/cat-013-m3-heat-inserts.md) | M3 brass heat-set inserts ×100 | 1 | $12 | $12 | |
| 21 | (uncataloged, low-volume) | M2 SHCS assortment | 1 | $10 | $10 | |
| 22 | (uncataloged, low-volume) | Velcro battery straps ×3 | 1 pack | $10 | $10 | |
| 23 | (uncataloged, low-volume) | 3M VHB tape, 1/2" | 1 | $8 | $8 | |
| 24 | (uncataloged, low-volume) | Zip ties assortment | 1 | $8 | $8 | |
| 25 | (uncataloged, low-volume) | Heat shrink tubing kit | 1 | $10 | $10 | |
| | | **Hardware subtotal** | | | **$81** | |

---

## Cost breakdown

| Category | Cost |
|---|---|
| Airframe + electronics (incl. spare FC) | $437 |
| Power & charging | $212 |
| Radio (TX) | $80 |
| Ground station | $408 |
| Filament | $62 |
| Hardware | $81 |
| Tools (see `tooling.md`) | $311 |
| Solder consumables (cat-014, included in tooling) | — |
| **Total v1 build** | **~$1,591** |

### Per-airframe cost (v2+ when tools/radio/laptop already owned)

- Airframe + electronics minus spare FC: $343
- 4 batteries: ~$112 (some reusable from v1)
- Filament (per-print share): ~$10
- Hardware: ~$30
- **Per-additional-airframe: ~$370–490**

---

## Changes from v1.0

Driven by procurement research run on 2026-05-04:

1. **GPS swap.** Matek M10Q-5883 → Holybro M10 V2. Matek's M10 series is end-of-life. Holybro is in production, ArduPilot-supported, with bonus IP67 rating.
2. **TPU SKU corrected.** Bambu doesn't sell TPU 95A HF in 0.5kg. Updated to 1kg ($42 vs old $35) — gets us 2× the filament for 20% more.
3. **RX disambiguated.** Tower antenna variant chosen over Flat. Tower routes simply through canopy on outdoor builds; Flat is for racing layouts.
4. **Telem radio wattage specified.** 100mW chosen (BOM previously left this open). 500mW was the suggested middle option but offers no benefit at <500m range — costs more, runs hotter.
5. **Frame branding pinned.** TBS-branded Source One V5 at GetFPV chosen as canonical. RDQ and Pyrodrone variants stay as fallbacks (same open-source design).
6. **Battery vendor changed.** GetFPV instead of CNHL-direct. Higher unit cost (~$28 vs $21) but resolves US warehouse routing ambiguity and matches single-vendor consolidation policy.
7. **Prices refreshed.** Multiple lines saw +30–70% increase since BOM v1.0 (5 days ago). Reality is what's in the catalog now.
8. **Format change.** Each line now references a catalog entry by ID. Catalog holds the ranked SKU list, abstract spec, and reorder guidance. BOM is just "what to procure for this build."

## Outstanding flags

- Verify GetFPV stock at order time. Some core items were OOS as of 2026-05-04 — consider rank-2 SKUs in each catalog entry if still OOS.
- Toughbook CF-54 listings vary widely on eBay. Verify "daylight-readable" (sometimes called "outdoor display" or "sunlight-readable") in the listing photos before buying.
- Holybro M10 V2 cable connector may need clipping/resoldering to match SpeedyBee F405 V4 GPS pads. Plan for ~10 min of extra solder work.
