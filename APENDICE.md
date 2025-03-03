# APÊNDICE
## CRIAR UM AMBIENTE VIRTUAL:
1. **Crie o ambiente virtual:**
   Você pode instalar o `virtualenv` usando o `pip`, que é o gerenciador de pacotes do Python.

   Para instalar o `virtualenv`, você pode executar o seguinte comando:

   ```
   pip install virtualenv
   ```

   Depois de instalar o `virtualenv`, você pode criar um novo ambiente virtual com o seguinte comando:

   ```
   virtualenv venv
   ```

   Ou:

   ```
   python -m venv venv
   ```

   Se quiser, você pode substituir "venv" pelo nome que você deseja dar ao seu ambiente virtual (Não se esqueça de atualizar o `.gitignore`). Em seguida, você pode ativar o ambiente virtual com os seguintes comandos:

   - No Windows:

   ```
   venv\Scripts\activate
   ```

   - No Linux/Mac:

   ```
   source venv/bin/activate
   ```

   Uma vez ativado o ambiente virtual, você pode tentar instalar os pacotes necessários usando o `pip`, e eles serão instalados apenas no escopo do ambiente virtual, evitando possíveis conflitos com outros pacotes no seu sistema.

---

## GERECIANDO MULTIPLAS VERSÕES DO PYTHON:
O `pyenv` é uma ferramenta que permite gerenciar múltiplas versões do interpretador Python no seu sistema. Ele funciona de forma semelhante ao `nvm` (Node Version Manager) e ao `volta`, mas para Python, facilitando a instalação, troca e uso de diferentes versões em projetos distintos.  

1. **Instalando o `pyenv` no Windows**:  
O `pyenv` não é instalado diretamente via `pip`. No Windows, a instalação pode ser feita via o repositório oficial do `pyenv-win`:  

   1. **Baixar e instalar o `pyenv-win`**  
      Abra o PowerShell como administrador e execute:  
      ```powershell
      Invoke-WebRequest -UseBasicParsing -Uri https://pyenv.run | Invoke-Expression
      ```  
      Isso instalará o `pyenv`, `pyenv-doctor`, `pyenv-win`, e `pyenv-update`.

   2. **Adicionar `pyenv` ao PATH**  
      Se o instalador automático não configurar corretamente o ambiente, faça manualmente:  
      - **Abra as Variáveis de Ambiente**  
      - No Windows, pesquise por **"Variáveis de Ambiente"** e abra.  
      - **Adicione os seguintes caminhos ao `PATH` do sistema ou do usuário**:
      ```
      C:\pyenv\pyenv-win\bin
      C:\pyenv\pyenv-win\shims
      ```
      - Reinicie o terminal após isso.

   3. **Verificar se a instalação foi bem-sucedida**  
      ```sh
      pyenv --version
      ```

2. **Instalando e Gerenciando Múltiplas Versões do Python**:
Com o `pyenv`, você pode instalar diferentes versões do Python, incluindo versões antigas, recentes, Anaconda, PyPy e versões específicas de desenvolvimento.  

- Para listar versões disponíveis:  
  ```sh
  pyenv install --list
  ```
- Para instalar versões específicas:  
  ```sh
  pyenv install 3.9.1
  pyenv install 3.10.4
  ```

3. **Alternando Entre Versões do Python**:
O `pyenv` permite definir qual versão do Python será usada de três formas:  

- **Globalmente** (para todo o sistema):  
  ```sh
  pyenv global 3.9.1
  ```
- **Por usuário** (padrão para o usuário atual):  
  ```sh
  pyenv shell 3.10.4
  ```
- **Por diretório/projeto** (criando um arquivo `.python-version`):  
  ```sh
  pyenv local 3.10.4
  ```

Isso garante que projetos diferentes utilizem versões de Python compatíveis sem conflitos.

4. **Atualizando e Desinstalando o `pyenv`**:
- Para atualizar o `pyenv`:  
  ```sh
  pyenv update
  ```
- Para desinstalar o `pyenv-win`, basta remover as pastas `C:\pyenv\pyenv-win` e limpar as variáveis de ambiente adicionadas.

---

