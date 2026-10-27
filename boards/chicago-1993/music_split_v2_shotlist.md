# Chicago 1993: music split v2 shot list

`music_split_v2.mp4`: 1920x1080, 24 fps, 1428 frames (59.50 s). Left panel is Chicago, right panel is the counter-world (steel), with a 16 px gutter. Track: `lyria_opt1.mp3` (edited), 92.3 BPM, 22 bars.

## Arc

One rider's trip mirrored by one heat of steel. Chicago: waiting in the rain → the bus arrives → boarding → pulling away down the sodium strip → (break) → the ride across the city by bus, L and train at full speed → back through the sodium side streets → the empty shelter. Steel: the ladle fills → the slab enters the rolls → tap and hot bar → (break: the run-out slows) → the mill at full speed → billets cool on the line → ingots cool in the dark.

## Cut rules

- Every cut lands on a bar downbeat, using frame indices taken from the librosa downbeat grid at 24 fps. Both panels cut on the same frame.
- Energy comes from bars per shot: sparse (bars 1–4) 4 bars, groove (5–12) 2 bars, break (13) 1 bar, peak (14–21) 1 bar, release (22) runs to the end.
- `gen_edl.py` declares pairs by bar index and asserts they tile the bars at the section rate. `render_v2.py` re-derives frames from the bar indices and refuses to render on any mismatch. `check_edl.py` re-verifies the EDL and the rendered file.

## Pairing grammar

Every simultaneous pair must pass one of these rules, each checked by machine against motion measured from the footage (optical flow, luma, warmth), not against catalog tags alone.

| Rule | Name | Shape | Used at bars |
|---|---|---|---|
| `FALL_INTO` | Falling into a pool | drops hit standing water ↔ molten stream drops into the ladle | 1 |
| `SAME_WAY` | Same way across the frame | the main subject crosses the frame in the same direction on both sides | 5, 7, 11, 13, 17, 18, 19, 20, 21 |
| `WINDOW_RIDE` | Window ride | both shot from a moving train window, scenery streaming the same way | 16 |
| `STROKE` | Mechanical stroke | a repeating machine stroke in a locked frame (wiper arm ↔ forge ram) | 15 |
| `MOLTEN_LIGHT` | Sodium = molten | orange light in the dark: sodium streaks ↔ molten metal | 9, 14 |
| `REPEATED_UNITS` | Repeated units sliding past | a grid of identical units slides the same way (streetlights ↔ billets) | (not used in v2) |
| `STILL_GLOW` | Still glow | a lit box/pool at rest in the dark (shelter ↔ cooling ingots) | 22 |

## Shots

