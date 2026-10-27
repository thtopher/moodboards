"""Stage 3 - cut list. Usage: .venv/bin/python cutlist.py beats.json moments.json OUT/cutlist.json [--config cfg.json]
Rules (all cuts are detected downbeats; both panels share one cut list, so they always cut in sync):
  1. Anchors: every 'top' moment and every 'high' moment (config anchor_ranks) is a mandatory cut.
  2. Between two anchors, the base cut rate of the energy level applies (bars_per_shot: sparse 4 / groove 2 /
     break 1 / peak 1 / release = hold to the end). The span is split into the fewest whole-bar shots that respect it;
     among equal splits the one whose cut points carry the most moment score wins (med moments, novelty, kick).
  3. min_shot_bars (default 1): an anchor that would make a shorter shot is dropped (lower score loses).
  4. Lead: frames are emitted for each lead in config leads; frame = round(t*fps) - lead (first frame stays 0).
  5. Half-bar snare cut (optional, off by default): only inside 'peak', only on a bar whose mid-bar snare is the
     strongest hit of the bar and clearly above the downbeat; it is marked half_bar and reported."""
import argparse,json,os,sys,itertools,numpy as np
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from common import jdump
DEFAULT=dict(fps=24,bars_per_shot=dict(sparse=4,groove=2,brk=1,peak=1,release=0),anchor_ranks=['top','high'],
             min_shot_bars=1,leads=[0,1,2],half_bar=False)
def run(beats_json,moments_json,out_json,cfg=None,quiet=False):
    C=dict(DEFAULT,**(cfg or {})); B=json.load(open(beats_json)); M=json.load(open(moments_json))['moments']
    D=[m['t'] for m in M]; n=len(D); T=B['duration']; fps=C['fps']
    step=lambda e:C['bars_per_shot']['brk' if e=='break' else e]
    anchors=[0]+[m['i'] for m in M if m['rank'] in C['anchor_ranks'] and m['i']>0]
    # min shot: drop the weaker of two anchors closer than min_shot_bars
    keep=[anchors[0]]
    for a in anchors[1:]:
        if a-keep[-1]<C['min_shot_bars']:
            if M[a]['score']>M[keep[-1]]['score'] and keep[-1]!=0: keep[-1]=a
        else: keep.append(a)
    anchors=keep+[n]
    cuts=[]
    for a,b in zip(anchors[:-1],anchors[1:]):
        e=M[a]['energy']; s=step(e)
        if s==0 or b-a<=s: cuts.append(a); continue
        k=-(-(b-a)//s)                      # fewest shots
        best=None
        for inner in itertools.combinations(range(a+1,b),k-1):
            pts=(a,)+inner+(b,)
            if max(np.diff(pts))>s: continue
            sc=sum(M[i]['score'] for i in inner)-0.01*np.std(np.diff(pts))
            if best is None or sc>best[0]: best=(sc,pts)
        cuts+=list(best[1][:-1])
    shots=[]
    for j,a in enumerate(cuts):
        b=cuts[j+1] if j+1<len(cuts) else n
        t0=D[a] if a>0 else 0.0; t1=D[b] if b<n else T
        m=M[a]
        sh=dict(n=j,bar0=a,bar1=b,bars=b-a,t0=round(t0,4),t1=round(t1,4),energy=m['energy'],
                hits=(m['labels'] or ['base']) if a>0 else ['start'],rank=m['rank'] if a>0 else None,why=m['why'] if a>0 else '',
                frames={str(L):[max(0,round(t0*fps)-L) if a>0 else 0, round(t1*fps)-L if b<n else round(T*fps)] for L in C['leads']})
        shots.append(sh)
    half=[]
    # half-bar snare exception: evaluated always, applied only if config half_bar is on. A peak bar qualifies only
    # if its mid-bar snare clearly beats the downbeat (>=0.8 and >=1.3x the stronger of kick/snare on the downbeat).
    cand=[dict(bar=m['i'],t=m['mid_t'],mid_snare=m['mid_snare'],downbeat=max(m['kick'],m['snare'])) for m in M
          if m['energy']=='peak' and m['mid_snare']>=0.8 and m['mid_snare']>=1.3*max(m['kick'],m['snare'])]
    if C['half_bar']: half=cand
    out_half_eval=dict(qualifying=cand,peak_mid_snare=[m['mid_snare'] for m in M if m['energy']=='peak'])
    out=dict(config=C,beats=os.path.abspath(beats_json),moments=os.path.abspath(moments_json),duration=T,end_frame=round(T*fps),
             downbeats=D,shots=shots,half_bar_cuts=half,half_bar_eval=out_half_eval)
    jdump(out,out_json)
    if not quiet:
        for s in shots: print(f"{s['n']:>2} bar {s['bar0']:>2}-{s['bar1']:<2} {s['t0']:7.3f}-{s['t1']:<7.3f} {s['energy']:<7} {','.join(s['hits']):<30} f(lead1)={s['frames']['1']}")
    return out
if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('beats'); ap.add_argument('moments'); ap.add_argument('out'); ap.add_argument('--config')
    a=ap.parse_args(); run(a.beats,a.moments,a.out,json.load(open(a.config)) if a.config else None)
