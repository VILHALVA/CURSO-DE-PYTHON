# CONDICIONAIS PARTE 2
As condicionais aninhadas, também conhecidas como condicionais dentro de condicionais, permitem que você crie estruturas de decisão complexas, com base em múltiplas condições. Em Python, isso é feito aninhando `if`, `elif`, e `else` dentro de outras condicionais. Vamos explorar como usar condicionais aninhadas em Python.

## Estrutura Básica de Condicionais Aninhadas
A estrutura básica de condicionais aninhadas envolve a criação de condicionais dentro de outras condicionais. Aqui está a sintaxe geral:

```python
if condicao_externa:
    # Código a ser executado se a condicao_externa for verdadeira
    if condicao_interna_1:
        # Código a ser executado se a condicao_interna_1 for verdadeira
    elif condicao_interna_2:
        # Código a ser executado se a condicao_interna_2 for verdadeira
    else:
        # Código a ser executado se a condicao_interna_1 e condicao_interna_2 forem falsas
else:
    # Código a ser executado se a condicao_externa for falsa
```

As condicionais internas (`if`, `elif`, `else`) estão aninhadas dentro da condicional externa (`if`). Você pode adicionar quantas condicionais internas forem necessárias, criando estruturas de decisão mais complexas.

## Exemplo de Condicionais Aninhadas
Vamos considerar um exemplo onde queremos determinar a categoria de um produto com base no seu preço e quantidade em estoque. Existem três categorias: "Caro", "Médio" e "Barato". Aqui está um código que faz isso usando condicionais aninhadas:

```python
preco = 100
quantidade = 50

if quantidade > 100:
    if preco > 50:
        categoria = "Caro"
    else:
        categoria = "Médio"
else:
    categoria = "Barato"

print(f"Este produto é da categoria: {categoria}")
```

Neste exemplo, as condicionais internas verificam o preço e a quantidade, enquanto a condicional externa verifica a quantidade. Dependendo dos valores, o programa determina a categoria do produto.

## Dicas para Usar Condicionais Aninhadas
1. **Mantenha o Código Limpo**: À medida que você aninha mais condicionais, o código pode ficar mais complexo. Certifique-se de manter seu código organizado e com boas práticas de formatação para torná-lo mais legível.

2. **Comentários Descritivos**: Adicione comentários descritivos ao seu código para explicar a lógica das condicionais aninhadas, especialmente se elas forem complexas.

3. **Evite Profundidade Excessiva**: Evite criar condicionais aninhadas profundas demais, pois isso pode tornar o código difícil de entender e depurar. Se necessário, considere a possibilidade de dividir a lógica em funções menores.

4. **Teste com Dados de Exemplo**: Ao trabalhar com condicionais aninhadas, é importante testar com diferentes conjuntos de dados de exemplo para garantir que todas as condições sejam tratadas corretamente.

As condicionais aninhadas são uma ferramenta poderosa para criar lógica condicional complexa em seus programas Python. Com cuidado e prática, você pode usá-las para resolver problemas complexos de decisão de forma eficaz.