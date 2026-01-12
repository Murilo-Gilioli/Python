"""
DESAFIO 066

Crie um programa que leia vários numeros inteiros pelo teclado. O Programa só vai para quando o usuário digitar o valor 999, que é a condiçao de parada. No final, mostre quantos números foram digitados e qual foi a Soma entre eles (Desconsiderando o Flag)

Assistir até: Aula 15
"""

n = s = c = 0

while True:
    s += n
    n = int(input("Digite um Numero [999 P/ Parar] "))

    # Condiçao de Parada.
    if n == 999:
        break

    c += 1

# Resultados.
print(f"Voce Digitou {c} Numeros e a Soma entre eles é: {s}")