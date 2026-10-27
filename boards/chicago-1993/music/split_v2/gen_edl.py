"""v2 EDL generator: music-synced split screen, cuts on bar downbeats only, both panels in lockstep.
Pairs are declared on BARS (never seconds). Each pair cuts both panels on the same downbeat frame.
Section cut rates come from grammar.SECTIONS; a pair whose bar span disagrees with its section aborts."""
import json,numpy as np,sys
from grammar import grid,SECTIONS,section_of,RULES,BANNED,window_stats,quality_fail,catalog,scan,FPS
A,DF=grid(); CAT=catalog(); NB=len(A['downbeats'])
L2R,R2L=+1,-1
# (bar, nbars, chicago candidates, counter candidates, rule, dir, link, chicago beat, counter beat, opts)
PAIRS=[
 (0,4,['t-rain-puddles'],['a-kover-ladle'],'FALL_INTO',None,'rain rings in the puddle ↔ the steel stream falling into the ladle (zone 17 pair)','Waiting: rain pools at the curb','Charge: the ladle fills',{}),
 (4,2,['c-impr-bus-night'],['a-acroni-rolls'],'SAME_WAY',L2R,'the bus pulls into the stop ↔ the slab rolls into the stand, same direction (zone 17 pair)','Arrival: the bus pulls in','The slab enters the rolls',{}),
 (6,2,['c-impr-crossing'],['a-servant-slab'],'SAME_WAY',L2R,'riders cross to the bus ↔ the glowing slab slides through, same direction (zone 17 pair)','Boarding: riders cross','The slab runs through',{}),
 (8,2,['c-edison-storefronts'],['a-servant-tap'],'MOLTEN_LIGHT',None,'the sodium-lit strip ↔ the open-hearth tap: the same orange in the dark','Pulling away down the sodium strip','The tap glows',{}),
 (10,2,['c-ic92-night'],['a-servant-roll','a-drama-wire'],'SAME_WAY',R2L,'orange-lit traffic ↔ a hot bar, crossing the same way (zone 17 pair)','Traffic slides past the window','Hot bar in motion',{}),
 (12,1,['t-rain-reflect'],['a-acroni-runout'],'SAME_WAY',L2R,'feet through a puddle reflection ↔ a slab easing down the run-out (zone 17 pair)','Break: feet in the puddle','The run-out slows',{}),
 (13,1,['c-doha-sodium'],['a-vicart-sparks','a-irontap'],'MOLTEN_LIGHT',None,'sodium streaks through a wet windshield ↔ a ladle over the open furnace, sparks flying','The ride: sodium streaks','Ladle over the furnace',{}),
 (14,1,['t-rain-wipers'],['a-hendrichs-drop','a-forge-hammer'],'STROKE',None,'the wiper arm sweeps ↔ the drop-forge ram strikes','Wipers','Drop forge',{}),
 (15,1,['c-amtrak95'],['a-inland-train','a-ecsteel-train'],'WINDOW_RIDE',R2L,'Chicago industrial edge ↔ Indiana Harbor mills, both seen from a train window streaming the same way','Train window, gray industrial edge','Mills past the train window',{}),
 (16,1,['c-94-loop'],['a-mills-fast','a-kover-fast'],'SAME_WAY',L2R,'the L swings through the Loop ↔ hot strip races the stands, same direction','The L through the Loop','Hot strip races the stands',{}),
 (17,1,['c-harrison-arrive'],['a-kover-pan','a-drama-wire'],'SAME_WAY',R2L,'the subway train sweeps the platform ↔ the pan along stacked billets, same direction','Train into Harrison','Billets sweep past',{}),
 (18,1,['c-94-skyline'],['a-ecsteel-train','a-inland-train'],'SAME_WAY',L2R,'the Chicago skyline ↔ the East Chicago smokestack skyline, both sliding the same way under a steel-blue sky','Skyline across the lot','Mill stacks from the train',{'lo':{'c-94-skyline':28.3}}),
 (19,1,['c-94-northside','c-94-loop'],['a-acroni-fast','a-drama-wire'],'SAME_WAY',R2L,'three-flats rush past the L ↔ the roller table rushes past: top speed, same direction','Back porches from the L','Roller table at speed',{}),
 (20,1,['c-edison-sodium'],['a-kover-billets','a-servant-slab'],'SAME_WAY',L2R,'sodium side streets ↔ glowing billets on the line: the same orange, drifting the same way (zone 17 pair)','Home: sodium side streets','Billets cool on the line',{'lo':{'a-kover-billets':10.15}}),
 (21,1,['c-impr-shelter'],['a-servant-pour'],'STILL_GLOW',None,'the lit, empty shelter ↔ ingots cooling in the dark','Release: the empty shelter (holds)','Ingots cool',{'chi_freeze':True}),
]
def target(sec):  # pace preference per section
    return {'sparse':'calm','break':'calm','release':'calm','groove':'mid','peak':'fast'}[sec]
