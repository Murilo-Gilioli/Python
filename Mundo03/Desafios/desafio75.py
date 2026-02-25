"""
DESAFIO 075

Crie um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9
B) Em que posição foi digitado o primeiro valor 3
C) Quais foram os Números Pares.

Assistir até: Aula 16
"""
valores = (int(input("Primeiro Valor: ")),int(input("Segundo Valor: ")),int(input("Terceiro Valor: ")),int(input("Quarto Valor: ")))
count = 0
print(f"\nVoce Digitou os Valores {valores}")

print(f"o Valor 9 Apareceu {valores.count(9)} vezes.")

# for n in valores:
#     if n == 3:
#         count += 1
# if count == 0:
#     print("o Valor 3 nao foi Digitado.")
# else:
#     print(f"o Valor 3 Apareceu pela primeira vez na Posição {valores.index(3)}.")

# OU

if 3 in valores:
    print(f"o Valor 3 Apareceu pela primeira vez na Posição {valores.index(3)}.")
else:
    print("o Valor 3 nao foi Digitado.")

print("os Numeros Pares Digitados Foram: ", end="")
for n in valores:
    if n % 2 == 0:
        print(n, end=" ")


