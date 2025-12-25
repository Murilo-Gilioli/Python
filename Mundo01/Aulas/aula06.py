"""
# from biblioteca import ... (importa apenas o item desejado da biblioteca)
# import biblioteca (importa todos os itens da biblioteca)

math.ceil() - Arredonda o Numero para Cima.
math.floor() - Arredonda o Numero para Baixo.
math.sqrt() - Faz a Raiz Quadrada do Numero.
""" 

import math;

num = int(input("digite um Numero: "))
raiz = math.sqrt(num)
print(math.floor(raiz))