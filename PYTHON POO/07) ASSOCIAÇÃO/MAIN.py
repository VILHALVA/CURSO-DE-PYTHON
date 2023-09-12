from CLASSES import Escritor, Caneta, MaquinaEscrever

escritor = Escritor("PEDRO")
caneta = Caneta("BIC")
maquina = MaquinaEscrever()

print(escritor.nome)
print(caneta.marca)
maquina.escrever()

escritor.ferramenta = maquina
escritor.ferramenta.escrever()

del escritor
print(caneta.marca)
MaquinaEscrever()