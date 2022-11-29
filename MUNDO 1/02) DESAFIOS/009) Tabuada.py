#============ TABUADA: ===============================
import time

num = int(input("😎Digite um número para ver a sua tabuada:\n>>>"))

print("⏳Processando...",end="\r")
time.sleep(3)

print("-" *15)
print("{} × {:2} = {}".format(num, 0, num*0))
print("{} × {:2} = {}".format(num, 1, num*1))
print("{} × {:2} = {}".format(num, 2, num*2))
print("{} × {:2} = {}".format(num, 3, num*3))
print("{} × {:2} = {}".format(num, 4, num*4))
print("{} × {:2} = {}".format(num, 5, num*5))
print("{} × {:2} = {}".format(num, 6, num*6))
print("{} × {:2} = {}".format(num, 7, num*7))
print("{} × {:2} = {}".format(num, 8, num*8))
print("{} × {:2} = {}".format(num, 9, num*9))
print("{} × {:2} = {}".format(num, 10, num*10))
print("-" *15)