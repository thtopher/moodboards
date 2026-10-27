"""Sky and Sheen full-song split screen v1: the single source of truth for the pairing grammar.
Imported by gen_edl.py (to build), render.py (to render) and check_edl.py (to verify the EDL independently).

Left panel = A · Sky (clouds, sunsets, VHS lens flares, orbit). Right panel = B · Sheen (iridescent films, oil,
molds, metals, crystals). Every simultaneous pair declares one RULE. Generated pairs must pass the rule's machine
check on the *measured* window stats (scan/<clip>.npz over the exact source window on screen); the 17 board
match-cut pairs (zone 17 on the board, checked by eye there) are pinned to the moments in the song they fit."""
import json,os,re,numpy as np
HERE=os.path.dirname(os.path.abspath(__file__))
ROOT='/workspace/moodboard/sky-and-sheen'
FPS=24; PW=952
CUTLIST=HERE+'/sync/cutlist.json'; MUSIC=ROOT+'/edits/song/song.wav'; OVERRIDE=HERE+'/sync/override.json'
NORM=HERE+'/norm/'
# ---------------------------------------------------------------- data
_C=None
def catalog():
    global _C
    if _C is None: _C={r['id']:r for r in json.load(open(ROOT+'/footage/catalog.json'))}
    return _C
_s,_k,_t={},{},{}
def scan(c):
    if c not in _s: z=np.load(f'{HERE}/scan/{c}.npz'); _s[c]={k:np.array(z[k]) for k in z.files}
    return _s[c]
def cutscan(c):
    if c not in _k: j=json.load(open(f'{HERE}/cuts/{c}.json')); j['d24']=np.array(j['d24']); _k[c]=j
    return _k[c]
def thumbs(c):
    if c not in _t: _t[c]=np.load(f'{HERE}/thumbs/{c}.npy',mmap_mode='r')
    return _t[c]
def year(c):
    m=re.search(r'(1[89]\d\d|20\d\d)',catalog()[c]['source_date'] or ''); return int(m.group(1)) if m else 2015
def width(c): return int(catalog()[c]['master_res'].split('x')[0])
def cutlist():
    C=json.load(open(CUTLIST)); assert C['config']['fps']==FPS; return C
def frames(lead):
    """Shot boundaries in frames for one lead: [(f0,f1)] per shot, contiguous, ending on the music's last frame."""
    C=cutlist(); F=[tuple(s['frames'][str(lead)]) for s in C['shots']]
    for a,b in zip(F[:-1],F[1:]): assert a[1]==b[0],'cut list is not contiguous'
    return F,C['end_frame']
# ---------------------------------------------------------------- pace (the board's pace tags, adjusted for speed)
TH=[2,5,10,17]   # board-relative thresholds on pace_raw (tools/catalog.py)
def pace(c,speed=1.0): return 1+sum(catalog()[c]['pace_raw']*speed>=t for t in TH)
TARGET={'sparse':(1,2),'break':(1,2),'groove':(2,3),'peak':(4,5),'release':(1,1)}
def pace_fit(p,energy):
    lo,hi=TARGET[energy]; return 0 if lo<=p<=hi else min(abs(p-lo),abs(p-hi))
# ---------------------------------------------------------------- measured window stats
def src_frames(i0,n,speed):
    """Source frame index of each output frame (normalized clips are 24 fps CFR, so this is exact at speed 1)."""
    return np.minimum(i0+np.round(np.arange(n)*speed).astype(int),10**9)
def window_stats(c,i0,n,speed=1.0):
    z=scan(c); t=z['t']; a=i0/FPS; b=(i0+(n-1)*speed)/FPS
    m=(t>=a-1e-6)&(t<=b+1e-6)
    if m.sum()<2: m=(t>=a-0.1)&(t<=b+0.1)
    lm=z['lm'][m]; w=z['sat'][m]+1e-3; h=np.radians(z['hue'][m])
    hue=float(np.degrees(np.arctan2((w*np.sin(h)).sum(),(w*np.cos(h)).sum()))%360)
    d=cutscan(c)['d24']; j0=i0+1; j1=min(len(d),int(np.ceil(i0+(n-1)*speed))+1)
    seg=d[j0:j1] if j1>j0 else np.array([0.0])
    # in-window spike: a frame diff well above both neighbours (the check's cut detector), with a lower floor for margin
    sp=[j for j in range(max(j0,1),min(j1,len(d)-1)) if d[j]>=17 and d[j]>=1.5*max(d[j-1],d[j+1])]
    mx,my=z['mdx'][m],z['mdy'][m]
    cons=lambda v:float(np.mean((np.sign(v)==np.sign(np.median(v)))&(np.abs(v)>=2))) if np.median(v)!=0 else 0.0
    return dict(dx_cons=cons(mx),dy_cons=cons(my),flow=float(np.median(z['fl'][m])),mdx=float(np.median(z['mdx'][m])),mdy=float(np.median(z['mdy'][m])),
                lum=float(lm.mean()),lum_floor=float(lm.min()),lum_max=float(z['lu'][m].max()),clip_max=float(z['clip'][m].max()),
                flash=float(np.abs(np.diff(lm)).max()) if len(lm)>1 else 0.0,sat=float(z['sat'][m].mean()),hue=hue,
                d_p95=float(np.percentile(seg,95)),cut_inside=bool(sp or any(i0<f<=i0+(n-1)*speed+1 for f in cutscan(c)['cut_frames'])))
