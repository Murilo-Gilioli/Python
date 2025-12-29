"""
DESAFIO 047

Crie um Programa que mostre na tela todos os numeros pares que estao no intervalo entre 1 e 50.

Assistir até: Aula 13
"""
from time import sleep


print("Os Numeros PARES entre 0 e 50 São:")
for c in range(0, 50+1):
    if c % 2 == 0:
        print(c)
        sleep(0.5)
print("FIM!")
        

