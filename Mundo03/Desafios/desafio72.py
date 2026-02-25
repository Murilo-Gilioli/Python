"""
DESAFIO 072

Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de 0 até 20.
seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

Assistir até: Aula 16
"""

numbers = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','one','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
num = int(input("Digite um Numero [Entre 0 e 20] "))

while True:
    if num < 0 or num > 20:
        num = int(input("Tente Novamente, Digite um Numero [Entre 0 e 20] "))
    else:
        print(f"Voce Digitou o Numero {numbers[num]}")
        break