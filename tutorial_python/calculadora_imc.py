def calcular_imc(peso, altura):
    """Calcula o Índice de Massa Corporal."""
    return peso / altura ** 2

def classificar_imc(imc):
    """Retorna a classificação do IMC."""
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25.0:
        return "Peso normal"
    elif imc < 30.0:
        return "Sobrepeso"
    else:
        return "Obesidade"

def relatorio_imc(nome, peso, altura):
    """Gera relatório completo de IMC."""
    imc = calcular_imc(peso, altura)
    classe = classificar_imc(imc)
    print(f"Paciente : {nome}")
    print(f"IMC : {imc:.2f}")
    print(f"Situação : {classe}")
relatorio_imc("João Silva", 82, 1.75)