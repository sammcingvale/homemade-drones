# v1 — Firmware

ArduCopter firmware and parameters for build v1.

## Folder layout

```
firmware/
├── README.md (this file)
├── flashed/                    # The exact .apj we put on the airframe
│   └── (e.g. arducopter-4.5.7-KakuteH7.apj)
└── params/
    ├── v1-001.params           # Per-airframe parameter dump (committed before each flight)
    └── v1-default.params       # Tuned baseline for the v1 design
```

## Initial flash workflow (first time on a new FC)

The v1 build uses the **Holybro Kakute H7 v1.5 + Tekko32 F4 50A ESC** stack (ArduCopter target `KakuteH7`). Flash path depends on what firmware (if any) is on the board when it arrives — verify on receipt before choosing a path below.

### Step 0 — verify what's on the board

Plug USB into the FC and connect to Mission Planner (or Betaflight Configurator). One of three states:

- **Already on ArduCopter** → skip to step 4 (update to latest stable).
- **ArduCopter bootloader only** (board appears as "ArduPilot Bootloader" in MP) → skip to step 4.
- **Betaflight or unknown** → start at step 1 (DFU + STM32CubeProgrammer).

### DFU first-flash path (Betaflight or blank board)

1. Download the latest stable ArduCopter firmware from https://firmware.ardupilot.org/Copter/stable/KakuteH7/
2. You want **`arducopter_with_bl.hex`** for the first flash (includes bootloader).
3. Save to `flashed/`.
4. Hold the BOOT button on the FC and plug USB into the laptop. FC enters DFU mode.
5. Use STM32CubeProgrammer (free from ST) to flash the .hex.
6. Disconnect USB, plug back in WITHOUT BOOT pressed. ArduCopter is now running.
7. From here on, use Mission Planner's "Install Firmware" → "Load custom firmware" to load `.apj` files.

### Mission Planner update path (board already has ArduPilot bootloader)

1. Download `arducopter.apj` (NOT `_with_bl.hex`) from https://firmware.ardupilot.org/Copter/stable/KakuteH7/
2. Save to `flashed/`.
3. In Mission Planner: Setup → Install Firmware → Load custom firmware → select the `.apj`.
4. FC reboots running ArduCopter.

### If you switch FC SKUs

The target name in URLs and filenames changes. Lookup table (matches `cat-002` ranked SKUs):

| FC SKU | ArduCopter target |
|---|---|
| Holybro Kakute H7 v1.5 (current v1 build) | `KakuteH7` |
| SpeedyBee F405 V4 | `SpeedyBeeF4V4` |
| SpeedyBee F405 V3 | `SpeedyBeeF4V3` |

## Param management

- `v1-default.params` is the canonical starting config for the v1 airframe design.
- Each physical airframe gets its own params file: `v1-001.params`, `v1-002.params`, etc.
- **Before every flight session:** dump current params from MP (Config → Full Parameter List → Save to file) and commit.
- **After tuning:** update `v1-default.params` if the changes apply to the design generally; otherwise leave it in the per-airframe file.

## Mission upload

Missions are not stored in the firmware repo (they're per-mission, ephemeral). Save `.waypoints` files alongside flight logs in `../flight-logs/<flight-id>/mission.waypoints`.

## Failsafe params (must be set before first flight)

Configured in `v1-default.params`:

| Parameter | Value | Purpose |
|---|---|---|
| `FS_THR_ENABLE` | 1 (RTL) | RC link loss → RTH |
| `BATT_FS_LOW_ACT` | 2 (RTL) | Low battery → RTH at 30% |
| `BATT_LOW_VOLT` | 14.4 (4S) | 30% threshold |
| `BATT_FS_CRT_ACT` | 1 (Land) | Critical battery → land at current pos |
| `BATT_CRT_VOLT` | 13.6 (4S) | 20% threshold |
| `FENCE_ENABLE` | 1 | Geofence active |
| `FENCE_TYPE` | 7 (alt + circle + polygon) | |
| `FENCE_RADIUS` | 30 (m) | Tight for v1 mission |
| `FENCE_ALT_MAX` | 15 (m) | Tight for v1 mission |
| `FENCE_ACTION` | 1 (RTL) | |
| `EK3_SRC1_YAW` | 1 (Compass) | |

Full param file will be generated and committed before G6.
