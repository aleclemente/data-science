import numpy as np

# Linhas: produtos (Notebook, Mouse, Teclado)
# Colunas: meses (Jan a Jun)
vendas = np.array([
    [120, 135, 148, 162, 175, 190],
    [340, 298, 312, 400, 390, 420],
    [ 88, 95, 102, 115, 97, 108],
])

produtos = ["Notebook", "Mouse", "Teclado"]

meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"]

# Total por produto (soma em linha)
total_produto = vendas.sum(axis=1)
for prod, total in zip(produtos, total_produto):
 print(f"{prod:<10}: {total} unidades")
 
# Média mensal geral
media_mes = vendas.mean(axis=0)
for mes, med in zip(meses, media_mes):
    print(f"{mes}: {med:.1f} unidades/produto")
 
# Melhor mês (maior total geral)
total_mes = vendas.sum(axis=0)
melhor_mes = meses[np.argmax(total_mes)]
print(f"\nMelhor mês: {melhor_mes} ({total_mes.max()} unidades)")

# Percentual de crescimento Jan → Jun
crescimento = (vendas[:, -1] - vendas[:, 0]) / vendas[:, 0] * 100
for prod, cresc in zip(produtos, crescimento):
    print(f"{prod:<10}: {cresc:+.1f}%")