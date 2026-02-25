"""
DESAFIO 074

Crie um programa que vai gerar cinco numeros aleatórios e colocar em uma tupla.

Depois disso, mostre a listagem de números gerados e tambem indique o menor e o maior valor que estao na Tupla.

Assistir até: Aula 16
"""
from random import randint

teste = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))

menor = 0
maior = 0

print(f"os Numeros Sorteados Foram:", end=" ")
for t in teste:
    print(f"{t} ", end="")

for cont in range(0, len(teste)):
    val = teste[cont]
    if cont == 0:
        maior = menor = teste[0]
    else:
        if val > maior:
            maior = val
        elif val < menor:
            menor = val      
print(f"\no Maior Numero é: {maior} e o Menor Numero é: {menor}")

# da para usar tambem o {max(numeros)} e {min(numeros)} para mostrar o Maior e Menor Numero de uma Tupla