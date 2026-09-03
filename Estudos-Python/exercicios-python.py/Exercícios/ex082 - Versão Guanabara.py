lista_geral = []
lista_par = []
lista_impar = []
while True:
    valor = int(input('Digite um valor inteiro: '))
    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break
for i, v in enumerate(lista_geral):
    if v % 2 == 0:
        lista_impar.append(v)
    else:
        lista_impar.append(v)
print(f'Lista completa: {lista_geral}')
print(f'Números pares dentro da lista: {lista_par}')
print(f'Números ímpares dentro da lista: {lista_impar}')