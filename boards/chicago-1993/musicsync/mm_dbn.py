"""Runs inside .venv-mm (madmom). Usage: mm_dbn.py in.wav out.npz
Writes the RNN beat/downbeat activations (100 fps) and DBN downbeat tracks for 2/3/4/6 beats per bar and the joint model."""
import sys,numpy as np
from madmom.features.downbeats import RNNDownBeatProcessor,DBNDownBeatTrackingProcessor
wav,out=sys.argv[1],sys.argv[2]
act=RNNDownBeatProcessor()(wav); res={'act':act}
for name,bpb in [('mm2',[2]),('mm3',[3]),('mm4',[4]),('mm6',[6]),('mmall',[2,3,4,6])]:
    try:
        r=DBNDownBeatTrackingProcessor(beats_per_bar=bpb,fps=100,min_bpm=40,max_bpm=220)(act)
    except Exception as e:
        r=np.zeros((0,2))
    res[name]=r
np.savez(out,**res)
