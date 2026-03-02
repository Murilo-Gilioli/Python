"""
DESAFIO 091

Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatorios. Guarde esses resultados em um dicionario. No final, coloque esse dicionario em ordem, sabendo que o vencedor tirou o maior número no dado.

Assistir até: Aula 18
"""
# Minha Solução Fazendo sem Conhecer os Metodos como itemgetter ou Metodos do tipo:

from random import randint
from time import sleep

jogadores = {}
ranking = {}
keyMaior = ""
maior = 0

# Valores para Cada Jogador
for player_num in range(1, 5):
    jogadores[f'jogador{player_num}'] = randint(1,6)

print(jogadores)

# Valores Sorteados:
print("Valores Sorteados:")
for chave, valor in jogadores.items():
    print(f"   O {chave} tirou {valor}")
    sleep(1)

# Ranking dos Jogadores:
print("Ranking dos Jogadores:")

# Encontra o Jogador com Maior Ponto nos Dados e Salva sua chave e valor
for iterar in range(len(jogadores)):
    maior = 0
    for key, value in jogadores.items():
        if value > maior:
            maior = value
            keyMaior = key

# Adiciona ele no Dicionario de Ranking, Deixando em Ordem do Maior pro Menor, faz isso até achar todos.
    ranking[f'{keyMaior}'] = maior
    del jogadores[f'{keyMaior}']

# Printa na Tela os Jogadores em suas devidas Posições, Nomes e Pontos.
contador = 1
for keys, values in ranking.items():
    print(f"{contador:>4}º Lugar: {keys} com {values}")
    contador = contador + 1
    sleep(1)

#                      Solução da Aula                        #

from random import randint
from time import sleep
from operator import itemgetter

jogo = {'jogador1': randint(1,6), 'jogador2': randint(1,6), 'jogador3': randint(1,6), 'jogador4': randint(1,6)}

print("Valores Sorteados:")
for chave, valor in jogo.items():
    print(f"   O {chave} tirou {valor}")
    sleep(0.4)

rank = sorted(jogo.items(),key=itemgetter(1), reverse=True)

for indice, valor in enumerate(ranking):
    print(f"{indice + 1}º lugar: {valor[0]} com {valor[1]}.")
    sleep(0.4)