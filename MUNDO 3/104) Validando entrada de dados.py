#============VALIDANDO A ENTRADA DE DADOS:=================================

def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print("\033[0;31m⛔ERRO! Digite um nª inteiro válido.\033[m")
        if ok:
            break
    return valor
    

n = leiaInt("😎Digite um número:\n>>>")
print(f"⭐Você acabou de digitar o número {n}")