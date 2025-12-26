"""
DESAFIO 041

A confederação nacional de nataçao precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

- até 9 anos: MIRIM
- até 14 anos: INFANTIL
- até 19 anos: JUNIOR
- até 20 anos: SÊNIOR
- Acima: MASTER

Assistir até: Aula 12
"""
from datetime import date

age_Of_Birth = int(input("Digite o Ano do seu Nascimento: ").strip())
current_Year = date.today().year
current_Age = (current_Year - age_Of_Birth)

if age_Of_Birth >= current_Year or age_Of_Birth < 0:
    print("Digite uma Data Valida.")
else :
    if current_Age <= 9:
      print(f"Voce tem {current_Age} Anos, a Sua Categoria é: MIRIM")
    elif current_Age >= 14 and current_Age <= 18:
     print(f"Voce tem {current_Age} Anos, a Sua Categoria é: INFANTIL")
    elif current_Age == 19:
     print(f"Voce tem {current_Age} Anos, a Sua Categoria é: JUNIOR")
    elif current_Age == 20:
      print(f"Voce tem {current_Age} Anos, a Sua Categoria é: SÊNIOR")
    elif current_Age >= 21:
     print(f"Voce tem {current_Age} Anos, a Sua Categoria é: MASTER")

