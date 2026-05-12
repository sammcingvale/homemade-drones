# Motor soft-mount

TPU 95A vibration-damping pad between each motor and the carbon arm. The M3 mount screws compress the pad slightly when torqued, and the TPU's residual compliance absorbs high-frequency motor vibration before it reaches the FC's gyro.

## Quantity: 4

One per motor.

## Geometry summary

| Dimension | Value | Notes |
|---|---|---|
| Outer diameter | 28 mm | matches EMAX ECO II 2207 motor base |
| Thickness | 2 mm | nominal compression range |
| Mount holes | 4 × M3 clearance (3.4 mm), 16 × 16 mm pattern | Source One V5 / EMAX 2207 standard |
| Center bore | 10 mm | clearance for motor base bearing boss |
| Volume per part | ~1.0 cm³ | ≈ 0.3 g per pad in TPU 95A at 25% infill |

## Mounting interface

**Stack-up (bottom → top):**

1. M3 SHCS head (from below the arm)
2. Source One V5 carbon arm
3. **This pad (TPU)**
4. EMAX ECO II 2207 motor base
5. M3 thread engaged in motor

Screws torque normally; the TPU pad compresses slightly under tightening pressure. Don't crush it — leave the screws snug, not gorilla-tight.

## Why this geometry (and what's deliberately *not* in v1)

- **Flat disc, not o-ring style or dimpled.** The simplest possible soft-mount. TPU 95A at 2 mm thickness gives enough compliance to damp the gyro-relevant 100–300 Hz band that a 5" build typically generates. More elaborate designs (o-ring contact, raised bosses, concentric grooves) come in v2 only if v1's gyro vibration shows up in ArduPilot's `PIDP.x/y/z` logs.
- **28 mm OD, not larger.** Same diameter as the motor base — no overhang, clean look, no risk of TPU getting nicked by a finger during install. If side cushioning becomes a thing, v2 can grow OD to 30 mm.
- **10 mm center bore.** Generous clearance for the EMAX bearing boss + airflow under the motor. The exact boss diameter on the EMAX ECO II 2207 is ~5–6 mm; 10 mm is overprovisioned but cheap.

## Files

| File | Role |
|---|---|
| `motor-soft-mount-v1.py` | source of truth (CadQuery) |
| `motor-soft-mount-v1.step` | exported STEP |
| `motor-soft-mount-v1.stl` | exported STL |
| `motor-soft-mount-v1-preview.svg` | top-down preview |
| `notes.md` | print orientation, slicer notes, lessons |

## Re-export

```bash
.venv/bin/python builds/v1/cad/motor-soft-mounts/motor-soft-mount-v1.py
```