## USANDO O `pyenv` NO AMBIENTE VIRTUAL:
1. **Instalar o `pyenv` (se ainda não tiver)** : 
Se ainda não instalou o `pyenv-win`, siga o guia oficial:  
🔗 [https://github.com/pyenv-win/pyenv-win](https://github.com/pyenv-win/pyenv-win)  

2. **Instalar a versão desejada do Python**: 
Verifique quais versões estão disponíveis:  
```sh
pyenv install --list
```  
Instale a versão específica (exemplo: 3.10.0):  
```sh
pyenv install 3.10.0
```  

3. **Criar um ambiente virtual com essa versão**: 
Execute o comando abaixo no terminal:  
```sh
"C:\pyenv\pyenv-win\versions\3.10.0\python.exe" -m venv venv
```  
Isso criará um ambiente virtual na pasta `venv` usando o Python 3.10.0.  

4. **Ativar o ambiente virtual**:  
- No **CMD** ou **PowerShell**:
  ```sh
  venv\Scripts\activate
  ```  
- No **Git Bash**:
  ```sh
  source venv/Scripts/activate
  ```  

5. **Verificar a versão do Python**:  
Após ativar o ambiente, confirme a versão usada:  
```sh
python --version
```  

Isso garante que o ambiente virtual está rodando com o Python instalado via `pyenv`. 🚀

---

## GERENCIANDO DEPENDÊNCIAS COM `poetry`:
### CONCEITO:
O `poetry` é uma ferramenta moderna para gerenciamento de dependências e empacotamento de projetos Python. Ele simplifica o processo de criação e manutenção de ambientes virtuais, instalação de pacotes, e gerenciamento de dependências, tornando o desenvolvimento em Python mais eficiente e organizado.

1. **Gerenciamento de Dependências**:
   - O `poetry` facilita a instalação, atualização e remoção de pacotes Python. Ele resolve automaticamente as dependências e assegura que todas as versões dos pacotes sejam compatíveis entre si.
   - As dependências são definidas em um arquivo chamado `pyproject.toml`, que é equivalente ao `package.json` no Node.js.

2. **Criação e Gerenciamento de Ambientes Virtuais**:
   - O `poetry` gerencia automaticamente ambientes virtuais para o projeto, garantindo que as dependências sejam isoladas, evitando conflitos entre pacotes de diferentes projetos.
   - Você pode usar o comando `poetry shell` para entrar no ambiente virtual ou `poetry run <comando>` para executar comandos diretamente dentro dele.

3. **Empacotamento e Distribuição**:
   - O `poetry` facilita a criação de pacotes para distribuição, gerando automaticamente arquivos como `setup.py` a partir das configurações no `pyproject.toml`.
   - Ele suporta a publicação de pacotes no PyPI ou em outros repositórios, simplificando o processo de distribuição de bibliotecas Python.

4. **Scripts Personalizados**:
   - O `poetry` permite definir scripts personalizados que podem ser executados com o comando `poetry run <script>`. Isso é útil para automatizar tarefas comuns no ciclo de desenvolvimento.

### ESTRUTURA:
O arquivo `pyproject.toml` é onde as configurações do projeto e as dependências são definidas. Um exemplo básico pode parecer assim:

```toml
[tool.poetry]
name = "meu-projeto"
version = "0.1.0"
description = "Uma breve descrição do projeto"
authors = ["Seu Nome <email@exemplo.com>"]

[tool.poetry.dependencies]
python = "^3.8"
flask = "^2.0.1"

[tool.poetry.dev-dependencies]
pytest = "^6.2.4"

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"
```

- **`[tool.poetry]`**: Contém metadados do projeto como nome, versão e descrição.
- **`[tool.poetry.dependencies]`**: Lista as dependências de produção do projeto.
- **`[tool.poetry.dev-dependencies]`**: Lista as dependências necessárias apenas para desenvolvimento (como ferramentas de teste).
- **`[build-system]`**: Define as configurações para o sistema de build, que são necessárias para empacotamento.

### COMANDOS:
- **`poetry init`**: Cria um novo arquivo `pyproject.toml` e inicia um novo projeto.
- **`poetry add <pacote>`**: Adiciona uma nova dependência ao projeto e a instala.
- **`poetry install`**: Instala todas as dependências listadas no `pyproject.toml`.
- **`poetry update`**: Atualiza as dependências para suas versões mais recentes compatíveis.
- **`poetry build`**: Cria pacotes distribuíveis (`sdist` e `wheel`) para o projeto.
- **`poetry publish`**: Publica o pacote no PyPI ou em outro repositório configurado.
- **`poetry run <comando>`**: Executa um comando no contexto do ambiente virtual.
- **`poetry shell`**: Entra no ambiente virtual do projeto.

---

## INSTALAR PACOTES E ADICIONÁ-LOS AO `REQUIREMENTS.TXT`:
1. **Instale os pacotes necessários para o seu projeto:**
   ```bash
   pip install <package_name>
   ```
   Por exemplo, para instalar o Flask:
   ```bash
   pip install flask
   ```

2. **Adicione todas as dependências instaladas ao `requirements.txt`:**
   ```bash
   pip freeze > requirements.txt
   ```

---

## INSTALAR DEPENDÊNCIAS A PARTIR DO `REQUIREMENTS.TXT`:
Para instalar todas as dependências listadas no `requirements.txt` em um novo ambiente ou em um ambiente existente, siga estes passos:

1. **Crie e ative um novo ambiente virtual (se ainda não estiver em um):**
   ```bash
   virtualenv venv
   source venv/bin/activate  # No Linux/MacOS
   # ou
   .\venv\Scripts\activate  # No Windows
   ```

2. **Instale todas as dependências a partir do `requirements.txt`:**
   ```bash
   pip install -r requirements.txt
   ```


