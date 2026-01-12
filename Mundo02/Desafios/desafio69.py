"""
DESAFIO 069

Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa Cadastrada, o programa deverá perguntar se o usuário quer ou nao continuar. No Final, Mostre:

A) Quantas Pessoas tem mais de 18 anos.
B) Quantos Homens foram Cadastrados.
C) Quantas Mulheres tem menos de 20 Anos.

Assistir até: Aula 15
"""
registerMore = "S"
moreEighteenYears = 0
lessEighteenYearsWomen = 0
howManyMen = 0

while True:
    print("-" * 35)
    print("         CADASTRE UMA PESSOA")
    print("-" * 35)

    age = int(input("Idade: "))
    gender = str(input("Sexo: [M/F] ")).capitalize().strip()

    # Verifying the Condicionals.
    if age > 18:
        moreEighteenYears += 1
    if gender == "M":
            howManyMen += 1
    if gender == "F" and age < 20:
        lessEighteenYearsWomen += 1
    
    # Verifying if He/She Wants to Continue.
    print("-" * 35)
    registerMore = str(input("Quer Continuar? [S/N] ")).capitalize().strip()

    # End of the Program and Showing the Results.
    if registerMore != "S":
        print(" -=-=-=-= FIM DO PROGRAMA =-=-=-= ")
        print(f"Total de Pessoas com mais de 18 anos: {moreEighteenYears}")
        print(f"Total de Homens Cadastrados: {howManyMen}")
        print(f"Total de Mulheres com menos de 20 anos: {lessEighteenYearsWomen}")
        break
