"""
DESAFIO 033

Faça um programa que leia tres numeros e mostre qual é o maior e qual é o menor.

Assistir até: Aula 10
"""
n1 = int(input("Digite um Numero: "))
n2 = int(input("Digite outro Numero: "))
n3 = int(input("Digite outro Numero: "))

print(f"Analisando os Numeros {n1,n2,n3}")

if (n1 > n2 and n3):
    print(f'{n1} é o maior Numero')
elif (n2 > n1 and n3):
    print(f'{n2} é o maior Numero')
elif (n3 > n1 and n2):
    print(f'{n3} é o maior Numero')


if (n1 < n2 and n1 < n3):
    print(f'{n1} é o menor Numero')
elif (n2 < n1 and n3):
    print(f'{n2} é o menor Numero')
elif (n3 < n1 and n2):
    print(f'{n3} é o menor Numero')

print(n3 < n1, n3 < n2)