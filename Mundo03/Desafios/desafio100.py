"""
DESAFIO 100

Faça um programa que tenha uma lista chamada numeros e duas funções chamadas sorteia() e somaPar(). A Priemira função vai sortear 5 numeros e vai coloca-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior.

Assistir até: Aula 20
"""
from random import randint
from time import sleep
numeros = []

def sorteia(lista):
    print(f"Sorteando 5 Valores da Lista: ", end="")
    for i in range(5):
        randnumber = randint(0,10)
        lista.append(randnumber)
        print(randnumber, end=" ")
    print("PRONTO!")
sorteia(numeros)

def somaPar(lista):
    pares = [x for x in lista if x % 2 == 0]
    soma = 0
    for par in pares:
        soma += par
    print(f"Somando os valores pares de {numeros} temos {soma}")
somaPar(numeros)