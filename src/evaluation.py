import numpy as np
from sklearn.metrics import confusion_matrix, recall_score, precision_score, accuracy_score, roc_auc_score
from scipy.stats import ks_2samp

def calcular_metricas_limiar(y_true, y_prob, limiar):
    """Calcula métricas avançadas (Recall, AUC, Gini, KS, etc) para um limiar específico."""
    y_pred = (y_prob >= limiar).astype(int)
    
    tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()
    especificidade = tn / (tn + fp) if (tn + fp) > 0 else 0
    
    recall = recall_score(y_true, y_pred)
    precisao = precision_score(y_true, y_pred, zero_division=0)
    acuracia = accuracy_score(y_true, y_pred)
    
    auc = roc_auc_score(y_true, y_prob)
    gini = (2 * auc) - 1
    
    prob_pos = y_prob[y_true == 1]
    prob_neg = y_prob[y_true == 0]
    ks_stat, _ = ks_2samp(prob_pos, prob_neg)
    
    return [
        round(recall, 4), round(auc, 4), round(gini, 4), 
        round(ks_stat, 4), round(especificidade, 4), 
        round(precisao, 4), round(acuracia, 4)
    ]

def extrair_matriz_quadrantes(y_true, y_prob, limiar):
    """Extrai os quadrantes da matriz de confusão e o volume de vistorias."""
    y_pred = (y_prob >= limiar).astype(int)
    tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()
    
    return {
        'Verdadeiros Negativos (TN - Seguras)': tn,
        'Falsos Positivos (FP - Alarme Falso)': fp,
        'Falsos Negativos (FN - Queda Omitida)': fn,
        'Verdadeiros Positivos (TP - Queda Detectada)': tp,
        'Total de Vistorias Geradas (TP + FP)': tp + fp
    }