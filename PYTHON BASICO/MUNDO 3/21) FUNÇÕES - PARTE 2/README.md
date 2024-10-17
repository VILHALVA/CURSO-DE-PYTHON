# FUNÇOES PARTE 2
Vamos continuar explorando as funções em Python, abordando os seguintes tópicos: docstrings, parâmetros opcionais, escopo de variáveis e retorno de valores.

**1. Docstrings:**

As docstrings são strings de documentação que descrevem o propósito e o funcionamento de uma função. Elas são colocadas como um comentário no início da função e são usadas para documentar o código. Você pode acessar a docstring de uma função usando o atributo `__doc__`. Aqui está um exemplo:

```python
def calcular_media(numeros):
    """
    Calcula a média dos números em uma lista.
    
    Argumentos:
    numeros (list): Uma lista de números.
    
    Retorna:
    float: A média dos números.
    """
    if len(numeros) == 0:
        return 0
    total = sum(numeros)
    return total / len(numeros)

# Acessar a docstring da função
print(calcular_media.__doc__)
```

**2. Parâmetros Opcionais:**

Você pode definir parâmetros opcionais em uma função, atribuindo um valor padrão aos parâmetros. Isso permite que você chame a função sem fornecer valores para os parâmetros opcionais, usando os valores padrão em vez disso. Aqui está um exemplo:

```python
def saudacao(nome, saudacao="Olá"):
    return f"{saudacao}, {nome}!"

# Chamar a função com um valor padrão
mensagem = saudacao("Alice")
print(mensagem)  # Resultado: "Olá, Alice!"

# Chamar a função com um valor personalizado
mensagem = saudacao("Bob", "Oi")
print(mensagem)  # Resultado: "Oi, Bob!"
```

**3. Escopo de Variáveis:**

Variáveis definidas dentro de uma função têm escopo local, o que significa que elas só podem ser acessadas dentro da função. Variáveis definidas fora de uma função têm escopo global, o que significa que elas podem ser acessadas em qualquer lugar do programa. Aqui está um exemplo:

```python
x = 10  # Variável global

def funcao():
    y = 20  # Variável local
    print(x)  # Acesso à variável global
    print(y)  # Acesso à variável local

funcao()
print(x)  # Acesso à variável global fora da função
# print(y)  # Isso resultará em um erro, pois y é uma variável local
```

**4. Retorno de Valores:**

Funções podem retornar valores usando a palavra-chave `return`. Você pode retornar um único valor ou uma tupla de valores. Aqui estão exemplos:

```python
def somar(a, b):
    return a + b

resultado = somar(5, 3)
print(resultado)  # Resultado: 8

def dividir_e_resto(dividendo, divisor):
    quociente = dividendo // divisor
    resto = dividendo % divisor
    return quociente, resto

q, r = dividir_e_resto(10, 3)
print(f"Quociente: {q}, Resto: {r}")  # Resultado: "Quociente: 3, Resto: 1"
```

Esses são conceitos fundamentais relacionados a funções em Python. Docstrings ajudam a documentar suas funções, parâmetros opcionais aumentam a flexibilidade, o escopo de variáveis controla a visibilidade das variáveis e o retorno de valores permite que as funções produzam resultados úteis.