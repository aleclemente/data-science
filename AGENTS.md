# AGENTS.md — data-science

Instruções para agentes de IA (Claude Code e outros) que trabalham neste repositório.

## O que é este repositório

As entregas do Alexandre Clemente na **Especialização em Ciência de Dados do IFRN** (ago/2026 até ~jun/2027): notebooks, scripts e dados de cada aula ou atividade. O repositório é **público**.

## Onde fica cada coisa

- **Uma pasta por disciplina**, com o código do IFRN no nome (`pos-1029-…`, `pos-1035-…`, `pos-1036-…`).
- **Dentro dela, uma pasta por aula ou atividade** (`aula-07-coleta-via-api/`, `atividade-01-desvio-padrao/`). Cada uma traz o enunciado, o que foi feito e como rodar.
- **O [README](README.md)** tem a tabela de todas as entregas. Ela é atualizada junto com cada entrega nova.
- **Ambiente:** `.venv` na raiz, criado a partir do `requirements.txt` ([INSTRUCOES_EXECUCAO.md](INSTRUCOES_EXECUCAO.md)).
- **Prazos e notas não ficam aqui.** O acompanhamento é feito fora deste repositório.

## Ligação com o PTT (TCC)

A análise exploratória e os experimentos de dados do PTT (o TCC, que também é a solução 001 da Licorsy) podem rodar aqui, numa pasta própria, até o repositório do PTT nascer na organização `licorsy`. Nesse momento, o que for do PTT vai para lá.

## Regras

1. **Nada pessoal nem secreto.** Sem chave de API, token ou senha, e sem dado pessoal (LGPD). Os dados aqui são públicos (IBGE, TSE, CNES) ou fictícios, criados para a aula. Se um notebook precisar de chave, use variável de ambiente e nunca deixe a chave na saída da célula.
2. **Material do professor:** mantenha o crédito e o `LEIA-ME` original da aula.
3. **Toda mudança sai num ramo novo**, com PR para o `develop`. Mensagens no padrão Conventional Commits (`feat(pos-1029): …`, `docs: …`).
4. **Não commite** `.venv/`, `__pycache__/` nem arquivos gerados grandes. Um dado de referência pequeno, que o notebook gera, pode ir junto da aula.
5. **Atividade avaliativa:** a entrega precisa ser algo que o Alexandre consiga explicar. Ajude a entender e a fazer, sem trocar a solução dele por uma pronta.
