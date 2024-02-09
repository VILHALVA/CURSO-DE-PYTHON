# CONDICIONAIS PARTE 1
As condicionais `if`, `elif` (abreviação de "else if") e `else` são estruturas fundamentais na programação que permitem que você tome decisões em seu código com base em condições específicas. Elas permitem que você controle o fluxo do programa, executando diferentes blocos de código dependendo de determinadas circunstâncias. Vamos explorar como essas condicionais funcionam em Python.

## A Estrutura Básica
A estrutura básica de uma condicional em Python é a seguinte:

```python
if condicao:
    # Código a ser executado se a condição for verdadeira
else:
    # Código a ser executado se a condição for falsa
```

- `if`: É a palavra-chave inicial da condicional e testa uma determinada condição.
- `condicao`: É a expressão booleana que é avaliada como verdadeira (`True`) ou falsa (`False`).
- `:` (dois pontos): Indica o início de um bloco de código.
- `else`: É uma parte opcional da condicional e é executada se a condição do `if` for falsa.
- `:` (dois pontos): Indica o início do bloco de código associado ao `else`.

## Exemplo de Uso
Aqui está um exemplo simples que verifica se um número é maior ou menor que 10 e exibe uma mensagem de acordo com o resultado:

```python
numero = 15

if numero > 10:
    print("O número é maior que 10.")
else:
    print("O número é menor ou igual a 10.")
```

Neste caso, como `numero` é igual a 15, a condição do `if` é verdadeira, então a primeira mensagem é impressa.

## Condicionais `elif`
Às vezes, você precisa testar várias condições diferentes. Para fazer isso, você pode usar a condicional `elif`. Aqui está a estrutura básica:

```python
if condicao1:
    # Código a ser executado se a condicao1 for verdadeira
elif condicao2:
    # Código a ser executado se a condicao1 for falsa e condicao2 for verdadeira
else:
    # Código a ser executado se todas as condições anteriores forem falsas
```

Você pode usar quantos blocos `elif` quiser para testar condições adicionais.

Exemplo:

```python
nota = 75

if nota >= 90:
    print("A nota é A")
elif nota >= 80:
    print("A nota é B")
elif nota >= 70:
    print("A nota é C")
else:
    print("A nota é D")
```

Neste exemplo, o programa verifica a nota e imprime a letra correspondente com base na faixa de notas.

## Conclusão
As condicionais `if`, `elif` e `else` são ferramentas fundamentais na programação Python para tomada de decisões. Elas permitem que você crie fluxos de controle condicionais e execute diferentes blocos de código com base em condições específicas. Dominar o uso de condicionais é essencial para escrever programas mais complexos e funcionais em Python.