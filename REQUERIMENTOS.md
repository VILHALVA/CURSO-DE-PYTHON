# REQUERIMENTOS E MAIS
O arquivo `requirements.txt` é usado para listar todas as dependências (pacotes) de um projeto Python. Isso facilita a instalação de todas as dependências em um novo ambiente ou para outros desenvolvedores que estejam trabalhando no mesmo projeto.

## 1. CRIAR UM AMBIENTE VIRTUAL:
1. **Crie o ambiente virtual:**
   Você pode instalar o `virtualenv` usando o `pip`, que é o gerenciador de pacotes do Python.

   Para instalar o `virtualenv`, você pode executar o seguinte comando:

   ```
   pip install virtualenv
   ```

   Depois de instalar o `virtualenv`, você pode criar um novo ambiente virtual com o seguinte comando:

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

## 2. INSTALAR PACOTES E ADICIONÁ-LOS AO `REQUIREMENTS.TXT`:
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

## 3. INSTALAR DEPENDÊNCIAS A PARTIR DO `REQUIREMENTS.TXT`:
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

## CONCLUSÃO:
Trabalhar com ambientes virtuais e `requirements.txt` é uma prática essencial para manter seu projeto Python organizado e facilmente reproduzível. Isso garante que todos os colaboradores e ambientes de desenvolvimento estejam alinhados com as mesmas dependências e versões de pacotes.

