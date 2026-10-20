# Aula 07 — Mini-projeto: coleta de dataset real via API

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/aleclemente/data-science/blob/main/pos-1029-analise-e-ciencia-de-dados/aula-07-coleta-via-api/app/Aula-07-coleta-de-dataset-real-via-API.ipynb)

**Disciplina:** POS.1029 Análise e Ciência de Dados · **Professor:** Plácido Neto · **Prazo:** 20/10/2026

## Atividade

Escolher uma API pública real e construir um notebook que colete um dataset a partir dela, entregue já executado e com os arquivos JSON/CSV gerados. Enunciado completo em [docs/](docs/01-real-dataset-API-request-exercise-description.md).

## O que foi feito

- **IBGE (API de Localidades):** municípios do RN.
- **TSE (portal de dados abertos):** busca de conjuntos de dados com paginação.
- **Proveniência:** cada arquivo salvo em JSON e CSV leva um bloco com fonte, endpoint e data da coleta.

## Conteúdo

| Caminho | O que é |
|---|---|
| `app/` | Minha solução e os dados que ela gerou (`app/dados/`) |
| `docs/` | Enunciado da atividade, transcrito do ambiente da disciplina |
| `examples/` | Notebooks de exemplo da aula |

## Como rodar

Abra no Colab pelo botão acima, ou localmente com o ambiente da raiz do repositório (ver [INSTRUCOES_EXECUCAO.md](../../INSTRUCOES_EXECUCAO.md)).
