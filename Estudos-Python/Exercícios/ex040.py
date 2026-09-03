#Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:

#– Média abaixo de 5.0: REPROVADO

#– Média entre 5.0 e 6.9: RECUPERAÇÃO

#– Média 7.0 ou superior: APROVADO

cores = {'vermelho':'\033[1;31m',
         'verde':'\033[1;32m',
         'amarelo':'\033[1;33m'}

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2

if media >= 7:
    print(f'Tirando {n1:.1f} e {n2:.1f}, a média do aluno é {media}.')
    print (f"{cores['verde']}O aluno está APROVADO.\033[m")
elif media < 5:
    print(f'Tirando {n1:.1f} e {n2:.1f}, a média do aluno é {media}')
    print(f"{cores['vermelho']}O aluno está REPROVADO.\033[m")
elif 7 > media >= 5:
    print(f'Tirando {n1} e {n2}, a media do aluno é {media}')
    print(f"{cores['amarelo']}O aluno está de RECUPERAÇÃO")