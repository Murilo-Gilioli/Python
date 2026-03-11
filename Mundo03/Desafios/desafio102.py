"""
DESAFIO 102

Crie um programa que tenha uma função fatorial() que receba dois parametros: o primeiro que indique o numero a calcular e o outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou nao na tela o processo de cálculo do fatorial.

Assistir até: Aula 21
"""
def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um número;
    :param num: Int - O numero a ser calculado
    :param show: Boolean - (opcional) Mostrar ou nao a conta
    """
    f = 1
    print("-" * 30)    
    for c in range(num,0,-1):
        f = f*c
        if show == True:
            if c == 1:
                print(c, end=" = ")
            else:
                print(c, end=" x ")
    
    print(f)
help(fatorial)