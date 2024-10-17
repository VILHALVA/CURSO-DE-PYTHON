# CRIANDO UM CRUD
## CONCEITO:
CRUD é um acrônimo para Create, Read, Update e Delete, que representam as quatro operações básicas realizadas em bancos de dados ou sistemas de gerenciamento de dados. Essas operações correspondem a:

1. **Create (Criação):** Inserir novos registros ou objetos no banco de dados.
2. **Read (Leitura):** Recuperar informações existentes do banco de dados.
3. **Update (Atualização):** Modificar registros ou objetos existentes no banco de dados.
4. **Delete (Exclusão):** Remover registros ou objetos do banco de dados.

Essas operações formam a base para muitos sistemas de software que interagem com bancos de dados, desde aplicativos simples até sistemas complexos.

Aqui está um exemplo de como criar um CRUD simples em Python usando uma base de dados SQLite e a biblioteca `sqlite3`:

1. **Create (Criação):**
```python
import sqlite3

def create_record(conn, name, email):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
    conn.commit()
    cursor.close()

# Exemplo de uso
conn = sqlite3.connect('database.db')
create_record(conn, 'João', 'joao@example.com')
conn.close()
```

2. **Read (Leitura):**
```python
import sqlite3

def read_records(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    records = cursor.fetchall()
    cursor.close()
    return records

# Exemplo de uso
conn = sqlite3.connect('database.db')
records = read_records(conn)
print(records)
conn.close()
```

3. **Update (Atualização):**
```python
import sqlite3

def update_record(conn, user_id, new_email):
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET email=? WHERE id=?", (new_email, user_id))
    conn.commit()
    cursor.close()

# Exemplo de uso
conn = sqlite3.connect('database.db')
update_record(conn, 1, 'novo_email@example.com')
conn.close()
```

4. **Delete (Exclusão):**
```python
import sqlite3

def delete_record(conn, user_id):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id=?", (user_id,))
    conn.commit()
    cursor.close()

# Exemplo de uso
conn = sqlite3.connect('database.db')
delete_record(conn, 1)
conn.close()
```

Neste exemplo, estamos utilizando o SQLite como um banco de dados embutido, mas os princípios básicos do CRUD em Python são aplicáveis a outros sistemas de gerenciamento de bancos de dados também. Cada função executa uma operação específica em relação aos dados armazenados no banco de dados.

## TIPOS DE BANCO DE DADOS:
Em Python, você pode implementar o CRUD utilizando uma variedade de tipos de banco de dados e formatos de armazenamento de dados, como SQL, NoSQL, JSON, arquivos de texto (TXT), arquivos de dados serializados (pkl), entre outros. Cada tipo de banco de dados ou formato de armazenamento tem suas próprias características e é adequado para diferentes tipos de aplicativos. Aqui está uma breve explicação de como você poderia implementar o CRUD em diferentes tipos de armazenamento de dados:

1. **Bancos de Dados Relacionais (SQL):**
   - Exemplos incluem SQLite, MySQL, PostgreSQL, SQL Server, entre outros.
   - Você pode usar bibliotecas como `sqlite3`, `mysql-connector-python`, `psycopg2`, `pyodbc`, etc., para se conectar e interagir com esses bancos de dados.
   - O código de CRUD seria semelhante ao exemplo fornecido anteriormente, mas com diferenças nas consultas SQL e na conexão com o banco de dados específico.

2. **Bancos de Dados NoSQL:**
   - Exemplos incluem MongoDB, Cassandra, Redis, entre outros.
   - Para bancos de dados NoSQL, você usaria bibliotecas específicas para cada banco de dados, como `pymongo` para MongoDB.
   - As operações CRUD podem ser realizadas usando métodos fornecidos pelas respectivas bibliotecas.

3. **JSON:**
   - O Python possui suporte nativo para manipulação de JSON, mas você também pode usar a biblioteca `json`.
   - Para criar, ler, atualizar e excluir registros em um arquivo JSON, você manipularia o arquivo diretamente ou usaria as funções `json.dump()` e `json.load()` para salvar e carregar dados em um arquivo JSON.

4. **Arquivos de Texto (TXT):**
   - Para armazenar dados em arquivos de texto simples, você pode abrir o arquivo em modo de escrita ou leitura e escrever ou ler os dados conforme necessário.
   - A manipulação de arquivos de texto em Python é feita com funções como `open()`, `read()`, `write()`, etc.

5. **Arquivos de Dados Serializados (pkl):**
   - Python oferece suporte à serialização de objetos usando a biblioteca `pickle`.
   - Com `pickle`, você pode serializar objetos Python e armazená-los em arquivos para posterior recuperação.
   - As operações CRUD seriam realizadas serializando e desserializando objetos conforme necessário.

## SAIBA MAIS:
- [FAÇA O CURSO DE NODEJS](https://github.com/VILHALVA/CURSO-DE-NODEJS)
- [FAÇA O CURSO DE NODEJS COM MYSQL](https://github.com/VILHALVA/CURSO-DE-NODEJS-COM-MYSQL)
- [FAÇA O CURSO DE MYSQL](https://github.com/VILHALVA/CURSO-DE-MYSQL)
- [FAÇA O CURSO DE MYSQL COM PHP](https://github.com/VILHALVA/CURSO-DE-MYSQL-COM-PHP)
- [FAÇA O CURSO DE MARIADB](https://github.com/VILHALVA/CURSO-DE-MARIADB)
- [FAÇA O CURSO DE POSTGRESQL](https://github.com/VILHALVA/CURSO-DE-POSTGRESQL)
- [FAÇA O CURSO DE MONGODB](https://github.com/VILHALVA/CURSO-DE-MONGODB)
- [FAÇA O CURSO DE JSON](https://github.com/VILHALVA/CURSO-DE-JSON)

