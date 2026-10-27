"""Full-frame-rate hard-cut scan of source clips (the v2 scan samples at 12 fps and can miss an archival splice).
Uses the same spike detector as musicsync/check_render.py, so a window that passes here cannot show a cut there."""
import json,os,subprocess,sys,numpy as np
sys.path.insert(0,'/workspace/moodboard/musicsync')
F='/workspace/moodboard/chicago-1993/footage/'; O=os.path.join(os.path.dirname(os.path.abspath(__file__)),'cuts'); os.makedirs(O,exist_ok=True)
def spike_cuts(d,floor=20.0,ratio=1.5): return [i for i in range(1,len(d)) if d[i]>=floor and d[i]>=ratio*max(d[i-1],d[i+1] if i+1<len(d) else 0)]
def clip_cuts(clip):
    p=os.path.join(O,clip+'.json')
    if os.path.exists(p): return json.load(open(p))
    fps=eval(subprocess.run(['ffprobe','-v','error','-select_streams','v:0','-show_entries','stream=r_frame_rate','-of','csv=p=0',F+clip+'.mp4'],capture_output=True,text=True).stdout.strip())
    raw=subprocess.run(['ffmpeg','-v','error','-i',F+clip+'.mp4','-vf','scale=240:136,format=gray','-f','rawvideo','-'],capture_output=True,check=True).stdout
    V=np.frombuffer(raw,np.uint8).reshape(-1,136,240).astype(np.float32); d=np.r_[0,np.abs(np.diff(V,axis=0)).mean(axis=(1,2))]
    r=dict(fps=fps,cuts=[round(i/fps,3) for i in spike_cuts(d)]); json.dump(r,open(p,'w')); return r
if __name__=='__main__':
    from concurrent.futures import ThreadPoolExecutor
    clips=sys.argv[1:]
    with ThreadPoolExecutor(6) as ex:
        for c,r in zip(clips,ex.map(clip_cuts,clips)): print(c,r['cuts'])
