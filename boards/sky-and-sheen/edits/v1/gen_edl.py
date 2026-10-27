"""Build edl_v1.json: one Sky/Sheen pair per shot of the musicsync cut list (both panels cut on the same detected
downbeat frames). Greedy in shot order over measured windows of the normalized 24 fps clips:
  side score = pace fit to the bar's energy (board pace tags, speed-adjusted) + arc zone fit + age (older is better)
               - low resolution - darkness - repeats (max 3 uses, at least MIN_GAP shots apart, never overlapping)
  pair score = side scores + the weight of the strongest link rule that passes on the measured windows
               (board pairs are pinned to their moments and carry their own named rule).
Every cut must also be predicted to read as a clean hard cut in both panels (the check finds cuts from pixels):
predicted cut diff >= CUT_MIN and >= CUT_RATIO x the in-shot frame diffs on either side, for every lead."""
import json,sys,numpy as np
from grammar import *
C=cutlist(); SH=C['shots']; CAT=catalog(); LEADS=C['config']['leads']
FR={L:frames(L)[0] for L in LEADS}
CUT_MIN=30.0; CUT_RATIO=2.2; MIN_GAP=15; MAX_USES=3; STEP=4; PAD=2
used={}   # clip -> list of (shot, i0, i1)
def nwin(k): return max(FR[L][k][1]-FR[L][k][0] for L in LEADS)
def tdiff(c1,f1,c2,f2):
    a=thumbs(c1); b=thumbs(c2); f1=min(f1,len(a)-1); f2=min(f2,len(b)-1)
    return float(np.abs(a[f1].astype(np.float32)-b[f2].astype(np.float32)).mean())
def cut_ok(prev,c,i0,sp,k):
    """prev = (clip,i0,speed) on this panel for shot k-1; the new window starts at i0 of c."""
    if prev is None: return True,99.0
    pc,pi0,psp=prev; worst=99.0
    inc=src_frames(i0,2,sp); nxt=tdiff(c,inc[0],c,inc[1])
    for L in LEADS:
        n=FR[L][k-1][1]-FR[L][k-1][0]; out=src_frames(pi0,n,psp)
        d=tdiff(pc,out[-1],c,inc[0]); prv=tdiff(pc,out[-2],pc,out[-1])
        if d<CUT_MIN or d<CUT_RATIO*max(prv,nxt): return False,d
        worst=min(worst,d)
    return True,worst
_pw={}
def into_pin(prev,pc,k):
    """look-ahead: the next shot is a board pin; keep only windows that can cut cleanly into some clean window of it."""
    n=nwin(k)+PAD
    if (pc,k) not in _pw: _pw[(pc,k)]=[i for i in range(0,len(thumbs(pc))-n-1,6) if not quality_fail(window_stats(pc,i,n,1.0),relax_dark=True)]
    return any(cut_ok(prev,pc,i,1.0,k)[0] for i in _pw[(pc,k)])
def age_bonus(c):
    y=year(c); return 1.2 if y<=1940 else 0.9 if y<=1960 else 0.4 if y<=2000 else 0.0
def side_cands(k,world,prev,pin=None,top=60):
    sh=SH[k]; e=sh['energy']; arc=arc_of(k); zones=(arc[3] if world=='A' else arc[4]).split()
    n=nwin(k)+PAD; out=[]
    clips=[pin] if pin else [c for c,r in CAT.items() if r['world']==world and c not in BANNED and (r['zone']!='10' or k==0)]
    for c in clips:
        u=used.get(c,[])
        if not pin and any(c in v and kk>k for kk,v in PIN.items()): continue   # board-pair clips are saved for their moment
        if not pin and (len(u)>=MAX_USES or (u and k-u[-1][0]<MIN_GAP)): continue
        nf=len(thumbs(c)); speeds=[1.0]+([1.5,2.0] if e=='peak' and pace(c)<=3 else [1.5] if e=='groove' and pace(c)<=2 else [])
        per=[]
        for sp in speeds:
            span=int(np.ceil((n-1)*sp))+1
            for i0 in range(0,nf-span-1,STEP if not pin else 2):
                if any(not(i0+span+12<=a or i0>=b+12) for _,a,b in u): continue
                s=window_stats(c,i0,n,sp)
                if quality_fail(s,relax_dark=bool(pin)): continue
                ok,cd=cut_ok(prev,c,i0,sp,k)
                if not ok: continue
                if not pin and k+1 in PIN and not into_pin((c,i0,sp),PIN[k+1][0 if world=='A' else 1],k+1): continue
                p=pace(c,sp); sc=-2.0*pace_fit(p,e)+(1.5 if CAT[c]['zone'] in zones else 0)+age_bonus(c)
                sc-=1.0 if width(c)<LOWRES else 0; sc-=0.6 if width(c)<300 else 0
                sc-=max(0.0,(DARK-s['lum'])/12); sc-=3.0*len(u); sc-=0.4*(sp-1)
                sc+=min(2.0,0.05*s['flow']) if e=='peak' else (-min(1.0,0.1*s['flow']) if e in ('sparse','break','release') else 0)
                per.append((sc,c,i0,sp,n,s,p,cd))
        per.sort(key=lambda x:-x[0]); out+=per[:8]
    out.sort(key=lambda x:-x[0]); return out[:top]
def best_rule(a,b,ca,cb,pa,pb):
    best=None
    for key,R in RULES.items():
        ok,name,ev=(R['check'](a,b,ca,cb,pa,pb) if key=='PACE' else R['check'](a,b,ca,cb))
        if ok and (best is None or R['w']>best[0]): best=(R['w'],key,name,ev)
    return best
