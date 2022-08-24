# Guilherme Wilson Vieira dos Santos - Tecnólogo em Análise e Desenvolvimento de Sistemas

import random
print('~' * 50)
print(f'{"~> ZOMBIE DICE <~":^50}')
print('~' * 50)

#Looping para regra de no mínimo dois jogadores
n_j = int(input('Digite o número de Jogadores: '))
while n_j < 2:
    print('São necessários no mínimo 2 jogadores!')
    n_j = int(input('Digite o número de Jogadores: '))

#Armazenamento dos nomes dos jogadores
lista_nomes = []
if n_j >= 2:
    for c in range(n_j):
        nome = str(input(f'Digite o nome do {c+1}º Jogador: '))
        lista_nomes.append(nome)

#Turno Jogador
nomes = 0
while True:
    print(f'Turno do jogador {lista_nomes[nomes]}')
#Definição dos treze dados
#(1-6 Verde/7-10 Amarelo/ 11-13 Vermelho)
    lista_dados = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    lista_verde = ["C", "P", "C", "T", "P", "C"]
    lista_amarelo = ["T", "P", "C", "T", "P", "C"]
    lista_vermelho = ["T", "P", "T", "C", "P", "T"]

#Contadores
    verde = 0
    amarelo = 0
    vermelho = 0
    passo = 0
    tiro = 0
    cerebro = 0

#Sorteio de três dados aleatórioas
    lista_dados_sorteados = (random.sample(lista_dados, 3))

#Remoção dos dados sorteados
    for ns in lista_dados_sorteados:
        if ns <= 6:
            verde += 1
        elif 7 <= ns <= 10:
            amarelo += 1
        else:
            vermelho += 1
        for n in lista_dados:
            if n == ns:
                lista_dados.remove(ns)
    print(f'Você retirou {verde} dados VERDE')
    print(f'Você retirou {amarelo} dados AMARELO')
    print(f'Você retirou {vermelho} dados VERMELHO')

#Sorteio das funções de cada dado
    for d in range(verde):
        face = random.randint(0, 5)
        if face == 3:
            tiro += 1
        elif face == 0 or 2 or 5:
            cerebro += 1
        else:
            passo += 1
    for d in range(amarelo):
        face = random.randint(0, 5)
        if face == 0 or 3:
            tiro += 1
        elif face == 2 or 5:
            cerebro += 1
        else:
            passo += 1
    for d in range(vermelho):
        face = random.randint(0, 5)
        if face == 0 or 2 or 5:
            tiro += 1
        elif face == 3:
            cerebro += 1
        else:
            passo += 1
    print(f'Você teve {tiro} tiros {passo} passos e {cerebro} cerebros')
    if tiro == 3:
        print(f'Você tirou 3 tiros.\n{lista_nomes[nomes]} seu turno acabou!')
        break
    else:
        de = str(input('Você deseja continuar jogando? [S/N]: ')).upper().strip()[0]
        if de in 'N':
            print(f'{lista_nomes[nomes]} o seu turno acabou.')
            break

