import json,sys
sys.path.insert(0,'.')
from grammar import RULES
e=json.load(open('edl_v2.json'));fps=e['fps']
chi={c['f0']:c for c in e['chi']};ctr={c['f0']:c for c in e['ctr']}
def tc(f): s=f/fps; return f"{int(s//60)}:{s%60:05.2f}"
L=["# Chicago 1993: music split v2 shot list","",
"`music_split_v2.mp4`: 1920x1080, 24 fps, 1428 frames (59.50 s). Left panel is Chicago, right panel is the counter-world (steel), with a 16 px gutter. Track: `lyria_opt1.mp3` (edited), 92.3 BPM, 22 bars.","",
"## Arc","",e['arc'],"",
"## Cut rules","",
"- Every cut lands on a bar downbeat, using frame indices taken from the librosa downbeat grid at 24 fps. Both panels cut on the same frame.",
"- Energy comes from bars per shot: sparse (bars 1–4) 4 bars, groove (5–12) 2 bars, break (13) 1 bar, peak (14–21) 1 bar, release (22) runs to the end.",
"- `gen_edl.py` declares pairs by bar index and asserts they tile the bars at the section rate. `render_v2.py` re-derives frames from the bar indices and refuses to render on any mismatch. `check_edl.py` re-verifies the EDL and the rendered file.","",
"## Pairing grammar","","Every simultaneous pair must pass one of these rules, each checked by machine against motion measured from the footage (optical flow, luma, warmth), not against catalog tags alone.","",
"| Rule | Name | Shape | Used at bars |","|---|---|---|---|"]
for k,r in RULES.items():
    bars=[str(p['bar']+1) for p in e['pairs'] if p['rule']==k]
    L.append(f"| `{k}` | {r['name']} | {r['shape']} | {', '.join(bars) or '(not used in v2)'} |")
L+=["","## Shots","","| # | Time | Bar(s) | Frames | Section | Chicago (left) | Counter-world (right) | Rule | Link | Evidence |","|---|---|---|---|---|---|---|---|---|---|"]
for i,p in enumerate(e['pairs'],1):
    a,b=chi[p['f0']],ctr[p['f0']]
    def desc(c,beat):
        s=f"`{c['clip']}` @ {c['src_in']:.2f} s"
        if abs(c.get('speed',1)-1)>1e-3: s+=f" ×{c['speed']}"
        if c.get('freeze'): s+=f" (holds at {c['freeze']} s)"
        return s+f"<br>{beat}"
    bars=f"{p['bar']+1}" if p['bars']==1 else f"{p['bar']+1}–{p['bar']+p['bars']}"
    L.append(f"| {i} | {tc(p['f0'])}–{tc(p['f1'])} | {bars} | {p['f0']}–{p['f1']} | {p['section']} | {desc(a,p['chi_beat'])} | {desc(b,p['ctr_beat'])} | {p['rule_name']} | {p['link']} | {p['evidence']} |")
L+=["","## Dropped clips","","- `c-southloop88-tower` and `c-18th-platform`: pinkish 1988 daylight handheld flashes.","- `a-inland-train2`: blows out to white (around 54–55 s in v1).","","These are listed in `BANNED` in `grammar.py`, and the check fails if any of them appears.","",
"## Check output (`check_edl.py`)","","```",open('check_output.txt').read().strip(),"```",""]
open('../music_split_v2_shotlist.md','w').write("\n".join(L))
