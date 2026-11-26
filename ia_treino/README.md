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

## Fotos reais (o que mais melhora a precisão)
- Pastas `ia_treino/fotos_reais/NN - Nome/` (NN = 01 a 76 na ordem de `I` em `dados.py`; `77 - Nenhum resíduo` = fotos sem resíduo). O nome depois do número é livre.
- O que fotografar em cada pasta: `variacoes.py` (gera o kit "Guia Descarte - fotos para treino").
- ~20% das fotos de cada pasta ficam fora do treino, só para teste: o "TESTE COM FOTOS REAIS" é o número que decide se publica.
- Opções: `ALPHA=1_0` (MobileNet maior), `NT=400` (mais sintéticas), `REP=25` (variações por foto real), `FT=1` (ajuste fino, mais lento).
- As fotos reais não vão para o repositório (pasta ignorada pelo git).
- Ao incluir resíduo novo no fim de `I`, crie a pasta com o próximo número e renumere "Nenhum resíduo" para o último.
