# Boas Praticas em Python:

# List Comprehension: Evite criar listas vazias + append manual se puder simplificar.
lista = [
    {
        'nome': 'jose',
        'idade': 27,
        'sexo': 'M'
    },
    {
        'nome': 'joana',
        'idade': 27,
        'sexo': 'F'
    },{
        'nome': 'joana2',
        'idade': 27,
        'sexo': 'F'
    }
]

lista2 = [1,2,3,4,5]

fem = [x for x in lista if x['sexo'] == "F"]

print(fem)

# Faça Isso:
pares = [x for x in lista2 if x % 2 == 0]
# retorne cada valor (x) da lista se o valor (x) for par)

# Ao Invés disso: (Quando Conseguir)
par = []
for x in lista2:
    if x % 2 == 0:
        par.append(x)


print(type(9))