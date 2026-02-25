"""
DESAFIO 091

Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatorios. Guarde esses resultados em um dicionario. No final, coloque esse dicionario em ordem, sabendo que o vencedor tirou o maior número no dado.

Assistir até: Aula 18
"""
from random import randint
jogadores = {}

# Valores para Cada Jogador
for j in range(1, 5):
    jogadores[f'jogador{j}'] = randint(1,6)

# Valores Sorteados:
print("Valores Sorteados:")
for chave, valor in jogadores.items():
    print(f"o {chave} tirou {valor}")

# Ranking dos Jogadores:
print("Ranking dos Jogadores:")