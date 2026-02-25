"""
Variaveis Compostas (Tuplas, Listas e Dicionarios)

Tupla: um "Array-Const" de Python (),
uma Variavel com Varios Itens que nao podem ser modificados durante a Aplicaçao, e que Aceita Varios Tipos Dentro Da Mesma Tupla.
as tuplas sao IMUTÁVEIS.
"""

lanche = ("hambrugue", "Cerveja", "Pitiça", "Pudim")

# Formas de Fazer um "For" com a Tupla:
for c in lanche:
    print(c)

for pos, comida in enumerate(lanche):
    print(comida, pos)

for cont in range(0, len(lanche)):
    print(lanche[cont])

# Organiza a Tupla:
print(sorted(lanche))

# Concatenaçao de Tuplas:
a = (2,5,4)
b = (5,8,1,2)
c = a + b

# Alguns Metodos de Tuplas:
print(c.count(4)) # Mostra quantas vezes o Valor Apareceu

print(c.index(4, 0)) # Mostra em Qual Casa o Valor Está (ele pega o primeiro que aparecer, caso tenha mais de um)

# del() - Apaga Algo dentro de Python, e Tambem Consegue apagar a Tupla Toda.
pessoa = ("Murilo", 21, "M", 57.50, True)
del(pessoa)
print(pessoa)