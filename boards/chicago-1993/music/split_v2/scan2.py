"""Per-sample motion/exposure scan used by the v2 EDL generator and the checker.
Per sample (12 fps): t, fl (median flow px/s), dx/dy (median flow components px/s, +x = content moves right,
+y = content moves down), df (mean abs frame diff, cut detector), lu (99th pct luma), lm (mean luma),
clip (fraction of pixels >= 250), mdx/mdy (median flow of the moving pixels only = subject direction), mfrac (fraction of pixels moving), warm (mean R - mean B)."""
import cv2,numpy as np,sys,os
F='/workspace/moodboard/chicago-1993/footage/'
OUT=os.path.join(os.path.dirname(os.path.abspath(__file__)),'scan')
def scan(cid,fps=12):
    cap=cv2.VideoCapture(F+cid+'.mp4'); sfps=cap.get(cv2.CAP_PROP_FPS) or 24; step=max(1,round(sfps/fps))
    prev=None; R={k:[] for k in 't fl dx dy mdx mdy mfrac df lu lm clip warm'.split()}; i=0
    while True:
        ok,fr=cap.read()
        if not ok: break
        if i%step==0:
            sm=cv2.resize(fr,(160,int(160*fr.shape[0]/fr.shape[1])),interpolation=cv2.INTER_AREA)
            g=cv2.cvtColor(sm,cv2.COLOR_BGR2GRAY)
            if prev is not None:
                f=cv2.calcOpticalFlowFarneback(prev,g,None,0.5,3,15,3,5,1.2,0); k=sfps/step
                R['t'].append(i/sfps); R['fl'].append(float(np.median(np.linalg.norm(f,axis=2)))*k)
                R['dx'].append(float(np.median(f[...,0]))*k); R['dy'].append(float(np.median(f[...,1]))*k)
                mag=np.linalg.norm(f,axis=2); mv=mag>max(0.6,np.percentile(mag,80))  # moving pixels (subject motion)
                R['mfrac'].append(float((mag>0.6).mean()))
                R['mdx'].append(float(np.median(f[...,0][mv]))*k if mv.any() else 0.0)
                R['mdy'].append(float(np.median(f[...,1][mv]))*k if mv.any() else 0.0)
                R['df'].append(float(np.mean(cv2.absdiff(prev,g)))); R['lu'].append(float(np.percentile(g,99)))
                R['lm'].append(float(g.mean())); R['clip'].append(float((g>=250).mean()))
                R['warm'].append(float(sm[...,2].mean()-sm[...,0].mean()))
            prev=g
        i+=1
    np.savez(os.path.join(OUT,f'{cid}.npz'),**{k:np.array(v) for k,v in R.items()})
if __name__=='__main__':
    for c in sys.argv[1:]:
        if not os.path.exists(os.path.join(OUT,f'{c}.npz')): scan(c); print(c,flush=True)
