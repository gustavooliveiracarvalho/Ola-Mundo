'''Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:

– O nome com todas as letras maiúsculas e minúsculas.

– Quantas letras ao todo (sem considerar espaços).

– Quantas letras tem o primeiro nome.'''
from shlex import split

'''frase = str(input('Digite seu nome completo: ')).strip()

print(f'\nMaiúsculo: {frase.upper()}')
print(f'Minúscula: {frase.lower()}')

frase_sem_espaco = frase.replace(' ', '')
print(f'Quantidade de letras sem espaço: {len(frase_sem_espaco)}')

primeiro_nome = frase.split()[0]
print(f'Quantidade de letras do primeiro nome: {len(primeiro_nome)}') 

Fiz o código dessa forma acima, mas comparando o Guanabara com o chat GPT, pensei em
mesclar as soluções e meu código ficou assim:'''

nome = str(input('Digite seu nome completo: ')).strip()

print(f'Maiúsculo: {nome.upper()}')
print(f'Minúsculo: {nome.lower()}')
print(f'Total de letras: {len(nome) - nome.count(" ")}')
print(f'Total de letras primeiro nome: {len(nome.split()[0])}')







