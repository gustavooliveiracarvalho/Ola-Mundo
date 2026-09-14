#Módulo usado para construir minha função que será usada no exercício 107.

def aumentar(preco=0,taxa=0, formato=False):
    res = preco + (preco * taxa/100)
    return res if formato == False else monetario(res)


def diminuir(preco=0,taxa=0, formato=False):
    res = preco - (preco * taxa/100)
    return res if formato == False else monetario(res)


def dobro(preco=0, formato=False):
    res = preco * 2
    return res if formato == False else monetario(res)


def metade(preco=0, formato=False):
    res = preco / 2
    return res if formato == False else monetario(res)


def monetario(preco=0, sinal='R$'):
    return f'{sinal}{preco:>.2f}'.replace('.',',')