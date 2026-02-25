"""
DESAFIO 082

Crie um programa que vai ler varios numeros e colocar em uma lista.
Depois disso, crie duas listas extras que vao conter apenas os valores pares e os valores impares digitados, respectivamente.
Ao final, Mostre o conteudo das tres listas geradas.

Assistir até: Aula 17
"""
valores = []
par = []
impar = []

while True:
    num = int(input("Digite um Valor: "))
    valores.append(num)
    cont = str(input("Deseja Continuar? [S/N] ")).capitalize().strip()
    
    if num % 2 == 0:
        par.append(num)
    elif num % 2 == 1:
        impar.append(num)

    if cont == 'N':
        break

print(f"Valores Digitados: {valores}")
print(f"Valores Pares: {par}")
print(f"Valores Impares: {impar}")