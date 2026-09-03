('''Exercício Python 66: Crie um programa que leia números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, 
que é a condição de parada. No final, 
mostre quantos números foram digitados e 
qual foi a soma entre elas (desconsiderando o flag).''')

total_digitados = soma_total = 0

while True:
    num= int(input('Digite um número: '))

    if num == 999:
        break

    total_digitados += 1
    soma_total += num

print(f'Você digitou {total_digitados} números e a soma entre eles foi {soma_total}')
