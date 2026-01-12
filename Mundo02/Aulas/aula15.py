"""
Laços de Repetição: interrupçao

while True:
    if path:
        walk()
    elif noPath:
        jump()
    elif coin:
        pick up()
    if tropheu:
        jump()
        break
        
cont = 1
while cont <= 10:
    print(cont ,'..', end='')
    cont += 1
    if cont == 7:
        print(cont ,'..', end='')
        break
print("Acabou")  

while n != 999:
   s = s+n
   n = int(input("Digite um Numero: ")) 
print(f"a soma vale: {s}")
"""
n = s = 0

while True:
   n = int(input("Digite um Numero: "))
   if n == 999:
      break
   s += n
print(f"a soma vale: {s}")


