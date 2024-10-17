# VETORES (VARIAVEIS COMPOSTAS)
## CONCEITOS:
Em Python, assim como em muitas linguagens de programação, listas são estruturas de dados que permitem armazenar uma coleção de elementos do mesmo tipo em uma única variável. As listas são uma parte fundamental da programação, pois permitem manipular conjuntos de dados de forma eficiente. Aqui estão os conceitos-chave sobre listas em Python:

**Declaração de Listas:**

Para declarar uma lista em Python, você simplesmente precisa especificar os elementos entre colchetes `[]`. Você também pode inicializar a lista com elementos ou deixá-la vazia para adicionar elementos posteriormente. Aqui está um exemplo de declaração de lista:

```python
numeros = [10, 20, 30, 40, 50]  # Lista inicializada com elementos
nomes = []  # Lista vazia
```

**Acesso a Elementos de Listas:**

Para acessar os elementos de uma lista em Python, você usa o nome da lista seguido de um índice entre colchetes. O índice indica a posição do elemento na lista. Lembre-se de que os índices em Python começam em 0. Aqui está um exemplo:

```python
numeros[0] = 42  # Define o primeiro elemento da lista como 42
x = numeros[4]  # Atribui o quinto elemento da lista à variável x
```

**Tamanho de Listas:**

Você pode determinar o tamanho de uma lista em Python usando a função `len(lista)`. Isso retorna o número de elementos na lista. Por exemplo:

```python
len(numeros)  # Retorna 5
```

**Inicialização de Listas:**

Você pode inicializar uma lista ao declará-la ou em um momento posterior. Para inicializar uma lista ao declará-la, você pode atribuir os valores diretamente. Por exemplo:

```python
numeros = [10, 20, 30, 40, 50]  # Lista inicializada com elementos
```

Para inicializar uma lista em um momento posterior, você pode usar o método `append()` para adicionar elementos individualmente ou usar list comprehension para criar listas com base em alguma lógica.

**Operações com Listas:**

Você pode realizar várias operações com listas, como inserir, remover, ordenar, pesquisar e muito mais. Para realizar essas operações, você pode usar métodos integrados em Python ou loops e condicionais.

**Exemplo de Loop com Listas:**

Aqui está um exemplo de como usar um loop "for" para percorrer e imprimir os elementos de uma lista:

```python
for num in numeros:
    print(num, end=' ')
```

Neste exemplo, o loop percorre cada elemento da lista `numeros` e imprime seu valor.

Listas são uma ferramenta poderosa para lidar com coleções de dados em programação e são amplamente utilizadas para armazenar listas de informações, como números, nomes, resultados de pesquisas e muito mais. Elas permitem que você trabalhe com dados de forma organizada e eficiente em seus programas.

## EXERCICIOS:
* **01) VALOR NA LISTA:**
```python
valor = []
for c in range(1, 5):
    num = int(input(f"😎Digite [{c}/4] valor: "))
    valor.append(num)
print(valor)
```

* **02) PARES E IMPARES:**
```python
valor = [[], []]
total_par = total_impar = 0
cont = 1

while True:
    num = int(input(f"😎Digite o {cont}ª valor: "))
    cont += 1
    if num % 2 == 0:
        valor[0].append(num)
        total_par += 1
    elif num % 2 == 1:
        valor[1].append(num)
        total_impar += 1
    res = input("😎Deseja continuar [S/N]?: ").strip().upper()[0]
    if res == 'N':
        break

valor[0].sort()
valor[1].sort()

print(f"⭐Analisando {cont} valores:")
print(f"⭐Temos {total_par} pares e {total_impar} ímpares.")
print(f"⭐Os pares são: {valor[0]}")
print(f"⭐Os ímpares são: {valor[1]}")
```

* **03) MEDIA COM ALUNOS:**
```python
ficha = []
total = 1

while True:
    nome = input(f"😎Digite o nome do {total}ª aluno:\n>>>").strip()
    nota1 = float(input("😎Digite 1ª nota:\n>>>"))
    nota2 = float(input("😎Digite 2ª nota:\n>>>"))
    total += 1
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = input("😎Você quer continuar [S/N]?\n>>>").strip().upper()[0]
    if resp == 'N':
        break

print("_" * 35)
print(f"{'Nª':<4}{'NOME':<10}{'MÉDIA':>8}")
print("-" * 30)
for i, aluno in enumerate(ficha):
    print(f"{i:<4}{aluno[0]:<10}{aluno[2]:8.1f}")
    print("-" * 30)
print("_" * 35)

while True:
    opc = int(input("😎Você quer mostrar as notas de quem?\n⚡Envie 999 para interromper:\n>>>"))
    if opc == 999:
        print("\n⛔FIM")
        break
    if opc <= len(ficha) - 1:
        print(f"⭐Notas de {ficha[opc][0]} são {ficha[opc][1]}")

print("<<< 😬ATÉ NUNCA MAIS!!! >>>")
```