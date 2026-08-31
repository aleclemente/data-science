notas = []
# Entrada de dados
for i in range(3):
 nota = float(input(f"Digite a nota do aluno {i+1}: "))
 notas.append(nota)
# Cálculos
media = sum(notas) / len(notas)
maior = max(notas)
menor = min(notas)
aprovados = [n for n in notas if n >= 6.0]
print(f"Notas: {notas}")
print(f"Média: {media:.2f}")
print(f"Maior nota: {maior}")
print(f"Menor nota: {menor}")
print(f"Resultado Final: { "Aprovado" if media > 7.0 else "reprovado"}")