def busca(lista, elemento):
    primeiro = 0
    ultimo = len(lista)-1
    while primeiro <= ultimo:
        meio = (primeiro + ultimo) // 2
        print(meio)
        if lista[meio] == elemento:
            return meio
        else:
            if elemento < lista[meio]:
                ultimo = meio - 1
            else:
                primeiro = meio + 1
    return False
                
def test():
    print("teste 1: busca(['a', 'e', 'i'], 'e')")
    print(busca(['a', 'e', 'i'], 'e'))
    print("teste 2: busca([1, 2, 3, 4, 5], 6)")
    print(busca([1, 2, 3, 4, 5], 6))
    print("teste 3: busca([1, 2, 3, 4, 5, 6], 4)")
    print(busca([1, 2, 3, 4, 5, 6], 4))
    
test()
    
    