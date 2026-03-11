"""
DESAFIO 106

Faça um mini-sistema que utilize o Interactive Help do Python. O Usuario vai digitar o comando e o manual vai aparecer. Quando o usuario digitar a palavra "FIM", o programa se encerrará.

OBS: use cores.

Assistir até: Aula 21
"""
def header(title, color=None):
    print(f"\033[{color}m~" * len(title))
    print(f"{title}")
    print("~" * len(title), "\033[35m")

def helpFunction(item):
    return help(item)

while True:
    header(f"SISTEMA DE AJUDA PyHELP", color=31)
    res = str(input(f"\033[37mFunção ou Biblioteca > "))
    if res.upper() in ["FIM"]:
        break
    header(f"Acessando o manual do comando '{res}'", color=32)
    helpFunction(res)

    