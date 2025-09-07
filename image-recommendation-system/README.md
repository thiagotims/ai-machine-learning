# Sistema de Recomendação Visual por Similaridade 🔎🖼️ 
[![Python](https://img.shields.io/badge/Python-3.10-blue)](https://www.python.org/)   [![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange)](https://www.tensorflow.org/)  [![Colab](https://img.shields.io/badge/Run%20on-Colab-brightgreen)](https://colab.research.google.com/)
## 📝 Descrição
Este projeto consiste na implementação de um **sistema de recomendação de produtos baseado em imagens**, desenvolvido inteiramente no **Google Colab**.   Ele permite ao usuário fornecer imagens de consulta e retorna produtos visualmente semelhantes, considerando **cor, forma, textura e padrão visual**, sem depender de dados textuais como marca ou preço. Esse projeto foi implementado como "*desafio de projeto*" do curso *BairesDev - Machine Learning Training* promovido pela BairesDev em parceria com a Dio.

---
## ⚙️ Funcionalidades
- Upload de **ZIP com 4 imagens de consulta** (uma por classe: `cadeira`, `ursinho`, `bolsa`, `chapeu`).
- Download automático de imagens de referência usando **BingImageCrawler**.
- Extração de **embeddings visuais** via **MobileNetV2** pré-treinado.
- Busca eficiente de imagens similares usando **FAISS (faiss-cpu)**.
- Exibição das **4 imagens mais similares por classe**, com **cosine similarity** e resultados ordenados decrescentemente.
---

## 👨‍💻 Como Executar
1. Abra o notebook no **Google Colab**.
2. Instale dependências (já incluído no notebook):
    `pip install icrawler faiss-cpu tensorflow`
3. Faça upload do arquivo ZIP contendo a **4 imagens de consulta**.
4. Execute todas as células do notebook.
5. Visualize os resultados em grids interativos com as imagens de consulta e as mais similares.

---
## 🧰 Tecnologias

- **Google Colab** → execução e visualização interativa.
- **Python 3**
- **TensorFlow / Keras** → extração de embeddings via MobileNetV2.
- **FAISS (faiss-cpu)** → busca eficiente por similaridade.
- **ICrawler (BingImageCrawler)** → download automático de imagens.
- **IPython Display / HTML** → exibição interativa de resultados.
----
## 🖼️ Resultado

Exemplo contendo imagens inseridas (contornadas em vermelho) e as imagens geradas como resultado:

![predictions](https://github.com/thiagotims/ai-machine-learning/blob/main/image-recommendation-system/predictions/recommendations.png)

---
## 📋 Observações

- O sistema **usa apenas aparência visual** (sem análise de texto ou atributos de produto).
- Os nomes das imagens do ZIP devem conter a palavra-chave da classe (`cadeira`, `ursinho`, `bolsa`, `chapeu`) para serem reconhecidos corretamente.
- Para datasets grandes, considere adaptar para **FAISS GPU** para performance otimizada.
-----
## 📜 Licença

Este projeto é de caráter **educacional e experimental**. O dataset **FaceScrub** é público e disponível sob as condições fornecidas pelos autores.

💡 Projeto desenvolvido no **Google Colab** para estudo de **Visão Computacional** e **Deep Learning**.

----
## 📬 Contato
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/thiagotims/) [![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/devtim/) [![Gmail](https://img.shields.io/badge/Gmail-D14836?style=flat&logo=gmail&logoColor=white)](mailto:thiagotimdev@gmail.com)
