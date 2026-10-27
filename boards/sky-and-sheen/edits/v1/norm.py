"""Normalize every board clip to a constant-frame-rate panel master: 24 fps CFR (fixes the VFR sources), 952x1080
crop-fill (lanczos), yuv420p, no audio. The scan, the cut scan and the renderer all read these files, so a window
that is clean in the scan is exactly what appears on screen."""
import json,os,subprocess,sys
from concurrent.futures import ThreadPoolExecutor
F='/workspace/moodboard/sky-and-sheen/footage/'; O=os.path.join(os.path.dirname(os.path.abspath(__file__)),'norm')
W,H,FPS=952,1080,24
def norm(c):
    o=f'{O}/{c}.mp4'
    if os.path.exists(o): return c
    vf=f"fps={FPS},scale={W}:{H}:force_original_aspect_ratio=increase:flags=lanczos,crop={W}:{H},setsar=1,format=yuv420p"
    subprocess.run(['ffmpeg','-v','error','-y','-i',F+c+'.mp4','-an','-vf',vf,'-vsync','cfr','-r',str(FPS),'-c:v','libx264','-preset','fast','-crf','14','-threads','2',o+'.tmp.mp4'],check=True)
    os.rename(o+'.tmp.mp4',o); return c
if __name__=='__main__':
    C=[r['id'] for r in json.load(open(F+'catalog.json'))]
    with ThreadPoolExecutor(3) as ex:
        for c in ex.map(norm,C): print(c,flush=True)
