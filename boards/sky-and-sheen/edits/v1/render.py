"""Render sky_sheen_full_v1 lead variants from edl_v1.json. Usage: python3 render.py [lead ...]
Frame boundaries come from grammar.frames(lead) (the musicsync cut list), never from the EDL, and both panels are rendered
from the same shot list, so they cut on the same frame. Source frames are picked exactly (grammar.src_frames) from the
24 fps CFR normalized clips (norm/), the same frames the EDL's cut-detectability check predicted from.
Audio: the music track only, untouched (musicsync/mux.py)."""
import json,subprocess,sys,os,hashlib
sys.path.insert(0,'/workspace/moodboard/musicsync')
from mux import mux
from grammar import frames,FPS,MUSIC,NORM,HERE,src_frames
E=os.path.dirname(HERE)+'/'; W=HERE+'/'
e=json.load(open(W+'edl_v1.json'))
def run(a): subprocess.run(['ffmpeg','-v','error','-y']+a,check=True)
assert [c['shot'] for c in e['sky']]==[k['shot'] for k in e['sheen']]==[p['shot'] for p in e['pairs']]==list(range(len(e['pairs'])))
from concurrent.futures import ThreadPoolExecutor
def seg(s,fr):
    idx=[int(i) for i in src_frames(s['src_in_frame'],fr,s['speed'])]
    key=hashlib.sha1(json.dumps([s['clip'],idx]).encode()).hexdigest()[:12]; o=W+f'seg/{key}.mp4'
    if os.path.exists(o): return o
    if s['speed']==1.0:
        vf=f"trim=start_frame={idx[0]}:end_frame={idx[-1]+1},setpts=N/{FPS}/TB,format=yuv420p"
        run(['-i',NORM+s['clip']+'.mp4','-an','-vf',vf,'-r',str(FPS),'-frames:v',str(fr),'-c:v','libx264','-preset','fast','-crf','14',o+'.tmp.mp4'])
    else:   # sped-up shots: pick the exact source frames (decoded with OpenCV) and pipe them to x264
        import cv2
        cap=cv2.VideoCapture(NORM+s['clip']+'.mp4'); want=set(idx); got={}; n=0
        while n<=idx[-1]:
            ok,im=cap.read()
            if not ok: break
            if n in want: got[n]=im
            n+=1
        p=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','bgr24','-s','952x1080','-r',str(FPS),'-i','-',
                            '-pix_fmt','yuv420p','-c:v','libx264','-preset','fast','-crf','14',o+'.tmp.mp4'],stdin=subprocess.PIPE)
        for i in idx: p.stdin.write(got[min(i,max(got))].tobytes())
        p.stdin.close(); assert p.wait()==0
    got=int(subprocess.run(['ffprobe','-v','error','-count_frames','-show_entries','stream=nb_read_frames','-of','csv=p=0',o+'.tmp.mp4'],capture_output=True,text=True).stdout)
    assert got==fr,(s['clip'],got,fr)
    os.rename(o+'.tmp.mp4',o); return o
def panel(L,tag,lead,FR):
    with ThreadPoolExecutor(6) as ex: segs=list(ex.map(lambda n:seg(L[n],FR[n][1]-FR[n][0]),range(len(L))))
    ins=[]; fc=''
    for n in range(len(L)): ins+=['-i',segs[n]]; fc+=f"[{n}:v]setpts=PTS-STARTPTS[v{n}];"
    fc+=''.join(f'[v{n}]' for n in range(len(L)))+f"concat=n={len(L)}:v=1:a=0,setpts=N/{FPS}/TB[o]"
    out=W+f'seg/L{lead}_panel_{tag}.mp4'
    run(ins+['-filter_complex',fc,'-map','[o]','-r',str(FPS),'-c:v','libx264','-preset','medium','-crf','15',out]); return out
def render(lead):
    FR,END=frames(lead); T=END/FPS
    pa=panel(e['sky'],'sky',lead,FR); pb=panel(e['sheen'],'sheen',lead,FR)
    fc=f"color=c=0x0b0b0c:s=16x1080:r={FPS}:d={T}[g];[0:v]trim=end_frame={END},setpts=N/{FPS}/TB[a];[1:v]trim=end_frame={END},setpts=N/{FPS}/TB[b];[a][g][b]hstack=inputs=3:shortest=1,format=yuv420p[v]"
    vid=W+f'seg/L{lead}_video.mp4'
    run(['-i',pa,'-i',pb,'-filter_complex',fc,'-map','[v]','-an','-c:v','libx264','-preset','slow','-crf','20','-maxrate','8M','-bufsize','16M',vid])
    out=E+f'sky_sheen_full_v1_lead{lead}.mp4'; mux(vid,MUSIC,out); print('rendered',out,END,'frames',flush=True); return out
if __name__=='__main__':
    os.makedirs(W+'seg',exist_ok=True)
    for L in (sys.argv[1:] or ['0','1','2']): render(int(L))
