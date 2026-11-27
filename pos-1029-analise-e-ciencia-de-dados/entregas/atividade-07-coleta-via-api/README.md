# Atividade 07 — Mini-projeto: coleta de dataset real via API

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/aleclemente/data-science/blob/main/pos-1029-analise-e-ciencia-de-dados/entregas/atividade-07-coleta-via-api/atividade-07-coleta-via-api.ipynb)

**Disciplina:** POS.1029 — Análise e Ciência de Dados · **Professor:** Plácido Neto · **Avaliada:** sim

## Enunciado

Escolher uma API pública real e construir um notebook que colete um dataset a partir dela, entregue já executado e com os arquivos JSON/CSV gerados. O enunciado completo está no material do professor: [docs/](../../material/aula-07-coleta-via-api/docs/01-real-dataset-API-request-exercise-description.md).

## O que foi feito

- **IBGE (API de Localidades):** municípios do RN.
- **TSE (portal de dados abertos):** busca de conjuntos de dados com paginação.
- **Proveniência:** cada arquivo salvo em JSON e CSV leva um bloco com fonte, endpoint e data da coleta.

## Arquivos

- [atividade-07-coleta-via-api.ipynb](atividade-07-coleta-via-api.ipynb): a solução.
- [dados/](dados/): os arquivos JSON e CSV que o notebook gerou.

## Como rodar

Abra pelo botão do Colab, ou rode localmente com o ambiente da raiz do repositório ([INSTRUCOES_EXECUCAO.md](../../../INSTRUCOES_EXECUCAO.md)), a partir desta pasta. O notebook consulta as APIs do IBGE e do TSE, então precisa de internet.
