# Funções

def mostraLinha():
    print("-" * 30)
mostraLinha()

def titulo(title):
    print('-' * 30)
    print(f"{title:^30}")
    print('-' * 30)
titulo("Alunos")

def soma(a,b):
    s = a + b
    print(s)
soma(5,6)

# Empacotamento

def contador(*num):
    print(num)
contador(1,2,3,4)

def somas(*num):
    s = 0
    for valor in num:
        s += valor
    print(f"Somando todos os valores de {num}, resulta em {s}")
somas(1,3,5)
somas(8,3,5)

# Funçao com Lista

def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1

valores = [1,2,3,4,5]
dobra(valores)
print(valores)