# CURSO-DE-PYTHON
👨‍⚖️CURSO COMPRETO DE PYTHON.

[![GitHub Repo stars](https://img.shields.io/badge/VILHALVA-GITHUB-03A9F4?logo=github)](https://github.com/VILHALVA)
[![GitHub Repo stars](https://img.shields.io/badge/VEJA-DOCUMENTAÇÃO-03A9F4?logo=google)](https://docs.python.org/3/) <br>

[![GitHub Repo stars](https://img.shields.io/badge/-MUNDO%201-green)](https://www.youtube.com/playlist?list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6)
[![GitHub Repo stars](https://img.shields.io/badge/-MUNDO%202-green)](https://www.youtube.com/playlist?list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye)
[![GitHub Repo stars](https://img.shields.io/badge/-MUNDO%203-green)](https://www.youtube.com/playlist?list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye) <br>

<img src="https://images.vexels.com/media/users/3/166477/isolated/lists/9bb722f0e85ddbc1ce0f064534fd2311-icone-da-linguagem-de-programacao-python.png" align="center" width="280"> <br>

# 🤖REQUESITOS:
* 🤯[SABER LÓGICA DE PROGRAMAÇÃO](https://github.com/VILHALVA/CURSO-DE-ALGORITMO)
* 💻[INSTALAR O PYCHARM](https://www.jetbrains.com/pt-br/pycharm/)
* 💻[INSTALAR O PYTHON](https://python.org.br/instalacao-windows/)

# [MUNDO 1: FUNDAMENTOS](https://www.youtube.com/watch?v=S9uPNppGsGo&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6)
* ✅ INSTALANDO O PYCHARM
* ✅ PRIMEIROS COMANDOS
* ✅ CONHECENDO O INPUT
* ✅ VARIÁVEIS SIMPLES
* ✅ ESTRUTURAS CONDICIONAIS SIMPLES
* ✅ OPERADORES ARITMÉTICAS
* ✅ UTILIZANDO MÓDULOS
* ✅ OPERAÇÕES DE STRINGS
* ✅ CORES NO CONSOLE

# [MUNDO 2: ESTRUTURAS DE CONTROLE](https://www.youtube.com/watch?v=nJkVHusJp6E&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye)
* ✅ CONDICIONAIS ANINHADAS
* ✅ ESTRUTURAS DE REPETIÇÃO "FOR"
* ✅ ESTRUTURAS DE REPETIÇÃO "WHILE"
* ✅ INTERROPENDO REPETIÇÕES

# [MUNDO 3: ESTRUTURAS COMPOSTAS](https://www.youtube.com/playlist?list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH)
* ✅ VARIÁVEIS COMPOSTAS: TUPLAS
* ✅ VARIÁVEIS COMPOSTAS: LISTAS
* ✅ VARIÁVEIS COMPOSTAS: DICIONÁRIOS
* ✅ FUNÇÕES
* ✅ MÓDULOS E PACOTES
* ✅ TATAMENTO DE ERROS E EXCEÇÕES

![](https://i.imgur.com/waxVImv.png)
# 🤳SINTAXE DA LINGUAGEM:
👨‍⚖️VISÃO PANORÂMICA DA ESTRUTURA DO PYTHON COM O "MESTRE DO PYTHON".

## 01) VARIAVEIS SIMPLES:
* ↪️ Variáveis em Python são lugares reservados na memória de um dispositivo para o armazenamento de dados que posteriormente vão ser usados na execução de uma solução digital. Essas variáveis podem ter formatos e tamanhos diferentes, entre outras particularidades. Podemos pensar que a memória RAM de um dispositivo é como um grande armário, que comporta diversos itens no seu interior, e esse itens são as variáveis. Quando você abre um armário, lá podem estar roupas, calçados, livros e objetos decorativos em geral. Apesar de suas diferenças, todos esses itens podem ser armazenados em um único lugar e, na medida em que são retirados do seu espaço, fica uma lacuna que pode ser preenchida por outra variável ou pela mesma. Elas são declaradas: "NOME = ATRIBUTO".
```
# Declarando variáveis e atribuindo valores
nome = "João"
idade = 25
altura = 1.75
ativo = True

# Exibindo os valores das variáveis
print("Nome:", nome)
print("Idade:", idade)
print("Altura:", altura)
print("Ativo:", ativo)
```

## 02) ESTRUTURA CONDICIONAL:
* ↪️ Uma estrutura condicional na linguagem Python, como a Python "If", "Elif", "Else", corresponde a um bloco de código que é iniciado com uma expressão para avaliar se uma determinada condição é verdadeira ou falsa. Com ele, podemos testar se uma variável é igual a zero.
```
# Exemplo de estrutura condicional
idade = 20

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
```

```
# Exemplo de estrutura condicional mais complexa
idade = 20

if idade < 0:
    print("Idade inválida.")
elif idade < 18:
    print("Você é menor de idade.")
elif idade < 65:
    print("Você é adulto.")
else:
    print("Você é um idoso.")
```

## 03) ESTRUTURA DE REPETIÇÃO:
* ↪️ Em Python existem duas formas de criar uma estrutura de repetição: O "for" é usado quando se quer iterar sobre um bloco de código um número determinado de vezes. O "while" é usado quando queremos que o bloco de código seja repetido até que uma condição seja satisfeita.
```
# Exemplo de estrutura de repetição com o comando 'while'
contador = 0

while contador < 5:
    print("Contador:", contador)
    contador += 1
```

```
# Exemplo de estrutura de repetição com o comando 'for'
nomes = ["João", "Maria", "Pedro", "Ana"]

for nome in nomes:
    print("Nome:", nome)
```

## 04) VARIAVEIS COMPOSTAS:
* ↪️ Diferente da "Variavel Simples" (Uma Variavel só pode amarzenar um único dado). Na "Variavel Composta" uma unica Variavel pode armazenar varios dados (Até de Tipos diferentes). No python, temos 3 Tipos de Variaveis Compostas:
* ⏺️ TUPLAS: São Imutaveis (Não aceitam Inputs). Elas usam parenteses ( ).
```
# Exemplo de tupla
tupla = (1, "dois", 3.0, True)

# Acessando elementos da tupla
print(tupla[0])  # Saída: 1
print(tupla[1])  # Saída: "dois"

# Tentativa de modificar um elemento da tupla (resultará em erro)
tupla[0] = 10  # Erro: as tuplas são imutáveis
```
* ⏺️ LISTAS: São Mutavéis (Aceitam Inputs). Seus dados podem ser chamados via indice númerico (Não pode personalizar). Elas usam colchetes [ ].
```
# Exemplo de lista
lista = [1, 2, 3, 4, 5]

# Acessando elementos da lista
print(lista[0])  # Saída: 1
print(lista[2])  # Saída: 3

# Modificando um elemento da lista
lista[0] = 10
print(lista)  # Saída: [10, 2, 3, 4, 5]
```
* ⏺️ DICIONÁRIOS: São Mutavéis (Aceitam Inputs). Seus dados podem ser chamados via nome (Pode personalizar). Elas usam chaves { }.
```
# Exemplo de dicionário
dicionario = {"chave1": "valor1", "chave2": "valor2", "chave3": "valor3"}

# Acessando valores do dicionário
print(dicionario["chave1"])  # Saída: "valor1"
print(dicionario["chave3"])  # Saída: "valor3"

# Adicionando um novo par chave-valor ao dicionário
dicionario["chave4"] = "valor4"
print(dicionario)  # Saída: {"chave1": "valor1", "chave2": "valor2", "chave3": "valor3", "chave4": "valor4"}
```

## 05) FUNÇÕES:
* ↪️ As funções em Python servem para deixar o desenvolvimento de soluções digitais mais práticas, automatizadas, organizadas e dinâmicas. Isso porque elas moldam os códigos, permitindo que eles sejam reutilizados. Ou seja, quando aparece a necessidade, você não precisa repetir as mesmas instruções diversas vezes. Elas são declaradas com "def nome():". E são chamadas com "import nome" ou "from nome import sobrenome" ou "from nome import*"; Assim como "nome()". Gosto de dividir as funções em 2 CATEGORIAS:
* ⏺️FUNÇÕES INTERNAS: São funções que você cria. Elas estão na mesma pasta do seu script principal.
* ⏺️FUNÇÕES EXTERNAS: São funções criadas por outros (API). Elas são conhecidas como módulos (Arquivos) ou pacotes (Diretórios). Geralmente elas não estão na mesma pasta do seu script principal. Para serem usadas, elas precisam estar instaladas na sua maquina ou serem chamadas via url. A função mais famosa (Está na documentação) é o "pygame".
```
# Exemplo de função
def saudacao(nome): # Função que imprime uma saudação personalizada.
    print("Olá, " + nome + "! Bem-vindo(a)!")

# Chamando a função
saudacao("João")
```

## 06) CLASSES:
↪️ As classes são semelhantes a "FUNÇÕES". A maior diferença é que você pode colocar varias funções dentro de uma mesma Classe (Assim como em única FUNÇÃO você pode colocar muitas Variaveis). É importante salientar que a Classe é referente a POO (Orientação a Objetos). Na pratica você descreve os atributos de qualquer objeto (Jogos e Web usam muito desse principio). Elas são declaradas como "class nome():" e chamadas como "nome()".
```
# Exemplo de classe
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def apresentar(self):
        print("Olá, meu nome é", self.nome, "e tenho", self.idade, "anos.")

# Criando uma instância da classe
pessoa1 = Pessoa("João", 25)

# Chamando um método da classe
pessoa1.apresentar()
```

# 💖CARACTERISTICAS DA LINGUAGEM:
## ❤POSITIVAS:
* 1 - Sintaxe baseada em indentação: Python usa a indentação (recuo) para definir blocos de código em vez de chaves ou palavras-chave especiais. Isso significa que a estrutura do código é determinada pela quantidade de espaços ou tabulações no início de cada linha. A indentação consistente é essencial para que o código Python seja executado corretamente.
* 2 - Uso em projetos diversos: Python é amplamente utilizado em diversos tipos de projetos, como desenvolvimento web, análise de dados, automação de tarefas, inteligência artificial, aprendizado de máquina, criação de scripts e muito mais. É uma linguagem versátil que pode ser aplicada em diferentes áreas e oferece uma ampla gama de bibliotecas e frameworks especializados.
* 3 - Ênfase na legibilidade: A sintaxe limpa e a filosofia de design do Python enfatizam a legibilidade do código. Os programadores são encorajados a escrever código claro, conciso e fácil de entender, seguindo o princípio do "Zen do Python", que enfatiza a clareza sobre a complexidade.
* 4 - Ampla biblioteca padrão: O Python possui uma biblioteca padrão abrangente, que oferece muitas funcionalidades prontas para uso. Essa biblioteca inclui módulos para manipulação de strings, processamento de arquivos, acesso a bancos de dados, desenvolvimento web, teste unitário e muito mais. Isso torna o Python uma escolha conveniente para uma variedade de tarefas, pois muitas funcionalidades já estão disponíveis sem a necessidade de instalar bibliotecas adicionais.
* 5 - Comunidade ativa e suporte: Python tem uma comunidade grande e ativa de desenvolvedores em todo o mundo. Isso significa que há muitos recursos, fóruns de discussão, tutoriais e pacotes adicionais disponíveis para ajudar os programadores. A comunidade é conhecida por ser acolhedora e disposta a ajudar os iniciantes.
* 6 - Multiplataforma: Python é uma linguagem multiplataforma, o que significa que os programas escritos em Python podem ser executados em vários sistemas operacionais, como Windows, macOS e Linux, sem a necessidade de grandes modificações.

## 🖤NEGATIVAS:
* 1 - Desempenho relativo: Comparado a algumas linguagens de programação de baixo nível, como C++ ou Rust, Python tende a ter um desempenho inferior. Isso ocorre devido à sua natureza interpretada e tipagem dinâmica, o que pode resultar em um tempo de execução mais lento em certos cenários. No entanto, vale ressaltar que a maioria das aplicações não exige um desempenho extremamente rápido, e em muitos casos, o desempenho do Python é satisfatório.
* 2 - Gerenciamento de memória: Python utiliza um mecanismo de gerenciamento de memória automático, conhecido como "garbage collector". Embora isso seja conveniente para os desenvolvedores, pois não é necessário se preocupar com alocação e liberação manual de memória, em alguns casos, o garbage collector pode introduzir uma pequena sobrecarga e impactar no desempenho do programa.
* 3 - Escalabilidade vertical: O Python não é considerado tão adequado para escalabilidade vertical, ou seja, para aproveitar plenamente os recursos de máquinas com múltiplos núcleos ou clusters. Isso ocorre porque o Python possui um mecanismo chamado Global Interpreter Lock (GIL), que impede que múltiplas threads executem código Python simultaneamente em paralelo. Embora existam maneiras de contornar isso (usando processos em vez de threads, por exemplo), a escalabilidade vertical não é tão natural em Python quanto em algumas outras linguagens.
* 4 - Poucas vagas específicas de trabalho: Em comparação com algumas linguagens mais especializadas ou voltadas para domínios específicos, como C++ para desenvolvimento de jogos ou Java para desenvolvimento corporativo, Python pode ter menos vagas específicas disponíveis. No entanto, é importante notar que Python é usado em uma ampla variedade de setores e domínios, o que significa que ainda há muitas oportunidades para programadores Python em geral.
