"""
DESAFIO 020

O mesmo professor do desafio anterior quer sortear a ordem de apresentaçao de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

Assistir até: Aula 08
"""
import random;
a1 = str(input("Aluno 1: "))
a2 = str(input("Aluno 2: "))
a3 = str(input("Aluno 3: "))
a4 = str(input("Aluno 4: "))
list = [a1, a2, a3, a4]
random.shuffle(list)

print(f"A Ordem Sorteada Foi: {list}")