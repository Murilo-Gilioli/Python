"""
DESAFIO 097

Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parametro e mostre uma mensagem com tamanho adaptável.

Ex: 
escreva('Olá, Mundo!')

Saida:
~~~~~~~~~~~
Olá, Mundo!
~~~~~~~~~~~

Assistir até: Aula 20
"""
def escreva(txt, tam):
    print("~" * tam)
    print(f"{txt:^{tam}}")
    print("~" * tam)

# OU

def escreva(txt):
    print("~" * len(txt))
    print(f"{txt:^{len(txt)}}")
    print("~" * len(txt))

texto = input("Mensagem: ")
escreva(texto)