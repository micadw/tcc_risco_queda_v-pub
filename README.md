# 🌳 Modelagem Preditiva de Queda de Árvores em São Paulo

Este repositório contém o código e a metodologia do TCC focado na transição de abordagens reativas para modelos preditivos de zeladoria urbana, utilizando dados oficiais do portal GeoSampa.

Faça o download do dataset neste link [link do Google Drive/Kaggle] e salve o arquivo '99_MASTER_DATASET_READY.parquet' dentro da pasta 'data/processed/

## 🚀 Destaques do Projeto

* **Eficiência Operacional:** O modelo apresentou um **Lift de 10x**, demonstrando ser dez vezes mais assertivo na identificação de riscos do que as inspeções aleatórias tradicionais.
* **Performance (XGBoost):** O algoritmo campeão alcançou **73,8% de Recall**, priorizando a segurança pública e minimizando os falsos negativos (árvores em risco que passariam despercebidas).
* **Variáveis Chave:** A modelagem espacial foi construída com base em regras físicas avançadas, incluindo *Densidade Gravitacional*, *Isolamento Espacial* (Distância 3NN) e *Confinamento Radicular*.

## 📂 Estrutura do Repositório

A organização do projeto segue as melhores práticas de Data Science e MLOps:

    tcc-risco-queda-sp/
    │
    ├── data/                    <- (Os dados brutos devem ser baixados via GeoSampa)
    │   ├── raw/                 <- Dados brutos (Cadastro de árvores, Histórico quedas)
    │   └── processed/           <- Dados limpos e unificados
    │
    ├── docs/                    <- Documentação do projeto
    │   └── dicionario_de_dados.md <- Descrição detalhada das variáveis matemáticas
    │
    ├── notebooks/               <- Pipeline sequencial de análise e modelagem
    │   ├── 00_engenharia_geoespacial.ipynb <- Cálculo da física espacial (Scipy)
    │   ├── 01_auditoria_target.ipynb       <- Spatial Join do histórico de quedas
    │   ├── 02_preparacao_e_eda.ipynb       <- Análise exploratória e Feature Engineering
    │   ├── 03_modelagem_e_gridsearch.ipynb <- Modelagem (Lasso vs XGBoost)
    │   └── 04_aplicacao_pratica.ipynb      <- Simulação de deploy para a Defesa Civil
    │
    ├── results/                 <- Saídas e exportações
    │   ├── figures/             <- Matrizes de Confusão, Curvas ROC e Importância
    │   └── models/              <- Modelos otimizados e salvos em .joblib
    │
    ├── src/                     <- Funções modulares de engenharia de atributos
    │   ├── spatial_features.py  <- Motor do algoritmo KDTree
    │   ├── data_processing.py   <- Funções de normalização e pipelines
    │   └── model_evaluation.py  <- Scripts de métricas (Recall, AUC, KS)
    │
    └── README.md                <- Visão geral do projeto e instruções

## 🛠️ Como Rodar o Projeto

1. **Clone o repositório:**
   git clone https://github.com/SEU_USUARIO/tcc-risco-queda-sp.git
   cd tcc-risco-queda-sp

2. **Instale as dependências:**
   pip install -r requirements.txt

3. **Execute o Pipeline:**
   Recomenda-se a execução sequencial dos notebooks na pasta `notebooks/`, começando pelo `00_engenharia_geoespacial.ipynb` até à modelagem no `03_modelagem_e_gridsearch.ipynb`.

---
👤 **Autor:** Amilcar Ferraz Farina (Mica)  
🎓 **Instituição:** MBA em Gestão de Projetos - ESALQ/USP