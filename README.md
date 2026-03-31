# 🌳 Risco de Queda de Árvores em São Paulo: Modelagem Preditiva Geoespacial

Este repositório contém o código, os dados e a metodologia aplicados no trabalho de conclusão de curso focado na transição de abordagens reativas para modelos preditivos de zeladoria urbana. O modelo utiliza dados oficiais do portal GeoSampa (2014-2017) e algoritmos de Machine Learning (Regressão Lasso e XGBoost) para priorizar vistorias preventivas na malha viária do município[cite: 12, 62].

A unidade espacial de análise é o segmento viário, convertendo falhas pontuais em métricas de densidade probabilística e isolando o risco físico real.

## 🚀 Destaques do Projeto

* **Desempenho Preditivo (XGBoost):** O modelo final alcançou **82,06% de Recall**, superando a inspeção aleatória.
* **Eficiência Operacional (Lift):** A ferramenta demonstrou ser **12,8 vezes** mais assertiva na detecção de sinistros do que o método base.
* **Impacto Econômico:** A projeção do Limiar Preditivo Ótimo evidenciou um potencial de economia de recursos públicos superior a **R$ 110 milhões** para a municipalidade.
* **Física da Paisagem:** A modelagem validou a hipótese biomecânica de que a proximidade arbórea (Índice de Densidade Arbórea Gravitacional - IDAG) atua como forte ancoragem protetiva mútua. Em contrapartida, a exposição aerodinâmica plena e o isolamento espacial (AIV) exacerbam o risco.

## 📂 Estrutura do Repositório

A organização do projeto segue a seguinte arquitetura de diretórios:

tcc-risco-queda-sp/
│
├── data/                    
│   ├── raw/                 <- Dados brutos (Cadastro de árvores, Quedas SIGRC, Viário CET)
│   └── processed/           <- Dados limpos, unificados e agregados por segmento viário
│
├── docs/                    <- Documentação auxiliar
│   ├── dicionario_dados.csv <- Descrição tabular das variáveis e features geradas
│   └── dicionario_dados.gsheet
│
├── notebooks/               <- Pipeline sequencial de análise espacial e modelagem
│   ├── 01_data_transformation.ipynb <- Limpeza, feature engineering espacial e junções
│   ├── 02_modelagem.ipynb           <- Treinamento, GridSearch (Lasso, XGBoost) e métricas
│   ├── 03_mapa.ipynb                <- Rotinas de espacialização e exportação cartográfica
│
├── results/                 <- Saídas e artefatos do modelo
│   ├── figures/             <- Matrizes de confusão, Curvas ROC, Feature Importance
│   ├── maps/                <- Mapas temáticos de risco (GeoJSON/SHP)
│   ├── models/              <- Modelos treinados exportados (.joblib)
│   └── tables/              <- Tabelas de simulação financeira e métricas
│
├── src/                     <- Módulos Python com funções reaproveitáveis
│   ├── ETL_functions.py     <- Funções de extração e tratamento de dados base
│   ├── evaluation.py        <- Cálculo de métricas e custos operacionais
│   ├── optimization.py      <- Scripts de calibração de hiperparâmetros
│   ├── spatial_features.py  <- Motores de cálculo de distância (KDTree) e índices (IDAG/AIV)
│   ├── spatial_utils.py     <- Tratamento de geometrias e projeções
│   └── visualization.py     <- Funções padronizadas para plotagem de gráficos
│
├── LICENSE.txt              <- Licença MIT
├── README.md                <- Visão geral do projeto
└── requirements.txt         <- Dependências do ambiente Python (Pandas, GeoPandas, XGBoost, etc.)

## 🛠️ Como Reproduzir a Pesquisa

1. **Clone o repositório e acesse a pasta:**
   git clone https://github.com/micadw/tcc_risco_queda_v-pub.git
   cd tcc_risco_queda_v-pub

2. **Instale as dependências requeridas:**
   pip install -r requirements.txt

3. **Obtenção dos Dados:**
   Devido ao volume, os datasets finais processados podem ser baixados [neste link](https://drive.google.com/drive/folders/14ax6U4PoH0DDGJAZwFgVCKlc9xkfWUSm?usp=sharing) e extraídos no diretório `data/processed/`.

4. **Execução do Pipeline:**
   A esteira de dados foi desenhada para ser executada sequencialmente na pasta `notebooks/`:
   * Inicie pelo `01_data_transformation.ipynb` para recriar as métricas macrogeométricas.
   * Prossiga para o `02_modelagem.ipynb` para treinar os algoritmos e otimizar o Threshold.
   * Finalize no `03_mapa.ipynb` para gerar a estratificação do risco territorial urbano.

---
👤 **Autor:** Amilcar Ferraz Farina 
🎓 **Instituição:** Especialização em Data Science & Analytics – USP/ESALQ
