('''Exercício Python 52: Faça um programa que leia um número inteiro
 e diga se ele é ou não um número primo.''')

num = int(input('Digite um número inteiro: '))

cont = 0

for c in range(1, num + 1):
    if num % c == 0:
        print('\033[34m', end=' ')
        cont += 1
    else:
        print('\033[31m', end=' ')
    print(f'{c}', end= ' ')
print(f'\nO número {num} foi divisível {cont} vezes.')
if cont == 2:
    print('Por isso ele é PRIMO.')
else:
    print('\033[m', end=' ')
    print('Por isso ele NÃO é PRIMO.')

