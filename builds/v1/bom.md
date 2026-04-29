# v1 — Bill of Materials

**Status:** Ready to order
**Last verified:** 2026-04-29
**Total estimated cost:** ~$1,290 (one-time + per-airframe; see breakdown at bottom)

Prices are approximate and may shift between order date and arrival. Verify at checkout. All vendors listed ship to US.

## Airframe + electronics (per airframe)

| # | Slot | SKU | Vendor | Qty | Unit | Subtotal | Notes |
|---|---|---|---|---|---|---|---|
| 1 | Frame | Source One V5 5" Base Kit (no top plate) | RDQ / GetFPV | 1 | $25 | $25 | Open-source, ubiquitous. Order spare arms ($8) — likely needed before v1 retires. |
| 2 | FC + ESC stack | SpeedyBee F405 V4 BLS 55A 30x30 Stack | GetFPV / Pyrodrone / Amazon | 1 | $70 | $70 | ArduCopter-supported. Includes FC + 4-in-1 ESC. |
| 3 | Motors | EMAX ECO II 2207 1900KV | RDQ / GetFPV | 4 | $15 | $60 | Set of 4. Spec match: 4S, 5" prop. |
| 4 | Props | HQProp T5x4.3x3 (5-inch tri-blade) | RDQ / GetFPV | 4 sets | $3 | $12 | Get 4 sets minimum — they break. Set = 2CW + 2CCW. |
| 5 | GPS + compass | Matek M10Q-5883 GNSS+Compass | RDQ / Matek direct | 1 | $45 | $45 | u-blox M10, QMC5883L mag. ArduCopter-ready. |
| 6 | RC receiver | BetaFPV ELRS Lite Receiver (2.4GHz) | BetaFPV / GetFPV | 1 | $20 | $20 | T-antenna, solder-pad mount. |
| 7 | Telemetry radio (air) | Holybro SiK Telemetry Radio V3 915MHz (pair) | Holybro / GetFPV | 1 pair | $65 | $65 | One end on drone, one on Toughbook (USB). 915MHz = US-legal. |
| 8 | Spare FC + ESC | SpeedyBee F405 V4 BLS 55A Stack | (same) | 1 | $70 | $70 | Hedge against first-build solder mistakes. |
| | | | **Airframe + electronics subtotal** | | | **$367** | |

## Power & charging (one-time except batteries)

| # | Slot | SKU | Vendor | Qty | Unit | Subtotal | Notes |
|---|---|---|---|---|---|---|---|
| 9 | Battery | CNHL Black Series 1500mAh 4S 100C XT60 | CNHL direct (US warehouse) / GetFPV | 4 | $25 | $100 | 4 packs minimum for a real session. |
| 10 | Charger | ToolkitRC M7AC | RDQ / GetFPV / Amazon | 1 | $70 | $70 | Built-in AC, no separate PSU needed. |
| 11 | LiPo bag | Generic large LiPo bag (12"×9") | Amazon | 1 | $15 | $15 | Charging + storage + transport. |
| 12 | Smoke stopper | Generic XT60 inline smoke stopper | RDQ / GetFPV | 1 | $15 | $15 | First power-up safety. Use every revision. |
| | | | **Power subtotal** | | | **$200** | |

## Radio (TX) — one-time

| # | Slot | SKU | Vendor | Qty | Unit | Subtotal | Notes |
|---|---|---|---|---|---|---|---|
| 13 | Transmitter | RadioMaster Pocket (ELRS, M2 sticks) | RadioMaster / GetFPV / Amazon | 1 | $80 | $80 | Built-in ELRS at 2.4GHz. EdgeTX firmware. |
| 14 | TX charger | USB-C cable (any) | (have) | 1 | — | — | Pocket charges via USB-C. |
| | | | **Radio subtotal** | | | **$80** | |

## Ground station — one-time

