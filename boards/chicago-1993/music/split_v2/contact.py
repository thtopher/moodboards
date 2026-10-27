"""Contact sheet: one row per bar-cut pair; frames at cut+2, middle, end-2 of the full split frame, labeled."""
import json,subprocess,sys
from PIL import Image,ImageDraw,ImageFont
E='/workspace/moodboard/chicago-1993/edits/'; e=json.load(open(E+'v2/edl_v2.json'))
MP4=E+'music_split_v2.mp4'; W,H=560,315
try: font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',15); fb=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',17)
except Exception: font=fb=ImageFont.load_default()
def grab(f):
    p=subprocess.run(['ffmpeg','-v','error','-i',MP4,'-vf',f"select=eq(n\\,{f}),scale={W}:{H}",'-frames:v','1','-f','rawvideo','-pix_fmt','rgb24','-'],capture_output=True,check=True).stdout
    return Image.frombytes('RGB',(W,H),p)
rows=e['pairs']; LW=330
sheet=Image.new('RGB',(LW+3*W+40,len(rows)*(H+12)+60),(12,12,13)); d=ImageDraw.Draw(sheet)
d.text((12,14),'music_split_v2: every cut on a bar downbeat, both panels in lockstep. Row = one pair: cut+2f / middle / end-2f. Left panel Chicago, right counter-world.',fill=(230,230,230),font=fb)
for i,p in enumerate(rows):
    y=50+i*(H+12); f0,f1=p['f0'],p['f1']
    for j,f in enumerate((f0+2,(f0+f1)//2,f1-3)):
        sheet.paste(grab(f),(LW+j*(W+10),y))
    txt=[f"bar {p['bar']+1} · {f0/24:.2f}s · {p['section']}",p['rule_name'],'',f"L {p['chi']}",f"R {p['ctr']}",'',p['chi_beat'],'/ '+p['ctr_beat']]
    for k,t in enumerate(txt): d.text((12,y+4+k*21),t[:38],fill=(255,210,120) if k<2 else (220,220,220),font=fb if k<2 else font)
sheet.save(sys.argv[1] if len(sys.argv)>1 else E+'music_split_v2_contact.jpg',quality=85)
