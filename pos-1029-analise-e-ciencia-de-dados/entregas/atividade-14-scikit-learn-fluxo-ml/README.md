# Atividade 14 — scikit-learn e o fluxo de ML

**Disciplina:** POS.1029 — Análise e Ciência de Dados · **Professor:** Plácido Neto · **Avaliada:** sim (trabalho prático, 100 pontos)

## Enunciado

Aplicar o fluxo de trabalho do scikit-learn ao dataset de delivery da hamburgueria (600 pedidos fictícios) para responder: a partir das informações do pedido e da entrega, o modelo identifica os clientes insatisfeitos (avaliação ≤ 3)? O enunciado e o exemplo guiado estão em [material/aula-14-scikit-learn-fluxo-ml/](../../material/aula-14-scikit-learn-fluxo-ml/).

## O que foi feito

As 7 etapas pontuadas: alvo e proporção das classes → X, y e divisão estratificada → baseline → pipeline com regressão logística → segundo modelo (floresta aleatória) → validação cruzada → conclusão.

## Resultado

A escolha foi a regressão logística, pelo ROC-AUC (0,787 na validação cruzada e 0,799 no teste), com o F1 como desempate. Só a acurácia não serve: com 27,8% de insatisfeitos, o baseline acerta 72% prevendo sempre "satisfeito" e tem F1 = 0.

## Arquivos

- [atividade-14-scikit-learn-fluxo-ml.ipynb](atividade-14-scikit-learn-fluxo-ml.ipynb): a solução, revisada etapa por etapa (a versão entregue no Moodle).

## Como rodar

Rode com o ambiente da raiz ([INSTRUCOES_EXECUCAO.md](../../../INSTRUCOES_EXECUCAO.md)) a partir desta pasta. O notebook lê `../../material/aula-14-scikit-learn-fluxo-ml/dados/delivery_hamburgueria.csv`, sem precisar de internet.

**Diferença em relação à versão entregue:** só o caminho do CSV, que mudou com a reorganização do repositório.
