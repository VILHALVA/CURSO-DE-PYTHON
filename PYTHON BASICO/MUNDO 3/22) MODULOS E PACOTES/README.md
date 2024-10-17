# MODULOS E PACOTES
Módulos e pacotes são recursos essenciais em Python que ajudam a organizar e reutilizar código. Eles permitem dividir seu programa em partes menores e mais gerenciáveis e facilitam a colaboração em projetos maiores. Vamos explorar os conceitos de módulos e pacotes em Python.

**Módulos:**

- Um módulo é um arquivo Python que contém definições de funções, classes e variáveis.
- Ele permite que você reutilize código escrevendo funções e classes em um arquivo separado e, em seguida, importando esse arquivo em seu programa principal.
- Para criar um módulo, você pode criar um arquivo Python com a extensão ".py" e escrever código nele. Por exemplo, você pode criar um arquivo chamado "meu_modulo.py" com funções úteis.

```python
# Conteúdo de meu_modulo.py

def saudacao(nome):
    return f"Olá, {nome}!"

def calcular_media(numeros):
    if len(numeros) == 0:
        return 0
    total = sum(numeros)
    return total / len(numeros)
```

- Para usar um módulo em seu programa principal, você pode importá-lo usando a palavra-chave `import`.

```python
import meu_modulo

mensagem = meu_modulo.saudacao("Alice")
print(mensagem)  # Resultado: "Olá, Alice!"
```

**Pacotes:**

- Um pacote é uma coleção de módulos relacionados organizados em diretórios.
- Ele permite que você estruture seu código em hierarquias para melhor organização.
- Para criar um pacote, você precisa criar um diretório com um arquivo especial chamado `__init__.py`. O diretório deve conter os módulos relacionados.
- Por exemplo, você pode criar um pacote chamado "meu_pacote" com um módulo chamado "modulo1" e outro chamado "modulo2".

```
meu_pacote/
    __init__.py
    modulo1.py
    modulo2.py
```

- Para importar módulos de um pacote, você usa a notação de ponto.

```python
from meu_pacote import modulo1

mensagem = modulo1.saudacao("Bob")
print(mensagem)  # Resultado: "Olá, Bob!"
```

**Importações Relativas:**

- Para importar módulos dentro do mesmo pacote, você pode usar importações relativas.

```python
from . import modulo2

mensagem = modulo2.saudacao("Charlie")
print(mensagem)  # Resultado: "Olá, Charlie!"
```

**Resumo:**

- Módulos são arquivos Python que contêm código reutilizável.
- Pacotes são diretórios que contêm módulos relacionados.
- Você pode importar módulos usando a palavra-chave `import`.
- Importações relativas permitem importar módulos dentro do mesmo pacote.
- Módulos e pacotes ajudam na organização e reutilização de código em Python. Eles são essenciais para projetos maiores e mais complexos.