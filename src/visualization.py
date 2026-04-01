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

import pandas as pd
import matplotlib.pyplot as plt
import os
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.tools.tools import add_constant

def calcular_vif_completo(df, colunas_numericas):
    """
    Calcula o VIF para todas as variáveis numéricas fornecidas.
    """
    # 1. Filtra as colunas e preenche valores nulos (o VIF falha se houver NAs)
    X_num = df[colunas_numericas].copy()
    X_num = X_num.fillna(X_num.median())
    
    # 2. Adiciona a constante (obrigatório para a matemática correta do VIF)
    X_num_const = add_constant(X_num)
    
    # 3. Calcula o VIF iterativamente
    vif_data = pd.DataFrame()
    vif_data["Variável"] = X_num_const.columns
    vif_data["VIF"] = [variance_inflation_factor(X_num_const.values, i) for i in range(X_num_const.shape[1])]
    
    return vif_data

def plotar_e_salvar_vif_completo(vif_data, caminho_pasta='results/figures', sufixo=''):
    """
    Gera o gráfico do VIF com altura dinâmica.
    Requer um DataFrame 'vif_data' já calculado contendo as colunas 'Variável' e 'VIF'.
    """
    os.makedirs(caminho_pasta, exist_ok=True)
    
    # Garante que a constante foi removida e ordena
    df_plot = vif_data[vif_data['Variável'] != 'const'].sort_values('VIF', ascending=True)

    # Altura dinâmica: 0.4 polegadas por cada variável no dataset (mínimo de 6)
    altura_dinamica = max(6, len(df_plot) * 0.4)
    
    fig, ax = plt.subplots(figsize=(10, altura_dinamica))
    ax.barh(df_plot['Variável'], df_plot['VIF'], color='#95a5a6')
    ax.set_xlabel('Fator de Inflação da Variância (VIF)')
    ax.set_title('Análise de Multicolinearidade (Todas as Variáveis Numéricas)')

    # Linha de corte rigorosa
    ax.axvline(x=5.0, color='red', linestyle='--', linewidth=1.2, label='Limite Sugerido (VIF=5)')
    ax.legend()

    plt.tight_layout()

    # Salvar a imagem
    nome_arquivo = f'{caminho_pasta}/02_figura_vif_completo{sufixo}.jpg'
    plt.savefig(nome_arquivo, dpi=300, bbox_inches='tight')
    plt.show()