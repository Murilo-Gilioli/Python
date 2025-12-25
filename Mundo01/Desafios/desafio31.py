"""
DESAFIO 031

Desenvolva um programa que pergunte a distancia de uma viagem em KM. Calcule o preço da passagem, cobrando R$0,50 por KM para viagens de até 200KM e R$0,45 para Viagens mais Longas

Assistir até: Aula 10
"""

kms = int(input("Digite a Distancia em KM's de uma Viagem: "))

if kms <= 200:
    print(f"o valor da passagem será de R${kms * 0.50:.2f}")
else:
    print(f"o valor da passagem será de R${kms * 0.45:.2f}")