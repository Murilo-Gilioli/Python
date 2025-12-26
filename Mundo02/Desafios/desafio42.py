"""
DESAFIO 042

Refaça o DESAFIO 035 dos triangulos, acrescentando o recurso de mostrar que tipo de triangulo sera formado:

- Equilátero: todos os lados Iguais.
- Isósceles: dois lados iguais.
- Escaleno: Todos os lados diferentes.

Assistir até: Aula 12
"""
colors = {
    'red_Color': '\033[31m',
    'green_Color': '\033[32m',
    'yellow_Color': '\033[33m',
    'default_Color': '\033[37m'
}

print('Digite 3 comprimentos de uma Reta!')
l1 = float(input('Primeira Reta: '))
l2 = float(input('Segunda Reta: '))
l3 = float(input('Terceira Reta: '))

first_Test = l1 + l2 > l3
second_Test = l2 + l3 > l1
third_Test = l1 + l3 > l2

if first_Test and second_Test and third_Test:
    print('É Possivel fazer um Triangulo com essas Retas.')

    if l1 == l2 and l1 == l3:
        print(f'E ele seria um Triangulo {colors["red_Color"]} Equilátero. {colors["default_Color"]}')
    elif l1 == l2 or l1 == l3:
        print(f'E ele seria um Triangulo {colors["green_Color"]} Isósceles. {colors["default_Color"]}')
    elif l1 != l2 and l1 != l3:
        print(f'E ele seria um Triangulo {colors["yellow_Color"]} Escaleno. {colors["default_Color"]}')
else:
    print('nao é Possivel fazer um Triangulo com essas Retas')