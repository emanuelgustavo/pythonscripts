def soma_elementos(lista):
    soma = 0
    for e in lista:
        soma += e
    return soma

print(soma_elementos([1, 2, 3, 3, 3, 4]))