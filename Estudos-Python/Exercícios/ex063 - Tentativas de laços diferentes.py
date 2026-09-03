('''Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos 
de uma Sequência de Fibonacci. Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8 mais = int(input('Quantos termos deseja ver: '))''')

cores = {'azul':'\033[0;34m',
         'vermelho': '\033[1;31m',
         'verde': '\033[1;32m',
         'amarelo': '\033[1;33m',
         'limpa': '\033[m'}

n = int(input('Digite a quantidade de termos que deseja ver: '))

t1 = 0
t2 = 1

mais = n
termo_total = 0

while mais != 0:

    mostrados = 0

    while mostrados < mais:

        t3 = t1 + t2
        print(f"{t3} -> ", end=' ')

        t1 = t2
        t2 = t3

        mostrados += 1
        termo_total += 1

    print('Pausa\n', end= ' ')

    mais = int(input(f'''\nQuantos termos deseja ver a mais? 
{cores['vermelho']}AVISO: {cores['limpa']}caso deseje encerrar o programa, digite: 0.\n'''))

print(f'Contagem finalizada. Você verificou {termo_total} termos.')


