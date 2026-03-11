"""
Variaveis Compostas (Tuplas, Listas e Dicionarios)

Dicionarios: um Objeto do Python '{}',
ela é uma Variavel que pode ter Varios itens e ela tem Identificadores ao invés de Casas/Indices
"""
# Dicionario:
dados = {'nome': 'Pedro', 'idade': 25}

# Printar Dicionarios:
print(dados['idade'])

# Como Adicionar Itens no Dicionario:
dados['sexo'] = "M"
print(dados)

# Como remover Itens do Dicionario:
del dados["idade"]
print(dados)

# Estrutura:

filme = {
    # Key       Values
    'titulo': "Star Wars",
    'ano': 1997,
    'diretor': 'George Lucas'
}

print(filme)

# Como separar somente os Valores / Values:
print(filme.values())

# Como separar somente as Chaves / Keys:
print(filme.keys())

# Como separar pelas Chaves e Pelos Valores:
print(filme.items())

for k,v in filme.items():
    print(f"O {k} é {v}")

# Dicionarios dentro de uma Lista:
locadora = [
    {
        'titulo': "Star Wars",
        'ano': 1997,
        'diretor': 'George Lucas'
    },
    {
        'titulo': "Avengers",
        'ano': 2012,
        'diretor': 'Joss Whedon'
    },
    {
        'titulo': "Matrix",
        'ano': 1999,
        'diretor': 'Wachowski'
    }
]
print(locadora[0]['ano'])

################################

estado = {}
brasil = []

for c in range(3):
    estado['uf'] = str(input("Unidade Federativa: "))
    estado['sigla'] = str(input("Sigla do Estado: "))
    brasil.append(estado.copy())

for e in brasil:
    for v in e.values():
        print(f"{v}", end=' ')
    print()