def bubble_sort(lista):
    houve_troca = True
    print(lista)
    while houve_troca:        
        houve_troca = False        
        for x in range(1, len(lista)):
            y = x - 1
            if lista[x] < lista[y]:
                lista[x], lista[y] = lista[y], lista[x]
                houve_troca = True
            if houve_troca:    
                print(lista)
    return lista
'''    
def test():
    #print(bubble_sort([5, 1, 4, 2]))
    #bubble_sort([5, 1, 4, 2])
    print(bubble_sort([1, 5, 3, 4, 2, 0]))
    
test()
'''