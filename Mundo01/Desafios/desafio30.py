"""
DESAFIO 030

Escreva um programa que Leia um numero inteiro e mostre na sua tela se ele é PAR ou IMPAR

Assistir até: Aula 10
"""

number = int(input("Digite um Numero Inteiro: "))

if number % 2 == 0:
    print(f"o Numero {number} é Par.")
else:
    print(f"o Numero {number} é Impar.")