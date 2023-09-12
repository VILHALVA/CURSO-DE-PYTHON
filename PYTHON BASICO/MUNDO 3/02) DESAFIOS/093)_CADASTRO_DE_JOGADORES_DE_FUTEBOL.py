#=============CADASTRO DE JOGADORES DE FUTEBOL:==============================

jogador = dict()
partidas = list()

jogador["nome"] = str(input("😎Digite o nome:\n>>>"))
tot = int(input(f"😎Quantas partidas {jogador['nome']} jogou?\n>>>"))
for c in range(0, tot):
    partidas.append(int(input(f"😎Quantos gols na {c+1}ª partida?\n>>>")))
jogador["gols"] = partidas[:]
jogador["total"] = sum(partidas)

print("_" *35)
print(jogador)
print("_" *35)
for k, v in jogador.items():
    print(f"⚡O campo {k} tem o valor {v}")
print("_" *35)
print(f"⚡O jogador {jogador['nome']} jogou {len(jogador['gols'])} partidas:")
for i, v in enumerate(jogador["gols"]):
    print(f" ⏩Na {i+1}ª partida, fez {v} gols")
print(f"⭐Foi o total de {jogador['total']} gols!")
print("_" *35)

    	
