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

## Publicação (uma vez)
Em Settings > Pages, em "Source", escolha **GitHub Actions**.
