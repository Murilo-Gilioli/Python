"""
DESAFIO 004

Crie um Programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ele.

Assistir até: Aula 06
"""

valor = input("Digite algum Valor: ")
print("o Valor Digitado é: {}".format(valor))
print("o Tipo Primitivo do seu Valor é: ", type(valor))
print("Seu Valor é um Numero?: ", valor.isnumeric())
print("seu Valor é Alfanumerico?: ", valor.isalnum())
print("seu Valor é Decimal?: ", valor.isdecimal())
print("seu Valor é todo com Espaços?: ", valor.isspace())
print("seu Valor é todo Maiusculo?: ", valor.isupper())
print("seu Valor é todo Minusculo?: ", valor.islower())

# no Python 3.7, o Uso do Format pode ser Feito dessa Forma Tambem:

print(f"seu Valor é um Numero?: {valor.isnumeric()}")