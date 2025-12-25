"""
DESAFIO 025

Faça um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

Assistir até: Aula 09
"""
yourName = str(input("Digite o seu nome Completo: ")).title().strip()

verifyName = "Silva" in yourName
if verifyName:
    print("Voce tem 'Silva' no Nome!")
else:
    print("Voce nao tem 'Silva' no Nome!")