"""Shared helpers for musicsync. All times are seconds on the audio file's own timeline; nothing here assumes a BPM."""
import hashlib,json,os,subprocess,numpy as np
HERE=os.path.dirname(os.path.abspath(__file__))
PY=os.path.join(HERE,'.venv/bin/python'); PYMM=os.path.join(HERE,'.venv-mm/bin/python')
SR=44100
def sha(path):
    h=hashlib.sha256()
    with open(path,'rb') as f:
        for b in iter(lambda:f.read(1<<20),b''): h.update(b)
    return h.hexdigest()[:16]
def work_dir(audio,root=None):
    d=os.path.join(root or os.path.join(HERE,'cache'),sha(audio)); os.makedirs(d,exist_ok=True); return d
def to_wav(src,dst,sr=SR):
    """Decode anything ffmpeg reads (mp3/wav/mp4/mov...) to mono 44.1k wav. For MP4/AAC, ffmpeg honours the edit list,
    so encoder priming is removed exactly as a player does."""
    if not os.path.exists(dst):
        subprocess.run(['ffmpeg','-v','error','-y','-i',src,'-vn','-ac','1','-ar',str(sr),dst],check=True)
    return dst
def stems(wav,wd):
    """Demucs htdemucs 4-stem separation (drums, bass, other, vocals), cached."""
    out=os.path.join(wd,'htdemucs',os.path.splitext(os.path.basename(wav))[0])
    if not os.path.exists(os.path.join(out,'drums.wav')):
        subprocess.run([PY,'-m','demucs','-n','htdemucs','-d','cpu','-o',wd,wav],check=True,capture_output=True)
    return {k:os.path.join(out,k+'.wav') for k in ('drums','bass','other','vocals')}
def load(path,sr=SR):
    import librosa; y,_=librosa.load(path,sr=sr,mono=True); return y
HOP=220  # 5 ms at 44.1k
def band_flux(y,lo,hi,sr=SR,hop=HOP):
    import librosa
    S=np.abs(librosa.stft(y,n_fft=2048,hop_length=hop))**2; f=librosa.fft_frequencies(sr=sr,n_fft=2048)
    e=np.log1p(1e3*S[(f>=lo)&(f<=hi)].sum(0)); return np.maximum(0,np.diff(e,prepend=e[0]))
def peaks(env,pct=97,min_gap=0.09,hop=HOP,sr=SR):
    """Onset peaks with strength normalised to the 95th percentile of picked peaks (1.0 = a typical big hit)."""
    import scipy.signal as ss
    pk,_=ss.find_peaks(env,height=np.percentile(env,pct),distance=max(1,int(min_gap*sr/hop)))
    if not len(pk): return np.zeros(0),np.zeros(0)
    st=env[pk]/max(np.percentile(env[pk],95),1e-9); return pk*hop/sr,st
def drum_hits(drums_wav):
    y=load(drums_wav); k=band_flux(y,20,150); s=band_flux(y,1500,5000); b=band_flux(y,20,16000)
    kt,ks=peaks(k); st,ss_=peaks(s); bt,bs=peaks(b)
    return dict(kick=(kt,ks),snare=(st,ss_),all=(bt,bs))
def strength_near(t,times,strengths,win=0.04):
    m=np.abs(times-t)<=win; return float(strengths[m].max()) if m.any() else 0.0
def jdump(o,p): json.dump(o,open(p,'w'),indent=1,ensure_ascii=False,default=lambda v:v.item() if hasattr(v,'item') else str(v))
