"""119x135 gray thumbnails of every frame of each normalized clip (thumbs/<id>.npy, uint8), used to predict the
pixel difference of each planned cut (the check needs every cut to be a clear spike in both panels)."""
import os,subprocess,sys,numpy as np
from concurrent.futures import ThreadPoolExecutor
H=os.path.dirname(os.path.abspath(__file__))
def th(c):
    o=f'{H}/thumbs/{c}.npy'
    if os.path.exists(o): return c
    raw=subprocess.run(['ffmpeg','-v','error','-i',f'{H}/norm/{c}.mp4','-vf','scale=119:135:flags=area,format=gray','-f','rawvideo','-'],capture_output=True,check=True).stdout
    np.save(o,np.frombuffer(raw,np.uint8).reshape(-1,135,119)); return c
C=sorted(x[:-4] for x in os.listdir(H+'/norm') if x.endswith('.mp4') and 'tmp' not in x)
with ThreadPoolExecutor(3) as ex: list(ex.map(th,C))
print('done',len(C))
