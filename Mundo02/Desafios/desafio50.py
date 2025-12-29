"""
DESAFIO 050

Desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas daqueles que forem pares. se o valor digitado for impar, desconsidere-o.

Assistir até: Aula 13
"""
soma = 0

for c in range(0,6):
    valor = int(input("Digite um Valor: "))
    if valor % 2 == 0:
        soma += valor
print(f"a soma entre os Numeros Pares resultou em: {soma}")