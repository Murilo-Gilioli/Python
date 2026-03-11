"""
DESAFIO 101

Crie um programa que tenha uma função chamada voto() que vai receber como parametro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATORIO nas eleições

Assistir até: Aula 21
"""
from datetime import datetime
ano_atual = datetime.now().year

def voto(year):
    idade = ano_atual - year
    if idade >= 18 and idade <= 70:
        return f"com {idade} anos: Voto Obrigatorio"
    elif idade > 70:
        return f"com {idade} anos: Voto Opcional"
    else:
        return f"com {idade} anos: Voto Negado"

print(voto(2004))