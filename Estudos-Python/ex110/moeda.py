#Módulo usado para construir minha função que será usada no exercício 107.

def aumentar(preco=0,taxa=0, formato=False):
    """
    -> Calcula o aumento de um determinado preco.
    :param preco: Valor a ser aumentado.
    :param taxa: Taxa de aumento.
    :param formato: mostra ou não o sinal monetário do preco.
    :return: Retorna o preco com o aumento.
    """
    res = preco + (preco * taxa/100)
    return res if formato == False else monetario(res)


def diminuir(preco=0,taxa=0, formato=False):
    """
    -> Calcula o desconto de um determinado preco.
    :param preco: Valor a ser diminuido.
    :param taxa: Taxa de desconto.
    :param formato: mostra ou nao o sinal monetário do preco.
    :return: Retorna o preco com o desconto.
    """
    res = preco - (preco * taxa/100)
    return res if formato == False else monetario(res)


def dobro(preco=0, formato=False):
    """
    -> Calcula o dobro de um determinado preco.
    :param preco: Valor a ser dobrado.
    :param formato: mostra ou nao o sinal monetário do preco.
    :return: Retorna o preco dobrado.
    """
    res = preco * 2
    return res if formato == False else monetario(res)


def metade(preco=0, formato=False):
    """
    -> Calcula a metade de um determinado preco.
    :param preco: Valor a ser dividido pela metade.
    :param formato: mostra ou nao o sinal monetário do preco.
    :return: Retorna o preco dividido pela metade.
    """
    res = preco / 2
    return res if formato == False else monetario(res)


def monetario(preco=0, sinal='R$'):
    """
    -> Formata um preco para o formato brasileiro.
    :param preco: Valor a ser formatado.
    :param sinal: Sinal que acompanha o preco.
    :return: Retorna o preco formatado.
    """
    return f'{sinal}{preco:>.2f}'.replace('.',',')

def resumo(preco=0, taxaa=10, taxar=5):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{monetario(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(preco, taxaa, True)}')
    print(f'{taxar}% de redução: \t{diminuir(preco, taxar, True)}')
    print('-'*30)