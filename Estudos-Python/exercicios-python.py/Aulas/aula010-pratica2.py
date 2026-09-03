n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2

if m >= 6:
    print(f'Você foi aprovado com média: {m:.1f}')
else:
    print(f'Você foi reprovado com a média {m:.1f}')