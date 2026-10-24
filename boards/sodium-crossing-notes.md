# Sodium Crossing — research notes

_Compiled 24 Oct 2026 (America/Chicago). Board: `sodium-crossing.tldr` (built with ../build_tldr.py from `spec_tldr.json`, which `to_tldr_spec.py` derives from `spec.json`). Render: `sodium-crossing.png`._

## Thesis

The overnight car ferry is a stateless room lit by a colour that no longer exists: low-pressure sodium, whose last lamps were made in Scotland on 31 December 2019. Between two countries, after the duty-free shutters fall, a few hundred strangers share fluorescent cafeterias, humming corridors and orange-washed steel decks. Sodium Crossing treats that night as both procedure and elegy — wayfinding, safety drills and engine drone, staged with the tenderness of something about to disappear.

**Keywords:** sodium monochrome, stateless night, procedural tenderness, car-deck geometry, 3am cafeteria, duty-free afterglow, elegy for a light source, between two countries

## Narrative

**Why this theme.** I wanted a world that's specific, not a generic 'liminal' mood, and that has a built-in reason to feel elegiac. The overnight car ferry gives you both. Low-pressure sodium light is monochromatic (589 nm), so it flattens every colour into amber or black. Its last lamps were made in Hamilton, Scotland on 31 Dec 2019, and LED is now replacing it, ferry decks included. You can see that change on Paolo Villa's 2020 Ancona–Patras deck shots, which are lit blue-white. The ferry night is also a legal oddity. Duty-free started at Shannon in 1947, was abolished on intra-EU routes in 1999, survived on Baltic routes because Åland sits outside the EU tax union, and came back to UK routes after Brexit. The Silja Line Tax Free catalogue for 1995–96 (Internet Archive) shows that economy at its peak, just before the 1999 cut.

**History with weight.** The two great ferry disasters shape the board's tone. The *Herald of Free Enterprise* capsized at Zeebrugge in 1987 with its bow doors open: 193 dead in about 90 seconds. Many passengers were on a cheap promotion run by The Sun, and Ferry Aid's "Let It Be" followed. The *Estonia* was the former *Viking Sally* of 1980, whose deck 5 held the tax-free shops, cafeteria, disco and 'air seats'. She sank on the night crossing of 28 Sep 1994, with 852 dead. Both are referenced, never aestheticised; that's a Do/Don't rule.

**Disciplines.**
- **Theatre:** Anna Viebrock's 'inventing what one finds'. Her waiting rooms, foyers and aircraft cabins, with dark panelling, linoleum and fluorescent tubes, are exactly the ferry cafeteria. I paired her with Rimini Protokoll's *Cargo Sofia*: an audience in a truck crossing border checkpoints, which is a model for an immersive activation.
- **Photography:** Rut Blees Luxemburg's ~10-minute sodium exposures of London (1996) and Sugimoto's Seascapes, with exposures up to 3 hours.
- **Painting:** Whistler's nocturne of Southampton Water and Grimshaw's gas-lit docks are the pre-electric ancestors.
- **Fashion:** Helly Hansen's 1877 linseed-oil oilskins, Osti's tarpaulin Tela Stella for Stone Island, and Heron Preston's DSNY uniforms all set the precedent for reworking crew kit.
- **Film:** *Drive My Car* has the red Saab crossing to Hokkaido by overnight ferry. *Three Colours: Red* ends with a lost Channel ferry. *Leviathan* and *The Forgotten Space* treat the ship as body and as logistics.
- **Sound:** "Sailing By" before the 00:48 Shipping Forecast; COLREGs whistle bands (70–200 Hz for ships 200 m and longer); Foulis's 'low notes carry further' diaphone; a real 1980 Sealink *St Nicholas* engine-room recording in BBC Sound Effects; and night-ferry field recordings on radio aporee.
- **Type:** Rail Alphabet (Kinneir Calvert, 1965) was literally Sealink's ship lettering until the late 1980s. Open stand-ins are rendered: Overpass for Highway Gothic, Barlow, IBM Plex Mono, B612 (the Airbus cockpit face), DotGothic16, VT323, Archivo Narrow and Noto Sans JP.

