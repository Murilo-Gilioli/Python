"""
DESAFIO 081

Crie um programa que vai ler vários numeros e colocar em uma Lista.
Depois disso, Mostre:

A) Quantos Números foram digitados.
B) A Lista de Valores, Ordenada de forma Decrescente.
C) Se o Valor 5 foi Digitado e está ou nao na Lista.

Assistir até: Aula 17
"""
valores = []
cont = 0
num5 = 0

while True:
    cont += 1
    num = int(input("Digite um Numero: "))
    res = str(input("Quer Continuar? [S/N] ")).strip().upper()
    valores.append(num)

    if num == 5:
        num5 += 1

    if res == "N":
        break

print(f"No Total Foram Digitados {cont} Números.")
if num5 == 1:
    print("o Numero 5 Foi Digitado e está na Lista.")
else:
    print("o Numero 5 Nao Foi Digitado e nao está na Lista.")
    
valores.sort(reverse=True)
print(f"a Lista em Ordem Decrescente Fica: {valores}")