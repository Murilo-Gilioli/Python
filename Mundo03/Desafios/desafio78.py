"""
DESAFIO 078

Faça um programa que leia 5 valores numéricos e guarde-os em uma Lista.

No Final, mostre qual foi o Maior e o Menor Valor Digitado e as Suas Respectivas Posições na Lista.

Assistir até: Aula 17
"""
valores = []
maior = menor = 0

# Como Achar o Maior e Menor Valor com Método:
for valor in range(0,5):
    valores.append(int(input(f"{valor + 1}º Número: ")))  
    maior = max(valores)
    menor = min(valores)

# Como Achar o Maior e Menor Valor na Mão:
for valor in range(0,5):
    valores.append(int(input(f"{valor + 1}º Número: ")))  
    if maior == 0 and menor == 0:
        maior = menor = valores[0]
    if valores[valor] > maior:
        maior = valores[valor]
    elif valores[valor] < menor:
        menor = valores[valor]
    
print(f"o Maior Valor Digitado foi: {maior}, e está na posição: {valores.index(maior)}")
print(f"o Maior Valor Digitado foi: {menor}, e está na posição: {valores.index(menor)}")