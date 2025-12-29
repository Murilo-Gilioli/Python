"""
DESAFIO 051

Desenvolva um programa que leia o primeiro termo e a razao de uma PA. no final, mostre os 10 primeiros termos dessa progressao.

Assistir até: Aula 13
"""
print("=" * 30)
print("     10 TERMOS DE UMA P.A      ")
print("=" * 30)

first = int(input("Primeiro Termo: "))
num = int(input("Razão: "))

for c in range(1, 10 + 1):
    print(first, end=" → ")
    first += num
print("ACABOU!")