# Sky ↔ Sheen: full-song split screen (v1)

- `sky_sheen_full_v1_720p.mp4`: the pick (lead 1), 720p web copy. Sky on the left, Sheen on the right, every cut on a detected downbeat, both panels in lockstep, music only.
- `sky_sheen_full_v1_alt_lead0_480p.mp4`, `sky_sheen_full_v1_alt_lead2_480p.mp4`: the same edit with the cut frame 0 or 2 frames ahead of the downbeat.
- `sky_sheen_full_v1_shotlist.md`: time, bar, moment hit, offset and link rule for every shot, plus the check output.
- `sky_sheen_full_v1_contact.jpg`: one frame per shot. `sky_sheen_full_v1_overlay.png`: the cuts on the grid re-detected from the render's own audio.
- `song.mp3`: the song (192k mp3; the 93 MB WAV is not in the repo).
- `v1/`: EDL, scripts, the musicsync sync files (beats with the reviewed override, moments, cut list) and the check results for all three leads.
- `musicsync/`: updated `beats.py` (`move` and `regions` overrides), `check_render.py` (`--override`) and README.
