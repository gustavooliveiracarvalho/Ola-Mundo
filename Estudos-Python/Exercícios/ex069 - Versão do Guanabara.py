tot_18 = tot_homens = tot_mulher_20 = 0

while True:
    idade = int(input('Qual a sua idade? '))
    sexo = ' '

    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]

    if idade >= 18:
        tot_18 += 1

    if sexo == 'M':
        tot_homens += 1

    if sexo == 'F' and idade < 20:
        tot_mulher_20 += 1

    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]

    if resposta == 'N':
        break

print(f'Total de pessoas com mais de 18 anos: {tot_18}.')
print(f'Ao todo temos {tot_homens} homens cadastrados.')
print(f'E temos {tot_mulher_20} mulheres com menos de 20 anos.')
