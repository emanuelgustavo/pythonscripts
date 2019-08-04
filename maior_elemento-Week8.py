def maior_elemento(lista):
    tamLista = len(lista)
    a = lista[0]        
    for e in lista:
        if a < e:
            a = e
    return a

print(maior_elemento([5,6,7,9,10,2,4,5,15]))