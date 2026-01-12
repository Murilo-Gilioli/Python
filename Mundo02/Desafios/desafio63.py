"""
DESAFIO 063

Escreva um Programa que leia um número 'n' Inteiro qualquer e mostre na tela os 'n' primeiros elementos de uma sequencia de Fibonacci.

EX: 0 - 1 - 1 - 2 - 3 - 5 - 8

Assistir até: Aula 14
"""
print('-'*30)
print('Sequência de Fibonacci')
print('-'*30)

n = int(input("Quantos termos voce quer mostrar? "))
t1 = 0
t2 = 1
cont = 3

print(f"{t1} - {t2}", end="")
while cont <= n:
    t3 = t1 + t2
    print(f" - {t3}", end="")

    cont += 1
    t1 = t2
    t2 = t3