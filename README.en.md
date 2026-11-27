# Data Science Specialization — IFRN

[Português](README.md) | **English**

My work in the **Data Science Specialization at IFRN** (Federal Institute of Rio Grande do Norte, Brazil), Aug 2026 to ~Jun 2027: notebooks, scripts and data for each course's assignments, alongside the material the professors handed out. The content itself is in Brazilian Portuguese.

## How it is organized

One folder per course, named after its IFRN code. Inside each one:

- **`material/`**: what the professor handed out, unedited (notebooks, data, assignment statements, slides), with credit and license where available.
- **`entregas/`** ("deliverables"): my own work, one `atividade-NN-tema/` ("activity-NN-topic") folder per assignment, each with a README covering the assignment, what was done, the result and how to run it.

An assignment is published here only after its due date.

## Courses (2026.2)

| Course | Professor | Folder |
|---|---|---|
| POS.1029 — Data Analysis and Data Science | Plácido Neto | [pos-1029-analise-e-ciencia-de-dados/](pos-1029-analise-e-ciencia-de-dados/) |
| POS.1035 — Applied Statistics for Data Science | João Maria Filgueira | [pos-1035-estatistica-aplicada/](pos-1035-estatistica-aplicada/) |
| POS.1036 — Introduction to Machine Learning | Alexandre Lima | [pos-1036-aprendizado-de-maquina/](pos-1036-aprendizado-de-maquina/) |
| POS.0964 — Thesis Methodology I | Gustavo Fontoura | the thesis will have its own repository |

## Deliverables

| Course | Activity | What was done | Notebook |
|---|---|---|---|
| POS.1029 | [06 — Data processes and sources](pos-1029-analise-e-ciencia-de-dados/entregas/atividade-06-processos-e-fontes-de-dados/) | Collect from the CNES public API, load into SQLite, query with SQL, export to CSV/Parquet, web-scraping ethics checklist | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/aleclemente/ciencias-de-dados/blob/main/pos-1029-analise-e-ciencia-de-dados/entregas/atividade-06-processos-e-fontes-de-dados/atividade-06-processos-e-fontes-de-dados.ipynb) |
| POS.1029 | [07 — Real dataset collection via API](pos-1029-analise-e-ciencia-de-dados/entregas/atividade-07-coleta-via-api/) | Mini-project: datasets from the IBGE and TSE open-data APIs, with pagination and a provenance block, saved to JSON/CSV | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/aleclemente/ciencias-de-dados/blob/main/pos-1029-analise-e-ciencia-de-dados/entregas/atividade-07-coleta-via-api/atividade-07-coleta-via-api.ipynb) |
| POS.1029 | [08 — Web scraping with BeautifulSoup](pos-1029-analise-e-ciencia-de-dados/entregas/atividade-08-web-scraping/) | Scrape a fictional review site (on localhost) and Books to Scrape, respecting `robots.txt`, output to CSV/JSON | local |
| POS.1029 | [09 — Data quality and cleaning](pos-1029-analise-e-ciencia-de-dados/entregas/atividade-09-qualidade-limpeza/) | Practice exercise: duplicates, categories, IQR outliers, domain rules and missing values on synthetic triage data | Colab with Drive |
| POS.1029 | [10 — Full cleaning pipeline](pos-1029-analise-e-ciencia-de-dados/entregas/atividade-10-pipeline-limpeza/) | Documented ETL pipeline for synthetic lab exams, with cleaned dataset, validation and data dictionary | local |
| POS.1029 | [14 — scikit-learn and the ML workflow](pos-1029-analise-e-ciencia-de-dados/entregas/atividade-14-scikit-learn-fluxo-ml/) | Classify dissatisfied customers of a fictional delivery: baseline, logistic-regression pipeline, random forest and cross-validation | local |
| POS.1035 | [01 — Standard deviation](pos-1035-estatistica-aplicada/entregas/atividade-01-desvio-padrao/) | The mean minimizes the sum of squared deviations; sample standard deviation and comparison chart | Python script |
| POS.1035 | [02 — Value-added drivers in Rio Grande do Norte](pos-1035-estatistica-aplicada/entregas/atividade-02-fatores-valor-adicionado/) | Article on IBGE/SIDRA data for Guamaré (industry), Natal (services) and Ceará-Mirim (public administration), drafted with 3 AIs and reconciled | article (.docx) |
| POS.1036 | [01 — Centroids, breast cancer](pos-1036-aprendizado-de-maquina/entregas/atividade-01-centroides-cancer-de-mama/) | Nearest-centroid classifier on Breast Cancer Wisconsin (Original): overall and per-class accuracy (96.35%) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/aleclemente/ciencias-de-dados/blob/main/pos-1036-aprendizado-de-maquina/entregas/atividade-01-centroides-cancer-de-mama/atividade-01-centroides-cancer-de-mama.ipynb) |

## Running

Create the virtual environment at the root from [requirements.txt](requirements.txt). The step-by-step guide, with common errors, is in [INSTRUCOES_EXECUCAO.md](INSTRUCOES_EXECUCAO.md) (Portuguese). Notebooks that read files from the professor's material run from their own deliverable folder.
