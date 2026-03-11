def fatorial(num = 1):
    f = 1
    for c in range(num,0,-1):
        f = f * c
    return f

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()

print(f"Os resultados sao {f1} - {f2} - {f3}")

def parOuImpar(n=0):
    if n % 2 == 0:
        return True
    else:
        return False
    
num = int(input("Digite um Numero: "))
if parOuImpar(num):
    print("Par")
else:
    print("Impar")