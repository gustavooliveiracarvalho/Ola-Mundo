from random import choice

('''Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.''')

from random import randint
from time import sleep

print('''SUAS OPÇÕES:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')

opcao = int(input('Qual é a sua jogada?' ))

if opcao >= 3:
    print('Opção inválida! Digite uma das opções acima.')
else:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')
    sleep(1)

    lista = ['PEDRA', 'PAPEL', 'TESOURA']

    computador = randint(0, 2)

    if opcao == computador:
        print('=' * 40)
        print('EMPATE')
        print('=' * 40)
        print(f'O computador escolheu {lista[computador]}')
        print(f'O jogador escolheu {lista[opcao]}')
    elif (opcao == 0 and computador == 2) or \
            (opcao ==  2 and computador == 1) or \
                (opcao == 1 and computador == 0):
        print('=' * 40)
        print('VOCÊ VENCEU!!!')
        print('=' * 40)
        print(f'O computador escolheu {lista[computador]}.')
        print(f'O jogador escolheu {lista[opcao]}.')
    else:
        print('=' * 40)
        print('VOCÊ PERDEU!!!')
        print('=' * 40)
        print(f'O computador escolheu {lista[computador]}.')
        print(f'O jogador escolheu {lista[opcao]}.')