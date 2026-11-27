# Atividade 10 — Pipeline de limpeza completo

**Disciplina:** POS.1029 — Análise e Ciência de Dados · **Professor:** Plácido Neto · **Avaliada:** sim

## Enunciado

Construir um pipeline ETL documentado para 155 registros sintéticos de exames laboratoriais e entregar o notebook executado e comentado, o dataset limpo e o dicionário de dados. Os dados e os notebooks da aula estão em [material/aula-10-pipeline-limpeza/](../../material/aula-10-pipeline-limpeza/).

## O que foi feito

Extract e diagnóstico → duplicatas → tipos → padronização das categorias → inválidos e ausentes (código de erro 999, mediana) → engenharia de atributos (`faixa_etaria`, `mes_coleta` e o indicador clínico `alterado`) → codificação ordinal e one-hot → validação com `assert` → load e dicionário de dados. Resultado: 150 exames padronizados.

## Arquivos

- [atividade-10-pipeline-limpeza.ipynb](atividade-10-pipeline-limpeza.ipynb): a solução.
- [saida/](saida/): o dataset limpo e o dicionário de dados que o notebook gera.

## Como rodar

Rode com o ambiente da raiz ([INSTRUCOES_EXECUCAO.md](../../../INSTRUCOES_EXECUCAO.md)) a partir desta pasta. O notebook lê `../../material/aula-10-pipeline-limpeza/dados/` e grava em `saida/`, sem precisar de internet.

**Diferença em relação à versão entregue:** só o caminho da pasta de dados, que mudou com a reorganização do repositório.
