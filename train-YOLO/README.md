# 🧠 Treinamento da Rede YOLOv8 com a base de dados COCO128 no Google Colab

Este projeto demonstra o treinamento de uma rede **YOLOv8** utilizando o dataset **COCO128**, rodando **inteiramente no Google Colab** e salvando resultados diretamente no Google Drive. Esse projeto foi implementado no âmbito do desafio de projeto do curso BairesDev - Machine Learning Training promovido pela BairesDev em parceria com a Dio.

---
## 📌 Sobre o projeto

• Framework: [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)
• Dataset: **COCO128** (subset oficial do COCO, com 128 imagens em múltiplas classes)
• Ambiente: **Google Colab** (com GPU Tesla T4)
•  Armazenamento: **Google Drive** (dataset, YAML e resultados)

O objetivo é demonstrar um fluxo completo de:
1. Configuração do Colab e montagem do Google Drive.
2. Estruturação do dataset no formato YOLO.
3. Treinamento e validação do modelo YOLOv8.
4. Predição em imagens de teste.
5. Exportação do modelo treinado para deploy.
6. Inferência utilizando os modelos exportados.
---
## 📂 Estrutura de diretórios (Google Colab)

  Após organizar os arquivos no Google Drive, a pasta final deve ficar assim:


```bash
📁 /MyDrive/coco128/
├── images/
│ └── train2017/ # imagens do dataset
├── labels/
│ └── train2017/ # labels em formato YOLO
├── coco128.yaml # arquivo de configuração do dataset
└── runs/ # resultados de treino e predições
```

---
## 📊 Dataset COCO128
- O **COCO128** é um conjunto reduzido de 128 imagens do famoso **COCO dataset**.
- É utilizado pela Ultralytics como exemplo rápido para testes de treinamento.
- Contém **80 classes** de objetos anotadas em formato YOLO.
- Por ser pequeno, é ideal para prototipagem e validação de pipelines no Colab.

  Mais informações: [COCO128 Dataset](https://github.com/ultralytics/coco128)
---
## 📦 Dependências

#### ✅ Mínimas (treino e predição com Ultralytics)

No Colab, execute:
```bash
pip install "ultralytics==8.3.189"
```

Isso traz como dependências principais: torch e numpy.
Se for usar os exemplos de visualização/pós-processamento, instale também:
```bash
pip install opencv-python
```

#### 🔁 Exportação / Inferência (opcional, escolha conforme o formato)
- ONNX + ONNX Runtime (CPU/GPU):
```bash
pip install onnx onnxruntime  # (CPU)
# ou, se tiver GPU compatível:
# pip install onnx onnxruntime-gpu
```

TorchScript: já funciona com o torch que vem com o Ultralytics.

#### TensorRT (ENGINE): 
(requer TensorRT instalado no sistema. Em ambientes Colab públicos geralmente não está disponível por padrão.)

TensorFlow Lite (TFLite):
```bash
pip install "tensorflow<2.16"
```

---
## 🚀 Treinamento no Colab
O treinamento foi realizado no Colab com GPU, utilizando o seguinte comando:

```python
from ultralytics import YOLO


# carregar modelo pré-treinado YOLOv8 nano
model = YOLO("yolov8n.pt")

# treinar no coco128
results = model.train(
data="/content/drive/MyDrive/coco128/coco128.yaml",
epochs=10,
imgsz=640,
batch=16,
project="/content/drive/MyDrive/coco128/runs",
name="exp_coco128"
)
```

  Resultados, métricas e pesos ficam salvos em:
/MyDrive/coco128/runs/exp_coco128/

---
## 🔁 Reproduzindo no Colab

Se quiser rodar do zero, siga estes passos:


 ❶ Montar o Google Drive no Colab
```python
from google.colab import drive
drive.mount('/content/drive')
```

 ❷  Baixar e extrair o dataset COCO128
```python
!curl -L "https://ultralytics.com/assets/coco128.zip" -o coco128.zip

!unzip -q coco128.zip -d /content/drive/MyDrive/
```

❸  Criar o arquivo coco128.yaml no Drive
```python
import os

yaml_content = """path: /content/drive/MyDrive/coco128
train: images/train2017
val: images/train2017
names:
  0: person
  1: bicycle
  2: car
  ...
  79: toothbrush
"""
with open("/content/drive/MyDrive/coco128/coco128.yaml", "w") as f:
    f.write(yaml_content)

print("✅ coco128.yaml criado em /content/drive/MyDrive/coco128/")

```

❹  Instalar YOLOv8 e treinar

```python
!pip install ultralytics

from ultralytics import YOLO

model = YOLO("yolov8n.pt")
results = model.train(
    data="/content/drive/MyDrive/coco128/coco128.yaml",
    epochs=10,
    imgsz=640,
    batch=16,
    project="/content/drive/MyDrive/coco128/runs",
    name="exp_coco128"
)
```

---
## 📷 Resultados da predição

![Output](https://github.com/thiagotims/ai-machine-learning/blob/main/train-YOLO/predictions/247290e3-b4fa-48ef-84d8-5f99a7d2634f.jpeg)


----
## 📤 Exportação do modelo treinado

  Depois de treinar, você pode exportar o modelo para diversos formatos compatíveis com deploy em diferentes ambientes:

```python

from ultralytics import YOLO

# carregar último modelo treinado
model = YOLO("/content/drive/MyDrive/coco128/runs/exp_coco128/weights/best.pt")

# exportar para diferentes formatos
model.export(format="onnx")        # ONNX
model.export(format="torchscript") # TorchScript
model.export(format="engine")      # TensorRT
model.export(format="tflite")      # TensorFlow Lite
```

Os arquivos exportados serão salvos na mesma pasta do modelo original:
/MyDrive/coco128/runs/exp_coco128/weights/

----
## 🖼️ Inferência pós-exportação

  Após exportar, é possível carregar e rodar inferência diretamente com os formatos exportados.

🔹 Exemplo: inferência com modelo ONNX
```python
import onnxruntime as ort
import cv2

# carregar modelo ONNX
session = ort.InferenceSession("/content/drive/MyDrive/coco128/runs/exp_coco128/weights/best.onnx")

# carregar imagem de teste
image = cv2.imread("/content/drive/MyDrive/coco128/images/train2017/000000000009.jpg")
image_resized = cv2.resize(image, (640, 640))

# preparar entrada
import numpy as np
input_name = session.get_inputs()[0].name
input_data = image_resized.transpose(2,0,1)[None].astype(np.float32) / 255.0

# rodar inferência
outputs = session.run(None, {input_name: input_data})
print("🔎 Inferência ONNX finalizada!")

```

  🔹 Exemplo: inferência com modelo TorchScript
```python
import torch

# carregar modelo TorchScript
ts_model = torch.jit.load("/content/drive/MyDrive/coco128/runs/exp_coco128/weights/best.torchscript")

# rodar predição
img = torch.rand(1, 3, 640, 640)  # exemplo com tensor aleatório
preds = ts_model(img)
print("🔎 Inferência TorchScript finalizada!")

```

---
## 🏆 Conclusão

• Foi possível treinar e validar um modelo YOLOv8 usando um dataset leve (COCO128). 

• O fluxo é totalmente reproduzível no Google Colab, sem necessidade de configuração local.

• Além do treinamento, o modelo pode ser exportado para diversos formatos de deploy.

• A inferência pós-exportação garante que o modelo pode rodar em diferentes frameworks e dispositivos.

----
## 📜 Licença

Este projeto utiliza o dataset COCO128, que utiliza a licença Creative Commons Attribution 4.0 International (CC BY 4.0).

----
