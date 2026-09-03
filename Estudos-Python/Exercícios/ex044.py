('''Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal 

– 3x ou mais no cartão: 20% de juros''')


print(f'{" LOJAS CARVALHO ":=^40}')

compra = float(input('Preço das compras: R$ '))
print('''FORMAS DE PAGAMENTO
[1] - à vista dinheiro/cheque.
[2] - à vista no cartão
[3] - 2x no cartão.
[4] - 3x ou mais no cartão.''')

opcao = int(input('Qual a opção?'))

if opcao == 1:
    total = compra - (compra * 10 / 100)
elif opcao == 2:
    total = compra - (compra * 5 / 100)
elif opcao == 3:
    total = compra
    print(f'Sua compra será parcelada em 2x de R${total/2:.2f} SEM JUROS')
elif opcao == 4:
    parcelas3x = int(input('Quantas parcelas? '))
    total = compra + (compra * 20 / 100)
    print(f'Sua compra será parcelada em {parcelas3x}x de R${total/parcelas3x:.2f} COM JUROS.')
else:
    print('Opção de pagamento inválida. Tente novamente!')
    total = compra

print(f'Sua compra de R${compra} vai custar R${total:.2f}.')