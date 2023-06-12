#=========FUNÇÕES APROFUNDADAS:====================================

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("\033[31m😬ERRO! Digite um valor Inteiro!\033[m")
            continue
        except KeyboardInterrupt:
            print("🔺Houve erro! Usuário não digitou valor!")
            return n
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print("\033[31m😬ERRO! Digite um valor Real!\033[m")
            continue
        except KeyboardInterrupt:
            print("🔺Houve erro! Usuário não digitou valor!")
            return n
        else:
            return n
            
                  
n1 = leiaInt("😎Digite valor inteiro:\n>>>")
n2 = leiaFloat("😎Digite valor Real:\n>>>")
print("_" *35, f"\n⭐O valor digitado foi {n1} e {n2}\n", "_" *35)
