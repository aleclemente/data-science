# Data Science Postgraduate Specialization

This repository contains source code, notes, and materials for the **Postgraduate Specialization in Data Science** program at **IFRN** (Instituto Federal do Rio Grande do Norte).

## About

This specialization provides comprehensive training in data science concepts, techniques, and practical applications. The repository serves as a centralized hub for course materials, assignments, and collaborative projects. Most of the content is portuguese brazilian and organized by course modules, making it easy for students to navigate and access relevant resources.

## Courses and activities

The repository is organized **by course, then by class or activity**. Each course folder is named after its IFRN code; each activity folder has its own README with the assignment, what was done, and how to run it.

| Course | Activity | What was done | Notebook |
|---|---|---|---|
| [POS.1029 — Análise e Ciência de Dados](pos-1029-analise-e-ciencia-de-dados/) | [Aula 06 — Processos e fontes de dados](pos-1029-analise-e-ciencia-de-dados/aula-06-processos-e-fontes-de-dados/) | Collect from JSON and a public API (CNES), store in SQLite, query with SQL, export to CSV/Parquet, web-scraping ethics checklist | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/aleclemente/data-science/blob/main/pos-1029-analise-e-ciencia-de-dados/aula-06-processos-e-fontes-de-dados/Aula06_Processos_e_Fontes_de_Dados.ipynb) |
| | [Aula 07 — Coleta de dataset real via API](pos-1029-analise-e-ciencia-de-dados/aula-07-coleta-via-api/) | Mini-project: collect real datasets from the IBGE and TSE open-data APIs, with pagination and a provenance block, saved to JSON/CSV | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/aleclemente/data-science/blob/main/pos-1029-analise-e-ciencia-de-dados/aula-07-coleta-via-api/app/Aula-07-coleta-de-dataset-real-via-API.ipynb) |
| | [Aula 08 — Web scraping com BeautifulSoup](pos-1029-analise-e-ciencia-de-dados/aula-08-web-scraping/) | Scrape a fictional local book-review site (served on localhost), respecting `robots.txt`, and save the reviews to CSV/JSON; guided lab plus exercise | Local notebook (needs the bundled site) |
| | [Aula 09 — Qualidade de dados e limpeza](pos-1029-analise-e-ciencia-de-dados/aula-09-qualidade-limpeza/) | Diagnose and clean a synthetic triage dataset: missing values, duplicates, inconsistent categories, wrong units and tidy data; guided lab plus practice exercise | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/aleclemente/data-science/blob/main/pos-1029-analise-e-ciencia-de-dados/aula-09-qualidade-limpeza/Aula09_Qualidade_e_Limpeza_de_Dados.ipynb) |
| | [Aula 10 — Pipeline de limpeza completo](pos-1029-analise-e-ciencia-de-dados/aula-10-pipeline-limpeza/) | Graded delivery: end-to-end ETL cleaning of a synthetic lab-exams dataset, documented notebook, cleaned dataset and data dictionary; plus the professor's guided lab and practice exercise | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/aleclemente/data-science/blob/main/pos-1029-analise-e-ciencia-de-dados/aula-10-pipeline-limpeza/Aula10_Entrega_Alexandre_Clemente.ipynb) |
| | [Aula 12 — Laboratório: Matplotlib, Seaborn e Plotly](pos-1029-analise-e-ciencia-de-dados/aula-12-lab-matplotlib-seaborn-plotly/) | Professor's lab package: guided example on a synthetic delivery dataset (histogram, boxplot, violin, scatter, bars, correlation heatmap, palettes, management panel, interactive Plotly charts) plus a practice exercise with answer key | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/aleclemente/data-science/blob/main/pos-1029-analise-e-ciencia-de-dados/aula-12-lab-matplotlib-seaborn-plotly/Aula12_Visualizacao_Laboratorio.ipynb) |
| | [Aula 14 — scikit-learn e o fluxo de ML](pos-1029-analise-e-ciencia-de-dados/aula-14-scikit-learn-fluxo-ml/) | Graded practical work: classification on a synthetic delivery dataset (dissatisfied customers), with train/test split, a baseline, a logistic-regression pipeline, a second model and cross-validation; plus the professor's guided example | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/aleclemente/data-science/blob/main/pos-1029-analise-e-ciencia-de-dados/aula-14-scikit-learn-fluxo-ml/Aula14_Alexandre_Clemente.ipynb) |
| [POS.1035 — Estatística Aplicada à Ciência de Dados](pos-1035-estatistica-aplicada/) | [Atividade 01 — Média e desvio padrão](pos-1035-estatistica-aplicada/atividade-01-desvio-padrao/) | Show that the mean minimizes the sum of squared deviations, compute the sample standard deviation, plot the comparison | Python script |
| [POS.1036 — Introdução ao Aprendizado de Máquina](pos-1036-aprendizado-de-maquina/) | [Atividade 01 — Centroides, câncer de mama](pos-1036-aprendizado-de-maquina/entregas/atividade-01-centroides-cancer-de-mama/) | Nearest-centroid classifier on Breast Cancer Wisconsin (Original): missing rows and ID dropped, stratified split, overall and per-class accuracy (96.35%). Professor material in [material/](pos-1036-aprendizado-de-maquina/material/) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/aleclemente/ciencias-de-dados/blob/main/pos-1036-aprendizado-de-maquina/entregas/atividade-01-centroides-cancer-de-mama/atividade-01-centroides-cancer-de-mama.ipynb) |

Other folders:

- [pos-1029-analise-e-ciencia-de-dados/tutorial_python/](pos-1029-analise-e-ciencia-de-dados/tutorial_python/) — Python warm-up exercises (lists, functions, NumPy).

## Getting Started

Clone this repository and explore the organized folders by course module or topic.

### Environment Setup & Running Scripts

To set up the Python virtual environment (`venv`) and run scripts without missing module errors (e.g. `ModuleNotFoundError: No module named 'matplotlib'`), refer to the step-by-step guide in [**INSTRUCOES_EXECUCAO.md**](INSTRUCOES_EXECUCAO.md).

## Contributing

Feel free to contribute improvements, fixes, or additional resources to enhance the learning experience.

---

*Postgraduate Specialization in Data Science | IFRN*