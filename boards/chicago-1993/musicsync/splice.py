"""Music edit builder: whole-bar splices on detected downbeats only.
Usage: .venv/bin/python splice.py SOURCE source_beats.json "a0-a1,b0-b1,..." OUT.wav OUT_splices.json [--fade-in 1.2]
Segments are given in SOURCE BAR INDICES (from source_beats.json bars), half-open: "3-15" = bars 3..14.
Each joint is cut a hair before the incoming downbeat's transient on both sides (same offset, so the bar phase is
preserved) with a 10 ms equal-power crossfade. Refuses a segment boundary that is not a detected downbeat."""
import argparse,json,os,sys,numpy as np,soundfile as sf
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from common import *
PRE=0.012; XF=0.010
def transient(y,sr,t,win=0.03):
    """Attack time near a downbeat: steepest rise of the 2 ms envelope within +-win."""
    a,b=int((t-win)*sr),int((t+win)*sr); a=max(a,0); seg=np.abs(y[a:b])
    if len(seg)<10: return t
    h=int(0.002*sr); e=np.convolve(seg,np.ones(h)/h,'same'); d=np.diff(e)
    return (a+int(np.argmax(d)))/sr
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('src'); ap.add_argument('beats'); ap.add_argument('segs'); ap.add_argument('out'); ap.add_argument('meta')
    ap.add_argument('--fade-in',type=float,default=0.0); ap.add_argument('--fade-out',type=float,default=0.0)
    ap.add_argument('--lufs',type=float,default=-15.0,help='static gain to this integrated loudness (no compression, no limiter)')
    ap.add_argument('--tp-max',type=float,default=-1.5); a=ap.parse_args()
    B=json.load(open(a.beats)); D=[d['t'] for d in B['downbeats']]
    import librosa
    y,sr=librosa.load(a.src,sr=48000,mono=False); y=np.atleast_2d(y); mono=y.mean(0); T=y.shape[1]/sr
    segs=[tuple(map(int,s.split('-'))) for s in a.segs.split(',')]
    def bt(i): return D[i] if i<len(D) else T
    pieces=[]; meta=[]; pos=0.0
    for k,(b0,b1) in enumerate(segs):
        assert 0<=b0<b1<=len(D), f'segment {b0}-{b1} outside the {len(D)} detected downbeats'
        s_t=transient(mono,sr,bt(b0))-PRE if b0>0 or k>0 else bt(b0)-PRE
        e_t=transient(mono,sr,bt(b1))-PRE if b1<len(D) else T
        s_t=max(0.0,s_t)
        pieces.append(y[:,int(round(s_t*sr)):int(round(e_t*sr))])
        meta.append(dict(src_bar0=b0,src_bar1=b1,src_t0=round(s_t+PRE,4),src_t1=round(e_t+PRE,4) if b1<len(D) else round(T,4),
                         src_downbeat0=round(bt(b0),4),src_downbeat1=round(bt(b1),4) if b1<len(D) else None))
    xf=int(XF*sr); out=pieces[0]; joints=[]
    for p in pieces[1:]:
        joints.append(round(out.shape[1]/sr - XF/2 + PRE,4))   # edit time of the incoming downbeat
        r=np.linspace(0,1,xf); tail=out[:,-xf:]*np.cos(r*np.pi/2)+p[:,:xf]*np.sin(r*np.pi/2)
        out=np.concatenate([out[:,:-xf],tail,p[:,xf:]],axis=1)
    if a.fade_in: n=int(a.fade_in*sr); out[:,:n]*=np.linspace(0,1,n)
    if a.fade_out: n=int(a.fade_out*sr); out[:,-n:]*=np.linspace(1,0,n)
    # static gain only: the rendered audio must stay a scaled copy of this file, so no loudnorm/limiter downstream
    import subprocess,tempfile,re as _re
    tmp=tempfile.mktemp(suffix='.wav'); sf.write(tmp,out.T,sr,subtype='FLOAT')
    rep=subprocess.run(['ffmpeg','-hide_banner','-i',tmp,'-af','loudnorm=print_format=json','-f','null','-'],capture_output=True,text=True).stderr
    I=float(_re.search(r'"input_i" : "([-\d.]+)"',rep).group(1)); TP=float(_re.search(r'"input_tp" : "([-\d.]+)"',rep).group(1)); os.remove(tmp)
    gain=min(a.lufs-I,a.tp_max-TP); out=out*10**(gain/20)
    sf.write(a.out,out.T,sr,subtype='PCM_24')
    pos=0.0
    for m,p in zip(meta,pieces):
        m['edit_t0']=round(pos+ (PRE if m is not meta[0] or m['src_bar0']>0 else 0),4); pos+=p.shape[1]/sr-(XF if m is not meta[-1] else 0)
    jdump(dict(source=os.path.abspath(a.src),source_beats=os.path.abspath(a.beats),segments=meta,joints_edit_t=joints,
               preroll=PRE,crossfade=XF,duration=round(out.shape[1]/sr,4),gain_db=round(gain,2),measured_lufs=I,measured_tp=TP,fade_in=a.fade_in,fade_out=a.fade_out),a.meta)
    print('wrote',a.out,round(out.shape[1]/sr,3),'s; joints at',joints)
main()
