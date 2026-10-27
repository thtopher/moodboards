"""Non-circular render check. Usage:
  .venv/bin/python check_render.py RENDER.mp4 cutlist.json MUSIC.wav --lead L [--splices splices.json] [--panels 0:952,968:1920] [--out report.json]
Nothing is trusted from the cut list's own grid. It
  1. extracts the MP4's audio (honoring the AAC priming edit list) and re-runs beats.run() on it from scratch;
  2. finds every hard cut in each panel from the video pixels (frame-difference spikes), and requires every panel to
     cut on the same frames as the plan (lockstep, nothing missing, nothing extra);
  3. for each cut frame f, measures (f+lead)/fps against the nearest re-detected downbeat; FAIL if > 1 frame off,
     unless it is within 1 frame of a ranked moment re-scored on the render audio (moments are snapped to downbeats,
     so in practice both mean the same grid);
  4. music edit: every splice joint must sit within 1 frame of a re-detected downbeat; FAIL on any irregular bar
     (duration off the local median by >15%); FAIL on a low-end (<150 Hz) dip at a joint deeper than the source
     has at the same two downbeats (+3 dB tolerance);
  5. music-only audio: exactly one audio stream; aligned lag 0 (+-1 sample) against MUSIC.wav; fitted gain within
     +-0.5 dB of unity; null residual <= -20 dB overall and <= -12 dB in every 1 s window with music above -50 dBFS;
     length within 1 frame. Any clip audio, ambience, ducking or loudness processing fails this.
Exit code 1 on any FAIL."""
import argparse,json,os,subprocess,sys,numpy as np
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from common import *
import beats as BEATS
def decode(path,sr=48000,ch=2):
    raw=subprocess.run(['ffmpeg','-v','error','-i',path,'-map','0:a:0','-ac',str(ch),'-ar',str(sr),'-f','f32le','-'],capture_output=True,check=True).stdout
    return np.frombuffer(raw,np.float32).reshape(-1,ch)
def spike_cuts(d,floor=20.0,ratio=1.5):
    """Hard cuts from a frame-difference series: a one-frame spike well above both neighbours."""
    return [i for i in range(1,len(d)) if d[i]>=floor and d[i]>=ratio*max(d[i-1],d[i+1] if i+1<len(d) else 0)]
def is_hard_cut(P,f):
    """Tell a hard cut from a motion spike (wiper sweep, flame flicker, fast pan): a cut changes the luma
    histogram (L1 >= 0.25) AND the new picture persists (frame f+2 is >= 1.5x closer to f than to f-1, and
    symmetrically f-2 is closer to f-1 than to f+1)."""
    if f<2 or f+2>=len(P): return True
    h=lambda i:(lambda x:x/x.sum())(np.histogram(P[i],32,(0,256))[0].astype(float))
    mad=lambda a,b:np.abs(P[a]-P[b]).mean()+1e-3
    pers=min(mad(f+2,f-1)/mad(f+2,f),mad(f-2,f+1)/mad(f-2,f-1))
    return np.abs(h(f)-h(f-1)).sum()>=0.25 and pers>=1.5
