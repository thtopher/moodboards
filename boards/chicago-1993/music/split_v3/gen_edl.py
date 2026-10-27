"""v3 EDL: one pair per shot of the musicsync cut list. Both panels cut on the same detected downbeat (lockstep).
Pairs keep the v2 arc and rules; the shot count/lengths now come from the music (anchors on drums in, drums out,
break, drop, fill landings, release), so the pair list is written against shot indices of sync/cutlist.json."""
import json,sys,numpy as np
from grammar import RULES,BANNED,window_stats,quality_fail,catalog,scan,cutlist,FPS
from scan_cuts import clip_cuts
C=cutlist(); SH=C['shots']; CAT=catalog(); L2R,R2L=+1,-1
PAD=3/FPS   # windows are picked 3 frames longer so any lead variant (0-2 frames early) stays inside a clean window
# (chicago candidates, counter candidates, rule, dir, link, chicago beat, counter beat, opts)
PAIRS=[
 (['c-nightview','t-rain-window'],['a-servant-furnace','a-servant-ladle'],'STILL_GLOW',None,'the city at rest under sodium ↔ the furnace idling (fade in)','Night: the city at rest','The furnace idles',{}),
 (['t-rain-puddles'],['a-kover-ladle'],'FALL_INTO',None,'rain rings in the puddle ↔ the steel stream falling into the ladle (zone 17 pair)','Waiting: rain pools at the curb','Charge: the ladle fills',{}),
 (['c-impr-bus-night'],['a-acroni-rolls'],'SAME_WAY',L2R,'the bus pulls into the stop ↔ the slab rolls into the stand, same direction (zone 17 pair)','Arrival: the bus pulls in','The slab enters the rolls',{}),
 (['c-impr-crossing'],['a-servant-slab'],'SAME_WAY',L2R,'riders cross to the bus ↔ the glowing slab slides through, same direction (zone 17 pair)','Boarding: riders cross','The slab runs through',{}),
 (['c-edison-storefronts'],['a-servant-tap'],'MOLTEN_LIGHT',None,'the sodium-lit strip ↔ the open-hearth tap: the same orange in the dark','Pulling away down the sodium strip','The tap glows',{}),
 (['c-ic92-night'],['a-servant-roll','a-drama-wire'],'SAME_WAY',R2L,'orange-lit traffic ↔ a hot bar, crossing the same way (zone 17 pair)','Traffic slides past the window','Hot bar in motion',{}),
 (['c-doha-sodium'],['a-vicart-sparks','a-irontap'],'MOLTEN_LIGHT',None,'sodium streaks through a wet windshield ↔ a ladle over the open furnace, sparks flying','The ride: sodium streaks','Ladle over the furnace',{}),
 (['t-rain-wipers'],['a-hendrichs-drop','a-forge-hammer'],'STROKE',None,'the wiper arm sweeps ↔ the drop-forge ram strikes','Wipers','Drop forge',{}),
 (['c-edison-corner','c-metra92-dusk'],['a-irontap','a-servant-ladle','a-westinghouse-1904'],'MOLTEN_LIGHT',None,'a sodium corner slides up ↔ iron pours from the tap: the same orange in the dark','Sodium corner','Iron tap',{}),
 (['t-rain-reflect'],['a-acroni-runout'],'SAME_WAY',L2R,'feet through a puddle reflection ↔ a slab easing down the run-out (zone 17 pair)','Break: feet in the puddle','The run-out slows',{}),
 (['c-amtrak95'],['a-inland-train','a-ecsteel-train'],'WINDOW_RIDE',R2L,'Chicago industrial edge ↔ Indiana Harbor mills, both seen from a train window streaming the same way','Drop: train window, gray industrial edge','Mills past the train window',{}),
 (['c-94-loop'],['a-mills-fast','a-kover-fast'],'SAME_WAY',L2R,'the L swings through the Loop ↔ hot strip races the stands, same direction','The L through the Loop','Hot strip races the stands',{}),
 (['c-harrison-arrive'],['a-kover-pan','a-drama-wire'],'SAME_WAY',R2L,'the subway train sweeps the platform ↔ the pan along stacked billets, same direction','Train into Harrison','Billets sweep past',{}),
 (['c-94-skyline'],['a-ecsteel-train','a-inland-train'],'SAME_WAY',L2R,'the Chicago skyline ↔ the East Chicago smokestack skyline, both sliding the same way under a steel-blue sky','Skyline across the lot','Mill stacks from the train',{'lo':{'c-94-skyline':28.3}}),
 (['c-94-northside','c-94-loop'],['a-acroni-fast','a-drama-wire'],'SAME_WAY',R2L,'three-flats rush past the L ↔ the roller table rushes past: top speed, same direction','Back porches from the L','Roller table at speed',{}),
 (['c-cermak-arrive','c-harrison-arrive'],['a-drama-wire','a-kover-pan','a-servant-roll'],'SAME_WAY',None,'the train sweeps into Cermak ↔ wire rod whips past, same direction','Train into Cermak','Wire rod whips past',{'any_dir':True}),
 (['c-ic92-freight','c-impr-night-street'],['a-kover-fast','a-mills-roll','a-mills-fast'],'SAME_WAY',None,'the freight slides past under sodium ↔ hot strip slides through the stands, same direction','Freight under sodium','Strip through the stands',{'any_dir':True}),
 (['c-impr-night-street','c-gramaphone'],['a-mills-roll','a-servant-slab','a-kover-billets'],'SAME_WAY',None,'night street crowd drifts ↔ glowing stock drifts, same direction','Night street','Glowing stock drifts',{'any_dir':True}),
 (['c-impr-bus-lights','c-snow-plow','c-metra92-dusk'],['a-ssy-sparks','a-drama-sparks','a-vicart-sparks'],'MOLTEN_LIGHT',None,'headlights flare in the dark ↔ sparks shower off the furnace','Headlights flare','Sparks',{}),
 (['c-edison-sodium'],['a-kover-billets','a-servant-slab'],'SAME_WAY',L2R,'sodium side streets ↔ glowing billets on the line: the same orange, drifting the same way (zone 17 pair)','Home: sodium side streets','Billets cool on the line',{'lo':{'a-kover-billets':10.15}}),
 (['c-impr-shelter'],['a-servant-pour'],'STILL_GLOW',None,'the lit, empty shelter ↔ ingots cooling in the dark','Release: the empty shelter (holds)','Ingots cool',{'chi_freeze':True}),
]
assert len(PAIRS)==len(SH),f'{len(PAIRS)} pairs for {len(SH)} shots in the cut list'
def target(e): return {'sparse':'calm','break':'calm','release':'calm','groove':'mid','peak':'fast'}[e]
used={}
def windows(clip,dur,sec,dirn,freeze=False,lo=0.0,rule=None):
    if clip in BANNED: return []
    z=scan(clip); t=z['t']
    for sp in ([1.0] if freeze else [1.0,0.96,0.93,0.9]):
        span=min(dur*sp,3.0) if freeze else dur*sp; out=[]
        for a in t:
            if a+span>t[-1]: break
            if a<lo: continue
            if any(not(a+span<=u0 or a>=u1) for u0,u1 in used.get(clip,[])): continue
            if any(a-0.08<=c<=a+span+0.05 for c in clip_cuts(clip)["cuts"]): continue   # full-fps hard cut / flash inside
            s=window_stats(clip,a,span)
            if quality_fail(s): continue
            if dirn is not None and not(np.sign(s['mdx'])==dirn and abs(s['mdx'])>=8): continue
            sc={'calm':-s['flow'],'mid':-abs(s['flow']-10),'fast':s['flow']}[target(sec)]+(0.3*abs(s['mdx']) if dirn else 0)+(0.3*s['warm'] if rule in ('STILL_GLOW','MOLTEN_LIGHT') else 0)
            out.append((sc,float(a),sp,span,s))
        if out: return sorted(out,key=lambda x:-x[0])
    return []
