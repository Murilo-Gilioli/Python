"""
DESAFIO 059

Crie um Programa que leia dois valores e mostre um menu na tela:

[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos Números
[5] Sair do Programa

Seu programa deverá realizar a operaçao solicitada em cada caso.

Assistir até: Aula 13
"""

print('Digite Dois Valores Numéricos!')

v1 = int(input("Primeiro Valor: "))
v2 = int(input("Primeiro Valor: "))
print('Qual Ação Voce gostaria de Realizar com seus Numeros?')
print('\033[32m[1] Somar \033[37m')
print('\033[33m[2] Multiplicar \033[37m')
print('\033[34m[3] Maior \033[37m')
print('\033[35m[4] Novos Números \033[37m')
print('\033[36m[5] Sair do Programa \033[37m')

menuOption = int(input(": "))

while menuOption != 5:
    if menuOption == 1:
        print(f"a \033[32mSoma\033[37m entre eles é: {v1 + v2}")
        print(" ")
        print('Qual Ação Voce gostaria de Realizar com seus Numeros?')
        menuOption = int(input(": "))

    if menuOption == 2:
        print(f"a \033[33mMultiplicação\033[37m entre eles Resulta em: {v1 * v2}")
        print(" ")
        print('Qual Ação Voce gostaria de Realizar com seus Numeros?')
        menuOption = int(input(": "))

    if menuOption == 3:
        if v1 > v2:
            print(f"o \033[34mMaior\033[37m Valor entre eles é o: {v1}")
        else:
            print(f"o \033[34mMaior\033[37m Valor entre eles é o: {v2}")
        print(" ")
        print('Qual Ação Voce gostaria de Realizar com seus Numeros?')
        menuOption = int(input(": "))

    if menuOption == 4:
        v1 = int(input("Primeiro Valor: "))
        v2 = int(input("Segundo Valor: "))
        print(f"Seus \033[35mNovos Números\033[37m Agora sao: {v1} e {v2}")
        print(" ")
        print('Qual Ação Voce gostaria de Realizar com seus Novos Numeros?')
        print('\033[32m[1] Somar \033[37m')
        print('\033[33m[2] Multiplicar \033[37m')
        print('\033[34m[3] Maior \033[37m')
        print('\033[35m[4] Novos Números \033[37m')
        print('\033[36m[5] Sair do Programa \033[37m')
        menuOption = int(input(": "))
        
print("Você \033[36mSaiu do Programa\033[37m, Obrigado por Utilizar Nosso Programa!")
