totmaior = totmenor = 0
teste = []
teste.append('Gustavo')
teste.append(26)
galera = []
galera2 = []
dado = []
galera.append(teste[:])
teste [0] = ('Maria')
teste [1] = 22
galera.append(teste[:])
print(galera)
print('-'* 40)

galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera)
print(galera [2][1])
print(galera[0][0])
print(galera[0][1])
#como fazer uma lista dessas estruturas que estão dentro da variavel galera:
galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for p in galera:
    print(p) #aqui posso ir alterando o número para ir extraindo os dados que me interessam
    print(f'{p[0]} tem {p[1]} anos')

#pegando dados de mais de uma pessoa, ou, com entrada do próprio usuário.
for c in range (0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera2.append(dado[:])
    dado.clear()
print(galera2)

#exemplo mostrando pessoas que tenham mais de 20 anos.
for p in galera2:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmaior +=1
    else:
        print(f'{p[0]} é menor de idade.')
        totmenor +=1
print(f'Temos {totmaior} maiores e {totmenor} menores de idade')