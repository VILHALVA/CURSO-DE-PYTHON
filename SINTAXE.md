# SINTAXE DA LINGUAGEM:
## 0) FUNDAMENTOS:
Aqui está um exemplo de código em Python que utiliza os operadores aritméticos, relacionais e lógicos com diferentes tipos primitivos:
```python
# Operadores aritméticos
numero1 = 10
numero2 = 5

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2
resto = numero1 % numero2

# Operadores relacionais
valor1 = 10
valor2 = 5

igual = valor1 == valor2
diferente = valor1 != valor2
maior = valor1 > valor2
menor = valor1 < valor2
maior_ou_igual = valor1 >= valor2
menor_ou_igual = valor1 <= valor2

# Operadores lógicos
condicao1 = True
condicao2 = False

e = condicao1 and condicao2
ou = condicao1 or condicao2
nao = not condicao1

# Exibição dos resultados
print("Operadores aritméticos:")
print("Soma:", soma)
print("Subtração:", subtracao)
print("Multiplicação:", multiplicacao)
print("Divisão:", divisao)
print("Resto:", resto)

print("\nOperadores relacionais:")
print("Igual:", igual)
print("Diferente:", diferente)
print("Maior:", maior)
print("Menor:", menor)
print("Maior ou igual:", maior_ou_igual)
print("Menor ou igual:", menor_ou_igual)

print("\nOperadores lógicos:")
print("E:", e)
print("OU:", ou)
print("NÃO:", nao)
```
Neste exemplo, utilizamos variáveis com diferentes tipos primitivos, como inteiros (números) e booleanos (valores lógicos). Os operadores aritméticos (+, -, *, /, %) são usados para realizar cálculos matemáticos, enquanto os operadores relacionais (==, !=, >, <, >=, <=) são utilizados para comparar valores. Já os operadores lógicos (and, or, not) são utilizados para combinar condições lógicas.

Ao executar o código, os resultados dos cálculos e das comparações serão exibidos na saída. Os operadores relacionais retornam valores booleanos (True ou False) dependendo da condição avaliada, enquanto os operadores aritméticos retornam o resultado do cálculo. Os operadores lógicos também retornam valores booleanos com base nas condições combinadas.

Esses operadores são essenciais para realizar operações e tomar decisões em programação, permitindo que você manipule variáveis, compare valores e controle o fluxo do seu código.

## 1) VARIAVEIS SIMPLES:
Veja um exemplo de variável simples:
```python
nome = "Maria"
idade = 25
altura = 1.65
is_aluno = True
```
Neste exemplo, temos quatro variáveis simples declaradas: `nome`, `idade`, `altura` e `is_aluno`. Vamos explicar cada uma delas:

- A variável `nome` armazena uma cadeia de caracteres (string) com o valor "Maria". É utilizada para armazenar um nome.

- A variável `idade` é do tipo inteiro (int) e possui o valor 25. É utilizada para armazenar a idade de uma pessoa.

- A variável `altura` é do tipo float e possui o valor 1.65. É utilizada para armazenar a altura de uma pessoa.

- A variável `is_aluno` é do tipo booleano (bool) e possui o valor True. É utilizada para armazenar um valor lógico que indica se a pessoa é um aluno (no caso, True) ou não (False).

Em Python, não é necessário especificar explicitamente o tipo das variáveis, pois a linguagem é de tipagem dinâmica, ou seja, o tipo da variável é inferido automaticamente com base no valor atribuído a ela. Isso permite uma maior flexibilidade ao trabalhar com variáveis.

As variáveis em Python podem ser atualizadas com novos valores ao longo do programa. Por exemplo, podemos alterar o valor da variável `idade` para 30 da seguinte forma:
```python
idade = 30
```

O uso da função `input()` é muito comum em Python para obter dados inseridos pelo usuário durante a execução do programa. Veja um exemplo de como usar o `input()` em Python:

```python
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

print("Seu nome é", nome)
print("Sua idade é", idade)
```

Nesse exemplo, o programa solicita que o usuário insira seu nome e sua idade. A função `input()` é usada para receber as entradas do usuário, e o texto fornecido entre parênteses é exibido como uma mensagem para orientar o usuário sobre o que deve ser inserido.

