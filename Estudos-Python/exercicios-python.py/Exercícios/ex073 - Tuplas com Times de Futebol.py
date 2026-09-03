('''Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, 
na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da Chapecoense.''')

times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio',
         'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
         'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia',
         'São Paulo', 'Fluminense', 'Sport Recife',
         'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')

print(f'Lista de times: {times}')
print('-' * 30)

print(f'Os 5 primeiros são {times[0:5]}')
print('-' * 30)

print(f'Os 4 últimos são {times[-4:]}')
print('-' * 30)

print(f'Times em ordem alfabética {sorted(times)}')
print('-' * 30)

print(f'Colocação da Chapecoense: {times.index("Chapecoense")+1}ª posição.')
