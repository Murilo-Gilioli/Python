# Boas Praticas em Python:

# List Comprehension: Evite criar listas vazias + append manual se puder simplificar.
lista = [
    {
        'nome': 'jose',
        'idade': 27,
        'sexo': 'M'
    },
    {
        'nome': 'joana',
        'idade': 27,
        'sexo': 'F'
    },{
        'nome': 'joana2',
        'idade': 27,
        'sexo': 'F'
    }
]

lista2 = [1,2,3,4,5]

fem = [x for x in lista if x['sexo'] == "F"]

print(fem)

# Faça Isso:
pares = [x for x in lista2 if x % 2 == 0]
# retorne cada valor (x) da lista se o valor (x) for par)

# Ao Invés disso: (Quando Conseguir)
par = []
for x in lista2:
    if x % 2 == 0:
        par.append(x)





"""
:brain: in e not in
:white_check_mark: in → significa:

"está dentro"

:white_check_mark: not in → significa:

"não está dentro"

:dart: Aplicando no seu caso

Você quer validar se o sexo é válido (M ou F).

✔ Forma negativa (mais comum para erro):
```
if pessoa['sexo'] not in ["M", "F"]:
    print("Sexo inválido")
```
Isso significa:

Se NÃO estiver entre M ou F → erro

✔ Forma positiva (o que você perguntou)

Sim, pode usar in normalmente:
```
if pessoa['sexo'] in ["M", "F"]:
    print("Sexo válido")
```
Aqui significa:

Se estiver entre M ou F → válido

:fire: Exemplo prático com loop de validação

Forma mais comum:
```
pessoa['sexo'] = input("Sexo: [M/F] ").strip().upper()

while pessoa['sexo'] not in ["M", "F"]:
    pessoa['sexo'] = input("Valor inválido! Digite M ou F: ").strip().upper()
```
Aqui usamos not in porque estamos tratando erro.
"""