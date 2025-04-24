# 🎯 **MLflow Credit Scoring: Deploy via PyFuncModel**

## 📝 Descrição

Este projeto mostra uma abordagem alternativa para utilizar modelos de Machine Learning treinados com **MLflow**, realizando **previsões diretamente em Python** com a interface `PyFuncModel`, **sem necessidade de uma API local**.

Ideal para notebooks exploratórios, testes offline ou integração com pipelines Python puros, essa abordagem é simples, eficiente e mantém a consistência dos ambientes definidos durante o treino e logging do modelo.

> ✅ Esta versão **não utiliza `requests` ou `mlflow models serve`** — o modelo é carregado diretamente e utilizado via código.

O modelo servido encontra-se em 📁 [MLFlow-RF](https://github.com/thiagotims/ai-machine-learning/tree/main/MLFlow-RF)

O deploy do mesmo modelo utilizando API local encontra-se em 📁 [deploy-local]()

---

## ✨ Como utilizar o modelo

### Pré-requisitos

Certifique-se de ter:

- Python (≥ 3.12)
- MLflow (≥ 2.0)
- Um modelo salvo com `mlflow.sklearn`
- Dataset de entrada compatível (`Credit.csv`)

---

### Passos

1. **Clone o repositório e acesse a pasta:**

   ```bash
   git clone github.com/thiagotims/ai-machine-learning/tree/main/deploy-PyFuncModel
   cd deploy-PyFuncModel
   ```

2. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Carregue o modelo como PyFuncModel e execute previsões:**

   ```python
   import mlflow
   import pandas as pd

   # Caminho do modelo salvo
   model_uri = "runs:/<RUN_ID>/ModeloRF"

   # Carrega modelo
   loaded_model = mlflow.pyfunc.load_model(model_uri)

   # Pré-processa o dataset
   credito = pd.read_csv("Credit.csv")
   for col in credito.columns:
       if credito[col].dtype == 'object':
           credito[col] = credito[col].astype('category').cat.codes

   # Seleciona dados de entrada
   input_data = credito.iloc[0:5, 0:20]

   # Faz a previsão
   predicoes = loaded_model.predict(input_data)

   # Exibe os resultados
   resultado = pd.DataFrame(predicoes, columns=["Previsão"])
   resultado.index.name = "ID da Amostra"
   print(resultado)
   ```

---

## 🔄 Diferença para a versão com API Local

| Característica           | API Local (requests)                                | PyFuncModel (local direto)                      |
|--------------------------|-----------------------------------------------------|-------------------------------------------------|
| Forma de uso             | Envia JSON para um servidor local                   | Usa diretamente no Python                       |
| Dependência de API       | Requer rodar `mlflow models serve`                  | Não precisa servir o modelo                     |
| Comunicação              | Via HTTP (`requests.post`)                          | Funções nativas do MLflow                       |
| Uso ideal                | Integração com frontend / serviços web              | Notebooks, testes offline, pipelines Python     |

---

## 📦 Ficha Técnica

| 🔍 **Item**             | 📄 **Descrição**                                                 |
|-------------------------|------------------------------------------------------------------|
| **🛠️ Tecnologias**      | Python, Pandas, MLflow, Scikit-learn                             |
| **📦 Dependências**     | pandas, scikit-learn, mlflow                                     |
| **⚙️ Funcionalidade**   | Previsão direta com modelo Random Forest via PyFuncModel         |
| **📌 Modelo Utilizado** | Random Forest Classifier                                         |
| **🧪 Dataset**          | Credit.csv (features categóricas e numéricas)                    |
| **🚀 Carregamento**     | Via `mlflow.pyfunc.load_model`                                   |
| **🧑‍🧳 Formato de entrada**| DataFrame Pandas com colunas preprocessadas                     |


