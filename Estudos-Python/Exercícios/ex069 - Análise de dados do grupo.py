('''Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, 
o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.''')

#Qual informação entra?
homens_cadastrados = idade_mais_18 = menos_20 = 0

#O que acontece na repetição?
while True:
    print('CADASTRE UMA PESSOA')
    print('-' * 30)
    idade = int(input(f'Qual a idade: '))
    sexo = continuar = ' '

    while sexo not in "MF":
        sexo = str(input(f'Qual é o sexo? [M/F]: ')).upper().strip()

    if idade >= 18:
        idade_mais_18 += 1

    if sexo == "M":
        homens_cadastrados += 1

    if sexo == 'F' and idade < 20:
        menos_20 += 1

    while continuar not in "NS":
        continuar = str(input('Quer continuar? [S/N]')).upper().strip()

    if continuar == 'N':
        break

print(f'Total de pessoas com mais de 18 anos: {idade_mais_18}.')
print(f'Ao todo temos {homens_cadastrados} homens cadastrados.')
print(f'E temos {menos_20} mulheres com menos de 20 anos.')


