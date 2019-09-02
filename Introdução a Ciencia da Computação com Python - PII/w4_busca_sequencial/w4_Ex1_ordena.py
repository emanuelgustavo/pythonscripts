import functools

def ordenada(lista):

    ordenado = True
    lista_ordenada = lista
    fim = len(lista_ordenada)        
    for i in range(fim -1):
        #Inicialmente, o meno elemento já visto é o i-ésimo
        posicao_do_minimo = i            
        for j in range(i+1, fim):
            if lista_ordenada[j] < lista_ordenada[posicao_do_minimo]:
                posicao_do_minimo = j
                ordenado = False
        #Coloca o menor elemento encontrado no inicio da sub-lista
        #Para isso, troca de lugar os elementos nas posições i e posicao_do_minimo
        lista_ordenada[i], lista_ordenada[posicao_do_minimo] = lista_ordenada[posicao_do_minimo], lista_ordenada[i]

    return ordenado

def main():
    lista1 = [1,2,3,4,5,6,7,8,9,10]
    lista2 = [2,5,8,9,7,4,6,1,3,10]

    print(ordenada(lista1))
    print(ordenada(lista2))

main()