Após o usuário inserir os valores desejados e pressionar Enter, as entradas são armazenadas nas variáveis `nome` e `idade`. Em seguida, as informações são exibidas na tela usando a função `print()`.

É importante destacar que o `input()` sempre retorna uma string, independentemente do tipo de dado que o usuário tenha inserido. Se você precisar realizar operações numéricas com os valores inseridos pelo usuário, será necessário converter o tipo de dado usando as funções de conversão adequadas, como `int()` para inteiros ou `float()` para números de ponto flutuante.
```python
idade = input("Digite sua idade: ")
idade = int(idade)  # converte a string para inteiro

# Agora é possível realizar operações numéricas com a variável idade
```
O uso do `input()` permite que o programa interaja com o usuário, possibilitando a entrada de dados personalizados e tornando os programas mais dinâmicos e interativos.

As variáveis são fundamentais na programação, pois permitem armazenar e manipular dados durante a execução de um programa. Elas fornecem uma forma de referenciar e reutilizar valores, facilitando a organização e o processamento de informações.

## 2) ESTRUTURA CONDICIONAL:
### ESTRUTURA IF-ELSE:
Aqui está um exemplo de uma estrutura condicional `if-else` em Python:
```python
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
```
Nesse exemplo, o programa solicita que o usuário digite sua idade utilizando a função `input()`. Em seguida, a função `int()` é usada para converter a entrada, que é uma string, em um valor numérico do tipo inteiro.

Depois disso, a estrutura condicional `if-else` avalia se a idade inserida é maior ou igual a 18. Se a condição for verdadeira, ou seja, se a idade for maior ou igual a 18, a mensagem "Você é maior de idade" será exibida na tela. Caso contrário, a mensagem "Você é menor de idade" será exibida.

A estrutura `if-else` é muito útil para executar diferentes blocos de código dependendo de uma condição específica. Ela permite que você controle o fluxo do programa com base em determinadas circunstâncias.

