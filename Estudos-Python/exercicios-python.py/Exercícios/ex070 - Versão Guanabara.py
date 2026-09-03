tot_gasto = produtos_mais_de1000 = menor_preco = quantidade_produtos = 0
produto_mais_barato = ' '

while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço do produto: R$ '))

    if preco > 1000:
        produtos_mais_de1000 += 1

    quantidade_produtos += 1

    if quantidade_produtos == 1 or preco < menor_preco:
        menor_preco = preco
        produto_mais_barato = produto

    tot_gasto += preco

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]')).upper().strip()[0]

    if continuar == 'N':
        break

print(f'O total da compra foi R${tot_gasto:.2f}.')
print(f'Temos {produtos_mais_de1000} produtos que custam mais de R$1000.00.')
print(f'O produto mais barato foi: {produto_mais_barato}, que custa R${menor_preco:.2f}.')