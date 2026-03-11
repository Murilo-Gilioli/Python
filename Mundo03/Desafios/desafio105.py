"""
DESAFIO 105

Faça um programa que tenha uma função chamada notas() que recebe varias notas de alunos e vai retornar um dicionario com as seguintes informações:

- Quantidade de Notas
- A maior Nota
- A menor Nota
- A média da Turma
- A Situação (Opcional)

Adicione tambem as Docstrings da Função.

Assistir até: Aula 21
"""
def notas(*num, sit=False):
    nota = {}
    nota['total'] = len(num)
    nota['maior'] = max(num)
    nota['menor'] = min(num)
    nota['media'] = sum(num) / len(num)

    if sit == True:
        if nota['media'] >= 7:
            nota['situação'] = "BOA"
        elif nota['media'] >= 5:
            nota['situação'] = "RAZOAVEL"
        else:
            nota['situação'] = "RUIM"

    return nota


val = notas(85,2,30,0,0,0)
print(val)