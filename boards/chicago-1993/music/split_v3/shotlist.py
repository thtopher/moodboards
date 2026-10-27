"""Shot list markdown for v3. Usage: python shotlist.py LEAD CHECK_JSON OUT.md CHECK_TXT"""
import json,sys
sys.path.insert(0,'.')
from grammar import RULES,frames,FPS
lead=int(sys.argv[1]); CK=json.load(open(sys.argv[2])); OUT=sys.argv[3]
e=json.load(open('edl_v3.json')); FR,END=frames(lead); Sp=json.load(open('sync/splices.json')); B=json.load(open('sync/edit_beats.json'))
cuts={r['shot']:r for r in CK['cuts']}
def tc(f): s=f/FPS; return f"{int(s//60)}:{s%60:05.2f}"
L=["# Chicago 1993: music split v3 shot list","",
f"`music_split_v3.mp4` (lead {lead}): 1920x1080, 24 fps, {END} frames ({END/FPS:.2f} s). Left panel Chicago, right panel the counter-world (steel), 16 px gutter.",
f"Audio: `music_edit_v3.wav` only, no clip audio (AAC 256k, static gain {Sp['gain_db']:+.2f} dB to {Sp.get('measured_lufs',0)+Sp['gain_db']:.1f} LUFS, no loudnorm).",
f"Music: `lyria_opt1.mp3`, 6/8 at 180 eighths/min (2.0 s bars), {B['bar_pulses']} pulses per bar, {len(B['downbeats'])} detected downbeats.","",
"## Arc","",e['arc'],"",
"## How the cuts are made (musicsync)","",
"- **Beats:** Beat This! on the mix and on the Demucs drum stem, cross-checked with madmom's DBN at 2/3/4/6 beats per bar; ties broken on the drum-stem kick and snare. Real downbeat times are stored; there is no fixed BPM.",
"- **Moments:** each downbeat is scored for drums in or out, drop, break, release, fill landing (drum-stem energy in the last third of the previous bar) and section change (self-similarity novelty snapped to the downbeat).",
"- **Cut list:** every top and high moment is a cut. Between anchors the base rate applies: sparse 4 bars, groove 2, break 1, peak 1, release holds. Both panels share one list.",
f"- **Lead:** frame = round(t × 24) − {lead}.",
"- **Music edit:** whole-bar splices on source downbeats: source bars 4–15 + 20–29 + 33–38, cut just before the downbeat transient with a 10 ms equal-power crossfade. Joints fall at " + ", ".join(f"{j:.2f} s" for j in Sp['joints_edit_t'])+".","",
"## Shots","","| # | Time | Frames | Bars | Energy | Moment hit | Offset vs re-detected downbeat | Chicago (left) | Counter-world (right) | Rule | Link |","|---|---|---|---|---|---|---|---|---|---|---|"]
for i,p in enumerate(e['pairs']):
    a,b=e['chi'][i],e['ctr'][i]; f0,f1=FR[i]
    def desc(c,beat):
        s=f"`{c['clip']}` @ {c['src_in']:.2f} s"
        if abs(c.get('speed',1)-1)>1e-3: s+=f" ×{c['speed']}"
        if c.get('freeze'): s+=f" (holds at {c['freeze']} s)"
        return s+f"<br>{beat}"
    hit=', '.join(h.replace('_',' ') for h in p['hits']); why=p['why'].replace('|','/')
    off=f"{cuts[i]['offset_ms']:+.1f} ms" if i in cuts else "start"
    L.append(f"| {i+1} | {tc(f0)}–{tc(f1)} | {f0}–{f1} | {p['bars']} | {p['energy']} | **{hit}**<br><sub>{why}</sub> | {off} | {desc(a,p['chi_beat'])} | {desc(b,p['ctr_beat'])} | {p['rule_name']} | {p['link']} |")
L+=["","## Lead variants","",
"All three variants pass the check. The cuts are identical; only the cut frame moves.",
"- **lead 0:** each cut is rounded to the nearest frame, which lands it between 20 ms before and 21 ms after the downbeat. Nine of the 20 cuts fall after the hit, so the picture arrives late.",
"- **lead 1 (picked):** every cut falls 21–62 ms before the re-detected downbeat (median about 46 ms). None is late, and all sit inside the window where video leading the beat still reads as in sync. The kick and snare attacks come about 12 ms before the tracked downbeat, so the cut is on screen when the hit lands.",
"- **lead 2:** cuts fall 63–103 ms early. That is visibly ahead of the beat in the 2-bar groove shots.",
"Alternates: `music_split_v3_alt_lead0_480p.mp4` and `music_split_v3_alt_lead2_480p.mp4`.",
"","## Check output (`musicsync/check_render.py`)","","```",open(sys.argv[4]).read().strip() if len(sys.argv)>4 else '',"```",""]
open(OUT,'w').write("\n".join(L))
