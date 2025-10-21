"""
DESAFIO 018

Escreva um Programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo.

Assistir até: Aula 08
"""
import math;


ang = int(input("Digite o Valor de um Angulo: "))
cos = math.cos(math.radians(ang))
sen = math.sin(math.radians(ang))
tan = math.tan(math.radians(ang))
print(f"o Valor de Cosseno é: {cos:.2f}, o de Seno é: {sen:.2f}, e o da Tangente é: {tan:.2f}")