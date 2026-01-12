"""
DESAFIO 064

Crie um programa que leia vários numeros inteiros pelo teclado. o Programa so vai parar quando o usuário digitar o valor 999, que é a condiçao de parada. no final, mostre quantos numeros foram digitados e qual foi a soma entre eles (desconsiderando o Flag)

Assistir até: Aula 14
"""

number = int(input("Numero: "))
count = soma = 0

while number != 999:
    soma += number   
    count += 1     
    number = int(input("Outro Numero: "))
print(f"Voce digitou {count} Números.") # Numeros Digitados (Encontrado)
print(f"A Soma entre todos os Números foi de: {soma}") # Soma entre os Numeros (Calculado)