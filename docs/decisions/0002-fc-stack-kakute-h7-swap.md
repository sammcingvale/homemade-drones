# 0002 — FC stack swap: SpeedyBee F405 V4 → Holybro Kakute H7 v1.5

**Date:** 2026-05-11
**Status:** Accepted
**Applies to:** build v1 (and downstream until re-evaluated)

## Context

v1 BOM originally specified **SpeedyBee F405 V4 BLS 55A 30×30 Stack** as the rank-1 flight controller stack (catalog `cat-002`). Picked for cost (~$94), ubiquity in the ArduCopter community, well-documented DFU flash procedure, and broad distributor coverage.

During the procurement push on 2026-05-10/11, the V4 was OOS at every distributor we'd cataloged: GetFPV, Pyrodrone, Amazon (SpeedyBee storefront). No restock dates available. Holding the build for an unknown duration would directly violate OKR #1 (fly ASAP).

We had three options:

1. **Wait** for SpeedyBee F405 V4 restock at any distributor. Open-ended slip.
2. **Drop to SpeedyBee F405 V3** (the predecessor revision, same family, same firmware target family). Cheaper (~$80–90) and a direct drop-in. Stock also intermittent.
3. **Switch SKU to Holybro Kakute H7 v1.5 + Tekko32 F4 50A ESC stack.** Different vendor, different MCU (H7 instead of F405), different ESC firmware family (AM32 instead of BLHeli_S), $124.99 in stock at Holybro-direct.

## Decision

**Switch to Holybro Kakute H7 v1.5 + Tekko32 F4 4-in-1 50A ESC stack.** Rank-1 in cat-002 is updated to Holybro-direct at $124.99. SpeedyBee F405 V4 stays at rank-2 and V3 at rank-3 as fallbacks for future builds.

## Why this over option 1 (wait)

OKR #1 is fly ASAP. The whole v1 build was sequenced for time-to-G10 — waiting on a single SKU with no ETA is a procedural failure. The procurement research had already documented multiple acceptable substitutes; choosing one is exactly what the catalog's ranked-SKU structure is built for.

## Why this over option 2 (SpeedyBee F405 V3)

V3 was also intermittent at distributors, with the same OOS pattern as the V4. Switching to V3 was a sideways move with the same supply-chain risk. The Kakute H7 was confirmed in stock at the manufacturer directly on the day of order.

## Why this over other ArduCopter-supported 30×30 stacks

Kakute H7 is on the [ArduPilot supported autopilots list](https://ardupilot.org/copter/docs/common-autopilots.html) explicitly (target `KakuteH7`, ≥4.2.0). Holybro is an ArduPilot partner — first-party support, well-documented integration. We just successfully ordered the GPS module from Holybro-direct (cat-005), so the supply line is already open.

Spec check vs. the cat-002 abstract spec — every requirement met or exceeded:

| Requirement | Kakute H7 v1.5 + Tekko32 50A |
|---|---|
| 30.5×30.5mm mounting | ✅ identical pattern |
| ≥F405 MCU | ✅ STM32H743 (H7, exceeds spec) |
| ICM-42688P gyro | ✅ |
| Onboard baro | ✅ |
| 4-in-1 ESC ≥45A continuous | ✅ 50A |
| BLHeli_S / BLHeli_32 / AM32 | ✅ AM32 (modern open-source ESC firmware) |
| DSHOT600, bidi-DSHOT | ✅ default in AM32 |
| USB-C | ✅ |
| Onboard current sensor | ✅ |
| Dual BEC (5V + 9V) | ✅ 5V 2A + 9V 3A |

## Consequences

**Positive:**
- Build unblocked the day the decision was made.
- H7 MCU gives meaningful headroom for v2+ autonomy work (companion computer offload, more peripherals, more telemetry rate). Less likely to be the limiting factor when v2 work starts.
- AM32 ESC firmware is the modern successor to BLHeli_32 — open-source, actively maintained, full DSHOT support.
- Holybro vendor concentration: cat-005 (GPS) and cat-002 (FC) both sourced from Holybro-direct. One fewer shipping bill.

**Negative — accepted:**
- **+$31/unit (+33%)** vs SpeedyBee V4. With one spare in the BOM: +$62 total. New v1 total ~$1,653 vs $1,591. Manageable.
- **Documentation drift.** Most ArduCopter community howtos for 5" builds reference SpeedyBee F4 or Matek boards. Kakute H7 docs exist (Holybro's own + ArduPilot wiki) but the Stack Overflow / Reddit population is smaller. Mitigated by Holybro being an AP partner.
- **First-flash path may differ.** SpeedyBee ships with Betaflight (requires DFU + STM32CubeProgrammer). Kakute may ship blank, with ArduPilot bootloader, or with Betaflight depending on the SKU's run. `builds/v1/firmware/README.md` now branches on receipt to handle whichever state the board is in.
- **GPS cable will still need clip + resolder.** Same situation as with the V4 — Holybro M10 V2 connector and Kakute H7 GPS port are both standard Holybro pinouts but not always wired matching. Already flagged in cat-005 and BOM outstanding-flags.
- **Vendor concentration risk.** Holybro-direct is now single-source for two key items. If Holybro warehouse goes down or international shipping breaks, both items stall. Worth watching at v2 BOM time.

## Reversibility

High. cat-002 still lists the SpeedyBee V4 as rank-2 and V3 as rank-3. If the Kakute proves problematic (community support, parts availability, ESC quirks), switching back to a SpeedyBee F405 SKU is a one-line BOM change + firmware target rename. Spare FC purchase decision should weigh this.

## Follow-up actions

- [x] Update cat-002 (`hardware-library/parts-catalog/cat-002-fc-stack-30x30.md`)
- [x] Update BOM (`builds/v1/bom.md` — version bumped to v1.2)
- [x] Update firmware flash procedure (`builds/v1/firmware/README.md`)
- [x] Update requirements.md §6 vehicle spec table
- [ ] Decide whether to order the FC spare at the new price (~$125 vs $94). Defer until after G2 (initial bench bring-up) succeeds.
- [ ] On receipt: verify what firmware is on the Kakute board, choose the appropriate flash path.
