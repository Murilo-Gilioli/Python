"""
DESAFIO 036

Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. o programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar.

Calcule o valor da prestação mensal, sabendo que ela nao pode exceder 30% do salario ou entao o empréstimo sera negado.

Assistir até: Aula 12
"""

house_Value = float(input("Qual o Valor da Casa? ").strip())
salary = float(input("Qual o valor do seu Salario? ").strip())
years = float(input("Em Quantos anos voce irá pagar? ").strip())
mensally_To_Pay = years * 12
mensally_Value = house_Value / mensally_To_Pay
salary_Percent = 30 / 100 * salary

if mensally_Value < salary_Percent:
    print("o seu Emprestimo foi Aprovado.")
else:
    print("o seu Empréstimo foi Negado.")

