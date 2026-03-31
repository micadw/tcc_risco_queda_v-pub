import numpy as np
import pandas as pd
import geopandas as gpd
from scipy.spatial import cKDTree
from scipy import sparse

# ==========================================
# 1. DEFINIÇÃO DAS FUNÇÕES
# ==========================================

def preparar_indice_espacial(gdf):
    if gdf.crs.is_geographic:
        gdf = gdf.to_crs(epsg=31983)
    coords = np.c_[gdf.geometry.x, gdf.geometry.y]
    tree = cKDTree(coords)
    return coords, tree

def calcular_idag(coords, tree, raio_corte=15.0, beta=2.0):
    matriz_esparsa = tree.sparse_distance_matrix(tree, max_distance=raio_corte, output_type='coo_matrix')
    mask = matriz_esparsa.data > 0
    linhas, colunas, distancias = matriz_esparsa.row[mask], matriz_esparsa.col[mask], matriz_esparsa.data[mask]
    pesos = 1.0 / (distancias**beta + 1e-9)
    matriz_pesos = sparse.coo_matrix((pesos, (linhas, colunas)), shape=matriz_esparsa.shape)
    return np.array(matriz_pesos.sum(axis=1)).flatten()

def identificar_aiv(coords, tree, limite_isolamento=15.0):
    dists_1nn, _ = tree.query(coords, k=2, workers=-1)
    return (dists_1nn[:, 1] > limite_isolamento).astype(int)

def calcular_dva(coords, tree, vizinhos=3):
    dists_knn, _ = tree.query(coords, k=vizinhos + 1, workers=-1)
    return np.mean(dists_knn[:, 1:], axis=1)

def calcular_icc(df, col_arvores, col_largura, col_comprimento_km):
    # Converte o comprimento (em km) para metros (* 1000) e adiciona 1cm de tolerância na largura
    area_disponivel = (df[col_largura] + 0.01) * (df[col_comprimento_km] * 1000)
    confinamento = df[col_arvores] / area_disponivel
    return confinamento.replace([np.inf, -np.inf], 0).fillna(0)

def get_azimute(geom):
    try:
        if not geom or geom.is_empty:
            return 0.0
            
        rect = geom.minimum_rotated_rectangle
        if rect.geom_type != 'Polygon':
            return 0.0
            
        c = rect.exterior.coords
        
        # Obtém os vetores (dx, dy) dos dois lados adjacentes do retângulo
        dx1, dy1 = c[1][0] - c[0][0], c[1][1] - c[0][1]
        dx2, dy2 = c[2][0] - c[1][0], c[2][1] - c[1][1]
        
        # Seleciona o vetor correspondente à aresta mais longa (eixo da via)
        dx, dy = (dx1, dy1) if (dx1**2 + dy1**2) >= (dx2**2 + dy2**2) else (dx2, dy2)
            
        return float(np.degrees(np.arctan2(dy, dx)) % 180)
        
    except Exception as e:
        print(f"Erro no cálculo do azimute: {e}")
        return 0.0