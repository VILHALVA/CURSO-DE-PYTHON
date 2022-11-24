#==========JOGO DE PAR OU IMPA:=====================
from random import randint
v = 0
while True:
    jogador = int(input("😎Diga o valor:\n>>>"))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = " "
    while tipo not in "PI":
        tipo = str(input("😎É PAR ou IMPAR[P/I]:\n>>>")).strip().upper()[0]
    print("_" *35)
    print(f"⭐Você jogou {jogador}!\n⭐Eu joguei {computador}!\n⭐Total: {total}!")
    print("➕PAR" if total % 2 == 0 else "➖IMPAR")
    if tipo == "P":
        if total % 2 == 0:
            print("👍VENCEU!!!")
            v += 1
        else:
            print("👎PERDEU!!!")
            break
    elif tipo == "I":
        if total % 2 == 1:
            print("👍VENCEU!!!")
            v += 1
        else:
            print("👎PERDEU!!!")
            break
    
    print("_" *35)
    
    print("😎Vamos jogar novamente...")
print(f"⛔GAME OVER!!!\n🎂VOCÊ VENCEU {v} VEZES!!!")
print("_" *35)
            
        