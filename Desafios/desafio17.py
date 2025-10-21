"""
DESAFIO 017

Escreva um Programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa.

Assistir até: Aula 08
"""
import math

co = float(input("Digite o Valor do Comprimento do Cateto Oposto: "))
ca = float(input("Digite o Valor do Comprimento do Cateto Adjacente: "))
formule = (math.pow(co,2)) + (math.pow(ca,2))
# hi = (co ** 2) + (ca ** 2)
# hi = math.hypot(co, ca)
hi = math.sqrt(formule)

print(f"a Hipotenusa vai Medir: {hi:.1f}")