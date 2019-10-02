def bubble_sort(lista):
    
    for x in range(len(lista)-1):        
        y = x + 1
        while y < len(lista):            
            a = lista[x]
            b = lista[y]       
            if a > b:
                lista[x], lista[y] = lista[y], lista[x]
                x += 1            
                print(lista) 
            y += 1
    
    return lista
    
    
    
def test():
    #print(bubble_sort([5, 1, 4, 2]))
    #bubble_sort([5, 1, 4, 2])
    bubble_sort([1, 5, 3, 4, 2, 0])
    
test()