"""
DESAFIO 083

Crie um programa onde o usuario digite uma expressao qualquer que use parenteses. seu aplicativo deverá analisar se a expressao passada está com os parenteses abertos e fechados na ordem correta.

Assistir até: Aula 17
"""
expression = str(input("Digite a expressão: "))
expression_list = []

for l in expression:
    expression_list.append(l)

if expression_list.count("(") == expression_list.count(")"):
    print("Sua expressão está Correta!")
else:
    print("Sua expressão está Errada!")
