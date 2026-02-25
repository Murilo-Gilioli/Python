"""
DESAFIO 077

Crie um programa que tenha uma tupla com varias palavras (nao usar acentos), depois disso, voce deve mostrar para cada palavra, quais sao as suas vogais.

Assistir até: Aula 16
"""

words = ("Caneta", "Consoante", "Carvalho", "Selatonina", "Kamikaze")

for w in words:
    print(f"\nNa palavra {w} temos ", end="")
    for letra in w:
        if letra in "aeiou":
            print(f"{letra}", end=" ")