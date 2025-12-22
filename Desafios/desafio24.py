"""
DESAFIO 024

Faça um programa que leia o nome de uma cidade e diga se ela começa ou nao com o nome "SANTO"

Assistir até: Aula 09
"""
cityName = str(input("Digite o Nome de uma cidade: ")).title().strip()

separatedCityName = cityName.split()
if separatedCityName[0] == "Santo":
    print("Começa com 'Santo'")
else:
    print("Nao começa com 'Santo'")

#                    another way to do                            #

verifySanto = "Santo" in cityName
if verifySanto:
    print("Essa cidade começa com 'Santo'")
else:
    print("Essa cidade nao começa com 'Santo'")