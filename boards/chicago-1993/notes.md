# RAIN, 1993 — Chicago bus stop mood board: notes and spec

**Room:** tldraw live room `chicago-1993-bus-stop` (link in `board/.link`). **Repo:** `thtopher/moodboards`, media under `assets/chicago-1993/`.

## The world
A rainy night in 1993 at the **#49 Western** stop at **Lawrence & Western, Lincoln Square**, on Chicago's North Side. It's a working, middle-class city neighborhood: two- and three-flats, a corner tavern, a Walgreens, and the Brown Line (Ravenswood) at Western nearby. It's not a suburb and not a rough block. The bus is a CTA Flxible Metro. Rain on sodium light, wet asphalt, fluorescent shop glow, and the radio forecast saying "rain developing."

## Zones
01 The corner · 02 Light, dusk to sodium · 03 Rain · 04 The bus · 05 The people · 06 The neighborhood · 07 The L · 08 Camera · 09 Color strip · 10 Type & signage · 11 Sound · 12 Voice · 13 1993 timeline · 14 Counter-world A, steel · 15 Counter-world B, time-lapse and seasons · 16 Wildcards · 17 Match-cut pairs · 18 Footage index · 19 Pace ramp. Legend at the top left.

## Footage library
- Masters (H.264, source resolution): `/workspace/moodboard/chicago-1993/footage/<id>.mp4` on the box only, **not in git**.
- 480p proxies: `assets/chicago-1993/proxies/<id>.mp4` (raw.githubusercontent URLs); posters `assets/chicago-1993/posters/`; contact sheets `footage/sheets/<id>.jpg` (box).
- Catalog: `footage/catalog.csv` and `footage/catalog.json` (also copied to `boards/chicago-1993/` in the repo).

**96 clips, 39.3 min.**

| world | clips | min |
|---|---|---|
| chicago | 45 | 23.8 |
| counter-A | 23 | 6.6 |
| counter-B | 20 | 6.6 |
| wildcard | 8 | 2.3 |

### Minutes per pace step

| world | P1 | P2 | P3 | P4 | P5 |
|---|---|---|---|---|---|
| chicago | 2.6 | 3.9 | 4.8 | 7.9 | 4.6 |
| counter (all) | 4.3 | 4.4 | 3.4 | 2.7 | 0.8 |
| counter-A | 0.5 | 1.8 | 2.5 | 1.1 | 0.8 |
| counter-B | 3.0 | 2.3 | 1.0 | 0.4 | 0.0 |
| wildcard | 0.8 | 0.3 | 0.0 | 1.2 | 0.0 |

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
| rights / license | PD · CC0 · CC-BY · REF | REF = reference only, not cleared |

## Pace calibration
`pace_raw = 0.6 × flow_p50 + 0.4 × flow_p90`. Farneback dense optical flow, in px/s on frames downscaled to 160 px wide at 6 fps. Cuts are detected (framediff spikes) and excluded from the flow statistics.
Thresholds: **1** <3 near-static · **2** 3–9 slow · **3** 9–17 medium · **4** 17–25 brisk · **5** ≥25 high-velocity.
I calibrated by eye at the extremes and the boundaries. Locked-off time-lapse and still plates fall at 0–3. Bus pass-bys and lateral cab rides fall at 17–30. Night-drive streaks and the hot-strip mill run-out reach 25+. Raw values are in the catalog, so the steps can be re-cut.

## Match-cut pairs (zone 17)
Pairs share at least 3 of: color, direction, pace (±1), size, angle, move. Each pair was then checked for a visual or sound rhyme. The one-line notes are on the board.
t-rain-lens↔a-servant-slab · t-rain-puddle-ecu↔a-servant-pour · c-flx-pass↔a-drama-wire · c-cab-rav-canopy↔a-hsm-overhead · c-flx-arrive↔a-servant-furnace · t-rain-neon↔a-ssy-sparks · c-skyline-lights-on↔w-biolum-swarm · c-wbbm-accuweather↔b-pond-green · t-rain-feet↔a-hsm-rolls · t-rain-wet-street↔b-muldrow · c-wls-traffic↔w-biolum-chain · c-vhs-drive-streaks↔a-hsm-mill2

