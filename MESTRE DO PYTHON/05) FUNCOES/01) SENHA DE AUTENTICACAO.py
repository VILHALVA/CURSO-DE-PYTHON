from time import sleep
cont = 1

def tempo(txt1, I, txt2):
     print(f"😠Foram {cont} tentativas!!!", end="\r")
     sleep(2)
     for c in range(I, 0, -1):
         print(f"{txt1}: {c} {txt2}", end="\r")
         sleep(1)
     senha = str(input("🔐Digite a senha para começar:\n>>>"))   
senha = str(input("🔐Digite a senha para começar:\n>>>"))
while senha not in "VILHALVA":
    cont += 1
    senha = str(input("🔒Senha inválida!!!Tente novamente:\n>>>"))
    if cont == 3:
        tempo("⌛Aguarde", 60, "segundos...")        
    elif cont == 6:
        tempo("⌛Aguarde", 300, "segundos...")
    elif cont > 10:
        tempo("⌛Aguarde", 9999999, "segundos...")                
print("=" *35, f"\n👏PARABÉNS!!!\n🔓VOCÊ ACERTOU!!!\n⭐Foram {cont} tentativas!!!\n", "=" *35)
sleep(2)