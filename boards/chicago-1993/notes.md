# RAIN, 1993 — Chicago bus stop mood board: notes and spec

**Room:** tldraw live room `chicago-1993-bus-stop` (link in `board/.link`). **Repo:** `thtopher/moodboards`, media under `assets/chicago-1993/`.

## The world
A rainy night in 1993 at the **#49 Western** stop at **Lawrence & Western, Lincoln Square**, on Chicago's North Side. It's a working, middle-class city neighborhood: two- and three-flats, a corner tavern, a Walgreens, and the Brown Line (Ravenswood) at Western nearby. It's not a suburb and not a rough block. The bus is a CTA Flxible Metro. Rain on sodium light, wet asphalt, fluorescent shop glow, and the radio forecast saying "rain developing."

## Zones
01 The corner · 02 Light, dusk to sodium · 03 Rain · 04 The bus · 05 The people · 06 The neighborhood · 07 The L · 08 Camera · 09 Color strip · 10 Type & signage · 11 Sound · 12 Voice · 13 1993 timeline · 14 Counter-world A, steel · 15 Counter-world B, time-lapse and seasons · 16 Wildcards · 17 Match-cut pairs · 18 Footage index · 19 Pace ramp · 20 Licensable archives (Media Burn, AAPB, CFA; link cards only). Legend at the top left.

## Footage library
- Masters (H.264, source resolution): `/workspace/moodboard/chicago-1993/footage/<id>.mp4` on the box only, **not in git**.
- 480p proxies: `assets/chicago-1993/proxies/<id>.mp4` (raw.githubusercontent URLs); posters `assets/chicago-1993/posters/`; contact sheets `footage/sheets/<id>.jpg` (box).
- Catalog: `footage/catalog.csv` and `footage/catalog.json` (also copied to `boards/chicago-1993/` in the repo).

**111 clips, 38.9 min** (v2, re-sourced Oct 27, 2026; v1 was 96 clips, 39.3 min, 61 of them REF).

| world | clips | min |
|---|---|---|
| chicago | 49 | 22.0 |
| counter-A | 31 | 7.9 |
| counter-B | 23 | 6.7 |
| wildcard | 8 | 2.3 |

### Minutes per pace step

| world | P1 | P2 | P3 | P4 | P5 |
|---|---|---|---|---|---|
| chicago | 5.3 (11) | 6.4 (14) | 5.4 (14) | 4.1 (7) | 0.9 (3) |
| counter (all) | 3.4 (11) | 4.5 (17) | 4.3 (16) | 3.8 (14) | 0.9 (4) |
| counter-A | 0.0 (0) | 2.8 (10) | 2.7 (10) | 1.8 (8) | 0.7 (3) |
| counter-B | 2.6 (8) | 1.5 (5) | 1.6 (6) | 0.8 (3) | 0.2 (1) |
| wildcard | 0.8 (3) | 0.3 (2) | 0.0 (0) | 1.2 (3) | 0.0 (0) |

Cells are minutes (clip count).

### Minutes by source API

| source_api | clips | min |
|---|---|---|
| Wikimedia Commons API (imageinfo/extmetadata) | 83 | 30.4 |
| archive.org metadata API | 26 | 8.0 |
| NASA Images API (images-api.nasa.gov) | 2 | 0.5 |

## Tag vocabulary

| tag | values | how it's set |
|---|---|---|
| world | chicago · counter-A (steel) · counter-B (time-lapse/seasons) · wildcard | manual |
| color / color2 | sodium-orange · red-neon · green · cyan-fluorescent · steel-blue · white-glare · mono-gray · wet-black | k-means (6 colors) on frames sampled across the segment, mapped to the nearest family; `palette` holds the 6 hexes |
| angle | low · eye · high · overhead | manual, from the contact sheet |
| size | ECU · CU · MS · WS · EWS | manual |
| move | static · pan · tilt · track · handheld | manual, checked against flow |
| direction | L→R · R→L · toward · away · up · down · still | computed from mean optical flow (mean_dx > 0 = scene content moves L→R; mean_dy > 0 = down), then checked by eye. Rule: **the dominant on-screen motion**. For lateral tracks and pans, it is the way the scene slides; forward travel = toward. Manual corrections are in `footage/overrides.json` (11 clips). |
| pace | 1–5 | computed (below) |
| light | sodium · fluorescent · neon · headlights · daylight-overcast · daylight-sun · furnace · studio | manual |
| texture | rain · sparks · steam · grain · VHS | manual |
| source / source_date / original | archive item, year, link to the original at the in-point timestamp | |
| rights / license | PD · CC0 · CC-BY · CC-BY-SA | v2 has no REF clips. CC-BY/BY-SA need attribution (on each caption); BY-SA derivatives must be shared alike |
| source_api | archive.org metadata API · Wikimedia Commons API · NASA Images API | the API each clip was found and fetched through |

## Pace calibration
`pace_raw = 0.6 × flow_p50 + 0.4 × flow_p90`. Farneback dense optical flow, in px/s on frames downscaled to 160 px wide at 6 fps. Cuts are detected (framediff spikes) and excluded from the flow statistics.
Thresholds: **1** <3 near-static · **2** 3–9 slow · **3** 9–17 medium · **4** 17–25 brisk · **5** ≥25 high-velocity.
I calibrated by eye at the extremes and the boundaries. Locked-off time-lapse and still plates fall at 0–3. Bus pass-bys and lateral cab rides fall at 17–30. Night-drive streaks and the hot-strip mill run-out reach 25+. Raw values are in the catalog, so the steps can be re-cut.

## Match-cut pairs (zone 17)
Pairs share at least 3 of: color, direction, pace (±1), size, angle, move. Each pair was then checked for a visual or sound rhyme. The one-line notes are on the board. Rebuilt in v2 from cleared clips only.
c-impr-bus-night↔a-acroni-rolls · t-rain-puddles↔a-kover-ladle · c-doha-sodium↔b-lemaire · c-edison-sodium↔a-kover-billets · c-amtrak95↔a-inland-train2 · c-94-skyline↔b-cloudcomp · c-edison-grid↔w-biolum-swarm · t-rain-reflect↔a-acroni-runout · c-impr-crossing↔a-servant-slab · c-ic92-night↔a-servant-roll · c-rain93-nasa↔b-pond-rain · c-94-loop↔b-iss-earth

## Board build
The skeleton push was the only full push. Everything after it was pull-then-targeted patches (`board/p*.json`). The footage index (18) and pace ramp (19) use poster images that click through to the proxy, to keep the number of video players down. Zones 01–08, 10, 12–17 use playable video shapes.
Hosting: proxies play from raw.githubusercontent.com (verified in headless Chrome: currentTime advances, readyState 4, 0 console errors). GitHub Pages is not enabled. raw serves `application/octet-stream`, which Safari may refuse to play inline. Fallback is the poster plus the original link.

## Rights
- Stills: 75, all from Wikimedia Commons (PD or CC BY / BY-SA). Attribution is on each caption and in `images/stills.json`.
- Clips (v2): {'PD': 43, 'CC0': 2, 'CC-BY': 55, 'CC-BY-SA': 11}. **No REF clips remain.** Every clip came through an API (archive.org, Wikimedia Commons, NASA Images) and is PD or CC. The 61 v1 REF proxies and posters (YouTube uploads, station broadcasts, Kinolibrary previews) were removed from the public repo; they still exist in older git history.
- CC BY / BY-SA clips need the attribution in their caption. BY-SA (11 clips) means any derivative edit has to be shared alike.
- NASA material is a U.S. government work, but the NASA insignia and endorsement rules still apply.
- Copyrighted films (Thief, Hoop Dreams, The Fugitive, Night on Earth, Chungking Express) and 1993 music are link-only REF cards (stills zones), not footage.
- Rain plates are stand-ins (some are not Chicago or not 1993). Several stills are modern photos of 1993-era locations.

