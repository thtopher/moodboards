"""Render music_split_v3 lead variants from edl_v3.json. Usage: python render_v3.py [lead ...]
Frame boundaries come from grammar.frames(lead) (the musicsync cut list), never from the EDL; both panels are
rendered from the same shot list so they cut on the same frame. Audio: the music track only (musicsync/mux.py)."""
import json,subprocess,sys,os
sys.path.insert(0,'/workspace/moodboard/musicsync')
from mux import mux
from grammar import frames,FPS,MUSIC
F='/workspace/moodboard/chicago-1993/footage/'; E='/workspace/moodboard/chicago-1993/edits/'; W=E+'v3/'
e=json.load(open(W+'edl_v3.json'))
GR="eq=contrast=1.06:saturation=0.86:gamma=0.97"
def run(a): subprocess.run(['ffmpeg','-v','error','-y']+a,check=True)
assert [c['shot'] for c in e['chi']]==[k['shot'] for k in e['ctr']]==[p['shot'] for p in e['pairs']]==list(range(len(e['pairs'])))
from concurrent.futures import ThreadPoolExecutor
import hashlib
def seg(s,w,fr,T):
    key=hashlib.sha1(json.dumps([s['clip'],s['src_in'],s['speed'],s.get('freeze'),w,fr,GR]).encode()).hexdigest()[:12]
    o=W+f'seg/{key}.mp4'
    if os.path.exists(o): return o
    vf=f"setpts=(PTS-STARTPTS)/{s['speed']},scale={w}:1080:force_original_aspect_ratio=increase:flags=lanczos,crop={w}:1080,setsar=1,fps={FPS},{GR}"
    if s.get('freeze'): vf=f"trim=duration={s['freeze']},setpts=PTS-STARTPTS,"+vf+f",tpad=stop_mode=clone:stop_duration={T}"
    run(['-ss',str(s['src_in']),'-i',F+s['clip']+'.mp4','-an','-vf',vf+',format=yuv420p','-frames:v',str(fr),'-c:v','libx264','-preset','fast','-crf','16',o+'.tmp.mp4'])
    got=int(subprocess.run(['ffprobe','-v','error','-count_frames','-show_entries','stream=nb_read_frames','-of','csv=p=0',o+'.tmp.mp4'],capture_output=True,text=True).stdout)
    assert got==fr,(s['clip'],got,fr)
    os.rename(o+'.tmp.mp4',o); return o
def panel(L,w,tag,lead,FR,END):
    T=END/FPS; ins=[]; fc=''
    with ThreadPoolExecutor(6) as ex: segs=list(ex.map(lambda n:seg(L[n],w,FR[n][1]-FR[n][0],T),range(len(L))))
    for n,s in enumerate(L):
        f0,f1=FR[n]; fr=f1-f0
        ins+=['-i',segs[n]]; fc+=f"[{n}:v]setpts=PTS-STARTPTS[v{n}];"
    fc+=''.join(f'[v{n}]' for n in range(len(L)))+f"concat=n={len(L)}:v=1:a=0,setpts=N/{FPS}/TB[o]"
    out=W+f'seg/L{lead}_panel_{tag}.mp4'
    run(ins+['-filter_complex',fc,'-map','[o]','-r',str(FPS),'-c:v','libx264','-preset','medium','-crf','15',out]); return out
def render(lead):
    FR,END=frames(lead); T=END/FPS
    pc=panel(e['chi'],952,'chi',lead,FR,END); pk=panel(e['ctr'],952,'ctr',lead,FR,END)
    fc=f"color=c=0x0b0b0c:s=16x1080:r={FPS}:d={T}[g];[0:v]trim=end_frame={END},setpts=N/{FPS}/TB[c];[1:v]trim=end_frame={END},setpts=N/{FPS}/TB[k];[c][g][k]hstack=inputs=3:shortest=1,format=yuv420p[v]"
    vid=W+f'seg/L{lead}_video.mp4'
    run(['-i',pc,'-i',pk,'-filter_complex',fc,'-map','[v]','-an','-c:v','libx264','-preset','slow','-crf','23','-maxrate','4.6M','-bufsize','9M',vid])
    out=E+f'music_split_v3_lead{lead}.mp4'; mux(vid,MUSIC,out); print('rendered',out,END,'frames'); return out
if __name__=='__main__':
    os.makedirs(W+'seg',exist_ok=True)
    for L in (sys.argv[1:] or ['0','1','2']): render(int(L))
