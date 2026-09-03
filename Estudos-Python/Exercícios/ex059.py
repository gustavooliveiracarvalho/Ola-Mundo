('''Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.''')

#Ler dois valores
valores = []

for info0 in range(1, 3):
    numero = int(input(f'Informe o {info0}º valor: '))
    valores.append(numero)

while True:

    print('''\nMENU')
    [ 1 ] somar')
    [ 2 ] multiplicar')
    [ 3 ] maior')
    [ 4 ] novos números')
    [ 5 ] sair do programa''')

    opcao = int(input('Escolha uma opção: '))

    if opcao == 1:
        soma = valores[0] + valores[1]
        print(f'Resultado da soma entre {valores[0]} e {valores[1]}: {soma}')

    elif opcao == 2:
        multiplicar = valores[0] * valores[1]
        print(f'O resultado da multiplicação entre {valores[0]} e {valores[1]}: {multiplicar}')

    elif opcao == 3:
        if valores[0] > valores[1]:
            maior = valores[0]
        else:
            maior = valores[1]
        print(f'O maior entre {valores[0]} e {valores[1]}: {maior}')

    elif opcao == 4:
        valores = []

        for info00 in range(1, 3):
            numero00 = int(input(f'Digite o {info00}º valor: '))
            valores.append(numero00)
    elif opcao == 5:
        print('Finalizando...')
        break
    else:
        print('Opção inválida! Informe uma opção válida.')