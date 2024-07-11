# REQUERIMENTOS E MAIS
O arquivo `requirements.txt` é usado para listar todas as dependências (pacotes) de um projeto Python. Isso facilita a instalação de todas as dependências em um novo ambiente ou para outros desenvolvedores que estejam trabalhando no mesmo projeto.

## 1. CRIAR UM AMBIENTE VIRTUAL:
Um ambiente virtual permite criar um ambiente isolado para o seu projeto Python, onde você pode instalar pacotes sem afetar o sistema global ou outros projetos.

1. **Instale o `virtualenv` (se ainda não tiver instalado):**
   ```bash
   pip install virtualenv
   ```

2. **Crie um novo ambiente virtual:**
   ```bash
   virtualenv venv
   ```
   Aqui, `venv` é o nome do diretório onde o ambiente virtual será criado. Você pode escolher qualquer nome.

3. **Ative o ambiente virtual:**
   - No Linux/MacOS:
     ```bash
     source venv/bin/activate
     ```
   - No Windows:
     ```bash
     .\venv\Scripts\activate
     ```

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