GATE=dict(lum_min=16.0,lum_floor=8.0,clip_max=0.30,flash=45.0)
def quality_fail(s,relax_dark=False):
    r=[]
    if s['cut_inside']: r.append('hard cut or flash spike inside window')
    if s['lum']<(6.0 if relax_dark else GATE['lum_min']): r.append(f"too dark (mean luma {s['lum']:.0f})")
    if s['lum_floor']<(2.0 if relax_dark else GATE['lum_floor']): r.append(f"goes black (darkest sample {s['lum_floor']:.0f})")
    if s['clip_max']>GATE['clip_max']: r.append(f"blowout (clipped {s['clip_max']:.2f})")
    if s['flash']>GATE['flash']: r.append(f"exposure flash (luma jump {s['flash']:.0f})")
    return r
DARK=40.0      # mean luma below this reads dark: penalized, reported
LOWRES=480     # master narrower than this is penalized (4.5x upscale for 320x240)
BANNED={}      # clip -> reason (none yet)
# ---------------------------------------------------------------- link rules (measured)
def _hname(h):
    for lo,hi,n in [(0,18,'RED-ORANGE'),(18,45,'ORANGE'),(45,70,'GOLD'),(70,160,'GREEN'),(160,200,'CYAN'),(200,255,'BLUE'),(255,290,'VIOLET'),(290,340,'MAGENTA'),(340,360,'RED')]:
        if lo<=h<hi: return n
    return 'RED'
def hdiff(a,b): d=abs(a-b)%360; return min(d,360-d)
def r_dir(a,b,ca,cb):
    ok=np.sign(a['mdx'])==np.sign(b['mdx']) and abs(a['mdx'])>=6 and abs(b['mdx'])>=6 and min(a['dx_cons'],b['dx_cons'])>=0.7
    d='L→R' if a['mdx']>0 else 'R→L'
    return ok,f"DIRECTION CARRY · {d}",f"subject motion {a['mdx']:+.0f} / {b['mdx']:+.0f} px/s, both {d} ({a['dx_cons']*100:.0f}% / {b['dx_cons']*100:.0f}% of samples agree)"
def r_vert(a,b,ca,cb):
    ok=np.sign(a['mdy'])==np.sign(b['mdy']) and min(abs(a['mdy']),abs(b['mdy']))>=6 and min(a['dy_cons'],b['dy_cons'])>=0.7 and abs(a['mdy'])>=0.8*abs(a['mdx']) and abs(b['mdy'])>=0.8*abs(b['mdx'])
    d='RISE' if a['mdy']<0 else 'FALL'
    return ok,f"VERTICAL CARRY · {d}",f"vertical motion {a['mdy']:+.0f} / {b['mdy']:+.0f} px/s, both {'up' if d=='RISE' else 'down'}"
def r_hue(a,b,ca,cb):
    ok=a['sat']>=50 and b['sat']>=50 and hdiff(a['hue'],b['hue'])<=20
    return ok,f"HUE LOCK · {_hname((a['hue']+b['hue'])/2 if abs(a['hue']-b['hue'])<180 else ((a['hue']+b['hue']+360)/2)%360)}",f"hue {a['hue']:.0f}° / {b['hue']:.0f}° (Δ{hdiff(a['hue'],b['hue']):.0f}°), saturation {a['sat']:.0f} / {b['sat']:.0f}"
def r_churn(a,b,ca,cb):
    ok=ca['direction'] in ('churn','swirl') and cb['direction'] in ('churn','swirl') and a['flow']>=1.5 and b['flow']>=1.5
    return ok,"CHURN RHYME","both tagged churn/swirl, measured flow "+f"{a['flow']:.1f} / {b['flow']:.1f}"
