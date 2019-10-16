class Encontra_impares:

    def encontra_impares(self, lista, lista2=[]):
        if len(lista) <= 1:
            if lista[0] % 2 != 0:
                lista2.extend(lista)
                return lista2
            else:
                return lista2    
        else:
            if lista[len(lista)-1] % 2 != 0:
                lista2.append(lista[len(lista)-1])
                return encontra_impares(lista[:len(lista)-1], lista2)
            else:
                return encontra_impares(lista[:len(lista)-1], lista2)
            

def teste():
    impares = Encontra_impares()
    #lista = [x*x for x in range(1,6)]
    #print(impares.encontra_impares(lista))
    lista = [2]
    print(impares.encontra_impares(lista))
        
teste()
