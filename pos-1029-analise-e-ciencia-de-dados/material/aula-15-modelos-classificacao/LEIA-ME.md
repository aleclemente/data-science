# Aula 15 — Laboratório: Modelos de Classificação

Especialização em Ciência de Dados · Análise e Ciência de Dados · IFRN
Unidade 4 — Aprendizado de Máquina Aplicado (segunda aula)

## Conteúdo do pacote

| Arquivo | O que é |
|---|---|
| `Aula15_Classificacao_Laboratorio.ipynb` | **Laboratório guiado** (tumores de mama benignos × malignos, 569 exames), já executado: baseline, regressão logística, árvore de decisão, random forest e KNN, fronteiras de decisão, validação cruzada, matrizes de confusão, curvas ROC e limiar |
| `Aula15_Exercicio_Pratico.ipynb` | **Exercício prático (treino, não é entregue)**: os mesmos quatro modelos no dataset de diabetes Pima, em 10 passos com o resultado esperado em cada um |
| `Aula15_Exercicio_Gabarito.ipynb` | gabarito comentado do exercício, já executado |
| `dados/breast_cancer_wisconsin.csv` | dados do laboratório — é o `data.csv` do Kaggle, renomeado |
| `dados/diabetes.csv` | dados do exercício — o `diabetes.csv` do Kaggle |
| `figuras/` | gráficos exportados pelo laboratório guiado |
| `requirements.txt` | bibliotecas necessárias (scikit-learn 1.4 ou mais recente) |

## Origem dos dados (Kaggle)

* **Breast Cancer Wisconsin (Diagnostic)** — https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data
  569 exames, 30 medidas dos núcleos celulares, diagnóstico M (maligno) ou B (benigno).
  Original: W. H. Wolberg, W. N. Street e O. L. Mangasarian (Universidade de Wisconsin), UCI Machine Learning Repository.
* **Pima Indians Diabetes** — https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database
  768 pacientes, 8 medidas clínicas, `Outcome` 1 = diabetes.
  Original: National Institute of Diabetes and Digestive and Kidney Diseases (EUA), UCI Machine Learning Repository.

Para baixar você mesmo: crie uma conta gratuita no Kaggle, abra a página do dataset, clique em **Download** e copie o CSV para a pasta `dados/` (no laboratório, troque o caminho para `dados/data.csv`). Os registros são anônimos. Os notebooks são exercícios de aprendizado de máquina, não ferramentas de diagnóstico.

## Como rodar

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook                  # ou abra a pasta no VS Code (extensões Python e Jupyter)
```

Abra os notebooks **a partir desta pasta** (os caminhos `dados/...` são relativos).
