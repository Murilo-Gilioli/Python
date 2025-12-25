"""
DESAFIO 028

Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuario tentar descobrir qual foi o número escolhido pelo computador.

o Programa deverá escrever na tela se o usuario venceu ou perdeu.

Assistir até: Aula 10
"""

import random;
numero = random.randint(0,5)
chute = int(input("Digite um numero entre 0 e 5: "))

if chute == numero:
    print("Voce Ganhou!")
else:
    print(f"Voce Perdeu! o Numero Escolhido era {numero}!")