def r_silver(a,b,ca,cb):
    ok=a['sat']<=20 and b['sat']<=20 and abs(a['lum']-b['lum'])<=25
    return ok,"SILVER LOCK",f"both black-and-white film (saturation {a['sat']:.0f} / {b['sat']:.0f}), matched gray (luma {a['lum']:.0f} / {b['lum']:.0f})"
def r_still(a,b,ca,cb):
    ok=a['flow']<=1.2 and b['flow']<=1.2
    return ok,"STILL HOLD",f"both near-still (flow {a['flow']:.2f} / {b['flow']:.2f} px/s)"
def r_pace(a,b,ca,cb,pa=None,pb=None):
    ok=pa==pb and pa>=3
    return ok,f"PACE MATCH · {pa}",f"both measured at pace {pa} (board tag, speed-adjusted)"
def r_flow(a,b,ca,cb):
    ok=min(a['flow'],b['flow'])>=2.0 and max(a['flow'],b['flow'])<=1.35*min(a['flow'],b['flow'])
    return ok,"MOTION MATCH",f"the same amount of motion on both sides (flow {a['flow']:.1f} / {b['flow']:.1f} px/s)"
def r_tone(a,b,ca,cb):
    ok=abs(a['lum']-b['lum'])<=15 and abs(a['sat']-b['sat'])<=15
    return ok,"TONE MATCH",f"matched brightness and color strength (luma {a['lum']:.0f} / {b['lum']:.0f}, saturation {a['sat']:.0f} / {b['sat']:.0f})"
RULES={'DIR':dict(w=6.0,check=r_dir,desc='the main motion crosses the frame the same way on both sides'),
       'VERT':dict(w=5.0,check=r_vert,desc='both rise (or both fall) in frame'),
       'HUE':dict(w=5.0,check=r_hue,desc='the same hue fills both frames'),
       'CHURN':dict(w=4.0,check=r_churn,desc='turbulence on both sides'),
       'SILVER':dict(w=3.0,check=r_silver,desc='black-and-white film on both sides at the same gray'),
       'STILL':dict(w=3.0,check=r_still,desc='both frames held still'),
       'FLOW':dict(w=2.0,check=r_flow,desc='the same measured amount of motion'),
       'PACE':dict(w=1.5,check=r_pace,desc='same measured pace'),
       'TONE':dict(w=1.0,check=r_tone,desc='matched brightness and color strength (the weakest rule)')}
