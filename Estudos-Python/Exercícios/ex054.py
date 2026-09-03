('''Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final,
 mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores''')

from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0

for pess in range(1, 4):
    nasc = int(input(f'Qual a idade da {pess}ª pessoa: '))
    idade = atual - nasc
    if idade >= 18:
        totmaior += 1
    else:
        totmenor += 1
print(f'Ao todo {totmaior} pessoas são maiores de idade', end=' ')
print(f'e {totmenor} são pessoas menores de idade.')







