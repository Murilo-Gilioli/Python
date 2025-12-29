"""
for count in range(inicio, fim, iteraçao):
    açao
termina

for count in range(0,3):
    passo
    pula
passo
pega

for count in range(0,3):
    if moeda:
        pegar
    passo
    pula
passo
pega
"""
numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

for c in range(0, len(numeros), 1):
    print(c)
print("FIM")

n = int(input("Digite um Numero: "))
n2 = int(input("Digite um Numero: "))

for c in range(n, n2+1):
    print(c)