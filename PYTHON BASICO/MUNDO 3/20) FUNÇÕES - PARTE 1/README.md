# FUNÇOES PARTE 1
Em programação, funções são blocos de código que podem ser reutilizados para realizar uma tarefa específica. Vamos comparar um programa sem função com um programa que utiliza funções:

**Programa Sem Função:**

```python
# Programa sem função para calcular a média de três números

# Solicitar ao usuário para inserir três números
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

# Calcular a média
media = (numero1 + numero2 + numero3) / 3

# Exibir o resultado
print(f"A média dos números é: {media}")
```

**Programa Com Função:**

```python
# Programa com função para calcular a média de três números

# Função para calcular a média
def calcular_media(numero1, numero2, numero3):
    return (numero1 + numero2 + numero3) / 3

# Solicitar ao usuário para inserir três números
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

# Chamar a função para calcular a média
media = calcular_media(numero1, numero2, numero3)

# Exibir o resultado
print(f"A média dos números é: {media}")
```

**Empacotamento de Parâmetros:**

Empacotamento de parâmetros, também conhecido como empacotamento de argumentos, permite que você passe um número variável de argumentos para uma função. Em Python, você pode usar o operador `*` para empacotar parâmetros em uma tupla. Aqui está um exemplo:

```python
# Função que recebe um número variável de argumentos
def somar_numeros(*args):
    total = 0
    for numero in args:
        total += numero
    return total

# Chamar a função com diferentes números de argumentos
resultado1 = somar_numeros(1, 2, 3)
resultado2 = somar_numeros(10, 20, 30, 40, 50)

print(resultado1)  # Resultado: 6
print(resultado2)  # Resultado: 150
```

**Usando Funções com Listas:**

Funções também podem ser usadas com listas para realizar operações em elementos da lista. Aqui está um exemplo de uma função que calcula a média de uma lista de números:

```python
# Função para calcular a média de uma lista de números
def calcular_media(lista):
    if len(lista) == 0:
        return 0
    total = sum(lista)
    return total / len(lista)

# Exemplo de uso da função
numeros = [10, 20, 30, 40, 50]
media = calcular_media(numeros)
print(f"A média dos números é: {media}")
```

**Empacotamento e Desempacotamento de Parâmetros:**

Você pode empacotar parâmetros em uma lista ou tupla e desempacotá-los em uma função usando o operador `*` para empacotar e desempacotar. Aqui está um exemplo:

```python
# Função que recebe três argumentos
def mostrar_nomes(nome1, nome2, nome3):
    print(f"Nomes: {nome1}, {nome2}, {nome3}")

# Empacotar parâmetros em uma lista
nomes = ["Alice", "Bob", "Charlie"]

# Desempacotar parâmetros e chamar a função
mostrar_nomes(*nomes)
```

Neste exemplo, os nomes são empacotados em uma lista e, em seguida, desempacotados na função `mostrar_nomes`. Isso permite que você passe uma lista de nomes como argumentos separados para a função.