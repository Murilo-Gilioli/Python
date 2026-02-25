"""
DESAFIO 090

Faça um programa que leia nome e média de um aluno. guardando tambem a situação em um dicionario. No final, mostre o conteudo da estrutura na tela.

Assistir até: Aula 18
"""

aluno = {}

aluno['nome'] = str(input("Nome: "))
aluno['media'] = float(input(f"Media do {aluno['nome']}: "))

if aluno['media'] >= 7:
    aluno['situacao'] = "Aprovado"
else:
    aluno['situacao'] = "Reprovado"

print(f"Nome é igual a {aluno['nome']}")
print(f"Media é igual a {aluno['media']}")
print(f"Situação é igual a {aluno['situacao']}")