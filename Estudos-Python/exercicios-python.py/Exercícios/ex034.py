'''Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
 Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.'''

cores = {'verde':'\033[1;32m',
         'azul':'\033[1;34m',
         'amarelo':'\033[1;33m',
         'vermelho':'\033[1;31m'}

salario = float(input(f"{cores['azul']}Qual é o salário do funcionário?\033[m R$"))

if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)

print(f"{cores['vermelho']}Salário antigo: R${salario:.2f}\033[m / {cores['verde']}Salário novo: R${novo:.2f}")

