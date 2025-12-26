"""
DESAFIO 044

Elabora um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

- à vista dinheiro/cheque: 10% de Desconto.
- à vista no cartao: 5% de Desconto.
- em até 2x no cartao: Preço Normal.
- 3x ou mais no cartao: 20% de Juros.

Assistir até: Aula 12
"""

product_Value = float(input("Qual o Valor do Produto? "))
print("1 - à vista dinheiro/cheque: 10% de Desconto.")
print("2 - à vista no cartao: 5% de Desconto.")
print("3 - em até 2x no cartao: Preço Normal.")
print("4 - 3x ou mais no cartao: 20% de Juros.")
payment_Method = int(input("Qual seria a Forma de Pagamento? "))

if payment_Method == 1:
    discount = 10 / 100 * product_Value
    print(f"O valor a Pagar com o Desconto Ficará em R${product_Value - discount:.3f}")
elif payment_Method == 2:
    discount = 5 / 100 * product_Value
    print(f"O valor a Pagar com o Desconto Ficará em R${product_Value - discount:.3f}")
elif payment_Method == 3:
    print(f"O valor a Pagar Ficará em R${product_Value:.3f}")
elif payment_Method == 4:
    interest = 20 / 100 * product_Value
    print(f"O valor a Pagar com os Juros Ficará em R${product_Value + interest:.3f}")