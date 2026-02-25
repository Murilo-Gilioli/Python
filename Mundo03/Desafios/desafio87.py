"""
DESAFIO 087

Aprimore o desafio anterior, mostrando no final:

A) a Soma de todos os valores pares digitados.
B) a Soma dos valores da terceira Coluna.
C) o Maior valor da Segunda Linha.

Assistir até: Aula 17²
"""
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = 0

for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f"Digite o numero da [{l}/{c}]: "))
        if matriz[l][c] % 2 == 0:
            soma = soma + matriz[l][c]

for l in range(3):
    for c in range(3):
        print(f"[ {matriz[l][c]} ]", end="")
    print()

# A) a Soma de todos os valores pares digitados.
print(f"a Soma entre todos os valores Pares digitados é: {soma}")

# B) a Soma dos valores da terceira Coluna.
columnSum = (matriz[0][2] + matriz[1][2] + matriz[2][2])
print(f"a soma dos Valores da terceira coluna é: {columnSum}")

# C) o Maior valor da Segunda Linha.
print(f"o Maior Valor da segunda linha é: {max(matriz[1][0],matriz[1][1],matriz[1][2])}")