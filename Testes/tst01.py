def testsForTriangle(c1, c2, c3):
    firstTest = c1 + c2 > c3
    secondTest = c2 + c3 > c1
    thirdTest = c1 + c3 > c2

    if firstTest and secondTest and thirdTest:
        return print("é um Triangulo")
    else:
        return print("nao é um Triangulo")
       

testsForTriangle(50,50,50)