"""Gera docs/index.html (página única) a partir de dados.py, src/template.html e fotos/."""
import base64, io, json
from PIL import Image
from dados import B, I
PH='fotos/'
def jpg(fn,px=360,bg=(255,248,239)):
    im=Image.open(PH+fn).convert('RGBA'); im.thumbnail((px,px)); b=Image.new('RGB',(px,px),bg); b.paste(im,((px-im.size[0])//2,(px-im.size[1])//2),im.split()[3]); buf=io.BytesIO(); b.save(buf,'JPEG',quality=84,optimize=True)
    return 'data:image/jpeg;base64,'+base64.b64encode(buf.getvalue()).decode()
def png(fn,px):
    im=Image.open(PH+fn).convert('RGBA'); im.thumbnail((px,px)); buf=io.BytesIO(); im.save(buf,'PNG',optimize=True)
    return 'data:image/png;base64,'+base64.b64encode(buf.getvalue()).decode()
items=[dict(n=a,b=b,m=m,i=k,k=kw) for k,(a,b,m,f,kw) in enumerate(I) for b in [b]] if False else [dict(n=a,b=b,m=m,i=k,k=kw) for k,(a,b,m,f,kw) in enumerate(I)]
imgs=[jpg(f) if f else None for (_,_,_,f,_) in I]
kdp=png('logo_kdp.png',900)
html=open('src/template.html',encoding='utf-8').read()
html=html.replace('/*ITEMS*/',json.dumps(items,ensure_ascii=False)).replace('/*BINS*/',json.dumps({k:dict(n=v[0],c=v[1],t=v[2]) for k,v in B.items()},ensure_ascii=False)).replace('/*IMGS*/',json.dumps(imgs)).replace('%%KDP%%',kdp)
open('docs/index.html','w',encoding='utf-8').write(html); print(len(html)/1e6,'MB')
