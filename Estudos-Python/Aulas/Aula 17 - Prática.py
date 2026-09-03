#Abaixo estou usando tudo que aprendemos na aula teórica. é uma demonstração do que cada comando pode fazer.
num = [2, 5, 9 , 1]
num[2] = 3
num.append(7)
num.sort()
num.sort(reverse=True)
num.insert(6, 4)
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4.')
print(num)
print(f'Essa lista tem {len(num)} elementos.')

print('-' * 50)
#Abaixo está demonstrado como eu posso fazer uma lista e printar o resultado para o usuário, sem receber esses dados pelo teclado do usuário.
valores = list()
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')

print('-' * 50)
#Uso o código abaixo para fazer uma lista usando as entradas que o usuário passa pelo teclado.
valores = list()

for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')

print('-' * 50)
#Como fazer uma cópia de uma lista?
#Nota.: se eu não fizer o procedimento abaixo, eu estarei ligando uma lista na outra, ou seja, o que eu altero em uma, altera na outra.
#O procedimento abaixo é feito para que quando eu editar a Lista B eu não altere a lista A.
a = [2,3,4,7]
b = a[:] #se eu tirar esse [:] a lista "A" ficará interligada com a "B" e ai tudo que altera em uma, altera na outra.
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')