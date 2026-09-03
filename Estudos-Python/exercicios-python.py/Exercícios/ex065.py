('''Exercício Python 65: Crie um programa que leia vários 
números inteiros pelo teclado. No final da execução, 
mostre a média entre todos os valores e qual foi o maior e o 
menor valores lidos. O programa deve perguntar ao usuário se ele 
quer ou não continuar a digitar valores.''')


continuar = total_solicitacoes = media = maior_valor = menor_valor = total_numeros = 0

while not continuar == 'N':
    num = int(input('Digite um número: '))
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

    total_solicitacoes += 1
    total_numeros += num
    media = total_numeros / total_solicitacoes

    menor_valor = num

    if num > maior_valor:
        maior_valor = num

    if menor_valor < maior_valor:
        menor_valor = num

print(f'''\nVocê digitou {total_solicitacoes} números e a média foi {media:.2f}.
O maior valor foi {maior_valor} e o menor {menor_valor}.''')