def busca(seq, x):
    '''(list, float) -> boolean'''
    for i in range(len(seq)):
        if seq[i] == x:
            return i
    return False
    
def teste():
    numeros = [0,1,2,3,4,5,6,7,8,9,10]
    x = 2
    print(busca(numeros, x))

teste()
