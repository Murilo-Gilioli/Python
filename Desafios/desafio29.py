"""
DESAFIO 029

Escreva um programa que Leia a velocidade de um Carro.

se ele ultrapassar os 80km/h, mostre uma mensagem dizendo que ele foi multado.

a multa vai custar R$7,00 Por cada KM acima do Limite de Velocidade.

Assistir até: Aula 10
"""

vel = int(input("Digite a Velocidade de um Carro: "))

if vel > 80:
    multa = (vel - 80) * 7
    print(f"Voce Ultrapassou o Limite de Velocidade de 80KM/h! irá ser Multado no Valor de: R${multa}")
else:
    print("Voce está dentro do Limite de Velocidade.")