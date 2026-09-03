('''Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e
quantas mulheres têm menos de 20 anos.''')

from time import sleep
#Qual informação entra?
homem_mais_velho = ''
idade_homem_velho = 0
menos_20 = 0
soma = 0

#O que acontece na repetição?
for pessoa in range(1, 5):
    nome = str(input(f'Qual o nome da {pessoa}ª pessoa? '))
    idade = int(input(f'Qual a idade: '))
    sexo = str(input(f'Qual é o sexo? [M/F]: ')).upper().strip()

    soma += idade

    if sexo == 'M':
        if idade > idade_homem_velho:
            homem_mais_velho = nome
            idade_homem_velho = idade

    if sexo == 'F' and idade < 20:
        menos_20 += 1

media = soma / 4

#O que sai?
print('\nAnalisando o grupo...\n')
sleep(1.2)

if homem_mais_velho == '':
    print('Nenhum homem cadastrado.')
else:
    print(f'O homem mais velho tem {idade_homem_velho} anos e seu nome é {homem_mais_velho}.')

print(f'Quantidade de mulheres com menos de 20 anos: {menos_20}')
print(f'Média de idade do grupo: {media}')

