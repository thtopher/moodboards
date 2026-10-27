"""Shot list markdown. Usage: python3 shotlist.py LEAD OUT.md   (reads check_lead{0,1,2}.json/.txt next to this file)"""
import json,sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from grammar import RULES,frames,FPS,HERE,WEAK
from collections import Counter
lead=int(sys.argv[1]); OUT=sys.argv[2]; W=HERE+'/'
e=json.load(open(W+'edl_v1.json')); FR,END=frames(lead); B=json.load(open(W+'sync/beats.json')); O=json.load(open(W+'sync/override.json'))
CK={L:json.load(open(W+f'check_lead{L}.json')) for L in (0,1,2) if os.path.exists(W+f'check_lead{L}.json')}
cuts={r['shot']:r for r in CK[lead]['cuts']}
def tc(f): s=f/FPS; return f"{int(s//60)}:{s%60:05.2f}"
D=[x['t'] for x in B['downbeats']]; bl=[b-a for a,b in zip(D,D[1:])]
hitc=Counter(h for p in e['pairs'][1:] for h in p['hits'])
L=["# Sky ↔ Sheen: full-song split screen (v1) shot list","",
f"`sky_sheen_full_v1.mp4` (lead {lead}): 1920x1080, 24 fps, {END} frames ({END/FPS:.2f} s). Left panel Sky (A), right panel Sheen (B), 952 px panels and a 16 px gutter (0x0b0b0c). Both panels cut on the same frames.",
"Audio: the full song (`song.wav`) only, untouched (no gain, no edits, no splices), AAC 256k. No clip audio.",
f"Music: 4/4, {len(D)} downbeats from {D[0]:.2f} s to {D[-1]:.2f} s. The tempo drifts like a live take: bars run {bl[0]:.2f} s (~{240/bl[0]:.0f} BPM) at the start and {bl[-1]:.2f} s (~{240/bl[-1]:.0f} BPM) at the end. Real downbeat times are used; there is no fixed BPM.",
f"Cuts: {len(e['pairs'])-1}. Moments hit: "+', '.join(f"{k.replace('_',' ')} {v}" for k,v in hitc.most_common())+".","",
"## Arc","",e['arc'],"","| Section | Shots | Sky zones | Sheen zones | Note |","|---|---|---|---|---|"]
for a in e['sections']: L.append(f"| {a[2]} | {a[0]+1}–{a[1]+1} | {a[3]} | {a[4]} | {a[5]} |")
L+=["","## Link rules","","Each pair is chosen for one named rule that is measured on the actual windows (motion vectors, hue, saturation and luma from a 12 fps scan). The board's 17 match-cut pairs are pinned to the moments they suit and carry their board name.","",
"| Rule | Weight | Meaning | Uses |","|---|---|---|---|","| BOARD | 10 | one of the board's 17 match-cut pairs | "+str(sum(p['rule']=='BOARD' for p in e['pairs']))+" |"]
for k,R in RULES.items(): L.append(f"| {k} | {R['w']} | {R['desc']}{' (weak)' if k in WEAK else ''} | {sum(p['rule']==k for p in e['pairs'])} |")
L+=["","## Beat review (override)","","Beat This! doubled the pulse in three places and split one flam; each was checked against the drum stem (kick and snare onsets) and the bar lengths and fixed in `sync/override.json` (the check applies the same reviewed override to its re-detection of the render audio and also reports the raw result):",""]
for k,v in O['_review'].items(): L.append(f"- **{k} s:** {v}")
L.append(f"- Edits: removed {', '.join(f'{x:.2f}' for x in O['remove'])} s; moved "+', '.join(f"{m['from']:.3f}→{m['to']:.3f} s" for m in O['move'])+"; reviewed grids "+'; '.join(f"{r['from']:.2f}–{r['to']:.2f} s (downbeats "+', '.join(f'{t:.2f}' for t in r['downbeats'])+')' for r in O['regions'])+". Result: 0 irregular bars (the raw run had 10).")
LC=[x for x in B['downbeats'] if x['conf']<0.5]
L.append("- Downbeats still under 0.5 confidence (kept after review: the bar lengths stay regular through them): "+', '.join(f"{x['t']:.2f} s ({x['conf']:.2f})" for x in LC)+".")
L+=["","## Shots","","| # | Time | Frames | Bars | Energy | Section | Moment hit | Offset vs re-detected downbeat | Sky (left) | Sheen (right) | Rule | Why this pair |","|---|---|---|---|---|---|---|---|---|---|---|---|"]
for i,p in enumerate(e['pairs']):
    a,b=e['sky'][i],e['sheen'][i]; f0,f1=FR[i]
    def desc(c):
        s=f"`{c['clip']}` @ {c['src_in']:.2f} s"+(f" ×{c['speed']}" if abs(c['speed']-1)>1e-3 else '')
        return s+f"<br><sub>{c['title'][:70]} ({c['year']}){' · use '+str(c['use']) if c['use']>1 else ''}</sub>"
    hit=', '.join(h.replace('_',' ') for h in p['hits']); why=p['why'].replace('|','/')
    r=cuts.get(i); off=(f"{r['offset_ms']:+.1f} ms"+(" (override)" if r.get('support')=='override' else '')) if r else "start"
    L.append(f"| {i+1} | {tc(f0)}–{tc(f1)} | {f0}–{f1} | {p['bars']} | {p['energy']} | {p['section']} | **{hit}**<br><sub>{why}</sub> | {off} | {desc(a)} | {desc(b)} | {p['rule_name']}{' (weak)' if p['weak'] else ''} | {p['evidence'].replace('|','/')} |")
L+=["","## Lead variants",""]
for Lx,c in sorted(CK.items()):
    offs=[r['offset_ms'] for r in c['cuts']]
    L.append(f"- **lead {Lx}{' (picked)' if Lx==1 else ''}:** cut frame = round(t × 24) − {Lx}. Offsets {min(offs):+.0f} to {max(offs):+.0f} ms vs the re-detected downbeat (median {sorted(offs)[len(offs)//2]:+.0f} ms). Check: {'PASS' if c['pass'] else 'FAIL '+str(c['fails'])}.")
L+=["","Lead 1 puts each cut one frame (~42 ms) ahead of the downbeat, which reads as on the hit; lead 0 can land a cut after the hit, and lead 2 starts to look early.",
"","## Check output (`musicsync/check_render.py`, lead "+str(lead)+")","","```",open(W+f'check_lead{lead}.txt').read().strip(),"```",""]
open(OUT,'w').write("\n".join(L)); print(OUT)
