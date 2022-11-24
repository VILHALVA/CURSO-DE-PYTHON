#============ADICIONADO DICIONÁRIOS E LISTAS:=================================

galera = list()
pessoa = dict()
soma = média = 0

while True:
    pessoa.clear()
    pessoa["nome"] = str(input("😎Digite o nome:\n>>>")).strip().upper()
    while True:
        pessoa["sexo"] = str(input("😎Digite o seu sexo[M/F]:\n>>>")).strip().upper()[0]
        if pessoa["sexo"] in "MF":
            break
        print("⛔ERRO! Digite apenas M ou F!")
        
    if pessoa["sexo"] in "M":
        print(f"🍆Isso significa que {pessoa['nome']} é HOMEM!")
    if pessoa["sexo"] in "F":
        print(f"🍩Isso significa que {pessoa['nome']} é MULHER!")
    
    pessoa["idade"] = int(input("😎Digite a idade:\n>>"))
    soma += pessoa["idade"]
    print(f"😠{pessoa['nome']} registrado com sucesso!")
    galera.append(pessoa.copy())
    
    while True:    
        resp = str(input("😈Você quer continuar[S/N]?\n>>>")).strip().upper()[0]
        if resp in "SN":
            break
        print("⛔ERRO! Digite apenas S ou N!")  
    if resp in "Nn":
        break

média = soma / len(galera)

print("_" *35)
print(f"⭐Temos {len(galera)} pessoas cadastradas!\n⭐A média de idade é {média:5.2f} anos!\n⭐As mulheres cadastradas foram:")
for p in galera:
    if p["sexo"] in "Ff":
        print(f"⚡{p['nome']}!\n", end="")
print()
print("⭐A pessoa que está acima da média é:\n",end="")
for p in galera:
    if p["idade"] >= média:
        print("       ")
        for k, v in p.items():
            print(f"⚡{k} = {v}!\n",end="")
print()
print("_" *35)