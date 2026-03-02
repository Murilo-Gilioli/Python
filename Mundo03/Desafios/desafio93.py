"""
DESAFIO 093

Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso sera guardado em um dicionario, incluindo o total de gols feitos durante o campeonato.

Assistir até: Aula 18
"""
jogador = {}
gols = []
total = 0

jogador['nome'] = str(input("Nome: "))
partidas = int(input("Quantidade de Partidas: "))

for gol in range(partidas):
    gols.append(int(input(f"{'':>3}Quantos Gols na {gol + 1}ª Partida: ")))
    jogador['gols'] = gols

for g in gols:
    total += g
    jogador['total'] = total

print("-=" * 30)
print(jogador)

print("-=" * 30)
for key, value in jogador.items():
    print(f"O campo {key} tem o valor {value}")

print("-=" * 30)
print(f"o Jogador {jogador['nome']} jogou {partidas} Partidas.")
for valor in range(partidas):
    print(f"{'':>3} => Na partida {valor + 1}, fez {jogador['gols'][valor]} gols.")
print(f"Foi um total de {jogador['total']} gols.")