print("=" * 30)
print("     10 TERMOS DE UMA P.A      ")
print("=" * 30)

first = int(input("Primeiro Termo: "))
num = int(input("Razão: "))
terms = 10

def whileTest(terms,first,num):

    while terms != 0:
        print(first, end=" → ")
        first += num
        terms -= 1
        print(terms)
        if terms == 0:
            terms += int(input(""))

whileTest(terms, first, num)