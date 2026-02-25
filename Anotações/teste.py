valores = []
# print(valores)
# valores.remove(2)
# print(valores)

# while 2 in valores:
#     valores.remove(2)
# print(valores)

# for valor in range(0,5):
#     valores.append(int(input("Digite um Valor: ")))

# for c,v in enumerate(valores):
#     print(f"Valor: {v} na Casa: {c}...")
# print("Cheguei ao Final da Lista")

a = [2,3,4,7]
b = a[:]
b[2] = 8

valor = []
valorEx = [
    ["mari", [3,4]],
    ["maria", [5,6]],
    ["marias", [7,8]],
    ["mariasd", [9,10]]
]

valor1 = "joao"
valor2 = 1
valor3 = 2

valor.append([valor1, [valor2, valor3]])

print(valorEx)

for pos, valor in enumerate(valorEx):
    print(pos)

# print(f"{pos:<3} {aluno[0]:<10} {media:>10}") -- Alinha a Esquerda, Direita...












"""
    aluno = []
    nota = []
    aluno.append(nomealuno)
    nota.append(nota1)
    nota.append(nota2)
    aluno.clear()
    nota.clear()
"""