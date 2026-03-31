import numpy as np

def classificar_risco_operacional(probabilidades, threshold_otimo):
    """
    Classifica as probabilidades contínuas do XGBoost em 4 faixas de risco.
    O 'threshold_otimo' (calculado via matriz de custos) dita a entrada no Risco Alto.
    """
    # Define as réguas de corte
    limite_baixo = threshold_otimo * 0.5
    limite_critico = threshold_otimo + ((1.0 - threshold_otimo) * 0.5)

    condicoes = [
        probabilidades < limite_baixo,
        (probabilidades >= limite_baixo) & (probabilidades < threshold_otimo),
        (probabilidades >= threshold_otimo) & (probabilidades < limite_critico),
        probabilidades >= limite_critico
    ]
    
    classes = [
        '1 - Baixo Risco', 
        '2 - Risco Moderado', 
        '3 - Alto Risco (Prioridade de Vistoria)', 
        '4 - Risco Crítico (Emergência)'
    ]
    
    return np.select(condicoes, classes, default='Desconhecido')