| # | Slot | SKU | Vendor | Qty | Unit | Subtotal | Notes |
|---|---|---|---|---|---|---|---|
| 15 | Field laptop | Used Panasonic Toughbook CF-54 w/ daylight-readable screen, Win 10/11, ≥8GB RAM | eBay (search "Toughbook CF-54 sunlight") | 1 | $400 | $400 | Verify "outdoor" or "1000-nit" screen variant. Refurbished from a reputable seller. |
| 16 | USB-A extender | 6ft USB 2.0 A-male to A-female cable | Amazon | 1 | $8 | $8 | Lets the SiK radio sit clear of the laptop on the ground station table. |
| | | | **Ground station subtotal** | | | **$408** | |

## Filament

| # | SKU | Vendor | Qty | Unit | Subtotal | Notes |
|---|---|---|---|---|---|---|
| 17 | Bambu PETG Basic, 1kg, black | Bambu Lab | 1 | $25 | $25 | Canopy, mast, battery tray. |
| 18 | Bambu TPU 95A HF, 0.5kg, black | Bambu Lab | 1 | $35 | $35 | Soft mounts, antenna tubes. |
| | | **Filament subtotal** | | | **$60** | |

## Hardware (M3 / M2 + heat-set inserts)

| # | SKU | Vendor | Qty | Unit | Subtotal | Notes |
|---|---|---|---|---|---|---|
| 19 | M3 SHCS assortment kit (8mm, 10mm, 12mm, 16mm, 20mm) | Amazon | 1 | $15 | $15 | Stainless or 12.9 alloy. |
| 20 | M3 nylon-insert lock nuts ×50 | Amazon | 1 | $8 | $8 | Frame motor mounts. |
| 21 | M3 heat-set inserts ×100 (brass) | Amazon | 1 | $12 | $12 | For printed parts. Install with soldering iron. |
| 22 | M2 SHCS assortment | Amazon | 1 | $10 | $10 | Electronics-side. |
| 23 | Velcro battery straps (200mm ×3) | Amazon / RDQ | 1 pack | $10 | $10 | |
| 24 | 3M VHB tape, 1/2" wide | Amazon | 1 | $8 | $8 | RX, telem radio mount. |
| 25 | Zip ties assortment | Amazon | 1 | $8 | $8 | |
| 26 | Heat shrink tubing kit | Amazon | 1 | $10 | $10 | |
| | | **Hardware subtotal** | | | **$81** | |

---

## Cost breakdown

| Category | Cost |
|---|---|
| Airframe + electronics (incl. spare FC stack) | $367 |
| Power & charging | $200 |
| Radio (TX) | $80 |
| Ground station | $408 |
| Filament | $60 |
| Hardware | $81 |
| Tools (see `tooling.md`) | $235 |
| **Total v1 build** | **~$1,431** |

### Per-airframe cost (v2+ when tools/radio/laptop already owned)

- Airframe + electronics minus spare FC: $297
- 4 batteries: $100 (probably reuse some)
- Filament (per-print share): ~$10
- Hardware: ~$30 (heat-set inserts already owned; just frame screws, straps)
- **Per-additional-airframe: ~$340–440**

---

## Vendor notes

- **GetFPV / RDQ (Race Day Quads) / Pyrodrone:** US-based hobby distributors. Frame kits, motors, FCs, props. Solid for everything except batteries (slow shipping due to LiPo regulations).
- **CNHL:** Has a US warehouse. Faster than ordering from China. Decent prices.
- **Bambu Lab:** Filament direct from manufacturer. Other brands (Polymaker, Overture, Prusament) also fine.
- **Holybro / Matek:** Drone hardware specialists. Can buy direct or through distributors.
- **Amazon:** Use for hardware (screws, tools), occasionally for FCs but verify SKU carefully — counterfeits exist.

## Lead time planning

- Order **today** (or today's evening): everything except the laptop.
- Order Toughbook from eBay seller with ≤3-day shipping.
- Bambu filament: Bambu's direct shipping is fast (~3 days US).
- Total expected ship time: 3–5 business days for everything to arrive.

If anything is backordered: skip the spare FC stack first (line 8), then reconsider in week 2.