### ESTRUTURA SWITCH:
A partir do [Python 3.10](https://docs.python.org/3/whatsnew/3.10.html), foi introduzido o **Structural Pattern Matching**, que permite a utilização de uma estrutura semelhante ao `switch case`. O recurso utiliza a palavra-chave `match` e é bastante flexível, permitindo padrões simples ou complexos.

Aqui está um exemplo que simula uma funcionalidade semelhante ao `switch` para retornar mensagens baseadas no dia da semana:

```python
def saudacao(dia):
    match dia:
        case 1 | 7:
            return "FIM DE SEMANA. DOMINGO OU SÁBADO"
        case 2:
            return "SEGUNDA-FEIRA"
        case 3:
            return "TERÇA-FEIRA"
        case 4:
            return "QUARTA-FEIRA"
        case 5:
            return "QUINTA-FEIRA"
        case 6:
            return "SEXTA-FEIRA"
        case _:
            return "DIA INVÁLIDO!"

# Exemplo de uso
dia = 1
print(saudacao(dia))  # Saída: FIM DE SEMANA. DOMINGO OU SÁBADO
```

1. A palavra-chave **`match`** funciona como um ponto de decisão, onde o valor fornecido (`dia`) é comparado com os padrões especificados em cada **`case`**.
2. O operador **`|`** é usado para combinar múltiplos valores em um único padrão. No exemplo, `1 | 7` equivale a "domingo ou sábado".
3. O **`case _`** age como um **"default"**, capturando todos os valores que não correspondem aos padrões anteriores.

## 3) ESTRUTURA DE REPETIÇÃO:
### ESTRUTURA FOR:
A estrutura de repetição `for` em Python é usada para iterar sobre uma sequência de elementos, como uma lista, uma string ou um intervalo numérico. A sintaxe básica do `for` em Python é a seguinte:
```python
for elemento in sequencia:
    # Bloco de código a ser executado para cada elemento
```
O `elemento` é uma variável que assume o valor de cada elemento da `sequencia` a cada iteração do loop. O bloco de código dentro do `for` é executado para cada elemento da sequência.

Aqui está um exemplo de uso da estrutura `for` em Python:
```python
frutas = ["maçã", "banana", "laranja"]

for fruta in frutas:
    print(fruta)
```
Nesse exemplo, a lista `frutas` contém três elementos: "maçã", "banana" e "laranja". O loop `for` itera sobre cada elemento da lista e a variável `fruta` assume o valor de cada elemento a cada iteração. O bloco de código `print(fruta)` é executado para cada elemento, exibindo o nome de cada fruta.

A estrutura `for` em Python também pode ser usada com a função `range()` para criar um loop com um número específico de iterações. Por exemplo:
```python
for i in range(5):
    print(i)
```
Nesse caso, o loop `for` será executado 5 vezes, e a variável `i` assumirá os valores de 0 a 4 em cada iteração. O bloco de código `print(i)` exibirá os números de 0 a 4.

A estrutura `for` em Python é flexível e pode ser usada de várias maneiras para iterar sobre diferentes tipos de sequências. Ela é uma poderosa ferramenta para controlar a repetição de código com base em elementos de uma sequência.

### ESTRUTURA WHILE:
A estrutura de repetição `while` em Python é usada para executar um bloco de código repetidamente enquanto uma determinada condição for verdadeira. A sintaxe básica do `while` em Python é a seguinte:
```python
while condição:
    # Bloco de código a ser executado enquanto a condição for verdadeira
```
A `condição` é uma expressão booleana que é avaliada a cada iteração do loop. Enquanto a condição for verdadeira, o bloco de código dentro do `while` é executado. Se a condição se tornar falsa, o loop é encerrado e a execução continua após o bloco `while`.

Aqui está um exemplo de uso da estrutura `while` em Python:
```python
contador = 0

while contador < 5:
    print(contador)
    contador += 1
```
Nesse exemplo, o bloco `while` é executado enquanto o valor da variável `contador` for menor que 5. Dentro do loop, o valor atual do contador é exibido e o contador é incrementado em 1. O loop continuará a ser executado até que o contador atinja o valor 5.

É importante garantir que a condição do `while` seja eventualmente falsa para evitar loops infinitos. Se a condição nunca se tornar falsa, o loop continuará executando indefinidamente.

Além disso, é possível usar a palavra-chave `break` dentro do bloco `while` para interromper a execução do loop antecipadamente com base em uma determinada condição.

A estrutura `while` em Python oferece flexibilidade na execução de repetições com base em uma condição dinâmica. Ela é útil quando o número de iterações não é conhecido antecipadamente e depende da satisfação de uma condição específica.

### ESTRUTURA DO-WHILE:
Em Python, não há uma estrutura de repetição específica chamada `do-while` como em algumas outras linguagens de programação. No entanto, é possível obter um comportamento semelhante usando uma combinação de um loop `while` com uma verificação de condição no final.

Aqui está um exemplo de como implementar uma estrutura `do-while` em Python:
```python
while True:
    # Bloco de código a ser executado pelo menos uma vez

    # Condição de saída do loop
    if condição:
        break
```
Nesse exemplo, o loop `while True` é executado indefinidamente. O bloco de código dentro do loop é executado pelo menos uma vez, independentemente da condição. Em seguida, uma verificação de condição é feita usando um `if`. Se a condição for verdadeira, a instrução `break` é executada, interrompendo o loop e saindo dele.

Essa abordagem simula o comportamento do `do-while`, garantindo que o bloco de código seja executado pelo menos uma vez antes de verificar a condição de saída. No entanto, é importante garantir que haja uma condição de saída adequada para evitar loops infinitos.

Vale ressaltar que, em muitos casos, a estrutura `while` padrão é suficiente para atender às necessidades de repetição em Python, e o uso da estrutura `do-while` não é tão comum como em outras linguagens.

## 4) VARIAVEIS COMPOSTAS:
### TUPLAS:
Em Python, uma tupla é uma estrutura de dados semelhante a uma lista, mas com uma diferença fundamental: as tuplas são imutáveis, o que significa que seus elementos não podem ser alterados após a criação. As tuplas são representadas por parênteses () e podem conter diferentes tipos de elementos, como números, strings, booleanos e até mesmo outras tuplas.

Aqui está um exemplo de como criar e trabalhar com tuplas em Python:
```python
# Criando uma tupla
tupla = (1, 2, 3, "quatro", True)

# Acessando elementos da tupla
print(tupla[0])  # Saída: 1
print(tupla[3])  # Saída: "quatro"

# Iterando sobre os elementos da tupla
for elemento in tupla:
    print(elemento)

# Comprimento da tupla
print(len(tupla))  # Saída: 5

# Concatenando tuplas
outra_tupla = ("cinco", False)
tupla_concatenada = tupla + outra_tupla
print(tupla_concatenada)  # Saída: (1, 2, 3, "quatro", True, "cinco", False)
```
Observe que, uma vez criada, uma tupla não pode ser alterada. Isso significa que não é possível adicionar, remover ou modificar elementos individuais em uma tupla existente. Se você precisar realizar tais operações, pode ser necessário converter a tupla em uma lista, fazer as modificações desejadas e, em seguida, converter a lista de volta em uma tupla, se necessário.

As tuplas são úteis quando você precisa armazenar um conjunto de valores que não devem ser modificados, como coordenadas, informações de data e hora ou configurações de aplicativo. A imutabilidade das tuplas pode ajudar a garantir a integridade dos dados e evitar alterações acidentais.

### LISTAS:
Em Python, uma lista é uma estrutura de dados versátil e mutável que pode armazenar uma coleção ordenada de elementos. Diferente das tuplas, as listas podem ser modificadas, o que significa que é possível adicionar, remover e modificar elementos individuais.

As listas em Python são representadas por colchetes [] e podem conter elementos de diferentes tipos, como números, strings, booleanos e até mesmo outras listas. Aqui está um exemplo de como criar e trabalhar com listas em Python:
```python
# Criando uma lista
lista = [1, 2, 3, "quatro", True]

# Acessando elementos da lista
print(lista[0])  # Saída: 1
print(lista[3])  # Saída: "quatro"

# Modificando elementos da lista
lista[1] = "dois"
print(lista)  # Saída: [1, "dois", 3, "quatro", True]

# Adicionando elementos à lista
lista.append(5)
print(lista)  # Saída: [1, "dois", 3, "quatro", True, 5]

# Removendo elementos da lista
lista.remove("quatro")
print(lista)  # Saída: [1, "dois", 3, True, 5]

# Iterando sobre os elementos da lista
for elemento in lista:
    print(elemento)

# Comprimento da lista
print(len(lista))  # Saída: 5
```
Além das operações mencionadas acima, as listas em Python oferecem uma ampla variedade de métodos para manipulação, como inserção, extensão, ordenação, inversão, entre outros. Esses métodos permitem que você trabalhe de forma flexível e eficiente com os dados armazenados em listas.

As listas são uma estrutura de dados muito utilizada em Python, pois oferecem flexibilidade e facilidade de uso. Elas são amplamente empregadas para armazenar coleções de elementos, iterar sobre eles, realizar operações de busca e manipulação de dados.

### DICIONARIOS:
Em Python, um dicionário é uma estrutura de dados que permite armazenar pares de chave-valor, em que cada chave está associada a um valor específico. Diferentemente das listas, em que os elementos são acessados por meio de índices numéricos, nos dicionários, os valores são acessados por meio de suas chaves, que podem ser de qualquer tipo imutável, como strings, números ou tuplas.

Os dicionários em Python são representados por chaves {} e contêm uma série de pares chave-valor separados por vírgulas. Aqui está um exemplo de como criar e trabalhar com dicionários em Python:
```python
# Criando um dicionário
dicionario = {"nome": "João", "idade": 25, "cidade": "São Paulo"}

# Acessando valores pelos nomes das chaves
print(dicionario["nome"])   # Saída: "João"
print(dicionario["idade"])  # Saída: 25

# Modificando valores de um dicionário
dicionario["idade"] = 30
print(dicionario)  # Saída: {"nome": "João", "idade": 30, "cidade": "São Paulo"}

# Adicionando novos pares chave-valor ao dicionário
dicionario["profissão"] = "Engenheiro"
print(dicionario)  # Saída: {"nome": "João", "idade": 30, "cidade": "São Paulo", "profissão": "Engenheiro"}

# Removendo um par chave-valor do dicionário
del dicionario["cidade"]
print(dicionario)  # Saída: {"nome": "João", "idade": 30, "profissão": "Engenheiro"}

# Verificando se uma chave existe no dicionário
print("idade" in dicionario)   # Saída: True
print("endereço" in dicionario)  # Saída: False

# Iterando sobre os pares chave-valor do dicionário
for chave, valor in dicionario.items():
    print(chave + ": " + str(valor))

# Comprimento do dicionário
print(len(dicionario))  # Saída: 3
```
Os dicionários são extremamente úteis quando se precisa associar informações específicas a uma chave correspondente. Eles permitem um acesso rápido e eficiente aos valores por meio de suas chaves, o que é especialmente útil quando se precisa buscar, atualizar ou remover informações com base em identificadores únicos.

## 5) FUNÇÕES:
Veja um exemplo de função em Python com a importação de um módulo:
```python
# Importando um módulo
import math

# Definindo uma função
def calcular_area_circulo(raio):
    area = math.pi * raio ** 2
    return area

# Chamando a função e exibindo o resultado
raio = 5
area_circulo = calcular_area_circulo(raio)
print("A área do círculo de raio", raio, "é:", area_circulo)
```
Neste exemplo, importamos o módulo `math`, que fornece diversas funções matemáticas, incluindo a constante `pi`. Em seguida, definimos uma função chamada `calcular_area_circulo`, que recebe o raio de um círculo como argumento e retorna a área calculada usando a fórmula `pi * raio ** 2`. Finalmente, chamamos a função passando um valor de raio específico e exibimos o resultado.

Ao utilizar funções, podemos encapsular blocos de código que realizam uma determinada tarefa, tornando o código mais modular, reutilizável e fácil de entender. A importação de módulos permite que tenhamos acesso a recursos adicionais e funcionalidades prontas para uso em nossas funções.

## 6) CLASS POO:
Aqui está um exemplo de uma classe em Python que ilustra os quatro pilares da programação orientada a objetos: encapsulamento, herança, polimorfismo e abstração.
```python
# Exemplo de classe em Python
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def comer(self):
        pass

    def dormir(self):
        pass

# Classe derivada de Animal
class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def comer(self):
        print(f"{self.nome} está comendo ração.")

    def dormir(self):
        print(f"{self.nome} está dormindo.")

    def latir(self):
        print("Au au!")

# Classe derivada de Animal
class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def comer(self):
        print(f"{self.nome} está comendo ração.")

    def dormir(self):
        print(f"{self.nome} está dormindo.")

    def miar(self):
        print("Miau!")

# Exemplo de uso das classes
animal1 = Cachorro("Rex")
animal2 = Gato("Felix")

animal1.comer()
animal2.comer()

animal1.dormir()
animal2.dormir()

animal1.latir()
animal2.miar()
```
Neste exemplo, temos a classe base `Animal`, que representa um animal genérico, com os métodos `comer` e `dormir`. Em seguida, temos duas classes derivadas, `Cachorro` e `Gato`, que herdam da classe `Animal`. Essas classes especializam o comportamento do animal específico.

A classe `Cachorro` possui um método adicional `latir`, enquanto a classe `Gato` possui o método `miar`. Esses são exemplos de polimorfismo, pois as classes derivadas podem ter comportamentos diferentes para os mesmos métodos definidos na classe base.

Além disso, temos o encapsulamento, onde os atributos `nome` das classes são encapsulados e acessíveis por meio de métodos. E por fim, temos a abstração, onde a classe `Animal` é uma abstração de um animal genérico, enquanto as classes derivadas fornecem implementações específicas para diferentes tipos de animais.

Dessa forma, esse exemplo demonstra como a programação orientada a objetos em Python pode utilizar os quatro pilares para criar hierarquias de classes, reutilizar código e fornecer flexibilidade na implementação de comportamentos específicos.