WEAK={'PACE','SILVER','TONE','FLOW'}
# ---------------------------------------------------------------- the 17 board match-cut pairs (tools/pairs.py, zone 17)
BOARD=[
('a-cep427','b-gold-dendrite','HUE LOCK · ORANGE','Afterglow fills the sky with orange; molten gold fills the crucible with the same orange as it crusts over.','HUE'),
('a-cep-wind','b-soap-4','DIRECTION CARRY · L→R','Wind tears the clouds left to right at full speed; soap-film bands race the same way.','DIR'),
('a-sdo-blast','b-myxo-sphere','SHAPE RHYME · DISC','The sun as a red disc in extreme ultraviolet; a slime-mold sporangium as a gray disc in 1931.',None),
('a-shuttle-bokeh','b-gallium-drops','BOKEH → BEADS','Out-of-focus pad lights before dawn become beads of liquid gallium.',None),
('a-hsf87-flare','b-alfin-foil','FLARE → GLINT','A starburst flares as the sun clears the Earth; crumpled foil throws the same hard glints in 1956.',None),
('a-pipeline-storm','b-myxo-veins','BRANCH RHYME','Lightning forks under a storm head; plasmodium veins fork across the dish.',None),
('a-usda-heap','b-penicillium','GROWTH FRONT','A cumulus heap builds upward in 1920; a Penicillium fruiting body pushes up out of its colony.',None),
('a-rainier-sea','b-myxo-front','EDGE RHYME','The tinted edge of a cloud sea below Rainier; the lacy advancing edge of a slime mold.',None),
('a-iss-aurora-v','b-soap-1','COLOR BAND','Aurora curtains ripple as green bands; thin-film interference ripples as rainbow bands.',None),
('a-masada','b-rainier-mirror','HORIZON LINE','A flat Dead Sea sunrise horizon; a still mountain lake mirroring its peaks in 1920.',None),
('a-hsf81','b-soap-7','PACE MATCH · 5','The Earth streams past the shuttle window; soap-film cells stream and break into foam.',None),
('a-pipeline-title','b-alu-title','TYPE RHYME','"Pipeline to the Clouds" (GE, 1951); "Aluminum on the March" (Reynolds, 1956). Two industrial titles, sky and metal.',None),
('a-usda-sunwater','b-alfin-drops','SPECULAR SUN','Sun glitter on water, 1920; light beading on anodized metal, 1956.',None),
('a-iss-hurricane','b-vitc','SPIRAL','A hurricane eye from orbit; vitamin C crystals radiating in polarized light.',None),
('a-jt-sunset','b-physarum-tl','HUE LOCK · GOLD','Golden-hour clouds over Joshua Tree; a yellow Physarum spreading over oat flakes.','HUE'),
('a-gg-fog','b-oilslick-aerial','DIRECTION CARRY · R→L','Fog pours right to left past the Golden Gate; the 1969 Santa Barbara slick drifts the same way.','DIR'),
('a-iss-sunburst','b-bubble-burst','RIM LIGHT','The sun bursts on the curved rim of the Earth; light rides the curved rim of a bubble.',None),
]
BOARD_BY={(a,b):(n+1,r,note,m) for n,(a,b,r,note,m) in enumerate(BOARD)}
# ---------------------------------------------------------------- the arc (shot ranges of sync/cutlist.json)
# zones: 01 clouds · 02 sunsets · 03 VHS flares / shuttle · 04 orbit & sun · 05 films & oil · 06 molds · 07 metals · 08 crystals · 10 titles
ARC=[
 (0,0,'Titles','10','10','Two industrial titles: a sky made of letters, a metal made of letters'),
 (1,7,'First light','02 03','07 08','Dawn and the first flares ↔ beads, mirrors and crystals waking up'),
 (8,11,'Wind','01','05','The drop: wind tears the clouds ↔ soap films race'),
 (12,13,'Glitter','02 01','07','Break: sun glitter ↔ light beading on metal'),
 (14,15,'Cumulus','01','06','Clouds build ↔ molds grow'),
 (16,25,'Storm and mold','01','06 08','Storm heads and lightning ↔ slime molds and crystals, slow'),
 (26,28,'Orbit','03 04','05','The second drop: the Earth streams past the shuttle ↔ films stream'),
 (29,31,'Eye of the storm','04','08 06','Break: spirals and discs from above'),
 (32,44,'Full speed','01 04','05 07','Peak: aurora bands and racing clouds ↔ interference bands and metal'),
 (45,49,'Golden hour','02','06 07','Groove: gold and orange skies ↔ gold molds and molten gold'),
 (50,58,'Fog and slick','01 02','05 07','Peak: fog pours, clouds race ↔ oil slicks and films drift'),
 (59,59,'Hush','01 02','08 07','Drums out: one slow sky ↔ one slow crystal (holds 3 bars)'),
 (60,60,'Flare','03','07','Drums back in on the drop: a lens flare ↔ a glint on foil'),
 (61,68,'Night orbit','04 03','07 05','Peak: night passes and aurora ↔ metal and ferrofluid'),
 (69,69,'Rim light','03 04','05','Drums out: the sun on the rim of the Earth ↔ light on the rim of a bubble (holds 3 bars)'),
 (70,81,'All the light at once','01 02 03 04','05 06 07 08','Final peak: everything returns at speed'),
 (82,82,'Release','02','06 07','Release: the last gold'),
]
PIN={0:('a-pipeline-title','b-alu-title'),1:('a-shuttle-bokeh','b-gallium-drops'),3:('a-masada','b-rainier-mirror'),
     8:('a-cep-wind','b-soap-4'),12:('a-usda-sunwater','b-alfin-drops'),14:('a-usda-heap','b-penicillium'),
     15:('a-rainier-sea','b-myxo-front'),16:('a-pipeline-storm','b-myxo-veins'),26:('a-hsf81','b-soap-7'),
     29:('a-iss-hurricane','b-vitc'),31:('a-sdo-blast','b-myxo-sphere'),32:('a-iss-aurora-v','b-soap-1'),
     46:('a-jt-sunset','b-physarum-tl'),48:('a-cep427','b-gold-dendrite'),50:('a-gg-fog','b-oilslick-aerial'),
     60:('a-hsf87-flare','b-alfin-foil'),69:('a-iss-sunburst','b-bubble-burst')}
def arc_of(n):
    for a in ARC:
        if a[0]<=n<=a[1]: return a
    raise ValueError(n)
