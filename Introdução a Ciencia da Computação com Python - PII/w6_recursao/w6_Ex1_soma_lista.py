def soma_lista(lista):
    if len(lista) == 1:
        return lista[0]
    #print(lista)
    return lista[len(lista)-1] + soma_lista(lista[:len(lista)-1])
'''
def teste():
    lista = [x*x for x in range(11)]
    print(soma_lista(lista))
    
teste()
'''
