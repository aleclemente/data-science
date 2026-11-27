# AGENTS.md — ciencias-de-dados

Instruções para agentes de IA (Claude Code e outros) que trabalham neste repositório.

## O que é este repositório

As entregas do Alexandre Clemente na **Especialização em Ciência de Dados do IFRN** (ago/2026 até ~jun/2027): notebooks, scripts e dados de cada aula ou atividade. O repositório é **público**.

## Onde fica cada coisa

- **Uma pasta por disciplina**, com o código do IFRN no nome (`pos-1029-…`, `pos-1035-…`, `pos-1036-…`). Dentro dela, sempre 2 pastas e um README:
  - **`material/`**: o que o professor distribuiu, sem edição. Na POS.1029, um pacote por aula (`material/aula-10-pipeline-limpeza/`); na POS.1036, a cópia do repositório do professor.
  - **`entregas/`**: o que o Alexandre fez, uma pasta por atividade.
  - **`README.md`** da disciplina: professor, a tabela de entregas (com a coluna "Avaliada") e a do material, com a origem.
- **Os [README.md](README.md) (português) e [README.en.md](README.en.md) (inglês) da raiz** têm as disciplinas e a tabela de todas as entregas. Os 2 são atualizados juntos, a cada entrega nova.
- **Ambiente:** `.venv` na raiz, criado a partir do `requirements.txt` ([INSTRUCOES_EXECUCAO.md](INSTRUCOES_EXECUCAO.md)).
- **Prazos e notas não ficam aqui.** O acompanhamento é feito fora deste repositório.

## Estrutura e convenções das entregas

1. **Toda entrega é `entregas/atividade-NN-tema/`**, em kebab-case. Na POS.1029, NN é o número da aula; na POS.1036, o número que o professor deu; na POS.1035, que não numera, a ordem de data das entregas publicadas.
2. **O arquivo principal tem o nome da pasta** (`atividade-10-pipeline-limpeza.ipynb`, `atividade-01-desvio-padrao.py`), sem sufixo de autor: a pasta e o README já dizem de quem é.
3. **README da entrega:** enunciado, o que foi feito, resultado, arquivos e como rodar. Se o código mudou depois da entrega (um caminho, por exemplo), o README diz o quê.
4. **Dados do professor não são copiados:** a entrega os lê por caminho relativo (`../../material/aula-NN-…/dados/…`) e roda a partir da própria pasta. O que a entrega gera (`saida/`, `dados/`) fica nela.
5. **Só depois do prazo:** uma entrega com prazo aberto fica fora do git (no `.git/info/exclude` local) e entra num PR depois do prazo, porque o repositório é público.
6. **Material do professor:** é movido com `git mv`, nunca editado; o enunciado transcrito pelo Alexandre também vai para `material/`.
7. **Língua:** tudo em português, menos o `README.en.md`.

## Ligação com o PTT (TCC)

A análise exploratória e os experimentos de dados do PTT (o TCC, que também é a solução 001 da Licorsy) podem rodar aqui, numa pasta própria, até o repositório do PTT nascer na organização `licorsy`. Nesse momento, o que for do PTT vai para lá.

## Regras

1. **Nada pessoal nem secreto.** Sem chave de API, token ou senha, e sem dado pessoal (LGPD). Os dados aqui são públicos (IBGE, TSE, CNES) ou fictícios, criados para a aula. Se um notebook precisar de chave, use variável de ambiente e nunca deixe a chave na saída da célula.
2. **Material do professor:** mantenha o crédito, a licença e o `LEIA-ME` original da aula.
3. **Toda mudança sai num ramo novo**, com PR para o `develop`. Mensagens no padrão Conventional Commits (`feat(pos-1029): …`, `docs: …`).
4. **Não commite** `.venv/`, `__pycache__/` nem arquivos gerados grandes. Um dado de referência pequeno, que o notebook gera, pode ir junto da aula.
5. **Atividade avaliativa:** a entrega precisa ser algo que o Alexandre consiga explicar. Ajude a entender e a fazer, sem trocar a solução dele por uma pronta.
