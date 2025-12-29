"""
DESAFIO 048

faça um programa que calcule a soma entre todos os numeros impares que sao multiplos de tres e que se encontram no intervalo entre 1 e 500.

Assistir até: Aula 13
"""
s = 0
count = 0
for c in range(0, 500, 3):
    if c % 2 == 1:
        s += c
        count += 1
print(f"Foram encontrados {count} Numeros Impares, e a Soma entre todos eles é: {s}")