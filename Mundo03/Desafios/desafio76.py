"""
DESAFIO 076

Crie um programa que tenha uma tupla unica com nomes de produtos e seus respectivos preços, na sequencia.

no final, mostre uma listagem de preços, organizando os dados em forma tabular.

Assistir até: Aula 16
"""
produtos = ("Mouse", 120, "Teclado", 200, "Monitor", 500, "Gabinete", 250)

print("--" * 20)
print("          LISTAGEM DE PREÇOS")
print("--" * 20)

for c in range(0, len(produtos), 1):
    if c % 2 == 0:
        print(f"{produtos[c]:.<30}  ", end="")
    if c % 2 == 1:
        print(f"R$ {produtos[c]}")

print("...")