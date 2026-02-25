"""
Variaveis Compostas (Tuplas, Listas e Dicionarios)

Listas: um Array do Python '[]',
ela é uma Variavel com Varios Itens que podem ter varios itens dentro dela.

lista.append("Item") - Adiciona um Item no final da Lista.

lista.pop(0) - Remove o Valor da Casa Escolhida.
0: é a Casa em que voce quer Remover o Valor.

del lista[0] - Remove o Valor pela Casa Escolhida.
0: é a Casa em que voce quer Adicionar o Valor.

lista.pop("Item") - Remove o Item de Acordo com o Valor Inserido.
lista.pop(0) - Remove o Item de Acordo com a Casa Inserida.
lista.pop() - Remove o Ultimo item da Lista.

lista.insert(0, "Item") - Adiciona um Item na Casa Escolhida.
0: é a Casa em que voce quer Adicionar o Valor.
"Item": é o Valor que voce vai Adicionar na Casa Acima.
"""

lanche = ["Lanche", "Suco", "Pizza"]

if "Pizza" in lanche:
    lanche.remove('Pizza')
    print("Pizza Removida!")
print(lanche)

# Como Criar uma Lista atraves de um Range.
valores = list(range(4,11))
# Ele vai criar uma Lista, com os Valores de 4 até 10;

valores2 = [1,4,5,6,7,8,2,3]

valores2.sort() # Organiza os Valores em Ordem.

print(valores2)

valores2.sort(reverse=True) # Organiza os Valores em Ordem Inversa.

len(valores2) # Mostra Quantas Casas Tem a Lista (Comprimento).