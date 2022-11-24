#===========TUPLAS COM TIMES DE FUTEBOL:=============================
times = ("Corinthians", "Palmeiras", "Santos", "Grêmio", "Cruzeiro", "Flamengo", "Vasco", "Chapecoense",
         "Atlético", "Botafogo", "Atlético-PR", "Bahia", "São Paulo", "Fluminense", "Sport Recife", "EC Vitória", "Coritiba", "Avaí", "Ponte Preta", "Atlético-GO")

print("_" *30)
for t in times:
    print("😈",t)
print("-" *30)
print(f"⭐Os cinco primeiros colocados foram{times[:5]}!")
print("-" *30)
print(f"⭐Os últimos 4 colocados foram {times[-4:]}!")
print("-" *30)
print(f"⭐Times em ordem alfabética são {sorted(times)}!")
print("-" *30)
print(f"⭐A chapecoense está na {times.index('Chapecoense')+1}ª posição!")
print("_" *30)