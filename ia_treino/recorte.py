"""Extrai cada resíduo (RGBA) das fotos do site, removendo o fundo creme/uniforme."""
import os as _os
RAIZ=_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
DADOS=_os.path.join(RAIZ,'ia_treino','dados')
import sys, os, numpy as np
from PIL import Image
sys.path.insert(0, RAIZ)
from dados import I
OUT = DADOS + '/recortes'; os.makedirs(OUT, exist_ok=True)

def recorte(path):
    im = Image.open(path).convert('RGB'); a = np.asarray(im).astype(int)
    edge = np.concatenate([a[0], a[-1], a[:, 0], a[:, -1]])
    b0 = np.median(edge, axis=0); diff = np.abs(a - b0).max(axis=2)
    # fundo = região de baixa diferença ligada à borda; o resto (inclusive partes brancas internas) é o objeto
    from scipy import ndimage
    lab, _ = ndimage.label(diff < 7)
    borda = np.unique(np.concatenate([lab[0], lab[-1], lab[:, 0], lab[:, -1]]))
    fundo = np.isin(lab, borda[borda > 0])
    obj = ndimage.binary_opening(~fundo, iterations=1)
    alpha = np.clip(ndimage.gaussian_filter(obj.astype(float), 1.0), 0, 1)
    if edge.std(axis=0).max() >= 14:  # fundo não uniforme: usa a foto inteira
        alpha = np.ones_like(alpha)
    ys, xs = np.where(alpha > 0.3)
    y0, y1, x0, x1 = ys.min(), ys.max() + 1, xs.min(), xs.max() + 1
    rgba = np.dstack([a, (alpha * 255)]).astype('uint8')[y0:y1, x0:x1]
    return Image.fromarray(rgba, 'RGBA'), edge.std(axis=0).max()

if __name__ == '__main__':
    tiles = []
    for k, (n, b, m, f, kw) in enumerate(I):
        r, sd = recorte(RAIZ+'/fotos/' + f)
        r.save(f'{OUT}/{k:02d}.png')
        if sd >= 14: print('fundo não uniforme:', k, n, round(sd))
        t = Image.new('RGB', (160, 160), (40, 90, 160)); r2 = r.copy(); r2.thumbnail((150, 150))
        t.paste(r2, ((160 - r2.width) // 2, (160 - r2.height) // 2), r2); tiles.append(t)
    sheet = Image.new('RGB', (160 * 10, 160 * 8), 'white')
    for i, t in enumerate(tiles): sheet.paste(t, ((i % 10) * 160, (i // 10) * 160))
    sheet.save(DADOS + '/prancha_recortes.jpg', quality=80)
