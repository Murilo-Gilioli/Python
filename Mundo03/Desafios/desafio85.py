"""
DESAFIO 085

Crie um programa onde o usuario possa digitar sete valores numericos e cadastre-os em uma lista unica que mantenha separados os valores pares e impares. no final mostre os valores pares e impares em ordem crescente.

Assistir até: Aula 17²
"""

numeros = [[],[]]

for x in range(7):
    valor = int(input("Digite um Valor: "))

    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)

print("-" * 30)
numeros[0].sort()
numeros[1].sort()
print(f"Numeros Pares: {numeros[0]}")
print(f"Numeros Impares: {numeros[1]}")