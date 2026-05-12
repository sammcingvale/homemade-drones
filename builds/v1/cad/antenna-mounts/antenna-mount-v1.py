"""
antenna-mount-v1 — TPU 95A mount for the BetaFPV ELRS Lite V1.2 RX (Flat Antenna).

The BetaFPV ELRS Lite RX (Flat V1.2) is a single 11×10×3mm module (0.46g) with
an SMD ceramic antenna soldered flush to the PCB. No diversity, no detachable
antenna. This part holds the whole module out past the carbon frame edge so the
integrated antenna has RF clearance to the operator.

Quantity: 1 (single-antenna RX).

Was originally designed for the Tower variant (10×10×6mm) on 2026-05-11; Tower
was discontinued at BetaFPV and we ordered the Flat V1.2 instead. Geometric
adjustment is parameter-only (RX_W, RX_H) — design intent unchanged.
"""

from pathlib import Path

import cadquery as cq

# ===== parameters (mm) =====

# RX module dimensions (BetaFPV ELRS Lite V1.2, Flat Antenna variant)
# Source: BetaFPV product page, 2026-05-11 ("11mm*10mm*3mm (Flat)")
RX_W = 11.0
RX_D = 10.0
RX_H = 3.0
RX_SLOP = 1.0  # friction-fit clearance per axis

# Base — piggybacks on a corner standoff bolt with the canopy
BASE_W = 15.0
BASE_D = 15.0
BASE_T = 3.0
M3_CLEARANCE = 3.4

# Boom — extends the RX out past the carbon frame edge for RF clearance
BOOM_L = 22.0
BOOM_W = 8.0
BOOM_T = 4.0

# Cradle — rectangular tube (open top + open bottom) that grips the RX
CRADLE_WALL = 1.5
CRADLE_W = RX_W + RX_SLOP + 2 * CRADLE_WALL  # 14.0
CRADLE_D = RX_D + RX_SLOP + 2 * CRADLE_WALL  # 14.0
CRADLE_H = RX_H + RX_SLOP + 2 * CRADLE_WALL  # 10.0 (vertical with antenna up)

# ===== build =====
# Coordinate convention:
#   Base centered at origin on XY plane, bolts through Z=0 face
#   Boom extends in +X direction
#   Cradle is at the +X end of the boom, with the antenna pointing in +Z

base = (
    cq.Workplane("XY")
    .box(BASE_W, BASE_D, BASE_T, centered=(True, True, False))
    .faces(">Z")
    .workplane()
    .hole(M3_CLEARANCE)
)

boom = (
    cq.Workplane("XY")
    .box(BOOM_L, BOOM_W, BOOM_T, centered=(False, True, False))
    .translate((BASE_W / 2, 0, 0))
)

cradle_x_center = BASE_W / 2 + BOOM_L + CRADLE_W / 2

cradle_outer = (
    cq.Workplane("XY")
    .box(CRADLE_W, CRADLE_D, CRADLE_H, centered=(True, True, False))
    .translate((cradle_x_center, 0, 0))
)

# Open-top, open-bottom interior — tube grips the RX by friction on 4 side walls.
# Slightly overbuilt in Z (CRADLE_H + 2) so the through-cut breaks cleanly.
cradle_interior = (
    cq.Workplane("XY")
    .box(RX_W + RX_SLOP, RX_D + RX_SLOP, CRADLE_H + 2, centered=(True, True, False))
    .translate((cradle_x_center, 0, -1))
)

mount = base.union(boom).union(cradle_outer).cut(cradle_interior)

# ===== export =====
out_dir = Path(__file__).parent
stem = "antenna-mount-v1"

bb = mount.val().BoundingBox()
volume = mount.val().Volume()

cq.exporters.export(mount, str(out_dir / f"{stem}.step"))
cq.exporters.export(mount, str(out_dir / f"{stem}.stl"))

print(f"wrote {stem}.step and {stem}.stl to {out_dir}")
print(f"  bounding box: {bb.xlen:.1f} x {bb.ylen:.1f} x {bb.zlen:.1f} mm")
print(f"  volume: {volume / 1000:.2f} cm^3")
