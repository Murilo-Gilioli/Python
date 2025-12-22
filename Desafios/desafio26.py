"""
DESAFIO 026

Faça um programa que leia uma frase pelo teclado e mostre:

- Quantas vezes aparece a letra "A".
- Em que Posição ela aparece a primeira vez.
- Em que Posição ela aparece a ultima vez.

Assistir até: Aula 09
"""
sentence = str(input("Digite sua Frase: ")).strip().upper()
aCounts = sentence.count('A')
firstTime = sentence.find('A')
lastTime = sentence.rfind('A')

if aCounts != 0:
    print(f"Nessa Frase a Letra 'A' apareceu {aCounts} vezes.")
    print(f"Nessa Frase a Letra 'A' apareceu pela Primeira vez na Posição {firstTime}.")
    print(f"Nessa Frase a Letra 'A' apareceu pela Ultima vez na Posição {lastTime}.")
else:
    print("Essa frase nao tem a letra 'A'")