"""
DESAFIO 032

Faça um programa que leia um ano qualquer e mostre se ele é um Ano Bissexto.

Assistir até: Aula 10
"""

year = int(input("Digite um ano qualquer: "))
fourYears = year % 4
oneHundredYear = year % 100
fourHundredYears = year % 400

if oneHundredYear == 0 and fourHundredYears != 0 or fourYears < 0:
    print('Nao é um ano Bissexto')
elif fourHundredYears == 0 or fourYears == 0:
    print('É um ano Bissexto')