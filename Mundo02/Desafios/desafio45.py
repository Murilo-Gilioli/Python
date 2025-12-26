"""
DESAFIO 045

Crie um Programa que faça o computador jogar Jokenpô com voce.

Assistir até: Aula 12
"""
import random;
jokenpo = ["Pedra","Papel","Tesoura"]
computer = random.choice(jokenpo)

print("==" * 10)
print("VAMOS JOGAR JOKENPO!")
print("==" * 10)

print("Escolha um e Veremos quem Irá Ganhar.")
print("Pedra, Papel, Tesoura")
player = str(input(": ").strip().capitalize())

player_Win1 = player == "Pedra" and computer == "Tesoura"
player_Win2 = player == "Tesoura" and computer == "Papel"
player_Win3 = player == "Papel" and computer == "Pedra"

computer_Win1 = computer == "Pedra" and player == "Tesoura"
computer_Win2 = computer == "Tesoura" and player == "Papel"
computer_Win3 = computer == "Papel" and player == "Pedra"

if computer_Win1 or computer_Win2 or computer_Win3:
    print(f"Eu Ganhei! {computer} Vence de {player}! ")
elif player_Win1 or player_Win2 or player_Win3:
    print(f"Voce Ganhou! \033[31m{player} Vence de {computer}\033[37m")
elif player == computer:
    print(f"Deu Empate! {computer} Empata com {player}")