## v2 re-sourcing (Oct 27, 2026)
- **Priority used:** archive.org metadata API → Wikimedia Commons API (imageinfo/extmetadata; `filetype:video` search) → NASA Images API. `source_api` is set on every clip.
- **Not used (need a key, not signed up):** NARA Catalog API v2 (x-api-key), Pexels and Pixabay video APIs. The LoC JSON API had no usable 1990s Chicago street video. NOAA/USGS clips came via Commons.
- **Tradeoffs:**
  - There's no PD/CC Flxible-era CTA bus footage. The bus zone uses 2010s CTA buses at night (Impressions of Chicago, CC BY) as a stand-in. Period-true bus tape is in zone 20 (Media Burn, licensable).
  - Period feel comes from CC camcorder material from 1988–95: 1992 Metra/IC, 1993 IC, the 1994 L rides, Pilsen 1988, and Amtrak 1995.
  - Counter-world pace 4–5 was filled from Acroni, Koverhar, Inland/East Chicago train windows, Hendrichs, Men and Mills, and a cloud time-lapse. Windows were checked frame by frame to rule out scene cuts and animated diagrams.
- **Licensable archives (zone 20, excluded from minutes):**
  - **Media Burn:** 8 tapes as link cards (mediaburn.org page plus the Vimeo player URL); license via info@mediaburn.org. The embeds wouldn't play in headless Chrome (Vimeo bot wall), so this is not proof of a domain restriction. Nothing was downloaded from Vimeo.
  - **AAPB:** stream-only reference records.
  - **Chicago Film Archives:** McBrien/WTTW "Skyline: Chicago" outtakes from 1991–93. They're digitized but not online; license through CFA.

## Stills

