# Sky ↔ Sheen: full-song split screen (v1) shot list

`sky_sheen_full_v1.mp4` (lead 1): 1920x1080, 24 fps, 6132 frames (255.50 s). Left panel Sky (A), right panel Sheen (B), 952 px panels and a 16 px gutter (0x0b0b0c). Both panels cut on the same frames.
Audio: the full song (`song.wav`) only, untouched (no gain, no edits, no splices), AAC 256k. No clip audio.
Music: 4/4, 99 downbeats from 1.46 s to 253.48 s. The tempo drifts like a live take: bars run 2.82 s (~85 BPM) at the start and 2.40 s (~100 BPM) at the end. Real downbeat times are used; there is no fixed BPM.
Cuts: 82. Moments hit: change 35, base 16, section 15, fill landing 13, vocal in 12, drums in 7, drums out 6, drop 6, break 6, release 1.

## Arc

A day of sky mirrored by a day of sheen. Titles (sky in letters ↔ metal in letters) → first light: sunrise, pad-light bokeh and a flat horizon ↔ gallium beads, a mirror lake and crystals → the drop: wind tears the clouds ↔ soap films race → glitter → cumulus builds ↔ molds grow → storm heads and lightning ↔ slime molds → the second drop: the Earth streams past the shuttle ↔ films stream → the eye of the storm and the sun's disc ↔ spirals and sporangia → full speed: aurora and racing clouds ↔ interference bands and metal → golden hour ↔ gold molds and molten gold → fog and slick → a hush (drums out) → a lens flare ↔ a glint on the drop → night orbit ↔ metal → the sun on the Earth's rim ↔ light on a bubble's rim (drums out) → all the light at once → the last gold.

| Section | Shots | Sky zones | Sheen zones | Note |
|---|---|---|---|---|
| Titles | 1–1 | 10 | 10 | Two industrial titles: a sky made of letters, a metal made of letters |
| First light | 2–8 | 02 03 | 07 08 | Dawn and the first flares ↔ beads, mirrors and crystals waking up |
| Wind | 9–12 | 01 | 05 | The drop: wind tears the clouds ↔ soap films race |
| Glitter | 13–14 | 02 01 | 07 | Break: sun glitter ↔ light beading on metal |
| Cumulus | 15–16 | 01 | 06 | Clouds build ↔ molds grow |
| Storm and mold | 17–26 | 01 | 06 08 | Storm heads and lightning ↔ slime molds and crystals, slow |
| Orbit | 27–29 | 03 04 | 05 | The second drop: the Earth streams past the shuttle ↔ films stream |
| Eye of the storm | 30–32 | 04 | 08 06 | Break: spirals and discs from above |
| Full speed | 33–45 | 01 04 | 05 07 | Peak: aurora bands and racing clouds ↔ interference bands and metal |
| Golden hour | 46–50 | 02 | 06 07 | Groove: gold and orange skies ↔ gold molds and molten gold |
| Fog and slick | 51–59 | 01 02 | 05 07 | Peak: fog pours, clouds race ↔ oil slicks and films drift |
| Hush | 60–60 | 01 02 | 08 07 | Drums out: one slow sky ↔ one slow crystal (holds 3 bars) |
| Flare | 61–61 | 03 | 07 | Drums back in on the drop: a lens flare ↔ a glint on foil |
| Night orbit | 62–69 | 04 03 | 07 05 | Peak: night passes and aurora ↔ metal and ferrofluid |
| Rim light | 70–70 | 03 04 | 05 | Drums out: the sun on the rim of the Earth ↔ light on the rim of a bubble (holds 3 bars) |
| All the light at once | 71–82 | 01 02 03 04 | 05 06 07 08 | Final peak: everything returns at speed |
| Release | 83–83 | 02 | 06 07 | Release: the last gold |

## Link rules

Each pair is chosen for one named rule that is measured on the actual windows (motion vectors, hue, saturation and luma from a 12 fps scan). The board's 17 match-cut pairs are pinned to the moments they suit and carry their board name.

| Rule | Weight | Meaning | Uses |
|---|---|---|---|
| BOARD | 10 | one of the board's 17 match-cut pairs | 17 |
| DIR | 6.0 | the main motion crosses the frame the same way on both sides | 25 |
| VERT | 5.0 | both rise (or both fall) in frame | 5 |
| HUE | 5.0 | the same hue fills both frames | 14 |
| CHURN | 4.0 | turbulence on both sides | 2 |
| SILVER | 3.0 | black-and-white film on both sides at the same gray (weak) | 7 |
| STILL | 3.0 | both frames held still | 10 |
| FLOW | 2.0 | the same measured amount of motion (weak) | 1 |
| PACE | 1.5 | same measured pace (weak) | 1 |
| TONE | 1.0 | matched brightness and color strength (the weakest rule) (weak) | 1 |

## Beat review (override)

Beat This! doubled the pulse in three places and split one flam; each was checked against the drum stem (kick and snare onsets) and the bar lengths and fixed in `sync/override.json` (the check applies the same reviewed override to its re-detection of the render audio and also reports the raw result):

- **138.6-144.1 s:** Beat This! doubled the pulse during a drum fill (0.3 s pulses at an unchanged ~0.62 s beat). 138.57 -> 146.01 is 3 bars of 2.48 s; the true downbeats are 138.57, 141.08 and 143.48 (snare 141.03, kick 143.13 ahead). Remove the half-bar downbeats 139.82 and 142.29.
- **178.8-181.5 s:** Drums out from 176.28 to 183.94 (no kick); the trackers double the pulse and disagree from run to run (178.84 in the WAV, 179.47 in the AAC). Reviewed grid: 3 even bars of 2.551 s, downbeats 176.28, 178.84, 181.39, 183.94. Shot 59 holds across all three bars, so no cut depends on the inner downbeats.
- **203.2-208.8 s:** Drums drop out after the strong kick at 203.77 s and the pulse doubles. Reviewed grid: 2 bars, downbeats 203.80, 206.31 (the drums-out moment), 208.82.
- **131.0 s:** Flam on the downbeat: onsets at 131.01, 131.037 (strongest in the mix and the drum stem, kick at ~131.03) and 131.072. The source refinement picked 131.072, the render audio picked 131.037. Move the pulse to 131.037 so both agree on the real hit.
- Edits: removed 139.82, 142.29 s; moved 131.072→131.037 s; reviewed grids 176.28–183.94 s (downbeats 176.28, 178.84, 181.39, 183.94); 203.80–208.82 s (downbeats 203.80, 206.31, 208.82). Result: 0 irregular bars (the raw run had 10).
- Downbeats still under 0.5 confidence (kept after review: the bar lengths stay regular through them): 120.98 s (0.47), 126.05 s (0.35), 178.84 s (0.01), 181.39 s (0.35), 201.42 s (0.42), 206.31 s (0.11), 208.82 s (0.15).

## Shots

