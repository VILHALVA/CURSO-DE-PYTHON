#==========DICIONÁRIOS:============================================================================

pessoas = {"nome": "Samuel", "sexo": "M", "idade": 26}
print(pessoas) #< Exibe todo o dicionário.
print(pessoas["nome"]) #< Exibe o nome: "Samuel"
print(pessoas["sexo"]) #< Exibe o sexo: "M".
print(pessoas["idade"]) #< Exibe a idade: "26".
print(f"⭐O {pessoas['nome']} tem {pessoas['idade']} anos de idade!") #<Exibe nome e idade personalizado.
print(f"⭐O {pessoas['nome']} é do sexo {pessoas['sexo']}!") #<Exibe nome e sexo personalizado.
print(pessoas.keys()) #< Irá exibir o índice:"nome", "sexo" e "idade".
print(pessoas.values()) #< Irá exibir os valores: "Samuel", "M", "26".
print(pessoas.items()) #< Semelhante ao "print(pessoas)", exibe o dicionário completo.
pessoas["peso"] = 98.5 #< Adiciona o valor e índice ao dicionário (Diferente das tuplas e listas, no dicionário não precisa usar "append").

for k in pessoas.keys(): #>Elimina "{[()]}".
    print(k) #< Irá exibir o índice:"nome", "sexo" e "idade".
for v in pessoas.values(): #>Elimina "{[()]}".
    print(v) #< Irá exibir os valores: "Samuel", "M", "26".
for k, v in pessoas.items(): #>Elimina "{[()]}".
    print(f"{k} = {v}") #> Irá exibur o dicionário completo e personalizado.
#del pessoas["sexo"] #< Apaga o índice e o valor: "sexo".
#pessoas["nome"] = "Daniel" #< O nome "Leandro" substitui o "Samuel". 

#===========DICIONÁRIO DENTRO DE UMA LISTA:==========================================================

brasil = []
estado1 = {"uf": "Rio de janeiro", "sigla": "RJ"}
estado2 = {"uf": "São Paulo", "sigla": "SP"}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[0]) #< Exibe os dados do Rio de Janeiro
print(brasil[1]) #< Exibe os dados do São Paulo.
print(brasil[0]["uf"]) #< Exibe apenas: "Rio de janeiro"
print(brasil[1]["uf"]) #< Exibe apenas "São Paulo"
print(brasil[1]["sigla"]) #< Exibe apenas "SP"

#===========ADICIONANDO DADOS:========================================
	
estado = dict()
brasil = list()
for c in range(0, 3):
    estado["uf"] = str(input(f"😎Unidade federativa[{c+1}/3]:\n>>>"))
    estado["sigla"] = str(input(f"😎Sua sigla[{c+1}/3]:\n>>>"))
    brasil.append(estado.copy()) #>Enquanto nas tuplas e listas se usa "[:]" para fazer cópia, no dicionário se usa "copy()"
print(brasil)
for e in brasil:
    for k, v in e.items():
        print(f"⭐O campo {k} tem valor {v}")
    for v in e.values():
        print(v, end=" ")
    print()
    
    
    
