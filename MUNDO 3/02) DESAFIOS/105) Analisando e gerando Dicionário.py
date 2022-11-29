#==============ANALISANDO E GERANDO DICIONÁRIO:======================

def notas(*n, sit=False):
    """
    >FUNÇÃO PARA ANALISAR NOTAS:
    :param n: uma ou mais notas;
    :param sit: Se refere a situação;
    :return: Dicionário com várias informações.
    """
    
    r = dict()
    r["total"] = len(n)
    r["maior"] = max(n)
    r["menor"] = min(n)
    r["média"] = sum(n)/len(n)
    if sit:
        if r["média"] >= 7:
            r["situação"] = "BOA"
        elif r["média"] >= 5:
            r["situação"] = "RAZOÁVEL"
        else:
            r["situação"] = "RUIM"
    return r

resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
help(notas)