| # | Time | Bar(s) | Frames | Section | Chicago (left) | Counter-world (right) | Rule | Link | Evidence |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 0:00.00–0:10.46 | 1–4 | 0–251 | sparse | `t-rain-puddles` @ 0.13 s<br>Waiting: rain pools at the curb | `a-kover-ladle` @ 0.88 s<br>Charge: the ladle fills | Falling into a pool | rain rings in the puddle ↔ the steel stream falling into the ladle (zone 17 pair) | both tagged falling (down), both slow (flow 6.3 / 2.0) |
| 2 | 0:10.46–0:15.83 | 5–6 | 251–380 | groove | `c-impr-bus-night` @ 2.42 s ×0.9<br>Arrival: the bus pulls in | `a-acroni-rolls` @ 1.67 s<br>The slab enters the rolls | Same way across the frame | the bus pulls into the stop ↔ the slab rolls into the stand, same direction (zone 17 pair) | subject motion +32 / +17 px/s (L→R both) |
| 3 | 0:15.83–0:21.12 | 7–8 | 380–507 | groove | `c-impr-crossing` @ 0.08 s ×0.9<br>Boarding: riders cross | `a-servant-slab` @ 0.50 s<br>The slab runs through | Same way across the frame | riders cross to the bus ↔ the glowing slab slides through, same direction (zone 17 pair) | subject motion +16 / +25 px/s (L→R both) |
| 4 | 0:21.12–0:26.33 | 9–10 | 507–632 | groove | `c-edison-storefronts` @ 18.48 s<br>Pulling away down the sodium strip | `a-servant-tap` @ 13.58 s<br>The tap glows | Sodium = molten | the sodium-lit strip ↔ the open-hearth tap: the same orange in the dark | warm light source both (sodium/furnace), orange cast R-B 38 / 30 |
| 5 | 0:26.33–0:31.54 | 11–12 | 632–757 | groove | `c-ic92-night` @ 7.94 s<br>Traffic slides past the window | `a-servant-roll` @ 8.33 s<br>Hot bar in motion | Same way across the frame | orange-lit traffic ↔ a hot bar, crossing the same way (zone 17 pair) | subject motion -43 / -8 px/s (R→L both) |
| 6 | 0:31.54–0:34.12 | 13 | 757–819 | break | `t-rain-reflect` @ 2.42 s<br>Break: feet in the puddle | `a-acroni-runout` @ 3.40 s<br>The run-out slows | Same way across the frame | feet through a puddle reflection ↔ a slab easing down the run-out (zone 17 pair) | subject motion +19 / +9 px/s (L→R both) |
| 7 | 0:34.12–0:36.75 | 14 | 819–882 | peak | `c-doha-sodium` @ 15.73 s<br>The ride: sodium streaks | `a-vicart-sparks` @ 0.96 s<br>Ladle over the furnace | Sodium = molten | sodium streaks through a wet windshield ↔ a ladle over the open furnace, sparks flying | warm light source both (sodium/furnace), orange cast R-B 47 / 69 |
| 8 | 0:36.75–0:39.42 | 15 | 882–946 | peak | `t-rain-wipers` @ 5.80 s<br>Wipers | `a-hendrichs-drop` @ 7.20 s<br>Drop forge | Mechanical stroke | the wiper arm sweeps ↔ the drop-forge ram strikes | locked-off camera both, strong repeating motion (flow p90 53 / 44) |
| 9 | 0:39.42–0:42.12 | 16 | 946–1011 | peak | `c-amtrak95` @ 7.92 s<br>Train window, gray industrial edge | `a-inland-train` @ 2.54 s<br>Mills past the train window | Window ride | Chicago industrial edge ↔ Indiana Harbor mills, both seen from a train window streaming the same way | both tracking shots (move=track: track/track); subject motion -94 / -127 px/s (R→L both) |
| 10 | 0:42.12–0:44.71 | 17 | 1011–1073 | peak | `c-94-loop` @ 13.20 s<br>The L through the Loop | `a-mills-fast` @ 5.17 s<br>Hot strip races the stands | Same way across the frame | the L swings through the Loop ↔ hot strip races the stands, same direction | subject motion +100 / +51 px/s (L→R both) |
| 11 | 0:44.71–0:47.38 | 18 | 1073–1137 | peak | `c-harrison-arrive` @ 13.01 s<br>Train into Harrison | `a-kover-pan` @ 3.60 s<br>Billets sweep past | Same way across the frame | the subway train sweeps the platform ↔ the pan along stacked billets, same direction | subject motion -121 / -81 px/s (R→L both) |
| 12 | 0:47.38–0:50.04 | 19 | 1137–1201 | peak | `c-94-skyline` @ 28.32 s<br>Skyline across the lot | `a-ecsteel-train` @ 3.07 s<br>Mill stacks from the train | Same way across the frame | the Chicago skyline ↔ the East Chicago smokestack skyline, both sliding the same way under a steel-blue sky | subject motion +27 / +30 px/s (L→R both) |
| 13 | 0:50.04–0:52.71 | 20 | 1201–1265 | peak | `c-94-northside` @ 4.32 s<br>Back porches from the L | `a-acroni-fast` @ 1.94 s<br>Roller table at speed | Same way across the frame | three-flats rush past the L ↔ the roller table rushes past: top speed, same direction | subject motion -27 / -109 px/s (R→L both) |
| 14 | 0:52.71–0:55.42 | 21 | 1265–1330 | peak | `c-edison-sodium` @ 28.43 s<br>Home: sodium side streets | `a-kover-billets` @ 12.24 s<br>Billets cool on the line | Same way across the frame | sodium side streets ↔ glowing billets on the line: the same orange, drifting the same way (zone 17 pair) | subject motion +30 / +9 px/s (L→R both) |
| 15 | 0:55.42–0:59.50 | 22 | 1330–1428 | release | `c-impr-shelter` @ 0.25 s (holds at 3.0 s)<br>Release: the empty shelter (holds) | `a-servant-pour` @ 14.75 s<br>Ingots cool | Still glow | the lit, empty shelter ↔ ingots cooling in the dark | near-still (flow 0.4 / 1.0) and warm-lit (R-B 24 / 10) |

