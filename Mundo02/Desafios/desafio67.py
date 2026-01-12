"""
DESAFIO 067

Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O Programa será interrompido quando o número solicitado for Negativo.

Assistir até: Aula 15
"""
c = 1
n = 0

print("-" * 20)
print("     TABUADA     ")
print("-" * 20)

while True:
    print()
    n = int(input("Digite um Numero: "))
    print()
    c = 1

    # Tabuada.
    if n >= 0:
        while c <= 10:
            print(f"{n} x {c} = {n * c}")
            c += 1   

    # Break          
    elif n < 0:
        break
    
    
    
print("Acabou.")
