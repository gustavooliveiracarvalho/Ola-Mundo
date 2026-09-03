#Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#– O primeiro valor é maior
#– O segundo valor é maior
#– Não existe valor maior, os dois são iguais"

print('-=-' * 20)
print('Digite dois números e descubra o maior:')
print('-=-' * 20)

num = float(input('Primeiro número: '))
num2 = float(input('Segundo número: '))

if num > num2:
    print(f'{num} é maior que o {num2}')
elif num < num2:
    print(f'{num2} é maior que o {num}')
else:
    print('Os dois valores são IGUAIS.')
