"""Contact sheet for a v3 render: one row per pair, frames at cut+2 / middle / end-3, labeled with the moment it hits."""
import json,subprocess,sys
from PIL import Image,ImageDraw,ImageFont
sys.path.insert(0,'.'); from grammar import frames,FPS
E='/workspace/moodboard/chicago-1993/edits/'; e=json.load(open(E+'v3/edl_v3.json'))
lead=int(sys.argv[1]); MP4=E+f'music_split_v3_lead{lead}.mp4'; OUT=sys.argv[2]; W,H=560,315
FR,END=frames(lead)
font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',15); fb=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',17)
def grab(f):
    p=subprocess.run(['ffmpeg','-v','error','-i',MP4,'-vf',f"select=eq(n\\,{f}),scale={W}:{H}",'-frames:v','1','-f','rawvideo','-pix_fmt','rgb24','-'],capture_output=True,check=True).stdout
    return Image.frombytes('RGB',(W,H),p)
rows=e['pairs']; LW=360
sheet=Image.new('RGB',(LW+3*W+40,len(rows)*(H+12)+60),(12,12,13)); d=ImageDraw.Draw(sheet)
d.text((12,14),f'music_split_v3 (lead {lead}): every cut on a detected downbeat, both panels in lockstep, music track only. Row = one pair: cut+2f / middle / end-3f.',fill=(230,230,230),font=fb)
for i,p in enumerate(rows):
    y=50+i*(H+12); f0,f1=FR[i]
    for j,f in enumerate((f0+2,(f0+f1)//2,f1-3)): sheet.paste(grab(f),(LW+j*(W+10),y))
    hits=', '.join(h.replace('_',' ') for h in p['hits'])
    txt=[f"#{i+1} · {p['t0']:.2f}s · {p['bars']} bar{'s' if p['bars']>1 else ''} · {p['energy']}",f"hits: {hits}",p['rule_name'],'',f"L {p['chi']}",f"R {p['ctr']}",'',p['chi_beat'],'/ '+p['ctr_beat']]
    for k,t in enumerate(txt): d.text((12,y+4+k*21),t[:40],fill=(255,210,120) if k<3 else (220,220,220),font=fb if k<1 else font)
sheet.save(OUT,quality=85)
