"""Stage 2 - moments. Usage: .venv/bin/python moments.py AUDIO beats.json OUT/moments.json
Scores every detected downbeat for "this merits a visual shift", using the Demucs stems and the bars from beats.json.
Signals per bar: loudness (mix, drums, bass, vocals, in dB), drum presence, kick/snare onsets on the drum stem,
fills (dense drum hits in the last third of the previous bar), self-similarity novelty (Foote kernel, one bar wide,
on chroma+MFCC), vocal entries. Novelty peaks are snapped to the nearest downbeat (they smear ~0.1-0.2 s late).
Labels: drums_in, drums_out, drop, break, release, vocal_in (top); fill_landing, section (high); change (med).
Also writes an energy level per bar (sparse / groove / peak, plus break and release spans) for the cut-list stage."""
import argparse,json,os,sys,numpy as np
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from common import *
TOP={'drums_in','drums_out','drop','break','release','vocal_in'}; HIGH={'fill_landing','section'}
def run(audio,beats_json,out_json,quiet=False):
    import librosa,scipy.signal as ss
    from scipy.ndimage import uniform_filter1d
    B=json.load(open(beats_json)); wd=work_dir(audio); wav=to_wav(audio,os.path.join(wd,'mix.wav')); st=stems(wav,wd)
    D=np.array([d['t'] for d in B['downbeats']]); T=B['duration']; E=np.r_[D,T]; n=len(D)
    sr=22050; hop=512; fr=sr/hop
    y=librosa.load(wav,sr=sr)[0]; Y={k:librosa.load(p,sr=sr)[0] for k,p in st.items()}
    rms=lambda x:20*np.log10(librosa.feature.rms(y=x,hop_length=hop)[0]+1e-6)
    R={'mix':rms(y),**{k:rms(v) for k,v in Y.items()}}; t=np.arange(len(R['mix']))/fr
    def bar_db(k,i): m=(t>=E[i])&(t<E[i+1]); return float(np.mean(R[k][m])) if m.any() else -120.0
    db={k:np.array([bar_db(k,i) for i in range(n)]) for k in R}
    # novelty
    C=librosa.feature.chroma_cqt(y=y,sr=sr,hop_length=hop); M=librosa.feature.mfcc(y=y,sr=sr,hop_length=hop,n_mfcc=13)
    X=uniform_filter1d(np.vstack([librosa.util.normalize(C,axis=0),0.7*librosa.util.normalize(M[1:],axis=1)]),max(1,int(fr*0.33)),axis=1)
    S=np.corrcoef(X.T); N=S.shape[0]; bar=float(np.median(np.diff(D))) if n>1 else 2.0; L=max(4,int(fr*bar))
    g=np.outer(ss.windows.gaussian(2*L,L/2),ss.windows.gaussian(2*L,L/2)); K=np.kron([[1,-1],[-1,1]],np.ones((L,L)))*g
    Sp=np.pad(S,L,mode='edge'); nov=np.array([(Sp[i:i+2*L,i:i+2*L]*K).sum() for i in range(N)]); nov=np.maximum(nov,0)/max(nov.max(),1e-9)
    pk,_=ss.find_peaks(nov,height=0.25,distance=int(fr*bar*0.75)); nov_at=np.zeros(n)
    for p in pk:
        j=int(np.argmin(np.abs(D-t[min(p,len(t)-1)])))
        if abs(D[j]-t[min(p,len(t)-1)])<=0.5*bar: nov_at[j]=max(nov_at[j],nov[p])
    # drums
    H=drum_hits(st['drums']); kt,ks=H['kick']; stt,sts=H['snare']; at,as_=H['all']
    hits=np.r_[kt[ks>=0.3],stt[sts>=0.3]]
    late=np.array([((hits>=E[i+1]-(E[i+1]-E[i])/3)&(hits<E[i+1]-0.03)).sum() for i in range(n)])
    tot=np.array([((hits>=E[i])&(hits<E[i+1]-0.03)).sum() for i in range(n)])
    floor=np.percentile(db['drums'],10)
    # drums present: a real pattern of hits, or the stem clearly above its own floor (soft or bleedy drum stems)
    drums_on=(tot>=3)|(db['drums']>=floor+6)
    def seg_db(k,a,b): m=(t>=a)&(t<b); return float(np.mean(R[k][m])) if m.any() else -120.0
    late_db=np.array([seg_db('drums',E[i+1]-(E[i+1]-E[i])/3,E[i+1]-0.02) for i in range(n)])
    ref_late=np.median(late_db[drums_on]) if drums_on.any() else 0.0
    mx=db['mix'].max()
    voc_on=db['vocals']>db['vocals'].max()-15 if db['vocals'].max()>-45 else np.zeros(n,bool)
    typical_late=np.median(late[drums_on]) if drums_on.any() else 0
    out=[]; last_big_drop=None
    for i in range(n):
        lab=[]; why=[]
        d_mix=db['mix'][i]-db['mix'][i-1] if i else 0.0
        if i and drums_on[i] and not drums_on[i-1]: lab.append('drums_in'); why.append(f"drum stem {db['drums'][i-1]:.0f}→{db['drums'][i]:.0f} dB")
        if i and not drums_on[i] and drums_on[i-1]: lab.append('drums_out'); why.append(f"drum stem {db['drums'][i-1]:.0f}→{db['drums'][i]:.0f} dB")
        if i and d_mix>=6 and db['mix'][i]>=mx-6: lab.append('drop'); why.append(f"mix {d_mix:+.1f} dB")
        if i and d_mix<=-5 and db['mix'][i-1]>=mx-9: lab.append('break'); why.append(f"mix {d_mix:+.1f} dB"); last_big_drop=i
        if i and voc_on[i] and not voc_on[i-1]: lab.append('vocal_in')
        if i and drums_on[i-1] and ((late[i-1]>=3 and late[i-1]>=typical_late+2) or late_db[i-1]-ref_late>=4):
            lab.append('fill_landing'); why.append(f"fill in previous bar: {late[i-1]} late hits, late drum level {late_db[i-1]-ref_late:+.1f} dB vs typical")
        if nov_at[i]>=0.5: lab.append('section'); why.append(f"novelty {nov_at[i]:.2f}")
        elif nov_at[i]>=0.3 or (i and abs(d_mix)>=3): lab.append('change'); why.append(f"novelty {nov_at[i]:.2f}, mix {d_mix:+.1f} dB")
        kick=strength_near(D[i],kt,ks,0.05); sn_db=strength_near(D[i],stt,sts,0.05)
        mid=E[i]+(E[i+1]-E[i])/2; sn_mid=strength_near(mid,stt,sts,0.06)
        score=3*bool(TOP&set(lab))+2*bool(HIGH&set(lab))+1*('change' in lab)+nov_at[i]+0.15*abs(d_mix)+0.5*kick
        rank='top' if TOP&set(lab) else 'high' if HIGH&set(lab) else 'med' if lab else None
        out.append(dict(i=i,t=round(float(D[i]),4),labels=lab,rank=rank,score=round(float(score),3),why='; '.join(why),
                        novelty=round(float(nov_at[i]),3),mix_db=round(float(db['mix'][i]),1),drums_db=round(float(db['drums'][i]),1),
                        drums=bool(drums_on[i]),fill_hits=int(late[i-1]) if i else 0,kick=round(kick,2),
                        snare=round(sn_db,2),mid_t=round(float(mid),4),mid_snare=round(sn_mid,2)))
    # release: the last break-type drop in the final quarter is relabelled release
    if last_big_drop is not None and D[last_big_drop]>0.75*T:
        m=out[last_big_drop]; m['labels']=['release' if l=='break' else l for l in m['labels']]
    # energy per bar
    lvl=[]
    for i in range(n):
        if db['mix'][i]>=mx-3.5 and drums_on[i]: lvl.append('peak')
        elif db['mix'][i]<mx-9 or (not drums_on[i] and db['mix'][i]<mx-6): lvl.append('sparse')
        else: lvl.append('groove')
    for i,m in enumerate(out):
        if 'break' in m['labels']:
            j=i
            while j<n and not (set(out[j]['labels'])&{'drop','drums_in'} and j>i): lvl[j]='break'; j+=1
        if 'release' in m['labels']:
            for j in range(i,n): lvl[j]='release'
    for i,m in enumerate(out): m['energy']=lvl[i]
    jdump(dict(audio=os.path.abspath(audio),beats=os.path.abspath(beats_json),duration=T,moments=out,
               novelty_curve=dict(t=[round(float(x),3) for x in t[::4]],v=[round(float(x),3) for x in nov[::4]])),out_json)
    if not quiet:
        for m in out:
            if m['rank']: print(f"{m['t']:7.3f} {m['rank']:<4} {m['energy']:<7} {','.join(m['labels']):<28} {m['why']}")
    return out
if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('audio'); ap.add_argument('beats'); ap.add_argument('out'); a=ap.parse_args()
    run(a.audio,a.beats,a.out)
