import numpy as np
import pandas as pd
import geopandas as gpd
from scipy.spatial import cKDTree
from scipy import sparse

# ==========================================
# 1. DEFINIÇÃO DAS FUNÇÕES
# ==========================================

def imputar_por_proximidade(gdf, colunas_para_imputar):
    """
    Preenche valores nulos em colunas específicas usando o valor do 
    vizinho geográfico mais próximo que possua o dado.
    """
    # 1. Garantir que estamos trabalhando com coordenadas projetadas (metros)
    if gdf.crs.is_geographic:
        gdf = gdf.to_crs(epsg=31983)

    # Criamos uma cópia para não alterar o original de forma irreversível
    gdf_imputado = gdf.copy()

    for col in colunas_para_imputar:
        # Separa quem tem dados (treino) de quem não tem (alvo da imputação)
        tem_dados = gdf_imputado[gdf_imputado[col].notnull()]
        nao_tem_dados = gdf_imputado[gdf_imputado[col].isnull()]

        if nao_tem_dados.empty:
            print(f"Coluna {col} já está completa.")
            continue

        print(f"Imputando {len(nao_tem_dados)} valores na coluna: {col}...")

        # 2. Construir a árvore espacial apenas com os pontos que possuem dados
        coords_treino = np.c_[tem_dados.geometry.centroid.x, tem_dados.geometry.centroid.y]
        tree = cKDTree(coords_treino)

        # 3. Coordenadas de quem precisa receber os dados
        coords_alvo = np.c_[nao_tem_dados.geometry.centroid.x, nao_tem_dados.geometry.centroid.y]

        # 4. Encontrar o índice do vizinho mais próximo (k=1)
        # dists: distância até o vizinho | indices: posição do vizinho no array coords_treino
        _, indices = tree.query(coords_alvo, k=1, workers=-1)

        # 5. Mapear os valores encontrados de volta para o DataFrame original
        # O .iloc[indices] pega os valores corretos baseados na posição da árvore
        valores_recuperados = tem_dados[col].iloc[indices].values
        
        # Atualiza apenas as linhas que eram nulas
        gdf_imputado.loc[gdf_imputado[col].isnull(), col] = valores_recuperados

    return gdf_imputado