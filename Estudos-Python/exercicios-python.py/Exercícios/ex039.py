('''Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de
se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo 
que falta ou que passou do prazo.''')

from datetime import date
nascimento = int(input('Digite o ano em que nasceu: '))
sexo = str(input('Qual o seu sexo [M/F]? ')).strip().lower()
idade = date.today().year - nascimento
ano_18 = date.today().year + (18 - idade)

if sexo in ['f', 'feminino','fem']:
    print(f'O alistamento é só para o sexo Masculino.')
else:
    if idade > 18:
        print(f'Quem nasceu em {nascimento} tem {idade} anos em {date.today().year}.')
        print(f'Você já deveria ter se alistado há {date.today().year - ano_18} anos.')
        print(f'Seu alistamento foi em {ano_18}.')
    elif idade == 18:
        print(f'Quem nasceu em {nascimento} terá {idade} anos em {date.today().year}.')
        print(f'Você deve se alistar em {date.today().year}, o ano que completa 18 anos.')
        print(f'Seu alistamento será em {ano_18}.')
    elif idade < 18:
        saldo = 18 - idade
        print(f'Quem nasceu em {nascimento} tem {idade} anos em {date.today().year}.')
        print(f'Ainda faltam {saldo} anos para o seu alistamento.')
        print(f'Seu alistamento será no ano de {date.today().year + saldo}.')
