# Atividade 01 — Detecção de câncer de mama com centroides médios

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/aleclemente/ciencias-de-dados/blob/main/pos-1036-aprendizado-de-maquina/entregas/atividade-01-centroides-cancer-de-mama/atividade-01-centroides-cancer-de-mama.ipynb)

**Disciplina:** POS.1036 — Introdução ao Aprendizado de Máquina · **Professor:** Alexandre Lima · **Avaliada:** sim

## Enunciado

> Implementar um modelo de aprendizado de máquina que prevê se um nódulo mamário é de natureza benigna ou maligna, sobre o conjunto de dados [Breast Cancer Wisconsin (Original)](https://archive.ics.uci.edu/dataset/15/breast+cancer+wisconsin+original).
>
> Antes de iniciar a implementação, faça uma pesquisa sobre como o conjunto de dados foi gerado e qual é o significado de cada atributo preditivo.
>
> O conjunto de dados possui algumas instâncias com dados ausentes, as quais devem ser descartadas pela sua implementação. Repare que o atributo ID também deve ser descartado.
>
> Como modelo, você deve utilizar o classificador baseado em centróides médios apresentado em sala e apresentar como resultados a acurácia geral e as acurácias por classe. Você é livre para treinar outros modelos e apresentar os respectivos resultados.

## O que foi feito

Seguindo as fases do CRISP-DM:

1. **Entendimento dos dados:** download pelo `ucimlrepo` (id 15).
2. **Preparação:** as linhas com atributo ausente e a coluna ID foram descartadas, sobrando 683 instâncias. Depois veio a divisão estratificada entre treino e teste (`random_state=42`).
3. **Modelagem:** um centroide (média dos atributos) por classe, 2 (benigno) e 4 (maligno), calculado no treino. Cada amostra de teste recebe a classe do centroide mais próximo.
4. **Avaliação:** acurácia geral e acurácia por classe, tirada da matriz de confusão.

## Resultado

Acurácia geral de **96,35%** no conjunto de teste.

## Como rodar

Abra pelo botão do Colab ou rode localmente com o ambiente da raiz ([INSTRUCOES_EXECUCAO.md](../../../INSTRUCOES_EXECUCAO.md)). O notebook baixa o dataset do UCI, então precisa de internet.
