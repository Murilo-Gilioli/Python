# INTERACTIVE HELP
print(input.__doc__)
help(input)

# DOCSTRINGS
def contador(i,f,p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: INICIO DA CONTAGEM.
    :param f: FINAL DA CONTAGEM.
    :param p: PASSO DA CONTAGEM.
    :return: SEM RETORNO.
    """
    c = i
    while c <= f:
        print(f"{c}", end="..")
        c += p
    print("Fim!")

contador(2,10,2)
help(contador)

# PARAMETROS OPCIONAIS
def somar(a = 0,b = 0,c = 0):
    soma = a + b + c
    print(f"a Soma vale {soma}") 

somar(3,2,5)
somar(8,4)

# ESCOPO DE VARIAVEIS
def teste():
    # MODIFICA A VAR GLOBAL 'N' MSM DENTRO DA FUNÇÃO 
    global n
    n = 5
    x = 8
    print(f"na Função teste, n vale {n}")
    print(f"Na função teste, x vale {x}")

n = 2
print(n)
teste()

# RETORNANDO VALORES

def somar2(a = 0,b = 0,c = 0):
    soma = a + b + c
    return soma

val1 = somar2(3,2,5)
val2 = somar2(8,4)

print(val1, val2)