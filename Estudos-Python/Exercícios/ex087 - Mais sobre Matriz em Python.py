('''Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados
B) A soma dos valores da terceira coluna
C) O maior valor da segunda linha''')

#vou criar a matriz com 3 linhas e 3 colunas, para isso será utilizada sublistas, e cada sublista representa uma linha dentro da matriz, de forma que gere uma matriz 3x3.
matriz = [[0, 0, 0], 
          [0, 0, 0], 
          [0, 0, 0]]
#vou declarar variáveis para que possa fazer os cálculos e implementar as funcionalidades A, B e C.
spar = mai = scol = 0
#esse bloco é responsável por receber os dados e preencher a matriz com eles. Como ele funciona:
#para as linhas de 0 a 3 ele vai pegar os dados da 1 linha, percorrer as colunas de 1 a 3 e pegar os dados da 1 coluna, quando chegar ao final da contagem: 0, 1, 2, após isso, ele vai mudar de linha e pegar os dados da 2 linha, e assim por diante.
for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}], [{coluna}]: '))
print('-' * 30)
#esse bloco é responsável por apresentar a saída para o usuário com a formatação correta.
#ele pega dentro da lista "matriz" a linha e coluna e apresenta na tela com a formatação correta, por isso usei o "^5", pois ele centraliza o dado, 
#após isso, a variável "spar" = soma par, vai somar os valores que foram inseridos e validar se são pares.
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
        if matriz[linha][coluna] % 2 == 0:
            spar += matriz[linha][coluna]
    print()
print('-' * 30)
#esse print vai mostrar a soma de todos os valores pares inseridos.
print(f'A soma dos valores pares é {spar}.')
#esse for é responsável por somar os valores da terceira coluna e apresentar na tela. Ele pega a lista "matriz" e percorre as linhas de 0 a 3, e dentro de cada linha ele vai somar os valores da terceira coluna, ao final vai mostrar o valor para o usuário.
for linha in range (0, 3):
    scol += matriz[linha][2]
print(f'A soma dos valores da terceira coluna é {scol}.')
#esse "for" vai percorrer as colunas e verificar quem é o maior valor informado na segunda linha.
for coluna in range(0, 3):
    if coluna == 0:
        mai = matriz[1][coluna]
    elif matriz[1][coluna] > mai:
        mai = matriz[1][coluna]
print(f'O maior valor da segunda linha é {mai}.')