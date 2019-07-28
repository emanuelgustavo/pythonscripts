palavra = str(input("Digite uma palavra: "))

x = 0
troca = ""

while x < len(palavra):
    if palavra[x] in "aeiou":
        troca += "*"
    else:
        troca += palavra[x]
    x += 1

print(troca)
