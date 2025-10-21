"""
DESAFIO 016

Escreva um Programa que leia um numero Real qualquer pelo teclado e mostre na tela a sua porção inteira.

Ex: Digite um numero: 1.675
O numero 1.675 tem a Parte Inteira 1.

Assistir até: Aula 08
"""
import math

n1 = float(input("Digite um Numero Real: "))
print(f"o Numero Inteiro desse Numero é: {math.trunc(n1)}")