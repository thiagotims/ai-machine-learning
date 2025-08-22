# 📊 Cálculo de Métricas de Avaliação de Aprendizado

Este projeto demonstra como calcular as principais métricas utilizadas na avaliação de modelos de Machine Learning. Além disso, utiliza uma **matriz de confusão interativa** (com sliders no Jupyter Notebook) para permitir a visualização e experimentação dos resultados em tempo real.

---

## 🚀 Funcionalidades

- Cálculo automático das métricas de avaliação:
    - **Sensibilidade (Recall)**
    - **Especificidade**
    - **Acurácia**
    - **Precisão**
    - **F-score**
        
- Visualização da **matriz de confusão** em formato de heatmap.
    
- Interatividade com **sliders** no Jupyter Notebook para alterar valores de VP, VN, FP e FN.
---

## 📚 Fórmulas Utilizadas

|Métrica|Fórmula|
|---|---|
|Sensibilidade|VP / (VP + FN)|
|Especificidade|VN / (FP + VN)|
|Acurácia|(VP + VN) / N|
|Precisão|VP / (VP + FP)|
|F-score|2 * (P * S) / (P+S)|

Legenda:

- VP: Verdadeiros Positivos
- FN: Falsos Negativos
- FP: Falsos Positivos
- VN: Verdadeiros Negativos
- P: Precisão
- S: Sensibilidade
- N: Total de elementos

---

## 🛠️ Tecnologias Utilizadas

- Python 3
- Jupyter Notebook
- Bibliotecas:
    - `matplotlib`
    - `seaborn`
    - `numpy`
    - `ipywidgets`

---

## 📂 Estrutura do Projeto

```
📦 evaluation-metrics-ML
 ┣ 📜 evaluation_metrics.ipynb   # Notebook com código do projeto
 ┣ 📜 README.md                       # Documentação do projeto
 ┣ 📂 imagens                         # Pasta com prints de execução
     ┣ sliders.png
     ┣ heatmap.png
```

---

## ▶️ Como Executar

1. Clone este repositório:
    
    ```bash
    git clone https://github.com/thiagotims/evaluation-metrics-ML.git
    ```
    
2. Instale as dependências:
    
    ```bash
    pip install matplotlib seaborn numpy ipywidgets
    ```
    
3. Abra o Jupyter Notebook:
    
    ```bash
    jupyter notebook
    ```
    
4. Execute o notebook `metricas_classificacao.ipynb` e interaja com os **sliders** para visualizar os cálculos e a matriz de confusão.
    

---

## 📸 Exemplos de Execução

### Sliders para definição da matriz de confusão:

![Exemplo de sliders](https://chatgpt.com/c/imagens/sliders.png)

### Saída da matriz de confusão (heatmap):

![Exemplo de heatmap](https://chatgpt.com/c/imagens/heatmap.png)

### Saída das métricas calculadas:

```
Matriz de Confusão:
VP = 50, FN = 10, FP = 5, VN = 35

Métricas de Avaliação:
Sensibilidade (Recall): 0.83
Especificidade: 0.88
Acurácia: 0.85
Precisão: 0.91
F-score: 0.87
```

---

## 📖 Objetivo Educacional

O objetivo principal deste projeto é **entender na prática como cada métrica funciona** e como alterações na matriz de confusão impactam os valores calculados.

Ideal para estudantes e profissionais que desejam compreender melhor as métricas de avaliação de modelos de classificação.

---

## ✨ Autor

Projeto desenvolvido como exercício de aprendizado em Python e análise de métricas de classificação.
