"""
DESAFIO 013

Crie um Algoritmo que Leia o Salario de um Funcionario e mostre seu novo salario, com 15% de aumento.

Assistir até: Aula 07
"""

valueSalary = int(input("Digite o Valor do seu Salario: "))
increaseValue = 15 / 100 * valueSalary
increasedSalary= valueSalary + increaseValue

print(f"o Valor do seu Salario Atual é: R${valueSalary}")
print(f"o Valor do seu Novo Salario é: R${increasedSalary}")