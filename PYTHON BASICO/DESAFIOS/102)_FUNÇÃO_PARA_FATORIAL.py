#==========FUNÇÃO PARA FATORIAL:======================================

def fatorial(n, show=False):
    """
    ⭐CALCULE O FATORIAL DE UM NÚMERO:
    :param n: O número a ser calculado;
    :param show: (opcional) mostrar ou não o cálculo;
    :return: O valor do fatorial de um número n.
    """
    
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end="")
            if c > 1:
                print(" × ",end="")
            else:
                print(" = ",end="")
        f *= c
    return f

print(fatorial(5, show=True))
help(fatorial)