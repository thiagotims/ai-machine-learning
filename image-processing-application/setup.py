from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image_processing_application",
    version="0.0.1",
    author="Thiago Tim",
    author_email="thiagotimdev@gmail.com",
    description="Aplicação de processamento de imagem usando Skimage",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ubiratan-motta/Processador_de_Imagens",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)