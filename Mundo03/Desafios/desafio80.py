"""
DESAFIO 080

Crie um programa onde o usuario possa digitar cinco valores numericos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o Sort()).
No final, Mostre a lista ordenada na Tela.

Assistir até: Aula 17
"""
lista = []

for c in range(5):
    n = int(input("Digite um Valor: "))

    # se for o primeiro numero, ou o numero for maior que o ultimo da lista (lista[-1]), vai adicionar no final.
    if c == 0 or n > lista[-1]:
        lista.append(n)
    else:
        pos = 0

        while pos < len(lista):
            # se o numero for menor ou igual ao numero da lista, vai inserir na posição do mesmo o valor
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1
print(f"os valores digitados em ordem foram: {lista}")