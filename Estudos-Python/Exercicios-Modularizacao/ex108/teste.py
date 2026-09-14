('''Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro()
e metade(). Faca também um programa que importe esse módulo e use algumas dessas funções.''')

from ex108 import moeda

preço = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.monetario(preço)} é {moeda.monetario(moeda.metade(preço))}')
print(f'O dobro de {moeda.monetario(preço)} é {moeda.monetario(moeda.dobro(preço))}')
print(f'Aumentando 10%, temos {moeda.monetario(moeda.aumentar(preço, 10))}')