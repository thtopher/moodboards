"""Automated gate for the music-synced split screen. Exit code 1 on any FAIL.
EDL checks:  every cut on both panels is a bar downbeat frame (librosa grid -> 24 fps), panels cut on identical frames,
             cut rate matches the section plan, every pair declares a grammar rule and that rule's check passes on the
             catalog tags + the measured on-screen window, no banned clip, every window passes the quality gates.
Render checks (if the mp4 exists): frame count, a visible cut on BOTH halves at every declared cut frame,
             no black or blown-out frames on either half; undeclared hard cuts are reported."""
import json,sys,subprocess,numpy as np
from grammar import grid,SECTIONS,section_of,RULES,BANNED,window_stats,quality_fail,catalog,FPS,ROOT
EDL=sys.argv[1] if len(sys.argv)>1 else 'edl_v2.json'
MP4=sys.argv[2] if len(sys.argv)>2 else ROOT+'/edits/music_split_v2.mp4'
A,DF=grid(); CAT=catalog(); e=json.load(open(EDL)); END=DF[-1]; DSET=set(DF)
fails=[]; warns=[]; ok=[]
def F(m): fails.append(m)
# 1. grid + lockstep
for side in ('chi','ctr'):
    L=e[side]
    if L[0]['f0']!=0 or L[-1]['f1']!=END: F(f'{side}: does not span frame 0..{END}')
    for a,b in zip(L,L[1:]):
        if a['f1']!=b['f0']: F(f"{side}: gap/overlap at frame {a['f1']}/{b['f0']}")
    for s in L:
        if s['f0'] not in DSET or s['f1'] not in DSET: F(f"{side} {s['clip']}: cut at frame {s['f0']}/{s['f1']} is not a bar downbeat")
        if (s['f0'],s['f1'])!=(DF[s['bar']],DF[s['bar']+s['bars']]): F(f"{side} {s['clip']}: frames do not match bar {s['bar']+1}")
cuts={side:[s['f0'] for s in e[side]][1:] for side in ('chi','ctr')}
if cuts['chi']!=cuts['ctr']: F(f"panels out of sync: {sorted(set(cuts['chi'])^set(cuts['ctr']))}")
else: ok.append(f"{len(cuts['chi'])} cuts per panel, identical frames on both panels, all on bar downbeats: {cuts['chi']}")
# 2. section cut rate
for p in e['pairs']:
    sec,sa,sb,step=section_of(p['bar'])
    if not(p['bars']==step or p['bar']+p['bars']==len(DF)-1): F(f"bar {p['bar']+1}: {p['bars']}-bar shot in {sec} (plan: {step})")
# 3. grammar
by={(s['bar']):s for s in e['chi']}; bk={(s['bar']):s for s in e['ctr']}
for p in e['pairs']:
    c,k=by.get(p['bar']),bk.get(p['bar'])
    if not c or not k: F(f"bar {p['bar']+1}: missing a panel"); continue
    if p.get('rule') not in RULES or not p.get('link'): F(f"bar {p['bar']+1}: no declared link rule"); continue
    st=[]
    for s in (c,k):
        if s['clip'] in BANNED: F(f"bar {p['bar']+1}: banned clip {s['clip']} ({BANNED[s['clip']]})")
        w=window_stats(s['clip'],s['src_in'],s['src_span']); q=quality_fail(w)
        if q: F(f"bar {p['bar']+1} {s['clip']}@{s['src_in']}: "+'; '.join(q))
        if not(0.85<=s['speed']<=1.0): F(f"bar {p['bar']+1} {s['clip']}: speed {s['speed']} outside 0.85-1.0")
        st.append(w)
    good,why=RULES[p['rule']]['check'](CAT[c['clip']],CAT[k['clip']],st[0],st[1])
    (ok.append if good else F)(f"bar {p['bar']+1:>2} {p['rule']:<14} {c['clip']} ↔ {k['clip']}: {why}")
# 4. render
try:
    W,H=480,135
    raw=subprocess.run(['ffmpeg','-v','error','-i',MP4,'-vf',f'scale={W}:{H},format=gray','-f','rawvideo','-'],capture_output=True,check=True).stdout
    V=np.frombuffer(raw,np.uint8).reshape(-1,H,W).astype(np.float32)
    if len(V)!=END: F(f'render has {len(V)} frames, expected {END}')
    gl=round(952/1920*W); gr=round(968/1920*W)
    for name,P in (('left (Chicago)',V[:,:,:gl]),('right (counter-world)',V[:,:,gr:])):
        d=np.r_[0,np.abs(np.diff(P,axis=0)).mean(axis=(1,2))]; lm=P.mean(axis=(1,2))
        missed=[]
        for f in cuts['chi']:
            nb=np.r_[d[max(1,f-12):f-1],d[f+1:f+12]]
            if not (d[f]>max(1.8*np.median(nb),4.0) and d[f]>=d[max(1,f-3):f+4].max()): missed.append((f,round(float(d[f]),1),round(float(np.median(nb)),1)))
        if missed: F(f'{name}: declared cut not visible at frames {missed}')
        else: ok.append(f'render {name}: visible cut at all {len(cuts["chi"])} declared frames')
        und=[f for f in range(2,len(d)-1) if f not in cuts['chi'] and d[f]>max(4*np.median(d[max(1,f-12):f+12]),12)]
        if und: warns.append(f'{name}: undeclared hard changes at frames {und} (t={[round(f/FPS,2) for f in und]})')
        blk=np.where(lm<8)[0]; bo=np.where(lm>215)[0]
        if len(blk): F(f'{name}: {len(blk)} black frames, e.g. {blk[:8].tolist()}')
        if len(bo): F(f'{name}: {len(bo)} blown-out frames, e.g. {bo[:8].tolist()}')
        ok.append(f'render {name}: luma min {lm.min():.0f}, max {lm.max():.0f} (gates 8/215)')
except FileNotFoundError: warns.append('no render to check')
for m in ok: print('PASS',m)
for m in warns: print('WARN',m)
for m in fails: print('FAIL',m)
print('RESULT:', 'FAIL' if fails else 'PASS', f'({len(fails)} fail, {len(warns)} warn)')
sys.exit(1 if fails else 0)
