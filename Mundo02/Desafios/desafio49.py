"""
DESAFIO 049

Refaça o desafio 009, mostrando a tabuada de um numero que o usuario escolher, so que agora utilizando um laço for.

Assistir até: Aula 13
"""

number = int(input("Digite um Numero para Obter a Tabuada do Mesmo: "))

for c in range(0, 10+1):
    print(f"{number} x {c} = {c * number}")
print("FIM!")