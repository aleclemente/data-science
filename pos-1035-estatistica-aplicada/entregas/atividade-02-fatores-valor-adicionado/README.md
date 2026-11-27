# Atividade 02 — Fatores relevantes para o Valor Adicionado dos municípios do RN

**Disciplina:** POS.1035 — Estatística Aplicada à Ciência de Dados · **Professor:** João Maria Filgueira · **Avaliada:** sim (em grupo)

## Enunciado

> Utilizando os Portais Observatório Sebrae, IpeaData e IBGE-Cidades, elaborem um texto mostrando fatores relevantes para que um município tenha alto Valor Adicionado no setor de Indústria, no de Serviços e no de Administração:
>
> 1. Selecionem pelo menos um município com alto Valor Adicionado na Indústria.
> 2. Identifiquem fatores relevantes para essa realidade.
> 3. Elaborem um texto, com gráficos, explicando essa realidade.
> 4. Repitam os itens 1, 2 e 3 para Serviços e, finalmente, para a Administração.
> 5. Apresentem contribuições, dialogando o texto produzido com um artigo sobre desenvolvimento socioeconômico.

## O que foi feito

Um artigo curto, *O que explica o alto Valor Adicionado Bruto nos municípios do Rio Grande do Norte: Indústria, Serviços e Administração Pública*:

- **Dados:** VAB municipal por setor do IBGE/SIDRA (tabela 5938), ano de 2021, o mais recente com o VAB aberto por setor (para 2022 e 2023 o SIDRA só publica o PIB), mais o Censo 2022 e o CEMPRE 2021.
- **Municípios:** Guamaré (Indústria, cadeia de petróleo e gás), Natal (Serviços, escala e diversificação) e Ceará-Mirim (Administração Pública, que ali indica dependência, não desenvolvimento). Uma tabela compara os 3 com o RN.
- **Diálogo com a literatura:** Giovanini, Pereira e Almeida (2022), *Diversidade produtiva e crescimento econômico* (*Nova Economia*). A concentração em Natal, Mossoró e Parnamirim (46,9% do VAB do RN) é coerente com o efeito sobre os vizinhos descrito pelos autores, mas é tratada como hipótese: os dados não provam causa.

## Método

O texto partiu de um prompt único enviado a 3 IAs (Gemini, GPT e Perplexity). Os 3 rascunhos foram conciliados num texto só, e cada número foi conferido no SIDRA. Na conciliação saíram valores sem fonte, populações da prévia do Censo e uma autoria atribuída errado.

## Arquivos

- [atividade-02-fatores-valor-adicionado.docx](atividade-02-fatores-valor-adicionado.docx): o artigo entregue, com os 4 gráficos.
- [dados/dados-sidra-5938.csv](dados/dados-sidra-5938.csv): os dados do SIDRA usados nos gráficos (município, ano, variável, mil reais).
- [processo/](processo/): o prompt ([prompt-artigo-conciliado.txt](processo/prompt-artigo-conciliado.txt)) e os 3 rascunhos das IAs ([Gemini](processo/artigo-vab-rn-gemini.md), [GPT](processo/artigo-vab-rn-gpt.md), [Perplexity](processo/artigo-vab-rn-perplexity.md)).