| # | Time | Frames | Bars | Energy | Section | Moment hit | Offset vs re-detected downbeat | Sky (left) | Sheen (right) | Rule | Why this pair |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 0:00.00–0:09.88 | 0–237 | 3 | sparse | Titles | **start**<br><sub></sub> | start | `a-pipeline-title` @ 0.00 s<br><sub>"Pipeline to the Clouds" title in cloud letters, GE 1951 (1951)</sub> | `b-alu-title` @ 9.92 s<br><sub>Chrome title cards: "Aluminum on the March", Reynolds Metals 1956 (1956)</sub> | TYPE RHYME | board pair 12: "Pipeline to the Clouds" (GE, 1951); "Aluminum on the March" (Reynolds, 1956). Two industrial titles, sky and metal. |
| 2 | 0:09.88–0:12.71 | 237–305 | 1 | sparse | First light | **drums in**<br><sub>drum stem -88→-72 dB</sub> | -10.7 ms | `a-shuttle-bokeh` @ 8.42 s<br><sub>Pad lights and bokeh before dawn (2009)</sub> | `b-gallium-drops` @ 6.67 s<br><sub>Gallium drops merging (2015)</sub> | BOKEH → BEADS | board pair 04: Out-of-focus pad lights before dawn become beads of liquid gallium. |
| 3 | 0:12.71–0:18.25 | 305–438 | 2 | sparse | First light | **section**<br><sub>novelty 0.52</sub> | -6.0 ms | `a-pipeline-flare` @ 2.33 s<br><sub>Sun flare over a silhouetted ridge, 1951 (1951)</sub> | `b-crystal-grow` @ 5.00 s<br><sub>Crystal growing under the microscope, 1958 (1958)</sub> | STILL HOLD | both near-still (flow 0.24 / 0.15 px/s) |
| 4 | 0:18.25–0:20.96 | 438–503 | 1 | sparse | First light | **vocal in, change**<br><sub>novelty 0.30, mix +17.1 dB</sub> | +3.3 ms | `a-masada` @ 15.83 s<br><sub>Sunrise over the Dead Sea from Masada, 2008 (PAL video) (2008)</sub> | `b-rainier-mirror` @ 8.17 s<br><sub>Mirror lake under the peaks, 1920 (tinted) (1920)</sub> | HORIZON LINE | board pair 10: A flat Dead Sea sunrise horizon; a still mountain lake mirroring its peaks in 1920. |
| 5 | 0:20.96–0:23.75 | 503–570 | 1 | sparse | First light | **drums out, change**<br><sub>drum stem -31→-63 dB; novelty 0.30, mix -4.4 dB</sub> | -17.2 ms | `a-shuttle-sunrise` @ 9.17 s<br><sub>Sunrise behind the shuttle pads (2009)</sub> | `b-crystal-melt` @ 9.50 s<br><sub>Crystals forming in a drop, 1958 (1958)</sub> | DIRECTION CARRY · R→L | subject motion -10 / -11 px/s, both R→L (94% / 74% of samples agree) |
| 6 | 0:23.75–0:29.21 | 570–701 | 2 | sparse | First light | **drums in, change**<br><sub>drum stem -63→-30 dB; novelty 0.41, mix +1.1 dB</sub> | -14.2 ms | `a-aurora-pd` @ 9.17 s<br><sub>Northern lights over power lines, 2011 (720×480) (2011)</sub> | `b-gallium-heart` @ 11.67 s<br><sub>Gallium beating heart (2015)</sub> | HUE LOCK · ORANGE | hue 21° / 40° (Δ19°), saturation 108 / 224 |
| 7 | 0:29.21–0:31.83 | 701–764 | 1 | groove | First light | **vocal in, section**<br><sub>novelty 0.56</sub> | +11.5 ms | `a-cep-redsky` @ 0.00 s<br><sub>Red sky at morning (2006)</sub> | `b-alu-sheet` @ 0.00 s<br><sub>Sheet aluminum rippling past, 1956 (1956)</sub> | DIRECTION CARRY · R→L | subject motion -20 / -14 px/s, both R→L (100% / 75% of samples agree) |
| 8 | 0:31.83–0:34.62 | 764–831 | 1 | sparse | First light | **drums out**<br><sub>drum stem -30→-66 dB</sub> | -2.6 ms | `a-mcdonald` @ 3.00 s<br><sub>River crossing at golden hour (2015)</sub> | `b-oilwater` @ 19.17 s<br><sub>Water and sunflower oil on a magnetic stirrer (2015)</sub> | HUE LOCK · MAGENTA | hue 328° / 344° (Δ16°), saturation 57 / 73 |
| 9 | 0:34.62–0:37.29 | 831–895 | 1 | peak | Wind | **drums in, drop, section**<br><sub>drum stem -66→-31 dB; mix +7.9 dB; novelty 0.59</sub> | +10.5 ms | `a-cep-wind` @ 0.00 s<br><sub>Wind-torn clouds (2006)</sub> | `b-soap-4` @ 17.25 s<br><sub>Soap-film swirls (2020)</sub> | DIRECTION CARRY · L→R | board pair 02: Wind tears the clouds left to right at full speed; soap-film bands race the same way. Measured: subject motion +109 / +62 px/s, both L→R (100% / 100% of samples agree) (passes the DIR check). |
| 10 | 0:37.29–0:40.00 | 895–960 | 1 | groove | Wind | **change**<br><sub>novelty 0.44, mix -3.9 dB</sub> | -1.8 ms | `a-power-mackerel` @ 1.67 s<br><sub>Mackerel sky, silent era (1920)</sub> | `b-myxo-plasmodium` @ 15.83 s<br><sub>Plasmodium net, time-lapse 1931 (1931)</sub> | CHURN RHYME | both tagged churn/swirl, measured flow 2.3 / 6.9 |
| 11 | 0:40.00–0:42.67 | 960–1024 | 1 | groove | Wind | **change**<br><sub>novelty 0.40, mix +3.0 dB</sub> | +7.7 ms | `a-power-lake` @ 2.17 s<br><sub>Cloud bank over a lake (1920)</sub> | `b-myxo-cluster` @ 0.00 s<br><sub>Clustered sporangia, 1931 (1931)</sub> | SILVER LOCK (weak) | both black-and-white film (saturation 0 / 0), matched gray (luma 56 / 56) |
| 12 | 0:42.67–0:45.29 | 1024–1087 | 1 | peak | Wind | **change**<br><sub>novelty 0.45, mix +0.6 dB</sub> | -4.6 ms | `a-ext-bellevue` @ 7.17 s<br><sub>Clouds over Bellevue Canyon (2017)</sub> | `b-oilslick-surface` @ 14.50 s<br><sub>Oil-streaked surface water, Santa Barbara 1969 (1969)</sub> | DIRECTION CARRY · L→R | subject motion +22 / +61 px/s, both L→R (85% / 100% of samples agree) |
| 13 | 0:45.29–0:47.96 | 1087–1151 | 1 | break | Glitter | **drums out, break, vocal in, change**<br><sub>drum stem -30→-63 dB; mix -8.6 dB; novelty 0.28, mix -8.6 dB</sub> | +16.3 ms | `a-usda-sunwater` @ 5.83 s<br><sub>Sun on water, 1920 (1920)</sub> | `b-alfin-drops` @ 4.42 s<br><sub>Beads on anodized metal, 1956 (1956)</sub> | SPECULAR SUN | board pair 13: Sun glitter on water, 1920; light beading on anodized metal, 1956. |
| 14 | 0:47.96–0:50.71 | 1151–1217 | 1 | break | Glitter | **change**<br><sub>novelty 0.31, mix -13.1 dB</sub> | +4.1 ms | `a-vancouver95` @ 3.67 s<br><sub>Overcast churn, 1995 camcorder (1995)</sub> | `b-bubble-burst2` @ 2.83 s<br><sub>Large bubble bursting, 40× slow motion (2019)</sub> | DIRECTION CARRY · R→L | subject motion -7 / -8 px/s, both R→L (85% / 97% of samples agree) |
| 15 | 0:50.71–1:01.25 | 1217–1470 | 4 | sparse | Cumulus | **drums in, change**<br><sub>drum stem -69→-29 dB; novelty 0.50, mix +12.4 dB</sub> | +20.3 ms | `a-usda-heap` @ 3.33 s<br><sub>Heaped cumulus over the field (1920)</sub> | `b-penicillium` @ 0.00 s<br><sub>Penicillium vulpinum fruiting, time-lapse (2020)</sub> | GROWTH FRONT | board pair 07: A cumulus heap builds upward in 1920; a Penicillium fruiting body pushes up out of its colony. |
| 16 | 1:01.25–1:06.54 | 1470–1597 | 2 | groove | Cumulus | **vocal in, change**<br><sub>novelty 0.28, mix +4.7 dB</sub> | +11.0 ms | `a-rainier-sea` @ 0.00 s<br><sub>Sea of clouds below Camp Muir, 1920 (tinted) (1920)</sub> | `b-myxo-front` @ 0.00 s<br><sub>Advancing plasmodium front, time-lapse 1931 (1931)</sub> | EDGE RHYME | board pair 08: The tinted edge of a cloud sea below Rainier; the lacy advancing edge of a slime mold. |
| 17 | 1:06.54–1:09.21 | 1597–1661 | 1 | break | Storm and mold | **break, change**<br><sub>mix -5.3 dB; novelty 0.00, mix -5.3 dB</sub> | -20.3 ms | `a-pipeline-storm` @ 0.00 s<br><sub>Storm heads building, 1951 (1951)</sub> | `b-myxo-veins` @ 9.58 s<br><sub>Vein network pulsing, 1931 (1931)</sub> | BRANCH RHYME | board pair 06: Lightning forks under a storm head; plasmodium veins fork across the dish. |
| 18 | 1:09.21–1:11.83 | 1661–1724 | 1 | break | Storm and mold | **base**<br><sub></sub> | -12.6 ms | `a-cep453` @ 21.00 s<br><sub>Backlit cumulus, time-lapse (2007)</sub> | `b-physarum-au` @ 9.17 s<br><sub>Physarum crossing bark, time-lapse (2021)</sub> | DIRECTION CARRY · L→R | subject motion +6 / +7 px/s, both L→R (73% / 76% of samples agree) |
| 19 | 1:11.83–1:14.50 | 1724–1788 | 1 | break | Storm and mold | **vocal in, change**<br><sub>novelty 0.26, mix +5.2 dB</sub> | -6.6 ms | `a-usda-cumulus` @ 12.00 s<br><sub>Cumulus tower, 1920 USDA film (1920)</sub> | `b-myxo-dish` @ 11.17 s<br><sub>Slime mold on a dish, 1931 (1931)</sub> | SILVER LOCK (weak) | both black-and-white film (saturation 0 / 0), matched gray (luma 39 / 64) |
| 20 | 1:14.50–1:17.12 | 1788–1851 | 1 | break | Storm and mold | **base**<br><sub></sub> | -8.9 ms | `a-fowler-nm` @ 12.17 s<br><sub>Cloud time-lapse, New Mexico (2013)</sub> | `b-crystal-balls` @ 2.50 s<br><sub>Ball-bearing crystal lattice, 1958 (1958)</sub> | STILL HOLD | both near-still (flow 0.07 / 1.00 px/s) |
| 21 | 1:17.12–1:19.75 | 1851–1914 | 1 | break | Storm and mold | **base**<br><sub></sub> | +7.1 ms | `a-cep-boil` @ 16.50 s<br><sub>Boiling clouds (C. E. Price) (2006)</sub> | `b-opal` @ 2.33 s<br><sub>Opal play of color (2012)</sub> | VERTICAL CARRY · FALL | vertical motion +7 / +9 px/s, both down |
| 22 | 1:19.75–1:22.42 | 1914–1978 | 1 | break | Storm and mold | **change**<br><sub>novelty 0.49, mix -4.3 dB</sub> | +13.0 ms | `a-usda-silver` @ 0.83 s<br><sub>Silver-lined cloud edge (1920)</sub> | `b-physarum-flow` @ 18.33 s<br><sub>Shuttle streaming inside Physarum (2021)</sub> | STILL HOLD | both near-still (flow 0.98 / 0.57 px/s) |
| 23 | 1:22.42–1:25.00 | 1978–2040 | 1 | break | Storm and mold | **change**<br><sub>novelty 0.38, mix +4.0 dB</sub> | +5.7 ms | `a-cep431` @ 3.83 s<br><sub>Sunset with clouds (C. E. Price) (2007)</sub> | `b-slime-phy` @ 2.33 s<br><sub>Slime mold foraging, time-lapse (2013)</sub> | HUE LOCK · GOLD | hue 54° / 63° (Δ9°), saturation 52 / 63 |
| 24 | 1:25.00–1:27.54 | 2040–2101 | 1 | break | Storm and mold | **base**<br><sub></sub> | -15.0 ms | `a-cep386` @ 0.00 s<br><sub>Fair-weather cumulus, time-lapse (2007)</sub> | `b-bubble-freeze` @ 18.67 s<br><sub>Soap bubble freezing in Minnesota cold (2023)</sub> | STILL HOLD | both near-still (flow 0.66 / 0.15 px/s) |
| 25 | 1:27.54–1:29.88 | 2101–2157 | 1 | break | Storm and mold | **drums out, break, vocal in, change**<br><sub>drum stem -30→-65 dB; mix -9.6 dB; novelty 0.31, mix -9.6 dB</sub> | -12.6 ms | `a-usda-thunder` @ 1.50 s<br><sub>Backlit thunderhead, 1920 USDA film (1920)</sub> | `b-soapy-cc0` @ 4.83 s<br><sub>Iridescence in soapy water (2014)</sub> | STILL HOLD | both near-still (flow 0.21 / 0.24 px/s) |
| 26 | 1:29.88–1:32.67 | 2157–2224 | 1 | break | Storm and mold | **change**<br><sub>novelty 0.00, mix -14.6 dB</sub> | -18.9 ms | `a-goes-idalia` @ 0.67 s<br><sub>Sunrise on Hurricane Idalia, GOES-16 (2015)</sub> | `b-nacl` @ 21.33 s<br><sub>Salt crystal dissolving, microscope (2016)</sub> | VERTICAL CARRY · RISE | vertical motion -7 / -9 px/s, both up |
| 27 | 1:32.67–1:35.21 | 2224–2285 | 1 | groove | Orbit | **drop, section**<br><sub>mix +23.6 dB; novelty 1.00</sub> | +9.0 ms | `a-hsf81` @ 0.00 s<br><sub>Earth limb from the shuttle, STS-81 1997 (1997)</sub> | `b-soap-7` @ 0.00 s<br><sub>Soap-film cells breaking into foam (2020)</sub> | PACE MATCH · 5 | board pair 11: The Earth streams past the shuttle window; soap-film cells stream and break into foam. |
| 28 | 1:35.21–1:37.83 | 2285–2348 | 1 | groove | Orbit | **section**<br><sub>novelty 0.83</sub> | -13.5 ms | `a-iss-airglow` @ 0.00 s<br><sub>Airglow band and lightning (2013)</sub> | `b-alu-rain` @ 0.00 s<br><sub>Rain on aluminum, 1956 (1956)</sub> | DIRECTION CARRY · L→R | subject motion +74 / +55 px/s, both L→R (100% / 75% of samples agree) |
| 29 | 1:37.83–1:40.42 | 2348–2410 | 1 | groove | Orbit | **drums in, vocal in, change**<br><sub>drum stem -68→-28 dB; novelty 0.47, mix -2.0 dB</sub> | -12.5 ms | `a-iss-aurora` @ 0.00 s<br><sub>Aurora Australis from the ISS, 2011 (2011)</sub> | `b-alu-run` @ 0.83 s<br><sub>Bright sheet running through the rolls, 1956 (1956)</sub> | DIRECTION CARRY · L→R | subject motion +11 / +22 px/s, both L→R (77% / 72% of samples agree) |
| 30 | 1:40.42–1:43.00 | 2410–2472 | 1 | break | Eye of the storm | **break, change**<br><sub>mix -13.5 dB; novelty 0.00, mix -13.5 dB</sub> | -3.4 ms | `a-iss-hurricane` @ 13.17 s<br><sub>Hurricane eye from the ISS (2013)</sub> | `b-vitc` @ 26.67 s<br><sub>Vitamin C crystallizing under polarized light (2025)</sub> | SPIRAL | board pair 14: A hurricane eye from orbit; vitamin C crystals radiating in polarized light. |
| 31 | 1:43.00–1:45.54 | 2472–2533 | 1 | break | Eye of the storm | **change**<br><sub>novelty 0.00, mix +9.7 dB</sub> | +5.9 ms | `a-iss-daynight` @ 19.33 s<br><sub>Day into night over the terminator (2025)</sub> | `b-crystal-grow` @ 14.17 s<br><sub>Crystal growing under the microscope, 1958 (1958) · use 2</sub> | STILL HOLD | both near-still (flow 0.02 / 0.20 px/s) |
| 32 | 1:45.54–1:48.17 | 2533–2596 | 1 | break | Eye of the storm | **break, change**<br><sub>mix -14.3 dB; novelty 0.28, mix -14.3 dB</sub> | +3.3 ms | `a-sdo-blast` @ 2.50 s<br><sub>Flare and coronal ejection, SDO (2012)</sub> | `b-myxo-sphere` @ 4.00 s<br><sub>Sporangium sphere, 1931 (1931)</sub> | SHAPE RHYME · DISC | board pair 03: The sun as a red disc in extreme ultraviolet; a slime-mold sporangium as a gray disc in 1931. |
| 33 | 1:48.17–1:50.75 | 2596–2658 | 1 | peak | Full speed | **drop, change**<br><sub>mix +20.6 dB; novelty 0.27, mix +20.6 dB</sub> | -20.7 ms | `a-iss-aurora-v` @ 3.00 s<br><sub>Aurora curtain from the ISS (2013)</sub> | `b-soap-1` @ 6.00 s<br><sub>Soap-film thin-film bands (2020)</sub> | COLOR BAND | board pair 09: Aurora curtains ripple as green bands; thin-film interference ripples as rainbow bands. |
| 34 | 1:50.75–1:53.29 | 2658–2719 | 1 | peak | Full speed | **fill landing**<br><sub>fill in previous bar: 1 late hits, late drum level +5.3 dB vs typical</sub> | +13.5 ms | `a-tl-office` @ 7.83 s<br><sub>Clouds over an office block, 2006 webcam time-lapse (2006)</sub> | `b-alfin-octa` @ 7.33 s<br><sub>Faceted shapes turning, 1956 (1956)</sub> | DIRECTION CARRY · R→L | subject motion -68 / -152 px/s, both R→L (100% / 88% of samples agree) |
| 35 | 1:53.29–1:55.88 | 2719–2781 | 1 | peak | Full speed | **vocal in, fill landing, change**<br><sub>fill in previous bar: 2 late hits, late drum level +4.1 dB vs typical; novelty 0.00, mix +3.3 dB</sub> | -14.1 ms | `a-bresson-day` @ 19.17 s<br><sub>Clouds over Belfort (2011)</sub> | `b-soap-micro` @ 5.50 s<br><sub>Soap film under the microscope (2018)</sub> | HUE LOCK · BLUE | hue 214° / 206° (Δ9°), saturation 61 / 161 |
| 36 | 1:55.88–1:58.42 | 2781–2842 | 1 | peak | Full speed | **fill landing**<br><sub>fill in previous bar: 3 late hits, late drum level +4.3 dB vs typical</sub> | -9.8 ms | `a-ext-rimrock` @ 0.83 s ×1.5<br><sub>Winter clouds roiling over a rim (2017)</sub> | `b-ferro-ug` @ 11.00 s<br><sub>Ferrofluid in simulated microgravity (PAL) (2013)</sub> | DIRECTION CARRY · L→R | subject motion +33 / +33 px/s, both L→R (100% / 100% of samples agree) |
| 37 | 1:58.42–2:00.92 | 2842–2902 | 1 | groove | Full speed | **base**<br><sub></sub> | -2.5 ms | `a-gc-summer` @ 0.50 s<br><sub>Summer clouds over the Grand Canyon (2015)</sub> | `b-alu-sheet` @ 4.50 s<br><sub>Sheet aluminum rippling past, 1956 (1956) · use 2</sub> | HUE LOCK · RED-ORANGE | hue 14° / 355° (Δ19°), saturation 72 / 54 |
| 38 | 2:00.92–2:03.46 | 2902–2963 | 1 | groove | Full speed | **base**<br><sub></sub> | -16.8 ms | `a-pipeline-sea` @ 0.00 s<br><sub>Cloud sea from above, 1951 Technicolor (1951)</sub> | `b-alfin-mesh` @ 0.00 s<br><sub>Expanded-metal mesh, 1956 (1956)</sub> | PACE MATCH · 3 (weak) | both measured at pace 3 (board tag, speed-adjusted) |
| 39 | 2:03.46–2:06.00 | 2963–3024 | 1 | peak | Full speed | **vocal in, change**<br><sub>novelty 0.00, mix +3.9 dB</sub> | -19.3 ms | `a-cep-storm` @ 12.00 s ×2.0<br><sub>Approaching thunderstorm (2006)</sub> | `b-oilslick-surface` @ 17.83 s<br><sub>Oil-streaked surface water, Santa Barbara 1969 (1969) · use 2</sub> | DIRECTION CARRY · L→R | subject motion +26 / +54 px/s, both L→R (89% / 100% of samples agree) |
| 40 | 2:06.00–2:08.50 | 3024–3084 | 1 | peak | Full speed | **base**<br><sub></sub> | -6.8 ms | `a-cep366` @ 13.67 s ×1.5<br><sub>Cloud rows rolling, time-lapse (2007)</sub> | `b-rainier-mirror` @ 3.67 s ×1.5<br><sub>Mirror lake under the peaks, 1920 (tinted) (1920) · use 2</sub> | DIRECTION CARRY · R→L | subject motion -25 / -24 px/s, both R→L (100% / 100% of samples agree) |
| 41 | 2:08.50–2:11.00 | 3084–3144 | 1 | peak | Full speed | **base**<br><sub></sub> | -11.1 ms | `a-clouds2005` @ 12.00 s<br><sub>Altocumulus drift, 2005 video (2005)</sub> | `b-soap-4` @ 20.50 s<br><sub>Soap-film swirls (2020) · use 2</sub> | HUE LOCK · BLUE | hue 228° / 224° (Δ4°), saturation 60 / 180 |
| 42 | 2:11.00–2:13.58 | 3144–3206 | 1 | groove | Full speed | **change**<br><sub>novelty 0.39, mix -3.7 dB</sub> | +4.7 ms | `a-iss-night` @ 31.00 s<br><sub>City lights streaming below, ISS night pass (2025)</sub> | `b-soapy-cc0` @ 0.00 s<br><sub>Iridescence in soapy water (2014) · use 2</sub> | VERTICAL CARRY · RISE | vertical motion -16 / -11 px/s, both up |
| 43 | 2:13.58–2:16.04 | 3206–3265 | 1 | peak | Full speed | **change**<br><sub>novelty 0.43, mix +4.4 dB</sub> | +8.7 ms | `a-tl-pink` @ 1.17 s<br><sub>Pink-lit clouds, 2006 webcam time-lapse (2006)</sub> | `b-soap-7` @ 8.50 s<br><sub>Soap-film cells breaking into foam (2020) · use 2</sub> | DIRECTION CARRY · R→L | subject motion -87 / -35 px/s, both R→L (97% / 74% of samples agree) |
| 44 | 2:16.04–2:18.54 | 3265–3325 | 1 | peak | Full speed | **base**<br><sub></sub> | +2.6 ms | `a-iss-illum` @ 17.33 s<br><sub>Earth Illuminated: aurora and city lights (2012)</sub> | `b-alu-run` @ 6.50 s<br><sub>Bright sheet running through the rolls, 1956 (1956) · use 2</sub> | HUE LOCK · GOLD | hue 48° / 48° (Δ0°), saturation 87 / 62 |
| 45 | 2:18.54–2:21.04 | 3325–3385 | 1 | peak | Full speed | **vocal in**<br><sub></sub> | +18.2 ms | `a-bresson-eve` @ 14.00 s<br><sub>Evening clouds to moonrise (2011)</sub> | `b-alu-rain` @ 21.33 s<br><sub>Rain on aluminum, 1956 (1956) · use 2</sub> | VERTICAL CARRY · RISE | vertical motion -28 / -59 px/s, both up |
| 46 | 2:21.04–2:23.42 | 3385–3442 | 1 | groove | Golden hour | **base**<br><sub></sub> | +3.9 ms | `a-power-lake` @ 5.50 s<br><sub>Cloud bank over a lake (1920) · use 2</sub> | `b-myxo-stream` @ 0.00 s<br><sub>Cytoplasm streaming, microscopy 1931 (1931)</sub> | SILVER LOCK (weak) | both black-and-white film (saturation 0 / 0), matched gray (luma 51 / 64) |
| 47 | 2:23.42–2:25.96 | 3442–3503 | 1 | groove | Golden hour | **section**<br><sub>novelty 0.68</sub> | -20.6 ms | `a-jt-sunset` @ 0.00 s<br><sub>Joshua Tree clouds at sunset (2021)</sub> | `b-physarum-tl` @ 0.00 s<br><sub>Physarum spreading, time-lapse (2022)</sub> | HUE LOCK · GOLD | board pair 15: Golden-hour clouds over Joshua Tree; a yellow Physarum spreading over oat flakes. Measured: hue 47° / 43° (Δ4°), saturation 71 / 187 (passes the HUE check). |
| 48 | 2:25.96–2:28.46 | 3503–3563 | 1 | groove | Golden hour | **section**<br><sub>novelty 0.73</sub> | -3.2 ms | `a-usda-biplane` @ 0.00 s<br><sub>Biplane crossing a cloud bank (1920)</sub> | `b-myxo-plasmodium` @ 19.17 s<br><sub>Plasmodium net, time-lapse 1931 (1931) · use 2</sub> | SILVER LOCK (weak) | both black-and-white film (saturation 0 / 0), matched gray (luma 34 / 46) |
| 49 | 2:28.46–2:31.04 | 3563–3625 | 1 | groove | Golden hour | **section**<br><sub>novelty 0.61</sub> | -2.5 ms | `a-cep427` @ 0.00 s<br><sub>Afterglow (2007)</sub> | `b-gold-dendrite` @ 0.00 s<br><sub>Molten gold crusting into dendrites (2024)</sub> | HUE LOCK · ORANGE | board pair 01: Afterglow fills the sky with orange; molten gold fills the crucible with the same orange as it crusts over. Measured: hue 42° / 24° (Δ18°), saturation 112 / 251 (passes the HUE check). |
| 50 | 2:31.04–2:33.58 | 3625–3686 | 1 | groove | Golden hour | **section**<br><sub>novelty 0.52</sub> | +6.7 ms | `a-usda-sunwater` @ 0.00 s<br><sub>Sun on water, 1920 (1920) · use 2</sub> | `b-mold-colonies` @ 1.83 s<br><sub>Penicillium colonies on a dish, 1952 (1952)</sub> | SILVER LOCK (weak) | both black-and-white film (saturation 0 / 10), matched gray (luma 60 / 76) |
| 51 | 2:33.58–2:36.17 | 3686–3748 | 1 | peak | Fog and slick | **drop, vocal in, section**<br><sub>mix +7.4 dB; novelty 0.51</sub> | +4.1 ms | `a-gg-fog` @ 13.75 s<br><sub>Fog pouring past the Golden Gate (2007)</sub> | `b-oilslick-aerial` @ 15.92 s ×1.5<br><sub>Slick from the air, Santa Barbara 1969 (1969)</sub> | DIRECTION CARRY · R→L | board pair 16: Fog pours right to left past the Golden Gate; the 1969 Santa Barbara slick drifts the same way. Measured: subject motion -40 / -21 px/s, both R→L (100% / 88% of samples agree) (passes the DIR check). |
| 52 | 2:36.17–2:38.71 | 3748–3809 | 1 | peak | Fog and slick | **base**<br><sub></sub> | -1.7 ms | `a-bresson-night` @ 5.00 s ×2.0<br><sub>Orange night clouds over the city (2011)</sub> | `b-alfin-octa` @ 11.00 s<br><sub>Faceted shapes turning, 1956 (1956) · use 2</sub> | DIRECTION CARRY · R→L | subject motion -46 / -133 px/s, both R→L (100% / 91% of samples agree) |
| 53 | 2:38.71–2:41.21 | 3809–3869 | 1 | peak | Fog and slick | **base**<br><sub></sub> | +0.8 ms | `a-cep-wind` @ 3.33 s<br><sub>Wind-torn clouds (2006) · use 2</sub> | `b-soap-1` @ 17.00 s<br><sub>Soap-film thin-film bands (2020) · use 2</sub> | DIRECTION CARRY · L→R | subject motion +109 / +93 px/s, both L→R (100% / 74% of samples agree) |
| 54 | 2:41.21–2:43.75 | 3869–3930 | 1 | peak | Fog and slick | **base**<br><sub></sub> | -13.5 ms | `a-ext-bellevue` @ 11.83 s<br><sub>Clouds over Bellevue Canyon (2017) · use 2</sub> | `b-soap-micro` @ 8.83 s<br><sub>Soap film under the microscope (2018) · use 2</sub> | DIRECTION CARRY · L→R | subject motion +25 / +24 px/s, both L→R (88% / 75% of samples agree) |
| 55 | 2:43.75–2:46.25 | 3930–3990 | 1 | peak | Fog and slick | **section**<br><sub>novelty 0.52</sub> | -16.0 ms | `a-winchester` @ 6.50 s<br><sub>Sun flaring through clouds, Winchester (640×480) (2010)</sub> | `b-ferro-ug` @ 4.33 s<br><sub>Ferrofluid in simulated microgravity (PAL) (2013) · use 2</sub> | DIRECTION CARRY · R→L | subject motion -157 / -11 px/s, both R→L (100% / 84% of samples agree) |
| 56 | 2:46.25–2:48.79 | 3990–4051 | 1 | peak | Fog and slick | **section**<br><sub>novelty 0.66</sub> | -15.3 ms | `a-rainier-sea` @ 6.00 s<br><sub>Sea of clouds below Camp Muir, 1920 (tinted) (1920) · use 2</sub> | `b-oilslick-surface` @ 21.00 s<br><sub>Oil-streaked surface water, Santa Barbara 1969 (1969) · use 3</sub> | DIRECTION CARRY · L→R | subject motion +23 / +50 px/s, both L→R (100% / 100% of samples agree) |
| 57 | 2:48.79–2:51.25 | 4051–4110 | 1 | peak | Fog and slick | **section**<br><sub>novelty 0.56</sub> | +2.0 ms | `a-ext-rimrock` @ 5.33 s ×1.5<br><sub>Winter clouds roiling over a rim (2017) · use 2</sub> | `b-soap-4` @ 23.67 s<br><sub>Soap-film swirls (2020) · use 3</sub> | DIRECTION CARRY · L→R | subject motion +37 / +72 px/s, both L→R (100% / 100% of samples agree) |
| 58 | 2:51.25–2:53.71 | 4110–4169 | 1 | groove | Fog and slick | **change**<br><sub>novelty 0.41, mix -2.6 dB</sub> | -4.0 ms | `a-vancouver95` @ 0.00 s<br><sub>Overcast churn, 1995 camcorder (1995) · use 2</sub> | `b-myxo-spores` @ 0.00 s<br><sub>Spores bursting free, 1931 (1931)</sub> | SILVER LOCK (weak) | both black-and-white film (saturation 19 / 0), matched gray (luma 137 / 116) |
| 59 | 2:53.71–2:56.25 | 4169–4230 | 1 | peak | Fog and slick | **vocal in, change**<br><sub>novelty 0.46, mix +1.5 dB</sub> | -10.1 ms | `a-tl-office` @ 13.67 s<br><sub>Clouds over an office block, 2006 webcam time-lapse (2006) · use 2</sub> | `b-soap-7` @ 15.50 s<br><sub>Soap-film cells breaking into foam (2020) · use 3</sub> | HUE LOCK · GREEN | hue 113° / 106° (Δ8°), saturation 61 / 139 |
| 60 | 2:56.25–3:03.88 | 4230–4413 | 3 | sparse | Hush | **drums out, change**<br><sub>drum stem -59→-67 dB; novelty 0.00, mix -3.3 dB</sub> | +7.3 ms | `a-63n` @ 1.33 s<br><sub>Sunrise at 63°N (2011)</sub> | `b-oilwater` @ 10.83 s<br><sub>Water and sunflower oil on a magnetic stirrer (2015) · use 2</sub> | HUE LOCK · MAGENTA | hue 324° / 343° (Δ19°), saturation 86 / 73 |
| 61 | 3:03.88–3:06.42 | 4413–4474 | 1 | peak | Flare | **drums in, drop, change**<br><sub>drum stem -66→-20 dB; mix +6.4 dB; novelty 0.29, mix +6.4 dB</sub> | -20.3 ms | `a-hsf87-flare` @ 12.00 s<br><sub>Orbital sunrise starburst, STS-87 crew video 1997 (1997)</sub> | `b-alfin-foil` @ 1.67 s<br><sub>Crumpled foil glinting, 1956 (1956)</sub> | FLARE → GLINT | board pair 05: A starburst flares as the sun clears the Earth; crumpled foil throws the same hard glints in 1956. |
| 62 | 3:06.42–3:08.92 | 4474–4534 | 1 | peak | Night orbit | **fill landing**<br><sub>fill in previous bar: 1 late hits, late drum level +6.1 dB vs typical</sub> | +2.1 ms | `a-iss-aurora` @ 13.83 s ×2.0<br><sub>Aurora Australis from the ISS, 2011 (2011) · use 2</sub> | `b-alu-run` @ 12.17 s<br><sub>Bright sheet running through the rolls, 1956 (1956) · use 3</sub> | DIRECTION CARRY · L→R | subject motion +26 / +22 px/s, both L→R (76% / 100% of samples agree) |
| 63 | 3:08.92–3:11.46 | 4534–4595 | 1 | peak | Night orbit | **fill landing**<br><sub>fill in previous bar: 1 late hits, late drum level +6.4 dB vs typical</sub> | -12.2 ms | `a-hsf81` @ 3.17 s<br><sub>Earth limb from the shuttle, STS-81 1997 (1997) · use 2</sub> | `b-gallium-drops` @ 0.17 s ×1.5<br><sub>Gallium drops merging (2015) · use 2</sub> | HUE LOCK · CYAN | hue 179° / 171° (Δ8°), saturation 87 / 124 |
| 64 | 3:11.46–3:13.96 | 4595–4655 | 1 | peak | Night orbit | **fill landing**<br><sub>fill in previous bar: 1 late hits, late drum level +4.8 dB vs typical</sub> | +0.2 ms | `a-arches` @ 12.50 s ×2.0<br><sub>Balanced Rock at sunset (2015)</sub> | `b-gold-dendrite` @ 8.00 s<br><sub>Molten gold crusting into dendrites (2024) · use 2</sub> | HUE LOCK · RED-ORANGE | hue 7° / 27° (Δ20°), saturation 121 / 254 |
| 65 | 3:13.96–3:16.42 | 4655–4714 | 1 | peak | Night orbit | **fill landing**<br><sub>fill in previous bar: 1 late hits, late drum level +4.9 dB vs typical</sub> | +15.9 ms | `a-iss-airglow` @ 4.00 s<br><sub>Airglow band and lightning (2013) · use 2</sub> | `b-alu-rain` @ 24.50 s<br><sub>Rain on aluminum, 1956 (1956) · use 3</sub> | HUE LOCK · BLUE | hue 219° / 227° (Δ8°), saturation 96 / 128 |
| 66 | 3:16.42–3:18.92 | 4714–4774 | 1 | groove | Night orbit | **change**<br><sub>novelty 0.38, mix -2.3 dB</sub> | -0.2 ms | `a-sdo-flare` @ 0.00 s<br><sub>Solar flare in 131 Å, SDO (2012)</sub> | `b-opal` @ 11.83 s<br><sub>Opal play of color (2012) · use 2</sub> | STILL HOLD | both near-still (flow 0.75 / 0.00 px/s) |
| 67 | 3:18.92–3:21.38 | 4774–4833 | 1 | peak | Night orbit | **change**<br><sub>novelty 0.48, mix +2.7 dB</sub> | -9.5 ms | `a-bresson-eve` @ 5.17 s<br><sub>Evening clouds to moonrise (2011) · use 2</sub> | `b-oilslick-aerial` @ 22.00 s ×1.5<br><sub>Slick from the air, Santa Barbara 1969 (1969) · use 2</sub> | HUE LOCK · BLUE | hue 227° / 222° (Δ5°), saturation 86 / 135 |
| 68 | 3:21.38–3:23.75 | 4833–4890 | 1 | peak | Night orbit | **fill landing**<br><sub>fill in previous bar: 3 late hits, late drum level +4.3 dB vs typical</sub> | -0.5 ms | `a-iss-aurora-v` @ 0.00 s<br><sub>Aurora curtain from the ISS (2013) · use 2</sub> | `b-physarum-tl` @ 3.17 s ×1.5<br><sub>Physarum spreading, time-lapse (2022) · use 2</sub> | DIRECTION CARRY · L→R | subject motion +58 / +7 px/s, both L→R (100% / 98% of samples agree) |
| 69 | 3:23.75–3:26.25 | 4890–4950 | 1 | groove | Night orbit | **change**<br><sub>novelty 0.00, mix -4.8 dB</sub> | -5.1 ms (override) | `a-hsf-limb` @ 12.33 s<br><sub>Blue limb glow, shuttle video 2003 (2003)</sub> | `b-alfin-drops` @ 0.00 s ×1.5<br><sub>Beads on anodized metal, 1956 (1956) · use 2</sub> | STILL HOLD | both near-still (flow 0.06 / 0.07 px/s) |
| 70 | 3:26.25–3:33.79 | 4950–5131 | 3 | sparse | Rim light | **drums out**<br><sub>drum stem -61→-71 dB</sub> | -19.4 ms (override) | `a-iss-sunburst` @ 5.42 s<br><sub>Sunburst on the Earth limb, ISS (2013)</sub> | `b-bubble-burst` @ 7.67 s<br><sub>Bubble bursting, 40× slow motion (2019)</sub> | RIM LIGHT | board pair 17: The sun bursts on the curved rim of the Earth; light rides the curved rim of a bubble. |
| 71 | 3:33.79–3:36.25 | 5131–5190 | 1 | peak | All the light at once | **drums in, change**<br><sub>drum stem -64→-29 dB; novelty 0.00, mix +4.2 dB</sub> | -15.7 ms | `a-cep366` @ 18.17 s ×1.5<br><sub>Cloud rows rolling, time-lapse (2007) · use 2</sub> | `b-myxo-stream` @ 24.17 s<br><sub>Cytoplasm streaming, microscopy 1931 (1931) · use 2</sub> | DIRECTION CARRY · R→L | subject motion -22 / -7 px/s, both R→L (100% / 81% of samples agree) |
| 72 | 3:36.25–3:38.75 | 5190–5250 | 1 | break | All the light at once | **break, section**<br><sub>mix -5.7 dB; novelty 0.63</sub> | -1.7 ms | `a-usda-cumulus` @ 2.67 s<br><sub>Cumulus tower, 1920 USDA film (1920) · use 2</sub> | `b-myxo-front` @ 8.00 s<br><sub>Advancing plasmodium front, time-lapse 1931 (1931) · use 2</sub> | SILVER LOCK (weak) | both black-and-white film (saturation 0 / 0), matched gray (luma 37 / 58) |
| 73 | 3:38.75–3:41.29 | 5250–5311 | 1 | peak | All the light at once | **drop, section**<br><sub>mix +7.2 dB; novelty 0.60</sub> | +13.9 ms | `a-winchester` @ 1.67 s<br><sub>Sun flaring through clouds, Winchester (640×480) (2010) · use 2</sub> | `b-soap-1` @ 22.67 s<br><sub>Soap-film thin-film bands (2020) · use 3</sub> | CHURN RHYME | both tagged churn/swirl, measured flow 16.8 / 54.3 |
| 74 | 3:41.29–3:43.75 | 5311–5370 | 1 | peak | All the light at once | **change**<br><sub>novelty 0.35, mix -1.0 dB</sub> | -8.7 ms | `a-usda-biplane` @ 4.00 s ×2.0<br><sub>Biplane crossing a cloud bank (1920) · use 2</sub> | `b-ferro-ug` @ 0.33 s<br><sub>Ferrofluid in simulated microgravity (PAL) (2013) · use 3</sub> | STILL HOLD | both near-still (flow 0.68 / 0.28 px/s) |
| 75 | 3:43.75–3:46.21 | 5370–5429 | 1 | groove | All the light at once | **fill landing**<br><sub>fill in previous bar: 2 late hits, late drum level +4.0 dB vs typical</sub> | -9.7 ms | `a-cep-storm` @ 0.00 s<br><sub>Approaching thunderstorm (2006) · use 2</sub> | `b-crystal-melt` @ 1.83 s ×1.5<br><sub>Crystals forming in a drop, 1958 (1958) · use 2</sub> | DIRECTION CARRY · L→R | subject motion +14 / +7 px/s, both L→R (83% / 74% of samples agree) |
| 76 | 3:46.21–3:48.75 | 5429–5490 | 1 | groove | All the light at once | **fill landing**<br><sub>fill in previous bar: 2 late hits, late drum level +5.1 dB vs typical</sub> | -5.8 ms | `a-cep-boil` @ 0.00 s<br><sub>Boiling clouds (C. E. Price) (2006) · use 2</sub> | `b-crystal-snow` @ 0.17 s ×1.5<br><sub>Snow crystal, 1958 (1958)</sub> | MOTION MATCH (weak) | the same amount of motion on both sides (flow 2.4 / 2.2 px/s) |
| 77 | 3:48.75–3:51.25 | 5490–5550 | 1 | groove | All the light at once | **fill landing**<br><sub>fill in previous bar: 1 late hits, late drum level +4.4 dB vs typical</sub> | +26.6 ms | `a-shen-sunrise` @ 11.67 s<br><sub>Sunrise over the Shenandoah ridges (2015)</sub> | `b-crystal-balls` @ 5.83 s<br><sub>Ball-bearing crystal lattice, 1958 (1958) · use 2</sub> | STILL HOLD | both near-still (flow 1.09 / 1.01 px/s) |
| 78 | 3:51.25–3:56.29 | 5550–5671 | 2 | groove | All the light at once | **fill landing**<br><sub>fill in previous bar: 1 late hits, late drum level +4.2 dB vs typical</sub> | +7.3 ms | `a-cep-redsky` @ 3.33 s<br><sub>Red sky at morning (2006) · use 2</sub> | `b-myxo-dish` @ 0.00 s<br><sub>Slime mold on a dish, 1931 (1931) · use 2</sub> | DIRECTION CARRY · R→L | subject motion -17 / -7 px/s, both R→L (100% / 75% of samples agree) |
| 79 | 3:56.29–4:01.29 | 5671–5791 | 2 | groove | All the light at once | **base**<br><sub></sub> | +20.4 ms | `a-iss-night` @ 25.33 s<br><sub>City lights streaming below, ISS night pass (2025) · use 2</sub> | `b-nacl` @ 1.83 s<br><sub>Salt crystal dissolving, microscope (2016) · use 2</sub> | VERTICAL CARRY · RISE | vertical motion -16 / -9 px/s, both up |
| 80 | 4:01.29–4:03.75 | 5791–5850 | 1 | peak | All the light at once | **base**<br><sub></sub> | +21.7 ms | `a-tl-pink` @ 13.33 s<br><sub>Pink-lit clouds, 2006 webcam time-lapse (2006) · use 2</sub> | `b-alfin-foil` @ 4.83 s<br><sub>Crumpled foil glinting, 1956 (1956) · use 2</sub> | DIRECTION CARRY · R→L | subject motion -81 / -28 px/s, both R→L (100% / 81% of samples agree) |
| 81 | 4:03.75–4:08.58 | 5850–5966 | 2 | groove | All the light at once | **base**<br><sub></sub> | +20.7 ms | `a-cep453` @ 0.00 s ×1.5<br><sub>Backlit cumulus, time-lapse (2007) · use 2</sub> | `b-pond-color` @ 0.00 s<br><sub>Oil-film play of color on a pond (2015)</sub> | TONE MATCH (weak) | matched brightness and color strength (luma 133 / 137, saturation 48 / 35) |
| 82 | 4:08.58–4:13.42 | 5966–6082 | 2 | groove | All the light at once | **fill landing**<br><sub>fill in previous bar: 1 late hits, late drum level +4.4 dB vs typical</sub> | -4.9 ms | `a-gc-summer` @ 3.67 s<br><sub>Summer clouds over the Grand Canyon (2015) · use 2</sub> | `b-physarum-au` @ 0.00 s<br><sub>Physarum crossing bark, time-lapse (2021) · use 2</sub> | DIRECTION CARRY · L→R | subject motion +10 / +7 px/s, both L→R (100% / 72% of samples agree) |
| 83 | 4:13.42–4:15.50 | 6082–6132 | 1 | release | Release | **release, change**<br><sub>mix -13.2 dB; novelty 0.00, mix -13.2 dB</sub> | -20.6 ms | `a-cep427` @ 4.00 s<br><sub>Afterglow (2007) · use 2</sub> | `b-gallium-heart` @ 18.67 s<br><sub>Gallium beating heart (2015) · use 2</sub> | HUE LOCK · ORANGE | hue 43° / 40° (Δ3°), saturation 118 / 224 |

