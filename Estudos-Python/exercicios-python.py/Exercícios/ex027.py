'''Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa, mostrando
em seguida o primeiro e o último nome separadamente.'''

'''nome = str(input('Digite seu nome completo: ')).strip()

print('\nMuito prazer em te conhecer!')
print(f'Seu primeiro nome é {nome.split()[0]}')
print(f'Seu último nome é {nome.rsplit()[-1]}')'''

nome = str(input('Digite seu nome completo: ')).strip()

partes = nome.split()

print('\nMuito prazer em te conhecer')
print(f'Seu primeiro nome é {partes[0]}')
print(f'Seu último nome é {partes[-1]}')

