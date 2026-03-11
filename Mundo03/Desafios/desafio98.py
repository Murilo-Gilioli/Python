"""
DESAFIO 098

Faça um programa que tenha uma função chamada contador(), que receba tres parametros: inicio, fim e passo e realize a contagem.

Seu programa tem que realizar tres contagens através da função criada:

A) de 1 até 10, de 1 em 1
B) de 10 até 0, de 2 em 2
C) Uma Contagem personalizada.

Assistir até: Aula 20
"""
from time import sleep
def contador(ini, fim, passo):
    if passo == 0:
        passo = 1

    if ini > fim and passo > 0:
        passo = -passo
    elif ini < fim and passo < 0:
        passo = -passo

    print(f"Contagem de {ini} até {fim} de {passo} em {passo}")    

    if passo > 0:
        fim += 1
    elif passo < 0:
        fim -= 1 

    for i in range(ini,fim,passo):
        print(i, end=" ")
    print("FIM!")

contador(1,10,1)
contador(10,0,2)

inicio = int(input("Inicio: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))
contador(inicio,fim,passo)
