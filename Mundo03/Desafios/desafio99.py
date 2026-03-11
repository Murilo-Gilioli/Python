"""
DESAFIO 099

Faça um programa que tenha uma função chamada maior(), que receba vários parametros com valores inteiros.

Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

Assistir até: Aula 20
"""
def maior(*numeros):
    print("-" * 30)
    print("Analisando os Valores passados...")

    if len(numeros) == 0:
        print("Nao Houve Valores Informados.")

    else:
        maior = 0
        maior = numeros[0]
        for num in numeros:
            print(f"[{num}]", end=" ")
            if num > maior:
                    maior = num
        print(f"- Foram informados {len(numeros)} valores ao Todo")            
        print(f"O maior valor informado foi {maior}.")

maior(9,3,6,5,9,1,0,213,24)
maior(28,34,56,1,25,8,23,2)
maior(98,2,4,6)
maior(95,8)
maior(1)
maior()