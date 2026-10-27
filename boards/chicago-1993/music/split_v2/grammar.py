"""Pairing grammar + grid helpers for the music-synced split screen (v2).
Single source of truth: imported by gen_edl.py (to build), render_v2.py (to render) and check_edl.py (to verify).

Every simultaneous Chicago / counter-world pair must declare one RULE below. Each rule has a
machine check over the catalog tags and the *measured* window stats (scan/<clip>.npz, sampled
over the exact source window that is on screen), plus the human-readable shape rhyme."""
import json,os,numpy as np
HERE=os.path.dirname(os.path.abspath(__file__))
ROOT='/workspace/moodboard/chicago-1993'
FPS=24
ANALYSIS=ROOT+'/edits/music/analysis.json'
CATALOG=ROOT+'/footage/catalog.json'

# ---------------------------------------------------------------- grid
def grid():
    """Bar-downbeat frame grid. Cuts may only ever be expressed as bar indices into this list."""
    A=json.load(open(ANALYSIS)); END=round(A['T']*FPS)
    DF=[round(t*FPS) for t in A['downbeats']]+[END]
    assert DF==sorted(DF) and len(set(DF))==len(DF)
    return A,DF
# Cut rate per section, in bars per shot (energy is expressed by bar count + clip pace, never off-beat cuts)
SECTIONS=[('sparse',0,4,4),('groove',4,12,2),('break',12,13,1),('peak',13,21,1),('release',21,22,1)]
def section_of(bar):
    for n,a,b,step in SECTIONS:
        if a<=bar<b: return n,a,b,step
    raise ValueError(bar)

# ---------------------------------------------------------------- measured window stats
_cache={}
def scan(clip):
    if clip not in _cache:
        z=np.load(f'{HERE}/scan/{clip}.npz'); _cache[clip]={k:np.array(z[k]) for k in z.files}
    return _cache[clip]
def spikes(z):
    med=np.median(z['df'])+1e-3; return z['df']>max(4*med,18)
def window_stats(clip,a,span):
    z=scan(clip); t=z['t']; m=(t>=a)&(t<=a+span)
    if m.sum()<2: m=(t>=a-0.1)&(t<=a+span+0.1)
    lm=z['lm'][m]; jumps=np.abs(np.diff(lm)) if len(lm)>1 else np.array([0.0])
    sm=(t>a+1e-3)&(t<=a+span+0.09)  # a spike at sample t = cut between t-1/12 and t, so a spike exactly at a is fine
    return dict(flow=float(np.median(z['fl'][m])),flow90=float(np.percentile(z['fl'][m],90)),
                mdx=float(np.median(z['mdx'][m])),mdy=float(np.median(z['mdy'][m])),
                warm=float(np.mean(z['warm'][m])),lum=float(lm.mean()),lum_floor=float(lm.min()),lum_max=float(lm.max()),
                clip_max=float(z['clip'][m].max()),flash=float(jumps.max()),cut_inside=bool(spikes(z)[sm].any()))
# quality gates, shared by picker and checker
GATE=dict(lum_floor=13.0,lum_min=10.0,lum_max=200.0,clip_max=0.45,flash=60.0)
def quality_fail(s):
    r=[]
    if s['cut_inside']: r.append('scene cut inside window')
    if s['lum']<GATE['lum_min']: r.append(f"black (mean luma {s['lum']:.0f})")
    if s['lum_floor']<GATE['lum_floor']: r.append(f"goes black (darkest frame luma {s['lum_floor']:.0f})")
    if s['lum_max']>GATE['lum_max'] or s['clip_max']>GATE['clip_max']: r.append(f"blowout (luma max {s['lum_max']:.0f}, clipped {s['clip_max']:.2f})")
    if s['flash']>GATE['flash']: r.append(f"exposure flash (luma jump {s['flash']:.0f})")
    return r
