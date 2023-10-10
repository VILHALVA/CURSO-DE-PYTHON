# MANIPULANDO TEXTO 
Manipular texto é uma tarefa comum em programação, e Python oferece várias maneiras de fazer isso. Neste artigo, exploraremos algumas das operações mais comuns para manipulação de texto em Python.

## 1. Concatenação de Strings
Você pode combinar duas ou mais strings usando o operador `+` ou simplesmente juntando-as:

```python
nome = "João"
sobrenome = "Silva"
nome_completo = nome + " " + sobrenome
print(nome_completo)  # Isso imprimirá "João Silva"
```

## 2. Indexação e Fatiamento de Strings
Você pode acessar caracteres individuais em uma string usando índices. A indexação começa em 0 para o primeiro caractere.

```python
texto = "Python"
primeira_letra = texto[0]  # 'P'
segunda_letra = texto[1]   # 'y'
```

Você também pode fazer fatiamento (slicing) para extrair partes específicas de uma string:

```python
frase = "Python é uma linguagem de programação poderosa"
parte = frase[7:19]  # "é uma lingua"
```

## 3. Comprimento de uma String
Para obter o comprimento de uma string, você pode usar a função `len()`:

```python
frase = "Manipulando texto em Python"
comprimento = len(frase)
print(comprimento)  # Isso imprimirá "27"
```

## 4. Métodos de Strings
Python fornece vários métodos embutidos para manipular strings:

- `upper()`: Converte uma string em maiúsculas.
- `lower()`: Converte uma string em minúsculas.
- `strip()`: Remove espaços em branco no início e no final de uma string.
- `replace()`: Substitui uma substring por outra.
- `split()`: Divide uma string em uma lista de substrings com base em um delimitador.
- `join()`: Une uma lista de strings em uma única string.

Exemplo:

```python
texto = "Manipulação de Texto em Python"
maiusculas = texto.upper()
minusculas = texto.lower()
sem_espacos = texto.strip()
substituido = texto.replace("Python", "Java")
palavras = texto.split()  # Divide a frase em palavras
frase_nova = " ".join(palavras)  # Junta as palavras em uma nova frase
```

## 5. Formatação de Strings
Você pode formatar strings usando f-strings (Python 3.6 e posterior) ou o método `format()`:

```python
nome = "Maria"
idade = 30
mensagem = f"Olá, meu nome é {nome} e eu tenho {idade} anos."
```

Ou usando `format()`:

```python
nome = "Maria"
idade = 30
mensagem = "Olá, meu nome é {} e eu tenho {} anos.".format(nome, idade)
```

## 6. Verificação de Substrings
Você pode verificar se uma substring está presente em uma string usando o operador `in`:

```python
frase = "Python é uma linguagem de programação"
if "Python" in frase:
    print("A palavra 'Python' está na frase.")
```

Estas são apenas algumas das operações básicas para manipulação de texto em Python. Dependendo das suas necessidades, você pode explorar mais métodos e técnicas para trabalhar com strings. Python oferece uma grande flexibilidade para manipular texto de diversas maneiras.