('''Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:

5! = 5 x 4 x 3 x 2 x 1 = 120''')

numero = int(input('Digite o número que deseja saber o fatorial: '))

fatorial = 1
contador = numero

for c in range(1, numero + 1):
    print(contador, end=' ')
    fatorial *= contador
    print(' x ' if contador > 1 else f' = {fatorial}', end=' ')
    contador -= 1

print(f'\nO fatorial de {numero} é {fatorial}.')