**Steering-message sources folded in.**
- **Internet Archive:** I pulled the Silja Line Tax Free 1995–96 catalogue (4 pages) and ffmpeg frames from two Sealink TV ads (British Rail/Clare Francis 1982 at 2s/12s/14s; Doubletake 1988 at 1s/17s). Neither item states rights, so I've marked both reference-only. I also used radio aporee recordings, which are CC BY-SA 3.0.
- **Are.na:** Low yield. Searches for 'ferry', 'sodium', 'maritime signage', 'ferry interior' and 'liminal transport' turned up thin or off-theme channels. 'Captured: Bay Ferry' is sunny San Francisco bay with gulls; 'Sodium Lamp' is Kowloon Walled City. I linked only Anton Krebs' 'duty free' non-places channel and downloaded nothing from Are.na.
- **BBC Sound Effects:** Their search API returned excellent archival ferry SFX, which I linked. These are under the RemArc licence (personal, educational and research use).
- **Freesound:** It blocks curl, so I found its pages via web search and linked them.
- **Fonts In Use:** Real ferry and maritime lettering cases, linked: Viking Line's customised Friz Quadrata, the SS France 1969 brochure, Landsbjörg ferry lettering, Circular Quay ferry wharves, the Staten Island Ferry terminal, and British Rail/Rail Alphabet.

**Colour.** Sampled in Python by running k-means over the pooled zone images, plus pixel medians for the small safety colours. The palette is Night Hull Black #100B0B (38%), Sodium Core #E4A10A, Sodium Burn #B35F0A, Rust Halo #583112, Wet Steel #6F665F, Formica Oatmeal #C0A889, LED Deck Blue #104B97, Hull White #E7E8E8, Lifebuoy Red #A72A21 and Night Ferry Yellow #BCBD17.

**Gaps and caveats.**
- No stills from copyrighted films or photographers (Rut Blees Luxemburg, Sugimoto, Hido). Those are links only.
- Japanese ferry interiors are daytime shots. I found no Commons tatami-room-at-night image.
- COLREG Rule 35 (fog-signal interval) is not verified. I only cite Annex III frequencies.
- Grimshaw's *Liverpool Quay by Moonlight* (Tate) failed with HTTP 429, so it's omitted.
- The Freesound 'C–A–F chime' detail comes from a user comment and is anecdotal.
- Internet Archive items without a stated licence are reference-only.

## Image sources (70)

