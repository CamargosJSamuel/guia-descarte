"""Gera imagens de treino sintéticas: cada resíduo recortado é colado em fundos variados,
com variações de tamanho, rotação, luz, cor, sombra, desfoque, ruído e compressão."""
import os as _os
RAIZ=_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
DADOS=_os.path.join(RAIZ,'ia_treino','dados')
import glob, io, math, random
import numpy as np
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter

S = 224
RECORTES = sorted(glob.glob(DADOS + '/recortes/*.png'))
_cache = {}


def recorte(k):
    if k not in _cache:
        im = Image.open(RECORTES[k]).convert('RGBA'); im.thumbnail((400, 400)); _cache[k] = im
    return _cache[k]


def _ruido(r, s, escala):
    g = r.normal(0, 1, (max(2, s // escala), max(2, s // escala)))
    return np.asarray(Image.fromarray(g.astype('float32')).resize((s, s), Image.BICUBIC))


def fundo(r):
    """Fundo procedural: mesa, chão, parede, tecido, madeira, azulejo, gradiente."""
    s = 320
    paletas = [(235, 235, 232), (250, 248, 244), (200, 200, 200), (120, 120, 120), (60, 60, 62), (30, 30, 30),
               (190, 160, 120), (150, 110, 70), (100, 70, 45), (210, 190, 160), (170, 180, 190), (90, 110, 130),
               (60, 80, 60), (140, 150, 120), (220, 210, 190), (180, 60, 50), (40, 70, 120), (230, 220, 120)]
    base = np.array(paletas[r.integers(len(paletas))], float) + r.normal(0, 15, 3)
    t = r.integers(7)
    img = np.ones((s, s, 3)) * base
    if t == 0:  # liso com textura leve
        img += _ruido(r, s, r.integers(4, 40))[..., None] * r.uniform(3, 12)
    elif t == 1:  # madeira
        y = np.linspace(0, 1, s)[:, None] * np.ones((1, s))
        warp = _ruido(r, s, 32) * r.uniform(0.5, 2)
        veio = np.sin((y * r.uniform(15, 60) + warp) * math.pi)
        img = img * (1 + 0.12 * veio[..., None]) + _ruido(r, s, 3)[..., None] * 6
        if r.random() < 0.5: img = img.transpose(1, 0, 2)
    elif t == 2:  # granito / concreto
        img += _ruido(r, s, 1)[..., None] * r.uniform(8, 30) + _ruido(r, s, 20)[..., None] * 10
    elif t == 3:  # azulejo / piso
        n = r.integers(2, 7); w = s // n
        img = img.copy(); cor_rej = base * r.uniform(0.5, 0.9)
        for i in range(n + 1):
            img[max(0, i * w - 2):i * w + 2, :] = cor_rej; img[:, max(0, i * w - 2):i * w + 2] = cor_rej
        img += _ruido(r, s, 6)[..., None] * 5
    elif t == 4:  # tecido xadrez / listrado
        a = r.uniform(0.05, 0.2); p = r.integers(6, 30)
        xx = (np.arange(s) // p) % 2
        img = img * (1 - a * (xx[None, :] if r.random() < .5 else (xx[None, :] ^ xx[:, None])))[..., None]
    elif t == 5:  # gradiente de luz
        g = np.linspace(r.uniform(.5, 1), r.uniform(1, 1.4), s)
        img = img * (g[:, None] if r.random() < .5 else g[None, :])[..., None]
    else:  # duas superfícies (mesa + parede)
        c2 = np.array(paletas[r.integers(len(paletas))], float)
        cut = r.integers(s // 4, 3 * s // 4); img[:cut] = c2
        img += _ruido(r, s, 10)[..., None] * 6
    im = Image.fromarray(np.clip(img, 0, 255).astype('uint8'))
    if r.random() < 0.3:  # objetos genéricos ao fundo (formas)
        d = ImageDraw.Draw(im)
        for _ in range(r.integers(1, 4)):
            c = tuple(int(v) for v in r.integers(0, 255, 3)); x, y = r.integers(0, s, 2); w, h = r.integers(20, 90, 2)
            (d.ellipse if r.random() < .5 else d.rectangle)([x, y, x + w, y + h], fill=c)
    ang = r.uniform(0, 360)
    c = (s - S) // 2
    return im.rotate(ang, resample=Image.BILINEAR, expand=False).crop((c, c, c + S, c + S))


def mao(r, im):
    """Desenha uma mão estilizada (tom de pele) entrando pela borda."""
    tons = [(241, 194, 167), (224, 172, 135), (198, 134, 96), (141, 85, 54), (95, 60, 40)]
    c = np.array(tons[r.integers(len(tons))]) + r.integers(-12, 12, 3)
    lay = Image.new('RGBA', (S, S), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    cx, cy = r.integers(40, 184), S + 10; w = r.integers(60, 110)
    d.ellipse([cx - w // 2, cy - w, cx + w // 2, cy + w // 3], fill=tuple(c) + (255,))
    for i in range(4):
        fx = cx - w // 2 + 8 + i * (w - 16) // 3
        d.rounded_rectangle([fx - 8, cy - w - r.integers(30, 60), fx + 8, cy - w // 2], 8, fill=tuple(c) + (255,))
    lay = lay.rotate(r.uniform(0, 360), center=(S / 2, S / 2)).filter(ImageFilter.GaussianBlur(1))
    im.paste(lay, (0, 0), lay)


def objeto(r, k):
    o = recorte(k)
    if r.random() < 0.5: o = o.transpose(Image.FLIP_LEFT_RIGHT)
    if r.random() < 0.15:  # recorte parcial (só um pedaço do resíduo aparece)
        w, h = o.size; f = r.uniform(.6, .9)
        x0, y0 = int(r.uniform(0, 1 - f) * w), int(r.uniform(0, 1 - f) * h)
        o = o.crop((x0, y0, x0 + int(f * w), y0 + int(f * h)))
    rgb, a = o.convert('RGB'), o.split()[3]
    rgb = ImageEnhance.Brightness(rgb).enhance(r.uniform(.65, 1.3))
    rgb = ImageEnhance.Contrast(rgb).enhance(r.uniform(.7, 1.3))
    rgb = ImageEnhance.Color(rgb).enhance(r.uniform(.6, 1.35))
    o = rgb.convert('RGBA'); o.putalpha(a)
    ang = r.uniform(-180, 180) if r.random() < .5 else r.uniform(-25, 25)
    o = o.rotate(ang, resample=Image.BICUBIC, expand=True)
    # perspectiva leve (achata em uma direção)
    sx, sy = r.uniform(.8, 1.2), r.uniform(.8, 1.2)
    lado = r.uniform(.45, 1.0) * S
    esc = lado / max(o.size)
    return o.resize((max(4, int(o.width * esc * sx)), max(4, int(o.height * esc * sy))), Image.BICUBIC)


def compor(r, k):
    """k = índice do resíduo; k = -1 gera só fundo (classe 'nenhum resíduo')."""
    im = fundo(r).convert('RGBA')
    if k >= 0:
        o = objeto(r, k)
        m = .12
        x = int(r.uniform(-m * o.width, S - (1 - m) * o.width)) if o.width < S else int(r.uniform(S - o.width, 0))
        y = int(r.uniform(-m * o.height, S - (1 - m) * o.height)) if o.height < S else int(r.uniform(S - o.height, 0))
        if r.random() < .7:  # sombra
            sh = Image.new('RGBA', o.size, (0, 0, 0, 0)); al = o.split()[3].point(lambda v: v * r.uniform(.25, .55))
            sh.putalpha(al); sh = sh.filter(ImageFilter.GaussianBlur(r.uniform(3, 9)))
            im.paste(sh, (x + int(r.integers(-8, 12)), y + int(r.integers(2, 14))), sh)
        im.paste(o, (x, y), o)
    if r.random() < (.2 if k >= 0 else .4): mao(r, im)
    im = im.convert('RGB')
    # cena inteira: tom de luz, desfoque, ruído, compressão
    a = np.asarray(im).astype(float)
    a *= np.array([r.uniform(.85, 1.15), r.uniform(.9, 1.1), r.uniform(.85, 1.15)])
    a = a * r.uniform(.7, 1.2) + r.uniform(-20, 20)
    if r.random() < .3:  # vinheta / luz desigual
        yy, xx = np.mgrid[0:S, 0:S] / S - .5; a *= (1 - r.uniform(.2, .6) * (xx ** 2 + yy ** 2))[..., None]
    a += r.normal(0, r.uniform(0, 8), a.shape)
    im = Image.fromarray(np.clip(a, 0, 255).astype('uint8'))
    if r.random() < .35: im = im.filter(ImageFilter.GaussianBlur(r.uniform(.4, 1.8)))
    buf = io.BytesIO(); im.save(buf, 'JPEG', quality=int(r.integers(35, 95))); buf.seek(0)
    return Image.open(buf).convert('RGB')


if __name__ == '__main__':
    r = np.random.default_rng(1)
    sheet = Image.new('RGB', (S * 8, S * 4))
    ks = [0, 13, 19, 32, 44, 49, 57, 70, 5, 26, 38, 60, 66, 72, 15, -1, 1, 8, 22, 30, 41, 52, 64, 75, 3, 12, 29, 47, 55, 68, 74, -1]
    for i, k in enumerate(ks): sheet.paste(compor(r, k), ((i % 8) * S, (i // 8) * S))
    sheet.resize((S * 4, S * 2)).save(DADOS + '/prancha_treino.jpg', quality=85)