pairs=[]; A=[]; B=[]; prevA=prevB=None; last_rule=None
for k,sh in enumerate(SH):
    pin=PIN.get(k)
    ca_=side_cands(k,'A',prevA,pin[0] if pin else None); cb_=side_cands(k,'B',prevB,pin[1] if pin else None)
    if not ca_ or not cb_: sys.exit(f'shot {k}: no clean window (A {len(ca_)}, B {len(cb_)}) pin={pin}')
    best=None
    for xa in ca_:
        for xb in cb_:
            if pin:
                n,rname,note,mode=BOARD_BY[pin]; meas=None
                if mode: ok,_,ev=RULES[mode]['check'](xa[5],xb[5],CAT[xa[1]],CAT[xb[1]]); meas=(ok,ev)
                r=(10.0+(1.0 if meas and meas[0] else 0),'BOARD',rname,f"board pair {n:02d}: {note}"+(f" Measured: {meas[1]} ({'passes' if meas[0] else 'does not pass'} the {mode} check)." if meas else ''))
            else:
                r=best_rule(xa[5],xb[5],CAT[xa[1]],CAT[xb[1]],xa[6],xb[6])
                if r is None: continue
            tot=xa[0]+xb[0]+r[0]-(0.8 if r[1]==last_rule else 0)
            if best is None or tot>best[0]: best=(tot,xa,xb,r)
    if best is None: sys.exit(f'shot {k}: no pair passes any rule')
    tot,xa,xb,r=best; sides=[]
    for x in (xa,xb):
        sc,c,i0,sp,n,s,p,cd=x; span=int(np.ceil((n-1)*sp))+1
        used.setdefault(c,[]).append((k,i0,i0+span))
        sides.append(dict(shot=k,clip=c,world=CAT[c]['world'],zone=CAT[c]['zone'],src_in_frame=int(i0),src_in=round(i0/FPS,4),speed=sp,
                          src_span=round(span/FPS,3),pace=p,year=year(c),res=CAT[c]['master_res'],use=len(used[c]),
                          cut_diff=round(cd,1) if cd<99 else None,stats={q:(round(v,2) if isinstance(v,float) else v) for q,v in s.items()},
                          title=CAT[c]['title']))
    A.append(sides[0]); B.append(sides[1]); prevA=(xa[1],xa[2],xa[3]); prevB=(xb[1],xb[2],xb[3]); last_rule=r[1]
    arc=arc_of(k)
    pairs.append(dict(shot=k,bar0=sh['bar0'],bars=sh['bars'],t0=sh['t0'],t1=sh['t1'],energy=sh['energy'],hits=sh['hits'],rank=sh.get('rank'),
                      why=sh['why'],section=arc[2],section_note=arc[5],rule=r[1],rule_name=r[2],evidence=r[3],weak=r[1] in WEAK,
                      sky=sides[0]['clip'],sheen=sides[1]['clip'],score=round(tot,2)))
    print(f"#{k:>2} {sh['t0']:7.2f} {sh['bars']}b {sh['energy']:<7} {arc[2][:14]:<14} {r[2][:24]:<24} {xa[1]:<18} {xa[2]/FPS:6.2f} x{xa[3]} p{xa[6]} L{xa[5]['lum']:.0f} | {xb[1]:<18} {xb[2]/FPS:6.2f} x{xb[3]} p{xb[6]} L{xb[5]['lum']:.0f} cut {min(xa[7],xb[7]):.0f}",flush=True)
ARCTXT=("A day of sky mirrored by a day of sheen. Titles (sky in letters ↔ metal in letters) → first light: sunrise, pad-light bokeh "
        "and a flat horizon ↔ gallium beads, a mirror lake and crystals → the drop: wind tears the clouds ↔ soap films race → glitter → "
        "cumulus builds ↔ molds grow → storm heads and lightning ↔ slime molds → the second drop: the Earth streams past the shuttle ↔ "
        "films stream → the eye of the storm and the sun's disc ↔ spirals and sporangia → full speed: aurora and racing clouds ↔ "
        "interference bands and metal → golden hour ↔ gold molds and molten gold → fog and slick → a hush (drums out) → a lens flare ↔ a glint on the drop → "
        "night orbit ↔ metal → the sun on the Earth's rim ↔ light on a bubble's rim (drums out) → all the light at once → the last gold.")
json.dump(dict(fps=FPS,arc=ARCTXT,sections=ARC,pairs=pairs,sky=A,sheen=B,params=dict(CUT_MIN=CUT_MIN,CUT_RATIO=CUT_RATIO,MIN_GAP=MIN_GAP,MAX_USES=MAX_USES,PAD=PAD)),
          open(HERE+'/edl_v1.json','w'),indent=1,ensure_ascii=False)
from collections import Counter
print('rules',Counter(p['rule'] for p in pairs)); print('weak',sum(p['weak'] for p in pairs))
rep={c:len(v) for c,v in used.items() if len(v)>1}; print('repeats',len(rep),sum(v-1 for v in rep.values()),rep)
print('distinct A',len({a['clip'] for a in A}),'B',len({b['clip'] for b in B}))
print('dark',[(a['shot'],a['clip'],a['stats']['lum']) for a in A+B if a['stats']['lum']<DARK])
print('lowres',[(a['shot'],a['clip']) for a in A+B if width(a['clip'])<LOWRES])
