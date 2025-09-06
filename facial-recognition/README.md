# 🔎 Sistema de Reconhecimento Facial com FaceScrub

Este projeto apresenta um sistema de *reconhecimento facial de celebridades* desenvolvido em Python, utilizando **TensorFlow/Keras** para treinamento e **MTCNN** para detecção de rostos.   O projeto foi implementado e testado diretamente no **Google Colab**, utilizando o acesso à GPU gratuito da plataforma.

---
## 📌 Descrição do Projeto

O objetivo deste sistema é:
- Detectar rostos em imagens utilizando **MTCNN**  
- Treinar um modelo de classificação com base em **redes convolucionais (CNNs)**  
- Reconhecer *celebridades* a partir do dataset [**FaceScrub**](https://www.kaggle.com/datasets/rajnishe/facescrub-full)  
- Exibir a predição com **bounding box** no rosto detectado e o **nome da celebridade + percentual de confiança**

⚡ Devido a limitações de memória no Colab, foi selecionado um subconjunto do dataset contendo *10 classes (celebridades mais frequentes)*, o que permite treinar mais rápido e ainda demonstrar bem a eficácia do sistema.

---
## 📊 Dataset: FaceScrub

- Nome: **FaceScrub**  
- Fonte: [Kaggle - FaceScrub Full](https://www.kaggle.com/datasets/rajnishe/facescrub-full)  
- Total de imagens originais: **41.805**  
- Número de classes (celebridades): **513**  
- Estrutura original:
  - `actor_faces/` (atores masculinos)  
  - `actress_faces/` (atrizes femininas)  

Para este projeto, foi criada uma pasta combinada (`facescrub_selected/`) contendo apenas um *subconjunto com as top-N classes* (ex.: 10), a fim de reduzir o consumo de memória e acelerar o treinamento.

### 🎭 Celebridades Selecionadas (Top-10)

As classes utilizadas foram as *10 celebridades com mais imagens disponíveis no dataset*:
 - Kristin_Chenoweth: 148 imagens
 - America_Ferrera: 146 imagens
 - Gabriel_Macht: 140 imagens
 - Felicity_Huffman: 136 imagens
 - Holly_Marie_Combs: 133 imagens
 - Fran_Drescher: 132 imagens
 - Geena_Davis: 131 imagens
 - Debra_Messing: 130 imagens
 - Courteney_Cox: 128 imagens
 - Julie_Benz: 128 imagens

---

## 🧑‍💻 Tecnologias Utilizadas

• [Python 3](https://www.python.org/)  
• [Google Colab](https://colab.research.google.com/)  
• [TensorFlow / Keras](https://www.tensorflow.org/)  
• [scikit-learn](https://scikit-learn.org/stable/)  
• [MTCNN](https://github.com/ipazc/mtcnn)  
• [Matplotlib](https://matplotlib.org/)  

---

## ⚙️ Fluxo do Sistema

1. **Carregamento do dataset FaceScrub**  
2. **Seleção das top-N classes** mais frequentes  
3. **Pré-processamento das imagens** (redimensionamento, normalização, one-hot encoding dos rótulos)  
4. **Treinamento da CNN** com **data augmentation**  
5. **Avaliação do modelo** em dados de teste  
6. **Predição em imagens externas**  
   - Detecção de rostos (MTCNN)  
   - Recorte e classificação do rosto  
   - Exibição do bounding box com nome + confiança  

---

## 🚀 Como Executar

1. Clone este repositório no seu Google Drive ou ambiente local:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   ```

2. Baixe o dataset **FaceScrub** do Kaggle e organize em:
        `/content/drive/MyDrive/facescrub_full/`
    
3. Combine as pastas `actor_faces/` e `actress_faces/` em uma pasta única:
    `/content/drive/MyDrive/facescrub_selected/`
    
4. Abra o **notebook** no Google Colab e execute todas as células.

## 🖼️ Resultado

Exemplo de predição em imagem externa:

![Output](https://github.com/thiagotims/ai-machine-learning/blob/main/facial-recognition/predictions/predictions.png)

## 🔮 Melhorias Propostas
- Expandir para todas as 513 classes do FaceScrub (necessário mais memória/infraestrutura).
- Ajustar a arquitetura da CNN para maior robustez.
- Avaliar uso de **transfer learning** com modelos pré-treinados (ResNet, EfficientNet, MobileNet).
- Implementar uma API de reconhecimento facial em tempo real.

## 📜 Licença
Este projeto é de caráter **educacional e experimental**.   O dataset **FaceScrub** é público e disponível sob as condições fornecidas pelos autores.

💡 Projeto desenvolvido no **Google Colab** para estudo de **Visão Computacional** e **Deep Learning**.
