"""
DESAFIO 010

Crie um Algoritmo que Leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

Considere: US$1,00 = R$3,27

Assistir até: Aula 07
"""

n1 = int(input("digite o valor em Dinheiro que voce tem na sua Carteira: "))
buyDols = n1 / 3.27
print(f"com essa quantia voce consegue Comprar U${buyDols:.2f} Dolares")