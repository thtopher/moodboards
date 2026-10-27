"""Overlay: the cuts of a render on the grid re-detected from the rendered MP4's own audio (8 rows of ~32 s).
Usage: (musicsync venv) python overlay.py LEAD OUT.png"""
import json,sys,os,numpy as np,matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
sys.path.insert(0,'/workspace/moodboard/musicsync'); from common import work_dir,load,band_flux,HOP,SR,stems
H=os.path.dirname(os.path.abspath(__file__)); E=os.path.dirname(H)+'/'
lead=int(sys.argv[1]); OUT=sys.argv[2]
mp4=E+f'sky_sheen_full_v1_lead{lead}.mp4'; wd=work_dir(mp4)
B=json.load(open(wd+'/render_beats.json')); CK=json.load(open(H+f'/check_lead{lead}.json')); O=json.load(open(H+'/sync/override.json'))
y=load(wd+'/mix.wav'); d=load(stems(wd+'/mix.wav',work_dir(wd+'/mix.wav'))['drums'])
kick=band_flux(d,20,150); snare=band_flux(d,1500,5000); tt=np.arange(len(kick))*HOP/SR
import scipy.signal as ss; lp=ss.sosfiltfilt(ss.butter(4,150,'low',fs=SR,output='sos'),y); tl=np.arange(len(lp))/SR
P=np.array([p['t'] if isinstance(p,dict) else p for p in B['pulses']]); D=np.array([x['t'] for x in B['downbeats']]); T=B['duration']
NR=8; rows=[(i*T/NR,(i+1)*T/NR) for i in range(NR)]
fig,ax=plt.subplots(NR,1,figsize=(22,3.1*NR))
for a,(s,e) in zip(ax,rows):
    m=(tl>=s)&(tl<e); a.plot(tl[m][::20],lp[m][::20]/np.abs(lp).max(),color='0.6',lw=0.4)
    m=(tt>=s)&(tt<e); a.plot(tt[m],kick[m]/kick.max()*1.4+1.2,color='tab:red',lw=0.8); a.plot(tt[m],snare[m]/snare.max()+2.7,color='tab:blue',lw=0.8)
    for x in P[(P>=s)&(P<e)]: a.axvline(x,color='tab:green',lw=0.4,alpha=0.5)
    for x in D[(D>=s)&(D<e)]: a.axvline(x,color='tab:green',lw=2.4,alpha=0.8)
    for k in O['_review']:
        r0,r1=(map(float,k.split('-')) if '-' in k else (float(k)-0.3,float(k)+0.3))
        if r1>s and r0<e: a.axvspan(max(r0,s),min(r1,e),color='tab:orange',alpha=0.12); a.text(max(r0,s),-1.15,' reviewed override',color='tab:orange',fontsize=8)
    for r in CK['cuts']:
        x=r['aimed_at']
        if s<=x<e:
            a.axvline(x,color='k',lw=1.3,ls=':'); a.text(x+0.05,3.75,f"#{r['shot']+1} {'/'.join(h.replace('_',' ') for h in r['hits'])}\n{r['offset_ms']:+.0f} ms"+(' (ovr)' if r.get('support')=='override' else ''),fontsize=7,va='top')
    a.set_xlim(s,e); a.set_ylim(-1.25,3.9); a.set_yticks([])
ax[0].set_title(f'sky_sheen_full_v1 (lead {lead}): green thick = downbeats re-detected from the MP4 audio (Beat This! + madmom, with the reviewed override; thin = pulses); '
                f'black dotted = cut frame + lead; orange = override regions; red = kick, blue = snare (drum stem); gray = <150 Hz',fontsize=10)
plt.tight_layout(); plt.savefig(OUT,dpi=72); print(OUT)
