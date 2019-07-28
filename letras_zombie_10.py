letras = []

x = 1
vogais = 0
consoantes = 0

while x <= 10:
    n = str(input("Digite uma letra: "))
    letras.append(n)
    if n in "aeiou":
        vogais += 1
    else:
        consoantes += 1
    x += 1

print(letras)
print("%d sao vogais e %d sao consoantes." %(vogais, consoantes))
