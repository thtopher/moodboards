"""Stage 1 - beats. Usage: .venv/bin/python beats.py AUDIO OUT/beats.json [--override override.json]

Works on any audio (studio mix, live recording, the audio track of a rendered MP4). Stores real event times only:
no BPM and no fixed grid, so tempo drift and irregular bars in a live set are kept as they are.

1. Pulses: Beat This! (final0) beat times on the full mix, gaps filled locally, each nudged onto the nearest strong
   onset within 25 ms.
2. Downbeat evidence for every pulse, from seven independent hypotheses plus the drums:
   Beat This! downbeat probability on the mix and on the Demucs drum stem; madmom RNN downbeat activation; madmom DBN
   tracks with 2, 3, 4 and 6 beats per bar and the joint 2/3/4/6 model (votes); and the drum accent
   (kick 20-150 Hz + snare 1.5-5 kHz onsets on the drum stem), which breaks ties when the trackers disagree on phase.
3. Bars: dynamic programming over pulses. Bars of the dominant length cost nothing; any other length (an irregular bar)
   costs a penalty, so the phase only jumps when the evidence clearly says so.
4. Confidence per downbeat = votes x margin over the other phases of the same bar; low-confidence bars are listed.
5. Optional override file (hand corrections, applied last):
   {"bar_pulses": 6, "add": [t, ...], "remove": [t, ...], "shift": [{"from": t0, "to": t1, "pulses": k}]}"""
import argparse,json,os,subprocess,sys,numpy as np
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from common import *
W_EVID=dict(bt=1.0,btd=0.5,mm=0.7,acc=0.6,votes=0.8); P_IRR=1.6

def beat_this(paths):
    import torch
    from beat_this.inference import Audio2Beats
    from beat_this.preprocessing import load_audio
    a2b=Audio2Beats(checkpoint_path='final0',device='cpu',dbn=False); out={}
    for k,p in paths.items():
        sig,sr=load_audio(p)
        with torch.no_grad(): bl,dl=Audio2Frames_call(a2b,sig,sr)
        b,d=a2b.frames2beats(bl,dl)
        out[k]=dict(beats=np.array(b),downbeats=np.array(d),blog=bl.cpu().numpy(),dlog=dl.cpu().numpy())
    return out
def Audio2Frames_call(a2b,sig,sr):
    from beat_this.inference import Audio2Frames
    return Audio2Frames.__call__(a2b,sig,sr)
def madmom(wav,wd):
    out=os.path.join(wd,'madmom.npz')
    if not os.path.exists(out): subprocess.run([PYMM,os.path.join(HERE,'mm_dbn.py'),wav,out],check=True,capture_output=True)
    z=np.load(out); return {k:z[k] for k in z.files}
def fill_gaps(t):
    t=list(t); i=1
    while i<len(t):
        loc=np.median(np.diff(t[max(0,i-8):i+8])) if len(t)>3 else t[i]-t[i-1]
        g=t[i]-t[i-1]
        if g>1.6*loc:
            n=int(round(g/loc)); t[i:i]=[t[i-1]+g*k/n for k in range(1,n)]; i+=n-1
        i+=1
    return np.array(t)
def frame_max(logit,t,fps,win):
    i=int(round(t*fps)); a,b=max(0,i-win),min(len(logit),i+win+1)
    return float(logit[a:b].max()) if b>a else 0.0
sig=lambda x:1/(1+np.exp(-x))

