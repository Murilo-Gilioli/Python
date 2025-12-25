"""
DESAFIO 034

Escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento.

para salarios superioes a R$1.250,00 - Calcule um aumento de 10%

Para os inferioes ou iguais, o aumento é de 15%.

Assistir até: Aula 10
"""
salary = int(input("Digite o Valor do seu Salario: "))

if salary > 1250:
    salaryIncrease = 10 / 100 * salary
    salary += salaryIncrease
else:
    salaryIncrease = 15 / 100 * salary
    salary += salaryIncrease
    
print(f"O seu Aumento Salarial foi de: R${salaryIncrease:.2f}, resultando em R${salary:.2f}")