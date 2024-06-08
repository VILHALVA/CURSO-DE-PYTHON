# MANUAL
## 1. INSTALAÇÃO DO PYTHON
Python é uma linguagem de programação que requer a instalação do interpretador Python.

### WINDOWS:
1. Acesse o [site oficial do Python](https://www.python.org/downloads/).
2. Baixe o instalador adequado para Windows.
3. Execute o instalador e marque a opção "Add Python to PATH".
4. Siga as instruções na tela para concluir a instalação.

Para verificar se a instalação foi bem-sucedida, abra o Prompt de Comando e execute:
```sh
python --version
```

### MACOS:
1. Acesse o [site oficial do Python](https://www.python.org/downloads/).
2. Baixe o instalador adequado para macOS.
3. Execute o instalador e siga as instruções na tela.

Para verificar se a instalação foi bem-sucedida, abra o Terminal e execute:
```sh
python3 --version
```

### LINUX:
1. Abra um terminal.
2. Execute os seguintes comandos para instalar o Python:
   ```sh
   sudo apt update
   sudo apt install python3
   ```
3. Para instalar o gerenciador de pacotes `pip`, execute:
   ```sh
   sudo apt install python3-pip
   ```

Para verificar se a instalação foi bem-sucedida, abra um terminal e execute:
```sh
python3 --version
```

## 2. CONFIGURAÇÃO DA IDE (INTEGRATED DEVELOPMENT ENVIRONMENT):
Usar uma IDE facilita muito o desenvolvimento em Python. Algumas das IDEs mais populares são PyCharm e Visual Studio Code.

### PYCHARM:
1. Acesse o [site do PyCharm](https://www.jetbrains.com/pycharm/download/).
2. Baixe a versão Community (gratuita) ou a versão Professional (paga).
3. Instale a IDE seguindo as instruções para o seu sistema operacional.

### VISUAL STUDIO CODE:
1. Baixe e instale o Visual Studio Code no [site oficial](https://code.visualstudio.com/).
2. Abra o Visual Studio Code.
3. Instale a extensão Python:
   1. Clique no ícone de Extensões no lado esquerdo.
   2. Pesquise por "Python" e instale a extensão oficial da Microsoft.

## 3. CRIANDO O PRIMEIRO PROJETO EM PYTHON:
### PASSO A PASSO PARA CRIAR UM PROJETO NO PYCHARM:
1. Abra o PyCharm.
2. Clique em "New Project".
3. Nomeie seu projeto e selecione o diretório onde ele será salvo. Clique em "Create".

### CRIANDO UM ARQUIVO PYTHON:
1. No painel do lado esquerdo, clique com o botão direito na pasta do projeto.
2. Selecione "New" > "Python File".
3. Nomeie o arquivo como `hello_world.py` e clique em "OK".

### ESCREVENDO O CÓDIGO:
No arquivo `hello_world.py` que foi criado, escreva o seguinte código:
```python
print("Hello, World!")
```

### EXECUTANDO O PROJETO NO PYCHARM:
1. Clique com o botão direito no arquivo `hello_world.py`.
2. Selecione "Run 'hello_world'".

### PASSO A PASSO PARA CRIAR UM PROJETO NO VISUAL STUDIO CODE:
1. Abra o Visual Studio Code.
2. Clique em "File" > "Open Folder" e selecione ou crie uma pasta para seu projeto.
3. No painel do lado esquerdo, clique com o botão direito na pasta aberta e selecione "New File".
4. Nomeie o arquivo como `hello_world.py` e clique em "OK".

### ESCREVENDO O CÓDIGO:
No arquivo `hello_world.py`, escreva o seguinte código:
```python
print("Hello, World!")
```

### EXECUTANDO O PROJETO NO VISUAL STUDIO CODE:
1. Abra o terminal integrado no Visual Studio Code (View > Terminal).
2. No terminal, certifique-se de que está no diretório do projeto.
3. Execute o comando:
   ```sh
   python hello_world.py
   ```

Você verá a mensagem `Hello, World!` impressa no terminal.

## CONCLUSÃO:
Agora você tem o Python instalado e configurado, além de um ambiente de desenvolvimento Python pronto com o PyCharm ou Visual Studio Code. Você criou e executou seu primeiro projeto Python. A partir daqui, você pode explorar mais sobre a linguagem Python, bibliotecas e frameworks para expandir suas habilidades de programação.