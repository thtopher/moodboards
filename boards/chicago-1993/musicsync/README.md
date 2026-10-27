# musicsync

This pipeline cuts video to music. It works on any audio, including live recordings that drift in tempo, because it never assumes a fixed BPM. Every time it uses is a detected time.

```
setup.sh                      # one-time: .venv (Beat This!, Demucs) + .venv-mm (madmom, Python 3.11)
beats.py   AUDIO beats.json [--override ovr.json]
moments.py AUDIO beats.json moments.json
cutlist.py beats.json moments.json cutlist.json [--config cfg.json]
splice.py  SOURCE source_beats.json "3-15,19-29,32-38" edit.wav splices.json   # optional music edit
mux.py     VIDEO MUSIC.wav OUT.mp4                                            # the only audio path
check_render.py OUT.mp4 cutlist.json MUSIC.wav --lead L [--splices splices.json] [--panels 0:952,968:1920]
```

## Stages

- **Beats (`beats.py`)**
  - Beat This! runs on the mix and on the Demucs drum stem to get the pulses. Gaps are filled and each pulse is refined to the nearest onset within ±25 ms.
  - Bar length is cross-checked with madmom's DBN at 2, 3, 4 and 6 beats per bar.
  - Downbeat phase is chosen by dynamic programming over the evidence: Beat This mix/drums, the madmom activation, kick and snare hits on the drum stem, and the hypothesis votes. An irregular bar is allowed but penalized.
  - Each downbeat gets a confidence score. The output also lists irregular bars (by duration) and pulse glitches.
  - An override file can shift, add or remove downbeats, or force the bar length. Use it on live recordings when the tracker loses its place.
- **Moments (`moments.py`)**
  - Every downbeat is scored, with these ranks:
    - **top:** drums in, drums out, drop, break, release, vocal in;
    - **high:** fill landing, section change;
    - **med:** change.
  - Signals are per-bar loudness of the mix and stems, drum presence, drum energy in the last third of the previous bar, and Foote self-similarity novelty on chroma and MFCC. Novelty peaks are snapped to the nearest downbeat.
  - Each bar also gets an energy level: sparse, groove, break, peak or release.
- **Cut list (`cutlist.py`)**
  - Top and high moments are mandatory cuts.
  - Between them the base rate applies: sparse 4 bars, groove 2, break 1, peak 1, and release holds to the end. A span is split into the fewest whole-bar shots, and among equal splits the one with the highest moment scores wins.
  - Minimum shot length is 1 bar.
  - Frames are emitted per lead: `frame = round(t*fps) - lead`.
  - The half-bar snare exception is evaluated every time but applied only with `half_bar: true`, and only where the mid-bar snare clearly beats the downbeat.
- **Music edit (`splice.py`)**
  - Splices are whole bars only, on detected downbeats. Each side is cut 12 ms before the downbeat transient and joined with a 10 ms equal-power crossfade.
  - The only level change is a static gain to −15 LUFS (true peak ≤ −1.5 dB).
- **Audio:** `mux.py` maps the music track only, as AAC with no filters. There is no clip-audio path. Level the music upstream.
- **Check (`check_render.py`, non-circular)**
  - Downbeats and moments are re-detected from the rendered MP4's own audio.
  - Cuts are detected from the pixels of each panel. They must match the plan and be in lockstep across panels.
  - **FAIL if:**
    - a cut is more than 1 frame (after lead) from a re-detected downbeat or ranked moment;
    - a splice is more than 1 frame off a downbeat;
    - any bar is irregular;
    - the low end dips at a splice more than in the source plus 3 dB;
    - the output audio differs from the music track. This means: more than one audio stream, lag beyond ±1 sample, gain off by more than 0.5 dB, null residual above −20 dB overall or above −12 dB in any 1 s window, or a length difference over 1 frame.