## Board build
The skeleton push was the only full push. Everything after it was pull-then-targeted patches (`board/p*.json`). The footage index (18) and pace ramp (19) use poster images that click through to the proxy, to keep the number of video players down. Zones 01–08, 10, 12–17 use playable video shapes.
Hosting: proxies play from raw.githubusercontent.com (verified in headless Chrome: currentTime advances, readyState 4, 0 console errors). GitHub Pages is not enabled. raw serves `application/octet-stream`, which Safari may refuse to play inline. Fallback is the poster plus the original link.

## Rights
- Stills: 75, all from Wikimedia Commons (PD or CC BY / BY-SA). Attribution is on each caption and in `images/stills.json`.
- Clips: Counter({'REF': 61, 'PD': 28, 'CC-BY': 6, 'CC0': 1}). REF items (YouTube uploads, station broadcasts, Kinolibrary previews) are **reference only, not cleared**. Their 480p proxies are in a public repo; take them down or make the repo private before sharing widely.
- Copyrighted films (Thief, Hoop Dreams, The Fugitive, Night on Earth, Chungking Express) and 1993 music are link-only REF cards.
- Rain plates are stand-ins (some are not Chicago or not 1993). Several stills are modern photos of 1993-era locations.

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

| id | world | zone | s | color | dir | pace (raw) | rights | original |
|---|---|---|---|---|---|---|---|---|
| c-skyline-lake-night | chicago | 02 | 44 | wet-black | still | 1 (1.37) | REF | https://www.youtube.com/watch?v=65-CBHHz1aE&t=0s |
| c-marina-bluehour | chicago | 02 | 30 | steel-blue | still | 2 (3.19) | REF | https://www.youtube.com/watch?v=6KGXEKXPp5k&t=0s |
| c-marina-night | chicago | 02 | 35 | wet-black | still | 1 (2.52) | REF | https://www.youtube.com/watch?v=6KGXEKXPp5k&t=150s |
| c-skyline-sunset | chicago | 02 | 40 | sodium-orange | still | 1 (0.23) | REF | https://www.youtube.com/watch?v=gqmYzZf0ONo&t=0s |
| c-skyline-lights-on | chicago | 02 | 32 | steel-blue | still | 1 (0.28) | REF | https://www.youtube.com/watch?v=gqmYzZf0ONo&t=284s |
| c-vhs-drive-sodium | chicago | 02 | 58 | sodium-orange | toward | 5 (29.25) | REF | https://www.youtube.com/watch?v=BUZQW2v2meM&t=0s |
| c-vhs-drive-streaks | chicago | 08 | 30 | sodium-orange | toward | 4 (23.84) | REF | https://www.youtube.com/watch?v=BUZQW2v2meM&t=88s |
| c-vhs-skyline-drive | chicago | 06 | 32 | mono-gray | L→R | 5 (26.09) | REF | https://www.youtube.com/watch?v=BUZQW2v2meM&t=128s |
| c-vhs-storefronts | chicago | 05 | 24 | sodium-orange | still | 5 (31.55) | REF | https://www.youtube.com/watch?v=BUZQW2v2meM&t=212s |
| c-night-drive-98 | chicago | 02 | 11 | sodium-orange | toward | 4 (18.16) | REF | https://www.youtube.com/watch?v=6RZ1jcNaEb8&t=0s |
| c-cab-lake-title | chicago | 08 | 12 | wet-black | still | 2 (8.08) | REF | https://www.youtube.com/watch?v=Nty8Y8GzAAM&t=0s |
| c-cab-lake-oncoming | chicago | 06 | 40 | mono-gray | toward | 4 (19.63) | REF | https://www.youtube.com/watch?v=Nty8Y8GzAAM&t=1058s |
| c-cab-lake-loop | chicago | 06 | 60 | mono-gray | toward | 4 (17.49) | REF | https://www.youtube.com/watch?v=Nty8Y8GzAAM&t=1500s |
| c-cab-rav-loop | chicago | 06 | 50 | mono-gray | toward | 3 (13.58) | REF | https://www.youtube.com/watch?v=rZ7PSQYUI80&t=0s |
| c-cab-rav-pass | chicago | 06 | 50 | cyan-fluorescent | toward | 4 (21.88) | REF | https://www.youtube.com/watch?v=rZ7PSQYUI80&t=810s |
| c-cab-rav-north | chicago | 01 | 60 | cyan-fluorescent | toward | 3 (12.78) | REF | https://www.youtube.com/watch?v=rZ7PSQYUI80&t=1260s |
| c-cab-rav-backs | chicago | 06 | 57 | mono-gray | toward | 4 (19.4) | REF | https://www.youtube.com/watch?v=H2SF-uG4UYI&t=76s |
| c-cab-rav-canopy | chicago | 05 | 43 | wet-black | toward | 3 (12.28) | REF | https://www.youtube.com/watch?v=H2SF-uG4UYI&t=247s |
| c-trains-arrive-93 | chicago | 08 | 32 | mono-gray | toward | 4 (23.0) | REF | https://www.youtube.com/watch?v=eqTpnx8kXFU&t=298s |
| c-trains-platform-93 | chicago | 08 | 26 | mono-gray | R→L | 4 (18.88) | REF | https://www.youtube.com/watch?v=eqTpnx8kXFU&t=358s |
| c-logan-flats | chicago | 06 | 28 | sodium-orange | still | 5 (30.25) | REF | https://www.youtube.com/watch?v=Q05UetheZEg&t=120s |
| c-logan-graystones | chicago | 06 | 30 | mono-gray | L→R | 5 (27.55) | REF | https://www.youtube.com/watch?v=Q05UetheZEg&t=170s |
| c-lincoln-blockparty | chicago | 07 | 30 | mono-gray | still | 4 (24.44) | REF | https://www.youtube.com/watch?v=x2ZonMufpTQ&t=60s |
| c-wild-night-taxi | chicago | 07 | 12 | sodium-orange | L→R | 5 (26.72) | REF | https://www.youtube.com/watch?v=HXYSzMTXUTA&t=10s |
| c-flx-interior | chicago | 04 | 31 | mono-gray | toward | 5 (44.75) | REF | https://www.youtube.com/watch?v=itgzLEipyNU&t=9s |
| c-flx-arrive | chicago | 04 | 30 | mono-gray | toward | 3 (11.69) | REF | https://www.youtube.com/watch?v=aokh0S7BoM8&t=0s |
| c-flx-pass | chicago | 04 | 14 | mono-gray | R→L | 4 (21.03) | REF | https://www.youtube.com/watch?v=hHWzn6GjHTM&t=6s |
| c-flx-garage | chicago | 04 | 16 | steel-blue | L→R | 3 (15.88) | REF | https://www.youtube.com/watch?v=-1LMRwcLZCg&t=0s |
| c-bulls96-bokeh | chicago | 02 | 13 | red-neon | L→R | 5 (31.21) | REF | https://www.youtube.com/watch?v=Ix0o9KKXD90&t=21s |
| c-bulls96-drive | chicago | 02 | 18 | red-neon | toward | 5 (25.24) | REF | https://www.youtube.com/watch?v=Ix0o9KKXD90&t=42s |
| c-bulls96-crowd | chicago | 07 | 32 | red-neon | still | 5 (27.85) | REF | https://www.youtube.com/watch?v=Ix0o9KKXD90&t=180s |
| c-bulls92-division | chicago | 13 | 26 | red-neon | R→L | 3 (14.97) | REF | https://www.youtube.com/watch?v=frHHXtgmYpk&t=0s |
| c-wbbm-fire-night | chicago | 12 | 25 | mono-gray | up | 3 (9.2) | REF | https://archive.org/details/wbbm-tv-530pm-news-december-12-1993?start=780 |
| c-wbbm-woolworth | chicago | 13 | 25 | mono-gray | still | 2 (5.22) | REF | https://archive.org/details/wbbm-tv-530pm-news-december-12-1993?start=912 |
| c-wbbm-accuweather | chicago | 10 | 72 | green | still | 2 (7.31) | REF | https://archive.org/details/wbbm-tv-530pm-news-december-12-1993?start=1060 |
| c-wbbm-bulls | chicago | 13 | 44 | mono-gray | L→R | 4 (20.73) | REF | https://archive.org/details/wbbm-tv-530pm-news-december-12-1993?start=1536 |
| c-wbbm-jewel | chicago | 05 | 22 | steel-blue | still | 3 (10.18) | REF | https://archive.org/details/wbbm-tv-530pm-news-december-12-1993?start=540 |
| c-wls-traffic | chicago | 10 | 18 | steel-blue | still | 2 (7.44) | REF | https://archive.org/details/wls-tv-4pm-news-may-18-1993?start=672 |
| c-wls-skyline-night | chicago | 02 | 16 | sodium-orange | still | 2 (6.78) | REF | https://archive.org/details/wls-tv-4pm-news-may-18-1993?start=2120 |
| t-rain-puddle-ecu | chicago | 03 | 6 | sodium-orange | down | 1 (1.4) | REF | https://www.youtube.com/watch?v=zDpGdDFh8Hs&t=0s |
| t-rain-feet | chicago | 03 | 16 | wet-black | L→R | 3 (13.82) | REF | https://www.youtube.com/watch?v=zDpGdDFh8Hs&t=164s |
| t-rain-pavement-night | chicago | 03 | 36 | wet-black | away | 4 (19.62) | REF | https://www.youtube.com/watch?v=ypYHOJ2QkXY&t=0s |
| t-rain-neon | chicago | 03 | 60 | red-neon | still | 2 (5.33) | REF | https://www.youtube.com/watch?v=ypYHOJ2QkXY&t=90s |
| t-rain-wet-street | chicago | 03 | 20 | mono-gray | L→R | 4 (23.36) | REF | https://www.youtube.com/watch?v=mnQiLtBx-OY&t=130s |
| t-rain-lens | chicago | 03 | 23 | sodium-orange | L→R | 4 (23.37) | REF | https://www.youtube.com/watch?v=mnQiLtBx-OY&t=385s |
| a-ssy-glare | counter-A | 14 | 20 | wet-black | still | 3 (9.96) | PD | https://archive.org/details/SteelASy1936?start=270 |
| a-ssy-sparks | counter-A | 14 | 15 | wet-black | down | 2 (8.71) | PD | https://archive.org/details/SteelASy1936?start=390 |
| a-ssy-pour | counter-A | 14 | 20 | wet-black | down | 2 (6.43) | PD | https://archive.org/details/SteelASy1936?start=700 |
| a-hsm-steam | counter-A | 14 | 20 | wet-black | up | 3 (12.33) | REF | https://archive.org/details/fc-fc-4518?start=153 |
| a-hsm-rolls | counter-A | 14 | 20 | wet-black | L→R | 3 (9.31) | REF | https://archive.org/details/fc-fc-4518?start=450 |
| a-hsm-runout | counter-A | 14 | 20 | wet-black | R→L | 5 (27.71) | REF | https://archive.org/details/fc-fc-4518?start=540 |
| a-drama-pour | counter-A | 14 | 20 | mono-gray | down | 2 (7.31) | PD | https://archive.org/details/gov.archives.arc.12505?start=500 |
| a-drama-sparks | counter-A | 14 | 15 | mono-gray | down | 2 (4.46) | PD | https://archive.org/details/gov.archives.arc.12505?start=1140 |
| a-servant-furnace | counter-A | 14 | 20 | sodium-orange | still | 3 (12.87) | PD | https://archive.org/details/steel-man-s-servant-1938?start=596 |
| a-servant-tap | counter-A | 14 | 20 | sodium-orange | down | 3 (9.69) | PD | https://archive.org/details/steel-man-s-servant-1938?start=720 |
| a-servant-ladle | counter-A | 14 | 20 | sodium-orange | down | 3 (9.07) | PD | https://archive.org/details/steel-man-s-servant-1938?start=868 |
| a-servant-pour | counter-A | 14 | 25 | sodium-orange | down | 2 (3.18) | PD | https://archive.org/details/steel-man-s-servant-1938?start=952 |
| a-servant-slab | counter-A | 14 | 25 | sodium-orange | L→R | 4 (20.66) | PD | https://archive.org/details/steel-man-s-servant-1938?start=1090 |
| a-servant-roll | counter-A | 14 | 15 | sodium-orange | R→L | 3 (10.31) | PD | https://archive.org/details/steel-man-s-servant-1938?start=1230 |
| a-modern-slab | counter-A | 14 | 14 | cyan-fluorescent | still | 1 (1.13) | REF | https://archive.org/details/oamodern-steel-making?start=322 |
| a-modern-pour | counter-A | 14 | 15 | sodium-orange | down | 2 (4.84) | REF | https://archive.org/details/oamodern-steel-making?start=462 |
| a-modern-ingot | counter-A | 14 | 15 | red-neon | still | 1 (1.57) | REF | https://archive.org/details/oamodern-steel-making?start=686 |
| b-growth-bloom | counter-B | 15 | 20 | mono-gray | up | 2 (5.31) | REF | https://archive.org/details/200634_The_Growth_of_Plants?start=18 |
| b-growth-tendril | counter-B | 15 | 20 | mono-gray | up | 2 (7.99) | REF | https://archive.org/details/200634_The_Growth_of_Plants?start=90 |
| b-growth-flower | counter-B | 15 | 20 | mono-gray | up | 2 (3.85) | REF | https://archive.org/details/200634_The_Growth_of_Plants?start=180 |
| b-trees-buds | counter-B | 15 | 20 | green | up | 2 (3.68) | REF | https://archive.org/details/4083_Seasonal_Changes_In_Trees?start=104 |
| b-trees-leaves | counter-B | 15 | 20 | green | up | 1 (2.37) | REF | https://archive.org/details/4083_Seasonal_Changes_In_Trees?start=290 |
| b-trees-winter | counter-B | 15 | 20 | green | still | 1 (1.26) | REF | https://archive.org/details/4083_Seasonal_Changes_In_Trees?start=530 |
| b-bean-germ | counter-B | 15 | 25 | mono-gray | up | 1 (2.64) | PD | https://archive.org/details/6109_Growing_Things_A_Film_Lesson_in_Nature_Study_01_00_43_01?start=215 |
| b-pond-water | counter-B | 15 | 22 | wet-black | still | 2 (6.34) | PD | https://archive.org/details/SpringCo1952?start=40 |
| b-pond-rain | counter-B | 15 | 22 | sodium-orange | still | 3 (16.32) | PD | https://archive.org/details/SpringCo1952?start=250 |
| b-pond-green | counter-B | 15 | 20 | green | still | 3 (15.97) | PD | https://archive.org/details/SpringCo1952?start=500 |
| b-plantgrowth | counter-B | 15 | 25 | wet-black | up | 1 (1.17) | PD | https://archive.org/details/PlantGrowth?start=0 |
| b-blue-flowers | counter-B | 15 | 20 | steel-blue | up | 1 (0.69) | CC0 | https://archive.org/details/TimelapseOfOpeningFlowersOnBlueScreen?start=0 |
| b-rose-open | counter-B | 15 | 15 | green | toward | 2 (4.35) | CC-BY | https://commons.wikimedia.org/wiki/File:Time-lapse_of_a_flower_blooming.webm (at 0:00) |
| b-rose-black | counter-B | 15 | 8 | green | toward | 1 (1.58) | CC-BY | https://commons.wikimedia.org/wiki/File:Time-lapse_of_opening_red_rose_isolated_on_black_background.Blooming_red_roses_flower_buds.webm (at 0:00) |
| b-gardenia | counter-B | 15 | 20 | green | toward | 1 (0.65) | CC-BY | https://commons.wikimedia.org/wiki/File:Time_lapse_of_a_gardenia_flower_opening.webm (at 0:00) |
| b-echinopsis | counter-B | 15 | 20 | red-neon | toward | 1 (0.56) | CC-BY | https://commons.wikimedia.org/wiki/File:Antares_Hybrid_Echinopsis_Flower_Opening_Time_Lapse_..._Six_Flowers_at_Once.webm (at 0:00) |
| b-clouds | counter-B | 15 | 20 | green | up | 1 (0.53) | PD | https://commons.wikimedia.org/wiki/File:Cloud_evolution_in_under_a_minute.ogv (at 0:00) |
| b-muldrow | counter-B | 15 | 26 | mono-gray | L→R | 4 (19.51) | PD | https://archive.org/details/nps-video-dena-muldrow-surge-time-lapse-may-8-to-july-1-2021?start=0 |
| b-hurricane | counter-B | 15 | 20 | wet-black | R→L | 2 (4.7) | PD | https://commons.wikimedia.org/wiki/File:Hurricane-Matthew_4k-Time_Lapse.webm (at 0:00) |
| w-biolum-blue | wildcard | 16 | 6 | wet-black | still | 2 (3.82) | PD | https://archive.org/details/noaa-oe-video-edu-resources-dsd-bioluminescence?start=6 |
| w-biolum-swarm | wildcard | 16 | 14 | steel-blue | still | 1 (1.75) | PD | https://archive.org/details/noaa-oe-video-edu-resources-dsd-bioluminescence?start=462 |
| w-biolum-chain | wildcard | 16 | 12 | steel-blue | still | 1 (1.91) | PD | https://archive.org/details/noaa-oe-video-edu-resources-dsd-bioluminescence?start=336 |
| w-shrimp-spew | wildcard | 16 | 11 | wet-black | L→R | 2 (3.6) | PD | https://archive.org/details/noaa-oe-video-explorations-19biolum-logs-jun16-media-shrimp-spew?start=0 |
| w-squid | wildcard | 16 | 22 | wet-black | still | 1 (1.35) | PD | https://archive.org/details/noaa-oe-video-edu-themes-bioluminescence-media-multimedia-giant-squid?start=0 |
| w-press-vanuatu | wildcard | 16 | 28 | sodium-orange | L→R | 4 (17.36) | CC-BY | https://commons.wikimedia.org/wiki/File:Printing_the_Paper.webm (at 0:12) |
| w-press-lvrj | wildcard | 16 | 16 | wet-black | up | 4 (18.99) | CC-BY | https://commons.wikimedia.org/wiki/File:The_910_ton_printing_presses_at_the_Las_Vegas_Review-Journal_were_the_largest_in_the_world_when_installed_in_2000.webm (at 0:00) |
| w-press-1937 | wildcard | 16 | 26 | wet-black | down | 4 (22.25) | PD | https://commons.wikimedia.org/wiki/File:Tidningstryck_1937.ogv (at 1:18) |
| a-hsm-track | counter-A | 14 | 12 | wet-black | R→L | 5 (28.05) | REF | https://archive.org/details/fc-fc-4518?start=340 |
| a-hsm-overhead | counter-A | 14 | 12 | wet-black | toward | 4 (23.36) | REF | https://archive.org/details/fc-fc-4518?start=364 |
| a-drama-wire | counter-A | 14 | 12 | mono-gray | R→L | 4 (23.4) | PD | https://archive.org/details/gov.archives.arc.12505?start=1550 |
| a-drama-tilt | counter-A | 14 | 12 | mono-gray | down | 3 (11.48) | PD | https://archive.org/details/gov.archives.arc.12505?start=851 |
| a-hsm-pan | counter-A | 14 | 15 | wet-black | R→L | 5 (38.26) | REF | https://archive.org/details/fc-fc-4518?start=56 |
| a-hsm-mill2 | counter-A | 14 | 15 | wet-black | toward | 4 (22.79) | REF | https://archive.org/details/fc-fc-4518?start=386 |
| b-winter-train | counter-B | 15 | 15 | mono-gray | L→R | 3 (11.74) | PD | https://archive.org/details/gov.archives.arc.12505?start=681 |