# Redução de Dimensionalidade em Imagens

## Resumo do Projeto

Este projeto em Python realiza transformações de imagens coloridas, reduzindo a quantidade de informação visual por meio de duas operações principais: conversão para **escala de cinza** e **binarização** (preto e branco). O objetivo é demonstrar como reduzir a complexidade das imagens para facilitar análises ou processamento posterior, sem depender de bibliotecas complexas de processamento de imagem além do Python nativo e PIL para manipulação básica. Esse projeto foi implementado no âmbito do desafio de projeto do curso *BairesDev - Machine Learning Training* promovido pela BairesDev em parceria com a Dio.

O projeto inclui **duas versões do código**:

1. **Versão simples (média dos canais RGB)**:
    - Converte a imagem em cinza utilizando a média simples dos canais vermelho, verde e azul.
    - Binariza a imagem usando um limiar fixo de 128.
        
2. **Versão com luminância perceptiva**:    
    - Converte a imagem em cinza considerando a percepção humana de luminosidade, usando a fórmula: `Gray = 0.299*R + 0.587*G + 0.114*B`.
    - A binarização também é baseada nesta escala de cinza perceptiva.
        
## Funcionalidades

- Abrir uma imagem usando uma **caixa de diálogo do sistema operacional** (Tkinter).
- Converter para **escala de cinza**.
- Converter para **imagem binarizada** (preto e branco).
- Mostrar as imagens originais e transformadas lado a lado usando **Matplotlib**.
- Salvar as imagens resultantes em arquivos locais (`saida_cinza.jpg`, `saida_binaria.jpg`).
    

## Estrutura do Código
- `to_grayscale(image)`: Converte a imagem para escala de cinza.
- `to_binary(image, limiar=128)`: Converte a imagem para preto e branco, com limiar ajustável.
- `escolher_imagem()`: Abre a caixa de diálogo para seleção da imagem.
- `main_cinza()`: Executa apenas a conversão em cinza.
- `main_binaria()`: Executa apenas a conversão binária.
- `main_comparacao()`: Executa todas as transformações e mostra os resultados lado a lado.
## Como Executar

1. Clone este repositório:
```bash
git clone https://github.com/thiagotims/ai-machine-learning/img-dimensionality-reduction.git
```

2. Instale as dependências (Python 3, Pillow, Matplotlib):
```bash
pip install pillow matplotlib
```

3. Execute o script principal:
```bash
python image_transform.py
```

4. Escolha a imagem desejada na caixa de seleção.
    
5. Comente ou descomente a função desejada no bloco `if __name__ == "__main__":` para rodar:
    - `main_cinza()`
    - `main_binaria()`
    - `main_comparacao()`
## Resultados
1. Imagem transformada: [image-transformed.png](https://github.com/thiagotims/ai-machine-learning/blob/main/img-dimensionality-reduction/image-transformed.png)
2. Imagem transformada (com luminância): [image-transformed(luminance).png](https://github.com/thiagotims/ai-machine-learning/blob/main/img-dimensionality-reduction/image-transformed(luminance).png)



## Observações
- A versão com **luminância perceptiva** oferece resultados mais próximos da percepção visual humana, pois pondera o canal verde mais fortemente, refletindo a sensibilidade do olho.
- O projeto utiliza **Python nativo** para o cálculo da escala de cinza e binarização, sem recorrer a funções prontas de bibliotecas de processamento de imagem.
## Licença
Este projeto é open-source e pode ser usado e modificado livremente.
