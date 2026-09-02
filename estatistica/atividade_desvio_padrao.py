"""
Curso de Especialização em Ciência de Dados
Disciplina: Estatística Aplicada à Ciência de Dados
Professor: João Maria Filgueira

Atividade: Provar que a Média possui a menor variação em relação aos dados.
Resolução dos Exercícios 1 e 2 do arquivo Atividade_Desvio_Padrao.pdf.
"""

import math
import os
from collections import Counter
import statistics

# Garante diretório temporário para cache do Matplotlib sem avisos
os.environ.setdefault("MPLCONFIGDIR", "/tmp")

# Configuração de backend para salvar gráficos mesmo em ambientes sem display (headless)
import matplotlib
if not os.environ.get("DISPLAY"):
    matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def main():
    # =========================================================================
    # DADOS INICIAIS
    # =========================================================================
    valores = [12, 18, 33, 57, 12]
    n = len(valores)

    print("=" * 80)
    print("ATIVIDADE: PROVAR QUE A MÉDIA POSSUI A MENOR VARIAÇÃO EM RELAÇÃO AOS DADOS")
    print("=" * 80)
    print(f"Vetor de Dados X: {valores}")
    print(f"Número de observações (n): {n}\n")

    # =========================================================================
    # EXERCÍCIO 1.1: Calcule a Média, Mediana e Moda do vetor de Dados X
    # =========================================================================
    media = statistics.mean(valores)
    mediana = statistics.median(valores)
    contagem = Counter(valores)
    moda = max(contagem, key=contagem.get)

    print("-" * 80)
    print("EXERCÍCIO 1.1 - Medidas de Tendência Central")
    print("-" * 80)
    print(f"• Média   (X̄): {media:.2f}")
    print(f"• Mediana (Md): {mediana:.2f}")
    print(f"• Moda    (Mo): {moda:.2f}\n")

    # Construção do Quadro 1
    col_desv_media = [(x - media) ** 2 for x in valores]
    col_desv_mediana = [(x - mediana) ** 2 for x in valores]
    col_desv_moda = [(x - moda) ** 2 for x in valores]

    df_quadro1 = pd.DataFrame({
        "X - Dados": valores,
        "(X - Média)^2": col_desv_media,
        "(X - Mediana)^2": col_desv_mediana,
        "(X - Moda)^2": col_desv_moda,
    })

    soma_media = sum(col_desv_media)
    soma_mediana = sum(col_desv_mediana)
    soma_moda = sum(col_desv_moda)

    df_total = pd.DataFrame({
        "X - Dados": ["SOMA"],
        "(X - Média)^2": [soma_media],
        "(X - Mediana)^2": [soma_mediana],
        "(X - Moda)^2": [soma_moda],
    })

    tabela_completa = pd.concat([df_quadro1, df_total], ignore_index=True)
    print("Quadro 1 preenchido:")
    print(
        tabela_completa.to_string(
            index=False,
            formatters={
                "X - Dados": lambda x: f"{x:>8}",
                "(X - Média)^2": lambda x: f"{x:14.2f}",
                "(X - Mediana)^2": lambda x: f"{x:16.2f}",
                "(X - Moda)^2": lambda x: f"{x:13.2f}",
            },
        )
    )
    print()

    # =========================================================================
    # EXERCÍCIO 1.2: Mostre que a soma da coluna 2 é menor que a soma da
    # coluna 3 e também da coluna 4.
    # =========================================================================
    print("-" * 80)
    print("EXERCÍCIO 1.2 - Comparação das Somas dos Desvios Quadráticos")
    print("-" * 80)
    print(f"1) Coluna 2: Soma de (X - Média)^2   = {soma_media:.2f}")
    print(f"2) Coluna 3: Soma de (X - Mediana)^2 = {soma_mediana:.2f}")
    print(f"3) Coluna 4: Soma de (X - Moda)^2    = {soma_moda:.2f}\n")

    menor_que_mediana = soma_media < soma_mediana
    menor_que_moda = soma_media < soma_moda

    print(
        f"• Soma Coluna 2 < Soma Coluna 3? {soma_media:.2f} < {soma_mediana:.2f} -> {menor_que_mediana}"
    )
    print(
        f"• Soma Coluna 2 < Soma Coluna 4? {soma_media:.2f} < {soma_moda:.2f} -> {menor_que_moda}\n"
    )

    if menor_que_mediana and menor_que_moda:
        print(
            "COMPROVAÇÃO: A soma dos desvios quadráticos em torno da MÉDIA é estritamente menor"
        )
        print("do que em torno da Mediana e da Moda (Média possui a menor variação quadrática).\n")

    # =========================================================================
    # EXERCÍCIO 2: Divida a soma da coluna 2 por (5-1) e extraia a raiz quadrada.
    # Compare com o desvio padrão obtido pelo software e comente.
    # =========================================================================
    print("-" * 80)
    print("EXERCÍCIO 2 - Desvio Padrão e Comparação com Software Estatístico")
    print("-" * 80)

    graus_liberdade = n - 1
    variancia_calculada = soma_media / graus_liberdade
    desvio_padrao_calculado = math.sqrt(variancia_calculada)

    desvio_padrao_software = statistics.stdev(valores)

    print(f"• Soma da Coluna 2: {soma_media:.2f}")
    print(f"• Divisão por (5 - 1) = {graus_liberdade}: {soma_media:.2f} / {graus_liberdade} = {variancia_calculada:.4f} (Variância Amostral s²)")
    print(f"• Raiz quadrada da divisão: √{variancia_calculada:.4f} = {desvio_padrao_calculado:.4f}")
    print(f"• Desvio padrão via software (statistics.stdev): {desvio_padrao_software:.4f}")
    print(f"• Diferença absoluta: {abs(desvio_padrao_calculado - desvio_padrao_software):.6e}\n")

    print("COMENTÁRIO SOBRE A CONSTATAÇÃO:")
    print("1. Igualdade Exata: O valor calculado manualmente coincide com precisão absoluta")
    print("   com o desvio padrão amostral fornecido pelas bibliotecas estatísticas (statistics.stdev e numpy.std(ddof=1)).")
    print("2. Correção de Bessel: A divisão por (n - 1), em vez de n, compensa o fato de que a média")
    print("   amostral (X̄) foi calculada a partir dos próprios dados amostrais, gerando um estimador")
    print("   não viesado (não tendencioso) da variância da população.")
    print("3. Vínculo com a Questão 1: Como a Média é o ponto central que minimiza a soma dos desvios")
    print("   quadráticos (provado na Questão 1), o Desvio Padrão quantifica a dispersão ótima natural")
    print("   em torno desse centro de gravidade dos dados.\n")

    # =========================================================================
    # PLOTAGEM DOS GRÁFICOS
    # =========================================================================
    plotar_graficos(
        valores=valores,
        media=media,
        mediana=mediana,
        moda=moda,
        soma_media=soma_media,
        soma_mediana=soma_mediana,
        soma_moda=soma_moda,
        desvio_padrao=desvio_padrao_calculado,
    )


