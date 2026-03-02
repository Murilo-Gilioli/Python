"""
DESAFIO 092

- (OK) Crie um programa que leia nome, ano de nascimento e carteira de trabalho. 
- (OK) se por acaso a CTPS for diferente de ZERO, o dicionario recebera tambem o ano de contratação e o salário.
- (OK) Calcule e acrescente, alem da idade, com quantos anos a pessoa vai se aposentar.
- (OK) cadastre-os (com idade) em um dicionario.


Assistir até: Aula 18
"""
from datetime import datetime
ano_atual = datetime.now().year
usuario = dict()

usuario['nome'] = str(input("Nome: ")).capitalize()
ano = int(input("Ano de Nascimento: "))
usuario['idade'] = ano_atual - ano
usuario['ctps'] = int(input("Carteira de Trabalho (0: Não Tem): "))

if usuario['ctps'] != 0:
    usuario['ano_contratacao'] = int(input("Ano de Contratação: "))
    usuario['salario'] = float(input("Salário: R$"))
    usuario['aposentadoria'] = 65 - usuario['idade']

print("-=" * 30)
for key, value in usuario.items():
    print(f" - {key} tem o valor {value}")



