"""
DESAFIO 039

faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:

- se ele ainda vai se alistar ao serviço militar.
- se é a hora de se alistar
- se já passou do tempo do alistamento

seu programa tambem devera mostrar o tempo que falta ou que passou do prazo.

Assistir até: Aula 12
"""
from datetime import date

date_Of_Birth = int(input("Qual é o Ano do seu Nascimento? "))
current_Year = date.today().year
current_Age = current_Year - date_Of_Birth
age_To_Enlistment = 18

if current_Age <= 16:
    print(f"Ainda faltam {age_To_Enlistment - current_Age} Anos para voce se alistar no Serviço Militar.")
elif current_Age == 17:
    print("Voce ja pode se alistar no Serviço Militar.")
elif current_Age >= 18:
    print(f"Voce ja Frequentou/Passou do tempo do Alistamento à {current_Age - age_To_Enlistment} Anos.")