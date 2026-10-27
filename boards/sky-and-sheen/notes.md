# Sky & Sheen — mood board notes

Live room: https://moodboard-room.thtopher.workers.dev/r/sky-and-sheen

Two worlds intercut with strange continuity:
- **World A, Sky:** clouds, sunsets, analog/VHS-style lens flare and video skies.
- **World B, Sheen:** oil and thin film, slime molds and molds, chrome and wet metal, microscopy and crystal.

## Footage
- 108 clips, 35.4 min total (A 17.8, B 17.6). All audio is stripped.
- Sources: archive.org has 61 clips (17.9 min, including NASA and NARA items). Wikimedia Commons has 47 clips (17.5 min, including NASA/NOAA uploads).
- Licenses: public domain or US government 66 clips. CC BY 15, CC BY-SA 15, CC0 3. Nine Prelinger clips (3.5 min) are treated as PD but should be verified before commercial use.

## Measurement
- **Pace:** pace_raw = 0.6·flow_p50 + 0.4·flow_p90, using Farneback optical flow at 160 px and 6 fps.
  - Levels 1–5 use board-relative thresholds [2, 5, 10, 17].
  - The Chicago-scale level (thresholds [3, 9, 17, 25]) is kept in `pace_chicago`.
- **Direction:**
  - still if flow p50 is under 1.5
  - else translation gives L→R, R→L, up or down
  - else divergence gives toward or away
  - else curl gives swirl
  - else churn
  - Manual overrides are noted in `direction_note`.
- **Color:** one dominant family per clip, plus `iridescent` when 4 or more hue families each reach a weight of 0.06 or more.

## Match-cut rules (A → B)
1. HUE LOCK · ORANGE: cep427 → gold dendrite
2. DIRECTION CARRY · L→R: cep-wind → soap film 4
3. SHAPE RHYME · DISC: SDO blast → myxo sphere
4. BOKEH → BEADS: shuttle bokeh → gallium drops
5. FLARE → GLINT: HSF 1987 flare → foil
6. BRANCH RHYME: Pipeline storm → myxo veins
7. GROWTH FRONT: USDA cumulus heap → penicillium
8. EDGE RHYME: Rainier sea → myxo front
9. COLOR BAND: ISS aurora → soap film 1
10. HORIZON LINE: Masada → Rainier mirror
11. PACE MATCH · 5: HSF 1981 → soap film 7
12. TYPE RHYME: Pipeline title → aluminum title
13. SPECULAR SUN: USDA sun on water → foil drops
14. SPIRAL: ISS hurricane → vitamin C crystal
15. HUE LOCK · GOLD: Joshua Tree sunset → physarum time-lapse
16. DIRECTION CARRY · R→L: Golden Gate fog → oil slick aerial
17. RIM LIGHT: ISS sunburst → bubble burst
