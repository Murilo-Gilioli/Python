"""
DESAFIO 079

Crie um programa onde o usuario possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número ja exista lá dentro, ele nao sera adicionado. No final, serão exibidos todos os valores únicos digitados, em Ordem Crescente.

Assistir até: Aula 17
"""

valores = []

while True:
    addNum = int(input("Digite um Valor: "))

    while valores.count(addNum) == 1:
        addNum = int(input("Valor já Registrado... Digite outro Valor: "))

    if valores.count(addNum) != 1:
        valores.append(addNum)
        print(f"Valor Registrado com Sucesso!")
        continuar = str(input("Você Gostaria de Continuar? [S/N] ")).strip().upper()

    if continuar == "N":
        break

valores.sort()
print(f"Voce Digitou os Valores {valores}")