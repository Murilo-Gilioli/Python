"""
DESAFIO 060

Faça um programa que leia um Numero qualquer e mostre o seu Fatorial.

EX: 5! = 5x4x3x2x1 = 120

Assistir até: Aula 14
"""

n = int(input("Digite um Numero para ver o seu Fatorial: "))
val = n
res = 1

while n != 0:  
    n -= 1
    res += res * n
  
print(f"o Fatorial de {val} é {res}")


