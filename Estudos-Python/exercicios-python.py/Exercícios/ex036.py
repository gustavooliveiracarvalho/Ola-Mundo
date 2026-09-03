'''Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário
para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e
 em quantos anos ele vai pagar.
 A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.'''

from time import sleep
cores = {'azul':'\033[0;34m',
         'vermelho': '\033[1;31m',
         'verde': '\033[1;32m',
         'amarelo': '\033[1;33m',
         'limpa': '\033[m'}

valor_casa = float(input(f"{cores['azul']}Qual o valor da casa?{cores['limpa']} R$"))
salario = float(input(f"{cores['azul']}Qual o seu salário?{cores['limpa']} R$"))
anos = int(input(f"{cores['azul']}Em quantos anos deseja pagar?{cores['limpa']} R$"))

if anos <= 0 or salario <= 0 or valor_casa <= 0:
    print(f"{cores['vermelho']}Quantidade inválida. Digite novamente!")

else:
    print(f"{cores['amarelo']}Aguarde! Estamos analisando sua solicitação...")
    sleep(2)

    prestacao = valor_casa / (anos * 12)

    if prestacao > salario * 30 / 100:
        print(f"{cores['vermelho']}Empréstimo negado! A prestação é maior que 30% do seu salário.")
        print(f"{cores['azul']}Salário atual:{cores['limpa']} R${salario:.3f} / {cores['azul']}prestação: {cores['limpa']}R${prestacao:.3f}")
    else:
        print(f"{cores['verde']}Empréstimo aprovado! A prestação é menor que 30% do seu salário.")
        print(f"{cores['azul']}Sua prestação ficará em:{cores['limpa']} R${prestacao:.3f}")
