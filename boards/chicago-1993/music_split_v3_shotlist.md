# Chicago 1993: music split v3 shot list

`music_split_v3.mp4` (lead 1): 1920x1080, 24 fps, 1345 frames (56.04 s). Left panel Chicago, right panel the counter-world (steel), 16 px gutter.
Audio: `music_edit_v3.wav` only, no clip audio (AAC 256k, static gain -1.76 dB to -15.0 LUFS, no loudnorm).
Music: `lyria_opt1.mp3`, 6/8 at 180 eighths/min (2.0 s bars), 6 pulses per bar, 28 detected downbeats.

## Arc

One rider's trip mirrored by one heat of steel. Chicago: the city at rest → waiting in the rain → the bus arrives on the drums → boarding → pulling away down the sodium strip → (drums out: the ride starts quietly, wipers, sodium) → (break: feet in the puddle) → the drop: the ride across the city by train, L and subway at full speed → back through the sodium side streets → the empty shelter. Steel: the furnace idles → the ladle fills → the slab enters the rolls → tap and hot bar → forge and tap → (break: the run-out slows) → the mill at full speed → billets cool on the line → ingots cool in the dark.

## How the cuts are made (musicsync)

- **Beats:** Beat This! on the mix and on the Demucs drum stem, cross-checked with madmom's DBN at 2/3/4/6 beats per bar; ties broken on the drum-stem kick and snare. Real downbeat times are stored; there is no fixed BPM.
- **Moments:** each downbeat is scored for drums in or out, drop, break, release, fill landing (drum-stem energy in the last third of the previous bar) and section change (self-similarity novelty snapped to the downbeat).
- **Cut list:** every top and high moment is a cut. Between anchors the base rate applies: sparse 4 bars, groove 2, break 1, peak 1, release holds. Both panels share one list.
- **Lead:** frame = round(t × 24) − 1.
- **Music edit:** whole-bar splices on source downbeats: source bars 4–15 + 20–29 + 33–38, cut just before the downbeat transient with a 10 ms equal-power crossfade. Joints fall at 24.04 s, 44.03 s.

## Shots

