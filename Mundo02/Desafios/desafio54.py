"""
DESAFIO 054

Crie um programa que leia o ano de nascimento de sete pessoas. no final, mostre quantas pessoas ainda nao atingiram a maioridade e quantas ja sao maiores.

Assistir até: Aula 13
"""
from datetime import date
maior = 0
menor = 0

for c in range(0,7):
    current_Year = date.today().year
    birthYear = int(input("Digite seu Ano de Nascimento: "))
    current_Age = (current_Year - birthYear)
    if current_Age >= 18:
        maior += 1
    else:
        menor += 1

print(f"Dessas 7 Pessoas, {maior} ja sâo maiores de idade, e {menor} sao Menores.")