pairs=[]; chi=[]; ctr=[]
for sh,(chis,ctrs,rule,dirn,link,beat_c,beat_k,opt) in zip(SH,PAIRS):
    sec=sh['energy']; dur=(sh['t1']-sh['t0'])+PAD
    assert rule in RULES,rule
    opts={}
    for side,cands,freeze in (('chi',chis,opt.get('chi_freeze',False)),('ctr',ctrs,False)):
        opts[side]=[(c,w) for c in sorted(cands,key=lambda c:c in used) for w in windows(c,dur,sec,dirn,freeze,opt.get('lo',{}).get(c,0.0),rule)[:60]]
    best=None
    for ci,(cc,cw) in enumerate(opts['chi']):
        for ki,(kc,kw) in enumerate(opts['ctr']):
            ok,why=RULES[rule]['check'](CAT[cc],CAT[kc],cw[4],kw[4])
            if ok:
                rank=ci+ki+(100 if cc in used else 0)+(100 if kc in used else 0)+10*chis.index(cc)+10*ctrs.index(kc)
                if best is None or rank<best[0]: best=(rank,cc,cw,kc,kw,why)
    if not best: print("chi opts",[(c,round(w[1],2)) for c,w in opts["chi"]][:5],"ctr opts",[(c,round(w[1],2),round(w[4]["flow"],1),round(w[4]["warm"],1)) for c,w in opts["ctr"]][:8]); sys.exit(f"shot {sh['n']}: no window pair satisfies {rule} for {chis} / {ctrs}")
    _,cc,cw,kc,kw,why=best; sides=[]
    for c,(sc,a,sp,span,st),freeze in ((cc,cw,opt.get('chi_freeze',False)),(kc,kw,False)):
        used.setdefault(c,[]).append((a-0.1,a+span+0.2))
        d=dict(shot=sh['n'],clip=c,src_in=round(a,3),speed=sp,src_span=round(span,3),stats={k:(round(v,2) if isinstance(v,float) else v) for k,v in st.items()},
               world=CAT[c]['world'],pace=CAT[c]['pace'])
        if freeze: d['freeze']=round(span,3)
        sides.append(d)
    chi.append(sides[0]); ctr.append(sides[1])
    pairs.append(dict(shot=sh['n'],bar0=sh['bar0'],bars=sh['bars'],t0=sh['t0'],t1=sh['t1'],energy=sec,hits=sh['hits'],why=sh['why'],
                      rule=rule,rule_name=RULES[rule]['name'],link=link,evidence=why,chi=sides[0]['clip'],ctr=sides[1]['clip'],chi_beat=beat_c,ctr_beat=beat_k))
ARC=("One rider's trip mirrored by one heat of steel. Chicago: the city at rest → waiting in the rain → the bus arrives on the drums → boarding → "
     "pulling away down the sodium strip → (drums out: the ride starts quietly, wipers, sodium) → (break: feet in the puddle) → the drop: the ride across the city by train, L and "
     "subway at full speed → back through the sodium side streets → the empty shelter. Steel: the furnace idles → the ladle fills → the slab enters the rolls → tap and hot bar → "
     "forge and tap → (break: the run-out slows) → the mill at full speed → billets cool on the line → ingots cool in the dark.")
json.dump(dict(fps=FPS,cutlist=C['shots'],arc=ARC,pairs=pairs,chi=chi,ctr=ctr),open('edl_v3.json','w'),indent=1,ensure_ascii=False)
for p,c,k in zip(pairs,chi,ctr):
    print(f"#{p['shot']:>2} {p['t0']:6.2f} {p['energy']:<7} {','.join(p['hits'])[:22]:<22} {p['rule']:<13} {c['clip']:<20} {c['src_in']:<6} x{c['speed']} | {k['clip']:<18} {k['src_in']:<6} x{k['speed']} :: {p['evidence'][:60]}")
