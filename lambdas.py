import random

def is_odd(n):
    return True if n % 2 == 0 else False

numeros = []
pares = []

for i in range (11):
    numeros.append(random.randint(0, 100))

for i in numeros:
    if is_odd(i):
        pares.append(i)

pares_lambda = filter(lambda numero: numero % 2 == 0, numeros)

print(numeros)
print(pares)
for par in pares_lambda:
    print(par, end=' ')


mpf = lambda: print("Minha primeira função!")

mpf()

num_1 = 5
num_2 = 12
soma = lambda num_1, num_2: num_1 + num_2
soma(num_1, num_2)

idade = int(input('Digite a idade: '))
nome = input('Digite o nome: ')

usuario = lambda nome, idade: print('{} possui {} anos.'.format(nome, idade))

usuario(nome, idade)

