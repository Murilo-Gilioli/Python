"""
DESAFIO 057

Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitaçao novamente até ter um valor correto.

Assistir até: Aula 14
"""
gender = str(input("Sexo: ")).upper()


while gender != "F" and gender != "M":
    gender = str(input("Digite um Genero Correto (M/F): ")).upper()