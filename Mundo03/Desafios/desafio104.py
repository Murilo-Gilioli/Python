"""
DESAFIO 104

Faça um programa que tenha uma função chamada leiaInt(), que vai funcionar de forma semelhante a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.

Ex:
n = leiaInt('Digite um n')

Assistir até: Aula 21

if type(valor) == int:
        print(type(valor))
    else:
        print("né nao")
"""
def leiaInt(message):
    while True:
        valor = input(f"\033[37m{message}")
        if valor.isnumeric():
            return valor
        else:
            print(f"\033[31m ERRO! Digite um número inteiro válido")

n = leiaInt("Digite um Numero: ")
print(f"Voce acabou de digitar o Número {n}")