used={}
def windows(clip,dur,sec,dirn,freeze=False,lo=0.0):
    """All clean windows for a clip, best first: list of (score, src_in, speed, span, stats)."""
    if clip in BANNED: return []
    z=scan(clip); t=z['t']
    for sp in ([1.0] if freeze else [1.0,0.96,0.93,0.9]):
        span=min(dur*sp,3.0) if freeze else dur*sp; out=[]
        for a in t:
            if a+span>t[-1]: break
            if a<lo: continue
            if any(not(a+span<=u0 or a>=u1) for u0,u1 in used.get(clip,[])): continue
            s=window_stats(clip,a,span)
            if quality_fail(s): continue
            if dirn is not None and not(np.sign(s['mdx'])==dirn and abs(s['mdx'])>=8): continue
            sc={'calm':-s['flow'],'mid':-abs(s['flow']-10),'fast':s['flow']}[target(sec)]+(0.3*abs(s['mdx']) if dirn else 0)
            out.append((sc,float(a),sp,span,s))
        if out: return sorted(out,key=lambda x:-x[0])
    return []
pairs=[]; chi=[]; ctr=[]
bar=0
for (b0,nb,chis,ctrs,rule,dirn,link,beat_c,beat_k,opt) in PAIRS:
    assert b0==bar,f'pairs must tile the bars contiguously (gap/overlap at bar {b0})'
    sec,sa,sb,step=section_of(b0)
    assert rule in RULES,rule
    assert nb==step or b0+nb==NB, f'bar {b0}: {nb}-bar shot but section {sec} cuts every {step} bars'
    assert b0+nb<=sb or b0+nb==NB, f'bar {b0}: shot crosses the {sec} section boundary'
    f0,f1=DF[b0],DF[b0+nb]; dur=(f1-f0)/FPS
    opts={}
    for side,cands,freeze in (('chi',chis,opt.get('chi_freeze',False)),('ctr',ctrs,False)):
        opts[side]=[(c,w) for c in sorted(cands,key=lambda c:c in used) for w in windows(c,dur,sec,dirn,freeze,opt.get('lo',{}).get(c,0.0))[:40]]
    best=None
    for ci,(cc,cw) in enumerate(opts['chi']):
        for ki,(kc,kw) in enumerate(opts['ctr']):
            ok,why=RULES[rule]['check'](CAT[cc],CAT[kc],cw[4],kw[4])
            if ok:
                rank=ci+ki+(100 if cc in used else 0)+(100 if kc in used else 0)
                if best is None or rank<best[0]: best=(rank,cc,cw,kc,kw,why)
    if not best: sys.exit(f'bar {b0}: no window pair satisfies {rule} for {chis} / {ctrs}')
    _,cc,cw,kc,kw,why=best; sides=[]
    for c,(sc,a,sp,span,st),freeze in ((cc,cw,opt.get('chi_freeze',False)),(kc,kw,False)):
        used.setdefault(c,[]).append((a-0.1,a+span+0.2))
        sh=dict(bar=b0,bars=nb,f0=f0,f1=f1,clip=c,src_in=round(a,3),speed=sp,src_span=round(span,3),stats={k:(round(v,2) if isinstance(v,float) else v) for k,v in st.items()},
                world=CAT[c]['world'],pace=CAT[c]['pace'])
        if freeze: sh['freeze']=round(span,3)
        sides.append(sh)
    chi.append(sides[0]); ctr.append(sides[1])
    pairs.append(dict(bar=b0,bars=nb,section=sec,f0=f0,f1=f1,rule=rule,rule_name=RULES[rule]['name'],link=link,evidence=why,
                      chi=sides[0]['clip'],ctr=sides[1]['clip'],chi_beat=beat_c,ctr_beat=beat_k))
    bar=b0+nb
assert bar==NB
ARC=("One rider's trip mirrored by one heat of steel. Chicago: waiting in the rain → the bus arrives → boarding → pulling away "
     "down the sodium strip → (break) → the ride across the city by bus, L and train at full speed → back through the sodium side streets → the empty shelter. "
     "Steel: the ladle fills → the slab enters the rolls → tap and hot bar → (break: the run-out slows) → the mill at full speed → billets cool on the line → ingots cool in the dark.")
json.dump(dict(fps=FPS,end_frame=DF[-1],downbeat_frames=DF,arc=ARC,pairs=pairs,chi=chi,ctr=ctr),open('edl_v2.json','w'),indent=1,ensure_ascii=False)
for p,c,k in zip(pairs,chi,ctr):
    print(f"bar {p['bar']+1:>2} f{p['f0']:>4}-{p['f1']:<4} {p['section']:<7} {p['rule']:<14} {c['clip']:<20} in={c['src_in']:<6} x{c['speed']} | {k['clip']:<18} in={k['src_in']:<6} x{k['speed']} :: {p['evidence']}")
