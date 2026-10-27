"""Contact sheet: one frame per shot (cut+3 frames) of a render, 6 per row, labeled. Usage: python3 contact.py LEAD OUT.png OUT_web.jpg"""
import json,subprocess,sys,os
from PIL import Image,ImageDraw,ImageFont
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); from grammar import frames,FPS,HERE
E=os.path.dirname(HERE)+'/'; e=json.load(open(HERE+'/edl_v1.json'))
lead=int(sys.argv[1]); MP4=E+f'sky_sheen_full_v1_lead{lead}.mp4'; W,H=480,270; COLS=6; LH=74
FR,END=frames(lead); n=len(e['pairs'])
want=[min(FR[i][0]+3,FR[i][1]-1) for i in range(n)]
import cv2   # one sequential decode pass, grab the wanted frames
cap=cv2.VideoCapture(MP4); ws=set(want); got={}; k=0
while k<=max(want):
    ok,im=cap.read()
    if not ok: break
    if k in ws: got[k]=cv2.resize(cv2.cvtColor(im,cv2.COLOR_BGR2RGB),(W,H),interpolation=cv2.INTER_AREA).tobytes()
    k+=1
p=b''.join(got[f] for f in want)
font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',13); fb=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',14)
ft=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',22)
rows=(n+COLS-1)//COLS; G=10
sheet=Image.new('RGB',(COLS*(W+G)+G,70+rows*(H+LH+G)),(12,12,13)); d=ImageDraw.Draw(sheet)
d.text((G,14),f'Sky ↔ Sheen, full song (lead {lead}): {n} shots, {n-1} cuts, every cut on a detected downbeat, both panels in lockstep. One frame per shot (cut + 3 frames).',fill=(235,235,235),font=ft)
d.text((G,44),'Left panel: Sky.  Right panel: Sheen.  Label: shot · time · bars · energy · moment hit / link rule / clips.',fill=(170,170,170),font=font)
for i,pr in enumerate(e['pairs']):
    r,c=divmod(i,COLS); x=G+c*(W+G); y=70+r*(H+LH+G)
    sheet.paste(Image.frombytes('RGB',(W,H),p[i*W*H*3:(i+1)*W*H*3]),(x,y))
    hits=', '.join(h.replace('_',' ') for h in pr['hits'])
    d.text((x,y+H+3),f"#{i+1} · {FR[i][0]/FPS:.2f}s · {pr['bars']}b · {pr['energy']} · {hits}"[:62],fill=(255,210,120),font=fb)
    d.text((x,y+H+21),pr['rule_name'][:60],fill=(230,230,230),font=font)
    d.text((x,y+H+38),f"L {pr['sky']}"[:30],fill=(180,200,230),font=font); d.text((x+W//2,y+H+38),f"R {pr['sheen']}"[:30],fill=(230,200,180),font=font)
sheet.save(sys.argv[2])
web=sheet.copy(); web.thumbnail((2000,99999)); web.save(sys.argv[3],quality=82)
print(sys.argv[2],sheet.size,sys.argv[3],web.size)
