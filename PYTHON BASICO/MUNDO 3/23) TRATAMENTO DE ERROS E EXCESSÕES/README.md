# TRATAMENTO DE ERROS E EXCESSÕES
O tratamento de erros e exceções é uma parte fundamental da programação em Python, pois ajuda a tornar seus programas mais robustos e resistentes a falhas inesperadas. Em Python, as exceções são eventos que ocorrem durante a execução do programa que podem interromper o fluxo normal de execução. Vamos explorar como tratar erros e exceções em Python.

**Blocos Try e Except:**

Em Python, você pode usar blocos `try` e `except` para lidar com exceções. O código que pode levantar uma exceção é colocado dentro do bloco `try`, e o código que lida com a exceção é colocado dentro do bloco `except`. Aqui está um exemplo:

```python
try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
    print(f"O resultado é {resultado}")
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")
except ValueError:
    print("Erro: Você não digitou um número válido.")
```

Neste exemplo, o programa tenta converter a entrada do usuário em um número inteiro e depois divide 10 por esse número. Se o usuário inserir "0", uma exceção `ZeroDivisionError` será levantada, e o programa tratará esse erro exibindo uma mensagem apropriada. Se o usuário inserir algo que não pode ser convertido em um número, uma exceção `ValueError` será tratada.

**Cláusula `else` no Bloco `try` e `finally`:**

Você também pode usar a cláusula `else` no bloco `try` para executar código que deve ser executado somente se nenhum erro ocorrer. Além disso, a cláusula `finally` permite que você execute código que deve ser executado independentemente de ocorrer uma exceção ou não.

```python
try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")
except ValueError:
    print("Erro: Você não digitou um número válido.")
else:
    print(f"O resultado é {resultado}")
finally:
    print("Fim do programa")
```

**Levantando Exceções:**

Você também pode levantar exceções manualmente usando a palavra-chave `raise`. Isso pode ser útil quando você deseja criar exceções personalizadas em seu código.

```python
def dividir(a, b):
    if b == 0:
        raise ValueError("Divisão por zero não é permitida")
    return a / b

try:
    resultado = dividir(10, 0)
except ValueError as erro:
    print(f"Erro: {erro}")
```

Neste exemplo, a função `dividir` levanta uma exceção `ValueError` se o segundo argumento for zero. O programa trata essa exceção no bloco `try`/`except`.

**Exceções Genéricas:**

Você também pode capturar exceções genéricas usando a classe base `Exception`. No entanto, é geralmente recomendável capturar exceções específicas sempre que possível, pois isso torna o código mais claro e seguro.

```python
try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
except Exception as erro:
    print(f"Erro: {erro}")
```

**Personalizando Exceções:**

Você pode criar suas próprias exceções personalizadas definindo classes que herdam da classe base `Exception`.

```python
class MeuErro(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)

try:
    raise MeuErro("Isso é um erro personalizado")
except MeuErro as erro:
    print(f"Erro: {erro}")
```

O tratamento de erros e exceções em Python é uma habilidade importante para lidar com situações inesperadas e tornar seus programas mais robustos. É importante considerar cuidadosamente quais exceções podem ocorrer em seu código e como você deseja tratá-las para criar um código mais confiável e resiliente.