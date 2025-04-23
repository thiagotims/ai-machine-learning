# 🧠 Monitoramento de Treinamento com MLflow em Redes Neurais Keras

Este projeto demonstra como integrar o MLflow para rastrear e monitorar o treinamento de uma rede neural construída com Keras (via TensorFlow) usando o conjunto de dados MNIST. A aplicação mostra o uso de *autologging* para registrar automaticamente parâmetros, métricas, modelo e visualizações, com foco na facilidade de reprodutibilidade e transparência em experimentos de Machine Learning.

Ideal para quem deseja implementar boas práticas de MLOps mesmo em projetos de aprendizado supervisionado simples.

---

## 📊 Ficha Técnica

| 🔍 **Item**              | 📄 **Descrição**                                                        |
|--------------------------|-------------------------------------------------------------------------|
| **🛠️ Tecnologias**        | Python, TensorFlow (Keras), MLflow, NumPy, Matplotlib                   |
| **📦 Dependências**       | tensorflow, mlflow, scikit-learn, matplotlib                            |
| **📊 Dataset Utilizado**  | MNIST (imagens de dígitos manuscritos 28x28)                            |
| **📌 Modelo**             | Rede Neural Feedforward com camadas Dense e Dropout                     |
| **⚙️ Funcionalidade**     | Registro automático de parâmetros, métricas, gráficos e modelo com MLflow |
| **🔄 Número de Runs**     | Definido via `mlflow.start_run()`, controlado por execução de célula     |
| **⚠️ Observação**         | MLflow ainda não é compatível com TensorFlow 2.19 — use TF 2.18.0        |

---

## 🚀 Execução

1. Instale as dependências necessárias (de preferência em um ambiente virtual):
   ```bash
   pip install tensorflow==2.18.0 mlflow scikit-learn matplotlib
   ```

2. Execute o notebook `MLFlow_Keras.ipynb` célula por célula.

3. Acompanhe os experimentos via MLflow UI:
   ```bash
   mlflow ui
   ```

4. Acesse em: [http://localhost:5000](http://localhost:5000)

---

## 📁 Organização

- `MLFlow_Keras.ipynb`: notebook principal com todo o código comentado.
- `README.md`: descrição do projeto e instruções de uso.
- `acuracia.png`: gráfico com a evolução da acurácia nos conjuntos de validação.
- `loss.png`: gráfico com a evolução das perdas no conjunto de validação.
