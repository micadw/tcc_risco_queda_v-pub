import numpy as np

def otimizar_threshold_financeiro(y_train, y_prob_train, custo_fp=1700, multiplicador_fn=17):
    """
    Simula o custo operacional para diversos limiares e retorna o ponto de menor impacto financeiro.
    """
    custo_fn = custo_fp * multiplicador_fn
    
    lista_thresholds = []
    lista_custos_fp = []
    lista_custos_fn = []
    lista_custos_totais = []

    for threshold in np.arange(0.01, 1.0, 0.01):
        pred_simulada = (y_prob_train >= threshold).astype(int)
        
        fp = np.sum((pred_simulada == 1) & (y_train == 0))
        fn = np.sum((pred_simulada == 0) & (y_train == 1))

        custo_fp_atual = fp * custo_fp
        custo_fn_atual = fn * custo_fn
        custo_atual = custo_fp_atual + custo_fn_atual

        lista_thresholds.append(threshold)
        lista_custos_fp.append(custo_fp_atual)
        lista_custos_fn.append(custo_fn_atual)
        lista_custos_totais.append(custo_atual)

    indice_menor_custo = np.argmin(lista_custos_totais)
    threshold_otimo = lista_thresholds[indice_menor_custo]
    menor_custo_total = lista_custos_totais[indice_menor_custo]

    # Dicionário de resultados para plotagem e relatórios
    resultados = {
        'threshold_otimo': threshold_otimo,
        'menor_custo_total': menor_custo_total,
        'historico': {
            'limiares': lista_thresholds,
            'custos_fp': lista_custos_fp,
            'custos_fn': lista_custos_fn,
            'custos_totais': lista_custos_totais
        }
    }
    
    return resultados