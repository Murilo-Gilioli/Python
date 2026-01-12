"""
DESAFIO 070

Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuario vai continuar. No final, mostre:

A) Qual é o total Gasto na Compra.
B) Quantos produtos custam mais de R$1000.
C) Qual é o nome do Produto mais Barato.

Assistir até: Aula 15
"""

soma = moreExpensives = 0
moreProducts = "S"
cheapiestProduct = 0
cheapiestProductName = ""

while True:
    # Product Infos.
    productName = str(input("Nome do Produto: ")).capitalize().strip()
    productValue = float(input("Preço: "))
    moreProducts = str(input("Quer Continuar? [S/N] ")).capitalize().strip()

    # Data Tratament
    soma += productValue

    if productValue > 1000:
        moreExpensives += 1

    if cheapiestProduct == 0:
        cheapiestProduct = productValue
        print(cheapiestProduct)

    if productValue < cheapiestProduct:
        cheapiestProduct = productValue
        cheapiestProductName = productName
        print(cheapiestProduct)


    # End of the Program and Showing the Results.
    if moreProducts != "S":
        print(f"o Valor total gasto na Compra foi de R${soma:.2f}")
        print(f"Temos {moreExpensives} Produtos custando mais de R$1000.00")
        print(f"O Produto Mais Barato foi {cheapiestProductName}, e custou R${cheapiestProduct:.2f}")
        break