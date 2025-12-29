"""
DESAFIO 046

Crie um Programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio, indo de 10 até 0, com uma pausa de 1 segundo entre eles

Assistir até: Aula 13
"""
from time import sleep

print("CONTAGEM REGRESSIVA PARA OS FOGOS!!")
for c in range(10,0,-1):
    print(c)
    sleep(1)
print("🎆🎆🎆🎆🎆")
