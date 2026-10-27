"""v3 grammar: identical pairing rules, gates and window stats to v2 (imported, not copied), but the cut grid now
comes from the musicsync cut list (detected downbeats + ranked moments), never from a fixed BPM grid."""
import json,os,sys,importlib.util
HERE=os.path.dirname(os.path.abspath(__file__))
_spec=importlib.util.spec_from_file_location('grammar_v2',os.path.join(HERE,'..','v2','grammar.py')); g2=importlib.util.module_from_spec(_spec); _spec.loader.exec_module(g2)
RULES,BANNED,GATE,quality_fail,window_stats,scan,catalog=g2.RULES,g2.BANNED,g2.GATE,g2.quality_fail,g2.window_stats,g2.scan,g2.catalog
FPS=24
CUTLIST=os.path.join(HERE,'sync','cutlist.json')
MUSIC='/workspace/moodboard/chicago-1993/edits/music/v3/music_edit_v3.wav'
def cutlist():
    C=json.load(open(CUTLIST)); assert C['config']['fps']==FPS; return C
def frames(lead):
    """Shot boundaries in frames for one lead: [(f0,f1)] per shot, contiguous, ending on the music's last frame."""
    C=cutlist(); F=[tuple(s['frames'][str(lead)]) for s in C['shots']]
    for a,b in zip(F[:-1],F[1:]): assert a[1]==b[0],'cut list is not contiguous'
    return F,C['end_frame']
