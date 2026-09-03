('''Exercício Python 47: Crie um programa que mostre na tela todos
 os números pares que estão no intervalo entre 1 e 50.''')

#Abertura do programa
('''print(Bem vindo ao contador de números pares!
Aqui você descobrirá quais os números pares entre 1 e 50).

#Estrutura do contador de números pares
for num in range(1, 51):
    if num % 2 == 0:
        print(f'O número {num} é par.', end=' ')
else:
    print(f'\nAnalise finalizada!')''')

for n in range(2, 51, 2):
    print(n, end=' ')
print('Acabou!')
