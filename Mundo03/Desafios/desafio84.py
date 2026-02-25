"""
DESAFIO 084

Faça um programa que leia nome e peso de varias pessoas, guardando tudo em uma lista. no final, mostre:

A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma Listagem com as pessoas mais leves.

Assistir até: Aula 17²
"""
temp = []
princ = []
mai = men = 0

while True:
    temp.append(str(input("Nome: ")))
    temp.append(float(input("Peso: ")))

    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]

    princ.append(temp[:])
    temp.clear()
    continuar = str(input("Quer Continuar? [S/N]: ")).capitalize().strip()
    if continuar == 'N':
        break

for p in princ:
    if p[1] == mai:
        print(f"Maior Peso: {p[0]}")
    if p[1] == men:
        print(f"Menor Peso: {p[0]}")