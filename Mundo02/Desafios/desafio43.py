"""
DESAFIO 043

Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e msotre seu status, de acordo com a tabela abaixo:

- Abaixo de 18.5: Abaixo do Peso
- Entre 18.5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida

Assistir até: Aula 12
"""
import math

kg = float(input("Qual o seu Peso? "))
height = float(input("Qual a sua Altura? "))
imc = kg / height ** 2

if imc < 18.5:
    print("Voce está abaixo do Peso!")
elif imc >= 18.5 and imc <= 25:
    print("Voce está com o Peso Ideal!")
elif imc > 25 and imc <= 30:
    print("Voce está com Sobrepeso!")
elif imc > 30 and imc  <= 40:
    print("Voce está com Obesidade!")
elif imc > 40:
    print("Voce está com Obesidade Mórbida")