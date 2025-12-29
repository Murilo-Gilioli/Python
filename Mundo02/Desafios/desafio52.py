"""
DESAFIO 052

Faça um programa que leia um numero inteiro e diga se ele é ou nao um numero primo.

Assistir até: Aula 13
"""
number = int(input("Digite um Numero Inteiro: "))
value = 0

for c in range(1, 10 + 1):
    if number % c == 0:
        value += 1

if value <= 2:
   print(f"o Numero {number} é um Numero Primo")
else:
    print(f"o Numero {number} não é um Numero Primo")