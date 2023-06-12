#==========ALISTAMENTO MILITAR:============================
import datetime

atual = datetime.date.today().year
sexo = str(input("😎Qual é o seu sexo?\n😎masculino ou feminino?\n>>>")).strip().upper()
if sexo == "MASCULINO":
    nasc = int(input("😎Digite o ano do seu nascimento:\n>>>"))
    idade = atual - nasc

    print("_" *35)
    if idade == 18:
        resultado = "⭐Tem que se alistar imediatamente!"
    elif idade < 18:
        saldo = 18 - idade 
        ano = atual + saldo
        resultado = "⭐Faltam {:.0f} anos para o alistamento!\n⭐Seu alistamento será em {:.0f}!".format(saldo, ano)
    elif idade > 18:
        saldo = idade - 18
        ano = atual - saldo
        resultado = "⭐Deveria ter se alistado há {:.0f} anos!\n⭐Seu alistamento foi em {:.0f}!".format(saldo, ano)
        
    print("⭐Para quem nasceu em {:.0f};\n⭐Tem {:.0f} anos em {:.0f};\n{}".format(nasc, idade, atual, resultado))
    print("_" *35)
elif sexo == "FEMININO":
    print("😔Sinto muito!!!; Em nosso país só é permitido homens!!!")
else:
    print("😡Não compreendo!!!")