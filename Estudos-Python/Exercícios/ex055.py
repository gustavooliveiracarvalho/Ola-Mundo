('''Exercício Python 55: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.''')

#O que entra?
menor_peso = 0
maior_peso = 0

#O que acontece a cada repetição?
for pessoa in range(1, 6):
    peso = float(input(f'Qual o peso da {pessoa}ª pessoa: '))

#O que precisa ser guardado?
    if pessoa == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso

#O que sai?
print(f'Menor peso: {menor_peso}Kg')
print(f'Maior peso: {maior_peso}Kg')
