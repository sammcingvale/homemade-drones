# RC Receiver — ELRS 2.4GHz

**Catalog ID:** cat-006
**Status:** active
**Last verified:** 2026-05-11

## Abstract spec

- ExpressLRS (ELRS) protocol, 2.4GHz band
- ELRS firmware version ≥3.x (current generation)
- CRSF output to FC (single UART, telemetry back to TX)
- Integrated SMD ceramic antenna (Tower or Flat form factor — both function equivalently; Tower has a 6mm vertical profile, Flat is flush at 3mm)
- 5V input (FC provides 5V on RX pad)
- ≤2g
- Pre-attached 4× silicon wires (5V, GND, RX, TX) for solder to FC pads
- Diversity: not required for v1 mission profile (<500m range); single-antenna is sufficient

## Ranked SKUs

| Rank | Mfr part | Vendor | URL | Unit price | Notes |
|---|---|---|---|---|---|
| 1 | BetaFPV ELRS Lite V1.2 2.4GHz Receiver w/ Flat Antenna | GetFPV | https://www.getfpv.com/betafpv-elrs-lite-v1-1-2-4ghz-receiver-w-flat-antenna.html | $8.99 | **promoted from Flat-variant fallback on 2026-05-11** — Tower variant was discontinued at BetaFPV. PCB 11×10×3mm, integrated SMD ceramic antenna (flush), pre-attached 4-wire cable, 0.46g. Ships with ELRS 3.3.0. |
| 2 | BetaFPV ELRS Lite V1.2 2.4GHz Receiver w/ Flat Antenna | BetaFPV direct | https://betafpv.com/products/elrs-lite-receiver | $8.99 | manufacturer-direct fallback |
| 3 | BetaFPV ELRS Lite 2.4GHz Receiver w/ Ceramic Tower antenna | BetaFPV direct | https://betafpv.com/products/elrs-lite-receiver | (discontinued) | sold out at BetaFPV as of 2026-05-11. Was rank-1 before the Flat substitution. PCB 10×10×6mm, integrated tower antenna, 0.47g. Listed for posterity. |
| 4 | RadioMaster RP1 ELRS RX | GetFPV | https://www.getfpv.com/ | ~$15 | matches RadioMaster Pocket TX brand; verify URL at order time |

## Reorder guidance

Suggested trigger: on hand ≤ 1. Suggested order qty: 1.

## Notes

- TX and RX must run **matching ELRS firmware versions**. Update both at the same time.
- Bind procedure: power TX in bind mode, power RX (3 quick power-cycles or hold bind button), they auto-pair.
- **Tower vs Flat antenna form factor:** both BetaFPV ELRS Lite variants use an integrated SMD ceramic antenna on the receiver PCB — no detachable pigtail in either. Tower is 6mm tall (vertical orientation), Flat V1.2 is 3mm tall (flush). For this build's antenna-mount design (`builds/v1/cad/antenna-mounts/`), both fit the same parametric cradle with a one-line `RX_H` change. The earlier "do not substitute" warning was based on incomplete info — removed.
- Always test RC link loss failsafe **on the bench** before any flight. Pull TX battery, verify RX outputs failsafe values to FC.
