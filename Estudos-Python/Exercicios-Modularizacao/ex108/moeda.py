#Módulo usado para construir minha função que será usada no exercício 107.

def aumentar(preco=0,taxa=0):
    res = preco + (preco * taxa/100)
    return res
def diminuir(preco=0,taxa=0):
    res = preco - (preco * taxa/100)
    return res
def dobro(preco=0):
    res = preco * 2
    return res
def metade(preco=0):
    res = preco / 2
    return res
def monetario(preco=0, sinal='R$'):
    return f'{sinal}{preco:>.2f}'.replace('.',',')