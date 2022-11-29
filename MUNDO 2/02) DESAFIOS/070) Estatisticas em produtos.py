#==========ESTATÍSTICAS EM PRODUTOS:=========================={
from time import sleep
total = totmil = menor = maior = cont = 0
barato = " "
caro = " "

while True:
    produto = str(input("😎Digite o nome do produto:\n>>>")).strip()
    preço = float(input("😎Digite o preço[R$]:\n>>>"))
    
    cont += 1
    total += preço

    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto  
    if cont == 1 or preço > maior:
        maior = preço  
        caro = produto
    
    resp = " "
    while resp not in "SN":
        resp = str(input("😎Quer continuar?\n>>>")).strip().upper()[0]
    if resp == "N":
        break

print("⌛Processando...",end="\r")
sleep(3)
print("_" *35) 
print(f"⭐A compra custou(R$): {total:3.2f}!\n⭐São {totmil} p. custando mais de R$1000!\n⭐O mais caro foi {caro}...\n⚡Custando R${maior:.2f}!\n⭐O mais barato foi {barato}...\n⚡Custando R${menor:.2f}!")  
print("_" *35)     
print("{:-^30}".format("⛔FIM"))
