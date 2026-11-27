# Especialização em Ciência de Dados — IFRN

**Português** | [English](README.en.md)

Meu trabalho na **Especialização em Ciência de Dados do IFRN** (Instituto Federal do Rio Grande do Norte), de ago/2026 a ~jun/2027: notebooks, scripts e dados das atividades de cada disciplina, junto com o material que os professores distribuíram.

## Como está organizado

Uma pasta por disciplina, com o código do IFRN no nome. Dentro de cada uma:

- **`material/`**: o que o professor distribuiu, sem edição (notebooks, dados, enunciados, slides), com o crédito e a licença quando há.
- **`entregas/`**: o que eu fiz, uma pasta `atividade-NN-tema/` por atividade, com um README que traz o enunciado, o que foi feito, o resultado e como rodar.

Uma atividade só é publicada aqui depois do prazo de entrega.

## Disciplinas (2026.2)

| Disciplina | Professor | Pasta |
|---|---|---|
| POS.1029 — Análise e Ciência de Dados | Plácido Neto | [pos-1029-analise-e-ciencia-de-dados/](pos-1029-analise-e-ciencia-de-dados/) |
| POS.1035 — Estatística Aplicada à Ciência de Dados | João Maria Filgueira | [pos-1035-estatistica-aplicada/](pos-1035-estatistica-aplicada/) |
| POS.1036 — Introdução ao Aprendizado de Máquina | Alexandre Lima | [pos-1036-aprendizado-de-maquina/](pos-1036-aprendizado-de-maquina/) |
| POS.0964 — Metodologia Aplicada ao TCC I | Gustavo Fontoura | o TCC terá repositório próprio |

## Entregas

| Disciplina | Atividade | O que foi feito | Notebook |
|---|---|---|---|
| POS.1029 | [04 — Laboratório NumPy e Pandas I](pos-1029-analise-e-ciencia-de-dados/entregas/atividade-04-numpy-pandas-i/) | Leitura correta de CSV, `loc`/`iloc`, filtragem booleana, ausentes e cruzamento com Excel nas matrículas sintéticas do IFRN | Colab com Drive |
| POS.1029 | [05 — Laboratório Pandas II](pos-1029-analise-e-ciencia-de-dados/entregas/atividade-05-pandas-ii-agrupamentos-joins/) | `groupby`, `agg`, `pivot_table`, `merge` (left × inner), `apply` e *method chaining* nas mesmas matrículas | Colab com Drive |
| POS.1029 | [06 — Processos e fontes de dados](pos-1029-analise-e-ciencia-de-dados/entregas/atividade-06-processos-e-fontes-de-dados/) | Coleta pela API do CNES, carga em SQLite, consulta SQL, exportação para CSV/Parquet e checklist de ética do scraping | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/aleclemente/data-science/blob/main/pos-1029-analise-e-ciencia-de-dados/entregas/atividade-06-processos-e-fontes-de-dados/atividade-06-processos-e-fontes-de-dados.ipynb) |
| POS.1029 | [07 — Coleta de dataset real via API](pos-1029-analise-e-ciencia-de-dados/entregas/atividade-07-coleta-via-api/) | Mini-projeto: datasets das APIs abertas do IBGE e do TSE, com paginação e bloco de proveniência, salvos em JSON/CSV | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/aleclemente/data-science/blob/main/pos-1029-analise-e-ciencia-de-dados/entregas/atividade-07-coleta-via-api/atividade-07-coleta-via-api.ipynb) |
| POS.1029 | [08 — Web scraping com BeautifulSoup](pos-1029-analise-e-ciencia-de-dados/entregas/atividade-08-web-scraping/) | Raspagem de um site fictício de resenhas (em localhost) e do Books to Scrape, respeitando o `robots.txt`, com saída em CSV/JSON | local |
| POS.1029 | [09 — Qualidade de dados e limpeza](pos-1029-analise-e-ciencia-de-dados/entregas/atividade-09-qualidade-limpeza/) | Exercício de treino: duplicatas, categorias, outliers pelo IQR, regras de domínio e ausentes em dados sintéticos de triagem | Colab com Drive |
| POS.1029 | [10 — Pipeline de limpeza completo](pos-1029-analise-e-ciencia-de-dados/entregas/atividade-10-pipeline-limpeza/) | Pipeline ETL documentado de exames laboratoriais sintéticos, com dataset limpo, validação e dicionário de dados | local |
| POS.1029 | [14 — scikit-learn e o fluxo de ML](pos-1029-analise-e-ciencia-de-dados/entregas/atividade-14-scikit-learn-fluxo-ml/) | Classificação dos clientes insatisfeitos de um delivery fictício: baseline, pipeline de regressão logística, floresta aleatória e validação cruzada | local |
| POS.1035 | [01 — Desvio padrão](pos-1035-estatistica-aplicada/entregas/atividade-01-desvio-padrao/) | A média minimiza a soma dos desvios quadráticos; desvio padrão amostral e gráfico comparativo | script Python |
| POS.1035 | [02 — Fatores do Valor Adicionado no RN](pos-1035-estatistica-aplicada/entregas/atividade-02-fatores-valor-adicionado/) | Artigo com dados do IBGE/SIDRA sobre Guamaré (Indústria), Natal (Serviços) e Ceará-Mirim (Administração Pública), escrito com 3 IAs conciliadas | artigo (.docx) |
| POS.1036 | [01 — Centroides, câncer de mama](pos-1036-aprendizado-de-maquina/entregas/atividade-01-centroides-cancer-de-mama/) | Classificador por centroides médios no Breast Cancer Wisconsin (Original): acurácia geral e por classe (96,35%) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/aleclemente/data-science/blob/main/pos-1036-aprendizado-de-maquina/entregas/atividade-01-centroides-cancer-de-mama/atividade-01-centroides-cancer-de-mama.ipynb) |

## Como rodar

Crie o ambiente virtual na raiz a partir do [requirements.txt](requirements.txt). O passo a passo, com os erros comuns, está em [INSTRUCOES_EXECUCAO.md](INSTRUCOES_EXECUCAO.md). Os notebooks que leem arquivos do material do professor rodam a partir da pasta da própria entrega.
