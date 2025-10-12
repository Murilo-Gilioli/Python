"""
DESAFIO 008

Crie um Algoritmo que Leia um valor em metros e o exiba convertido em centimetros e milimetros.

Assistir até: Aula 07
"""

m = int(input("Digite um Valor em Metros: "))
cm = m * 100
mm = cm * 10
print(f"{m} Metro tem: {cm} Centimetros e {mm} Milimetros")