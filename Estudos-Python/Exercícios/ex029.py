'''Exercício Python 29: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.'''
from time import sleep
velocidade = float(input('Qual a velocidade atual do carro?'))

multa = (velocidade - 80) * 7

print('PROCESSANDO...')
sleep(2)

if velocidade > 80:
    print(f'MULTADO! Você excedeu o limite permitido que é de 80Km/h.')
    print(f'Você deve pagar uma multa de R${multa:.2f}.')
    print('Tenha um bom dia! Dirija com segurança!')
else:
    print(f'Você está dentro do limite da via: {velocidade}km/h')
    print('Tenha um bom dia! Dirija com segurança!')

