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

## GERECIANDO MULTIPLAS VERSÕES DO PYTHON:
O `pyenv` é uma ferramenta que funciona de forma muito semelhante ao `nvm` (Node Version Manager) e ao `volta`, mas para a linguagem Python. Ele permite que você gerencie múltiplas versões do interpretador Python no seu sistema, facilitando a instalação, troca, e uso de diferentes versões de Python em diferentes projetos.

1. **Instalação de Múltiplas Versões do Python**:
   - Com o `pyenv`, você pode instalar diferentes versões do Python, desde versões antigas até as mais recentes, e até mesmo versões específicas como Anaconda, PyPy, ou versões específicas de desenvolvimento.
   - Comandos típicos incluem:
     ```bash
     pyenv install 3.9.1
     pyenv install 3.10.4
     ```

2. **Troca entre Versões**:
   - O `pyenv` permite que você troque entre diferentes versões do Python globalmente, por usuário, ou até mesmo em nível de diretório/projeto.
   - Para definir uma versão global:
     ```bash
     pyenv global 3.9.1
     ```
   - Para definir uma versão para o diretório atual (projeto):
     ```bash
     pyenv local 3.10.4
     ```
   - Isso cria um arquivo `.python-version` no diretório do projeto, que indica ao `pyenv` qual versão do Python usar naquele contexto.

3. **Compatibilidade com Ferramentas**:
   - O `pyenv` trabalha bem com ferramentas como o `poetry`, que gerenciam dependências e ambientes virtuais. Depois de definir a versão do Python com `pyenv`, você pode usar o `poetry` para gerenciar as dependências do projeto nessa versão específica do Python.

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


