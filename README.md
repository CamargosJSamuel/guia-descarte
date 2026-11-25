# Guia de Descarte

Site de página única (HTML) para consulta de descarte de resíduos. Publicado pelo GitHub Pages.

## Estrutura
- `dados.py`: lixeiras, itens, motivos e fotos. A manutenção do dia a dia é aqui.
- `src/template.html`: layout, estilos e funções do site.
- `fotos/`: fotos dos itens e o logo. O build as reduz e embute na página.
- `build.py`: gera `docs/index.html`.
- `.github/workflows/pages.yml`: gera e publica o site a cada envio para `main`.

## Rodar no computador
```
python -m venv .venv
.venv\Scripts\activate        # Windows (Linux/Mac: source .venv/bin/activate)
pip install -r requirements.txt
python build.py
```
Abra `docs/index.html` no navegador.

## Manutenção
- **Editar motivo ou nome:** altere o texto em `dados.py`.
- **Novo item:** em `dados.py`, inclua o nome numa chamada `N(...)` da lixeira certa e a foto em `PHOTOS` (arquivo em `fotos/site_new/`, PNG quadrado, fundo claro).
- **Remover item:** apague o nome da chamada `N(...)` e a linha em `PHOTOS`.
- **Atualizar a data de revisão:** procure "novembro de 2026" em `src/template.html` (2 lugares).
- Para publicar: `git add . && git commit -m "ajuste" && git push`. O site atualiza em 1 a 2 minutos.

## Explicação de erro no teste rápido
No fim de `dados.py`: `ERRO_BIN` tem um texto por lixeira ("por que não nesta lixeira") e `ERRO_ITEM` tem textos próprios para confusões comuns, criados com `E([itens],[lixeiras erradas],'texto')`. Sem texto próprio, o teste mostra o motivo do item mais o texto da lixeira escolhida.

Alternativas do teste: `CONFUSAO` (em `dados.py`) lista, para cada lixeira correta, as lixeiras que mais confundem. O teste junta isso com os pares de `ERRO_ITEM` para montar opções parecidas.

## Uso sem internet (instalar no celular)
O site vira um aplicativo instalável (PWA). `src/sw.js` guarda a página no aparelho e `src/static/` tem o manifesto e os ícones. A versão do cache muda sozinha a cada build, então ajustes chegam na próxima abertura com internet.

## Buscas sem resultado
Em `src/template.html`, procure `const STATS={code:''}` e coloque o código do seu GoatCounter (ex.: `'guiadescarte'`, de guiadescarte.goatcounter.com). Vazio = desligado. Só registra o termo buscado, sem dados pessoais, uma vez por termo e por visita. Os termos aparecem em "Events" no painel do GoatCounter.

## Publicação (uma vez)
Em Settings > Pages, em "Source", escolha **GitHub Actions**.

## Recursos de uso
- Abas: Guia, Teste e Aprender (Você sabia? e instalação no celular).
- Favoritos: estrela no card ou no resíduo aberto; ficam salvos no aparelho (`gd_f`).
- Link direto: `?r=<nome-do-resíduo>` abre o resíduo; botão Compartilhar no resíduo aberto.
- Fotos: `jpg()` em `build.py` padroniza enquadramento e fundo (quadrado, creme).
