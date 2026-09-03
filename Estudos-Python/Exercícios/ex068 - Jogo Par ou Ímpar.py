('''Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. 
O jogo só será interrompido quando o jogador perder, 
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.''')

from random import randint

vitorias = soma = par_impar_resultado = 0

while True:
    numero = int(input('Diga um valor: '))
    par_impar = str(input('Par ou Ímpar? [P/I]: ')).upper().strip()

    computador = randint(0, 10)

    soma = numero + computador

    if soma % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'IMPAR'

    if (soma % 2 == 0 and par_impar == 'P') or (soma % 2 != 0 and par_impar == 'I'):
        print(f'Você venceu!')
        print('-' * 30)
        print(f'Você jogou {numero} e o computador escolheu {computador}. Total de {soma} é {resultado}.')
        vitorias += 1

    else:
        print(f'Você perdeu!')
        print('-' * 30)
        print(f'Você jogou {numero} e o computador escolheu {computador}. Total de {soma} é {resultado}.')
        break

print('-' * 30)
print(f'GAME OVER! Você venceu {vitorias} vezes.')
