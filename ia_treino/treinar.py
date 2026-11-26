"""Treina o identificador de resíduos.

Etapa 1: MobileNet congelada extrai características de imagens sintéticas (fotos do guia em fundos variados)
         e de fotos reais (ia_treino/fotos_reais/NN - Nome/*.jpg) aumentadas; uma camada final aprende as classes.
Etapa 2 (FT=1): ajuste fino das últimas camadas da MobileNet com imagens (sintéticas + reais).
Parte das fotos reais fica separada só para teste: é o número que vale para decidir publicar.

Variáveis: ALPHA (7_5 ou 1_0), NT (sintéticas por classe), REP (cópias aumentadas por foto real), FT (0/1), EP_FT.
"""
import os as _os
RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
DADOS = _os.path.join(RAIZ, 'ia_treino', 'dados')
import os, sys, json, time, glob, re, io
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import numpy as np
from multiprocessing import Pool
from PIL import Image, ImageEnhance, ImageFilter, ImageOps
sys.path.insert(0, RAIZ + '/ia_treino'); sys.path.insert(0, RAIZ)
import gerar
from dados import I

ALPHA = os.environ.get('ALPHA', '7_5')
N_TREINO, N_VAL = int(os.environ.get('NT', 200)), 40
REP = int(os.environ.get('REP', 25))
FT, EP_FT = os.environ.get('FT', '0') == '1', int(os.environ.get('EP_FT', 4))
FOTOS = os.environ.get('FOTOS', os.path.join(RAIZ, 'ia_treino', 'fotos_reais'))
NC = len(I) + 1  # última classe = "nenhum resíduo"
OUT = DADOS; os.makedirs(OUT, exist_ok=True)
NOMES = [a for a, *_ in I] + ['(nenhum resíduo)']


