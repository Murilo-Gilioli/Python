"""
DESAFIO 095

Aprimore o desafio 093 para que ele funcione com vários jogadores, incluindo um sistema de visualizaçao de detalhes do aproveitamento de cada jogador

Assistir até: Aula 18
"""
jogadores = []
jogador = {}
gols = []

while True:
    jogador['nome'] = input("Nome: ").strip().capitalize()
    partidas = int(input("Quantidade de Partidas: "))

    for gol in range(partidas):
        gols.append(int(input(f"{'':>3}Quantos Gols na {gol + 1}ª Partida: ")))

    jogador['gols'] = gols
    jogador["total"] = sum(gols)
    jogadores.append(jogador.copy())
    
    res = input("Quer Continuar? [S/N] ").strip().upper()
    if res in ["N"]:
        print("Acabou")
        break

print("-=" * 30)
print(f"{"cod"} {"nome"} {"gols":>15} {"total":>20}")
print("-" * 50)

for casa,jogador in enumerate(jogadores):
   print(f"{casa:<3} {jogador['nome']:<15} {str(jogador['gols']):<15} {jogador['total']:>10}")

while True:
    show = int(input("Mostrar dados de qual Jogador? (999 para Parar): "))
    if show in [999]:
        break
    if show >= len(jogadores):
        print(f"ERRO! Nao existe jogador com código {show}")
    else:
        print(f"-- LEVANTAMENTO DO JOGADOR {jogadores[show]['nome']}:")
        for i in range(len(jogadores[show]['gols'])):
            print(f"no jogo {i + 1} fez {jogadores[show]['gols'][i]} gols.")