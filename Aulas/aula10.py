n1 = float(input("Digite a Primeira Nota: "))
n2 = float(input("Digite a Segunda Nota: "))
media = (n1 + n2) / 2
print(f"{media:.1f}")

if media >= 5:
    print("sua Nota está acima da Média!")
else:
    print("Sua Nota está abaixo da Média!")