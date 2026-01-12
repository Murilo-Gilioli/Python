"""
DESAFIO 061

Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressao usando a estrutura WHILE.

Assistir até: Aula 14
"""

print("=" * 30)
print("     10 TERMOS DE UMA P.A      ")
print("=" * 30)

first = int(input("Primeiro Termo: "))
num = int(input("Razão: "))
terms = int(input("Termos: "))

while terms != 0:
    print(first, end=" → ")
    first += num
    terms -= 1
print("ACABOU!")