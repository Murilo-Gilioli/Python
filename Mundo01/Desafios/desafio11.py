"""
DESAFIO 011

Crie um Algoritmo que Leia a Largura e a altura de uma parede em metros, calcule sua área e a quantidade de tinta necessaria para pinta-la, sabendo que cada litro de tinta, pinta uma área de 2m².

Assistir até: Aula 07
"""

height = int(input("Altura da Parede: "))
width = int(input("Largura da Parede: "))
area = height * width
sinkQuantity = area / 2

print(f"a Área de uma Parede de {height}m de Altura e {width}m de Largura é de: {area}m²")
print(f"a Quantidade de Tinta que seria necessaria para Pinta-la seria de: {sinkQuantity} Litros de Tinta")