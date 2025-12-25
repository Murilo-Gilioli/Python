"""
DESAFIO 035

Desenvolva um programa que leia o comprimento de tres retas e diga ao usuario se elas podem ou nao formar um triangulo.

Assistir até: Aula 10
"""
print("Digite o Comprimento de 3 Retas para Saber se é possivel formar um Triangulo com elas!")
c1 = float(input("Primeiro Comprimento: "))
c2 = float(input("Segundo Comprimento: "))
c3 = float(input("Terceiro Comprimento: "))

firstTest = c1 + c2 > c3
secondTest = c2 + c3 > c1
thirdTest = c1 + c3 > c2

if firstTest and secondTest and thirdTest:
    print("É possivel fazer um Triangulo com essas Retas.")
else:
    print("Nao é possivel fazer um Triangulo com essas Retas.")