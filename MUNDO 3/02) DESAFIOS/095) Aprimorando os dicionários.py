#==========APRIMORANDO OS DICIONÁRIOS:=============================

time = list()
jogador = dict()
partidas = list()
cont = 1

while True:
    jogador.clear()
    jogador["nome"] = str(input(f"😎Digite o nome do {cont}ª jogador:\n>>>"))
    cont += 1
    tot = int(input(f"😎Quantas partidas {jogador['nome']} jogou?\n>>>"))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f"😎Quantos gols na {c+1}ª partida?\n>>>")))
    jogador["gols"] = partidas[:]
    jogador["total"] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input("😈Você quer continuar[S/N]?:\n>>>")).strip().upper()[0]
        if resp in "SN":
            break
        print("⛔ERRO! Digite S ou N!")
    if resp in "Nn":
        break

print("_" *30)
print("cod ", end="")
for i in jogador.keys():
    print(f"{i:<10}", end="")
print()
print("_" *30)
for k, v in enumerate(time):
    print(f"{k:>3} ", end="")
    for d in v.values():
        print(f"{str(d):<10}", end="")
    print()
print("_" *30)

while True:
    busca = int(input("😎Digite o número do jogador para mostrar os dados!\n⛔Envie 999 para parar:\n>>>"))
    if busca == 999:
        break
    if busca >= len(time):
        print("⛔ERRO! Não existe jogador com esse valor!")
    else:
        print(f"--DADOS DO JOGADOR: {time[busca]['nome']}:")
        for i, g in enumerate(time[busca]['gols']):
            print(f"   ⚡No jogo {i+1} fez {g} gols!")
    print("_" *30)

    	