"""
DESAFIO 103

Faça um programa que tenha uma função chamada ficha(), que receba dois parametros opcionais: o nome de um jogador e quantos gols ele marcou.

O Programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado nao tenha sido informado corretamente.

Assistir até: Aula 21
"""

def ficha(playerName, gols):
    if playerName == '':
        playerName = "<Desconhecido>"
    if gols == '':
        gols = 0
        
    return f"o Jogador {playerName} fez {gols} gol(s) no campeonato."

nome = input("Nome do jogador: ")
gols = input("Número de Gols: ")
res = ficha(nome, gols)
print(res)