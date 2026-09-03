('''Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while.''')


num = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razao: '))

contador = 1
termo = num

while contador <= 10:
    print(f"{termo}", end=' -> ')

    termo += razao
    contador += 1

print('FIM!')