"""
DESAFIO 012

Crie um Algoritmo que Leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

Assistir até: Aula 07
"""

valueProduct = int(input("Digite o Preço do Produto: "))
discountValue= 5 / 100 * valueProduct
discountProduct = valueProduct - discountValue
print(f"o valor do Produto Original é: R${valueProduct},")
print(f"com Desconto, o Valor do Produto Fica: R${discountProduct}")