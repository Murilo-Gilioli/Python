"""
DESAFIO 065

Crie um programa que leia vários numeros inteiros pelo teclado. no final da execução, mostre a média entre todos os valores e qual foi o maior e o menor dos valores lidos. o programa deve perguntar ao usuário se ele quer ou nao continuar a Digitar Valores.

Assistir até: Aula 14
"""
number = int(input("Digite um Numero: "))
newNumbers = 'S'
count = soma = 0
maior = menor = 0

while newNumbers != "N":
    count += 1
    soma += number
    newNumbers = str(input("Quer Continuar Digitando Novos Valores? (S / N) ")).upper()

    # Maior e Menor Valor (Encontrado)
    if count == 1:
        maior = menor = number
    else:
        if number > maior:
            maior = number
        elif number < menor:
            menor = number
        
    # Continuar Digitando? (Verificado)
    if newNumbers != 'N':
        number = int(input("Digite outro Numero: "))

print(f"o Maior valor encontrado foi de {maior}")
print(f"o Menor valor encontrado foi de {menor}")

# Média entre os Valores (Calculado)
print(f"a Média entre todos os Valores foi de: {soma / count}") 