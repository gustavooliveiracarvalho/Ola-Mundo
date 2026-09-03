('''Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
 No final, mostre os 10 primeiros termos dessa progressão.''')

num = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razao: '))
decimo = num + (10 - 1) * razao

for c in range(num, decimo + razao, razao):
    print(f"{c}", end='-> ')
print('ACABOU')