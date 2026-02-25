"""
DESAFIO 086

Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
no final, mostre a matriz na tela, com a formatação correta

Assistir até: Aula 17²
"""
matriz = [[],[],[]]
first = 0
second = 0

for c in range(9):
    if second == 3:
        first += 1
        second = 0

    valor = int(input(f'Digite um valor para [{first,second}]:  '))
    matriz[first].append(valor)
    second += 1

print(f"[  {matriz[0][0]}  ] [  {matriz[0][1]}  ] [  {matriz[0][2]}  ]")
print(f"[  {matriz[1][0]}  ] [  {matriz[1][1]}  ] [  {matriz[1][2]}  ]")
print(f"[  {matriz[2][0]}  ] [  {matriz[2][1]}  ] [  {matriz[2][2]}  ]")

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
print(soma)

# B) a Soma dos valores da terceira Coluna.
columnSum = (matriz[0][2] + matriz[1][2] + matriz[2][2])
print(columnSum)

# C) o Maior valor da Segunda Linha.
print(max(matriz[1][0],matriz[1][1],matriz[1][2]))
"""