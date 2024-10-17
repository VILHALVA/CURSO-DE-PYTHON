# ENTRADA DE DADOS 
## INPUT
Em Python, a função `input()` é usada para receber entrada de dados do usuário via teclado. Aqui está como você pode usá-la:

```python
# Solicita ao usuário que insira um valor e armazena na variável 'nome'
nome = input("Digite seu nome: ")

# Imprime a mensagem de boas-vindas usando o valor fornecido pelo usuário
print("Olá,", nome, "! Bem-vindo!")
```

Neste exemplo:

- `input("Digite seu nome: ")` solicita ao usuário que insira um valor e exibe a mensagem "Digite seu nome: " como prompt.
- O valor inserido pelo usuário é armazenado na variável `nome`.
- Em seguida, a função `print()` exibe uma mensagem de boas-vindas usando o valor fornecido pelo usuário.

É importante notar que a função `input()` sempre retorna uma string, independentemente do tipo de entrada fornecido pelo usuário. Se você deseja receber um tipo diferente de entrada (como um número inteiro ou um número de ponto flutuante), você precisa converter explicitamente o valor retornado pela função `input()` para o tipo desejado usando as funções `int()` ou `float()`. Por exemplo:

```python
# Solicita ao usuário que insira um número inteiro e o converte para int
idade = int(input("Digite sua idade: "))

# Imprime a idade fornecida pelo usuário
print("Sua idade é:", idade)
```

Neste caso, `int(input("Digite sua idade: "))` solicita ao usuário que insira um número inteiro e converte o valor retornado pela função `input()` para um número inteiro usando a função `int()`. O mesmo conceito se aplica se você estiver esperando um número de ponto flutuante, substituindo `int()` por `float()`.

## TRATAMENTO DE ERROS E EXCEÇÕES:
Em Python, o tratamento de erros e exceções é feito usando blocos `try`, `except`, `else` e `finally`. Aqui está uma explicação básica de como esses blocos funcionam:

1. **Bloco try-except:**
   - O código que pode potencialmente gerar um erro é colocado dentro do bloco `try`.
   - Se nenhum erro ocorrer, o bloco `except` é ignorado e o programa continua sua execução normalmente.
   - Se ocorrer um erro durante a execução do bloco `try`, o Python procura por um bloco `except` correspondente. Se encontrar, o código dentro do bloco `except` é executado.

```python
try:
    # Código que pode gerar um erro
    x = int(input("Digite um número: "))
    resultado = 10 / x
    print("O resultado é:", resultado)
except ZeroDivisionError:
    # Código executado se uma divisão por zero ocorrer
    print("Erro: Divisão por zero!")
except ValueError:
    # Código executado se a conversão para int não for bem-sucedida
    print("Erro: Entrada inválida! Você deve digitar um número inteiro.")
```

2. **Bloco else:**
   - O bloco `else` é executado se nenhum erro ocorrer dentro do bloco `try`.
   - É útil para colocar código que deve ser executado apenas se nenhuma exceção for lançada.

```python
try:
    x = int(input("Digite um número: "))
    resultado = 10 / x
except ZeroDivisionError:
    print("Erro: Divisão por zero!")
except ValueError:
    print("Erro: Entrada inválida! Você deve digitar um número inteiro.")
else:
    print("Nenhuma exceção ocorreu!")
```

3. **Bloco finally:**
   - O bloco `finally` é opcional e é executado sempre, independentemente de ocorrer uma exceção ou não.
   - É útil para colocar código que deve ser executado independentemente de qualquer exceção.

```python
try:
    x = int(input("Digite um número: "))
    resultado = 10 / x
except ZeroDivisionError:
    print("Erro: Divisão por zero!")
except ValueError:
    print("Erro: Entrada inválida! Você deve digitar um número inteiro.")
else:
    print("Nenhuma exceção ocorreu!")
finally:
    print("Este bloco sempre será executado, ocorrendo uma exceção ou não.")
```

O tratamento de erros e exceções em Python permite que você crie código mais robusto e tolerante a falhas, lidando com situações imprevistas de forma elegante e controlada.

Aqui está uma tabela que resume os principais tipos de exceções que podem ser tratadas no bloco `except`:

| Tipo de Exceção           | Descrição                                                    |
|---------------------------|--------------------------------------------------------------|
| `Exception`               | Captura qualquer exceção que não tenha uma classe específica. |
| `TypeError`               | Erro de tipo: ocorre quando uma operação é executada em um tipo inadequado. |
| `ValueError`              | Erro de valor: ocorre quando uma função recebe um argumento com o tipo correto, mas um valor inadequado. |
| `ZeroDivisionError`       | Erro de divisão por zero: ocorre quando uma divisão ou módulo é executado com divisor igual a zero. |
| `IndexError`              | Erro de índice: ocorre quando um índice está fora do intervalo válido para uma sequência ou contêiner. |
| `KeyError`                | Erro de chave: ocorre quando uma chave não existe em um dicionário. |
| `FileNotFoundError`       | Erro de arquivo não encontrado: ocorre quando um arquivo que deve ser aberto não é encontrado no sistema. |
| `IOError`                 | Erro de E/S (entrada/saída): ocorre quando ocorre um problema durante operações de E/S, como a abertura ou leitura de um arquivo. |
| `NameError`               | Erro de nome: ocorre quando um identificador não está definido ou não foi encontrado no escopo atual. |
| `SyntaxError`             | Erro de sintaxe: ocorre quando o interpretador encontra um código que não segue a sintaxe correta de Python. |
| `IndentationError`        | Erro de indentação: ocorre quando a indentação do código não está correta, como em blocos `if`, `else`, `for`, etc. |
| `KeyboardInterrupt`       | Exceção gerada quando o usuário pressiona Ctrl+C para interromper a execução de um programa. |
| `MemoryError`             | Erro de memória: ocorre quando o Python não consegue alocar memória suficiente para a execução de um programa. |
| `OverflowError`           | Erro de estouro: ocorre quando um cálculo resulta em um valor que é muito grande para ser representado. |
| `ImportError`             | Erro de importação: ocorre quando um módulo não pode ser importado corretamente. |
| `ModuleNotFoundError`     | Erro de módulo não encontrado: ocorre quando um módulo especificado em uma instrução de importação não pode ser encontrado. |

Esses são apenas alguns exemplos de tipos de exceções comuns em Python. Existem muitos outros tipos de exceções que podem ser capturados e tratados de acordo com as necessidades específicas do seu programa.