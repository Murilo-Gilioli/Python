"""
DESAFIO 015

Escreva um Programa que pergunte a quantidade de KMs Percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por KM Rodado.

Assistir até: Aula 07
"""

days = int(input("Quantos Dias Foram Alugados? : "))
kms = int(input("Quantos KM's Foram Percorridos? : "))
valueForDays = days * 60
valueForKms = kms * 0.15
valueForPay = valueForDays + valueForKms
print(f"o Valor Total a Pagar é de R${valueForPay:.2f}")
