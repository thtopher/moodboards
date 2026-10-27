"""Render music_split_v2.mp4 from edl_v2.json.
Frame boundaries are NOT read from the EDL: they are re-derived from each shot's bar index via grammar.grid(),
so a shot can only start/end on a bar downbeat, and both panels are rendered from the same pair list."""
import json,subprocess,sys
from grammar import grid,FPS
F='/workspace/moodboard/chicago-1993/footage/'; E='/workspace/moodboard/chicago-1993/edits/'; W=E+'v2/'
A,DF=grid(); e=json.load(open(W+'edl_v2.json')); END=DF[-1]; T=END/FPS
GR="eq=contrast=1.06:saturation=0.86:gamma=0.97"
def run(a): subprocess.run(['ffmpeg','-v','error','-y']+a,check=True)
def frames_of(s):
    f0,f1=DF[s['bar']],DF[s['bar']+s['bars']]
    assert (f0,f1)==(s['f0'],s['f1']),f"EDL frames drifted off the bar grid at bar {s['bar']}"
    return f0,f1
# lockstep: both panels must be the same bar spans in the same order
assert [(c['bar'],c['bars']) for c in e['chi']]==[(k['bar'],k['bars']) for k in e['ctr']]==[(p['bar'],p['bars']) for p in e['pairs']]
def panel(L,w,tag):
    ins=[];fc=''
    for n,s in enumerate(L):
        f0,f1=frames_of(s); fr=f1-f0
        vf=f"setpts=(PTS-STARTPTS)/{s['speed']},scale={w}:1080:force_original_aspect_ratio=increase:flags=lanczos,crop={w}:1080,setsar=1,fps={FPS},{GR}"
        if s.get('freeze'): vf=f"trim=duration={s['freeze']},setpts=PTS-STARTPTS,"+vf+f",tpad=stop_mode=clone:stop_duration={T}"
        o=W+f'seg/{tag}{n:02d}.mp4'
        run(['-ss',str(s['src_in']),'-i',F+s['clip']+'.mp4','-an','-vf',vf+',format=yuv420p','-frames:v',str(fr),'-c:v','libx264','-preset','fast','-crf','16',o])
        got=int(subprocess.run(['ffprobe','-v','error','-count_frames','-show_entries','stream=nb_read_frames','-of','csv=p=0',o],capture_output=True,text=True).stdout)
        assert got==fr,(s['clip'],got,fr)
        ins+=['-i',o]; fc+=f"[{n}:v]setpts=PTS-STARTPTS[v{n}];"
    fc+=''.join(f'[v{n}]' for n in range(len(L)))+f"concat=n={len(L)}:v=1:a=0,setpts=N/{FPS}/TB[o]"
    run(ins+['-filter_complex',fc,'-map','[o]','-r',str(FPS),'-c:v','libx264','-preset','medium','-crf','15',W+f'panel_{tag}.mp4'])
AMB={'a-acroni-rolls','a-inland-train','a-acroni-fast'}   # counter-world clips whose own sound (mill noise, no music/speech) is mixed in, low
def audio():
    ins=['-i',E+'music/music_edit.wav','-i',F+'t-rain-street.mp4','-i',F+'t-rain-pouring.mp4','-i',F+'t-rain-street.mp4']
    fc=("[0:a]aresample=48000,asplit=2[mus][key];"
        "[1:a]atrim=0:20,asetpts=N/SR/TB,aresample=48000,pan=stereo|c0=c0|c1=c0[r1];"
        "[2:a]atrim=2:30,asetpts=N/SR/TB,aresample=48000,pan=stereo|c0=c0|c1=c0[r2];"
        "[3:a]atrim=0:20,asetpts=N/SR/TB,aresample=48000,pan=stereo|c0=c0|c1=c0[r3];"
        f"[r1][r2]acrossfade=d=2[r12];[r12][r3]acrossfade=d=2,atrim=0:{T},volume=0.32,afade=t=in:d=1.0[rain];")
    bus=[s for s in e['chi'] if s['clip']=='c-impr-bus-night'][0]['f0']/FPS
    fc+=(f"anoisesrc=d=2.2:c=white:r=48000:a=0.5,highpass=f=1800,lowpass=f=7000,pan=stereo|c0=c0|c1=c0,afade=t=in:d=0.05,afade=t=out:st=0.9:d=1.3,volume=0.35,adelay={int(bus*1000)}|{int(bus*1000)}[hiss];")
    k=4; parts=[]
    for s in e['ctr']:
        if s['clip'] in AMB:
            t0=s['f0']/FPS; d=(s['f1']-s['f0'])/FPS
            ins+=['-ss',str(s['src_in']),'-t',str(d),'-i',F+s['clip']+'.mp4']
            fc+=f"[{k}:a]aresample=48000,pan=stereo|c0=c0|c1=c0,lowpass=f=5000,afade=t=in:d=0.04,afade=t=out:st={max(0,d-0.08)}:d=0.08,volume=0.22,adelay={int(t0*1000)}|{int(t0*1000)}[k{k}];"; parts.append(f'[k{k}]'); k+=1
    n=2+len(parts)
    fc+=f"[rain][hiss]{''.join(parts)}amix=inputs={n}:normalize=0:duration=longest,apad=whole_dur={T},atrim=0:{T}[sfx];"
    fc+="[sfx][key]sidechaincompress=threshold=0.03:ratio=6:attack=20:release=400:makeup=1[duck];"
    fc+=f"[mus][duck]amix=inputs=2:normalize=0:duration=first,atrim=0:{T},afade=t=out:st={T-1.5}:d=1.5,loudnorm=I=-15:TP=-1.5:LRA=11[a]"
    run(ins+['-filter_complex',fc,'-map','[a]','-ar','48000','-c:a','pcm_s16le',W+'mix.wav'])
if __name__=='__main__':
    import os; os.makedirs(W+'seg',exist_ok=True)
    audio(); panel(e['chi'],952,'chi'); panel(e['ctr'],952,'ctr')
    fc=f"color=c=0x0b0b0c:s=16x1080:r={FPS}:d={T}[g];[0:v]trim=end_frame={END},setpts=N/{FPS}/TB[c];[1:v]trim=end_frame={END},setpts=N/{FPS}/TB[k];[c][g][k]hstack=inputs=3:shortest=1,format=yuv420p[v]"
    run(['-i',W+'panel_chi.mp4','-i',W+'panel_ctr.mp4','-i',W+'mix.wav','-filter_complex',fc,'-map','[v]','-map','2:a','-t',str(T),'-c:v','libx264','-preset','slow','-crf','23','-maxrate','4.6M','-bufsize','9M','-c:a','aac','-b:a','192k','-movflags','+faststart',E+'music_split_v2.mp4'])
    print('rendered',E+'music_split_v2.mp4',END,'frames')
