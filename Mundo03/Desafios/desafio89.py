"""
DESAFIO 089

Crie um programa que leia nome e duas notas de varios alunos e guarde tudo em uma lista composta. no final, mostre um boletim contendo a média de cada um e o permita que o usuario possa mostrar as notas de cada aluno individualmente

Assistir até: Aula 17²
"""
alunos = []

# Pegar o Nome e as Notas dos Alunos e coloca na Lista.
while True:
    nomealuno = str(input("Nome do Aluno: ")).capitalize().strip()
    nota1 = float(input("Primeira Nota: "))
    nota2 = float(input("Segunda Nota: "))
    alunos.append([nomealuno,[nota1,nota2]])

    res = str(input("Quer Continuar? [S/N] ")).capitalize().strip()
    if res == "N":
        break

# Prints dos Modelos do Boletim.
print("-" * 26)
print(f"{'Nº':<3} {'NOME':<10} {"MÉDIA":>10}")
print("-" * 26)

# Soma da Media e Print dos Alunos e Notas.
for pos, aluno in enumerate(alunos):
    notas = aluno[1]
    media = (notas[0] + notas[1]) / 2
    print(f"{pos:<3} {aluno[0]:<10} {media:10.2f}")

# Mostrar Notas dos Alunos Individualmente.
while True:
    print("-" * 30)
    student_number = int(input("Mostrar notas de qual aluno? (999 interrompe): "))

    for pos, aluno in enumerate(alunos):
        if pos == student_number:
            print(f"Notas de {alunos[pos][0]} são {alunos[pos][1]}")
        elif student_number == 999:
            break
        elif pos != student_number:
            print("Digite um Numero Válido!")
        
    # Finalização da Aplicação.
    if student_number == 999:
        print("FINALIZANDO...")
        print("<<< VOLTE SEMPRE >>>")
        break