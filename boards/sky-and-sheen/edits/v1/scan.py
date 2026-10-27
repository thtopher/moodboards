"""Per-clip scan of the normalized 24 fps panel masters (norm/<id>.mp4).
12 fps sample stats (scan/<id>.npz): t, fl (median flow px/s at 160 px wide), dx/dy, mdx/mdy (median flow of the
moving pixels = subject direction, +x right, +y down), df, lm (mean luma), lu (p99 luma), clip (fraction >=250),
warm (R-B), hue (circular mean hue in degrees, saturation-weighted), sat (mean saturation 0-255).
Full-rate cut scan (cuts/<id>.json): the same spike detector check_render.py uses, on the same 1/4-scale gray
frames, plus the per-frame diff series d24 so the generator can predict how loud a planned cut will be."""
import cv2,json,numpy as np,sys,os

HERE=os.path.dirname(os.path.abspath(__file__)); N=HERE+'/norm/'
def spike_cuts(d,floor=20.0,ratio=1.5): return [i for i in range(1,len(d)) if d[i]>=floor and d[i]>=ratio*max(d[i-1],d[i+1] if i+1<len(d) else 0)]
def scan(cid):
    out=f'{HERE}/scan/{cid}.npz'; oc=f'{HERE}/cuts/{cid}.json'
    if os.path.exists(out) and os.path.exists(oc): return cid
    cap=cv2.VideoCapture(N+cid+'.mp4'); prev=None; prevq=None; d24=[0.0]
    R={k:[] for k in 't fl dx dy mdx mdy mfrac df lu lm clip warm hue sat'.split()}; i=0
    while True:
        ok,fr=cap.read()
        if not ok: break
        q=cv2.resize(cv2.cvtColor(fr,cv2.COLOR_BGR2GRAY),(238,270),interpolation=cv2.INTER_AREA).astype(np.float32)
        if prevq is not None: d24.append(float(np.abs(q-prevq).mean()))
        prevq=q
        if i%2==0:
            sm=cv2.resize(fr,(160,182),interpolation=cv2.INTER_AREA); g=cv2.cvtColor(sm,cv2.COLOR_BGR2GRAY)
            if prev is not None:
                f=cv2.calcOpticalFlowFarneback(prev,g,None,0.5,3,15,3,5,1.2,0); k=12
                mag=np.linalg.norm(f,axis=2); mv=mag>max(0.6,np.percentile(mag,80))
                R['t'].append(i/24); R['fl'].append(float(np.median(mag))*k)
                R['dx'].append(float(np.median(f[...,0]))*k); R['dy'].append(float(np.median(f[...,1]))*k)
                R['mfrac'].append(float((mag>0.6).mean()))
                R['mdx'].append(float(np.median(f[...,0][mv]))*k if mv.any() else 0.0)
                R['mdy'].append(float(np.median(f[...,1][mv]))*k if mv.any() else 0.0)
                R['df'].append(float(np.mean(cv2.absdiff(prev,g)))); R['lu'].append(float(np.percentile(g,99)))
                R['lm'].append(float(g.mean())); R['clip'].append(float((g>=250).mean()))
                R['warm'].append(float(sm[...,2].mean()-sm[...,0].mean()))
                hsv=cv2.cvtColor(sm,cv2.COLOR_BGR2HSV); h=hsv[...,0].astype(float)*2*np.pi/180; s=hsv[...,1].astype(float)
                R['hue'].append(float(np.degrees(np.arctan2((s*np.sin(h)).sum(),(s*np.cos(h)).sum()))%360)); R['sat'].append(float(s.mean()))
            prev=g
        i+=1
    np.savez(out,**{k:np.array(v) for k,v in R.items()})
    d=np.array(d24); json.dump(dict(fps=24,frames=len(d),cuts=[round(j/24,4) for j in spike_cuts(d)],cut_frames=spike_cuts(d),d24=[round(x,2) for x in d]),open(oc,'w'))
    return cid
if __name__=='__main__':
    from concurrent.futures import ProcessPoolExecutor
    C=sys.argv[1:] or sorted(x[:-4] for x in os.listdir(N) if x.endswith('.mp4') and 'tmp' not in x)
    with ProcessPoolExecutor(3) as ex:
        for c in ex.map(scan,C): print(c,flush=True)
