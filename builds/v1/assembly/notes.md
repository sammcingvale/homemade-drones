# v1 Assembly Notes

Fill in as you build. Photograph every step (drop into `./photos/`). Future builds reuse this as the assembly guide.

## Pre-assembly

- [ ] All parts received and accounted for against BOM.
- [ ] Tools laid out on workspace.
- [ ] Soldering iron tinned.
- [ ] Watched a 5" build walkthrough (Joshua Bardwell or Mark of UAVTech recommended).

## Stage 1 — Frame assembly (estimated 30 min)

Source One V5 instructions ship with the kit. Generally:

1. [ ] Unpack frame, verify part count.
2. [ ] Install motor mount screws into arms (don't tighten yet).
3. [ ] Apply Loctite 243 (blue) to motor screw threads.
4. [ ] Sandwich arms between top/bottom plates with standoffs at the four corners.
5. [ ] Tighten standoff screws hand-tight.

Photo: `photos/01-frame-assembled.jpg`
Notes:

## Stage 2 — Motor install (estimated 15 min)

1. [ ] Identify CW vs CCW motors (check labels and prop direction in motor spec sheet).
2. [ ] Install motors per the standard X-config:
   - Front-Right (M1): CCW prop, motor spins CW from above (standard ArduCopter)
   - Back-Right (M2): CW prop, motor spins CCW
   - Back-Left (M3): CCW prop, motor spins CW
   - Front-Left (M4): CW prop, motor spins CCW
3. [ ] Apply Loctite 243 to motor screws.
4. [ ] Tighten motor screws.
5. [ ] Verify motors spin freely by hand.

Note ArduCopter motor numbering convention is different from Betaflight. Refer to: https://ardupilot.org/copter/docs/connect-escs-and-motors.html

Photo: `photos/02-motors-installed.jpg`
Notes:

## Stage 3 — Soldering (estimated 90 min, first time)

⚠️ **Iron stays in the stand between joints. Eye protection on. Workspace clear of LiPos.**

### 3a. Tin everything first
- [ ] Tin the four motor pads on ESC.
- [ ] Tin the battery pad (positive and negative).
- [ ] Strip and tin the four motor wires.
- [ ] Strip and tin the battery lead wires.

### 3b. Solder motors to ESC
- [ ] Motor 1 → M1 pads (any wire to any pad — direction reversed in firmware later if wrong).
- [ ] Motor 2 → M2 pads.
- [ ] Motor 3 → M3 pads.
- [ ] Motor 4 → M4 pads.

### 3c. Solder battery lead with XT60
- [ ] Pre-tin XT60 cups before soldering wires.
- [ ] Heat shrink over each wire BEFORE soldering — easy to forget.
- [ ] Verify polarity: red to +, black to -.

### 3d. Multimeter check
- [ ] Continuity check: each motor wire to corresponding ESC pad.
- [ ] **No continuity** between battery + and -.
- [ ] **No continuity** between battery + and any motor wire.

Photo: `photos/03-stack-soldered.jpg`
Notes:

## Stage 4 — Stack mounting (estimated 20 min)

1. [ ] Mount FC + ESC stack to frame using vibration-damping rubber grommets (included in stack kit).
2. [ ] Connect FC to ESC via the included ribbon cable. Verify orientation per stack manual.
3. [ ] Verify USB-C port is accessible from outside the stack.

Photo: `photos/04-stack-mounted.jpg`
Notes:

## Stage 5 — Receiver install (estimated 20 min)

1. [ ] Solder RX power (5V, GND) and signal (TX of RX → RX of UART on FC) to FC.
2. [ ] ELRS receiver typically uses CRSF protocol on UART2 by default. Check FC pinout.
3. [ ] Mount RX with VHB tape on the bottom plate, antennas extending past the frame.
4. [ ] Antennas at 90° to each other for diversity.

Photo: `photos/05-rx-installed.jpg`
Notes:

## Stage 6 — GPS + compass install (estimated 20 min)

1. [ ] Print and install GPS mast (≥80mm tall).
2. [ ] Mount GPS module on top of mast with M3 screws or VHB.
3. [ ] Solder GPS wires to FC: 5V, GND, TX→RX (UART), RX→TX, SDA, SCL (for compass).
4. [ ] Verify compass orientation arrow points forward.

Photo: `photos/06-gps-mast.jpg`
Notes:

## Stage 7 — Telemetry radio install (estimated 15 min)

1. [ ] Mount SiK air radio on top plate or canopy with VHB.
2. [ ] Solder radio to FC UART (typically UART1 for telemetry).
3. [ ] Antenna extends vertically clear of frame.

Photo: `photos/07-telem-installed.jpg`
Notes:

## Stage 8 — Canopy + final assembly (estimated 20 min)

1. [ ] Install printed canopy over the stack.
2. [ ] Verify nothing pinches when closed.
3. [ ] Check all wires are strain-relieved (zip ties, hot glue at vibration points).
4. [ ] Install battery tray on bottom plate.
5. [ ] Install Velcro battery strap.

Photo: `photos/08-final-assembly.jpg`
Notes:

## Stage 9 — Pre-power-up check

⚠️ **Smoke stopper between battery and drone for first power-up.**

- [ ] Visual inspection: no loose wires, no exposed solder.
- [ ] Multimeter: no battery short.
- [ ] All M3 frame screws tight.
- [ ] **Props OFF.**

Ready for G1 (bench power-on).

---

## Issues encountered (running log)

| Stage | Issue | Resolution |
|---|---|---|
|  |  |  |
