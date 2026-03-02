"""
DESAFIO 094

Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionario e todos os dicionarios em uma lista. no final, mostra:

A) Quantas pessoas foram cadastradas.
B) A Média de idade do grupo.
C) Uma lista com todas as mulheres.
D) Uma lista com todas as pessoas com idade acima da média

Assistir até: Aula 18
"""
person = {}
people_list = []
women_list = []

while True:
    # Ler Nome, Sexo, Idade, colocar dentro de um dicionario e colocar dentro de uma Lista (OK)
    person['nome'] = str(input("Nome: ")).strip().capitalize()
    person['sexo'] = str(input("Sexo: [M/F] ")).strip().upper()

    # Verificação de Valores (M (Masculino) ou F (Feminino));
    while person['sexo'] not in ["M", "F"]:
        print("ERRO! Por Favor, digite apenas M ou F.")
        person['sexo'] = str(input("Sexo: [M/F] ")).strip().upper()

    person['idade'] = int(input("Idade: "))    

    # Se for Mulher, Adiciona em uma Lista Separada.
    if person["sexo"] == "F":
        women_list.append(person.copy())
    people_list.append(person.copy())

    # Verificação de Valores (S (Sim) ou N (Não));
    res = str(input("Quer Continuar? [S/N] ")).strip().upper()
    while res not in ["S", "N"]:
        print("ERRO! Responda apenas com S ou N.")
        res = str(input("Quer Continuar? [S/N] ")).strip().upper()

    if res == 'N':
        print("-=" * 30)
        break

# A) Quantas pessoas foram cadastradas. (OK)
print(f"A) Ao todo temos {len(people_list)} pessoas cadastradas.")

# B) A Média de idade do grupo (OK).
soma = 0
media = 0

for pessoa in people_list:
    soma += pessoa['idade']
    media = soma / len(people_list)
print(f"B) A média de idade é de {media} anos.")

# C) Uma lista com todas as mulheres. (OK)
print(f"C) As mulheres cadastradas foram:", end="")
for woman in women_list:
    print(f" {woman['nome']}", end="") 

# D) Uma lista com todas as pessoas com idade acima da média
print()
print("D) Lista das pessoas que estão acima da media:")
for person in people_list:
    if person['idade'] > media:
        print(f"{"":>4}nome = {person['nome']}; sexo = {person['sexo']}; idade = {person['idade']}")
    

print("<< ENCERRADO >>")