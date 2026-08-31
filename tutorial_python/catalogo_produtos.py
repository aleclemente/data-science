catalogo = {
 "notebook": {"preco": 3200.00, "estoque": 15},
 "mouse": {"preco": 89.90, "estoque": 40},
 "teclado": {"preco": 150.00, "estoque": 8},
}
def exibir_catalogo(cat):
 print(f"{"Produto":<12} {"Preço":>10} {"Estoque":>9}")
 print("-" * 34)
 for produto, info in cat.items():
  print(f"{produto:<12} R${info['preco']:>8.2f} {info['estoque']:>9}")
exibir_catalogo(catalogo)
# Total em estoque
total = sum(i["preco"] * i["estoque"] for i in catalogo.values())
print(f"\nValor total em estoque: R$ {total:,.2f}")