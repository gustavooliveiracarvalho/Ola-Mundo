('''Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número
 que o usuário escolher, só que agora utilizando um laço for.''')

#Entrada de dados
num = int(input('Digite um número para ver a sua tabuada: '))

#Cálculo
for c in range(1, 11):
    print(f"{num} X {c} = {num*c}")
