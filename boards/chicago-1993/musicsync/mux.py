"""Music-only mux (the only audio path in this pipeline). Usage: python mux.py VIDEO MUSIC.wav OUT.mp4
The output carries exactly one audio stream: the music track, AAC-encoded with no filters (no clip audio, no
ambience, no ducking, no loudnorm). Level the music upstream (splice.py --lufs uses a static gain) so the
check can null-test the render against the music file. The video stream is copied untouched."""
import subprocess,sys
def mux(video,music,out,bitrate='256k'):
    cmd=['ffmpeg','-v','error','-y','-i',video,'-i',music,'-map','0:v:0','-map','1:a:0','-c:v','copy',
         '-c:a','aac','-b:a',bitrate,'-ar','48000','-movflags','+faststart',out]
    subprocess.run(cmd,check=True); return out
if __name__=='__main__':
    if len(sys.argv)!=4: sys.exit(__doc__)
    mux(*sys.argv[1:])
