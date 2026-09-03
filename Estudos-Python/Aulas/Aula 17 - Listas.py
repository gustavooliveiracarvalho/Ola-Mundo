#Nessa aula, vamos aprender o que são LISTAS e como utilizar listas em Python.
#As listas são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuais.

#VARIÁVEIS COMPOSTAS - LISTAS

#Diferente das tuplas, as listas aceitam a modificação: acréscimo ou redução de elementos, após ter definido ela.

#COMANDOS NAS LISTAS
# .append() serve para adicionar um dado dentro da minha lista. Ex.: lanche.append('hamburguer')
#Ele vai adicionar o novo dado no final da minha lista, o insert é usado para adicionar em qualquer lugar da lista.

# .insert(0,'novo dado') serve para inserir um dado em qualquer posição da lista. Ex.: lanche.insert(0,'cachorro quente')
#Eu insiro o cachorro quente na posição 0 e coloco o hambúrguer, que antes estava na posição [0], na posição [1].

# del serve para deletar um dado na lista. Ex.: dellanche(3)

# pop('dado que quero remover') usado para eliminar o último elemento, mas posso passar como parametro indice a posição que quero eliminar. Ex.: lanche.pop(3)
#O POP ELIMINA PELO INDICE E NÃO PELO DADO QUE EU QUERO TIRAR, PRECISO SELECIONAR O INDICE CERTO.

# remove('dado que quero remover'). Aqui você não indica o indice que quer eliminar (0,1,2,3...), vocÊ indica o valor ('pizza', 'carro amarelo'...) Ex.: lanche.remove('pizza')

#REMOVENDO USANDO "IF"
#Se eu quiser remover um elemento que não sei se está na minha lista?
#Seu eu tentar remover usando os termos anteriores, vai dar um erro. Logo, eu preciso validar se o dado está na lista para remover.

#FORMA CORRETA DE FAZER:
#if 'pizza' in lanche:
#    lanche.remove('pizza')

#CRIANDO LISTAS ATRAVÉS DE RANGES:
# valores = list(range(4,11))

#essa lista vai contar de 4 a 10: 45678910 e vai colocar um indice (que vai de 0 a 6).

#SE EU QUISER FORA DE ORDEM?
#Primeiro vou definir os valores que eu quero:
# valores = [8,2,5,4,9,3,0]

#Depois vou usar o sort para por em ordem, caso eu queira por em ordem:
# valores.sort() - esse comando vai ordenar e colocar: 0,2,3,4,5,8,9

#E SE EU QUISER INVERTER A ORDEM DE NOVO?
#Eu vou usar um parâmetro que é o "reverse":
# valores = [8,2,5,4,9,3,0]
# valores.sort(reverse = True) - vai ficar: [9,8,5,4,3,2,0]

#COMO SABER O TAMANHO DE UMA LISTA?
#Para descobrir o tamanho de uma lista usamos "len"
# valores = [8,2,5,4,9,3,0]
# len(valores) - ele vai contar começando em zero: [0,1,2,3,4,5,6,7]
# len será igual a 7.