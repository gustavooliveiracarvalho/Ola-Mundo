('''Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.''')

lista_geral = []
lista_par = []
lista_impar = []
while True:
    valor = int(input('Digite um valor inteiro: '))
    lista_geral.append(valor)
    if valor % 2 == 0:
        lista_par.append(valor)
    else:
        lista_impar.append(valor)
    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break
lista_par.sort()
lista_impar.sort()
lista_geral.sort()
print(f'Lista completa: {lista_geral}')
print(f'Números pares dentro da lista: {lista_par}')
print(f'Números ímpares dentro da lista: {lista_impar}')
