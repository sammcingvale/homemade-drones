# RC Receiver — ELRS 2.4GHz

**Catalog ID:** cat-006
**Status:** active
**Last verified:** 2026-05-10

## Abstract spec

- ExpressLRS (ELRS) protocol, 2.4GHz band
- ELRS firmware version ≥3.x (current generation)
- CRSF output to FC (single UART, telemetry back to TX)
- Tower (vertical monopole) antenna preferred for outdoor builds with canopy mounting — better polarization tolerance for ground-to-air
- 3.3V or 5V input acceptable (FC provides 5V on RX pad)
- ≤2g
- Solder pads or 4-pin JST-SH (FC pad layout works for either)
- Diversity antennas optional but preferred (2x antennas at 90°)

## Ranked SKUs

| Rank | Mfr part | Vendor | URL | Unit price | Notes |
|---|---|---|---|---|---|
| 1 | BetaFPV ELRS Lite 2.4GHz Receiver w/ Ceramic Tower antenna | GetFPV | https://www.getfpv.com/betafpv-elrs-lite-2-4ghz-receiver-w-ceramic-tower-antenna.html | ~$15 | OOS at GetFPV 2026-05-10. **Do not silently substitute the Flat-antenna variant — different geometry, mismatches canopy plan.** |
| 2 | BetaFPV ELRS Lite 2.4GHz Receiver w/ Ceramic Tower antenna | BetaFPV direct | https://betafpv.com/ | ~$9 | manufacturer-direct, cheaper |
| 3 | RadioMaster RP1 ELRS RX | GetFPV | https://www.getfpv.com/ | ~$15 | matches RadioMaster Pocket TX brand; verify URL at order time |

## Reorder guidance

Suggested trigger: on hand ≤ 1. Suggested order qty: 1.

## Notes

- TX and RX must run **matching ELRS firmware versions**. Update both at the same time.
- Bind procedure: power TX in bind mode, power RX (3 quick power-cycles or hold bind button), they auto-pair.
- Tower antenna (vertical) routes simply through the canopy. **Flat antenna variant is a separate BetaFPV SKU at the same vendor — do not substitute.** Flat is for racing builds with top-mounted RX, not our Source One V5 canopy plan.
- Always test RC link loss failsafe **on the bench** before any flight. Pull TX battery, verify RX outputs failsafe values to FC.
