import random

numeros = []

n = int(input("Digite a quantidade de numeros: "))

for i in range(n):
    numeros.append(random.randint(1, 1000))

print(numeros)
