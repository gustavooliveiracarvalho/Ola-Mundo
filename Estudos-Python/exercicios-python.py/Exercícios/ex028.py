'''Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número
 inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número
escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.'''

from random import randint
from time import sleep

escolhido = randint(0, 5) #Faz o computador "PENSAR".

print('-=-' * 20)
print('Vou pensar em um número de 0 a 5. TENTE ADIVINHAR!')
print('-=-' * 20)

numero = int(input('Advinhe qual número o computador escolheu de 0 a 5: '))#USUÁRIO TENTA ADIVINHAR.

print('PROCESSANDO...')
sleep(3)

if numero == escolhido:
    print('Você acertou! Parabéns Mãe Dináh, você me venceu.')
else:
    print(f'Errado! o número escolhido foi {escolhido}.')
