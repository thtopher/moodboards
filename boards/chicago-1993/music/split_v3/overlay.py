"""Overlay: v3 cuts on the true grid re-detected from the rendered MP4's own audio. Usage: python overlay.py LEAD OUT.png"""
import json,sys,os,numpy as np,matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
sys.path.insert(0,'/workspace/moodboard/musicsync'); from common import work_dir,load,band_flux,HOP,SR,stems
lead=int(sys.argv[1]); OUT=sys.argv[2]; E='/workspace/moodboard/chicago-1993/edits/'
mp4=E+f'music_split_v3_lead{lead}.mp4'; wd=work_dir(mp4)
B=json.load(open(wd+'/render_beats.json')); CK=json.load(open(f'check_lead{lead}.json')); Sp=json.load(open('sync/splices.json'))
y=load(wd+'/mix.wav'); d=load(stems(wd+'/mix.wav',work_dir(wd+'/mix.wav'))['drums'])
kick=band_flux(d,20,150); snare=band_flux(d,1500,5000); tt=np.arange(len(kick))*HOP/SR
import scipy.signal as ss; lp=ss.sosfiltfilt(ss.butter(4,150,'low',fs=SR,output='sos'),y); tl=np.arange(len(lp))/SR
P=np.array(B['pulses']) if not isinstance(B['pulses'][0],dict) else np.array([p['t'] for p in B['pulses']])
D=np.array([x['t'] for x in B['downbeats']]); T=B['duration']
rows=[(0,19),(19,38),(38,T)]
fig,ax=plt.subplots(3,1,figsize=(20,11))
for a,(s,e) in zip(ax,rows):
    m=(tl>=s)&(tl<e); a.plot(tl[m][::20],lp[m][::20]/np.abs(lp).max(),color='0.6',lw=0.4)
    m=(tt>=s)&(tt<e); a.plot(tt[m],kick[m]/kick.max()*1.4+1.2,color='tab:red',lw=0.8); a.plot(tt[m],snare[m]/snare.max()+2.7,color='tab:blue',lw=0.8)
    for x in P[(P>=s)&(P<e)]: a.axvline(x,color='tab:green',lw=0.4,alpha=0.5)
    for x in D[(D>=s)&(D<e)]: a.axvline(x,color='tab:green',lw=2.4,alpha=0.8)
    for j in Sp['joints_edit_t']:
        if s<=j<e: a.axvline(j,color='tab:purple',lw=1.5,ls='--'); a.text(j,-1.15,' splice',color='tab:purple',fontsize=8)
    for r in CK['cuts']:
        x=r['aimed_at']
        if s<=x<e:
            a.axvline(x,color='k',lw=1.3,ls=':'); a.text(x+0.05,3.75,f"#{r['shot']+1} {'/'.join(h.replace('_',' ') for h in r['hits'])}\n{r['offset_ms']:+.0f} ms",fontsize=7.5,va='top')
    a.set_xlim(s,e); a.set_ylim(-1.25,3.9); a.set_yticks([])
ax[0].set_title(f'music_split_v3 (lead {lead}): green thick = downbeats re-detected from the MP4 audio (Beat This + madmom, thin = pulses); black dotted = cut frame + lead; '
                f'purple = music splices; red = kick, blue = snare (drum stem); gray = <150 Hz',fontsize=10)
plt.tight_layout(); plt.savefig(OUT,dpi=80)