## Lead variants

- **lead 0:** cut frame = round(t × 24) − 0. Offsets -21 to +27 ms vs the re-detected downbeat (median -2 ms). Check: PASS.
- **lead 1 (picked):** cut frame = round(t × 24) − 1. Offsets -21 to +27 ms vs the re-detected downbeat (median -2 ms). Check: PASS.
- **lead 2:** cut frame = round(t × 24) − 2. Offsets -21 to +27 ms vs the re-detected downbeat (median -2 ms). Check: PASS.

Lead 1 puts each cut one frame (~42 ms) ahead of the downbeat, which reads as on the hit; lead 0 can land a cut after the hit, and lead 2 starts to look early.

## Check output (`musicsync/check_render.py`, lead 1)

```
sky_sheen_full_v1_lead1.mp4 lead 1: re-detected 99 downbeats, 4 pulses/bar, irregular bars []
  override /workspace/moodboard/sky-and-sheen/edits/v1/sync/override.json applied to the re-detection; raw re-detection: 103 downbeats, irregular bars at 138.57, 139.82, 141.08, 142.29, 176.28, 179.47, 203.54, 204.80, 205.98, 207.21
  cuts confirmed by the raw re-detection: 80/82; override-only: #68 203.79s, #69 206.29s
 shot frame  aimed_at  downbeat  offset   raw   pixels  hits
   1   237    9.917    9.927  -10.7  -52.4  yes  drums_in
   2   305   12.750   12.756   -6.0  -47.7  yes  section
   3   438   18.292   18.288   +3.3  -38.4  yes  vocal_in,change
   4   503   21.000   21.017  -17.2  -58.9  yes  drums_out,change
   5   570   23.792   23.806  -14.2  -55.9  yes  drums_in,change
   6   701   29.250   29.238  +11.5  -30.2  yes  vocal_in,section
   7   764   31.875   31.878   -2.6  -44.3  yes  drums_out
   8   831   34.667   34.656  +10.5  -31.2  yes  drums_in,drop,section
   9   895   37.333   37.335   -1.8  -43.4  yes  change
  10   960   40.042   40.034   +7.7  -34.0  yes  change
  11  1024   42.708   42.713   -4.6  -46.2  yes  change
  12  1087   45.333   45.317  +16.3  -25.3  yes  drums_out,break,vocal_in,change
  13  1151   48.000   47.996   +4.1  -37.6  yes  change
  14  1217   50.750   50.730  +20.3  -21.4  yes  drums_in,change
  15  1470   61.292   61.281  +11.0  -30.7  yes  vocal_in,change
  16  1597   66.583   66.604  -20.3  -61.9  yes  break,change
  17  1661   69.250   69.263  -12.6  -54.3  yes  base
  18  1724   71.875   71.882   -6.6  -48.3  yes  vocal_in,change
  19  1788   74.542   74.551   -8.9  -50.6  yes  base
  20  1851   77.167   77.160   +7.1  -34.6  yes  base
  21  1914   79.792   79.779  +13.0  -28.7  yes  change
  22  1978   82.458   82.453   +5.7  -35.9  yes  change
  23  2040   85.042   85.057  -15.0  -56.7  yes  base
  24  2101   87.583   87.596  -12.6  -54.2  yes  drums_out,break,vocal_in,change
  25  2157   89.917   89.936  -18.9  -60.6  yes  change
  26  2224   92.708   92.699   +9.0  -32.6  yes  drop,section
  27  2285   95.250   95.263  -13.5  -55.2  yes  section
  28  2348   97.875   97.888  -12.5  -54.2  yes  drums_in,vocal_in,change
  29  2410  100.458  100.462   -3.4  -45.0  yes  break,change
  30  2472  103.042  103.036   +5.9  -35.8  yes  change
  31  2533  105.583  105.580   +3.3  -38.3  yes  break,change
  32  2596  108.208  108.229  -20.7  -62.3  yes  drop,change
  33  2658  110.792  110.778  +13.5  -28.2  yes  fill_landing
  34  2719  113.333  113.347  -14.1  -55.7  yes  vocal_in,fill_landing,change
  35  2781  115.917  115.927   -9.8  -51.5  yes  fill_landing
  36  2842  118.458  118.461   -2.5  -44.1  yes  base
  37  2902  120.958  120.975  -16.8  -58.4  yes  base
  38  2963  123.500  123.519  -19.3  -61.0  yes  vocal_in,change
  39  3024  126.042  126.049   -6.8  -48.5  yes  base
  40  3084  128.542  128.553  -11.1  -52.8  yes  base
  41  3144  131.042  131.037   +4.7  -37.0  yes  change
  42  3206  133.625  133.616   +8.7  -33.0  yes  change
  43  3265  136.083  136.081   +2.6  -39.0  yes  base
  44  3325  138.583  138.565  +18.2  -23.4  yes  vocal_in
  45  3385  141.083  141.079   +3.9  -37.7  yes  base
  46  3442  143.458  143.479  -20.6  -62.2  yes  section
  47  3503  146.000  146.003   -3.2  -44.9  yes  section
  48  3563  148.500  148.502   -2.5  -44.2  yes  section
  49  3625  151.083  151.077   +6.7  -34.9  yes  section
  50  3686  153.625  153.621   +4.1  -37.6  yes  drop,vocal_in,section
  51  3748  156.208  156.210   -1.7  -43.3  yes  base
  52  3809  158.750  158.749   +0.8  -40.9  yes  base
  53  3869  161.250  161.263  -13.5  -55.2  yes  base
  54  3930  163.792  163.808  -16.0  -57.7  yes  section
  55  3990  166.292  166.307  -15.3  -57.0  yes  section
  56  4051  168.833  168.831   +2.0  -39.6  yes  section
  57  4110  171.292  171.296   -4.0  -45.7  yes  change
  58  4169  173.750  173.760  -10.1  -51.8  yes  vocal_in,change
  59  4230  176.292  176.284   +7.3  -34.4  yes  drums_out,change
  60  4413  183.917  183.937  -20.3  -62.0  yes  drums_in,drop,change
  61  4474  186.458  186.456   +2.1  -39.5  yes  fill_landing
  62  4534  188.958  188.970  -12.2  -53.8  yes  fill_landing
  63  4595  191.500  191.500   +0.2  -41.5  yes  fill_landing
  64  4655  194.000  193.984  +15.9  -25.8  yes  fill_landing
  65  4714  196.458  196.458   -0.2  -41.8  yes  change
  66  4774  198.958  198.968   -9.5  -51.1  yes  change
  67  4833  201.417  201.417   -0.5  -42.2  yes  fill_landing
  68  4890  203.792  203.797   -5.1  -46.8  yes  change
  69  4950  206.292  206.311  -19.4  -61.1  yes  drums_out
  70  5131  213.833  213.849  -15.7  -57.3  yes  drums_in,change
  71  5190  216.292  216.293   -1.7  -43.4  yes  break,section
  72  5250  218.792  218.778  +13.9  -27.8  yes  drop,section
  73  5311  221.333  221.342   -8.7  -50.3  yes  change
  74  5370  223.792  223.801   -9.7  -51.4  yes  fill_landing
  75  5429  226.250  226.256   -5.8  -47.5  yes  fill_landing
  76  5490  228.792  228.765  +26.6  -15.1  yes  fill_landing
  77  5550  231.292  231.284   +7.3  -34.4  yes  fill_landing
  78  5671  236.333  236.313  +20.4  -21.2  yes  base
  79  5791  241.333  241.312  +21.7  -19.9  yes  base
  80  5850  243.792  243.771  +20.7  -21.0  yes  base
  81  5966  248.625  248.630   -4.9  -46.6  yes  fill_landing
  82  6082  253.458  253.479  -20.6  -62.2  yes  release,change
  audio: 1 stream, lag 0 samples, gain -0.07 dB, null residual -23.200000762939453 dB (worst 1 s window -15.100000381469727 dB at 28 s)
PASS
```
