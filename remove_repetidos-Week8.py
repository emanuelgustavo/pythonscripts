def remove_repetidos(lista):
    listaSemRepetidos = []
    for e in lista:
        if e not in listaSemRepetidos:
            listaSemRepetidos.append(e)
    return sorted(listaSemRepetidos)


lista = [2, 4, 2, 2, 3, 3, 1]
print(remove_repetidos(lista))