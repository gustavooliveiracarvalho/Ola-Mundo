resp = 'S'
soma = quant = media = maior = menor = 0

while resp == 'S':
    num = int(input('Digite um número: '))

    soma += num
    quant += 1

#A lógica por trás do maior e menor foi: eu tenho zero números, quem é o maior? Nenhum!
#Agora eu tenho 1 número (5). Quem é o maior e o menor? O próprio 5, porque só tem ele.
#Dessa forma, enquanto a quantidade for 1 (primeiro número informado), esse número será o maior e menor.
#Quando for inserido o segundo número, ai o "if" dentro do "else" compara o número atual com o maior e menor encontrado até agora.
#E que váriavél controla isso? O contador que ta com nome "quant", ela armazena o valor a cada rodada.
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]

media = soma / quant
print(f'Você digitou {quant} números e a média foi {media:.2f}.')
print(f'O maior valor foi {maior} e o menor foi {menor}.')
