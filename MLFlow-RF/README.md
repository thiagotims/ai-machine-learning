# 🌲 Random Forest com MLflow: Registro e Comparação de Modelos em Classificação de Crédito

Este projeto implementa um pipeline completo de classificação binária com *Random Forest*, aplicado à base de dados German Credit. O foco está na rastreabilidade e na análise comparativa de múltiplas execuções de modelos usando **MLflow**.

## 📌 Objetivo

O objetivo é explorar o impacto de diferentes hiperparâmetros nos resultados do modelo e registrar automaticamente essas variações com **MLflow**, possibilitando a comparação e o rastreio dos melhores resultados. O modelo final é selecionado com base na **acurácia** e registrado automaticamente no **Model Registry**.

---

## ⚙️ Etapas do Projeto

- 🔍 **Carregamento e pré-processamento** dos dados categóricos e numéricos;
- 🌳 **Treinamento de modelos Random Forest** com diferentes hiperparâmetros (`n_estimators`, `max_depth`, `min_samples_split`);
- 📈 **Cálculo de métricas de performance** (acurácia, recall, precisão, F1, AUC, log loss);
- 📁 **Log de parâmetros, métricas e gráficos** com MLflow;
- 🏆 **Seleção automática do melhor modelo** com base na acurácia;
- 📦 **Registro do modelo final no MLflow Model Registry**;
- 🖼️ Geração de gráficos (matriz de confusão e curva ROC) para análise visual.

---

## 📋 Ficha Técnica

|🔍 **Item**|📄 **Descrição**|
|---|---|
|**🛠️ Tecnologias**|Python, scikit-learn, MLflow, pandas, matplotlib|
|**📦 Dependências**|mlflow, sklearn, pandas, matplotlib|
|**⚙️ Funcionalidade**|Treinamento, rastreamento e registro de modelos Random Forest com MLflow|
|**📊 Métricas Avaliadas**|Acurácia, Recall, Precision, F1-Score, AUC, Log Loss|
|**📌 Dataset**|German Credit Dataset (1000 observações, 21 variáveis)|
|**🧪 Nº de Execuções de Modelos**|135 combinações diferentes de hiperparâmetros|
|**🏆 Seleção do Melhor Modelo**|Automática com base na acurácia mais alta|
|**📦 Registro de Modelo**|Automatizado via `mlflow.register_model()`|
|**🖼️ Visualizações**|Matriz de confusão e curva ROC salvas e logadas no MLflow|

---

## 📁 Estrutura dos Arquivos

- `on-git_MLFlow_RF.md`: script principal com todo o pipeline de execução;
- `confusionrf.png` e `rocfr.png`: imagens salvas de gráficos durante os experimentos;
- Modelos e métricas são armazenados no **tracking server** do MLflow.

---

## 🚀 Como Executar

1. Clone o repositório:
  
```bash 
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio  
```

2. Instale os requisitos:

```bash 
pip install -r requirements.txt
```
3. Execute o script:

```bash 
python on-git_MLFlow_RF.md
``` 
4. Visualize os experimentos:

```bash 
mlflow ui
``` 
---

#### 📈 Exemplo de Saída

📊 Top 5 modelos por acurácia:
   n_estimators  max_depth  min_samples_split  acuracia
   ...           ...        ...                ...

✅ Melhor modelo com base em acurácia:
n_estimators: 100
max_depth: None
min_samples_split: 5
acuracia: 0.7733
run_id: a1a363ce68ba4ebc83b609269a657a8c

📦 Modelo registrado no MLflow com nome 'MelhorModeloRF'

---

## 🧠 Conclusão
Este projeto demonstra como integrar uma técnica de machine learning robusta com uma ferramenta moderna de experiment tracking. A abordagem facilita a auditoria, melhoria contínua e reprodutibilidade de experimentos.

Contribuições são bem-vindas! ⭐

