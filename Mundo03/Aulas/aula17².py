pessoas = []
galera = []

 # Para fazer uma copia perfeita da lista, utilize [:], por exemplo galera.append(pessoas[:]), caso voce altere algum valor de "pessoas", nao irá mudar dentro de galera

for c in range(2):
    pessoas.append(str(input("Nome: ")))
    pessoas.append(int(input("Idade: ")))
    galera.append(pessoas[:])
    pessoas.clear()

for pessoa in galera:
    if pessoa[1] >= 21:
        print(f"{pessoa[0]} é Maior de idade.")
    else:
        print(f"{pessoa[0]} é Menor de idade")
