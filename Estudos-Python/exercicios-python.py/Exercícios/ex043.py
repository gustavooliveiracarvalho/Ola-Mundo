('''Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, 
calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso

– Entre 18,5 e 25: Peso Ideal

– 25 até 30: Sobrepeso

– 30 até 40: Obesidade

– Acima de 40: Obesidade Mórbida''')

#Biblioteca
from time import sleep

#Entrada de dados
peso = float(input('Digite o seu peso: (Kg) '))
altura = float(input('Digite sua altura: (m) '))

print('CALCULANDO IMC...')
sleep(1.2)

#Cálculo
imc = peso / (altura ** 2)

#Regras
if imc < 18.5:
    print('Abaixo do peso')
elif imc < 25:
    print('Peso Ideal')
elif imc < 30:
    print('Sobrepseso')
elif imc < 40:
    print('Obesidade')
elif imc < 40:
    print('Obesidade Mórbica, Cuidado!')

#Fim do programa
print('-=-' * 20)
print('Obrigado! Você descobriu seu IMC.')
