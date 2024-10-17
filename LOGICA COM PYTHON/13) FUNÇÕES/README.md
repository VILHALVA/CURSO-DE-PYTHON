# FUNÇÕES
## CONCEITOS:
Em Python, funções são blocos de código que realizam tarefas específicas e podem receber argumentos como entrada e retornar um valor como saída. Elas são uma parte fundamental da programação estruturada e modular, permitindo que você quebre um programa em partes menores e mais gerenciáveis. Aqui estão os conceitos chave sobre funções em Python:

**Definindo Funções em Python:**

Para definir uma função em Python, você precisa especificar seu nome, seus parâmetros (se houver), e o código que a função executa. Aqui está uma estrutura típica de uma função em Python:

```python
def nome_da_funcao(parametro1, parametro2, ...):
    # Código da função
    return resultado
```

- `nome_da_funcao`: É o nome da função, que você escolhe de acordo com a tarefa que a função executa.

- `parametro1`, `parametro2`, ...: São os parâmetros que a função pode receber como entrada. Eles são opcionais e servem para passar dados para a função.

- `return resultado`: É a instrução que indica o valor de retorno da função.

**Chamando Funções em Python:**

Para usar uma função em Python, você a chama pelo nome e passa os argumentos necessários. Aqui está como você chama uma função:

```python
resultado = nome_da_funcao(arg1, arg2, ...)
```

- `nome_da_funcao`: É o nome da função que você deseja chamar.

- `arg1`, `arg2`, ...: São os argumentos que você passa para a função, correspondendo aos parâmetros definidos na função.

**Escopo em Funções:**

O escopo refere-se à visibilidade e acessibilidade das variáveis em um programa. Em Python, as variáveis definidas dentro de uma função têm escopo local, o que significa que elas só são acessíveis dentro da própria função. Isso também se aplica aos parâmetros da função.

Por exemplo:

```python
def minha_funcao(x):
    print(x)  # x é acessível aqui

x = 10  # x é uma variável diferente da x da função
print(x)  # x é acessível aqui
minha_funcao(5)  # x da função é diferente do x fora da função
```

Neste exemplo, `x` é uma variável local dentro da função `minha_funcao` e não interfere com a variável `x` definida fora da função.

**Diferenças Entre Escopo:**

- Variáveis definidas dentro de uma função são chamadas de variáveis locais e só são visíveis dentro dessa função. Elas não afetam o escopo global do programa.

- Variáveis definidas fora de qualquer função são chamadas de variáveis globais e são visíveis em todo o programa. Elas têm um escopo global.

É importante tomar cuidado ao usar variáveis globais, pois elas podem ser acessadas e modificadas de qualquer lugar do programa, o que pode tornar o código mais difícil de depurar e entender. O uso de variáveis locais é preferível sempre que possível, pois ajuda a encapsular a lógica e evita efeitos colaterais indesejados.

## EXERCICIOS:
* **01) PAR OU IMPAR:**
```python
def par_impar(num):
    if num % 2 == 0:
        valor = "👍PAR!"
    elif num % 2 == 1:
        valor = "👎ÍMPAR!"
    else:
        valor = "😬NÃO SEI"
    print("⭐O número", num, "é", valor)

def principal():
    num = int(input("😎Digite um valor: "))
    par_impar(num)
    print("⛔FIM")

principal()
```

* **02) FATORIAL:**
```python
def fatorial(n, show=False):
    f = 1
    for c in range(1, n + 1):
        if show:
            print(c, end='')
            if c > 1:
                print(' × ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f

n = int(input("😎Digite um valor:\n>>>"))
f = fatorial(n, True)
print(f"⭐O valor de {n} é {f}")
```

* **03) SEQUÊNCIA FIBONACCI:**
```python
n = int(input("😎Digite a quantidade de termos que deseja ver: "))
t1 = 0
t2 = 1
print(t1, "›", t2, end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(" »", t3, "!", end='')
    t1, t2 = t2, t3
    cont += 1
print(" ⟩⛔FIM!!! ")
```