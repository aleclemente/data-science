# Atividade 08 — Web scraping com BeautifulSoup

**Disciplina:** POS.1029 — Análise e Ciência de Dados · **Professor:** Plácido Neto · **Avaliada:** sim

## Enunciado

Completar o exercício prático da aula (os trechos `# TODO`) e entregar o notebook executado, com os arquivos CSV/JSON gerados. O ponto de partida e o laboratório guiado estão em [material/aula-08-web-scraping/](../../material/aula-08-web-scraping/).

## O que foi feito

- **Parte A — Estante Potiguar:** raspagem do mini-site fictício de resenhas, servido em `localhost`, depois de consultar o `robots.txt`.
- **Parte B — Books to Scrape:** raspagem das 5 primeiras páginas do catálogo do site real de treino.
- **Parte C — Salvar e refletir:** resultados em CSV e JSON, e uma reflexão ética (`robots.txt`, `User-Agent` identificado, intervalo entre requisições e LGPD).

## Arquivos

- [atividade-08-web-scraping.ipynb](atividade-08-web-scraping.ipynb): a solução.

## Como rodar

Notebook local, porque precisa do mini-site do material do professor: rode com o ambiente da raiz ([INSTRUCOES_EXECUCAO.md](../../../INSTRUCOES_EXECUCAO.md)) a partir desta pasta. O notebook coloca o site no ar em `http://localhost:8000/`, lendo `../../material/aula-08-web-scraping/site_resenhas`. A Parte B precisa de internet.

**Diferença em relação à versão entregue:** só o caminho do `site_resenhas`, que mudou com a reorganização do repositório.
