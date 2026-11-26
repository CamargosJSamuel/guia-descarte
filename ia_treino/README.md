# Identificador por foto — como treinar de novo

O modelo aprende com as fotos do próprio guia (`fotos/`). Retreine sempre que incluir ou trocar resíduos.

1. Ambiente (uma vez):
   ```
   python -m venv .venv-ia && .venv-ia/bin/pip install -r ia_treino/requirements.txt
   .venv-ia/bin/pip install --no-deps tensorflowjs==4.22.0
   ```
   Baixe o MobileNet para `ia_treino/dados/`:
   `https://github.com/fchollet/deep-learning-models/releases/download/v0.6/mobilenet_7_5_224_tf_no_top.h5`
2. Recortar os resíduos: `python ia_treino/recorte.py` (confira `ia_treino/dados/prancha_recortes.jpg`).
3. Treinar (≈10 min): `python ia_treino/treinar.py`.
4. Converter para o site:
   ```
   tensorflowjs_converter --input_format keras --quantize_float16 '*' --weight_shard_size_bytes 8388608 ia_treino/dados/modelo_7_5.h5 src/ia
   ```
5. `python3 build.py` e publicar.

Fotos reais (opcional, melhora a precisão): coloque em `ia_treino/fotos_reais/<número do resíduo>/` e inclua no treino.
A ordem das classes é a ordem de `I` em `dados.py`, mais "nenhum resíduo" no fim.
