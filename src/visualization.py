import matplotlib.pyplot as plt
import seaborn as sns
import os

def plotar_tradeoff_financeiro(historico_custos, threshold_otimo, menor_custo, caminho_exportacao=None):
    """Plota a curva 'U' de otimização de custos operacionais."""
    fig, ax = plt.subplots(figsize=(10, 6))

    ax.plot(historico_custos['limiares'], historico_custos['custos_fp'], label='Custo de Vistorias (FP)', color='#3498db', linestyle='--')
    ax.plot(historico_custos['limiares'], historico_custos['custos_fn'], label='Custo de Quedas (FN)', color='#e74c3c', linestyle='--')
    ax.plot(historico_custos['limiares'], historico_custos['custos_totais'], label='CUSTO TOTAL', color='#2c3e50', linewidth=2.5)

    ax.axvline(x=threshold_otimo, color='#27ae60', linestyle=':', linewidth=2, label=f'Ponto Ótimo ({threshold_otimo:.2f})')
    ax.plot(threshold_otimo, menor_custo, marker='o', markersize=8, color='#27ae60')

    ax.set_title('Otimização Operacional: Trade-off de Custos (Vistoria vs. Queda)', fontsize=13, weight='bold')
    ax.set_xlabel('Limiar de Probabilidade Preditiva (Threshold)', fontsize=11)
    ax.set_ylabel('Impacto Financeiro Simulado no Treino (R$)', fontsize=11)
    ax.set_xlim(0, 1)
    ax.grid(alpha=0.3)
    ax.legend(loc='upper center', fontsize=10)

    plt.tight_layout()
    if caminho_exportacao:
        plt.savefig(caminho_exportacao, dpi=300, bbox_inches='tight')
    plt.show()