# ---------- fotos reais ----------
def fotos_reais():
    """Pastas 'NN - Nome' (NN = 1..76 na ordem de dados.py; 77 = nenhum resíduo). Retorna treino e teste."""
    tr, te = [], []
    r = np.random.default_rng(5)
    for d in sorted(glob.glob(os.path.join(FOTOS, '*'))):
        m = re.match(r'(\d+)', os.path.basename(d))
        if not (m and os.path.isdir(d)): continue
        k = int(m.group(1)) - 1
        if not 0 <= k < NC: continue
        fs = sorted(f for f in glob.glob(os.path.join(d, '**', '*'), recursive=True)
                    if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp', '.jfif')))
        fs = [fs[i] for i in r.permutation(len(fs))]
        nt = len(fs) // 5 if len(fs) >= 5 else (1 if len(fs) >= 3 else 0)  # ~20% para teste
        te += [(f, k) for f in fs[:nt]]; tr += [(f, k) for f in fs[nt:]]
    return tr, te


def abrir(f, s=224):
    im = ImageOps.exif_transpose(Image.open(f)).convert('RGB')
    w, h = im.size; z = min(w, h)
    return im.crop(((w - z) // 2, (h - z) // 2, (w + z) // 2, (h + z) // 2)).resize((s, s), Image.BICUBIC)


def aumentar(r, f):
    """Variação aleatória de uma foto real: recorte, giro, espelho, luz, cor, desfoque, compressão."""
    im = ImageOps.exif_transpose(Image.open(f)).convert('RGB')
    w, h = im.size; z = min(w, h) * r.uniform(.6, 1.0)
    x, y = r.uniform(0, w - z), r.uniform(0, h - z)
    im = im.crop((int(x), int(y), int(x + z), int(y + z))).resize((256, 256), Image.BICUBIC)
    if r.random() < .5: im = im.transpose(Image.FLIP_LEFT_RIGHT)
    im = im.rotate(r.uniform(-25, 25), resample=Image.BILINEAR).crop((16, 16, 240, 240))
    im = ImageEnhance.Brightness(im).enhance(r.uniform(.7, 1.3))
    im = ImageEnhance.Contrast(im).enhance(r.uniform(.75, 1.25))
    im = ImageEnhance.Color(im).enhance(r.uniform(.7, 1.3))
    if r.random() < .3: im = im.filter(ImageFilter.GaussianBlur(r.uniform(.3, 1.5)))
    b = io.BytesIO(); im.save(b, 'JPEG', quality=int(r.integers(40, 95))); b.seek(0)
    return Image.open(b).convert('RGB')


# ---------- lotes de imagens ----------
def _lote_sint(args):
    seed, ks = args; r = np.random.default_rng(seed)
    return np.stack([np.asarray(gerar.compor(r, k if k < len(I) else -1)) for k in ks])


def _lote_real(args):
    seed, fs = args; r = np.random.default_rng(seed)
    return np.stack([np.asarray(aumentar(r, f)) for f in fs])


def backbone():
    import tf_keras as K
    return K.applications.MobileNet(input_shape=(224, 224, 3), alpha={'1_0': 1.0, '7_5': 0.75, '5_0': 0.5}[ALPHA],
                                    include_top=False, weights=f'{DADOS}/mobilenet_{ALPHA}_224_tf_no_top.h5', pooling='avg')


def _emb(bb, lotes, fn, nome):
    xs = []; t = time.time()
    with Pool(2) as p:
        for i, imgs in enumerate(p.imap(fn, lotes)):
            xs.append(bb.predict(imgs.astype('float32') / 127.5 - 1, verbose=0))
            if i % 20 == 0: print(nome, i, '/', len(lotes), f'{time.time() - t:.0f}s', flush=True)
    return np.concatenate(xs) if xs else np.zeros((0, bb.output_shape[-1]))


def emb_sint(bb, nome, n, seed0):
    f = f'{OUT}/emb_{ALPHA}_{nome}_{n}.npz'
    if os.path.exists(f): d = np.load(f); return d['x'], d['y']
    ys = np.array([k for k in range(NC) for _ in range(n * (2 if k == NC - 1 else 1))])
    np.random.default_rng(seed0).shuffle(ys)
    x = _emb(bb, [(seed0 * 100000 + i, ys[i:i + 64]) for i in range(0, len(ys), 64)], _lote_sint, nome)
    np.savez(f, x=x, y=ys); return x, ys


def emb_real(bb, tr):
    if not tr: return np.zeros((0, bb.output_shape[-1])), np.zeros(0, int)
    itens = [(f, k) for f, k in tr for _ in range(REP)]
    np.random.default_rng(3).shuffle(itens)
    x = _emb(bb, [(900000 + i, [f for f, _ in itens[i:i + 64]]) for i in range(0, len(itens), 64)], _lote_real, 'reais')
    return x, np.array([k for _, k in itens])


def relatorio(p, y, titulo):
    if not len(y): print(titulo, ': sem fotos'); return
    top1 = (p.argmax(1) == y).mean(); top3 = np.mean([y[i] in np.argsort(-p[i])[:3] for i in range(len(y))])
    print(f'{titulo}  top-1 {top1:.1%}  top-3 {top3:.1%}  ({len(y)} fotos)')
    erros = {}
    for i in np.where(p.argmax(1) != y)[0]:
        erros.setdefault(NOMES[y[i]], []).append(NOMES[p[i].argmax()])
    for n, e in sorted(erros.items(), key=lambda t: -len(t[1]))[:15]: print(f'   {n} -> {", ".join(e[:4])}')


if __name__ == '__main__':
    import tf_keras as K
    tr, te = fotos_reais()
    print(f'fotos reais: {len(tr)} treino, {len(te)} teste, {len({k for _, k in tr + te})} classes com foto')
    bb = backbone()
    xs, ys = emb_sint(bb, 'treino', N_TREINO, 11)
    xv, yv = emb_sint(bb, 'val', N_VAL, 77)
    xr, yr = emb_real(bb, tr)
    xte = bb.predict(np.stack([np.asarray(abrir(f)) for f, _ in te]).astype('float32') / 127.5 - 1, verbose=0) if te else np.zeros((0, xs.shape[1]))
    yte = np.array([k for _, k in te])
    x = np.concatenate([xs, xr]); y = np.concatenate([ys, yr])
    w = np.concatenate([np.ones(len(ys)), np.full(len(yr), 3.0)])  # foto real pesa mais
    head = K.Sequential([K.layers.Input((x.shape[1],)), K.layers.Dropout(0.3),
                         K.layers.Dense(256, activation='relu'), K.layers.Dropout(0.3),
                         K.layers.Dense(NC, activation='softmax')])
    head.compile(K.optimizers.Adam(1e-3), 'sparse_categorical_crossentropy', ['accuracy'])
    vx, vy = (xte, yte) if len(yte) else (xv, yv)
    head.fit(x, y, sample_weight=w, validation_data=(vx, vy), epochs=80, batch_size=128, verbose=2,
             callbacks=[K.callbacks.EarlyStopping(patience=10, restore_best_weights=True)])
    relatorio(head.predict(xv, verbose=0), yv, 'VALIDAÇÃO SINTÉTICA')
    relatorio(head.predict(xte, verbose=0), yte, 'TESTE COM FOTOS REAIS')

    inp = K.layers.Input((224, 224, 3))
    full = K.Model(inp, head(bb(K.layers.Rescaling(1 / 127.5, offset=-1)(inp))))
    if FT:  # ajuste fino: libera o fim da MobileNet e treina com imagens
        bb.trainable = True
        for l in bb.layers[:-20]: l.trainable = False
        for l in bb.layers:
            if isinstance(l, K.layers.BatchNormalization): l.trainable = False
        full.compile(K.optimizers.Adam(1e-5), 'sparse_categorical_crossentropy', ['accuracy'])

        class Mix(K.utils.Sequence):
            def __init__(s, n): s.n = n
            def __len__(s): return s.n
            def __getitem__(s, i):
                r = np.random.default_rng(int(time.time() * 1e6) % 2**31 + i)
                ks = r.integers(0, NC, 32 if tr else 64)
                a = [np.asarray(gerar.compor(r, k if k < len(I) else -1)) for k in ks]; b = list(ks)
                for j in r.integers(0, len(tr), 32) if tr else []:
                    a.append(np.asarray(aumentar(r, tr[j][0]))); b.append(tr[j][1])
                return np.stack(a).astype('float32'), np.array(b)
        vd = (np.stack([np.asarray(abrir(f)) for f, _ in te]).astype('float32'), yte) if te else None
        full.fit(Mix(int(os.environ.get('STEPS', 150))), epochs=EP_FT, validation_data=vd, verbose=2, workers=2, use_multiprocessing=False)
        if te: relatorio(full.predict(vd[0], verbose=0), yte, 'TESTE COM FOTOS REAIS (após ajuste fino)')
    full.save(f'{OUT}/modelo_{ALPHA}.h5')
    json.dump(NOMES, open(f'{OUT}/classes.json', 'w'), ensure_ascii=False)
    print('salvo', f'{OUT}/modelo_{ALPHA}.h5')
