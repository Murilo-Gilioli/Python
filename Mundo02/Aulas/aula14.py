"""
while not apple:
    passo
pega

while not apple:
    if path:
        walk
    if hole:
        jump
    if coin:
        pick up
pick up


"""
r = "S"

while r == "S":
    n = int(input("Digite um valor: "))
    r = str(input("Quer Continuar? [S/N] ")).upper()
print("FIM")

n = 1

par = impar = 0
while n != 0:
    n = int(input("Digite um Numero: "))
    if n != 0:
        if n % 2 == 0:
            par += 1
        elif n % 2 == 1:
            impar += 1

print(f"Voce digitou {par} Numeros pares e {impar} Numeros impares.")