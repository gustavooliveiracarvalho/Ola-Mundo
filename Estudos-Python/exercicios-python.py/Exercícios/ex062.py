('''Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
 O programa encerrará quando ele disser que quer mostrar 0 termos.''')

#Variáveis que recebem os principais dados para calcular uma PA (Progressão Aritimética)
termo = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razão: '))

#Variável que vai controlar o programa inteiro, ela armazena a quantidade de vezes que o usuário solicitou um termo.
quantidade = 10

#Variável que controla a soma da quantidade de termos que o usuário pediu para ver.
total_mostrados = 0

#Laço principal, ele controla os 10 primeiros termos que serão mostrados e a cada nova atualização, ele controla a quantidade de termos contados.
while quantidade != 0:

#Variável que conta quantos termos fora mostrados.
    mostrados = 0

#Laço que controla a quantidade de termos solicitados com a quantidade de termos mostrados.
    while mostrados < quantidade:
        
#Bloco que realiza o cálculo da PA a cada nova solicitação do usuário e a soma de termos solicitados pelo usuário.
        print(f"{termo} ->", end = ' ')

        termo += razao
        mostrados += 1
        total_mostrados += 1

    print('Pausa')
#Váriavel que atualiza o a quantidade de termos que serão mostrados na proxima rodada do laço.
    quantidade = int(input('\nQuantos termos você deseja mostrar a mais: '))

#Finalização do programa e exibição do valor armazenado na variável que controla o total de termos mostrados.
print('\nContagem de termos finalizada.')
print(f'Você verificou {total_mostrados} termos no total.')