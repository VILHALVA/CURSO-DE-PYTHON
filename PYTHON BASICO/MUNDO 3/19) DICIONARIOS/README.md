# DICIONARIOS
Dicionários são uma estrutura de dados fundamental em Python que permitem associar valores a chaves. Eles são conhecidos como "mapas" em outras linguagens de programação. Os dicionários são usados para armazenar coleções de dados que podem ser acessados e modificados rapidamente por meio de chaves únicas. Aqui está como criar e usar dicionários em Python:

## Criando um Dicionário
Você pode criar um dicionário usando chaves `{}` e especificando pares chave-valor separados por dois-pontos `:`. Por exemplo:

```python
meu_dicionario = {"nome": "João", "idade": 30, "cidade": "São Paulo"}
```

Neste exemplo, temos um dicionário com três pares chave-valor: "nome", "idade" e "cidade".

## Acessando Valores em um Dicionário
Você pode acessar valores em um dicionário usando as chaves correspondentes:

```python
nome = meu_dicionario["nome"]  # Acessa o valor associado à chave "nome"
idade = meu_dicionario["idade"]  # Acessa o valor associado à chave "idade"
```

## Modificando Valores em um Dicionário
Dicionários são mutáveis, o que significa que você pode modificar os valores associados às chaves existentes:

```python
meu_dicionario["idade"] = 31  # Modifica o valor associado à chave "idade" para 31
```

## Adicionando Novos Pares Chave-Valor
Você pode adicionar novos pares chave-valor a um dicionário:

```python
meu_dicionario["email"] = "joao@example.com"  # Adiciona um novo par chave-valor
```

## Removendo Pares Chave-Valor
Você pode remover pares chave-valor usando a palavra-chave `del`:

```python
del meu_dicionario["cidade"]  # Remove o par chave-valor com a chave "cidade"
```

## Verificando a Existência de Chaves
Para verificar se uma chave existe em um dicionário, você pode usar a palavra-chave `in`:

```python
if "email" in meu_dicionario:
    print("A chave 'email' existe no dicionário.")
```

## Comprimento de um Dicionário
Você pode obter o número de pares chave-valor em um dicionário usando a função `len()`:

```python
quantidade_de_pares = len(meu_dicionario)  # Obtém o número de pares chave-valor
```

## Iterando em Dicionários
Você pode usar loops `for` para iterar através das chaves, dos valores ou dos pares chave-valor de um dicionário:

```python
meu_dicionario = {"nome": "João", "idade": 30, "cidade": "São Paulo"}

# Iterando pelas chaves
for chave in meu_dicionario:
    print(chave)

# Iterando pelos valores
for valor in meu_dicionario.values():
    print(valor)

# Iterando pelos pares chave-valor
for chave, valor in meu_dicionario.items():
    print(chave, valor)
```

Os dicionários são uma estrutura de dados muito flexível e útil em Python. Eles são amplamente utilizados para armazenar informações organizadas e associativas. É importante notar que as chaves em um dicionário devem ser únicas, mas os valores podem ser de qualquer tipo de dados, inclusive outras estruturas de dados, como listas ou dicionários aninhados.