| # | Time | Frames | Bars | Energy | Moment hit | Offset vs re-detected downbeat | Chicago (left) | Counter-world (right) | Rule | Link |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 0:00.00–0:02.00 | 0–48 | 1 | sparse | **start**<br><sub></sub> | start | `t-rain-window` @ 21.04 s<br>Night: the city at rest | `a-servant-ladle` @ 0.33 s<br>The furnace idles | Still glow | the city at rest under sodium ↔ the furnace idling (fade in) |
| 2 | 0:02.00–0:10.00 | 48–240 | 4 | sparse | **change**<br><sub>novelty 0.27, mix +15.1 dB</sub> | +11.3 ms | `t-rain-puddles` @ 0.07 s<br>Waiting: rain pools at the curb | `a-kover-ladle` @ 6.80 s<br>Charge: the ladle fills | Falling into a pool | rain rings in the puddle ↔ the steel stream falling into the ladle (zone 17 pair) |
| 3 | 0:10.00–0:14.00 | 240–336 | 2 | groove | **drums in, section**<br><sub>drum stem -45→-41 dB; novelty 0.97</sub> | +19.5 ms | `c-impr-bus-night` @ 2.50 s<br>Arrival: the bus pulls in | `a-acroni-rolls` @ 4.07 s<br>The slab enters the rolls | Same way across the frame | the bus pulls into the stop ↔ the slab rolls into the stand, same direction (zone 17 pair) |
| 4 | 0:14.00–0:18.00 | 336–432 | 2 | groove | **section**<br><sub>novelty 0.78</sub> | +13.6 ms | `c-impr-crossing` @ 0.58 s<br>Boarding: riders cross | `a-servant-slab` @ 1.17 s<br>The slab runs through | Same way across the frame | riders cross to the bus ↔ the glowing slab slides through, same direction (zone 17 pair) |
| 5 | 0:18.00–0:22.00 | 432–528 | 2 | groove | **fill landing, section**<br><sub>fill in previous bar: 1 late hits, late drum level +6.5 dB vs typical; novelty 0.79</sub> | +12.7 ms | `c-edison-storefronts` @ 18.42 s<br>Pulling away down the sodium strip | `a-servant-tap` @ 14.25 s<br>The tap glows | Sodium = molten | the sodium-lit strip ↔ the open-hearth tap: the same orange in the dark |
| 6 | 0:22.00–0:24.00 | 528–576 | 1 | groove | **section**<br><sub>novelty 0.73</sub> | +11.8 ms | `c-ic92-night` @ 10.61 s<br>Traffic slides past the window | `a-servant-roll` @ 9.50 s<br>Hot bar in motion | Same way across the frame | orange-lit traffic ↔ a hot bar, crossing the same way (zone 17 pair) |
| 7 | 0:24.00–0:26.00 | 576–624 | 1 | sparse | **drums out, fill landing, section**<br><sub>drum stem -38→-46 dB; fill in previous bar: 3 late hits, late drum level +7.8 dB vs typical; novelty 0.77</sub> | +11.3 ms | `c-doha-sodium` @ 2.13 s<br>The ride: sodium streaks | `a-vicart-sparks` @ 5.84 s<br>Ladle over the furnace | Sodium = molten | sodium streaks through a wet windshield ↔ a ladle over the open furnace, sparks flying |
| 8 | 0:26.00–0:29.96 | 624–719 | 2 | sparse | **section**<br><sub>novelty 0.75</sub> | +20.8 ms | `t-rain-wipers` @ 18.67 s<br>Wipers | `a-hendrichs-drop` @ 5.04 s<br>Drop forge | Mechanical stroke | the wiper arm sweeps ↔ the drop-forge ram strikes |
| 9 | 0:29.96–0:31.96 | 719–767 | 1 | sparse | **section**<br><sub>novelty 1.00</sub> | -11.8 ms | `c-edison-corner` @ 0.07 s<br>Sodium corner | `a-irontap` @ 4.40 s<br>Iron tap | Sodium = molten | a sodium corner slides up ↔ iron pours from the tap: the same orange in the dark |
| 10 | 0:31.96–0:33.96 | 767–815 | 1 | break | **break, section**<br><sub>mix -8.7 dB; novelty 0.52</sub> | -20.0 ms | `t-rain-reflect` @ 2.75 s<br>Break: feet in the puddle | `a-acroni-runout` @ 3.60 s<br>The run-out slows | Same way across the frame | feet through a puddle reflection ↔ a slab easing down the run-out (zone 17 pair) |
| 11 | 0:33.96–0:35.96 | 815–863 | 1 | peak | **drums in, drop, section**<br><sub>drum stem -46→-38 dB; mix +15.4 dB; novelty 0.87</sub> | -7.7 ms | `c-amtrak95` @ 8.68 s<br>Drop: train window, gray industrial edge | `a-inland-train` @ 3.20 s<br>Mills past the train window | Window ride | Chicago industrial edge ↔ Indiana Harbor mills, both seen from a train window streaming the same way |
| 12 | 0:35.96–0:37.96 | 863–911 | 1 | peak | **base**<br><sub></sub> | -18.1 ms | `c-94-loop` @ 11.92 s<br>The L through the Loop | `a-mills-fast` @ 5.08 s<br>Hot strip races the stands | Same way across the frame | the L swings through the Loop ↔ hot strip races the stands, same direction |
| 13 | 0:37.96–0:39.96 | 911–959 | 1 | peak | **section**<br><sub>novelty 0.82</sub> | -8.6 ms | `c-harrison-arrive` @ 13.55 s<br>Train into Harrison | `a-kover-pan` @ 3.84 s<br>Billets sweep past | Same way across the frame | the subway train sweeps the platform ↔ the pan along stacked billets, same direction |
| 14 | 0:39.96–0:41.96 | 959–1007 | 1 | peak | **change**<br><sub>novelty 0.44, mix +0.8 dB</sub> | -9.1 ms | `c-94-skyline` @ 28.32 s<br>Skyline across the lot | `a-ecsteel-train` @ 7.81 s<br>Mill stacks from the train | Same way across the frame | the Chicago skyline ↔ the East Chicago smokestack skyline, both sliding the same way under a steel-blue sky |
| 15 | 0:41.96–0:44.00 | 1007–1056 | 1 | peak | **fill landing, section**<br><sub>fill in previous bar: 1 late hits, late drum level +11.3 dB vs typical; novelty 0.79</sub> | -9.5 ms | `c-94-northside` @ 13.68 s<br>Back porches from the L | `a-acroni-fast` @ 2.20 s<br>Roller table at speed | Same way across the frame | three-flats rush past the L ↔ the roller table rushes past: top speed, same direction |
| 16 | 0:44.00–0:45.96 | 1056–1103 | 1 | peak | **section**<br><sub>novelty 0.71</sub> | +6.8 ms | `c-cermak-arrive` @ 25.49 s<br>Train into Cermak | `a-drama-wire` @ 8.41 s<br>Wire rod whips past | Same way across the frame | the train sweeps into Cermak ↔ wire rod whips past, same direction |
| 17 | 0:45.96–0:48.00 | 1103–1152 | 1 | peak | **base**<br><sub></sub> | -15.4 ms | `c-ic92-freight` @ 38.97 s<br>Freight under sodium | `a-kover-fast` @ 2.32 s<br>Strip through the stands | Same way across the frame | the freight slides past under sodium ↔ hot strip slides through the stands, same direction |
| 18 | 0:48.00–0:50.00 | 1152–1200 | 1 | peak | **change**<br><sub>novelty 0.40, mix +0.4 dB</sub> | -4.1 ms | `c-impr-night-street` @ 6.76 s<br>Night street | `a-mills-roll` @ 6.92 s<br>Glowing stock drifts | Same way across the frame | night street crowd drifts ↔ glowing stock drifts, same direction |
| 19 | 0:50.00–0:52.00 | 1200–1248 | 1 | peak | **change**<br><sub>novelty 0.45, mix +1.1 dB</sub> | +0.4 ms | `c-impr-bus-lights` @ 0.58 s<br>Headlights flare | `a-vicart-sparks` @ 1.04 s<br>Sparks | Sodium = molten | headlights flare in the dark ↔ sparks shower off the furnace |
| 20 | 0:52.00–0:54.00 | 1248–1296 | 1 | peak | **fill landing, section**<br><sub>fill in previous bar: 1 late hits, late drum level +11.6 dB vs typical; novelty 0.88</sub> | -5.0 ms | `c-edison-sodium` @ 29.03 s<br>Home: sodium side streets | `a-kover-billets` @ 12.80 s<br>Billets cool on the line | Same way across the frame | sodium side streets ↔ glowing billets on the line: the same orange, drifting the same way (zone 17 pair) |
| 21 | 0:54.00–0:56.04 | 1296–1345 | 1 | release | **release, change**<br><sub>mix -21.7 dB; novelty 0.43, mix -21.7 dB</sub> | -5.5 ms | `c-impr-shelter` @ 0.33 s (holds at 2.106 s)<br>Release: the empty shelter (holds) | `a-servant-pour` @ 11.17 s<br>Ingots cool | Still glow | the lit, empty shelter ↔ ingots cooling in the dark |

