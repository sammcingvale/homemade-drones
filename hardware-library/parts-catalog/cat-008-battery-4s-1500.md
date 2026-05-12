# LiPo Battery — 4S 1500mAh

**Catalog ID:** cat-008
**Status:** active
**Last verified:** 2026-05-11

## Abstract spec

- 4S configuration (14.8V nominal, 16.8V full, 14.0V land-now threshold per ArduCopter `BATT_CRT_VOLT`)
- 1300–1500 mAh capacity
- ≥100C continuous discharge rating
- XT60 connector
- JST-XH balance lead
- ≤180g
- ≤90 × 38 × 35 mm physical envelope (fits the printed battery tray at `builds/v1/cad/battery-tray/`). **Envelope loosened 2026-05-11** — the original ≤90 × 35 × 30 mm spec under-specified the rank-1 CNHL V2.0 130C pack (actual 76 × 36 × 33 mm), forcing a 1–3 mm interference on two axes. Envelope now reflects the verified rank-1 pack plus ~2 mm headroom.

## Ranked SKUs

| Rank | Mfr part | Vendor | URL | Unit price | Notes |
|---|---|---|---|---|---|
| 1 | CNHL Black Series V2.0 1500mAh 4S 130C XT60 | GetFPV | https://www.getfpv.com/cnhl-black-series-v2-0-130c-4s-lipo-battery-1500mah.html | $31.49 | in stock at GetFPV 2026-05-10. **130C strictly exceeds the spec floor.** Verified physical dimensions: 76 × 36 × 33 mm, 164 g (multi-distributor confirmation 2026-05-11). Replaces the V1 100C SKU which is no longer carried. |
| 2 | CNHL Black Series 1500mAh 4S 100C XT60 (V1, older) | CNHL US warehouse | https://cnhl-us.com/ (verify URL at order time) | ~$21 | cheaper, older V1 spec — only use if rank-1 unavailable |
| 3 | Tattu R-Line 1550mAh 4S 100C | GetFPV | https://www.getfpv.com/ | ~$32 | premium alternative; verify URL at order time |

## Reorder guidance

4 packs is the minimum for a useful field session. Reorder when at or below 4 healthy packs.

Suggested trigger: on hand ≤ 4. Suggested order qty: 4.

## Notes

- LiPos are consumables. **Lifespan: ~150–300 cycles** depending on care.
- Retire any pack that:
  - Has visible swelling
  - Shows >0.05V cell-to-cell imbalance after a full charge
  - Drops below 14.0V under hover load
  - Has been damaged in a crash (puffed, dented, hot)
- Retired packs: discharge to 0V via saltwater bath (24+ hours), then dispose at battery recycling drop-off.
- Storage: 3.8V/cell if not flying within 48h. Modern smart chargers do this automatically.
- Retired packs are written off as attrition; reorder accordingly.
