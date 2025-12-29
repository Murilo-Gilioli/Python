"""
DESAFIO 037

Escreva um programa que leia um numero inteiro qualquer e peça para o usuario escolher qual sera a base de conversao:

-1 para binário
-2 para octal
-3 para hexadecimal

Assistir até: Aula 12
"""

num = int(input("Digite um numero inteiro: "))
print("""Escolha uma das bases para a conversao:
    [1] converter para BINARIO
    [2] converter para OCTAL
    [3] converter para HEXADECIMAL""")
opcao = int(input("Sua opçao: "))

if opcao == 1:
    print(f"{num} convertido para binario é igual a {bin(num)[2:]}")
elif opcao == 2:
    print(f"{num} convertido para OCTAL é igual a {oct(num)[2:]}")
elif opcao == 3:
    print(f"{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}")
else:
    print("Tente Novamente.")