# Clips banned from the edit, with the reason (Topher's v1 notes)
BANNED={'c-southloop88-tower':'pinkish 1988 daylight handheld flash at the v1 peak',
        'c-18th-platform':'pinkish 1988 daylight handheld flash at the v1 peak',
        'a-inland-train2':'blows out to white (v1, ~54-55 s)'}

# ---------------------------------------------------------------- rules
WARM_LIGHT={'sodium','furnace','headlights','fluorescent'}
def _dir(s): return 'L→R' if s['mdx']>0 else 'R→L'
def _same_dir(a,b,minmag=6.0):
    ok=np.sign(a['mdx'])==np.sign(b['mdx']) and abs(a['mdx'])>=minmag and abs(b['mdx'])>=minmag
    return ok,f"subject motion {a['mdx']:+.0f} / {b['mdx']:+.0f} px/s ({_dir(a)} both)" if ok else f"directions differ or weak: {a['mdx']:+.0f} vs {b['mdx']:+.0f} px/s"
def r_fall_into(ca,cb,a,b):
    ok=ca['direction']=='down' and cb['direction']=='down' and a['flow']<9 and b['flow']<9
    return ok,f"both tagged falling (down), both slow (flow {a['flow']:.1f} / {b['flow']:.1f})"
def r_same_way(ca,cb,a,b): return _same_dir(a,b)
def r_window_ride(ca,cb,a,b):
    ok,why=_same_dir(a,b)
    t=ca['move']=='track' and cb['move']=='track'
    return ok and t,f"both tracking shots (move=track: {ca['move']}/{cb['move']}); "+why
def r_stroke(ca,cb,a,b):
    ok=ca['move']=='static' and cb['move']=='static' and a['flow90']>=15 and b['flow90']>=15
    return ok,f"locked-off camera both, strong repeating motion (flow p90 {a['flow90']:.0f} / {b['flow90']:.0f})"
def r_molten_light(ca,cb,a,b):
    ok=a['warm']>=15 and b['warm']>=15 and ca['light'] in WARM_LIGHT and cb['light'] in WARM_LIGHT
    return ok,f"warm light source both ({ca['light']}/{cb['light']}), orange cast R-B {a['warm']:.0f} / {b['warm']:.0f}"
def r_repeated_units(ca,cb,a,b):
    ok,why=_same_dir(a,b); return ok,"rows of repeated units; "+why
def r_still_glow(ca,cb,a,b):
    ok=a['flow']<=3 and b['flow']<=3 and a['warm']>=5 and b['warm']>=5
    return ok,f"near-still (flow {a['flow']:.1f} / {b['flow']:.1f}) and warm-lit (R-B {a['warm']:.0f} / {b['warm']:.0f})"
RULES={
 'FALL_INTO':      dict(name='Falling into a pool', shape='drops hit standing water ↔ molten stream drops into the ladle', check=r_fall_into),
 'SAME_WAY':       dict(name='Same way across the frame', shape='the main subject crosses the frame in the same direction on both sides', check=r_same_way),
 'WINDOW_RIDE':    dict(name='Window ride', shape='both shot from a moving train window, scenery streaming the same way', check=r_window_ride),
 'STROKE':         dict(name='Mechanical stroke', shape='a repeating machine stroke in a locked frame (wiper arm ↔ forge ram)', check=r_stroke),
 'MOLTEN_LIGHT':   dict(name='Sodium = molten', shape='orange light in the dark: sodium streaks ↔ molten metal', check=r_molten_light),
 'REPEATED_UNITS': dict(name='Repeated units sliding past', shape='a grid of identical units slides the same way (streetlights ↔ billets)', check=r_repeated_units),
 'STILL_GLOW':     dict(name='Still glow', shape='a lit box/pool at rest in the dark (shelter ↔ cooling ingots)', check=r_still_glow),
}
def catalog(): return {x['id']:x for x in json.load(open(CATALOG))}
