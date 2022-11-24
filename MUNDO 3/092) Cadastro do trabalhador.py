#==========CADASTRO DO TRABALHADOR:============================
from datetime import datetime

dados = dict()
dados["nome"] = str(input("😎Digite seu nome:\n>>>"))
nasc = int(input("😎Digite seu ano de nascimento:\n>>>"))
dados["idade"] = datetime.now().year - nasc
dados["ctps"] = int(input("😎Sua carteira de trabalho.\n😎Envie 0 se não tiver:\n>>>"))

if dados["ctps"] != 0:
    dados["contratação"] = int(input("😎Seu ano de contratação:\n>>>"))
    dados["salário"] = float(input("😎Qual é o seu salário[R$]?:\n>>>"))
    dados["aposentadoria"] = dados["idade"] + ((dados["contratação"] + 35) - datetime.now().year)
    
print("_" *35)
for k, v in dados.items():
    print("-" *20, f"\n★{k} é {v}!\n", "-" *20) 
print("_" *35)