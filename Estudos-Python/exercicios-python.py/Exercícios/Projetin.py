#vou tentar criar um programa que interaja com meus compromissos estudantis
#ele vai perguntar o que estudei no dia e me mostrar o que eu fiz e o que eu deveria ter feio
#quero randomizar algumas frases para ir aparecendo como motivacional
#vou dedicar uma parte a coletar o tempo que fiquei em cada materia
from random import choice
from datetime import datetime
materias = []
tempo = 0
dia = datetime.now().weekday()
dias_semana = ('segunda-feira', 'terça-feira', 'quarta-feira',
               'quinta-feira', 'sexta-feira', 'sábado', 'domingo')
tmp_150min = 150
tmp_240min = 240
tmp_120min = 120
seg = ('Pyhton', 'Exercícios da aula', 'Inglês', 'Organizar anotações')
ter = ('Python', 'Escrever exercícios sem olhar', 'Git/Github', 'Inglês')
qua = ('Exercícios mais difíceis', 'Refatorar códigos antigos', 'Inglês', 'Revisão de erros da semana')
qui = ('Python', 'AWS', 'Inglês', 'Inglês', 'Git/Github')
sex = ('Projeto', 'Inglês')
sab = ('Resolver exercícios antigos sem consultar', 'Evoluir o projeto pessoal', 'Github')
dom = ('Revisar anotações', 'Corrigir exercícios que deram trabalho', 'Planejar a semana seguinte', 'Ler documentação ou artigo técnico em inglês')

while True:
    print('-'*40)
    print(f'{dias_semana[dia]}')
    print('''ACOMPANHE SEUS ESTUDOS!
    [1] - Ver o cronograma do dia.
    [2] - Ver minhas estatísticas.
    [3] - Encerrar o programa.''')
    print('-' *30)
    opcao = int(input('Qual a opção?'))
    if opcao == 3:
        break
    if opcao == 1 and dia == 0:
        print(seg)
    elif opcao == 1 and dia == 1:
        print(ter)
    elif opcao == 1 and dia == 2:
        print(qua)
    elif opcao == 1 and dia == 3:
        print(qui)
    elif opcao == 1 and dia == 4:
        print(sex)
    elif opcao  == 1 and dia == 5:
        print(sab)
    elif opcao == 1 and dia == 6:
        print(dom)
    if opcao == 2:
        while True:
            materias.append(str(input('Quais matérias estudou hoje? ')))
            print('=' * 30)
            continuar = str(input('Você estudou mais alguma matéria? [S/N]')).upper().strip()[0]
            if continuar == 'N':
                if dia == 0:
                    tempo = float(input('Tempo total de estudo: '))
                    tmp_dif = tmp_150min - tempo
                    print(f'O tempo estimado em minutos era {tmp_150min} e você realizou {tempo}.')
                    print(f'Cronograma de estudos de {dias_semana[dia]}: {seg}')
                    print(f'Matérias que você estudou neste dia: {materias}')
                    print('O programa será encerrado. Volte sempre!')
                elif dia == 1:
                    tempo = float(input('Tempo total de estudo: '))
                    tmp_dif = tmp_150min - tempo
                    print(f'O tempo estimado em minutos era {tmp_150min} e você realizou {tempo}.')
                    print(f'Cronograma de estudos de {dias_semana[dia]}: {ter}')
                    print(f'Matérias que você estudou neste dia: {materias}')
                    print('O programa será encerrado. Volte sempre!')
                elif dia == 2:
                    tempo = float(input('Tempo total de estudo: '))
                    tmp_dif = tmp_150min - tempo
                    print(f'O tempo estimado em minutos era {tmp_150min} e você realizou {tempo}.')
                    print(f'Cronograma de estudos de {dias_semana[dia]}: {qua}')
                    print(f'Matérias que você estudou neste dia: {materias}')
                    print('O programa será encerrado. Volte sempre!')
                elif dia == 3:
                    tempo = float(input('Tempo total de estudo: '))
                    tmp_dif = tmp_150min - tempo
                    print(f'O tempo estimado em minutos era {tmp_150min} e você realizou {tempo}.')
                    print(f'Cronograma de estudos de {dias_semana[dia]}: {qui}')
                    print(f'Matérias que você estudou neste dia: {materias}')
                    print('O programa será encerrado. Volte sempre!')
                elif dia == 4:
                    tempo = float(input('Tempo total de estudo: '))
                    tmp_dif = tmp_150min - tempo
                    print(f'O tempo estimado em minutos era {tmp_150min} e você realizou {tempo}.')
                    print(f'Cronograma de estudos de {dias_semana[dia]}: {sex}')
                    print(f'Matérias que você estudou neste dia: {materias}')
                    print('O programa será encerrado. Volte sempre!')
                elif dia == 5:
                    tempo = float(input('Tempo total de estudo: '))
                    tmp_dif = tmp_240min - tempo
                    print(f'O tempo estimado em minutos era {tmp_240min} e você realizou {tempo}.')
                    print(f'Cronograma de estudos de {dias_semana[dia]}: {sab}')
                    print(f'Matérias que você estudou neste dia: {materias}')
                    print('O programa será encerrado. Volte sempre!')
                elif dia == 6:
                    tempo = float(input('Tempo total de estudo: '))
                    tmp_dif = tmp_120min - tempo
                    print(f'O tempo estimado em minutos era {tmp_120min} e você realizou {tempo}.')
                    print(f'Cronograma de estudos de {dias_semana[dia]}: {dom}')
                    print(f'Matérias que você estudou neste dia: {materias}')
                    print('O programa será encerrado. Volte sempre!')
                break
        break
frases = (
    'Um dia ruim de estudo ainda é melhor do que nenhum estudo.',
    'Consistência vence motivação.',
    'Cada exercício resolvido aproxima você do seu objetivo.',
    'Errar faz parte do aprendizado.',
    'Não compare seu capítulo 1 com o capítulo 20 de outra pessoa.',
    'A disciplina faz o que a motivação não consegue.',
    'Hoje melhor que ontem. Amanhã melhor que hoje.',
    'Todo desenvolvedor já travou exatamente como você está travando agora.',
    'O importante é não parar de escrever código.','Hoje você escreveu código. Isso já é progresso.',
    'Não tenha medo dos erros; tenha medo de parar de tentar.',
    'A repetição constrói habilidade.',
    'Todo bug resolvido aumenta sua experiência.',
    'Você não precisa ser o melhor hoje. Precisa apenas continuar.',
    'Programação é prática. Continue praticando.',
    'Um exercício por dia vale mais que uma maratona uma vez por mês.',
    'A disciplina transforma iniciantes em profissionais.',
    'Seu código de hoje será melhor que o de ontem.',
    'Persistência é a habilidade mais importante de um programador.'
)
print('-'*40)
print(f'Frase do dia:\n {choice(frases)}')
print('-'*40)
#a saida sera o tempo que fiquei e o quanto eu tinha que ter ficado
