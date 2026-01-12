"""
DESAFIO 068

Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

Assistir até: Aula 15
"""
from random import randint

print("-" * 35)
print("     VAMOS JOGAR PAR OU IMPAR     ")
print("-" * 35)

computer_Wins = 0
player_Wins = 0

while True:
    # Computer Configs.
    computer_Num = randint(0,10)
    computer_ParImpar = ""

    # Player Configs.
    player_Num = int(input("Digite um Valor: "))
    if player_Num < 0:
        player_Num = int(input("Digite um Valor: "))

    player_ParImpar = str(input("Par ou Impar? [P/I] ")).capitalize().strip()
    if player_ParImpar != "P" and player_ParImpar != "I":
        player_ParImpar = str(input("Par ou Impar? [P/I] ")).capitalize().strip()

    # Game Configs.
    par = (player_Num + computer_Num) % 2 == 0
    impar = (player_Num + computer_Num) % 2 == 1
    if player_ParImpar == "P":
        computer_ParImpar = "I"
    elif player_ParImpar == "I":
        computer_ParImpar = 'P'

    # The Result.
    print("-" * 25)
    print(f"Voce Jogou {player_Num} e o Computador {computer_Num}.")
    print("-" * 25)

    if player_ParImpar == "P" and par == True or player_ParImpar == "I" and impar == True:
        player_Wins += 1
        print("Você VENCEU!")
        print("-" * 25)
        print("Vamos jogar Novamente...")
    else:
        computer_Wins += 1
        print("Você PERDEU!")
        print("-" * 25)
        print(f"Voce Venceu {player_Wins} Vezes.")
        break