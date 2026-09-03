('''Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.''')

temp = []
princ = []
pesados = []
leves = []
pesos = []

while True:
    temp.append(str(input('Informe o nome do pessoa: ')))
    temp.append(float(input('Informe o peso do pessoa: ')))
    princ.append(temp[:])
    temp.clear()
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
for p in princ:
    pesos.append(p[1])
maior = max(pesos)
menor = min(pesos)
for p in princ:
    if p[1] == maior:
        pesados.append(p)
for p in princ:
    if p[1] == menor:
        leves.append(p)
print(f'Pessoas cadastradas {len(princ)}')
print(f'Pessoas mais pesadas {pesados}')
print(f'Pessoas mais leves {leves}')