## Lead variants

All three variants pass the check. The cuts are identical; only the cut frame moves.
- **lead 0:** each cut is rounded to the nearest frame, which lands it between 20 ms before and 21 ms after the downbeat. Nine of the 20 cuts fall after the hit, so the picture arrives late.
- **lead 1 (picked):** every cut falls 21–62 ms before the re-detected downbeat (median about 46 ms). None is late, and all sit inside the window where video leading the beat still reads as in sync. The kick and snare attacks come about 12 ms before the tracked downbeat, so the cut is on screen when the hit lands.
- **lead 2:** cuts fall 63–103 ms early. That is visibly ahead of the beat in the 2-bar groove shots.
Alternates: `music_split_v3_alt_lead0_480p.mp4` and `music_split_v3_alt_lead2_480p.mp4`.

## Check output (`musicsync/check_render.py`)

```
music_split_v3_lead1.mp4 lead 1: re-detected 28 downbeats, 6 pulses/bar, irregular bars []
 shot frame  aimed_at  downbeat  offset   raw   pixels  hits
   1    48    2.042    2.030  +11.3  -30.4  yes  change
   2   240   10.042   10.022  +19.5  -22.2  yes  drums_in,section
   3   336   14.042   14.028  +13.6  -28.1  yes  section
   4   432   18.042   18.029  +12.7  -29.0  yes  fill_landing,section
   5   528   22.042   22.030  +11.8  -29.9  yes  section
   6   576   24.042   24.030  +11.3  -30.4  yes  drums_out,fill_landing,section
   7   624   26.042   26.021  +20.8  -20.9  yes  section
   8   719   30.000   30.012  -11.8  -53.5  yes  section
   9   767   32.000   32.020  -20.0  -61.7  yes  break,section
  10   815   34.000   34.008   -7.7  -49.4  yes  drums_in,drop,section
  11   863   36.000   36.018  -18.1  -59.8  yes  base
  12   911   38.000   38.009   -8.6  -50.3  yes  section
  13   959   40.000   40.009   -9.1  -50.8  yes  change
  14  1007   42.000   42.010   -9.5  -51.2  yes  fill_landing,section
  15  1056   44.042   44.035   +6.8  -34.9  yes  section
  16  1103   46.000   46.015  -15.4  -57.1  yes  base
  17  1152   48.042   48.046   -4.1  -45.8  yes  change
  18  1200   50.042   50.041   +0.4  -41.3  yes  change
  19  1248   52.042   52.047   -5.0  -46.7  yes  fill_landing,section
  20  1296   54.042   54.047   -5.5  -47.2  yes  release,change
  splice 24.040: +9.7 ms to downbeat, low-end dip -2.5 dB (source -3.0 dB)
  splice 44.033: +1.4 ms to downbeat, low-end dip -22.0 dB (source -23.0 dB)
  audio: 1 stream, lag 0 samples, gain -0.01 dB, null residual -37.599998474121094 dB (worst 1 s window -28.600000381469727 dB at 33 s)
  panel 0: in-shot motion spikes (not cuts: histogram unchanged or picture does not persist): frames [630, 666, 694, 913, 1043]
  panel 1: in-shot motion spikes (not cuts: histogram unchanged or picture does not persist): frames [684, 1210, 1212, 1236]
PASS
```
