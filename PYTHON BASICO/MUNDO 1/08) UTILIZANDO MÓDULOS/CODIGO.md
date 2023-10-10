# CODIGO
Vou fornecer um exemplo abrangente que utiliza vários módulos Python para realizar uma tarefa útil. Neste exemplo, vamos criar um programa simples para baixar imagens da internet usando os módulos `requests` e `Pillow` (Python Imaging Library).

Certifique-se de que você tenha os módulos `requests` e `Pillow` instalados antes de executar este exemplo. Você pode instalá-los usando o `pip`:

```
pip install requests
pip install Pillow
```

Aqui está o código:

```python
import os
import requests
from PIL import Image

def download_image(url, pasta_destino):
    # Obter o nome do arquivo da URL
    nome_arquivo = url.split("/")[-1]

    # Verificar se a pasta de destino existe, caso contrário, criá-la
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)

    # Construir o caminho completo para salvar o arquivo
    caminho_arquivo = os.path.join(pasta_destino, nome_arquivo)

    # Enviar uma solicitação GET para baixar a imagem
    response = requests.get(url)

    if response.status_code == 200:
        # Abrir e salvar a imagem localmente
        with open(caminho_arquivo, 'wb') as arquivo:
            arquivo.write(response.content)
        print(f"Imagem baixada com sucesso como {caminho_arquivo}")
        return caminho_arquivo
    else:
        print(f"Falha ao baixar a imagem de {url}")
        return None

def redimensionar_imagem(caminho_imagem, largura, altura):
    imagem = Image.open(caminho_imagem)
    imagem_redimensionada = imagem.resize((largura, altura), Image.ANTIALIAS)
    imagem_redimensionada.save(caminho_imagem)
    print(f"Imagem redimensionada para {largura}x{altura} pixels")

if __name__ == "__main__":
    url_imagem = "https://www.example.com/imagem.jpg"
    pasta_destino = "imagens"
    largura_desejada = 800
    altura_desejada = 600

    caminho_imagem = download_image(url_imagem, pasta_destino)
    if caminho_imagem:
        redimensionar_imagem(caminho_imagem, largura_desejada, altura_desejada)
```

Neste exemplo, estamos:

1. Importando os módulos `os`, `requests`, e `Pillow`.
2. Definindo uma função `download_image()` para baixar uma imagem da internet e salvá-la localmente.
3. Definindo uma função `redimensionar_imagem()` para redimensionar a imagem para um tamanho específico.
4. No bloco principal do programa, especificamos a URL da imagem, a pasta de destino, a largura e altura desejadas.
5. Chamando `download_image()` para baixar a imagem e `redimensionar_imagem()` para redimensioná-la (se o download for bem-sucedido).

Este é um exemplo prático que ilustra como os módulos Python podem ser usados para automatizar tarefas úteis, como o download e manipulação de imagens da internet.