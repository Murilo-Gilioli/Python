"""
DESAFIO 053

Crie um programa que leia uma frase qualquer e diga se ela é um polindromo, desconsiderando os espaços.

EX: 
APOS A SOPA.
A SACADA DA CASA.
A TORRE DA DERROTA.
O LOBO AMA O BOLO.
ANOTARAM A DATA DA MARATONA.

Assistir até: Aula 13
"""
first_Text = str(input("Escreva uma frase: ")).strip().split()
textNoSpace = "".join(first_Text).upper()
comparation_Text = ""

for c in range(len(textNoSpace) -1, -1, -1):
    comparation_Text += textNoSpace[c]

print(f"o Contrario de {textNoSpace} é {comparation_Text}")

if comparation_Text == textNoSpace:
    print("a Frase Digitada é um Polindromo")
else:
    print("a Frase Digitado nao é um Polindromo")