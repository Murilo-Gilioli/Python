# MANIPULANDO CADEIAS DE TEXTO
frase = "Curso em Video Python"

# FATIAMENTO - [começa : termina : pular]
print(frase[9])
print(frase[9:14])
print(frase[9:21:2])
print(frase[:5])
print(frase[15:])
print(frase[9::3])

# ANÁLISE - len(length).
print(len(frase))

# count('') - Mostra quantas vezes o caractere se repete.
print(frase.count('o', 0 , 13))

# find('') - Mostra de qual posiçao a frase que vc digitou começou.
print(frase.find('deo'))

# in - verifica se a string existe dentro da variavel.
print("Curso" in frase)

# TRANSFORMAÇÃO - replace("Str1", "Str2") - Substitui a String "1" pela "2".
print(frase.replace("Video", "Foda"))

# Upper() - Deixa a String em letras MAIUSCULAS.
print(frase.upper())

# Lower() - Deixa a String em letras minusculas.
print(frase.lower())

# Capitalize() - Deixa com a Primeira Letra Maiuscula e o Resto em minusculo.
print(frase.capitalize())

# Title() - Deixa Todas as Primeiras Letras Maiusculas e o Resto minusculo.
print(frase.title())

# Strip() - Remove os Espaços Inuteis (do começo e do final da String);
# Há Tambem o  lstrip() e o rstrip(), que remove só da Esquerda ou Direita;
frase2 = "  Aprenda Python  "
print(frase2.strip())

# DIVISAO - Split() - Remove os Espaços e Cria uma "String Nova" com Cada Palavra entre Elas, Montando um Array de Palavras com a Frase Antiga;
print(frase.split())

# JUNÇÃO - "char".join(var) - ele Cria uma String Unica Novamente, Juntando cada Palavra Separada de um Array e separando elas com o Character que vc desejar
frase3 = ["Curso", "em", "Video", "Python"]
print(" ".join(frase3))