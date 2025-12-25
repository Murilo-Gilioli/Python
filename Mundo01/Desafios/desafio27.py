"""
DESAFIO 027

Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente.

EX: Ana Maria de Souza.
Primeiro = Ana
Último = Souza

Assistir até: Aula 09
"""

name = "Murilo Gilioli Cordeiro de Souza"

separatedName = name.split()

print(f"Primeiro Nome: {separatedName[0]}")
print(f"Ultimo Nome: {separatedName[-1]}")