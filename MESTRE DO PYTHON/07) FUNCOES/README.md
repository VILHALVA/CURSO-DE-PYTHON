# FUNCÕES
Em Python, funções são blocos de código reutilizáveis que realizam uma tarefa específica. Elas ajudam a organizar o código, torná-lo mais legível e facilitar a reutilização de código. Aqui está uma explicação detalhada sobre funções em Python:

**Definição de Funções:**

Para definir uma função em Python, você usa a palavra-chave `def`, seguida pelo nome da função e, opcionalmente, parâmetros entre parênteses. O bloco de código da função é indentado após a declaração da função. Aqui está um exemplo de uma função simples que retorna a soma de dois números:

```python
def soma(a, b):
    resultado = a + b
    return resultado
```

Neste exemplo, `soma` é o nome da função e `a` e `b` são os parâmetros. A função retorna a soma de `a` e `b`.

**Chamando Funções:**

Depois de definir uma função, você pode chamá-la em qualquer lugar do seu programa fornecendo os valores dos argumentos, se houver. Aqui está como você chama a função `soma` definida acima:

```python
resultado = soma(3, 5)
print(resultado)  # Saída: 8
```

Neste exemplo, `3` e `5` são passados como argumentos para os parâmetros `a` e `b`, respectivamente.

**Parâmetros Padrão:**

Você pode fornecer valores padrão para os parâmetros de uma função. Isso permite que a função seja chamada com menos argumentos do que o número total de parâmetros. Aqui está um exemplo:

```python
def saudacao(nome, saudacao='Olá'):
    print(f'{saudacao}, {nome}!')

saudacao('Maria')  # Saída: Olá, Maria!
saudacao('João', 'Oi')  # Saída: Oi, João!
```

Neste exemplo, se nenhum valor for fornecido para o parâmetro `saudacao`, ele assumirá o valor padrão `'Olá'`.

**Retorno de Valores:**

Uma função pode retornar um valor usando a palavra-chave `return`. Você pode retornar múltiplos valores separados por vírgula. Aqui está um exemplo:

```python
def dividir(a, b):
    if b == 0:
        return 'Erro: divisão por zero'
    else:
        return a / b

resultado = dividir(10, 2)
print(resultado)  # Saída: 5.0
```

Neste exemplo, se `b` for zero, a função retorna uma mensagem de erro. Caso contrário, ela retorna o resultado da divisão de `a` por `b`.

**Escopo de Variáveis:**

Variáveis definidas dentro de uma função têm escopo local, o que significa que elas só podem ser acessadas dentro da própria função. Variáveis definidas fora de qualquer função têm escopo global, o que significa que elas podem ser acessadas em qualquer lugar do programa.

**Recursão:**

Python suporta recursão, o que significa que uma função pode chamar a si mesma. Aqui está um exemplo de uma função recursiva para calcular o fatorial de um número:

```python
def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

resultado = fatorial(5)
print(resultado)  # Saída: 120
```

Neste exemplo, a função `fatorial` chama a si mesma para calcular o fatorial de `n - 1` até que `n` seja igual a zero.

As funções são uma parte fundamental da programação em Python e são amplamente utilizadas para dividir o código em partes reutilizáveis e modularizadas. Elas permitem uma melhor organização do código, facilitando a manutenção e o desenvolvimento de programas mais complexos.