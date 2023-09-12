#===========DICIONÁRIO EM PYTHON:======================================

aluno = dict()
aluno["nome"] = str(input("😎Digite o nome:\n>>>")).strip()
aluno["média"] = float(input(f"😎Média de aluno {aluno['nome']}:\n>>>"))
if aluno["média"] >= 7:
    aluno["situação"] = "Aprovado"
elif 5 <= aluno["média"] < 7:
    aluno["situação"] = "Recuperação"
else:
    aluno["situação"] = "Reprovado"

print("_" *35)
for k, v in aluno.items():
    print(f"⭐{k} é igual a {v}!\n", "-" *35)
print("_" *35)
