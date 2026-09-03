lanche = 'Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita'

#abaixo são vários exemplos de como fazer fatiamento, posso usar os vários tipos de acordo com a necessidade.
#tuplas são IMUTÁVEIS, eu não consigo substituir ou acrescentar novas informações numa Tupla já feita.
print(lanche)
print(lanche[1])
print(lanche[2])
print(lanche[3])
print(lanche[1:3])
print(lanche[-4])
print(lanche[:2])
print(lanche[-3:])

#Se eu usar for dentro dessa tupla, ele vai mostrar cada informação a cada contador do meu for. Esse formato não consegue mostrar a posição da informação dentro da tupla.
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi para caramba!')

#Outra forma de usar o for para fazer a mesma coisa do exemplo acima desse, porém, mostrando a posição do dado na Tupla.
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}, na posição {cont}')
print('-' * 30)
print('{:^30}'.format('EXEMPLO COM ENUMERATE'))

#Outra forma de usar o for, usando "enumerate" para mostrar a posição dos dados dentro da Tupla.
for psc, comida in enumerate(lanche):
    print(f'Eu vou comer {comida}, na posição {psc}')

#Outra forma de fazer Tupla é com "sorted", ele coloca os dados em ordem.
print(sorted(lanche))

#mostra a quantidade de dados que tem na minha tupla.
print(len(lanche))

print('-' * 30)
print('{:^30}'.format('EXEMPLO COM DUAS TUPLAS'))

#Se eu fizer uma variável e somar duas tuplas dentro dela, ela vai juntar os dois valores. E a ordem das variáveis afeta a forma como é feita a junção.
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c)
#Mostra a quantidade de dados dentro da variável
print(len(c))
#Mostra quantas vezes o elemento que eu escolhi, no caso o "5", aparece dentro da Tupla.
print(c.count(5))

#Mostra em que posição está o elemento que eu escolhi dentro da Tupla, no caso o "8". Ele pega sempre a primeira ocorrência (primeira vez que o número aparece).
print(c)
print(c.index(8))

#Se eu não quiser pegar a primeira ocorrência, essa maneira abaixo mostra em que posição está o número "2", contando até da posição "4", posso fazer isso de acordo com a
# posição que quero consultar, nesse caso tem um "2" na posição "3" e um "2" na posição "4". Eu escolhi o da posição "4".
print(c)
print(c.index(2, 4))

print('-' * 30)
print('{:^30}'.format('EXEMPLO COM PESSOA'))

pessoa = ('Gustavo', 26, 'M', 64.00)
print(pessoa)

#Uso "del" quando eu quero deletar uma Tupla ou qualquer outra coisa em Pyhton.
#Eu consigo deletar uma tupla por completo, mas não consigo deletar só um elemento dela. 
pessoa = ('Gustavo', 26, 'M', 64.00)
del(pessoa)
print(pessoa)