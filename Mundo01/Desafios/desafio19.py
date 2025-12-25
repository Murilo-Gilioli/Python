"""
DESAFIO 019

Um professor quer sortear um dos seus quatro alunos para apagar o quadro, Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

Assistir até: Aula 08
"""
import random
a1 = str(input("Aluno 1: "))
a2 = str(input("Aluno 2: "))
a3 = str(input("Aluno 3: "))
a4 = str(input("Aluno 4: "))

print(random.choice([a1,a2,a3,a4]))