def run(audio,out_json,override=None,root=None,quiet=False):
    wd=work_dir(audio,root); wav=to_wav(audio,os.path.join(wd,'mix.wav')); st=stems(wav,wd)
    bt=beat_this({'mix':wav,'drums':st['drums']}); mm=madmom(wav,wd); hits=drum_hits(st['drums'])
    # 1. pulses
    P=fill_gaps(bt['mix']['beats'])
    y=load(wav); env=band_flux(y,30,16000); et=np.arange(len(env))*HOP/SR
    refined=[]
    for t in P:
        m=np.abs(et-t)<=0.025
        if m.any() and env[m].max()>3*np.median(env[np.abs(et-t)<=0.3]+1e-9): t=float(et[m][np.argmax(env[m])])
        refined.append(t)
    P=np.array(refined); n=len(P); ibi=np.median(np.diff(P))
    # 2. evidence
    hyps={'bt_mix':bt['mix']['downbeats'],'bt_drums':bt['drums']['downbeats']}
    for k in ('mm2','mm3','mm4','mm6','mmall'):
        r=mm[k]; hyps[k]=r[r[:,1]==1,0] if len(r) else np.zeros(0)
    def to_idx(D):
        s=set()
        for d in D:
            j=int(np.argmin(np.abs(P-d)))
            if abs(P[j]-d)<=0.4*ibi: s.add(j)
        return s
    HI={k:to_idx(v) for k,v in hyps.items()}
    kt,ks=hits['kick']; stt,sts=hits['snare']
    acc=np.array([strength_near(t,kt,ks)+0.5*strength_near(t,stt,sts) for t in P]); acc=acc/max(np.percentile(acc,95),1e-9)
    ev=dict(bt=np.array([sig(frame_max(bt['mix']['dlog'],t,50,2)) for t in P]),
            btd=np.array([sig(frame_max(bt['drums']['dlog'],t,50,2)) for t in P]),
            mm=np.array([frame_max(mm['act'][:,1],t,100,3) for t in P]),
            acc=np.clip(acc,0,1.5),
            votes=np.array([sum(i in HI[k] for k in HI)/len(HI) for i in range(n)]))
    S=sum(W_EVID[k]*ev[k] for k in W_EVID)
    # bar length in pulses: mode of Beat This downbeat spacing, cross-checked by the madmom DBN meters
    def gaps(ix):
        ix=sorted(ix); return [b-a for a,b in zip(ix,ix[1:]) if 1<b-a<=16]
    cand={}
    for k,ix in HI.items():
        g=gaps(ix)
        if g: v,c=np.unique(g,return_counts=True); cand[k]=int(v[np.argmax(c)])
    ov=json.load(open(override)) if override else {}
    B=int(ov.get('bar_pulses') or cand.get('bt_mix') or cand.get('mmall') or 4)
    # 3. DP over pulses
    alts=[k for k in range(max(2,B-3),B+4) if k!=B]
    dp=np.full(n,-1e9); bp=np.full(n,-1)
    for i in range(n):
        best,arg=(0.0,-1) if i<B+3 else (-1e9,-1)
        for k,pen in [(B,0.0)]+[(k,P_IRR) for k in alts]:
            j=i-k
            if j>=0 and dp[j]-pen>best: best,arg=dp[j]-pen,j
        dp[i]=S[i]+best; bp[i]=arg
    end=int(np.argmax(dp[max(0,n-B-3):]))+max(0,n-B-3); D=[]
    while end>=0: D.append(end); end=bp[end]
    D=sorted(D)
    # overrides
    edits=[]
    for sh in ov.get('shift',[]):
        D=[d+sh['pulses'] if sh['from']<=P[d]<=sh['to'] else d for d in D]; edits.append(sh)
    for t in ov.get('remove',[]):
        D=[d for d in D if abs(P[d]-t)>0.4*ibi]; edits.append({'remove':t})
    for t in ov.get('add',[]):
        D=sorted(set(D)|{int(np.argmin(np.abs(P-t)))}); edits.append({'add':t})
    D=[d for d in sorted(set(D)) if 0<=d<n]
    # 4. confidence
    dbs=[]
    for d in D:
        alt=[S[d+k] for k in range(-(B-1),B) if k and 0<=d+k<n]
        margin=S[d]-max(alt) if alt else 1.0
        votes={k:(d in HI[k]) for k in HI}
        conf=float(np.clip(0.5*np.mean(list(votes.values()))+0.5*sig(3*margin),0,1))
        dbs.append(dict(t=round(float(P[d]),4),pulse=int(d),conf=round(conf,3),margin=round(float(margin),3),votes=votes,
                        evidence={k:round(float(ev[k][d]),3) for k in ev}))
    bars=[]
    for a,b in zip(D,D[1:]+[n]):
        bars.append(dict(i=len(bars),t0=round(float(P[a]),4),t1=round(float(P[b]),4) if b<n else round(float(len(y)/SR),4),
                         pulses=int(b-a),regular=None))
    # a bar is irregular when its DURATION departs from the local bar length (drift-tolerant: median of the 8 nearest bars);
    # a wrong pulse count at normal duration is a pulse-layer glitch, reported separately
    dur=np.array([x['t1']-x['t0'] for x in bars[:-1]])
    for k,x in enumerate(bars[:-1]):
        loc=np.median(dur[max(0,k-4):k+5]); x['regular']=bool(abs(dur[k]/loc-1)<=0.15)
        x['pulse_glitch']=bool(x['regular'] and x['pulses']!=B)
    irregular=[x for x in bars[:-1] if not x['regular']]
    low=[x for x in dbs if x['conf']<0.5]
    res=dict(audio=os.path.abspath(audio),sha=sha(audio),duration=round(len(y)/SR,4),
             bar_pulses=B,bar_pulse_candidates=cand,
             pulses=[round(float(t),4) for t in P],downbeats=dbs,bars=bars,
             irregular_bars=[dict(i=x['i'],t0=x['t0'],t1=x['t1'],pulses=x['pulses']) for x in irregular],
             pulse_glitch_bars=[x['i'] for x in bars[:-1] if x.get('pulse_glitch')],
             low_confidence=[dict(t=x['t'],conf=x['conf']) for x in low],overrides=edits,
             method='pulses: Beat This! mix (onset-refined); bars: DP over Beat This!/madmom 2-3-4-6/drum-accent evidence')
    jdump(res,out_json)
    if not quiet:
        print(f"{audio}: {n} pulses, {len(dbs)} downbeats, {B} pulses/bar (candidates {cand}), "
              f"{len(irregular)} irregular bars, {len(low)} low-confidence downbeats")
    return res
if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('audio'); ap.add_argument('out'); ap.add_argument('--override'); a=ap.parse_args()
    run(a.audio,a.out,a.override)