def video_cuts(mp4,panels,fps):
    w,h=[int(x) for x in subprocess.run(['ffprobe','-v','error','-select_streams','v:0','-show_entries','stream=width,height','-of','csv=p=0',mp4],capture_output=True,text=True).stdout.strip().split(',')]
    sw,sh=w//4,h//4
    raw=subprocess.run(['ffmpeg','-v','error','-i',mp4,'-vf',f'scale={sw}:{sh},format=gray','-f','rawvideo','-'],capture_output=True,check=True).stdout
    V=np.frombuffer(raw,np.uint8).reshape(-1,sh,sw).astype(np.float32); out=[]
    for x0,x1 in panels:
        P=V[:,:,x0//4:x1//4]; d=np.r_[0,np.abs(np.diff(P,axis=0)).mean(axis=(1,2))]
        out.append((spike_cuts(d),d,P))
    return out,len(V)
def lowdip(y,sr,t):
    import scipy.signal as ss
    b,a=ss.butter(4,150/(sr/2)); l=ss.filtfilt(b,a,y)
    def db(a0,a1): s=l[max(0,int(a0*sr)):int(a1*sr)]; return 10*np.log10(np.mean(s**2)+1e-12)
    win=[db(t+k*0.05,t+k*0.05+0.05) for k in range(-2,4)]
    ctx=np.median([db(t+k*0.05,t+k*0.05+0.05) for k in range(-20,20)])
    return float(min(win)-ctx)
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('mp4'); ap.add_argument('cutlist'); ap.add_argument('music')
    ap.add_argument('--lead',type=int,required=True); ap.add_argument('--splices'); ap.add_argument('--panels',default=None); ap.add_argument('--out')
    a=ap.parse_args(); C=json.load(open(a.cutlist)); fps=C['config']['fps']; fr=1/fps
    fails=[]; R=dict(render=a.mp4,lead=a.lead)
    # 1. re-detect on the render's own audio
    wd=work_dir(a.mp4); wav=to_wav(a.mp4,os.path.join(wd,'mix.wav'))
    B=BEATS.run(wav,os.path.join(wd,'render_beats.json'),quiet=True)
    D=np.array([d['t'] for d in B['downbeats']])
    import moments as MOM
    Ms=MOM.run(wav,os.path.join(wd,'render_beats.json'),os.path.join(wd,'render_moments.json'),quiet=True)
    ranked=np.array([m['t'] for m in Ms if m['rank'] in ('top','high')])
    R['redetected']=dict(downbeats=len(D),bar_pulses=B['bar_pulses'],irregular_bars=B['irregular_bars'],low_confidence=B['low_confidence'])
    if B['irregular_bars']: fails.append(f"irregular bars in the render audio: {B['irregular_bars']}")
    # 2. cuts from pixels
    W=int(subprocess.run(['ffprobe','-v','error','-select_streams','v:0','-show_entries','stream=width','-of','csv=p=0',a.mp4],capture_output=True,text=True).stdout)
    panels=[tuple(map(int,p.split(':'))) for p in a.panels.split(',')] if a.panels else [(0,W)]
    pc,nfr=video_cuts(a.mp4,panels,fps)
    plan=[s['frames'][str(a.lead)][0] for s in C['shots'][1:]]
    R['motion_spikes']={}; hard=[]
    for k,(cuts,_,Pk) in enumerate(pc):
        miss=sorted(set(plan)-set(cuts)); extra=sorted(set(cuts)-set(plan))
        real=[f for f in extra if is_hard_cut(Pk,f)]; R['motion_spikes'][k]=[f for f in extra if f not in real]
        if miss: fails.append(f'panel {k}: planned cuts not found in the pixels at frames {miss}')
        if real: fails.append(f'panel {k}: unplanned hard cuts at frames {real}')
        hard.append(tuple(sorted(set(cuts)-set(R['motion_spikes'][k]))))
    if len(set(hard))>1: fails.append('panels do not cut on the same frames')
    rows=[]
    for s in C['shots'][1:]:
        f=s['frames'][str(a.lead)][0]; seen=all(f in c for c,_,_ in pc)
        t=(f+a.lead)/fps; j=int(np.argmin(np.abs(D-t))); off=t-D[j]
        mo=float(np.min(np.abs(ranked-t))) if len(ranked) else 9
        ok=seen and (abs(off)<=fr+1e-6 or mo<=fr+1e-6)
        rows.append(dict(shot=s['n'],frame=f,shown_at=round(f/fps,4),aimed_at=round(t,4),nearest_downbeat=round(float(D[j]),4),
                         offset_ms=round(off*1000,1),raw_offset_ms=round((f/fps-D[j])*1000,1),moment_ms=round(mo*1000,1) if mo<9 else None,
                         seen_in_pixels=seen,hits=s['hits'],ok=bool(ok)))
        if not ok: fails.append(f"cut {s['n']} at frame {f}: {off*1000:+.1f} ms from the nearest re-detected downbeat")
    R['cuts']=rows; R['video_frames']=nfr
    # 4. splices
    y=decode(a.mp4,44100,1)[:,0]
    if a.splices:
        Sp=json.load(open(a.splices)); src=decode(Sp['source'],44100,1)[:,0]; sj=[]
        for k,j in enumerate(Sp['joints_edit_t']):
            off=float(np.min(np.abs(D-j))); dip=lowdip(y,44100,j)
            s_out=Sp['segments'][k]['src_downbeat1']; s_in=Sp['segments'][k+1]['src_downbeat0']
            ref=min(lowdip(src,44100,s_out),lowdip(src,44100,s_in))
            ok=off<=fr and dip>=ref-3
            sj.append(dict(edit_t=j,downbeat_offset_ms=round(off*1000,1),low_dip_db=round(dip,1),source_low_dip_db=round(ref,1),ok=ok))
            if off>fr: fails.append(f'music splice at {j:.3f} s is {off*1000:.0f} ms off the re-detected downbeat')
            if dip<ref-3: fails.append(f'low-end hole at the splice at {j:.3f} s ({dip:.1f} dB vs source {ref:.1f} dB)')
        R['splices']=sj
    # 5. music only
    ns=subprocess.run(['ffprobe','-v','error','-select_streams','a','-show_entries','stream=index','-of','csv=p=0',a.mp4],capture_output=True,text=True).stdout.split()
    x=decode(a.mp4,48000,2); m=decode(a.music,48000,2); n=min(len(x),len(m))
    xm,mm_=x[:n].mean(1),m[:n].mean(1); seg=slice(48000,min(n,48000*11))
    c=np.correlate(xm[seg],mm_[seg.start-480:seg.stop+480],mode='valid'); lag=int(np.argmax(c))-480
    g=float(np.dot(x[:n].ravel(),m[:n].ravel())/np.dot(m[:n].ravel(),m[:n].ravel()))
    res=x[:n]-g*m[:n]; e=lambda v:10*np.log10(np.mean(v**2)+1e-15)
    tot=e(res)-e(m[:n]); wins=[]
    for i in range(0,n-48000,48000):
        mw=m[i:i+48000]
        if e(mw)>-50: wins.append((i/48000,e(res[i:i+48000])-e(mw)))
    worst=max(wins,key=lambda w:w[1])
    R['audio']=dict(audio_streams=len(ns),lag_samples=lag,gain_db=round(20*np.log10(abs(g)),2),residual_db=round(tot,1),
                    worst_window=dict(t=worst[0],residual_db=round(worst[1],1)),length_diff_ms=round((len(x)-len(m))/48,1))
    A=R['audio']
    if len(ns)!=1: fails.append(f'{len(ns)} audio streams (want exactly the music)')
    if abs(lag)>1: fails.append(f'audio is {lag} samples off the music track')
    if abs(A['gain_db'])>0.5: fails.append(f"audio level differs from the music track by {A['gain_db']} dB")
    if tot>-20: fails.append(f'audio differs from the music track (null residual {tot:.1f} dB)')
    if worst[1]>-12: fails.append(f'audio differs from the music track around {worst[0]:.0f} s (residual {worst[1]:.1f} dB)')
    if abs(len(x)-len(m))>48000/fps: fails.append(f"audio length differs from the music by {A['length_diff_ms']} ms")
    R['fails']=fails; R['pass']=not fails
    if a.out: jdump(R,a.out)
    print(f"{os.path.basename(a.mp4)} lead {a.lead}: re-detected {len(D)} downbeats, {B['bar_pulses']} pulses/bar, irregular bars {B['irregular_bars']}")
    print(' shot frame  aimed_at  downbeat  offset   raw   pixels  hits')
    for r in rows: print(f"  {r['shot']:>2} {r['frame']:>5} {r['aimed_at']:8.3f} {r['nearest_downbeat']:8.3f} {r['offset_ms']:+6.1f} {r['raw_offset_ms']:+6.1f}  {'yes' if r['seen_in_pixels'] else 'NO ':<4} {','.join(r['hits'])}")
    for s in R.get('splices',[]): print(f"  splice {s['edit_t']:.3f}: {s['downbeat_offset_ms']:+.1f} ms to downbeat, low-end dip {s['low_dip_db']} dB (source {s['source_low_dip_db']} dB)")
    print(f"  audio: {A['audio_streams']} stream, lag {A['lag_samples']} samples, gain {A['gain_db']:+.2f} dB, null residual {A['residual_db']} dB (worst 1 s window {A['worst_window']['residual_db']} dB at {A['worst_window']['t']:.0f} s)")
    for k,v in R['motion_spikes'].items():
        if v: print(f"  panel {k}: in-shot motion spikes (not cuts: histogram unchanged or picture does not persist): frames {v}")
    print('PASS' if not fails else 'FAIL:\n  '+'\n  '.join(fails)); sys.exit(0 if not fails else 1)
main()
