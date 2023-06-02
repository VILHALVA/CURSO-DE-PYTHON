from time import sleep

cont = 1
for c in range(0, 101, 1):
    print(f"⭐Contagem: {c}", end="\r")
    cont += 1
    sleep(0.1)