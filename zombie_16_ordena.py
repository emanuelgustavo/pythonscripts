import random

numeros = []

for i in range(6):
    n = random.randint(1, 60)
    if n not in numeros:
        numeros.append(n)
    numeros.sort()

print(numeros)
