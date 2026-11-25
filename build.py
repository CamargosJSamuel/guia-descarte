"""Gera docs/index.html (página única) a partir de dados.py, src/template.html e fotos/."""
import base64, hashlib, io, json, shutil, glob, os
from PIL import Image
from dados import B, I, ERRO_BIN, ERRO_ITEM, CONFUSAO
PH='fotos/'
def jpg(fn,px=400,bg=(255,248,239),fill=0.84):
    """Foto quadrada padronizada: recorta ao objeto, uniformiza o fundo (creme) e centraliza com a mesma margem."""
    import numpy as np
    im=Image.open(PH+fn).convert('RGBA')
    flat=Image.new('RGB',im.size,bg); flat.paste(im,mask=im.split()[3])
    a=np.asarray(flat).astype(int); h,w=a.shape[:2]
    edge=np.concatenate([a[0],a[-1],a[:,0],a[:,-1]])
    b0=np.median(edge,axis=0); diff=np.abs(a-b0).max(axis=2)
    ys,xs=np.where(diff>22)
    out=Image.new('RGB',(px,px),bg)
    if edge.std(axis=0).max()<14 and len(xs)>200:       # fundo uniforme: dá para recortar com segurança
        x0,x1=np.percentile(xs,[0.3,99.7]).astype(int); y0,y1=np.percentile(ys,[0.3,99.7]).astype(int)
        pad=int(0.03*max(w,h)); x0=max(0,x0-pad); y0=max(0,y0-pad); x1=min(w,x1+pad); y1=min(h,y1+pad)
        t=np.clip((diff[y0:y1,x0:x1]-6)/20,0,1)[...,None]   # fundo vira exatamente o creme, sombras suaves ficam
        crop=(np.array(bg)*(1-t)+a[y0:y1,x0:x1]*t).astype('uint8')
        sub=Image.fromarray(crop)
    else:
        sub=flat
    s=min(px*fill/sub.width,px*fill/sub.height,1.15)   # sem ampliar demais (evita desfocar)
    sub=sub.resize((max(1,round(sub.width*s)),max(1,round(sub.height*s))),Image.LANCZOS)
    out.paste(sub,((px-sub.width)//2,(px-sub.height)//2))
    buf=io.BytesIO(); out.save(buf,'JPEG',quality=84,optimize=True)
    return 'data:image/jpeg;base64,'+base64.b64encode(buf.getvalue()).decode()
def png(fn,px):
    im=Image.open(PH+fn).convert('RGBA'); im.thumbnail((px,px)); buf=io.BytesIO(); im.save(buf,'PNG',optimize=True)
    return 'data:image/png;base64,'+base64.b64encode(buf.getvalue()).decode()
items=[dict(n=a,b=b,m=m,i=k,k=kw) for k,(a,b,m,f,kw) in enumerate(I) for b in [b]] if False else [dict(n=a,b=b,m=m,i=k,k=kw) for k,(a,b,m,f,kw) in enumerate(I)]
imgs=[jpg(f) if f else None for (_,_,_,f,_) in I]
kdp=png('logo_kdp.png',900)
html=open('src/template.html',encoding='utf-8').read()
from datetime import datetime
from zoneinfo import ZoneInfo
REV=datetime.now(ZoneInfo('America/Sao_Paulo')).strftime('%d/%m/%Y às %H:%M')
html=html.replace('/*CONF*/',json.dumps(CONFUSAO,ensure_ascii=False)).replace('/*ERRB*/',json.dumps(ERRO_BIN,ensure_ascii=False)).replace('/*ERRI*/',json.dumps(ERRO_ITEM,ensure_ascii=False)).replace('/*ITEMS*/',json.dumps(items,ensure_ascii=False)).replace('/*BINS*/',json.dumps({k:dict(n=v[0],c=v[1],t=v[2]) for k,v in B.items()},ensure_ascii=False)).replace('/*IMGS*/',json.dumps(imgs)).replace('%%KDP%%',kdp).replace('%%REV%%',REV).replace('%%QR%%',open('src/qr.svg',encoding='utf-8').read())
open('docs/index.html','w',encoding='utf-8').write(html); print(len(html)/1e6,'MB')

# arquivos estáticos (ícones, manifesto) e service worker com versão do conteúdo
for f in glob.glob('src/static/*'): shutil.copy(f,'docs/')
v=hashlib.sha1(html.encode('utf-8')).hexdigest()[:10]
open('docs/sw.js','w',encoding='utf-8').write(open('src/sw.js',encoding='utf-8').read().replace('%%V%%',v)); print('sw',v)
