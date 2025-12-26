"""
DESAFIO 038

Escreva um programa que leia dois numeros inteiros e compare-os, mostrando na tela uma mensagem:

- o Primeiro valor é Maior.
- o Segundo valor é Maior.
- nao existe valor maior, os dois sao Iguais.

Assistir até: Aula 12
"""

num1 = int(input("Digite um Numero: "))
num2 = int(input("Digite outro Numero: "))

print("Comparando...")
if num1 > num2:
    print("o Primeiro valor é Maior")
elif num2 > num1:
    print("o Segundo valor é Maior")
else:
    print("nao existe valor maior, os dois sao Iguais")