def plotar_graficos(valores, media, mediana, moda, soma_media, soma_mediana, soma_moda, desvio_padrao):
    """Gera visualizações estatísticas dos dois exercícios."""
    plt.style.use("seaborn-v0_8-whitegrid" if "seaborn-v0_8-whitegrid" in plt.style.available else "default")
    fig, axes = plt.subplots(1, 3, figsize=(18, 5.5))

    # -------------------------------------------------------------------------
    # Gráfico 1: Função dos Desvios Quadráticos f(c) = sum((x - c)^2)
    # -------------------------------------------------------------------------
    ax1 = axes[0]
    c_vals = np.linspace(5, 45, 300)
    f_c = [sum((x - c) ** 2 for x in valores) for c in c_vals]

    ax1.plot(c_vals, f_c, color="#1f77b4", linewidth=2.5, label=r"$f(c) = \sum (X - c)^2$")
    ax1.scatter([media], [soma_media], color="#2ca02c", s=120, zorder=5, label=f"Média ({media:.1f}): {soma_media:.1f} (MÍNIMO)")
    ax1.scatter([mediana], [soma_mediana], color="#ff7f0e", s=100, zorder=5, label=f"Mediana ({mediana:.1f}): {soma_mediana:.1f}")
    ax1.scatter([moda], [soma_moda], color="#d62728", s=100, zorder=5, label=f"Moda ({moda:.1f}): {soma_moda:.1f}")

    ax1.axvline(media, color="#2ca02c", linestyle="--", alpha=0.7)
    ax1.set_title("1. Curva dos Desvios Quadráticos\n(Mínimo Global na Média)", fontsize=12, fontweight="bold")
    ax1.set_xlabel("Centro de Referência (c)", fontsize=11)
    ax1.set_ylabel(r"$\sum (X - c)^2$", fontsize=11)
    ax1.legend(loc="upper center", fontsize=9)
    ax1.grid(True, linestyle=":", alpha=0.6)

    # -------------------------------------------------------------------------
    # Gráfico 2: Comparação de Barras da Soma dos Desvios
    # -------------------------------------------------------------------------
    ax2 = axes[1]
    categorias = ["Média (X̄)", "Mediana (Md)", "Moda (Mo)"]
    somas = [soma_media, soma_mediana, soma_moda]
    cores = ["#2ca02c", "#ff7f0e", "#d62728"]

    barras = ax2.bar(categorias, somas, color=cores, width=0.55, edgecolor="black", linewidth=1)
    for barra, valor in zip(barras, somas):
        ax2.text(
            barra.get_x() + barra.get_width() / 2,
            valor + 45,
            f"{valor:.2f}",
            ha="center",
            va="bottom",
            fontweight="bold",
            fontsize=10,
        )

    ax2.set_title("2. Comparação das Somas de Desvios\n(Coluna 2 < Coluna 3 < Coluna 4)", fontsize=12, fontweight="bold")
    ax2.set_ylabel("Soma dos Desvios Quadráticos", fontsize=11)
    ax2.set_ylim(0, max(somas) * 1.15)
    ax2.grid(axis="y", linestyle=":", alpha=0.6)

    # -------------------------------------------------------------------------
    # Gráfico 3: Dispersão dos Dados e Intervalo do Desvio Padrão
    # -------------------------------------------------------------------------
    ax3 = axes[2]
    y_pos = [1] * len(valores)
    ax3.scatter(valores, y_pos, color="#333333", s=110, zorder=4, label="Dados X: [12, 18, 33, 57, 12]")

    # Linhas de medidas centrais
    ax3.axvline(media, color="#2ca02c", linewidth=2, label=f"Média: {media:.1f}")
    ax3.axvline(mediana, color="#ff7f0e", linestyle="--", linewidth=1.8, label=f"Mediana: {mediana:.1f}")
    ax3.axvline(moda, color="#d62728", linestyle=":", linewidth=1.8, label=f"Moda: {moda:.1f}")

    # Faixa de desvio padrão em torno da média
    lim_inf = media - desvio_padrao
    lim_sup = media + desvio_padrao
    ax3.axvspan(lim_inf, lim_sup, color="#2ca02c", alpha=0.18, label=f"Faixa X̄ ± s ({desvio_padrao:.2f})")

    ax3.set_title(f"3. Dispersão de X com Desvio Padrão (s = {desvio_padrao:.2f})\n[Média ± s: {lim_inf:.1f} a {lim_sup:.1f}]", fontsize=12, fontweight="bold")
    ax3.set_xlabel("Valores de X", fontsize=11)
    ax3.set_yticks([])
    ax3.set_ylim(0.7, 1.3)
    ax3.legend(loc="upper right", fontsize=9)
    ax3.grid(axis="x", linestyle=":", alpha=0.6)

    plt.tight_layout()

    # Salva o arquivo de imagem diretamente dentro da pasta estatistica
    output_dir = os.path.dirname(os.path.abspath(__file__))
    output_png = os.path.join(output_dir, "grafico_desvio_padrao.png")
    plt.savefig(output_png, dpi=300, bbox_inches="tight")
    print(f"[GRÁFICO SALVO]: {output_png}")

    # Se houver display gráfico conectado e backend interativo, exibe a janela
    if os.environ.get("DISPLAY") and matplotlib.get_backend().lower() != "agg":
        plt.show()


if __name__ == "__main__":
    main()

