#==========MENU DE CADASTRO:===============================

#-------------FUNCOES BÁSICAS:--------------------------
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("\033[31m😬ERRO! Digite um valor Inteiro!!!\033[m")
            continue
        except KeyboardInterrupt:
            print("🔺Houve erro! Usuário não digitou valor!")
            return n
        else:
            return n

def linha(tam=35):
    return "_" * tam

def cabeçalho(txt):
    print(linha())
    print(txt.center(28))
    print(linha())
    
def menu(lista):
    cabeçalho("😈MENU PRINCIPAL:")
    c = 1
    for item in lista:
        print(f"\033[33m{c}\033[m - \033[34m{item}\033[m")
        c += 1
    print(linha())
    opc = leiaInt("\033[32m😎Digite o número da sua opção:\n>>>\033[m")
    return opc
    
    
#-----------CRIAR/LER ARQUIVO:-----------------------------------------------
#import ex115.lib.interface import *
	
def arquivoExiste(nome):
    try:
        a = open(nome, "rt")
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def criarArquivo(nome):
    try:
        a = open(nome, "wt+")
        a.close()
    except:
        print("🔻Falha ao criar arquivo!!!")
    else:
        print(f"👍Arquivo {nome} criado com sucesso!!!")

def lerArquivo(nome):
    try:
        a = open(nome, "rt")
    except:
        print("🔻Falha ao ler arquivo!!!")
    else:
        cabeçalho ("🎂PESSOAS CADASTRADAS:")
        for linha in a:
            dado = linha.split(";")
            dado[1] = dado[1].replace("\n", "")
            print(f"👤{dado[0]:<15}{dado[1]:3>} anos")
    finally:
        a.close()
        
def cadastrar(arq, nome=0, idade=0):
    try:
        a = open(arq, "at")
    except:
        print("🔻Falha ao abrir arquivo!!!")
    else:
        try:
            a.write(f"{nome};{idade}\n")
        except:
            print("🔻Falha ao escrever os dados!!!")
        else:
            print(f"👍Novo registro de {nome} adicionado com sucesso!!!")
            a.close()
            
        
#--------PROGRAMA PRINCIPAL:-----------------------------------
from time import sleep

arq = "CADASTRO.txt"
if not arquivoExiste(arq):
    criarArquivo(arq)        
    
while True:
    resposta = menu(["PESSOAS CADRASTRADAS", "CADASTRAR NOVA PESSOA", "SAIR DO PROGRAMA"])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho("➕NOVO CADASTRO:")
        nome = str(input("👤NOME:\n>>>"))
        idade = leiaInt("👤IDADE:\n>>>")
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho("⛔FIM DO SISTEMA")
        break
    else:
        cabeçalho("\033[31m⛔ERRO! Digite uma opção válida!!!\033[m") 
    sleep(2)


