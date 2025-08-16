from PIL import Image
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog

# Função 1 - Converter para escala de cinza (usando luminância perceptiva)
def to_grayscale(image):
    largura, altura = image.size
    pixels = image.load()

    for y in range(altura):
        for x in range(largura):
            r, g, b = pixels[x, y]
            # Fórmula de luminância perceptiva
            gray = int(0.299 * r + 0.587 * g + 0.114 * b)
            pixels[x, y] = (gray, gray, gray)
    return image

# Função 2 - Converter para imagem binarizada (preto e branco)
def to_binary(image, limiar=128):
    largura, altura = image.size
    pixels = image.load()

    for y in range(altura):
        for x in range(largura):
            r, g, b = pixels[x, y]
            # Converter para escala de cinza primeiro (luminância)
            gray = int(0.299 * r + 0.587 * g + 0.114 * b)
            # Binarizar
            valor = 255 if gray >= limiar else 0
            pixels[x, y] = (valor, valor, valor)
    return image

# --------------------
# Função para escolher arquivo via caixa do SO
# --------------------
def escolher_imagem():
    root = tk.Tk()
    root.withdraw()  # Esconde a janela principal
    caminho = filedialog.askopenfilename(
        title="Selecione uma imagem",
        filetypes=[("Imagens", "*.jpg *.jpeg *.png *.bmp")]
    )
    return caminho

# --------------------
# Blocos principais
# --------------------

def main_cinza():
    caminho = escolher_imagem()
    imagem = Image.open(caminho).convert("RGB")
    gray_img = imagem.copy()
    gray_img = to_grayscale(gray_img)
    gray_img.save("saida_cinza.jpg")

    # Mostrar resultado
    plt.imshow(gray_img)
    plt.title("Imagem em Cinza")
    plt.axis("off")
    plt.show()
    print("Imagem em cinza salva!")


def main_binaria():
    caminho = escolher_imagem()
    imagem = Image.open(caminho).convert("RGB")
    bin_img = imagem.copy()
    bin_img = to_binary(bin_img, limiar=128)
    bin_img.save("saida_binaria.jpg")

    # Mostrar resultado
    plt.imshow(bin_img)
    plt.title("Imagem Binária")
    plt.axis("off")
    plt.show()
    print("Imagem binária salva!")


def main_comparacao():
    caminho = escolher_imagem()
    imagem = Image.open(caminho).convert("RGB")

    gray_img = to_grayscale(imagem.copy())
    bin_img = to_binary(imagem.copy(), limiar=128)

    # Mostrar todas lado a lado
    fig, axs = plt.subplots(1, 3, figsize=(12, 4))
    axs[0].imshow(imagem)
    axs[0].set_title("Original")
    axs[0].axis("off")

    axs[1].imshow(gray_img)
    axs[1].set_title("Cinza (Luminância)")
    axs[1].axis("off")

    axs[2].imshow(bin_img)
    axs[2].set_title("Binária")
    axs[2].axis("off")

    plt.tight_layout()
    plt.show()
    print("Comparação concluída!")


# --------------------
# Execução controlada
# --------------------
if __name__ == "__main__":
    # Escolha qual parte rodar comentando/descomentando
    # main_cinza()
    # main_binaria()
    main_comparacao()
