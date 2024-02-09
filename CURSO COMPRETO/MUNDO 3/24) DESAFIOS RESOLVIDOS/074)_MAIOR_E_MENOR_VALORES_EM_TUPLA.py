#==============MAIOR E MENOR NÚMEROS EM TUPLA:================================
from random import randint
números = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print("⭐Eu sortei os valores:",end=" ")
for n in números:
    print(f"{n}",end=" ")
print(f"\n⭐O maior valor foi {max(números)}!\n⭐O menor valor foi {min(números)}!")