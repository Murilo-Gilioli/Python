"""
DESAFIO 062

Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O Programa encerra quando ele disser que quer mostrar 0 Termos.

Assistir até: Aula 14
"""

print("=" * 30)
print("     10 TERMOS DE UMA P.A      ")
print("=" * 30)

first = int(input("Primeiro Termo: "))
num = int(input("Razão: "))
terms = 10


while terms != 0:
    print(first, end=" → ")
    first += num
    terms -= 1
    if terms == 0:
        print()
        print("Voce Gostaria de Colocar mais alguns Termos? se sim, Coloque a Quantidade, Caso nao, Coloque 0")
        terms += int(input("→ "))
print("FIM!")