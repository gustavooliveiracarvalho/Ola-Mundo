('''Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, 
já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.''')

lista = []

for c in range(0, 5):
#pede número
    valor = int(input('Digite um valor: '))
    achou = False
#analisa onde ele entra e adiciona na posição correta
    for c, v in enumerate(lista):
        if valor < v:
            lista.insert(c, valor)
            achou = True
            break
    if achou == False:
        lista.append(valor)
#entrega a lista em ordem
print(lista)