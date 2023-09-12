#==========CRIANDO UM MENU DE OPÇÕES:=====================
from time import sleep

n1 = float(input("😎Digite o primeiro valor:\n>>>"))
n2 = float(input("😎Digite o segundo valor:\n>>>"))

opção = 0
while opção != 5:
    print("_" *35)
    print('''
    	⭐MENU DE OPÇÕES:
    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR 
    [ 4 ] NOVOS NÚMEROS 
    [ 5 ] SAIR DO PROGRAMA''')
    print("_" *35)

    opção = int(input("😎Qual é a sua opção?\n>>>"))

    if opção == 1:
        print("⭐A soma de {} + {} = {}!".format(n1, n2, n1+n2))
        sleep(3)
    elif opção == 2:
        print("⭐A multiplicação de {} × {} = {}!".format(n1, n2, n1*n2))
        sleep(3)
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print("⭐Entre {} e {}; O maior é {}!!!".format(n1, n2, maior))
        sleep(3)
    
    elif opção == 4:
        print("⭐Informe os números novamente!!!")
        n1 = float(input("😎Digite o primeiro valor:\n>>>"))
        n2 = float(input("😎Digite o segundo valor:\n>>>"))
        
    elif opção == 5:
        print("⏳Finalizando...",end= "\r")
        sleep(3)
        print("⛔FIM DO PROGRAMA!!!")
        exit()
    
    else:
        print("😠Valor inválido!!!Tente novamente!!!")
        sleep(2)
    
    