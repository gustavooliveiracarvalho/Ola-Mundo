('''''Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
Caso o número já exista lá dentro, ele não será adicionado. 
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.''')

lista = []

while True:
    valor = int(input('Digite um valor: '))

    if valor in lista:
        print('Valor duplicado! Não vou adicionar...')
    else:
        lista.append(valor)
        print('Valor adicionado com sucesso!')

    continuar = str(input('Quer continuar? [S/N]')).upper().strip()
    if continuar in 'N':
        break

print('-' * 30)
lista.sort()
print(f'Você digitou os valores: {lista}.')