- `images/light--ferry-light-trail-rostock.jpg` — Radomianin · CC BY-SA 4.0 · via Wikimedia Commons — https://commons.wikimedia.org/wiki/File:Ferry_light_trail,_Rostock.jpg
- `images/light--frederikshavn-from-ferry.jpg` — Leonhard Lenz · CC0 · via Wikimedia Commons — https://commons.wikimedia.org/wiki/File:Frederikshavn_harbor_at_night_seen_from_ferry_2022-08-17_03.jpg
- `images/light--helsinki-terminal-night.jpg` — Leonhard Lenz · CC0 · via Wikimedia Commons — https://commons.wikimedia.org/wiki/File:Makasiiniterminaali_Helsinki_at_night_2022-09-18_01.jpg
- `images/light--howth-late-walk.jpeg` — Giuseppe Milo · CC BY 3.0 · via Wikimedia Commons — https://commons.wikimedia.org/wiki/File:A_Late_Walk_Howth_Ireland_Color_Street_Photography_(199507437).jpeg
- `images/light--hps-bulb.jpg` — SAF1999 · CC BY 4.0 · via Wikimedia Commons — https://commons.wikimedia.org/wiki/File:Street_Lamp.jpg
- `images/light--lansiterminaali-night.jpg` — JIP · CC BY-SA 4.0 · via Wikimedia Commons — https://commons.wikimedia.org/wiki/File:View_towards_L%C3%A4nsiterminaali_at_night.jpg
- `images/light--lysekil-refinery-fog.jpg` — W.carter · CC0 · via Wikimedia Commons — https://commons.wikimedia.org/wiki/File:Preemraff_Lysekil_oil_refinery_on_a_foggy_night.jpg
- `images/light--night-deck-ancona-patras-1.jpg` — Paolo Villa · CC BY-SA 4.0 · via Wikimedia Commons — https://commons.wikimedia.org/wiki/File:02_2020_Grecia_photo_Paolo_Villa_FO199956_(traghetto_Ancona_Patrasso_-_sopraccoperta_di_notte_-_ferry_-_on_deck_in_the_nightferry).jpg
- `images/light--night-deck-ancona-patras-2.jpg` — Paolo Villa · CC BY-SA 4.0 · via Wikimedia Commons — https://commons.wikimedia.org/wiki/File:02_2020_Grecia_photo_Paolo_Villa_FO199953_(traghetto_Ancona_Patrasso_-_sopraccoperta_di_notte_-_ferry_-_on_deck_in_the_night).jpg
- `images/light--punta-de-piedras-night.jpg` — Wilfredor · CC0 · via Wikimedia Commons — https://commons.wikimedia.org/wiki/File:Ferry_docked_at_Punta_de_Piedras_terminal_at_night,_Margarita_Island,_Venezuela.jpg
- `images/light--rotterdam-port-night.jpg` — Steven Lek · CC BY-SA 4.0 · via Wikimedia Commons — https://commons.wikimedia.org/wiki/File:Port_of_Rotterdam_by_night_2014.JPG
- `images/light--snow-sodium-tuntorp.jpg` — W.carter · CC BY-SA 4.0 · via Wikimedia Commons — https://commons.wikimedia.org/wiki/File:Snow_under_a_street_lamp_in_Tuntorp_3.jpg
- `images/light--sodium-glow-milton-keynes.jpg` — John Chryslar · CC0 · via Wikimedia Commons — https://commons.wikimedia.org/wiki/File:Sodium_glow_in_Great_Holm_Milton_Keynes.jpg
- `images/light--stena-hss-holyhead.jpg` — Eric Jones · CC BY-SA 2.0 · via Wikimedia Commons — https://commons.wikimedia.org/wiki/File:The_Stena_HSS_idling_in_the_Inner_Harbour_-_geograph.org.uk_-_1457595.jpg
- `images/light--stena-scotia-belfast-night.jpg` — Albert Bridge · CC BY-SA 2.0 · via Wikimedia Commons — https://commons.wikimedia.org/wiki/File:The_%22Stena_Scotia%22_(night_view),_Albert_Quay,_Belfast_harbour_(September_2019)_-_geograph.org.uk_-_6256828.jpg
- `images/spaces--baie-de-seine-corridor.jpg` — Kolforn (Kolforn) · CC BY-SA 4.0 · via Wikimedia Commons — https://commons.wikimedia.org/wiki/File:2017-12-20_Cabin_corridor,_Baie_de_Seine.JPG
- `images/spaces--ferry-kyoto-corridor.jpg` — JeanGilbetCasanis · CC0 · via Wikimedia Commons — https://commons.wikimedia.org/wiki/File:FerryKyotoSuperiorCorridor.jpg
- `images/spaces--ferry-mishima-2nd-class.jpg` — Olegushka · CC0 · via Wikimedia Commons — https://commons.wikimedia.org/wiki/File:2cl_Ferrymishima_20170318.jpg
- `images/spaces--finnjet-buffet.jpg` — No machine-readable author provided. Kjet assumed (based on  · CC BY-SA 2.5 · via Wikimedia Commons — https://commons.wikimedia.org/wiki/File:Finnjet_Buffet_Entrance.jpg
- `images/spaces--hankyu-ferry-2nd-class.jpg` — Kuruman from Tokyo, Japan · CC BY 2.0 · via Wikimedia Commons — https://commons.wikimedia.org/wiki/File:%E9%98%AA%E4%B9%9D%E3%83%95%E3%82%A7%E3%83%AA%E3%83%BC_%E4%BA%8C%E7%AD%89%E8%88%B9%E5%AE%A4_(8704112779).jpg
- `images/spaces--isle-of-arran-interior.jpg` — Cameron Shaw · CC BY-SA 4.0 · via Wikimedia Commons — https://commons.wikimedia.org/wiki/File:Isle_of_Arran_interior.jpg
- `images/spaces--mont-st-michel-blue-note-bar.jpg` — Andy Li · CC0 · via Wikimedia Commons — https://commons.wikimedia.org/wiki/File:Blue_Note_Bar_on_Deck_9_-_MV_Mont_St_Michel_2025-03-30.jpg
- `images/spaces--mont-st-michel-self-service.jpg` — Andy Li · CC0 · via Wikimedia Commons — https://commons.wikimedia.org/wiki/File:La_Galerie_self-service_restaurant_on_Deck_8_-_MV_Mont_St_Michel_2025-03-30.jpg
- `images/spaces--new-taima-info-desk.jpg` — Shangkuanlc · CC BY-SA 4.0 · via Wikimedia Commons — https://commons.wikimedia.org/wiki/File:Information_desk_of_New_Taima_ferry_(between_Matsu_and_Taiwan)_01.jpg
- `images/spaces--ocean-tokyu-interior.jpg` — ジョンドウ · CC BY-SA 4.0 · via Wikimedia Commons — https://commons.wikimedia.org/wiki/File:%E3%82%AA%E3%83%BC%E3%82%B7%E3%83%A3%E3%83%B3%E6%9D%B1%E4%B9%9D%E3%83%95%E3%82%A7%E3%83%AA%E3%83%BC%E8%88%B9%E5%86%85.jpg
- `images/spaces--silja-festival-cabin.jpg` — Sergey Ashmarin · CC BY-SA 3.0 · via Wikimedia Commons — https://commons.wikimedia.org/wiki/File:%27Silja_Festival%27_cabin_interior_-_panoramio.jpg
- `images/spaces--silja-galaxy-06.jpg` — AleWi · CC BY-SA 4.0 · via Wikimedia Commons — https://commons.wikimedia.org/wiki/File:Silja_Line_Galaxy_201907-_06.jpg
- `images/spaces--silja-galaxy-07.jpg` — AleWi · CC BY-SA 4.0 · via Wikimedia Commons — https://commons.wikimedia.org/wiki/File:Silja_Line_Galaxy_201907-_07.jpg
- `images/spaces--stena-danica-33.jpg` — AleWi · CC BY-SA 4.0 · via Wikimedia Commons — https://commons.wikimedia.org/wiki/File:Interi%C3%B6r,_Stena_Danica,_20230410,_pic_33.jpg
- `images/spaces--stena-danica-cafe.jpg` — AleWi · CC BY-SA 4.0 · via Wikimedia Commons — https://commons.wikimedia.org/wiki/File:Interi%C3%B6r,_Stena_Danica,_cafe,_taste,_20230410,_pic_01.jpg
- `images/spaces--sunflower-gold-restaurant.jpg` — Olegushka · CC0 · via Wikimedia Commons — https://commons.wikimedia.org/wiki/File:Restaurant_SunflowerGold_20071215.jpg
- `images/spaces--sunflower-sapporo-promenade.jpg` — Totti · CC BY-SA 4.0 · via Wikimedia Commons — https://commons.wikimedia.org/wiki/File:Sunflower_Sapporo_promenade.jpg
- `images/spaces--tallink-mystar-lounge.jpg` — Tony Webster · CC BY 2.0 · via Wikimedia Commons — https://commons.wikimedia.org/wiki/File:Business_Lounge_on_Tallink_MyStar_Ferry_from_Helsinki_to_Tallinn_(53928790508).jpg
- `images/spatial--assembly-station-sign.jpg` — Dominic Nelson · CC BY-SA 4.0 · via Wikimedia Commons — https://commons.wikimedia.org/wiki/File:MV_St._Francis_Xavier_-_assembly_station_No.1_-_Oct_2024.jpg
- `images/spatial--bergama-engine-room.jpg` — Koray · CC BY-SA 4.0 · via Wikimedia Commons — https://commons.wikimedia.org/wiki/File:Engine_room_of_Bergama_ferry_10.jpg
- `images/spatial--corran-car-deck.jpg` — Richard Webb · CC BY-SA 2.0 · via Wikimedia Commons — https://commons.wikimedia.org/wiki/File:Car_deck,_Corran_Ferry_-_geograph.org.uk_-_8018879.jpg
- `images/spatial--lifebuoy-floodlight.jpg` — Jules Verne Times Two · CC BY-SA 4.0 · via Wikimedia Commons — https://commons.wikimedia.org/wiki/File:Red_lifebuoy_and_floodlight_on_white_railing,_Blue_Star_Myconos_ship,_Icarian_Sea,_Greece_julesvernex2.jpg
- `images/spatial--night-ferry-signs.jpg` — Reinhard Dietrich · Public domain · via Wikimedia Commons — https://commons.wikimedia.org/wiki/File:Night_ferry_Hinweisschilder.JPG
- `images/spatial--norsky-car-deck.jpg` — Mick Garratt · CC BY-SA 2.0 · via Wikimedia Commons — https://commons.wikimedia.org/wiki/File:The_Car_Deck_of_the_M-V_Norsky_-_geograph.org.uk_-_1453148.jpg
- `images/spatial--roro-ramp-hoegh-osaka.jpg` — Peter Facey · CC BY-SA 2.0 · via Wikimedia Commons — https://commons.wikimedia.org/wiki/File:Ro-Ro_ramp_of_the_Hoegh_Osaka,_at_berth_101_(geograph_4322699).jpg
- `images/spatial--lashing-bollard.jpg` — W.carter · CC BY-SA 4.0 · via Wikimedia Commons — https://commons.wikimedia.org/wiki/File:Lashing_on_bollard_on_the_ship_Gunnar_Thorson.jpg
- `images/history--townsend-thoresen-badge.jpg` — Kolforn (Kolforn) · CC BY-SA 4.0 · via Wikimedia Commons — https://commons.wikimedia.org/wiki/File:-2019-12-06_Townsend_Thoresen_car_ferries_enamel_badge.JPG
- `images/history--sealink-ticket-1986.jpg` — Eweht · CC BY-SA 4.0 · via Wikimedia Commons — https://commons.wikimedia.org/wiki/File:Dunlaoghaire_-_Sealink-F%C3%A4hrschiff-Einzelfahrschein_Fahrrad_-_August_1986.jpg
- `images/wardrobe--crew-safety-gear-ramp.jpg` — Ssemmanda will · CC BY-SA 4.0 · via Wikimedia Commons — https://commons.wikimedia.org/wiki/File:Ferry_Docked_at_Ramp_with_Vehicles_Boarding_and_Crew_in_Safety_Gear..jpg
- `images/wardrobe--hine-stevedores-1912.jpg` — Lewis Hine · Public domain · via Wikimedia Commons — https://commons.wikimedia.org/wiki/File:Stevedores_ny_1912.jpg
- `images/wardrobe--star-ferry-crew-billhook.jpg` — Daniel Case · CC BY-SA 3.0 · via Wikimedia Commons — https://commons.wikimedia.org/wiki/File:Star_Ferry_crew_using_billhook_to_catch_rope_at_Central_ferry_pier,_Hong_Kong.jpg
- `images/film--sealink-1982-advert-t2s.jpg` — British Rail / Sealink, 1982 · Internet Archive (rights not stated; reference only) — https://archive.org/details/british-rail-sealink-claire-francis
- `images/film--sealink-1982-advert-t12s.jpg` — British Rail / Sealink, 1982 · Internet Archive (rights not stated; reference only) — https://archive.org/details/british-rail-sealink-claire-francis
- `images/film--sealink-1982-advert-t14s.jpg` — British Rail / Sealink, 1982 · Internet Archive (rights not stated; reference only) — https://archive.org/details/british-rail-sealink-claire-francis
- `images/film--sealink-doubletake-1988-t1s.jpg` — Sealink British Ferries, 1988 · Internet Archive (rights not stated; reference only) — https://archive.org/details/SealinkDoubletakeAdvert
- `images/film--sealink-doubletake-1988-t17s.jpg` — Sealink British Ferries, 1988 · Internet Archive (rights not stated; reference only) — https://archive.org/details/SealinkDoubletakeAdvert
- `images/spaces--smallwood-cafeteria.jpg` — André Carrotflower · CC BY-SA 2.0 · via Wikimedia Commons — https://commons.wikimedia.org/wiki/File:TV-009-0416_(15052525776).jpg
- `images/spaces--fanafjord-vending.jpg` — Wolfmann · CC BY-SA 4.0 · via Wikimedia Commons — https://commons.wikimedia.org/wiki/File:Ferdamat_snacks_and_coffee_vending_machines_in_Fanafjord_ferry,_Hordaland,_Norway,_2018-03-05_IMG_5587.jpg
- `images/light--belmont-waiting-room-night.jpg` — Mike Pennington · CC BY-SA 2.0 · via Wikimedia Commons — https://commons.wikimedia.org/wiki/File:Waiting_room_at_Belmont_ferry_terminal_at_night_-_geograph.org.uk_-_2626996.jpg
- `images/art--grimshaw-liverpool-docks-night.jpg` — John Atkinson Grimshaw · Public domain · via Wikimedia Commons — https://commons.wikimedia.org/wiki/File:John_Atkinson_Grimshaw_(1836-1893)_-_Liverpool_Docks_by_Night_-_WAG_10328_-_Walker_Art_Gallery.jpg
- `images/art--turner-snow-storm.jpg` — J. M. W. Turner · Public domain · via Wikimedia Commons — https://commons.wikimedia.org/wiki/File:J.M.W._Turner_%E2%80%93_Snow_Storm_-_Steam-Boat_off_a_Harbour%27s_Mouth.jpg
- `images/art--whistler-southampton-water.jpg` — James McNeill Whistler · Public domain · via Wikimedia Commons — https://commons.wikimedia.org/wiki/File:James_McNeill_Whistler_-_Nocturne,_Blue_and_Gold%E2%80%94Southampton_Water_-_1900.52_-_Art_Institute_of_Chicago.jpg
- `images/history--finnjet-travemunde-1987.jpg` — Wolfgang Fricke · CC BY 3.0 · via Wikimedia Commons — https://commons.wikimedia.org/wiki/File:Finnjet_IMO_7359632_F_Travem%C3%BCnde_1987.jpg
- `images/history--herald-of-free-enterprise-1984.jpg` — Franz Golhen · Public domain · via Wikimedia Commons — https://commons.wikimedia.org/wiki/File:Herald_of_Free_Enterprise.jpg
- `images/history--holyhead-ferry-1-1975.jpg` — Albert Bridge · CC BY-SA 2.0 · via Wikimedia Commons — https://commons.wikimedia.org/wiki/File:The_%22Holyhead_Ferry_1%22_at_Dun_Laoghaire_-_geograph.org.uk_-_2307693.jpg
- `images/history--ionic-ferry-larne-1986.jpg` — Albert Bridge · CC BY-SA 2.0 · via Wikimedia Commons — https://commons.wikimedia.org/wiki/File:The_%22Ionic_Ferry%22_at_Larne_-_geograph.org.uk_-_570793.jpg
- `images/history--new-akashia-2004.jpg` — NKNS · CC BY-SA 3.0 · via Wikimedia Commons — https://commons.wikimedia.org/wiki/File:Shin_Nihonkai_Ferry_New_Akashia.jpg
- `images/history--sealink-folkestone-1979.jpg` — David Dixon · CC BY-SA 2.0 · via Wikimedia Commons — https://commons.wikimedia.org/wiki/File:Sealink_Ferry_at_Folkestone_Harbour_Pier,_1979_-_geograph.org.uk_-_4409068.jpg
- `images/history--st-brendan-fishguard-1987.jpg` — Andreas F. Borchert · CC BY-SA 4.0 · via Wikimedia Commons — https://commons.wikimedia.org/wiki/File:Fishguard_Ferry_St._Brendan_of_Sealink_1987_08_13.jpg
- `images/history--townsend-thoresen-1981.jpg` — Peter Jeffery · CC BY-SA 2.0 · via Wikimedia Commons — https://commons.wikimedia.org/wiki/File:A_Townsend_Thoresen_Ferry_Leaves_Port_-_geograph.org.uk_-_5283604.jpg
- `images/history--viking-sally-1980.jpg` — Bo Palmqvist · CC BY-SA 4.0 · via Wikimedia Commons — https://commons.wikimedia.org/wiki/File:Viking_Sally_001.jpg
- `images/history--silja-taxfree-catalog-1995-p0.jpg` — Silja Line, 1995 · Internet Archive scan (rights not stated; reference only) — https://archive.org/details/silja-line-tax-free-1995-1996/page/n0
- `images/history--silja-taxfree-catalog-1995-p10.jpg` — Silja Line, 1995 · Internet Archive scan (rights not stated; reference only) — https://archive.org/details/silja-line-tax-free-1995-1996/page/n10
- `images/history--silja-taxfree-catalog-1995-p40.jpg` — Silja Line, 1995 · Internet Archive scan (rights not stated; reference only) — https://archive.org/details/silja-line-tax-free-1995-1996/page/n40
- `images/history--silja-taxfree-catalog-1995-p60.jpg` — Silja Line, 1995 · Internet Archive scan (rights not stated; reference only) — https://archive.org/details/silja-line-tax-free-1995-1996/page/n60

## Text, link, sound and type sources

- [Thesis] Why sodium — https://en.wikipedia.org/wiki/Sodium-vapor_lamp
- [Thesis] Why 'between two countries' — https://en.wikipedia.org/wiki/Duty-free_shop
- [Typography] Rail Alphabet / New Rail Alphabet / Rail Alphabet 2 — commercial (A2-TYPE) — https://www.a2-type.co.uk/new-rail-alphabet
- [Typography] Transport / New Transport — commercial (A2-TYPE) — https://www.a2-type.co.uk/new-transport
- [Typography] DIN 1451 — commercial (Linotype) — https://www.myfonts.com/collections/din-1451-font-linotype
- [Typography] Frutiger — commercial (Linotype) — https://www.myfonts.com/collections/frutiger-font-linotype
- [Typography] Tratex — Swedish road-sign face (Karl-Gustaf Gustafsson) — https://en.wikipedia.org/wiki/Tratex
- [Typography] Fonts In Use: British Rail identity and signs 1965–1990s (Rail Alphabet) — https://fontsinuse.com/uses/62451/british-rail-identity-and-signs-1965-1990s
- [Typography] Fonts In Use: Viking Line bus-stop ads, Stockholm 2004 — https://fontsinuse.com/uses/167/viking-line-bus-stop-ads
- [Typography] Fonts In Use: SS France 'Croisière de Europe' brochure, 1969 — https://fontsinuse.com/uses/14200/ss-france-croisiere-de-europe-1969
- [Typography] Fonts In Use: Slysavarnafélagið Landsbjörg ferry lettering, Reykjavík — https://fontsinuse.com/uses/195/slysavarnafelagid-landsbjorg
- [Typography] Fonts In Use: NSW transport signs incl. Circular Quay Ferry Wharves — https://fontsinuse.com/uses/22183/nsw-transport-signs
- [Typography] Fonts In Use: Staten Island Ferry Whitehall Terminal — https://fontsinuse.com/uses/1776/staten-island-ferry-whitehall-terminal
- [Fashion & Wardrobe] Helly Hansen — oilskins since 1877 — https://www.hellyhansen.com/about-us/heritage
- [Fashion & Wardrobe] Stone Island — Tela Stella, 1982 — https://www.monclergroup.com/en/brands/stone-island/history
- [Fashion & Wardrobe] Heron Preston — UNIFORM for DSNY (2016) — https://heronpreston.com/pages/led_upcycled/dsny
- [Fashion & Wardrobe] Craig Green — workwear and uniform, reworked — http://craig-green.com/
- [Film & Moving Image] Drive My Car (Ryusuke Hamaguchi, 2021) — https://en.wikipedia.org/wiki/Drive_My_Car_(film)
- [Film & Moving Image] Three Colours: Red (Kieślowski, 1994) — https://www.criterion.com/current/posts/2064-red-a-fraternity-of-strangers
- [Film & Moving Image] Leviathan (Castaing-Taylor & Paravel, 2012) — https://en.wikipedia.org/wiki/Leviathan_(2012_film)
- [Film & Moving Image] The Forgotten Space (Allan Sekula & Noël Burch, 2010) — https://www.theforgottenspace.net/static/info.html
- [Film & Moving Image] Songs from the Second Floor (Roy Andersson, 2000) — https://en.wikipedia.org/wiki/Songs_from_the_Second_Floor
- [Film & Moving Image] The Other Side of Hope (Aki Kaurismäki, 2017) — https://en.wikipedia.org/wiki/The_Other_Side_of_Hope
- [Film & Moving Image] Fallen Angels (Wong Kar-wai, 1995) — https://en.wikipedia.org/wiki/Fallen_Angels_(1995_film)
- [Film & Moving Image] Under the Skin (Jonathan Glazer, 2013) — https://en.wikipedia.org/wiki/Under_the_Skin_(2013_film)
- [Film & Moving Image] Ferry Tales (Katja Esson, 2003) — https://en.wikipedia.org/wiki/Ferry_Tales
- [Theatre & Set Design] Anna Viebrock — 'inventing what one finds' — https://www.spiegel.de/kultur/gesellschaft/die-buehnenbilder-der-anna-viebrock-ranzige-treppe-ins-nichts-a-778001.html
- [Theatre & Set Design] Christoph Marthaler — https://en.wikipedia.org/wiki/Christoph_Marthaler
- [Theatre & Set Design] Rimini Protokoll — Cargo Sofia (Stefan Kaegi) — https://www.rimini-protokoll.de/website/en/project/cargo-sofia-x
- [Fine Art & Photography] Rut Blees Luxemburg — London: A Modern Project (1996) — https://rutbleesluxemburg.com/london%20-%20a%20modern%20project
- [Fine Art & Photography] Hiroshi Sugimoto — Seascapes (from 1980) — https://en.wikipedia.org/wiki/Hiroshi_Sugimoto
- [Fine Art & Photography] Allan Sekula — Fish Story — https://en.wikipedia.org/wiki/Allan_Sekula
- [Fine Art & Photography] Todd Hido — houses at night — https://en.wikipedia.org/wiki/Todd_Hido
- [Fine Art & Photography] Edward Hopper — https://en.wikipedia.org/wiki/Edward_Hopper
- [Fine Art & Photography] Vilhelm Hammershøi — https://en.wikipedia.org/wiki/Vilhelm_Hammersh%C3%B8i
- [Fine Art & Photography] Bernd and Hilla Becher — https://en.wikipedia.org/wiki/Bernd_and_Hilla_Becher
- [Fine Art & Photography] Are.na: 'duty free' channel (Anton Krebs) — https://www.are.na/anton-krebs/duty-free-7aaq1ji4qxy
- [Sound & Music] Sailing By — Ronald Binge (1963) — https://en.wikipedia.org/wiki/Sailing_By
- [Sound & Music] Shipping Forecast (00:48) — BBC Radio 4 / Met Office — https://en.wikipedia.org/wiki/Shipping_Forecast
- [Sound & Music] Ambient 1: Music for Airports — Brian Eno (1979) — https://en.wikipedia.org/wiki/Ambient_1:_Music_for_Airports
- [Sound & Music] The Sinking of the Titanic — Gavin Bryars (1969/1975) — https://en.wikipedia.org/wiki/The_Sinking_of_the_Titanic_(composition)
- [Sound & Music] Substrata — Biosphere (1997) — https://en.wikipedia.org/wiki/Substrata_(album)
- [Sound & Music] An Empty Bliss Beyond This World — The Caretaker (2011) — https://en.wikipedia.org/wiki/An_Empty_Bliss_Beyond_This_World
- [Sound & Music] Music for Nine Post Cards — Hiroshi Yoshimura (1982) — https://en.wikipedia.org/wiki/Music_for_Nine_Post_Cards
- [Sound & Music] Still Way — Satoshi Ashikawa (1982) — https://en.wikipedia.org/wiki/Satoshi_Ashikawa
- [Sound & Music] Different Trains — Steve Reich (1988) — https://en.wikipedia.org/wiki/Different_Trains
- [Sound & Music] Untrue — Burial (2007) — https://en.wikipedia.org/wiki/Untrue_(album)
- [Sound & Music] Pop — Gas (2000) — https://en.wikipedia.org/wiki/Pop_(Gas_album)
- [Sound & Music] The Disintegration Loops — William Basinski (2001) — https://en.wikipedia.org/wiki/The_Disintegration_Loops
- [Sound & Music] Maritime Rites — Alvin Curran (1984 NPR; reissue 2004) — https://en.wikipedia.org/wiki/Alvin_Curran
- [Sound & Music] Let It Be — Ferry Aid (1987) — https://en.wikipedia.org/wiki/Ferry_Aid
- [Sound & Music] Dansband — Swedish dance-band genre — https://en.wikipedia.org/wiki/Dansband
- [Sound & Music] Motif: the whistle — https://www.ecfr.gov/current/title-33/chapter-I/subchapter-E/part-86/section-86.01
- [Sound & Music] Motif: the diaphone — https://en.wikipedia.org/wiki/Foghorn
- [Sound & Music] Motif: the PA chime — https://freesound.org/people/theblockofsound235/sounds/350948/
- [Sound & Music] BBC Sound Effects 07043043 — Car Ferry engine room (Sealink 'St. Nicholas', 17,400 t, buil — https://sound-effects.bbcrewind.co.uk/07043043
- [Sound & Music] BBC Sound Effects 07018067 — Cross-Channel car ferry, wind & rough sea — https://sound-effects.bbcrewind.co.uk/07018067
- [Sound & Music] BBC Sound Effects 07018114 — Southampton foghorn, two blasts — https://sound-effects.bbcrewind.co.uk/07018114
- [Sound & Music] BBC Sound Effects 07014011 — Cars driving off ferry ramp — https://sound-effects.bbcrewind.co.uk/07014011
- [Sound & Music] Freesound — Ferry Announcement 080621 (LG) — https://freesound.org/people/LG/sounds/55501/
- [Sound & Music] Freesound — 170722_MediumFerry_BelowDeck (blaukreuz) — https://freesound.org/people/blaukreuz/sounds/398851/
- [Sound & Music] radio aporee — 'baltic sea, night ferry, ventilation shaft on deck' (Dirk Raulf) — https://archive.org/details/aporee_2557_3549
- [Sound & Music] radio aporee — 'ferry, cardeck' (Dirk Raulf) — https://archive.org/details/aporee_2545_3535
- [Sound & Music] radio aporee — 'Stena Line, North Sea - cabin walk' (Sophie Standford) — https://archive.org/details/aporee_58144_66667
- [Historical & Cultural Referents] Night Ferry, 1936–1980 — https://en.wikipedia.org/wiki/Night_Ferry
- [Historical & Cultural Referents] Sealink, 1970–1984 — https://en.wikipedia.org/wiki/Sealink
- [Historical & Cultural Referents] MS Herald of Free Enterprise / Zeebrugge, 1987 — https://en.wikipedia.org/wiki/MS_Herald_of_Free_Enterprise
- [Historical & Cultural Referents] MS Estonia, 1994 — https://en.wikipedia.org/wiki/MS_Estonia
- [Historical & Cultural Referents] GTS Finnjet (1977–2008) — https://en.wikipedia.org/wiki/GTS_Finnjet
- [Historical & Cultural Referents] Silja Serenade (1990) — https://en.wikipedia.org/wiki/MS_Silja_Serenade
- [Historical & Cultural Referents] Hankyu Ferry — Japan's first long-distance car-ferry operator — https://en.wikipedia.org/wiki/Hankyu_Ferry
- [Historical & Cultural Referents] Rail Alphabet — https://en.wikipedia.org/wiki/Rail_Alphabet
- [Historical & Cultural Referents] Internet Archive — Silja Line Tax Free 1995–96 catalogue (full scan) — https://archive.org/details/silja-line-tax-free-1995-1996
- Additional sources read: https://sodane.hokkaido.jp/column/202205140600002117.html ; https://www.soft99.co.jp/matei_carlife/episode6/ ; https://en.wikipedia.org/wiki/Three_Colours:_Red ; https://www.legislation.gov.uk/uksi/1989/1798/schedule/part/8/paragraph/1/made ; http://www.dreamideamachine.com/?p=99662 ; https://www.theguardian.com/artanddesign/2009/apr/23/rut-blees-luxemburg-best-shot-photography ; https://www.tate.org.uk/whats-on/tate-liverpool/project-space-rut-blees-luxemburg ; https://nbl.snl.no/Helly_J._Hansen ; https://www.propermag.com/?p=110886 ; https://www.wallpaper.com/fashion-beauty/craig-green-interview-2025 ; https://fontsinuse.com/typefaces/129940/rail-alphabet ; https://sound-effects.bbcrewind.co.uk/licensing ; https://raw.githubusercontent.com/google/fonts/main/ofl/*/DESCRIPTION.en_us.html (font descriptions)
