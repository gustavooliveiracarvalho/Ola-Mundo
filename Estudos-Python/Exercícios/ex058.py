('''Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” 
em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, 
mostrando no final quantos palpites foram necessários para vencer.''')

from random import randint
from time import sleep

computador = randint(0, 5)  # Faz o computador "PENSAR".

print('-=-' * 20)
print('O computador está pensando em um número de 0 a 5.')
print('-=-' * 20)
sleep(1)

print('PROCESSANDO...')
sleep(1.1)

print('Você consegue advinhar?')

palpites = 0
acertou = False

while not acertou:
    jogador = int(input('Qual é seu palpite: '))
    palpites += 1

    if jogador == computador:
        acertou = True
    else:
        if jogador > computador:
            print('Menos... Tente mais uma vez!')
        elif jogador < computador:
            print('Mais... Tente mais uma vez!')

print(f'Você acertou! Parabéns Mãe Dináh, você me venceu.')
print(f'Número de tentativas para acertar: {palpites}')