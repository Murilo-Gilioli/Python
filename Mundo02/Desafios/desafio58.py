"""
DESAFIO 058

Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

Assistir até: Aula 14
"""
from random import randint
computer = randint(0,10)

print("-" * 25)
print("TENTE DESCOBRIR O NÚMERO!")
print("-" * 25)
print("Estou pensando em um Número entre 0 e 10, Qual é o seu Chute?")

player = int(input(""))
attempts = 0

while player != computer:
    player = int(input("ERRADO! Tente outro Chute: "))
    attempts += 1
print(f"ACERTOU! Mas voce precisou de {attempts} Tentativas para Acertar!")
