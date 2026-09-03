('''Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes''')


from time import sleep

cor = {'azul': '\033[34m',
         'vermelho': '\033[31m',
         'amarelo': '\033[33m',
       'verde': '\033[32m',
       'limpa': '\033[m'
}

a = float(input(f"{cor['azul']}Primeiro segmento{cor['limpa']}: "))
b = float(input(f"{cor['azul']}Segundo segmento{cor['limpa']}: "))
c = float(input(f"{cor['azul']}Terceiro segmento{cor['limpa']}: "))

if a + b > c and a + c > b and b + c > a:
    print(f"{cor['verde']}É possível formar um triângulo!{cor['limpa']}")
    print(f"Verificando tipo...")
    sleep(1.5)
    if a == b == c:
        print(f"{cor['azul']}Os segmentos podem formar um triângulo\033[m {cor['amarelo']}EQUILÁTERO{cor['limpa']}.")
    elif a == b or a == c or b == c:
        print(f"{cor['azul']}Os segmentos podem formar um triângulo\033[m {cor['amarelo']}ISÓSCELES{cor['limpa']}.")
    else:
        print(f"{cor['azul']}Os segmentos podem formar um triângulo\033[m {cor['amarelo']}ESCALENO{cor['limpa']}.")
else:
    print(f"{cor['vermelho']}Não é possível formar um triângulo! Informe valores válidos{cor['limpa']}.")




