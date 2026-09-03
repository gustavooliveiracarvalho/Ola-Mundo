from random import randint

vitoria = 0

while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '

    while tipo not in 'PpIi':
        tipo = str(input('Par ou Ímpar [P/I]: ')).strip().upper()[0]

    print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {total}')

    print(f'DEU PAR' if total % 2 == 0 else 'DEU IMPAR')

    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            vitoria += 1
        else:
            print('Você PERDEU!')
            break

    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente!')
print(f'GAME OVER! Você venceu {vitoria} vezes.')
