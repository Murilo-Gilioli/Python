"""
DESAFIO 022

Faça um programa que leia o nome completo de uma pessoa e mostre:

- O Nome com todas as letras MAIUSCULAS.
- O Nome com todas minúsculas.
- Quantas letras ao todo (sem espaços).
- Quantas letras tem o primeiro nome.

Assistir até: Aula 09
"""

name = str(input("Digite seu Nome: "))
upperName = name.upper()
lowerName = name.lower()
separatingName = name.split()
erasedSpaces = ''.join(separatingName)
print(f"Nome em Letras Maiusculas: {upperName}")
print(f"Nome em Letras minusculas: {lowerName}")
print(f"Quantas Letras sem os Espaços: {len(erasedSpaces)}")
print(f"Quantas Letras tem o Primeiro Nome: {len(separatingName[0])}")