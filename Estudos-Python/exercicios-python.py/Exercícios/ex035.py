'''Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas
 e diga ao usuário se elas podem ou não formar um triângulo.'''

cores = {'verde':'\033[1;32m',
         'azul':'\033[1;34m',
         'amarelo':'\033[1;33m',
         'vermelho':'\033[1;31m'}

print(f"{cores['amarelo']}-=-" * 20)
print(f"{cores['verde']}Analisador de Triângulos")
print(f"{cores['amarelo']}-=-" * 20)

r1 = float(input(f"{cores['azul']}Digite o valor da primeira reta: "))
r2 = float(input(f"{cores['azul']}Digite o valor da segunda reta: "))
r3 = float(input(f"{cores['azul']}Digite o valor da terceira reta: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(f"{cores['verde']}Os segmentos acima podem formar um triângulo!")
else:
    print(f"{cores['vermelho']}Os segmentos acima não podem formar um triângulo!")

