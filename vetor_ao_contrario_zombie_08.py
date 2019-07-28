numeros = []

x = 1

while x <= 10:
    numeros.append(int(input("Digite um numero: ")))
    print(numeros)
    x += 1
x = 9
while x >= 0:
    print(numeros[x])
    x -= 1

