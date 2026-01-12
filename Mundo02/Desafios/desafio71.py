"""
DESAFIO 071

Crie um programa que simule o funcionamento de um Caixa Eletrônico. no inicio, pergunte ao usuário qual será o valor a ser sacado (Número Inteiro) e o Programa vai informar quantas cédulas de cada valor serão entregues.

OBS: Considere que o caixa possui cédulas de R$1, R$10, R$20 e R$50. 

Assistir até: Aula 15

------------------------------

por50 = valor % 50
por502 = valor // 50
print(por50, por502, "50")

por20 = por50 % 20
por202 = por50 // 20
print(por20, por202, "20")

por10 = por50 % 10
por102 = por50 // 10
print(por10, por102, "10")

por1 = por50 % 1
por12 = por50 // 1
print(por1, por12, "10")
--------------------------------

# Notas de 50:
if valor % 50 == 0:
    nota50 = valor // 50
    valor = valor % 50
elif valor % 50 != 0:
    nota50 = valor // 50
    valor = valor % 50

# Notas de 20:
if valor % 20 == 0:
    nota20 = valor // 20
    valor = valor % 20
elif valor % 20 != 0:
    nota20 = valor // 20
    valor = valor % 20

# Notas de 10:
if valor % 10 == 0:
    nota10 = valor // 10
    valor = valor % 10
elif valor % 10 != 0:
    nota10 = valor // 10
    valor = valor % 10
    
# Notas de 1:
if valor % 1 == 0:
    nota1 = valor // 1
    valor = valor % 1
elif valor % 1 != 0:
    nota1 = valor // 1
    valor = valor % 1
"""
valor = 296
total = valor
ced = 50
totced = 0

while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f"total de {totced} cédulas de R${ced}")
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break