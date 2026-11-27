# Atividade 06 — Processos e fontes de dados

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/aleclemente/ciencias-de-dados/blob/main/pos-1029-analise-e-ciencia-de-dados/entregas/atividade-06-processos-e-fontes-de-dados/atividade-06-processos-e-fontes-de-dados.ipynb)

**Disciplina:** POS.1029 — Análise e Ciência de Dados · **Professor:** Plácido Neto · **Avaliada:** sim

## Enunciado

Montar um script que carrega dados de fontes distintas (arquivo JSON e API pública), grava num banco SQLite, consulta com SQL, exporta para outros formatos e passa pelo checklist de verificação ética e legal antes de fazer web scraping.

## O que foi feito

- **Coleta e preparação:** dados de estabelecimentos de saúde do RN pela API de dados abertos do Ministério da Saúde (CNES).
- **Armazenamento e consulta:** carga num banco SQLite e consulta SQL sobre ele.
- **Exportação:** o mesmo conjunto em CSV e Parquet, com a comparação de tamanho dos arquivos.
- **Ética e legalidade:** checklist de verificação para web scraping.

## Arquivos

- [atividade-06-processos-e-fontes-de-dados.ipynb](atividade-06-processos-e-fontes-de-dados.ipynb): a solução.
- O pacote de dados de exemplo da aula está no material do professor: [material/aula-06-processos-e-fontes-de-dados/](../../material/aula-06-processos-e-fontes-de-dados/).

## Como rodar

Abra pelo botão do Colab, ou rode localmente com o ambiente da raiz do repositório ([INSTRUCOES_EXECUCAO.md](../../../INSTRUCOES_EXECUCAO.md)), a partir desta pasta. O notebook consulta a API do CNES, então precisa de internet.
