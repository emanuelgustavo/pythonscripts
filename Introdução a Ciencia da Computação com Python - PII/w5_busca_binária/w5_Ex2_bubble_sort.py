def bubble_sort(lista):
    fim = len(lista)
    first = True
    for i in range(fim-1, 0, -1):
        if first:
            print(lista)
            first = False
        for j in range(i):
            a = lista[j]
            b = lista[j+1]
            if a > b:
                lista[j] = b
                lista[j+1] = a
                print(lista) 
    print(lista)                 
    return lista
'''
def test():
    bubble_sort([5, 1, 3, 4, 2, 0])

test()
'''