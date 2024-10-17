num = opr = c = 0
while True:
    num = int(input("😎Digite um número:\n🔔Envie float caso queira parar:\n>>>"))
    if num < 0:
        break
    opr = str(input("😎Digite o sinal aritmético[+×÷-]:\n>>>"))
    for c in range(1, 11):
        if opr == "×":
            print(f"{num} × {c:2} = {num*c}")
        elif opr == "+":
            print(f"{num} + {c:2} = {num+c}")
        elif opr == "-":
            print(f"{num} - {c:2} = {num-c}")
        elif opr == "÷":
            print(f"{num} ÷ {c:2} = {num/c}")
        else:
            print(f"😠Valor {opr} é inválido!!!")
print("⛔FIM!!")