## Dropped clips

- `c-southloop88-tower` and `c-18th-platform`: pinkish 1988 daylight handheld flashes.
- `a-inland-train2`: blows out to white (around 54–55 s in v1).

These are listed in `BANNED` in `grammar.py`, and the check fails if any of them appears.

## Check output (`check_edl.py`)

```
PASS 14 cuts per panel, identical frames on both panels, all on bar downbeats: [251, 380, 507, 632, 757, 819, 882, 946, 1011, 1073, 1137, 1201, 1265, 1330]
PASS bar  1 FALL_INTO      t-rain-puddles ↔ a-kover-ladle: both tagged falling (down), both slow (flow 6.3 / 2.0)
PASS bar  5 SAME_WAY       c-impr-bus-night ↔ a-acroni-rolls: subject motion +32 / +17 px/s (L→R both)
PASS bar  7 SAME_WAY       c-impr-crossing ↔ a-servant-slab: subject motion +16 / +25 px/s (L→R both)
PASS bar  9 MOLTEN_LIGHT   c-edison-storefronts ↔ a-servant-tap: warm light source both (sodium/furnace), orange cast R-B 38 / 30
PASS bar 11 SAME_WAY       c-ic92-night ↔ a-servant-roll: subject motion -43 / -8 px/s (R→L both)
PASS bar 13 SAME_WAY       t-rain-reflect ↔ a-acroni-runout: subject motion +19 / +9 px/s (L→R both)
PASS bar 14 MOLTEN_LIGHT   c-doha-sodium ↔ a-vicart-sparks: warm light source both (sodium/furnace), orange cast R-B 47 / 69
PASS bar 15 STROKE         t-rain-wipers ↔ a-hendrichs-drop: locked-off camera both, strong repeating motion (flow p90 53 / 44)
PASS bar 16 WINDOW_RIDE    c-amtrak95 ↔ a-inland-train: both tracking shots (move=track: track/track); subject motion -94 / -127 px/s (R→L both)
PASS bar 17 SAME_WAY       c-94-loop ↔ a-mills-fast: subject motion +100 / +51 px/s (L→R both)
PASS bar 18 SAME_WAY       c-harrison-arrive ↔ a-kover-pan: subject motion -121 / -81 px/s (R→L both)
PASS bar 19 SAME_WAY       c-94-skyline ↔ a-ecsteel-train: subject motion +27 / +30 px/s (L→R both)
PASS bar 20 SAME_WAY       c-94-northside ↔ a-acroni-fast: subject motion -27 / -109 px/s (R→L both)
PASS bar 21 SAME_WAY       c-edison-sodium ↔ a-kover-billets: subject motion +30 / +9 px/s (L→R both)
PASS bar 22 STILL_GLOW     c-impr-shelter ↔ a-servant-pour: near-still (flow 0.4 / 1.0) and warm-lit (R-B 24 / 10)
PASS render left (Chicago): visible cut at all 14 declared frames
PASS render left (Chicago): luma min 10, max 185 (gates 8/215)
PASS render right (counter-world): visible cut at all 14 declared frames
PASS render right (counter-world): luma min 26, max 175 (gates 8/215)
RESULT: PASS (0 fail, 0 warn)
```
