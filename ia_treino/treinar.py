"""Treina o identificador: MobileNet (congelada) extrai características; uma camada final aprende os resíduos."""
import os as _os
RAIZ=_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
DADOS=_os.path.join(RAIZ,'ia_treino','dados')
import os, sys, json, time
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import numpy as np
from multiprocessing import Pool
sys.path.insert(0, RAIZ + '/ia_treino'); sys.path.insert(0, RAIZ)
import gerar
from dados import I

ALPHA = os.environ.get('ALPHA', '7_5')
N_TREINO, N_VAL = int(os.environ.get('NT', 200)), 40
NC = len(I) + 1  # +1 = "nenhum resíduo"
OUT = DADOS


def _lote(args):
    seed, ks = args
    r = np.random.default_rng(seed)
    return np.stack([np.asarray(gerar.compor(r, k if k < len(I) else -1)) for k in ks])


def backbone():
    import tf_keras as K
    return K.applications.MobileNet(input_shape=(224, 224, 3), alpha={'1_0': 1.0, '7_5': 0.75, '5_0': 0.5}[ALPHA], include_top=False,
                                    weights=f'{DADOS}/mobilenet_{ALPHA}_224_tf_no_top.h5', pooling='avg')


def embeddings(nome, n, seed0):
    f = f'{OUT}/emb_{ALPHA}_{nome}.npz'
    if os.path.exists(f): d = np.load(f); return d['x'], d['y']
    ys = np.array([k for k in range(NC) for _ in range(n * (2 if k == NC - 1 else 1))])
    np.random.default_rng(seed0).shuffle(ys)
    lotes = [(seed0 * 100000 + i, ys[i:i + 64]) for i in range(0, len(ys), 64)]
    bb = backbone(); xs = []; t = time.time()
    with Pool(2) as p:
        for i, imgs in enumerate(p.imap(_lote, lotes)):
            xs.append(bb.predict(imgs.astype('float32') / 127.5 - 1, verbose=0))
            if i % 20 == 0: print(nome, i * 64, '/', len(ys), f'{time.time() - t:.0f}s', flush=True)
    x = np.concatenate(xs); np.savez(f, x=x, y=ys); return x, ys


if __name__ == '__main__':
    import tf_keras as K
    xt, yt = embeddings('treino', N_TREINO, 11)
    xv, yv = embeddings('val', N_VAL, 77)
    head = K.Sequential([K.layers.Input((xt.shape[1],)), K.layers.Dropout(0.3),
                         K.layers.Dense(256, activation='relu'), K.layers.Dropout(0.3),
                         K.layers.Dense(NC, activation='softmax')])
    head.compile(K.optimizers.Adam(1e-3), 'sparse_categorical_crossentropy', ['accuracy'])
    head.fit(xt, yt, validation_data=(xv, yv), epochs=60, batch_size=128, verbose=2,
             callbacks=[K.callbacks.EarlyStopping(patience=8, restore_best_weights=True)])
    p = head.predict(xv, verbose=0)
    top1 = (p.argmax(1) == yv).mean(); top3 = np.mean([yv[i] in np.argsort(-p[i])[:3] for i in range(len(yv))])
    print(f'VALIDAÇÃO (sintética)  top-1 {top1:.1%}  top-3 {top3:.1%}')
    nomes = [a for a, *_ in I] + ['(nenhum resíduo)']
    acc = {nomes[k]: float((p.argmax(1)[yv == k] == k).mean()) for k in range(NC)}
    for n, a in sorted(acc.items(), key=lambda t: t[1])[:12]: print(f'  {a:.0%}  {n}')
    # modelo completo: imagem 224x224 (0..255) -> probabilidades
    bb = backbone()
    inp = K.layers.Input((224, 224, 3))
    x = K.layers.Rescaling(1 / 127.5, offset=-1)(inp)
    out = head(bb(x))
    full = K.Model(inp, out); full.save(f'{OUT}/modelo_{ALPHA}.h5')
    json.dump(nomes, open(f'{OUT}/classes.json', 'w'), ensure_ascii=False)
    print('salvo')
