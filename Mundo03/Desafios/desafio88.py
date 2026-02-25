"""
DESAFIO 088

Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O Programa vai perguntar quantos jogos serao gerados e vai sortear 6 numeros entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

Assistir até: Aula 17²
"""
import random;
jogos = []
palpites = int(input("Quantos Palpites Vai Querer? "))
randomNum = random.randint(1,60)

for p in range(palpites):
    numeros = []
    for n in range(6):
        numeros.append(random.randint(1,60))
    jogos.append(numeros[:])
    numeros.clear()

for j in jogos:
    print(j)