| slug | zone | rights | title | page |
|---|---|---|---|---|
| canal-randolph-2002 | z04 | CC-BY CC BY 2.0 | 20021219 01 Canal St. @ Randolph St. (5527643303).jpg | https://commons.wikimedia.org/wiki/File:20021219_01_Canal_St._@_Randolph_St._(5527643303).jpg |
| 77th-garage-flxibles | z04 | CC-BY CC BY-SA 2.0 | 77th Street CTA Bus Garage.jpg | https://commons.wikimedia.org/wiki/File:77th_Street_CTA_Bus_Garage.jpg |
| canal-randolph-2011 | z04 | CC-BY CC BY 2.0 | 20110111 08 CTA bus, Canal St. @ Randolph St..jpg | https://commons.wikimedia.org/wiki/File:20110111_08_CTA_bus,_Canal_St._@_Randolph_St..jpg |
| michigan-roosevelt-1978 | z04 | CC-BY CC BY-SA 4.0 | 12 110978 First Church of Christ Scientist.jpg | https://commons.wikimedia.org/wiki/File:12_110978_First_Church_of_Christ_Scientist.jpg |
| 63rd-street-1973 | z07 | PD Public domain | BLACKS USING BUS TRANSPORTATION ON 63RD STREET IN CHICAGO DU | https://commons.wikimedia.org/wiki/File:BLACKS_USING_BUS_TRANSPORTATION_ON_63RD_STREET_IN_CHICAGO_DURING_1973_THERE_WERE_272,803,082_PEOPLE_WHO_RODE_THIS..._-_NARA_-_556203.jpg |
| sheridan-stop-1973 | z07 | PD Public domain | CTA BUSMAN WAITS WITH COMMUTERS FOR BUS AT THE SHERIDAN ROAD | https://commons.wikimedia.org/wiki/File:CTA_BUSMAN_WAITS_WITH_COMMUTERS_FOR_BUS_AT_THE_SHERIDAN_ROAD_STOP_-_NARA_-_547205.jpg |
| davis-dusk-2018 | z06 | CC-BY CC BY-SA 4.0 | Davis Theater Hope Hague (2).jpg | https://commons.wikimedia.org/wiki/File:Davis_Theater_Hope_Hague_(2).jpg |
| davis-night-2018 | z06 | CC-BY CC BY-SA 4.0 | Davis Theater Hope Hague (3).jpg | https://commons.wikimedia.org/wiki/File:Davis_Theater_Hope_Hague_(3).jpg |
| davis-2008 | z06 | CC-BY CC BY 2.0 | Davis Theatre Chicago.jpeg | https://commons.wikimedia.org/wiki/File:Davis_Theatre_Chicago.jpeg |
| davis-block-2024 | z06 | CC-BY CC BY-SA 2.0 | Davis Theater, Lincoln Avenue, Lincoln Square, Chicago, IL.j | https://commons.wikimedia.org/wiki/File:Davis_Theater,_Lincoln_Avenue,_Lincoln_Square,_Chicago,_IL.jpg |
| greystone-1888 | z06 | CC-BY CC BY-SA 4.0 | Emerald Avenue, Bridgeport, Chicago, IL (54831816397).jpg | https://commons.wikimedia.org/wiki/File:Emerald_Avenue,_Bridgeport,_Chicago,_IL_(54831816397).jpg |
| greystone-1898 | z06 | CC-BY CC BY-SA 4.0 | Emerald Avenue, Bridgeport, Chicago, IL (54832667106).jpg | https://commons.wikimedia.org/wiki/File:Emerald_Avenue,_Bridgeport,_Chicago,_IL_(54832667106).jpg |
| greystone-1884 | z06 | CC-BY CC BY-SA 4.0 | 24th Street, Chinatown, Chicago, IL (54839594244).jpg | https://commons.wikimedia.org/wiki/File:24th_Street,_Chinatown,_Chicago,_IL_(54839594244).jpg |
| greystone-uptown | z06 | CC-BY CC BY-SA 2.0 | Sheridan Road, Uptown, Chicago, IL (54508000853).jpg | https://commons.wikimedia.org/wiki/File:Sheridan_Road,_Uptown,_Chicago,_IL_(54508000853).jpg |
| hermosa-bungalow | z06 | CC-BY CC BY-SA 4.0 | Michael Faheny House 3124 N. Kilbourn Ave. (Chicago, IL.).jp | https://commons.wikimedia.org/wiki/File:Michael_Faheny_House_3124_N._Kilbourn_Ave._(Chicago,_IL.).jpg |
| brick-bungalow-1 | z06 | CC-BY CC BY-SA 4.0 | Emerald Avenue, Bridgeport, Chicago, IL (54835488180).jpg | https://commons.wikimedia.org/wiki/File:Emerald_Avenue,_Bridgeport,_Chicago,_IL_(54835488180).jpg |
| brick-bungalow-2 | z06 | CC-BY CC BY-SA 4.0 | Emerald Avenue, Bridgeport, Chicago, IL (54832901914).jpg | https://commons.wikimedia.org/wiki/File:Emerald_Avenue,_Bridgeport,_Chicago,_IL_(54832901914).jpg |
| ravenswood-western-1992 | z01 | CC-BY CC BY 2.0 | 19920628 28 CTA Ravenswood L @ Western (4846726530).jpg | https://commons.wikimedia.org/wiki/File:19920628_28_CTA_Ravenswood_L_@_Western_(4846726530).jpg |
| western-brown-2004 | z01 | CC-BY CC BY 2.0 | 20040110 22 CTA Western Ave. Brown Line station.jpg | https://commons.wikimedia.org/wiki/File:20040110_22_CTA_Western_Ave._Brown_Line_station.jpg |
| western-brown-2006 | z01 | CC-BY CC BY-SA 2.0 | CTA Western Brown Line Station 060305.jpg | https://commons.wikimedia.org/wiki/File:CTA_Western_Brown_Line_Station_060305.jpg |
| western-sign | z10 | PD Public domain | Western (Brown).png | https://commons.wikimedia.org/wiki/File:Western_(Brown).png |
| western-from-platform-2025 | z01 | CC-BY CC BY 4.0 | Western Ave at CTA Brown Line - July 2025.jpg | https://commons.wikimedia.org/wiki/File:Western_Ave_at_CTA_Brown_Line_-_July_2025.jpg |
| western-station-2011 | z01 | CC-BY CC BY-SA 2.0 | Western station.jpg | https://commons.wikimedia.org/wiki/File:Western_station.jpg |
| western-stop-blur-2009 | z01 | CC-BY CC BY 2.0 | Western Stop (3896596192).jpg | https://commons.wikimedia.org/wiki/File:Western_Stop_(3896596192).jpg |
| bus-shelter-2007 | z05 | CC-BY CC BY-SA 3.0 | 20071107 New CTA Bus Stop with 3D ad.JPG | https://commons.wikimedia.org/wiki/File:20071107_New_CTA_Bus_Stop_with_3D_ad.JPG |
| bus-stop-sign-2007 | z05 | CC-BY CC BY-SA 3.0 | Chicagobusstop.jpg | https://commons.wikimedia.org/wiki/File:Chicagobusstop.jpg |
| bus-stop-sign-night-2008 | z05 | CC-BY CC BY-SA 3.0 | CTA Bus Stop.jpg | https://commons.wikimedia.org/wiki/File:CTA_Bus_Stop.jpg |
| newspaper-box-2006 | z05 | CC-BY CC BY-SA 2.0 | Soldier on hot box (203851385).jpg | https://commons.wikimedia.org/wiki/File:Soldier_on_hot_box_(203851385).jpg |
| flip-dot-sign | z05 | CC-BY CC BY 2.0 | Flip-dot destination signage for route 1 on a San Francisco  | https://commons.wikimedia.org/wiki/File:Flip-dot_destination_signage_for_route_1_on_a_San_Francisco_ETI_trolleybus_(2008).jpg |
| sodium-lamp-night | z02 | CC-BY CC BY-SA 4.0 | 2014-10-31 23 30 00 Sodium vapor street light at night along | https://commons.wikimedia.org/wiki/File:2014-10-31_23_30_00_Sodium_vapor_street_light_at_night_along_Terrace_Boulevard_in_Ewing,_New_Jersey.JPG |
| sodium-warmup | z02 | CC-BY CC BY-SA 4.0 | 2014-12-26 16 52 11 Sodium vapor street light just after tur | https://commons.wikimedia.org/wiki/File:2014-12-26_16_52_11_Sodium_vapor_street_light_just_after_turning_on_for_the_night_on_Terrace_Boulevard_at_Dunmore_Avenue_in_Ewing,_New_Jersey.JPG |
| sodium-dusk-vertical | z02 | CC-BY CC BY-SA 4.0 | 2014-12-26 16 52 58 Sodium vapor street light just after tur | https://commons.wikimedia.org/wiki/File:2014-12-26_16_52_58_Sodium_vapor_street_light_just_after_turning_on_for_the_night_on_Terrace_Boulevard_at_Dunmore_Avenue_in_Ewing,_New_Jersey.JPG |
| sodium-older-arm | z02 | CC-BY CC BY-SA 4.0 | 2014-12-26 16 56 05 Sodium vapor street light on an older su | https://commons.wikimedia.org/wiki/File:2014-12-26_16_56_05_Sodium_vapor_street_light_on_an_older_support_just_after_turning_on_for_the_night_along_Meriden_Avenue_in_Ewing,_New_Jersey.jpg |
| sodium-snow | z02 | CC-BY CC BY-SA 4.0 | 2024-02-17 03 56 22 A sodium-vapor street light during a mod | https://commons.wikimedia.org/wiki/File:2024-02-17_03_56_22_A_sodium-vapor_street_light_during_a_moderate_snowfall_at_night_along_Aquetong_Lane_in_the_Mountainview_section_of_Ewing_Township,_Mercer_County,_New_Jersey.jpg |
| merch-mart-rain-2022 | z02 | CC-BY CC BY 2.0 | Merchandise Mart on a rainy night (52040145062).jpg | https://commons.wikimedia.org/wiki/File:Merchandise_Mart_on_a_rainy_night_(52040145062).jpg |
| taillight-puddle | z03 | CC-BY CC BY-SA 4.0 | Tail light reflection in Tuntorp.jpg | https://commons.wikimedia.org/wiki/File:Tail_light_reflection_in_Tuntorp.jpg |
| street-reflections | z03 | CC-BY CC BY-SA 4.0 | City streets; Reflections on the street surface after rain.j | https://commons.wikimedia.org/wiki/File:City_streets;_Reflections_on_the_street_surface_after_rain.jpg |
| chambery-green | z03 | CC-BY CC BY-SA 4.0 | Boulevard du Musée à Chambéry sous la pluie au feu vert (201 | https://commons.wikimedia.org/wiki/File:Boulevard_du_Mus%C3%A9e_%C3%A0_Chamb%C3%A9ry_sous_la_pluie_au_feu_vert_(2018).JPG |
| chambery-red | z03 | CC-BY CC BY-SA 4.0 | Boulevard du Musée à Chambéry sous la pluie au feu rouge (20 | https://commons.wikimedia.org/wiki/File:Boulevard_du_Mus%C3%A9e_%C3%A0_Chamb%C3%A9ry_sous_la_pluie_au_feu_rouge_(2018).JPG |
| chambery-amber | z03 | CC-BY CC BY-SA 4.0 | Boulevard du Musée à Chambéry sous la pluie au feu orange (2 | https://commons.wikimedia.org/wiki/File:Boulevard_du_Mus%C3%A9e_%C3%A0_Chamb%C3%A9ry_sous_la_pluie_au_feu_orange_(2018).JPG |
| chambery-pavement | z03 | CC-BY CC BY-SA 4.0 | Partie haute Rue de Boigne à Chambéry de nuit sous la pluie  | https://commons.wikimedia.org/wiki/File:Partie_haute_Rue_de_Boigne_%C3%A0_Chamb%C3%A9ry_de_nuit_sous_la_pluie_(2018).JPG |
| south-chicago-1941 | z14 | CC-BY CC BY 2.0 | South Chicago- vacant lot near Steel mills. (4408673027).jpg | https://commons.wikimedia.org/wiki/File:South_Chicago-_vacant_lot_near_Steel_mills._(4408673027).jpg |
| south-works-1940 | z14 | CC-BY CC BY 2.0 | Carnegie Illinois Steel Corp. South Works (4409436480).jpg | https://commons.wikimedia.org/wiki/File:Carnegie_Illinois_Steel_Corp._South_Works_(4409436480).jpg |
| south-works-91st | z14 | CC-BY CC BY 2.0 | South Works, Carnegie- Illinois, from (91th) St. (4409437750 | https://commons.wikimedia.org/wiki/File:South_Works,_Carnegie-_Illinois,_from_(91th)_St._(4409437750).jpg |
| us-steel-gate-2007 | z14 | CC-BY CC BY 2.0 | UNITED STATES STEEL SOUTH SIDE.jpg | https://commons.wikimedia.org/wiki/File:UNITED_STATES_STEEL_SOUTH_SIDE.jpg |
| sadlowski-south-works | z14 | PD Public domain | Ed Sadlowski and South Works Trim.jpg | https://commons.wikimedia.org/wiki/File:Ed_Sadlowski_and_South_Works_Trim.jpg |
| haer-aerial-1992 | z14 | PD Public domain | AERIAL VIEW, LOOKING EAST TOWARDS TCI-US STEEL, ENSLEY WORKS | https://commons.wikimedia.org/wiki/File:AERIAL_VIEW,_LOOKING_EAST_TOWARDS_TCI-US_STEEL,_ENSLEY_WORKS_OPEN_HEARTH_IN_BACKGROUND._-_Tennessee_Coal_and_Iron_Company,_Ensley_Works,_West_of_residential_and_commercial_HAER_ALA,37-BIRM.V,16-5.tif |
| pour-1971 | z14 | PD Public domain | Steelworkers at the Vicasa Steel Mill pour molten steel from | https://commons.wikimedia.org/wiki/File:Steelworkers_at_the_Vicasa_Steel_Mill_pour_molten_steel_from_the_smelter.jpg |
| ladle-color-1941 | z14 | PD Public domain | Ladle of molten iron is poured into an open hearth furnace f | https://commons.wikimedia.org/wiki/File:Ladle_of_molten_iron_is_poured_into_an_open_hearth_furnace_for_conversion_into_steel,_Allegheny_Ludlum_Steele_Corp,_Brackenridge,_Pa_Note_the_safety_latch_on_the_crane_hook.jpg |
| pour-1928 | z14 | PD Public domain | Pouring 135 ton steel Corrigan McKinney 1935.jpg | https://commons.wikimedia.org/wiki/File:Pouring_135_ton_steel_Corrigan_McKinney_1935.jpg |
| pig-iron-1942 | z14 | PD Public domain | Photograph of a Vat of Molten Pig Iron Being Poured into an  | https://commons.wikimedia.org/wiki/File:Photograph_of_a_Vat_of_Molten_Pig_Iron_Being_Poured_into_an_Open_Hearth_Furnace_at_the_Jones_and_Laughlin_Steel_Company,_Pittsburgh,_Pennsy_-_NARA_-_535922_(high_contrast).jpg |
| foundry-glow-2003 | z14 | PD Public domain | US Navy 030910-N-7542D-240 A worker from the Amite Foundry s | https://commons.wikimedia.org/wiki/File:US_Navy_030910-N-7542D-240_A_worker_from_the_Amite_Foundry_supervises_the_pouring_of_molten_steel_recycled_from_the_World_Trade_Center_into_a_ladle.jpg |
| caster-1993 | z14 | PD Public domain | INTERIOR OVERVIEW OF CONTINUOUS CASTER WITH NO. 12 LADLE. MO | https://commons.wikimedia.org/wiki/File:INTERIOR_OVERVIEW_OF_CONTINUOUS_CASTER_WITH_NO._12_LADLE._MOLTEN_STEEL_IS_POURED_FROM_LADLE_THROUGH_SHROUD_TO_TUNDISH._FROM_TUNDISH_STEEL_ENTERS_MOLD_THROUGH_SHROUD_AND_HAER_ALA,37-FAIRF,3C-1.tif |
| rotary-press-bilbao | z16 | CC-BY CC BY-SA 4.0 | Euzkadi egunkariaren errotatiba - Orconera eraikina - 01.jpg | https://commons.wikimedia.org/wiki/File:Euzkadi_egunkariaren_errotatiba_-_Orconera_eraikina_-_01.jpg |
| hbl-press-1927 | z16 | CC-BY CC BY 4.0 | The rotary press of newspaper Hufvudstadsbladet 1927 (Numero | https://commons.wikimedia.org/wiki/File:The_rotary_press_of_newspaper_Hufvudstadsbladet_1927_(Numeroimaton;_JOKAHBL3A_A01-19).tif |
| octuple-press | z16 | PD Public domain | Double Octuple Newspaper Press.jpg | https://commons.wikimedia.org/wiki/File:Double_Octuple_Newspaper_Press.jpg |
| harold-washington-library | z13 | CC-BY CC BY-SA 4.0 | Harold Washington Library from east.jpg | https://commons.wikimedia.org/wiki/File:Harold_Washington_Library_from_east.jpg |
| flood-1993-soil-map | z13 | PD Public domain | Mississippi Flood 1993.PNG | https://commons.wikimedia.org/wiki/File:Mississippi_Flood_1993.PNG |
| kaskaskia-flood-1993 | z13 | PD Public domain | Kaskaskia Island 1993 flooding.jpg | https://commons.wikimedia.org/wiki/File:Kaskaskia_Island_1993_flooding.jpg |
| cape-girardeau-1993 | z13 | PD Public domain | Cape Girardeau Missouri 1993.jpg | https://commons.wikimedia.org/wiki/File:Cape_Girardeau_Missouri_1993.jpg |
| festus-flood-1993 | z13 | PD Public domain | FEMA - 13708 - Photograph by Andrea Booher taken on 07-09-19 | https://commons.wikimedia.org/wiki/File:FEMA_-_13708_-_Photograph_by_Andrea_Booher_taken_on_07-09-1993_in_Mississippi_river,_Festus,_Missouri.jpg |
| new-comiskey-1990 | z13 | CC-BY CC BY-SA 2.0 | New Comiskey Park 1990.jpg | https://commons.wikimedia.org/wiki/File:New_Comiskey_Park_1990.jpg |
| old-comiskey-plate | z13 | CC-BY CC BY-SA 2.0 | Location of Old Comiskey Park Home Plate, U.S. Cellular Fiel | https://commons.wikimedia.org/wiki/File:Location_of_Old_Comiskey_Park_Home_Plate,_U.S._Cellular_Field,_Chicago,_Illinois_(9179565445).jpg |
| walkman-mid90s | z07 | CC-BY CC BY-SA 4.0 | Sony Walkman WM-EX116 cassette player.jpg | https://commons.wikimedia.org/wiki/File:Sony_Walkman_WM-EX116_cassette_player.jpg |
| starter-jacket | z07 | CC-BY CC BY-SA 3.0 | Starter dolphins-jacket.jpg | https://commons.wikimedia.org/wiki/File:Starter_dolphins-jacket.jpg |
| figure-in-rain | z07 | CC-BY CC BY 2.0 | Figure in the rain (24263897279).jpg | https://commons.wikimedia.org/wiki/File:Figure_in_the_rain_(24263897279).jpg |
| umbrellas-rain-nyc | z07 | CC-BY CC BY 2.0 | Times Square Rain (6387401445).jpg | https://commons.wikimedia.org/wiki/File:Times_Square_Rain_(6387401445).jpg |
| four-seasons-tree | z15 | CC-BY CC BY-SA 4.0 | "Four Seasons - Longbridge Road".png | https://commons.wikimedia.org/wiki/File:%22Four_Seasons_-_Longbridge_Road%22.png |
| fern-unfurling-1 | z15 | CC-BY CC BY-SA 4.0 | Fern fronds unfurling - Steall Falls.jpg | https://commons.wikimedia.org/wiki/File:Fern_fronds_unfurling_-_Steall_Falls.jpg |
| fern-unfurling-2 | z15 | CC-BY CC BY-SA 4.0 | Cibotum sp. unfurling frond.jpg | https://commons.wikimedia.org/wiki/File:Cibotum_sp._unfurling_frond.jpg |
| ice-crystals-pane | z15 | CC-BY CC BY-SA 4.0 | Ice Crystals on Window Pane.jpg | https://commons.wikimedia.org/wiki/File:Ice_Crystals_on_Window_Pane.jpg |
| star-trails-gemini | z15 | CC-BY CC BY 4.0 | Maunakea Star Trails Over Gemini North's Photo Voltaic Panel | https://commons.wikimedia.org/wiki/File:Maunakea_Star_Trails_Over_Gemini_North%27s_Photo_Voltaic_Panels_(gemini-gn-pv-tl-star-trails-dark-fin).jpg |
| vhs-camcorder | z08 | CC-BY CC BY-SA 4.0 | RCA AutoShot VHS Camcorder.jpg | https://commons.wikimedia.org/wiki/File:RCA_AutoShot_VHS_Camcorder.jpg |
| betacam-sp | z08 | CC-BY CC BY-SA 3.0 | Sony BVV-5 + JVC KY-D29 20090911.jpg | https://commons.wikimedia.org/wiki/File:Sony_BVV-5_%2B_JVC_KY-D29_20090911.jpg |
| green-river-2009 | z16 | CC-BY CC BY 2.0 | Green Chicago River on Saint Patricks Day 2009.jpg | https://commons.wikimedia.org/wiki/File:Green_Chicago_River_on_Saint_Patricks_Day_2009.jpg |

## Clips

| id | world | zone | s | color | dir | pace (raw) | rights | source_api | original |
|---|---|---|---|---|---|---|---|---|---|
| c-edison-corner | chicago | 01 | 38 | sodium-orange | toward | 2 (6.6) | CC-BY | Wikimedia Commons API (imageinfo/extmetadata) | https://commons.wikimedia.org/wiki/File:Flying_Around_Edison_Park_Chicago_3am.webm (at 1:02) |
| c-chilights-river | chicago | 02 | 35 | sodium-orange | still | 1 (0.38) | CC-BY | Wikimedia Commons API (imageinfo/extmetadata) | https://commons.wikimedia.org/wiki/File:Chicago_Lights_-_City_Timelapse.webm (at 0:00) |
| c-daynight | chicago | 02 | 34 | wet-black | still | 1 (1.76) | CC-BY | Wikimedia Commons API (imageinfo/extmetadata) | https://commons.wikimedia.org/wiki/File:Chicago_Day_and_Night.webm (at 0:00) |
| c-doha-sodium | chicago | 02 | 34 | sodium-orange | toward | 4 (22.52) | CC-BY | Wikimedia Commons API (imageinfo/extmetadata) | https://commons.wikimedia.org/wiki/File:Driving_under_rain_-_Doha,_Qatar.webm (at 1:11) |
| c-edison-grid | chicago | 02 | 40 | sodium-orange | toward | 1 (0.76) | CC-BY | Wikimedia Commons API (imageinfo/extmetadata) | https://commons.wikimedia.org/wiki/File:Flying_Around_Edison_Park_Chicago_3am.webm (at 5:50) |
| c-edison-sodium | chicago | 02 | 32 | sodium-orange | L→R | 3 (9.24) | CC-BY | Wikimedia Commons API (imageinfo/extmetadata) | https://commons.wikimedia.org/wiki/File:Flying_Around_Edison_Park_Chicago_3am.webm (at 4:48) |
| c-ic92-freight | chicago | 02 | 44 | wet-black | L→R | 1 (2.48) | CC-BY | Wikimedia Commons API (imageinfo/extmetadata) | https://commons.wikimedia.org/wiki/File:Illinois_Central_Action_1992!.webm (at 10:56) |
| c-ic92-night | chicago | 02 | 36 | wet-black | R→L | 2 (5.98) | CC-BY | Wikimedia Commons API (imageinfo/extmetadata) | https://commons.wikimedia.org/wiki/File:Illinois_Central_Action_1992!.webm (at 4:36) |
| c-impr-night-street | chicago | 02 | 17 | wet-black | L→R | 2 (5.53) | CC-BY | Wikimedia Commons API (imageinfo/extmetadata) | https://commons.wikimedia.org/wiki/File:Chicago_Impressions.webm (at 3:37) |
| c-metra92-dusk | chicago | 02 | 30 | wet-black | toward | 2 (8.91) | CC-BY | Wikimedia Commons API (imageinfo/extmetadata) | https://commons.wikimedia.org/wiki/File:Chicago_Metra_Action_1992!.webm (at 4:15) |
| c-nightview | chicago | 02 | 19 | wet-black | still | 1 (0.17) | CC-BY | Wikimedia Commons API (imageinfo/extmetadata) | https://commons.wikimedia.org/wiki/File:Night_view_of_Chicago.webm (at 0:00) |
| c-snow-sodium | chicago | 02 | 30 | sodium-orange | still | 3 (13.92) | CC-BY | Wikimedia Commons API (imageinfo/extmetadata) | https://commons.wikimedia.org/wiki/File:Chicago_Snowpocalypse_%27011_Part_2.webm (at 5:45) |
| t-rain-pouring | chicago | 03 | 30 | mono-gray | down | 3 (11.47) | CC-BY-SA | Wikimedia Commons API (imageinfo/extmetadata) | https://commons.wikimedia.org/wiki/File:Pouring_down_in_Wikimania_2017.webm (at 0:00) |
| t-rain-puddles | chicago | 03 | 13 | mono-gray | down | 3 (9.14) | CC-BY-SA | Wikimedia Commons API (imageinfo/extmetadata) | https://commons.wikimedia.org/wiki/File:Puddles_of_rain.webm (at 0:00) |
| t-rain-reflect | chicago | 03 | 16 | wet-black | L→R | 1 (1.72) | CC-BY | Wikimedia Commons API (imageinfo/extmetadata) | https://commons.wikimedia.org/wiki/File:Chicago_Impressions.webm (at 4:24) |
| t-rain-storm-chi | chicago | 03 | 31 | mono-gray | still | 2 (3.14) | CC-BY | Wikimedia Commons API (imageinfo/extmetadata) | https://commons.wikimedia.org/wiki/File:Bradhoc_-_Chicago_storm_7-12.ogv (at 0:00) |
| t-rain-street | chicago | 03 | 20 | mono-gray | down | 2 (5.68) | CC-BY-SA | Wikimedia Commons API (imageinfo/extmetadata) | https://commons.wikimedia.org/wiki/File:Heavy_rain_in_Boulevard_Rosemont,_Montreal.webm (at 0:00) |
| t-rain-wet-rails | chicago | 03 | 40 | wet-black | still | 2 (7.74) | CC-BY | Wikimedia Commons API (imageinfo/extmetadata) | https://commons.wikimedia.org/wiki/File:More_Illinois_Central_Action_1993!.webm (at 3:45) |
| t-rain-window | chicago | 03 | 40 | mono-gray | down | 1 (1.32) | CC-BY-SA | Wikimedia Commons API (imageinfo/extmetadata) | https://commons.wikimedia.org/wiki/File:Radevormwald_-_Raindrops_on_a_window_07_(1)_ies.webm (at 0:00) |
| t-rain-wipers | chicago | 03 | 23 | sodium-orange | toward | 3 (15.7) | CC-BY | Wikimedia Commons API (imageinfo/extmetadata) | https://commons.wikimedia.org/wiki/File:Driving_under_rain_-_Doha,_Qatar.webm (at 1:47) |
| c-gcm-bus-rain | chicago | 04 | 8 | mono-gray | L→R | 3 (14.93) | CC-BY | Wikimedia Commons API (imageinfo/extmetadata) | https://commons.wikimedia.org/wiki/File:Atmospheric_River_at_Grand_Central_Market_-_February_2024_-_Sarah_Stierch.webm (at 0:00) |
| c-impr-bus-lights | chicago | 04 | 7 | sodium-orange | toward | 2 (3.73) | CC-BY | Wikimedia Commons API (imageinfo/extmetadata) | https://commons.wikimedia.org/wiki/File:Chicago_Impressions.webm (at 4:12) |
| c-impr-bus-night | chicago | 04 | 8 | wet-black | R→L | 3 (9.91) | CC-BY | Wikimedia Commons API (imageinfo/extmetadata) | https://commons.wikimedia.org/wiki/File:Chicago_Impressions.webm (at 4:05) |
| c-snow-plow | chicago | 04 | 25 | sodium-orange | toward | 4 (24.34) | CC-BY | Wikimedia Commons API (imageinfo/extmetadata) | https://commons.wikimedia.org/wiki/File:Chicago_Snowpocalypse_%27011_Part_2.webm (at 4:50) |
| c-gramaphone | chicago | 05 | 23 | wet-black | L→R | 5 (34.87) | CC-BY-SA | Wikimedia Commons API (imageinfo/extmetadata) | https://commons.wikimedia.org/wiki/File:Gramaphone_Records_on_Clark_Street,_Chicago._August_2003.webm (at 1:22) |
| c-impr-shelter | chicago | 05 | 5 | sodium-orange | still | 1 (2.25) | CC-BY | Wikimedia Commons API (imageinfo/extmetadata) | https://commons.wikimedia.org/wiki/File:Chicago_Impressions.webm (at 4:19) |
| c-scenes74-signs | chicago | 05 | 39 | wet-black | still | 3 (10.72) | PD | Wikimedia Commons API (imageinfo/extmetadata) | https://commons.wikimedia.org/wiki/File:Chicago_Scenes_(ca._1974).webm (at 4:26) |
| c-southloop88-tower | chicago | 05 | 17 | red-neon | still | 5 (28.04) | CC-BY | Wikimedia Commons API (imageinfo/extmetadata) | https://commons.wikimedia.org/wiki/File:South_Loop_including_Dearborn_Station_Circa_April_1988.webm (at 0:48) |
| c-18th-rooftops | chicago | 06 | 24 | red-neon | L→R | 3 (15.66) | CC-BY | Wikimedia Commons API (imageinfo/extmetadata) | https://commons.wikimedia.org/wiki/File:18th_Street_Station_Circa_April_1988_(Silent).webm (at 0:18) |
| c-94-loop | chicago | 06 | 42 | mono-gray | toward | 4 (21.08) | CC-BY | Wikimedia Commons API (imageinfo/extmetadata) | https://commons.wikimedia.org/wiki/File:Chicago_1994.webm (at 0:38) |
| c-94-northside | chicago | 06 | 45 | mono-gray | toward | 4 (23.05) | CC-BY | Wikimedia Commons API (imageinfo/extmetadata) | https://commons.wikimedia.org/wiki/File:Chicago_1994.webm (at 4:20) |
| c-94-skyline | chicago | 06 | 40 | steel-blue | L→R | 4 (18.62) | CC-BY | Wikimedia Commons API (imageinfo/extmetadata) | https://commons.wikimedia.org/wiki/File:Chicago_1994.webm (at 3:00) |
| c-amtrak95 | chicago | 06 | 37 | mono-gray | R→L | 4 (23.26) | CC-BY | Wikimedia Commons API (imageinfo/extmetadata) | https://commons.wikimedia.org/wiki/File:Amtrak_into_Chicago_Jan_1995.webm (at 0:28) |
| c-edison-storefronts | chicago | 06 | 39 | sodium-orange | L→R | 2 (3.39) | CC-BY | Wikimedia Commons API (imageinfo/extmetadata) | https://commons.wikimedia.org/wiki/File:Flying_Around_Edison_Park_Chicago_3am.webm (at 6:41) |
| c-scenes74-streets | chicago | 06 | 44 | wet-black | L→R | 2 (8.91) | PD | Wikimedia Commons API (imageinfo/extmetadata) | https://commons.wikimedia.org/wiki/File:Chicago_Scenes_(ca._1974).webm (at 0:16) |
| c-18th-platform | chicago | 07 | 15 | red-neon | still | 5 (27.47) | CC-BY | Wikimedia Commons API (imageinfo/extmetadata) | https://commons.wikimedia.org/wiki/File:18th_Street_Station_Circa_April_1988_(Silent).webm (at 1:05) |
| c-impr-crossing | chicago | 07 | 6 | sodium-orange | L→R | 2 (7.55) | CC-BY | Wikimedia Commons API (imageinfo/extmetadata) | https://commons.wikimedia.org/wiki/File:Chicago_Impressions.webm (at 3:59) |
| c-impr-people | chicago | 07 | 21 | wet-black | L→R | 2 (3.02) | CC-BY | Wikimedia Commons API (imageinfo/extmetadata) | https://commons.wikimedia.org/wiki/File:Chicago_Impressions.webm (at 0:14) |
| c-scenes74-crowd | chicago | 07 | 31 | sodium-orange | L→R | 3 (16.68) | PD | Wikimedia Commons API (imageinfo/extmetadata) | https://commons.wikimedia.org/wiki/File:Chicago_Scenes_(ca._1974).webm (at 6:39) |
| c-94-title | chicago | 08 | 12 | green | still | 3 (12.87) | CC-BY | Wikimedia Commons API (imageinfo/extmetadata) | https://commons.wikimedia.org/wiki/File:Chicago_1994.webm (at 0:00) |
| c-cermak-arrive | chicago | 08 | 28 | mono-gray | toward | 2 (7.56) | CC-BY | Wikimedia Commons API (imageinfo/extmetadata) | https://commons.wikimedia.org/wiki/File:Cermak_Green_Line_Station-Night_March_2015.webm (at 1:07) |
| c-harrison-arrive | chicago | 08 | 20 | mono-gray | toward | 4 (17.19) | CC-BY-SA | Wikimedia Commons API (imageinfo/extmetadata) | https://commons.wikimedia.org/wiki/File:CTA_Harrison.ogv (at 1:10) |
| c-metra92-chyron | chicago | 08 | 20 | wet-black | still | 1 (0.51) | CC-BY | Wikimedia Commons API (imageinfo/extmetadata) | https://commons.wikimedia.org/wiki/File:Chicago_Metra_Action_1992!.webm (at 0:00) |
| c-cermak-signs | chicago | 10 | 25 | mono-gray | still | 3 (9.58) | CC-BY | Wikimedia Commons API (imageinfo/extmetadata) | https://commons.wikimedia.org/wiki/File:Cermak_Green_Line_Station-Night_March_2015.webm (at 0:30) |
| c-harrison-sign | chicago | 10 | 24 | mono-gray | still | 2 (8.24) | CC-BY-SA | Wikimedia Commons API (imageinfo/extmetadata) | https://commons.wikimedia.org/wiki/File:CTA_Harrison.ogv (at 0:34) |
| c-snow-people | chicago | 12 | 29 | sodium-orange | still | 3 (14.84) | CC-BY | Wikimedia Commons API (imageinfo/extmetadata) | https://commons.wikimedia.org/wiki/File:Chicago_Snowpocalypse_%27011_Part_2.webm (at 10:16) |
| c-classic-ic93 | chicago | 13 | 25 | steel-blue | still | 1 (1.11) | CC-BY | Wikimedia Commons API (imageinfo/extmetadata) | https://commons.wikimedia.org/wiki/File:Classic_Illinois_Central_in_Illinois_1993.webm (at 9:20) |
| c-ic93-datestamp | chicago | 13 | 20 | steel-blue | still | 3 (11.58) | CC-BY | Wikimedia Commons API (imageinfo/extmetadata) | https://commons.wikimedia.org/wiki/File:More_Illinois_Central_Action_1993!.webm (at 0:00) |
| c-rain93-nasa | chicago | 13 | 40 | wet-black | still | 1 (1.22) | PD | Wikimedia Commons API (imageinfo/extmetadata) | https://commons.wikimedia.org/wiki/File:1993_US_Rain.ogv (at 0:00) |
| a-acroni-fast | counter-A | 14 | 10 | wet-black | L→R | 5 (26.52) | CC-BY-SA | Wikimedia Commons API (imageinfo/extmetadata) | https://commons.wikimedia.org/wiki/File:Proizvodnja_vro%C4%8De_valjane_debele_plo%C4%8Devine_v_Acroni_SIJ_Jesenice.ogv (at 0:40) |
| a-acroni-rolls | counter-A | 14 | 16 | wet-black | R→L | 4 (23.27) | CC-BY-SA | Wikimedia Commons API (imageinfo/extmetadata) | https://commons.wikimedia.org/wiki/File:Proizvodnja_vro%C4%8De_valjane_debele_plo%C4%8Devine_v_Acroni_SIJ_Jesenice.ogv (at 5:30) |
| a-acroni-runout | counter-A | 14 | 16 | wet-black | L→R | 2 (5.79) | CC-BY-SA | Wikimedia Commons API (imageinfo/extmetadata) | https://commons.wikimedia.org/wiki/File:Proizvodnja_vro%C4%8De_valjane_debele_plo%C4%8Devine_v_Acroni_SIJ_Jesenice.ogv (at 2:50) |
| a-artemis-cam | counter-A | 14 | 12 | sodium-orange | down | 2 (8.79) | PD | NASA Images API (images-api.nasa.gov) | https://images.nasa.gov/details/Artemis I - Rocket Camera Footage (at 0:02) |
| a-drama-pour | counter-A | 14 | 20 | mono-gray | down | 2 (7.31) | PD | archive.org metadata API | https://archive.org/details/gov.archives.arc.12505?start=500 |
| a-drama-sparks | counter-A | 14 | 15 | mono-gray | down | 2 (4.46) | PD | archive.org metadata API | https://archive.org/details/gov.archives.arc.12505?start=1140 |
| a-drama-tilt | counter-A | 14 | 12 | mono-gray | down | 3 (11.48) | PD | archive.org metadata API | https://archive.org/details/gov.archives.arc.12505?start=851 |
| a-drama-wire | counter-A | 14 | 12 | mono-gray | R→L | 4 (23.4) | PD | archive.org metadata API | https://archive.org/details/gov.archives.arc.12505?start=1550 |
| a-ecsteel-train | counter-A | 14 | 10 | steel-blue | R→L | 4 (18.04) | CC-BY | Wikimedia Commons API (imageinfo/extmetadata) | https://commons.wikimedia.org/wiki/File:Steel_Mills_East_Chicago_%26_Indiana_Harbor.webm (at 0:38) |
| a-forge-hammer | counter-A | 14 | 12 | wet-black | down | 2 (5.19) | CC-BY | Wikimedia Commons API (imageinfo/extmetadata) | https://commons.wikimedia.org/wiki/File:Hammerverst%C3%A4hlung.webm (at 11:26) |
| a-fsb-plume | counter-A | 14 | 15 | sodium-orange | still | 2 (4.95) | PD | NASA Images API (images-api.nasa.gov) | https://images.nasa.gov/details/MSFC_XP01_V_0133_FSB1_BROLL (at 0:30) |
| a-hendrichs-drop | counter-A | 14 | 12 | mono-gray | down | 4 (23.38) | CC-BY | Wikimedia Commons API (imageinfo/extmetadata) | https://commons.wikimedia.org/wiki/File:Gesenkschmiede_Hendrichs.webm (at 7:39) |
| a-inland-train | counter-A | 14 | 18 | sodium-orange | R→L | 5 (26.01) | CC-BY | Wikimedia Commons API (imageinfo/extmetadata) | https://commons.wikimedia.org/wiki/File:Inland_Steel_(ArcelorMittal)_as_seen_from_train.webm (at 0:22) |
| a-inland-train2 | counter-A | 14 | 13 | sodium-orange | R→L | 5 (29.97) | CC-BY | Wikimedia Commons API (imageinfo/extmetadata) | https://commons.wikimedia.org/wiki/File:Inland_Steel_(ArcelorMittal)_as_seen_from_train.webm (at 1:54) |
| a-irontap | counter-A | 14 | 14 | red-neon | down | 4 (18.08) | CC-BY-SA | Wikimedia Commons API (imageinfo/extmetadata) | https://commons.wikimedia.org/wiki/File:%D0%92%D1%8B%D0%BF%D1%83%D1%81%D0%BA_%D1%87%D1%83%D0%B3%D1%83%D0%BD%D0%B0_%D0%B8%D0%B7_%D0%B4%D0%BE%D0%BC%D0%B5%D0%BD%D0%BD%D0%BE%D0%B9_%D0%BF%D0%B5%D1%87%D0%B8.webm (at 0:04) |
| a-kover-billets | counter-A | 14 | 15 | sodium-orange | L→R | 3 (13.65) | CC-BY | Wikimedia Commons API (imageinfo/extmetadata) | https://commons.wikimedia.org/wiki/File:HISTORIAA_%E2%80%A2_OVAKON_Koverharin_ter%C3%A4stehdas_1982_-_ter%C3%A4ksen_valmistus.webm (at 14:20) |
| a-kover-fast | counter-A | 14 | 9 | wet-black | L→R | 4 (23.53) | CC-BY | Wikimedia Commons API (imageinfo/extmetadata) | https://commons.wikimedia.org/wiki/File:HISTORIAA_%E2%80%A2_OVAKON_Koverharin_ter%C3%A4stehdas_1982_-_ter%C3%A4ksen_valmistus.webm (at 4:25) |
| a-kover-ladle | counter-A | 14 | 15 | sodium-orange | down | 2 (3.15) | CC-BY | Wikimedia Commons API (imageinfo/extmetadata) | https://commons.wikimedia.org/wiki/File:HISTORIAA_%E2%80%A2_OVAKON_Koverharin_ter%C3%A4stehdas_1982_-_ter%C3%A4ksen_valmistus.webm (at 12:11) |
| a-mills-fast | counter-A | 14 | 11 | wet-black | L→R | 4 (24.4) | PD | Wikimedia Commons API (imageinfo/extmetadata) | https://commons.wikimedia.org/wiki/File:Men_and_Mills,_c._1950.webm (at 31:44) |
| a-mills-roll | counter-A | 14 | 11 | wet-black | L→R | 3 (11.14) | PD | Wikimedia Commons API (imageinfo/extmetadata) | https://commons.wikimedia.org/wiki/File:Men_and_Mills,_c._1950.webm (at 25:52) |
| a-servant-furnace | counter-A | 14 | 20 | sodium-orange | still | 3 (12.87) | PD | archive.org metadata API | https://archive.org/details/steel-man-s-servant-1938?start=596 |
| a-servant-ladle | counter-A | 14 | 20 | sodium-orange | down | 3 (9.07) | PD | archive.org metadata API | https://archive.org/details/steel-man-s-servant-1938?start=868 |
| a-servant-pour | counter-A | 14 | 25 | sodium-orange | down | 2 (3.18) | PD | archive.org metadata API | https://archive.org/details/steel-man-s-servant-1938?start=952 |
| a-servant-roll | counter-A | 14 | 15 | sodium-orange | R→L | 3 (10.31) | PD | archive.org metadata API | https://archive.org/details/steel-man-s-servant-1938?start=1230 |
| a-servant-slab | counter-A | 14 | 25 | sodium-orange | L→R | 4 (20.66) | PD | archive.org metadata API | https://archive.org/details/steel-man-s-servant-1938?start=1090 |
| a-servant-tap | counter-A | 14 | 20 | sodium-orange | down | 3 (9.69) | PD | archive.org metadata API | https://archive.org/details/steel-man-s-servant-1938?start=720 |
| a-ssy-glare | counter-A | 14 | 20 | wet-black | still | 3 (9.96) | PD | archive.org metadata API | https://archive.org/details/SteelASy1936?start=270 |
| a-ssy-pour | counter-A | 14 | 20 | wet-black | down | 2 (6.43) | PD | archive.org metadata API | https://archive.org/details/SteelASy1936?start=700 |
| a-ssy-sparks | counter-A | 14 | 15 | wet-black | down | 2 (8.71) | PD | archive.org metadata API | https://archive.org/details/SteelASy1936?start=390 |
| a-vicart-sparks | counter-A | 14 | 14 | sodium-orange | down | 3 (13.38) | CC-BY | Wikimedia Commons API (imageinfo/extmetadata) | https://commons.wikimedia.org/wiki/File:Vicart_-_Aci%C3%A9rie.webm (at 0:10) |
| a-westinghouse-1904 | counter-A | 14 | 12 | mono-gray | down | 3 (9.58) | PD | Wikimedia Commons API (imageinfo/extmetadata) | https://commons.wikimedia.org/wiki/File:Casting_a_Guide_Box_-_Westinghouse_Works.webm (at 2:00) |
| b-bean-germ | counter-B | 15 | 25 | mono-gray | up | 1 (2.64) | PD | archive.org metadata API | https://archive.org/details/6109_Growing_Things_A_Film_Lesson_in_Nature_Study_01_00_43_01?start=215 |
| b-blue-flowers | counter-B | 15 | 20 | steel-blue | up | 1 (0.69) | CC0 | archive.org metadata API | https://archive.org/details/TimelapseOfOpeningFlowersOnBlueScreen?start=0 |
| b-cloudcomp | counter-B | 15 | 12 | mono-gray | L→R | 5 (28.99) | PD | Wikimedia Commons API (imageinfo/extmetadata) | https://commons.wikimedia.org/wiki/File:Timelapse_Clouds_Compilation.ogv (at 0:00) |
| b-cloudcomp2 | counter-B | 15 | 12 | wet-black | up | 4 (24.72) | PD | Wikimedia Commons API (imageinfo/extmetadata) | https://commons.wikimedia.org/wiki/File:Timelapse_Clouds_Compilation.ogv (at 2:36) |
| b-clouds | counter-B | 15 | 20 | green | up | 1 (0.53) | PD | Wikimedia Commons API (imageinfo/extmetadata) | https://commons.wikimedia.org/wiki/File:Cloud_evolution_in_under_a_minute.ogv (at 0:00) |
| b-echinopsis | counter-B | 15 | 20 | red-neon | toward | 1 (0.56) | CC-BY | Wikimedia Commons API (imageinfo/extmetadata) | https://commons.wikimedia.org/wiki/File:Antares_Hybrid_Echinopsis_Flower_Opening_Time_Lapse_..._Six_Flowers_at_Once.webm (at 0:00) |
| b-funnel | counter-B | 15 | 12 | white-glare | down | 4 (19.77) | CC-BY | Wikimedia Commons API (imageinfo/extmetadata) | https://commons.wikimedia.org/wiki/File:Funnel_Cloud_over_city_of_Ljubljana_Slovenia_23.7.2011.webm (at 0:13) |
| b-gardenia | counter-B | 15 | 20 | green | toward | 1 (0.65) | CC-BY | Wikimedia Commons API (imageinfo/extmetadata) | https://commons.wikimedia.org/wiki/File:Time_lapse_of_a_gardenia_flower_opening.webm (at 0:00) |
| b-hurricane | counter-B | 15 | 20 | wet-black | R→L | 2 (4.7) | PD | Wikimedia Commons API (imageinfo/extmetadata) | https://commons.wikimedia.org/wiki/File:Hurricane-Matthew_4k-Time_Lapse.webm (at 0:00) |
| b-iss-earth | counter-B | 15 | 12 | wet-black | toward | 3 (14.98) | PD | Wikimedia Commons API (imageinfo/extmetadata) | https://commons.wikimedia.org/wiki/File:Earth_Illuminated-_ISS_Time-lapse_Photography.webm (at 0:26) |
| b-iss-night | counter-B | 15 | 15 | wet-black | toward | 2 (4.12) | PD | Wikimedia Commons API (imageinfo/extmetadata) | https://commons.wikimedia.org/wiki/File:ISS073-E-1249495-1253256-20251112-Night_-_2025-11-12_ISS073_3762_Night.webm (at 0:00) |
| b-lemaire | counter-B | 15 | 12 | steel-blue | toward | 3 (10.36) | CC-BY | Wikimedia Commons API (imageinfo/extmetadata) | https://commons.wikimedia.org/wiki/File:Time-lapse_of_navigation_through_Lemaire_Channel,_Antarctica.webm (at 1:22) |
| b-muldrow | counter-B | 15 | 26 | mono-gray | L→R | 4 (19.51) | PD | archive.org metadata API | https://archive.org/details/nps-video-dena-muldrow-surge-time-lapse-may-8-to-july-1-2021?start=0 |
| b-plantgrowth | counter-B | 15 | 25 | wet-black | up | 1 (1.17) | PD | archive.org metadata API | https://archive.org/details/PlantGrowth?start=0 |
| b-pond-green | counter-B | 15 | 20 | green | still | 3 (15.97) | PD | archive.org metadata API | https://archive.org/details/SpringCo1952?start=500 |
| b-pond-rain | counter-B | 15 | 22 | sodium-orange | still | 3 (16.32) | PD | archive.org metadata API | https://archive.org/details/SpringCo1952?start=250 |
| b-pond-water | counter-B | 15 | 22 | wet-black | still | 2 (6.34) | PD | archive.org metadata API | https://archive.org/details/SpringCo1952?start=40 |
| b-rose-black | counter-B | 15 | 8 | green | toward | 1 (1.58) | CC-BY | Wikimedia Commons API (imageinfo/extmetadata) | https://commons.wikimedia.org/wiki/File:Time-lapse_of_opening_red_rose_isolated_on_black_background.Blooming_red_roses_flower_buds.webm (at 0:00) |
| b-rose-open | counter-B | 15 | 15 | green | toward | 2 (4.35) | CC-BY | Wikimedia Commons API (imageinfo/extmetadata) | https://commons.wikimedia.org/wiki/File:Time-lapse_of_a_flower_blooming.webm (at 0:00) |
| b-sthelens | counter-B | 15 | 18 | steel-blue | up | 2 (4.76) | PD | Wikimedia Commons API (imageinfo/extmetadata) | https://commons.wikimedia.org/wiki/File:Time-lapse_images_of_Mount_St._Helens_dome_growth_2004-2008.webm (at 0:10) |
| b-winter-train | counter-B | 15 | 15 | mono-gray | L→R | 3 (11.74) | PD | archive.org metadata API | https://archive.org/details/gov.archives.arc.12505?start=681 |
| b-winters-end | counter-B | 15 | 15 | steel-blue | still | 3 (12.41) | CC0 | Wikimedia Commons API (imageinfo/extmetadata) | https://commons.wikimedia.org/wiki/File:Timelapse_of_Winter%27s_End_at_Bertram_Creek_Park_overlooking_Okanagan_Lake,_includes_Snowmelt,_Sunset_and_Venus_Set.webm (at 0:05) |
| b-yaki-storm | counter-B | 15 | 15 | steel-blue | L→R | 1 (1.31) | PD | Wikimedia Commons API (imageinfo/extmetadata) | https://commons.wikimedia.org/wiki/File:Time-lapse_Video-_Winter_Storm_at_Yaki_Point_Grand_Canyon_2014-01-31_(12242435983).webm (at 0:05) |
| w-biolum-blue | wildcard | 16 | 6 | wet-black | still | 2 (3.82) | PD | archive.org metadata API | https://archive.org/details/noaa-oe-video-edu-resources-dsd-bioluminescence?start=6 |
| w-biolum-chain | wildcard | 16 | 12 | steel-blue | still | 1 (1.91) | PD | archive.org metadata API | https://archive.org/details/noaa-oe-video-edu-resources-dsd-bioluminescence?start=336 |
| w-biolum-swarm | wildcard | 16 | 14 | steel-blue | still | 1 (1.75) | PD | archive.org metadata API | https://archive.org/details/noaa-oe-video-edu-resources-dsd-bioluminescence?start=462 |
| w-press-1937 | wildcard | 16 | 26 | wet-black | down | 4 (22.25) | PD | Wikimedia Commons API (imageinfo/extmetadata) | https://commons.wikimedia.org/wiki/File:Tidningstryck_1937.ogv (at 1:18) |
| w-press-lvrj | wildcard | 16 | 16 | wet-black | up | 4 (18.99) | CC-BY | Wikimedia Commons API (imageinfo/extmetadata) | https://commons.wikimedia.org/wiki/File:The_910_ton_printing_presses_at_the_Las_Vegas_Review-Journal_were_the_largest_in_the_world_when_installed_in_2000.webm (at 0:00) |
| w-press-vanuatu | wildcard | 16 | 28 | sodium-orange | L→R | 4 (17.36) | CC-BY | Wikimedia Commons API (imageinfo/extmetadata) | https://commons.wikimedia.org/wiki/File:Printing_the_Paper.webm (at 0:12) |
| w-shrimp-spew | wildcard | 16 | 11 | wet-black | L→R | 2 (3.6) | PD | archive.org metadata API | https://archive.org/details/noaa-oe-video-explorations-19biolum-logs-jun16-media-shrimp-spew?start=0 |
| w-squid | wildcard | 16 | 22 | wet-black | still | 1 (1.35) | PD | archive.org metadata API | https://archive.org/details/noaa-oe-video-edu-themes-bioluminescence-media-multimedia-giant-squid?start=0 |
