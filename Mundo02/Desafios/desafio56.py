"""
DESAFIO 056

Desenvolva um programa que leia o "Nome", "Idade" e "Sexo" de 4 pessoas. No final do programa, Mostre:

> a Média de idade do Grupo.
> Qual é o Nome do Homem mais Velho.
> Quantas Mulheres tem menos de 20 anos.

Assistir até: Aula 13
"""
soma = 0
media_Age = 0
oldest_Age = 0
oldest_Name = ""
younger_Women = 0

for people in range(1,5):
    # Pega o Nome, Idade e o Genero das Pessoas.
    print(f"----- {people}ª Pessoa -----")
    name = str(input("Nome: ")).title().strip()
    age = int(input("Idade: "))
    gender = str(input("Genero (F/M): ")).title().strip()

    # Nome e Idade do Homem mais Velho (Encontrado).
    if gender == "M" and age > oldest_Age:
        oldest_Age = age
        oldest_Name = name

    # Quantas Mulheres tem menos de 20 Anos (Encontrado).
    if gender == "F" and age < 20:
        younger_Women += 1

# Media de Idade (Calculada).
soma += age
media_Age = soma / 4

print(f"a Media de idade desse grupo é de {media_Age} Anos.")
print(f"o Homem mais Velho desse grupo tem {oldest_Age} Anos e se Chama {oldest_Name}.")
print(f"ao Todo há {younger_Women} Mulheres com menos de 20 anos.")