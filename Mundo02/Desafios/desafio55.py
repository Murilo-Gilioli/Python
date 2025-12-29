"""
DESAFIO 055

Faça um programa que leia o peso de cinco pessoas. no final, mostre qual foi o maior e o menor peso lidos.

Assistir até: Aula 13
"""
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input("Digite o seu Peso: "))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print(f"o Maior Peso lido foi de {maior}Kg")
print(f"o Menor Peso lido foi de {menor}Kg")